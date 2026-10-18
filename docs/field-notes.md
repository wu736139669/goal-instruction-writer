# Field notes: long-running Goals in real work

Observations recorded on 2026-10-17; case library expanded on 2026-10-18.
[English introduction](../README.md) ·
[中文介绍](README.zh-CN.md).

These notes separate a maintainer's experience, inspectable project material,
and a measured local log audit. They explain why the rules exist and what the
available evidence supports.

The [English case library](cases/README.md) adds dedicated write-ups for
[source-led research](cases/source-led-research.md),
[Android SDK delivery](cases/android-sdk-delivery.md), and the
[public feedback loop](cases/open-source-feedback.md). The research and Godot
write-ups describe different stages of the same project.

## Game development

The maintainer reports a longest game-development workflow of **more than 60
hours** and identified a concrete session for a closer look: a Factory Town
Idle Godot port. Its local records cover October 13–17, from analysis and
architecture through playable systems and a 0.49 local candidate with Mac and
Android packages. The full recreation Goal remained active at the snapshot.

The [case study](cases/factory-town-idle.md) includes a delivery timeline, the
source/artifact identities inspected, and a
[public audit summary](cases/factory-town-idle-evidence.json). The 60+ hour
figure remains a first-person estimate. The records do not measure total active
compute time, continuous unattended execution, or a completed full recreation.

The practical value is continuity through a large chain of work:

| Phase | What the Goal carries forward |
| --- | --- |
| Initial brief | One observable game outcome, platform, scope, and acceptance criteria |
| Core implementation | A playable loop and one smallest next work unit |
| Content and assets | The original art/gameplay direction and deferred side quests |
| Debugging and playtesting | New evidence, remaining gaps, and affected checks |
| Build and handoff | Verified artifacts, limits, and an exact completion state |

The case also makes verification reuse concrete. A research-screen revision
reused 1,983 exact numerical comparisons because the checked core, inputs, and
fixtures still matched, while running current behavior and scene checks. The
next candidate changed the research-material rule, so those old comparisons
were not carried forward as proof of the changed core. Relevant current checks
were recorded instead. This illustrates the strategy; it is not a measured
before/after speedup from installing this skill.

Two publicly documented game projects show the kinds of artifacts this workflow
must preserve: [Moonlit Kingdom](https://toolpantry.app/gamedev/moonlit-kingdom)
and [Linjiang Chronicles](https://toolpantry.app/gamedev/linjiang-chronicles).
The public pages contain runtime clips, game structure, and explicit delivery
boundaries. They are recorded examples from the maintainer's work, not a
controlled comparison of this skill against a baseline.

The current English-only demonstration illustrates the documented Factory Town
Idle checkpoints; it contains no gameplay footage or reconstructed chat log.
The archived v0.2.0 video used an already-public Moonlit Kingdom forest/dispatch
recording, with Chinese game UI and bilingual captions. That separate project
is **not** a time-lapse or recording of the reported 60-hour run. A playable
development build and an engineering handoff are distinct from a store release;
the game pages record their own current status.

## Android SDK delivery

A local audit of a real Android SDK release found a useful distinction between
test count and execution cost. The final run had 505 SDK tests per variant and
21 UI tests per variant. Existing logs and JUnit XML were inspected; the audit
did not rerun the project.

| Measurement | Observed result | Interpretation |
| --- | --- | --- |
| Final SDK Debug suites | 24.541 seconds | Sum of the recorded suite durations |
| Final SDK Release suites | 20.073 seconds | Sum of the recorded suite durations |
| Final complete root check | 1 minute 30 seconds | Includes tests, compilation, lint, API and artifact work |
| Five broad root checks | 7 minutes 15 seconds total | Includes a failed API gate and later successful checks |
| All 14 recorded Gradle calls | 9 minutes 32 seconds total | Duplicate copies of failure logs were excluded |

The five root logs were `full1`, `full2`, `final-check`, `final-check2`, and
`final-check3`, reporting 115, 83, 81, 66, and 90 seconds respectively.
The source project and raw engineering bundle remain private. These are
maintainer-audited aggregate observations, not independently reproducible public
benchmarks. They do not measure total session duration or prove that validation
was the main cause of elapsed time.

Some reruns followed real changes: an API-checker compatibility correction and
cancellation/session race fixes. Those checks were justified. The improvement
is to invalidate the evidence that depends on a change, preserve unaffected
results, and schedule the required final release checks after the relevant
implementation settles. No before/after runtime saving is claimed for v0.2.0.

This case led to the new [verification strategy](../SKILL.md#verification-strategy)
and [SDK examples](../references/examples.md#sdk-delivery-choose-checks-after-a-successful-validation):

- Focused checks while editing; broader checks at required gates.
- Source/artifact and environment context for evidence reuse.
- A reason for each rerun and renewed consumer checks when an AAR changes.
- Suitable limits for costly commands, without treating a timeout as a pass.

## Open-source launch

The [October 11 evaluation](evaluations/2026-10-11-independent-goal-evaluation.md)
simulated a confirmed preview and performed two bounded read-only iterations.
It inspected packaging, the feedback path, and an external maintainer gate.
Its scope was instruction behavior and honest terminal states, not coding
throughput or long-run performance.

The [feedback thread](https://github.com/wu736139669/goal-instruction-writer/discussions/1)
also contains a reader's proposed edge case about waiting for replies versus
actionable work that makes no progress. That is a useful design question; it
is labeled as reading feedback rather than an installation/execution test.
Version 0.2.4 makes the scheduled-wait branch explicit across the skill and
templates, following the [maintainer reply](https://github.com/wu736139669/goal-instruction-writer/discussions/1#discussioncomment-19016524).
The historical evaluation remains evidence of two bounded read-only iterations;
it did not test waiting for a real deadline or an automatic resume.
