"""A small, read-only task-list CLI used in the recorded Goal example."""

import argparse
import json
import sys
from pathlib import Path


def load_tasks(path):
    tasks = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("task file must contain a JSON list")
    ids = set()
    for task in tasks:
        if not isinstance(task, dict):
            raise ValueError("each task must be an object")
        if type(task.get("id")) is not int or task["id"] in ids:
            raise ValueError("task IDs must be unique integers")
        if not isinstance(task.get("title"), str) or not task["title"].strip():
            raise ValueError("each task needs a non-empty title")
        if type(task.get("done")) is not bool:
            raise ValueError("each task needs a boolean done value")
        ids.add(task["id"])
    return tasks


def format_task(task):
    status = "done" if task["done"] else "open"
    return f'{task["id"]}: [{status}] {task["title"]}'


def main(argv=None):
    parser = argparse.ArgumentParser(description="List tasks without changing the file.")
    parser.add_argument("task_file", nargs="?", default="tasks.json")
    parser.add_argument(
        "--status", choices=("open", "done", "all"), default="all",
        help="show open, done, or all tasks (default: all)",
    )
    args = parser.parse_args(argv)
    try:
        tasks = load_tasks(args.task_file)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    for task in tasks:
        if args.status == "all" or task["done"] == (args.status == "done"):
            print(format_task(task))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
