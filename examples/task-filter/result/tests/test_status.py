import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIXED = (
    b'[\n'
    b'  {"id": 9, "title": "Caf\\u00e9 notes", "done": true},\n'
    b'  {"id": 2, "title": "Review", "done": false},\n'
    b'  {"id": 17, "title": "Ship", "done": true},\n'
    b'  {"id": 5, "title": "Verify", "done": false}\n'
    b']\n'
)
ALL_OUTPUT = (
    "9: [done] Café notes\n"
    "2: [open] Review\n"
    "17: [done] Ship\n"
    "5: [open] Verify\n"
).encode("utf-8")


class StatusTests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        self.directory = Path(directory.name)
        self.path = self.directory / "tasks.json"
        self.path.write_bytes(MIXED)

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "tasklist.py"), *map(str, args)],
            cwd=self.directory, capture_output=True, timeout=10,
        )

    def assert_success(self, result, expected):
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, expected)
        self.assertEqual(result.stderr, b"")

    def test_omitted_status_preserves_original_output_bytes(self):
        self.assert_success(self.run_cli(self.path), ALL_OUTPUT)

    def test_open_preserves_order_and_format(self):
        self.assert_success(
            self.run_cli(self.path, "--status", "open"),
            b"2: [open] Review\n5: [open] Verify\n",
        )

    def test_done_preserves_order_and_format(self):
        self.assert_success(
            self.run_cli(self.path, "--status", "done"),
            "9: [done] Café notes\n17: [done] Ship\n".encode("utf-8"),
        )

    def test_all_matches_original_and_omitted_status(self):
        omitted = self.run_cli(self.path)
        explicit = self.run_cli(self.path, "--status", "all")
        self.assert_success(explicit, ALL_OUTPUT)
        self.assertEqual(
            (explicit.returncode, explicit.stdout, explicit.stderr),
            (omitted.returncode, omitted.stdout, omitted.stderr),
        )

    def test_invalid_status_uses_argparse_error_without_listing(self):
        result = self.run_cli(self.path, "--status", "pending")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, b"")
        self.assertIn(b"usage:", result.stderr)
        self.assertIn(b"argument --status: invalid choice: 'pending'", result.stderr)
        self.assertEqual(self.path.read_bytes(), MIXED)

    def test_no_matching_status_succeeds_without_output(self):
        for status, done in (("open", b"true"), ("done", b"false")):
            with self.subTest(status=status):
                fixture = b'[{"id": 9, "title": "Only task", "done": ' + done + b'}]\n'
                self.path.write_bytes(fixture)
                self.assert_success(self.run_cli(self.path, "--status", status), b"")
                self.assertEqual(self.path.read_bytes(), fixture)

    def test_empty_list_succeeds_for_every_status(self):
        self.path.write_bytes(b"[]\n")
        for args in ((), ("--status", "open"), ("--status", "done"), ("--status", "all")):
            with self.subTest(args=args):
                self.assert_success(self.run_cli(self.path, *args), b"")
                self.assertEqual(self.path.read_bytes(), b"[]\n")

    def test_every_status_preserves_input_bytes(self):
        for args in ((), ("--status", "open"), ("--status", "done"), ("--status", "all")):
            with self.subTest(args=args):
                result = self.run_cli(self.path, *args)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, b"")
                self.assertEqual(self.path.read_bytes(), MIXED)

    def test_default_relative_path_works_for_every_status(self):
        for args, expected in (
            ((), ALL_OUTPUT),
            (("--status", "all"), ALL_OUTPUT),
            (("--status", "open"), b"2: [open] Review\n5: [open] Verify\n"),
            (("--status", "done"), "9: [done] Café notes\n17: [done] Ship\n".encode("utf-8")),
        ):
            with self.subTest(args=args):
                self.assert_success(self.run_cli(*args), expected)
                self.assertEqual(self.path.read_bytes(), MIXED)

    def test_filter_keeps_boolean_validation(self):
        fixture = b'[{"id": 9, "title": "Invalid", "done": "yes"}]\n'
        self.path.write_bytes(fixture)
        for status in ("open", "done", "all"):
            with self.subTest(status=status):
                result = self.run_cli(self.path, "--status", status)
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, b"")
                self.assertEqual(result.stderr, b"error: each task needs a boolean done value\n")
                self.assertEqual(self.path.read_bytes(), fixture)


if __name__ == "__main__":
    unittest.main()
