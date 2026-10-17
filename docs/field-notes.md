# Field notes: long-running Goals in real work

Recorded on 2026-10-17. [English introduction](../README.md) ·
[中文介绍](README.zh-CN.md).

These notes separate a maintainer's experience, inspectable project material,
and a measured local log audit. They explain why the rules exist and what the
available evidence supports.

## Game development

The maintainer reports a longest game-development workflow of **more than 60
hours**, taking a project from its initial request through development and
delivery. This is a first-person field report. The specific 60-hour session has
not been published here as a complete timestamped trace, and the duration is
not a speed, quality, or unattended-execution guarantee.

The practical value is continuity through a large chain of work:

| Phase | What the Goal carries forward |
| --- | --- |
| Initial brief | One observable game outcome, platform, scope, and acceptance criteria |
| Core implementation | A playable loop and one smallest next work unit |
| Content and assets | The original art/gameplay direction and deferred side quests |
| Debugging and playtesting | New evidence, remaining gaps, and affected checks |
| Build and handoff | Verified artifacts, limits, and an exact completion state |

Two publicly documented game projects show the kinds of artifacts this workflow
must preserve: [Moonlit Kingdom](https://toolpantry.app/gamedev/moonlit-kingdom)
and [Linjiang Chronicles](https://toolpantry.app/gamedev/linjiang-chronicles).
The public pages contain runtime clips, game structure, and explicit delivery
boundaries. They are recorded examples from the maintainer's work, not a
controlled comparison of this skill against a baseline.

The release video uses the already-public Moonlit Kingdom forest/dispatch
recording and identifies it by name. That excerpt is **not** a time-lapse or
recording of the reported 60-hour run. A playable development build and an
engineering handoff are distinct from a store release; the game pages record
their own current status.

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

## 中文说明

维护者报告过一次 60 多小时、从初始需求推进到游戏开发交付的完整工作流。
本文尚未公开对应会话的全量时间记录，因此把它作为使用经历，而非独立计时实验。
演示中的月光王国片段来自已公开的真实运行录像，明确标注项目名；它不被当作该
60 多小时工作流的连续录像。

Android 案例的数据来自对已有日志和单测 XML 的本地核查，未重跑项目。505 项测试
并不等于耗时很长：最终两变体 SDK 套件时间合计约 45 秒，14 次 Gradle 调用合计
9 分 32 秒。部分重跑修出了实际问题，因此新规则保留必要验收，改进重跑触发与证据
复用。v0.2.0 尚无对照测量，不宣称固定提速比例或节省工时。
