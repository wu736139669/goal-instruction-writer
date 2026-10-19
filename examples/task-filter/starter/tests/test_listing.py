import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ListingTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "tasklist.py"), *map(str, args)],
            cwd=ROOT, capture_output=True, text=True,
        )

    def test_default_lists_every_task_in_file_order(self):
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, (
            "1: [open] Review the release checklist\n"
            "2: [done] Write the migration note\n"
            "3: [open] Verify the delivery artifact\n"
            "4: [done] Record the previous checkpoint\n"
        ))

    def test_custom_file_and_nonsequential_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "custom.json"
            path.write_text(json.dumps([
                {"id": 9, "title": "Caf\u00e9 notes", "done": True},
                {"id": 2, "title": "Review", "done": False},
            ]), encoding="utf-8")
            result = self.run_cli(path)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "9: [done] Caf\u00e9 notes\n2: [open] Review\n")

    def test_empty_file_prints_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.json"
            path.write_text("[]\n", encoding="utf-8")
            result = self.run_cli(path)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")

    def test_listing_preserves_file_bytes(self):
        path = ROOT / "tasks.json"
        before = path.read_bytes()
        result = self.run_cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
