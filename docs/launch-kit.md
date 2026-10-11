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
> detect drift, and stop cleanly.

## Launch checklist

- [x] Public GitHub repository
- [x] Bilingual README with a 60-second demo
- [x] Topics for discovery
- [x] Discussions for questions and use cases
- [x] `v0.1.0` release
- [x] Issue templates and contribution guide
- [x] Social preview asset at `assets/social-preview.png`
- [ ] Upload the social preview in GitHub repository settings
- [ ] Publish the first community posts
- [ ] Collect three real use cases and turn them into examples

## Short post

### English

> I open-sourced a Codex skill for a problem I keep seeing with long-running
> agents: they continue working after they have drifted from the goal.
>
> Goal Instruction Writer lets you preview the loop first, then generates a
> Goal with acceptance evidence, drift checks, and explicit terminal states.
>
> Try it: https://github.com/wu736139669/goal-instruction-writer

### 中文

> 我开源了一个 Codex skill，专门解决长时间运行的 AI Agent 越做越偏的问题。
>
> 先预览循环，再生成带验收标准、漂移检查和明确终态的 Goal 指令。
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
