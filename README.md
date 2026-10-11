# Goal Instruction Writer

[![Latest release](https://img.shields.io/github/v/release/wu736139669/goal-instruction-writer?display_name=tag)](https://github.com/wu736139669/goal-instruction-writer/releases)
[![GitHub stars](https://img.shields.io/github/stars/wu736139669/goal-instruction-writer)](https://github.com/wu736139669/goal-instruction-writer/stargazers)
[![Validate skill](https://github.com/wu736139669/goal-instruction-writer/actions/workflows/validate.yml/badge.svg)](https://github.com/wu736139669/goal-instruction-writer/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **写 Goal 之前，先把循环摊开。**
>
> **Before an agent runs the Goal, make the loop reviewable.**

![Goal Instruction Writer social preview](assets/social-preview.png)

AI agent 很少因为“不够努力”失败，更多时候是做了很久以后已经偏离了原目标。
<code>goal-instruction-writer</code> 是一个 Codex skill，把“继续改进、直到满意”变成一份能被检查、能被暂停、能安全结束的 Goal 指令。

It turns vague requests into a contract with an observable outcome, a bounded loop,
evidence for every meaningful step, drift gates, and explicit terminal states.

## The idea in one picture

~~~mermaid
flowchart TD
    A["粗糙请求<br/>继续改进，直到满意"] --> B{"先预览？"}
    B -->|长任务 / 高成本 / 不确定| C["Loop Preview<br/>状态 · 分支 · 证据 · 终止"]
    B -->|短任务 / 可逆| D["Draft Goal"]
    C --> E{"用户确认循环"}
    E -->|修改| C
    E -->|确认| D
    D --> F["Goal Anchor<br/>目标 · 准则 · 范围 · 权限"]
    F --> G["一次迭代<br/>Inspect → Select → Act → Verify"]
    G --> H{"对齐检查"}
    H -->|ON_TARGET| I["记录证据和游标"]
    I --> J{"还有未完成准则？"}
    J -->|是| G
    J -->|否| K["GOAL COMPLETE"]
    H -->|SIDE_QUEST| L["延期清单"]
    L --> G
    H -->|DRIFTED| M["暂停并重新对齐"]
    M --> N["GOAL PAUSED: realignment required"]
    G --> O{"阻塞 / 预算 / 用户停止？"}
    O -->|阻塞| P["GOAL BLOCKED"]
    O -->|预算耗尽| Q["GOAL TIMEBOXED"]
    O -->|用户取消或越权| R["GOAL STOPPED"]
~~~

## Why this exists

| 常见问题 | 技能补上的约束 |
| --- | --- |
| 目标只有“变得更好” | 写成可观察的最终结果和验收证据 |
| 循环只有“继续尝试” | 每轮只选一个最小工作单元，并记录预期变化 |
| 新发现悄悄改变方向 | 用 Goal Anchor 冻结目标、准则、范围和权限 |
| 有用的旁支吞掉主线 | 标记 <code>SIDE_QUEST</code>，放入延期清单 |
| Agent 一直运行却没有进展 | 两轮等价无进展就暂停并重新对齐 |
| 外部依赖让任务无限等待 | 用 <code>GOAL BLOCKED</code> 写清楚依赖和解锁动作 |

## The three-layer contract

| Layer | 要回答的问题 | 可检查的证据 |
| --- | --- | --- |
| **Goal** | 最终应该存在什么结果？ | 文件、行为、决策或已验证事实 |
| **Loop** | 一轮怎样产生进展？ | 目标准则、预期变化、验证结果、下一游标 |
| **Termination** | 什么时候必须结束？ | <code>COMPLETE</code>、<code>BLOCKED</code>、<code>PAUSED</code>、<code>TIMEBOXED</code>、<code>STOPPED</code> |

Long-running work also gets a **Goal Anchor**:

~~~text
Goal Anchor: <one immutable outcome>
Success criteria: C1 <...>; C2 <...>; C3 <...>
Frozen scope: <invariants and forbidden side effects>
Allowed authority: <tools, files, systems, and approvals>
Current phase: <phase or milestone>
~~~

## Drift control in one picture

~~~mermaid
flowchart LR
    A["Goal Anchor"] --> B["Iteration record<br/>criterion · expected delta · scope reason"]
    B --> C["Act and verify"]
    C --> D{"Alignment"}
    D -->|ON_TARGET| E["Keep evidence<br/>choose next cursor"]
    E --> B
    D -->|SIDE_QUEST| F["Defer<br/>add revisit condition"]
    F --> B
    D -->|DRIFTED| G["Pause<br/>preserve checkpoint"]
    G --> H["Re-anchor after a decision"]
    H --> B
~~~

The rule is simple: activity is not progress. An iteration counts only when it
advances a named criterion and leaves evidence another agent can inspect.

## Install

### Recommended: open agent skills CLI

~~~bash
npx skills add wu736139669/goal-instruction-writer \
  --skill goal-instruction-writer -g -a codex -y
~~~

The command is verified against this repository and detects one skill:
<code>goal-instruction-writer</code>.

### Git clone fallback

~~~bash
SKILL_DIR="${CODEX_HOME:-$HOME/.codex}/skills/goal-instruction-writer"
git clone https://github.com/wu736139669/goal-instruction-writer.git \
  "$SKILL_DIR"
~~~

After installation, invoke it explicitly as <code>$goal-instruction-writer</code>, or let
Codex discover it automatically for Goal-shaped requests.

## 30-second usage

### 1. Preview a long or uncertain task

~~~text
Use $goal-instruction-writer in Preview mode.
先不要执行，展示目标、循环步骤、成功/失败分支、证据、漂移检查和终止条件。
~~~

The preview should expose the loop before any external side effect:

~~~text
Inspect baseline → choose one criterion → make one bounded change
→ verify evidence → classify ON_TARGET / SIDE_QUEST / DRIFTED
→ continue, defer, block, or realign
~~~

### 2. Confirm the loop

~~~text
确认这个循环。保留当前范围和终止条件，生成最终 Goal 指令。
~~~

### 3. Use the Goal during execution

~~~text
每轮开始前说明：目标准则、预期证据、范围理由。
每轮结束后说明：实际证据、对齐标签、剩余差距、下一游标。
如果两轮没有新进展，暂停并输出：GOAL PAUSED: realignment required。
~~~

For a short, reversible task, skip Preview and ask directly:

~~~text
Use $goal-instruction-writer to draft the final Goal for this task.
~~~

## Modes

| Mode | 什么时候用 | 结果 |
| --- | --- | --- |
| **Preview** | 想先看循环、分支和终止条件 | 可审阅的流程，不产生可执行 Goal |
| **Draft** | 只有一个模糊请求 | 完整的可复制 Goal |
| **Refine** | 已有 Goal 但缺字段或边界 | 保留原意的最小修订 |
| **Audit** | 怀疑会漂移、重复或越权 | 问题清单和最小修复 |
| **Convert** | 有 ticket、清单或项目 brief | 不扩展范围的 Goal 转换 |

## A small before/after

**Weak request**

~~~text
把 importer 修好，继续尝试直到它能工作。
~~~

**Reviewable Goal**

~~~text
目标：让 fixtures/quoted_multiline.csv 在现有 record model 中完整导入，行数不漂移。

循环：检查当前失败 → 选择一个解析假设 → 做一个最小改动 → 运行聚焦测试
      → 记录 diff 和结果 → 选择下一个未验证准则。

防漂移：每轮绑定一个准则、预期证据和范围理由；无关清理放入延期清单。

结束：所有验收项通过则 GOAL COMPLETE；两次等价失败则
GOAL BLOCKED: <具体原因>；四轮仍未完成则 GOAL TIMEBOXED: <状态>。
~~~

## What it controls—and what it does not

The skill designs and audits the instruction contract. Runtime access,
permissions, tool availability, and approval for external side effects remain
controlled by the host agent and the user.

For external gates, the correct behavior is to preserve evidence and stop with
the exact unblock needed. Waiting for a maintainer, owner, or missing dataset is
not a reason to invent more work.

## Resources

- [Skill entrypoint](SKILL.md)
- [Goal contract and ready-to-paste skeleton](references/goal-contract.md)
- [Loop preview format and flow diagram](references/loop-preview.md)
- [Drift detection and recovery](references/drift-control.md)
- [Coding, research, and open-source examples](references/examples.md)
- [Launch kit with ready-to-post copy](docs/launch-kit.md)
- [Contributing guide](CONTRIBUTING.md)
- [GitHub Discussions](https://github.com/wu736139669/goal-instruction-writer/discussions)

## Contributing

Have a real use case, a confusing preview, or a better drift rule? Open a
[Discussion](https://github.com/wu736139669/goal-instruction-writer/discussions)
for a workflow question, or open an issue for a focused change. Small pull
requests are welcome when they preserve the three-layer contract and include a
clear reason or example.

Before opening a pull request, run:

~~~bash
npx --yes skills add . --list
~~~

The same packaging check runs automatically in GitHub Actions.

## License

MIT. See [LICENSE](LICENSE).
