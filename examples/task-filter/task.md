# The feature request

Use Goal Instruction Writer to draft an execution contract for this small task.

Add `--status open|done|all` to the read-only Tasklist CLI.

- Omitting the flag must keep the current output byte-for-byte identical.
- `open` and `done` must select the corresponding tasks in original file order.
- `all` must match the original behavior.
- Invalid values must produce argparse's error response and a nonzero exit.
- An empty selection must succeed with no output.
- Listing must leave the input JSON file unchanged.
- Preserve the JSON schema, formatting, existing tests, and default file path.
- Add focused status-filter coverage and document the new flag.

During implementation use focused checks for the feature. Complete the required
full regression suite once the implementation is stable. Record real commands,
results, relevant file identities, and the next action. Reuse still-valid runtime
evidence after report-only edits. No timing improvement is assumed in advance.

Keep the task to at most four actionable iterations and 20 minutes. Stop after
two equivalent attempts add no acceptance progress or new relevant evidence.
Do not add, publish, or deploy unrelated features. If a required criterion cannot
be verified within those bounds, preserve the gap and report the appropriate
terminal state instead of claiming completion.
