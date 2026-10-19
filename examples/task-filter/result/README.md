# Tasklist starter

A small, read-only Python CLI that lists tasks and filters by completion status.

Requires Python 3.9 or later. No third-party packages are needed.

```sh
python3 tasklist.py
python3 tasklist.py tasks.json
python3 tasklist.py tasks.json --status open
python3 tasklist.py tasks.json --status done
python3 tasklist.py tasks.json --status all
python3 -m unittest discover -s tests -v
```

The optional task file defaults to `tasks.json` in the current directory.
`--status` accepts:

- `open`: list tasks whose `done` field is `false`.
- `done`: list tasks whose `done` field is `true`.
- `all` (default): list every task, with the same output as omitting the flag.

Invalid status values produce an argparse error on stderr and a nonzero exit.
An empty selection succeeds without output.

Task files contain a JSON list of objects with integer `id`, non-empty `title`,
and boolean `done` fields. Listing preserves file order and never saves changes.
