# Goal Instruction Writer

[![Latest release](https://img.shields.io/github/v/release/wu736139669/goal-instruction-writer?display_name=tag)](https://github.com/wu736139669/goal-instruction-writer/releases)
[![GitHub stars](https://img.shields.io/github/stars/wu736139669/goal-instruction-writer)](https://github.com/wu736139669/goal-instruction-writer/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **Preview the loop before you run the Goal.**

![Goal Instruction Writer social preview](assets/social-preview.png)

`goal-instruction-writer` is a Codex skill for turning vague requests into
bounded, evidence-driven Goal instructions. It is designed for work that runs
long enough to drift: coding tasks, research, automation, and multi-stage
agent workflows.

它解决的是一个具体问题：AI agent 做了很久之后，仍然在“努力工作”，但已经偏离了真正目标。技能会先让你检查循环，再生成带验收标准、漂移检查和明确终态的 Goal。

## What it does

- **Preview first:** inspect the iteration flow, branches, evidence, drift
  gates, and stop conditions before a final Goal is written.
- **Write the contract:** define an observable objective, baseline, scope,
  acceptance criteria, authority, and deliverable.
- **Keep long runs on target:** bind every iteration to a criterion and expected
  evidence; park side quests; pause when alignment is lost.
- **Stop cleanly:** distinguish `GOAL COMPLETE`, `GOAL BLOCKED`,
  `GOAL PAUSED`, `GOAL TIMEBOXED`, and `GOAL STOPPED`.

## 60-second demo

Start with a rough request:

```text
I need an agent to improve our importer. It can keep trying until it works.
```

Ask for a loop preview before generating the Goal:

```text
Use $goal-instruction-writer in Preview mode.
先展示循环的具体步骤、成功/失败分支、防偏航检查和结束条件，确认后再生成最终 Goal。
```

The preview makes the hidden decisions reviewable:

```text
Inspect the baseline → choose one criterion → make one bounded change
→ verify evidence → classify ON_TARGET / SIDE_QUEST / DRIFTED
→ continue, defer, block, or realign
```

After you confirm the loop, ask:

```text
确认这个循环，生成最终 Goal 指令。
```

For a short, reversible task, you can skip the preview and ask directly:

```text
Use $goal-instruction-writer to draft the final Goal for this task.
```

## Install

Clone the skill into the Codex skill directory:

```bash
git clone https://github.com/wu736139669/goal-instruction-writer.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/goal-instruction-writer"
```

Or copy the folder if you already downloaded the repository:

```bash
cp -R goal-instruction-writer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

The skill is discoverable automatically and can also be invoked explicitly as
`$goal-instruction-writer`.

## The contract

Every final Goal is organized around three layers:

| Layer | Question | Required proof |
| --- | --- | --- |
| Goal | What observable result should exist? | Acceptance criteria and evidence |
| Loop | How does one iteration produce progress? | Target criterion, expected delta, verification, cursor |
| Termination | When does the work legally end? | Complete, blocked, paused, timeboxed, or stopped state |

Long-running work also gets a **Goal Anchor**. The Anchor freezes the outcome,
criteria, scope, and authority. A new discovery may change the plan, but it
cannot silently change the Goal.

## Resources

- [Skill entrypoint](SKILL.md)
- [Goal contract and ready-to-paste skeleton](references/goal-contract.md)
- [Loop preview format and flow diagram](references/loop-preview.md)
- [Drift detection and recovery](references/drift-control.md)
- [Coding and research examples](references/examples.md)
- [Launch kit with ready-to-post copy](docs/launch-kit.md)
- [Contributing guide](CONTRIBUTING.md)

## Contributing

Have a real use case, a confusing preview, or a better drift rule? Open a
[Discussion](https://github.com/wu736139669/goal-instruction-writer/discussions)
for a workflow question, or open an issue for a focused change. Small pull
requests are welcome when they preserve the three-layer contract and include a
clear reason or example.

## License

MIT. See [LICENSE](LICENSE).
