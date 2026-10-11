---
name: goal-instruction-writer
description: Draft, refine, or audit durable Goal instructions for agents. Use when a task needs a clear observable outcome, a bounded execution loop, measurable acceptance evidence, and explicit complete, blocked, paused, or timeboxed states; do not use for ordinary one-shot prompts.
---

# Goal Instruction Writer

Turn a vague request into a ready-to-run Goal instruction that an agent can
execute without guessing what success, progress, or stopping means. Preserve
the user's intent, language, authority boundaries, and requested scope.

Read [references/goal-contract.md](references/goal-contract.md) when drafting
or auditing a Goal. Read [references/examples.md](references/examples.md) only
when a worked example would clarify the requested task.

## Choose the mode

- **Draft:** build a Goal from a rough request.
- **Refine:** preserve an existing Goal while closing missing objective,
  evidence, loop, or termination fields.
- **Audit:** identify ambiguity, unbounded repetition, unverifiable criteria,
  and unsafe or unauthorized transitions; propose the smallest fixes.
- **Convert:** turn a checklist, ticket, or project brief into a Goal without
  expanding its scope.

If the mode is not stated, infer it from the input. Ask only questions whose
answers would change the objective, authority, acceptance evidence, or legal
terminal state. Otherwise state assumptions and continue.

## Build the three-layer contract

### 1. Goal: define the outcome

Write one sentence with an observable end state. It should say what artifact,
behavior, decision, or verified change will exist when the work is complete.
Then make the contract concrete:

- **Baseline:** what exists now and which revision, source, or facts are
  authoritative.
- **Scope:** what may change and what is frozen.
- **Acceptance criteria:** observable checks tied to evidence, not activities
  such as “keep working” or “try harder.”
- **Dependencies and authority:** tools, access, owner decisions, and external
  gates the agent may or may not cross.
- **Deliverable:** the files, decision, report, or message that will be handed
  back.

Prefer one load-bearing outcome per Goal. Split unrelated outcomes into
separate Goals. Replace vague verbs such as “improve,” “handle,” or “finish”
with a measurable result.

### 2. Loop: define how progress is made

Use a bounded iteration with a visible progress signal:

1. **Inspect** the current state and the last durable cursor.
2. **Select** the smallest next work unit that can move an acceptance criterion.
3. **Act** within the allowed scope and authority.
4. **Verify** the result against the relevant criterion; capture the evidence.
5. **Record** the delta, remaining gap, and next cursor before another
   iteration.

State the iteration limit that fits the task: a timebox, tool or token budget,
maximum attempts, or a finite work-unit list. Add a no-op rule: do not repeat
the same action without new information; after a repeated failure, change the
hypothesis or stop with the blocker. The loop must be able to explain why the
next iteration is different from the previous one.

### 3. Termination: define legal endings

Make the terminal states explicit and mutually understandable:

- **Complete:** every acceptance criterion is verified and the deliverable is
  available.
- **Blocked:** a named dependency, missing authority, or unresolved failure
  prevents the next meaningful action; report the exact unblock needed.
- **Paused:** the owner explicitly asks to pause; preserve the cursor and do
  not resume without authorization.
- **Timeboxed/Budgeted:** the limit is reached before completion; report the
  verified progress, remaining gap, and the safest next action.
- **Stopped:** the owner cancels the work or an action would exceed the granted
  authority; do not silently continue.

Do not use “continue until satisfied,” “try indefinitely,” or a success claim
based only on effort. If the task has a local convention for terminal strings,
preserve it; otherwise give each state a short, exact label and require the
final response to include it.

## Produce the answer

Return the result in the user's language. Unless they request another format,
use this order:

1. **Design notes:** one short paragraph explaining the objective, loop, and
   termination choices; list assumptions or high-value open questions.
2. **Ready-to-paste Goal:** include the full instruction in a fenced block with
   `Objective`, `Baseline and scope`, `Acceptance criteria`, `Execution loop`,
   `Limits and no-op rule`, `Termination`, and `Reporting` sections.
3. **Audit notes:** if refining or auditing, name each remaining ambiguity and
   the smallest change that resolves it.

The ready-to-paste block must be executable as an instruction, not a discussion
of how one might write an instruction. Keep acceptance checks and terminal
states concrete enough that a later reviewer can decide them from evidence.
