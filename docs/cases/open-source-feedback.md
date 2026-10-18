# From a catalog submission to a maintained feedback loop

[Case library](README.md) · [Public discussion](https://github.com/wu736139669/goal-instruction-writer/discussions/1)

**Recorded through:** October 18, 2026. This case follows Goal Instruction
Writer's own release and contribution work, with public evidence links.

The task was to make a usable skill discoverable, obtain concrete feedback,
and carry justified improvements back into the canonical package. Packaging,
a submitted PR, a maintainer merge, and a user's installation are different
observable outcomes. The Goal needs to say which one is required.

## Two feedback paths that changed the instructions

| Date | Public event | Result |
| --- | --- | --- |
| Oct 11 | A reader proposed an [external-wait edge case](https://github.com/wu736139669/goal-instruction-writer/discussions/1#discussioncomment-18861864) | Concrete reading feedback identified ambiguity between waiting and failed actionable attempts |
| Oct 17 | [Agent Skill Exchange PR #119](https://github.com/agentskillexchange/skills/pull/119) was merged | A catalog maintainer reviewed the contribution and reported validation passed |
| Oct 17 | The maintainer contributed [a label clarification](https://github.com/agentskillexchange/skills/commit/94cd5ce20fe8ef49dd1de17946198d256fdef43f) | Drift realignment and an explicit owner pause received distinct labels |
| Oct 17 | Canonical [v0.2.3](https://github.com/wu736139669/goal-instruction-writer/releases/tag/v0.2.3) was published | The clarification was adopted into the upstream skill and references |
| Oct 18 | The author [answered the reader](https://github.com/wu736139669/goal-instruction-writer/discussions/1#discussioncomment-19016524) and published [v0.2.4](https://github.com/wu736139669/goal-instruction-writer/releases/tag/v0.2.4) | Scheduled waits, check triggers, deadline handling, and the no-progress rule were aligned |

This is a traceable contribution-and-maintenance result. The reader explicitly
described their comment as evaluation-reading feedback, rather than an
installation or execution test. The catalog maintainer's review establishes
that contribution's handling, not an independent long-running product benchmark.

## How the waiting branch becomes concrete

Suppose a required non-author response is pending and its feedback window is
still open. A useful cursor names the unmet criterion, last observation,
next agreed check time or relevant notification, and deadline.

Before that trigger, the agent can advance another criterion or yield with
the checkpoint preserved. A scheduled observation of "still pending" does
not become a failed implementation attempt. Actual queries and elapsed time
still consume the host's available budget. At the feedback deadline, an
unmet response criterion remains open and is reported as timeboxed.

That is an instruction branch, rather than a promise that the skill creates
a scheduler. The original [October 11 evaluation](../evaluations/2026-10-11-independent-goal-evaluation.md)
performed two bounded read-only iterations; it did not test a live waiting
period or automatic resumption.

## A reusable Goal contract

```markdown
Outcome: publish an installable skill, leave one contribution reviewable,
and capture the explicitly required amount of non-author feedback.
Authority: maintain this repository and its authorized submission; an external
maintainer owns the merge decision.
Loop: inspect the current evidence, choose one unmet criterion, make one
focused authorized change, verify it, and retain the next cursor.
Feedback: define what counts, the required response threshold, and a deadline.
Wait: preserve the pending dependency and next check trigger; continue
independent work or yield rather than repeatedly pinging the maintainer.
End: distinguish a submitted PR, a merged contribution, received feedback,
and verified adoption; report only the acceptance conditions actually met.
```

## What another maintainer can reuse

Make the submission reviewable before asking a curator to act. Treat a merge
as a maintainer-owned gate. Classify each reply by what it actually establishes,
then trace an accepted improvement through the canonical source and release.
The [current waiting rules](../../references/drift-control.md#scheduled-external-waits)
show how one concrete question can improve the reusable contract.
