#!/usr/bin/env python3
"""Build a minimal OpenAI plugin from a committed skill revision, using stdlib."""

import argparse
import hashlib
import json
import posixpath
import re
import struct
import subprocess
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
NAME = "goal-instruction-writer"
REPOSITORY = f"https://github.com/wu736139669/{NAME}"
RUNTIME = (
    "SKILL.md", "LICENSE", "agents/openai.yaml",
    "references/goal-contract.md", "references/drift-control.md",
    "references/examples.md", "references/loop-preview.md",
)


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args])


def digest(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(manifest, files):
    require(manifest["name"] == NAME, "Unexpected plugin identity")
    require(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"]), "Use a semantic version")
    require(manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "Unexpected schema")
    require(bool(manifest["author"]["name"].strip()), "Publisher name is required")
    interface = manifest["extensions"]["com.openai"]["interface"]
    for field, limit in (("displayName", 30), ("shortDescription", 30),
                         ("longDescription", 4000), ("developerName", 80)):
        value = interface[field]
        require(isinstance(value, str) and 0 < len(value.strip()) <= limit, f"Invalid {field}")
        require(not re.search(r"[\u3400-\u4dbf\u4e00-\u9fff]", value), f"Listing must be English: {field}")
    prompts = interface["defaultPrompt"]
    require(1 <= len(prompts) <= 3 and len(set(prompts)) == len(prompts), "Use up to three distinct prompts")
    require(all(0 < len(p) <= 128 and "@" not in p for p in prompts), "Invalid starter prompt")
    for field in ("websiteURL", "supportURL", "privacyPolicyURL"):
        url = urlsplit(interface[field])
        require(url.scheme == "https" and url.netloc and not url.username, f"Invalid {field}")
    for field in ("composerIcon", "logo"):
        path = interface[field]
        require(path.startswith("./") and path[2:] in files, f"Missing asset: {path}")
        data = files[path[2:]]
        require(data[:8] == b"\x89PNG\r\n\x1a\n" and len(data) <= 5 * 1024 * 1024, "Invalid PNG")
        width, height = struct.unpack(">II", data[16:24])
        require(width == height and 48 <= width <= 4096, "Icon must be square and 48–4096 px")
    for path, data in files.items():
        require(not path.startswith("/") and ".." not in PurePosixPath(path).parts, "Unsafe archive path")
        if not path.endswith(".md"):
            continue
        text = data.decode()
        for target in re.findall(r"\]\(([^\s)]+)\)", text):
            url = urlsplit(target)
            if url.scheme or not url.path:
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(path), url.path))
            require(resolved in files, f"Unresolved link in {path}: {target}")
    skill = files[f"skills/{NAME}/SKILL.md"].decode()
    require(skill.startswith("---\n") and f"name: {NAME}\n" in skill, "Invalid skill frontmatter")
    require(re.search(r"(?m)^description: .+", skill), "Missing skill description")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-ref", default="HEAD", help="Committed Git revision supplying the runtime")
    parser.add_argument("--output", type=Path, help="Output ZIP; defaults to dist/<name>-openai-<version>.zip")
    args = parser.parse_args()
    revision = git("rev-parse", "--verify", "--end-of-options", args.source_ref + "^{commit}").decode().strip()
    packaging = ROOT / "packaging/openai"
    manifest = json.loads((packaging / "plugin.json").read_text())
    files = {f"skills/{NAME}/{path}": git("show", f"{revision}:{path}") for path in RUNTIME}
    files.update({
        "plugin.json": json_bytes(manifest),
        "README.md": (packaging / "README.md").read_bytes(),
        "PRIVACY.md": (ROOT / "docs/privacy.md").read_bytes(),
        "LICENSE": git("show", f"{revision}:LICENSE"),
        "assets/logo.png": git("show", f"{revision}:assets/launch-logo.png"),
        "assets/icon.png": git("show", f"{revision}:assets/launch-logo-240.png"),
    })
    validate(manifest, files)
    # The portable manifest is canonical. This derived overlay supports older clients.
    compatibility = {key: manifest[key] for key in
                     ("name", "version", "description", "author", "homepage", "repository", "license", "keywords")}
    compatibility["skills"] = "./skills/"
    compatibility["interface"] = manifest["extensions"]["com.openai"]["interface"]
    compatibility["extensions"] = {"com.openai": {
        "publication": manifest["extensions"]["com.openai"]["publication"]
    }}
    files[".codex-plugin/plugin.json"] = json_bytes(compatibility)
    source = {
        "repository": REPOSITORY,
        "skillRevision": revision,
        "runtimeFiles": {path: digest(files[f"skills/{NAME}/{path}"]) for path in RUNTIME},
        "packagedFiles": {path: digest(data) for path, data in sorted(files.items())},
        "packagingInputs": {
            path: digest((ROOT / path).read_bytes()) for path in
            ("packaging/openai/plugin.json", "packaging/openai/README.md", "docs/privacy.md", "scripts/build_openai_plugin.py")
        },
    }
    files["SOURCE.json"] = json_bytes(source)
    output = (args.output or ROOT / f"dist/{NAME}-openai-{manifest['version']}.zip").resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for path, data in sorted(files.items()):
            info = ZipInfo(path, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data, compresslevel=9)
    with ZipFile(output) as archive:
        require(archive.testzip() is None, "Archive integrity failed")
        require(set(archive.namelist()) == set(files), "Unexpected archive contents")
        require(all(archive.read(p) == b for p, b in files.items()), "Archive round-trip mismatch")
    report = {
        "archive": output.name, "version": manifest["version"], "skillRevision": revision,
        "sizeBytes": output.stat().st_size, "sha256": digest(output.read_bytes()),
        "fileCount": len(files), "runtimeFileCount": len(RUNTIME),
        "checks": ["listing field limits", "packaged icons", "relative Markdown links",
                   "skill frontmatter", "committed runtime snapshot", "archive contents and integrity"],
    }
    output.with_suffix(".validation.json").write_bytes(json_bytes(report))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
