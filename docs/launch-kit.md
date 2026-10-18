# Launch Kit

This kit is for introducing Goal Instruction Writer to people who run coding,
research, automation, or multi-stage agent workflows.

## Positioning

**Audience:** people running an AI agent for more than a few iterations.

**Problem:** the agent keeps producing activity after the work has drifted away
from the requested outcome.

**Promise:** preview the loop before execution, bind every iteration to evidence,
and stop cleanly when the work is complete, blocked, or off target.

**Short description:**

> Preview the loop before you run the Goal. Write Goals that stay on target,
> preserve evidence across long runs, and stop cleanly. Continue useful work,
> or save a pending criterion until its next check time or relevant notification.

For the distinction between active iterations and continuation after a trigger,
use the [introduction](../README.md#active-work-and-waiting). The skill defines
the checkpoint and resume conditions; automatic wake-up requires host support.
The live wait/resume transition remains untested.

## Launch checklist

- [x] Public GitHub repository
- [x] Bilingual README with a 60-second demo
- [x] Topics for discovery
- [x] Discussions for questions and use cases
- [x] `v0.1.0` release
- [x] `v0.2.0` verification strategy and real-use field notes
- [x] Animated README excerpt and full demonstration video
- [x] Third-party distribution and submission guide
- [x] Inspected multi-day Factory Town Idle case with a delivery timeline
- [x] Issue templates and contribution guide
- [x] Social preview asset at `assets/social-preview.png`
- [x] Verified installation through the open agent skills CLI
- [ ] Upload the social preview in GitHub repository settings
- [ ] Publish the first community posts
- [ ] Collect three real use cases and turn them into examples

## Short post

For new English posts, choose a concrete story from the
[case library](cases/README.md): a game candidate, a research handoff, an SDK
software release, or a public contribution that changed the skill. Use that
case's recorded outcome and evidence boundary; the posts below retain their
original launch context.

### English

> I open-sourced the Goal-writing workflow I use for long-running agent work.
> My longest game-development workflow is an estimated 60+ hours. One concrete
> case follows a Factory Town Idle Godot port from analysis and architecture to
> a 0.49 local candidate with Mac and Android packages, while the full Goal
> continues.
>
> Goal Instruction Writer previews the loop first, then turns the request into
> an observable outcome, acceptance evidence, drift controls, and clear stop
> conditions. v0.2.0 adds focused verification and reuse of still-valid results.
> The README includes a recorded-gameplay demo and explains the evidence behind
> the field reports.
>
> Try it: https://github.com/wu736139669/goal-instruction-writer

### 中文

> 我把自己写长任务 Goal 的工作流开源成了一个 Codex skill。
> 我的游戏开发工作流最长一次估计超过 60 小时。公开案例记录了 Factory Town Idle
> Godot 项目从分析与架构推进到 0.49 本地候选、交付 Mac/APK 的过程，完整 Goal 仍在继续。
>
> 它先预览循环，再生成带结果、验收证据、防漂移和明确结束条件的 Goal。
> v0.2.0 还补上了按影响验证、复用有效结果和重跑触发规则。
> README 有真实游戏运行片段，也写清了使用报告和日志核查各自能证明什么。
>
> GitHub：https://github.com/wu736139669/goal-instruction-writer

## Community post

Use this longer version in an agent, developer-tools, or prompt-engineering
community:

```text
长时间运行的 AI Agent 有一个常见问题：它一直在工作，但工作的方向已经
偏离最初目标。

我做了一个开源 Codex skill：Goal Instruction Writer。

它的流程是：
1. 先预览每轮循环和所有分支；
2. 确认后再生成最终 Goal；
3. 每轮绑定一个验收标准和预期证据；
4. 旁支任务延后；
5. 两轮没有进展或发生偏航时暂停重对齐。

适合 coding、research、自动化和多阶段 agent 工作流。

如果你愿意试，最有价值的反馈是：哪一种任务最容易让你的 Agent 跑偏？
```

## Seven-day cadence

| Day | Content | Call to action |
| --- | --- | --- |
| 1 | Launch post with the 60-second demo | Try Preview mode |
| 2 | Before/after example: vague Goal vs bounded Goal | Share a failure case |
| 3 | Explain Goal Anchor and drift labels | Ask for a use case |
| 4 | Explain the loop preview flow | Open a Discussion |
| 5 | Coding example | Fork or adapt the skill |
| 6 | Research/automation example | Submit an example |
| 7 | Lessons learned and next roadmap | Star, issue, or contribute |

Keep one core message across channels and change the example, not the promise.
Reply to questions with concrete previews and link back to the relevant
reference instead of repeating a generic pitch.

## Measure the funnel

Track these signals weekly:

- README visits to clone or install;
- Preview-mode examples people share;
- Discussions and issue quality;
- Forks, pull requests, and contributed examples;
- Repeat use cases, not only one-time stars.

The first milestone is three independent use cases that improve the reference
examples. The second is a contributor who changes a rule or adds an adapter
without needing a private explanation.

## Directory submissions

The repository can be installed directly through the open agent skills CLI:

```bash
npx skills add wu736139669/goal-instruction-writer \
  --skill goal-instruction-writer -g -a codex -y
```

When submitting to a curated Codex or agent-skills directory, use this entry:

```text
- [goal-instruction-writer](https://github.com/wu736139669/goal-instruction-writer)
  - Preview agent loops and write drift-resistant Goal instructions with explicit evidence and terminal states.
```
