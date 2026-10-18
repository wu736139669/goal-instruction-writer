# Three short prompts to try

[Source and installation](https://github.com/wu736139669/goal-instruction-writer#start-in-two-minutes) ·
[Real case studies](cases/README.md)

Install the skill using the upstream README, then paste one prompt into Codex.
These are practice briefs to adapt, rather than reports of completed runs.
Each keeps the first response in planning or audit mode.

## 1. Preview a small, read-only task

Use this in a repository containing a `README.md`:

~~~text
Use $goal-instruction-writer in Preview mode.
Design a read-only Goal to audit local Markdown links in README.md and report
broken targets with proposed fixes. Limit the eventual audit to two passes.
Show the outcome, acceptance evidence, loop, checkpoint, and stop conditions.
Do not perform the audit or edit files yet.
~~~

Look for a clear definition of a local link, an evidence-backed finding format,
a finite audit loop, and a next step. A preview should not claim that links have
already been verified. Confirm or revise the loop before requesting a final Goal.

## 2. Audit a Goal that repeats expensive checks

~~~text
Use $goal-instruction-writer in Audit mode on the quoted instruction below.
Do not execute the instruction or change project files.

"Improve the settings screen until it feels polished. After every edit, run
the entire test suite, rebuild every platform, package a release, and repeat."

Identify missing acceptance evidence, unbounded repetition, and checks that
belong at a delivery gate. Propose the smallest replacement contract with
focused iteration checks, evidence-reuse conditions, a finite work budget,
and explicit stop states. Preserve any mandatory release requirements.
~~~

Look for concrete success criteria, checks chosen for the change, a rule for
invalidating old evidence, and a required final delivery gate. The audit should
not invent passing tests, a measured speedup, or authority to publish a release.

## 3. Preview a bounded game-development slice

~~~text
Use $goal-instruction-writer in Preview mode.
Design a Goal for a small desktop Godot production-game slice: one scene,
one resource, one producer, one purchasable upgrade, and local save/load.
Keep multiplayer, monetization, extra resources, and mobile releases out of scope.
Show the playable acceptance criteria, one bounded iteration, focused checks,
runtime playtest evidence, a build handoff, a durable checkpoint, and stop states.
Give the work a finite budget and expose any missing owner decisions.
Do not create the project or execute development yet.
~~~

Look for an observable playable loop, a save/continue check, a reviewable handoff,
and a next cursor tied to one criterion. If the budget ends with open criteria,
the report should preserve those gaps rather than claim a completed game.

The [Factory Town Idle case](cases/factory-town-idle.md) shows a larger maintainer
workflow with a dated delivery timeline and explicit evidence limits.

## After the preview

If the loop fits your intent, ask for the final Goal while preserving its scope
and stop conditions. Start the underlying work only when you also authorize
execution. Your host supplies tools, persistence, invocation, and permissions.

For feedback, share the host you used, which prompt you tried, and the output
that was useful or confusing in
[GitHub Discussions](https://github.com/wu736139669/goal-instruction-writer/discussions).
Share only material you intend to make public.

If these examples help,
[star the source repository](https://github.com/wu736139669/goal-instruction-writer)
to keep them handy and follow updates.
