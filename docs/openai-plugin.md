# OpenAI skills-only plugin package

The OpenAI package contains the canonical Goal Instruction Writer skill, its
four references, UI metadata, license, and icons. Runtime instructions remain
the v0.2.5 contract. Packaging source is in `packaging/openai/`.

Package preparation, an uploaded draft, review, and public directory publication
are separate states. The package and its public download do not establish an
approved OpenAI directory listing.

## Build

From a Git checkout with Python 3.9 or later:

```bash
python3 scripts/build_openai_plugin.py
```

The builder writes `dist/goal-instruction-writer-openai-0.2.5.zip` and a validation
report. Runtime files and icons come from committed `HEAD`. Use `--source-ref`
to select another commit. Packaging metadata and the privacy statement come
from the current checkout; their hashes are recorded separately in `SOURCE.json`.

The archive uses the portable root `plugin.json` plus a generated Codex
compatibility manifest. One `skills/goal-instruction-writer/` directory contains
the seven canonical runtime files. Fixed ZIP timestamps and sorted paths make
builds repeatable for the same inputs.

The builder checks listing limits, icons, bundled links, the source snapshot,
and archive integrity. These are package checks; they do not certify installed
model behavior or public directory approval.

The initial package was also checked against the official Agent Plugins JSON
Schema. Codex CLI 0.159.2 recognized it as an available v0.2.4 plugin through a
temporary local marketplace, and the Skills CLI found exactly one skill in the
extracted archive. The extracted skill passed `quick_validate.py`. Identical
inputs produced identical ZIP bytes. An installed fresh-chat behavior evaluation
has not been run for this plugin package.

## Try the skill

The [package README](../packaging/openai/README.md) contains three English prompts
for Preview, Draft, and Audit. Check that Preview preserves its confirmation
handoff, Draft contains observable criteria and explicit stop states, and Audit
identifies unbounded work and unnecessary repeated checks. A one-shot factual
question should not need this skill. A wait checkpoint needs a host-provided
future invocation; live wait/resume remains untested.

## Official upload

Upload the ZIP through the [OpenAI Plugins portal](https://platform.openai.com/plugins).
Resolve metadata and skill findings before review. Publisher verification and
submission permissions are account requirements. Review and publish only after
checking the final listing and required attestations.

The [privacy statement](privacy.md) describes the instruction package's data
handling. The developer display name in the public directory is controlled by
the verified publisher identity selected in the portal.

Official references: [package format](https://developers.openai.com/plugins/build/plugins),
[submission flow](https://developers.openai.com/plugins/deploy/submission), and
[plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines).
