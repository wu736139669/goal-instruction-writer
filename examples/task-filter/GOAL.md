# Goal: Add a read-only Tasklist status filter

## Objective

Deliver `--status open|done|all` in `tasklist.py`, with focused tests and documentation, while preserving the existing default output, input files, and CLI behavior covered by the frozen regression tests.

## Goal anchor

- Outcome: the status filter satisfies C1–C8 with valid evidence and no changes outside the allowed scope.
- Criteria: C1–C8 below are fixed; difficulty does not permit weakening them.
- Frozen boundary: existing tests, `tasks.json`, JSON schema and formatting, default file path, the pinned skill and its references, `AGENTS.md`, `TASK.md`, and all files outside the allowed scope.
- Current phase: instruction drafted; implementation and verification have not started. The host supplies execution separately. This artifact does not invoke a native durable Goal or authorize implementation during the drafting phase.

## Baseline and scope

- Authority: follow `AGENTS.md`, `TASK.md`, and this contract. Work in English. This is an isolated, maintainer-operated example, with no external trial or feedback requirement.
- Baseline: the workspace at the start of execution is authoritative. Before editing, inspect the current source, README, and frozen tests; record any existing changes, the available revision identity, Python version, and SHA-256 identities of relevant files. Do not overwrite unrelated existing changes.
- Capture the pre-change CLI's exit code, stdout bytes, and stderr bytes on a temporary mixed-status fixture with nonsequential IDs. Keep its contents and output in the evidence record for comparison after edits. Do not modify `tasks.json` to create fixtures.
- Feature edits are limited to `tasklist.py`, `README.md`, and a new `tests/test_status.py`. `GOAL.md` and `PROGRESS.md` may hold only the instruction contract and concise execution evidence; do not silently revise the anchor or acceptance criteria.
- Preserve the JSON schema and validation, task-line formatting, file order, and default relative path `tasks.json`. Listing must remain read-only.
- Use the existing Python standard library and local tools. Disposable test fixtures may use temporary directories; do not leave extra project files or bytecode artifacts.
- Do not use subagents, parallel agents, native durable-Goal tools, network services, package installation, commits, or pushes. Do not add artificial delays, benchmarks, dependencies, or unrelated features; do not publish or deploy anything.

## Acceptance criteria

- [ ] **C1 — Default compatibility:** omitting `--status` produces byte-for-byte identical stdout to the pre-change CLI for the same valid input, with the same successful exit and stderr. Preserve the default `tasks.json` path. Evidence: captured baseline comparison, focused assertions, and frozen listing tests.
- [ ] **C2 — Open selection:** `--status open` lists exactly tasks whose boolean `done` value is `false`, in their original file order, using unchanged line formatting. Evidence: a focused CLI test with mixed statuses and nonsequential IDs.
- [ ] **C3 — Done selection:** `--status done` lists exactly tasks whose boolean `done` value is `true`, in their original file order, using unchanged line formatting. Evidence: the corresponding focused CLI test.
- [ ] **C4 — Explicit all:** `--status all` matches the original unfiltered behavior byte-for-byte. Evidence: focused comparisons against both the captured baseline and omitted-flag output.
- [ ] **C5 — Invalid values:** an invalid status produces argparse's error response on stderr and a nonzero exit, with no task listing. Evidence: a focused subprocess test plus inspection that argparse choices enforce the three allowed values.
- [ ] **C6 — Empty selection:** selecting a status with no matching tasks succeeds with zero stdout bytes. Evidence: focused tests for no open matches, no done matches, and an empty input list.
- [ ] **C7 — Preservation:** listing with the flag omitted and with each valid value leaves input JSON bytes unchanged; JSON schema/validation, input formatting, existing tests, and other frozen files remain unchanged. Evidence: before/after fixture bytes, frozen-file identities and scope diff, source review, and the required full regression suite.
- [ ] **C8 — Delivery:** `tests/test_status.py` covers the behavioral requirements in C1–C7 without changing existing tests; `README.md` explains all choices, the default, and usage. The required full suite passes against the delivered implementation. `PROGRESS.md` and the final response identify actual commands, results, evidence identities, remaining gaps, and the next action or terminal state.

## Verification strategy

