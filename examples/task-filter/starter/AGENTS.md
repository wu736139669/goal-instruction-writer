# Recorded task fixture

Use English for all output and documentation.

This is an isolated, maintainer-operated example, not an external user trial.
Use only the pinned local `goal-instruction-writer` skill when asked to draft
the Goal. Do not invoke subagents, parallel agents, native durable-Goal tools,
network services, package installation, commits, or pushes.

The feature scope is `tasklist.py`, `README.md`, and a new
`tests/test_status.py`. Existing tests and `tasks.json` are frozen. `GOAL.md`
and `PROGRESS.md` may record the instruction contract and concise evidence.
The skill copy, this file, and other files are frozen during execution.

Use a focused status-filter test during edits. Run the existing full test suite
at the final delivery gate. Reuse valid results after report-only changes.
Do not add artificial delays, benchmarks, dependencies, or unrelated features.

Stop when the requested behavior and delivery evidence are complete. Report
the commands actually run and their results; do not claim evidence from an
unexecuted command.
