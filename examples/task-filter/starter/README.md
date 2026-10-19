# Tasklist starter

A deliberately small, read-only Python CLI. The starting version lists every
task; the exercise is to add a status filter while preserving existing output.

Requires Python 3.9 or later. No third-party packages are needed.

```sh
python3 tasklist.py tasks.json
python3 -m unittest discover -s tests -v
```

Task files contain a JSON list of objects with integer `id`, non-empty `title`,
and boolean `done` fields. Listing preserves file order and never saves changes.