- During edits, use the focused command `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -p 'test_status.py' -v`. Inspect affected code and assertions as needed; do not run the full suite on every edit.
- At the final delivery gate, once the implementation and tests are stable, run `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v`. This must include all unchanged existing tests and the new focused tests. Review the final diff for scope, README accuracy, and frozen-file preservation.
- Bound each test invocation to 60 seconds or the remaining overall time, whichever is shorter, using host timeout support or the Python standard library. A timeout or incomplete command leaves its associated criterion unverified. Do not install a timeout tool.
- Associate each result with the checked source/test hashes, fixture contents or hashes, frozen-file identities, Python version, relevant environment, exact command, exit status, and meaningful output summary. Record the baseline comparison itself, not merely an assertion that compatibility was checked.
- Reuse valid results while their source, tests, inputs, dependencies, and relevant environment remain unchanged. Mark evidence as newly run or reused. README, GOAL, or PROGRESS report-only edits do not invalidate unrelated runtime results; review any changed documentation separately.
- Before rerunning a check, record the concrete invalidating change, failure, or unresolved concern. Rerun affected checks, including checks that consume a changed artifact. Repeat the full suite only if a relevant change or unresolved failure invalidates the delivery result. No redundant final rerun is required after report-only edits.
- No speed improvement is assumed or required. Report only executed commands and observed outcomes. A proposed command, code review, or test added without execution is not passing runtime evidence.

## Execution loop

Use at most four actionable iterations, adapting each to the current evidence rather than following a fixed script:

1. Inspect the workspace and last `PROGRESS.md` cursor; check elapsed time and iteration budget. On the first iteration, establish the baseline before edits.
2. Select the smallest work unit for an unmet criterion. Before acting, record its criterion ID, expected observable delta, and reason it is within scope. The first unit should add focused status coverage and the minimal argparse/filter implementation using the existing loader and formatter.
3. Make only the authorized changes needed for that unit. Use subsequent iterations for evidence-driven repairs, documentation, or the final delivery gate. Reserve enough of the four-iteration and 20-minute budgets for the required full suite and reporting; verification and repair are not exempt from these limits.
4. Run the applicable focused checks; run the full suite only at the stable delivery gate or for a justified invalidated result. Capture actual evidence and update each affected criterion as open or verified.
5. Classify the result as `ON_TARGET` if a criterion advances or new relevant evidence supports a justified next action; `SIDE_QUEST` if useful but unnecessary; or `DRIFTED` if the anchor/scope is violated or the no-progress threshold is reached.
6. Record the change, evidence, remaining gap, decision, elapsed time, iteration count, consecutive equivalent no-progress attempts, and one next action in `PROGRESS.md`. Check termination before starting another iteration.

An actionable iteration is one selected work unit through verification and checkpointing, including a verification-only delivery unit. Do not evade the limit by renaming retries or splitting one attempt into uncounted substeps.

## Drift control

- Re-read the anchor after iteration 3, at the implementation-to-delivery milestone, and before any action that could exceed authority. Compare open/verified criteria, changed files, evidence validity, and remaining budget.
- Park side quests as a brief deferred note; do not implement them.
- Stop the current loop after any unauthorized scope/anchor change or two equivalent actionable attempts that add neither acceptance progress nor new relevant evidence. Emit `GOAL REALIGNMENT REQUIRED`, preserving the gap and cursor.
- Resume a realigned loop only with a recorded next action tied to the unchanged anchor and within the original remaining limits. Changes to scope, criteria, or exhausted limits require explicit owner authorization.

## Limits and no-op rule

- Execution ends no later than four actionable iterations or 20 minutes of wall-clock time from the first execution inspection, whichever comes first. Drafting time is outside the execution timebox. Host limits still apply.
- Do not repeat an action without new information. After an unproductive attempt, change the hypothesis based on relevant evidence or stop with the appropriate state. The second equivalent no-progress attempt triggers realignment; do not make a third.
- Stop immediately when all criteria and delivery evidence are complete. Further checking requires a concrete unresolved concern or invalidated evidence.

## Termination

Use one exact terminal label with a reason where indicated:

- `GOAL COMPLETE`: C1–C8 all have valid evidence and the scoped files and delivery report are available. Stop.
- `GOAL BLOCKED: <reason>`: a named dependency, missing authority, or unresolved failure prevents the next meaningful action. State the exact unblock needed and preserve unverified criteria.
- `GOAL PAUSED: <reason>`: the owner explicitly requests a pause. Preserve the cursor and resume only when authorized.
- `GOAL TIMEBOXED: <state>`: the iteration or time limit is reached before completion. Report verified progress, unverified criteria, and the safest next action; do not keep working or claim completion.
- `GOAL STOPPED: <reason>`: the owner cancels or the next action would exceed granted authority. Preserve evidence and stop.
- `GOAL REALIGNMENT REQUIRED`: the drift or equivalent-no-progress rule fires. Preserve the last justified cursor and the realignment needed; do not continue the current loop.

Never claim success from effort, an unexecuted command, or a partially verified criterion. If a required check cannot finish within the limits, retain the gap and choose the applicable non-complete state.

## Reporting

Keep `PROGRESS.md` concise: baseline identities, per-iteration target/delta/scope reason, actual commands and results, newly run versus reused evidence, criterion status, decisions, remaining limits, and next cursor. On termination, give the terminal label, changed files, commands actually run with their results, evidence reuse, remaining gaps, and the next action or precise unblock. For `GOAL COMPLETE`, the next action is none; the authorized work is finished.
