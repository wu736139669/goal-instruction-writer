import json
import tempfile
import unittest
from pathlib import Path

from tasklist import load_tasks


class StorageTests(unittest.TestCase):
    def check_invalid(self, value, message):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "tasks.json"
            path.write_text(json.dumps(value), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, message):
                load_tasks(path)

    def test_top_level_must_be_a_list(self):
        self.check_invalid({}, "JSON list")

    def test_tasks_must_be_objects(self):
        self.check_invalid(["task"], "object")

    def test_duplicate_ids_are_rejected(self):
        self.check_invalid([
            {"id": 1, "title": "First", "done": False},
            {"id": 1, "title": "Second", "done": True},
        ], "unique integers")

    def test_blank_titles_are_rejected(self):
        self.check_invalid([{"id": 1, "title": " ", "done": False}], "non-empty title")

    def test_done_must_be_boolean(self):
        self.check_invalid([{"id": 1, "title": "First", "done": "yes"}], "boolean done")


if __name__ == "__main__":
    unittest.main()
