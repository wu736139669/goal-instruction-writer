# Goal Instruction Examples

These examples show the shape of the output. They are deliberately small so
they can be adapted to a real task.

## Coding: fix a reproducible import failure

Weak request:

> Fix the importer and keep trying until it works.

Better Goal:

```markdown
# Goal: Make the CSV importer accept quoted multiline fields

## Objective
Update the importer so the fixture `fixtures/quoted_multiline.csv` loads into
the existing record model without truncation or row-count drift.

## Baseline and scope
- Baseline: current `main` revision and the existing importer test suite.
- Allowed scope: importer code, its focused tests, and fixture data needed to
  reproduce the failure.
- Frozen scope: public record fields, unrelated parsers, and dependencies.

## Acceptance criteria
- [ ] The focused fixture test passes and preserves the expected row count.
- [ ] Existing importer tests pass.
- [ ] The diff explains the parsing boundary and contains no unrelated edits.

## Execution loop
Inspect the failing fixture and parser state; make one smallest hypothesis-driven
change; run the focused test; record the result and diff; then choose the next
unmet criterion from the evidence.

## Limits and no-op rule
Use at most four hypothesis iterations. Do not repeat a failed parser change
without new evidence; after two equivalent failures, report the blocker.

## Termination
Emit `GOAL COMPLETE` only when all three criteria are verified. Emit
`GOAL BLOCKED: <reason>` if the fixture or required dependency is unavailable,
including the exact unblock needed. Emit `GOAL TIMEBOXED: <state>` after the
fourth iteration if the criteria remain open.

## Reporting
Return the revision, commands and results, changed files, remaining gap, and
the terminal label.
```

## Research: compare two options

Weak request:

> Research these tools and tell me which one is best.

Better Goal:

```markdown
# Goal: Recommend one analytics tool for the stated workload

## Objective
Produce a cited comparison of Tool A and Tool B and recommend one option for a
team with <constraints>, with the trade-offs explicit enough for a decision.

## Baseline and scope
- Baseline: official documentation and current pricing pages checked on the
  research date.
- Allowed scope: public, first-party sources plus the user's stated workload.
- Frozen scope: do not infer private capabilities or promise an unverified
  integration.

## Acceptance criteria
- [ ] Each decision criterion has a source and a short evidence quote or
  paraphrase.
- [ ] Material differences, costs, and constraints are compared in one table.
- [ ] The recommendation states when the other option would be better.

## Execution loop
Inspect one criterion at a time; collect the strongest primary source for each
tool; record evidence and uncertainty; update the comparison; then select the
next criterion that could change the recommendation.

## Limits and no-op rule
Cover the five agreed criteria and stop after one primary source per material
claim unless a conflict needs resolution. Do not keep searching after the
recommendation is stable and all criteria are sourced.

## Termination
Emit `GOAL COMPLETE` when the table, citations, and conditional recommendation
are complete. Emit `GOAL BLOCKED: <missing constraint or source>` when a decision
depends on an owner answer or inaccessible evidence.

## Reporting
Return the comparison, recommendation, uncertainty, sources, and terminal
label.
```

## Chinese output shape

When the user asks in Chinese, keep the same contract and translate the labels
or preserve exact terminal strings when a system already depends on them. For
example:

```markdown
目标：交付一个可验收的 <结果>
循环：检查 → 选择一个最小工作单元 → 执行 → 验证 → 记录游标
结束：`GOAL COMPLETE` / `GOAL BLOCKED: <原因>` / `GOAL TIMEBOXED: <状态>`
```
