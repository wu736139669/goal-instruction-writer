# Goal Instruction Writer（简体中文）

[![Latest release](https://img.shields.io/github/v/release/wu736139669/goal-instruction-writer?display_name=tag)](https://github.com/wu736139669/goal-instruction-writer/releases)
[![GitHub stars](https://img.shields.io/github/stars/wu736139669/goal-instruction-writer)](https://github.com/wu736139669/goal-instruction-writer/stargazers)
[![Validate skill](https://github.com/wu736139669/goal-instruction-writer/actions/workflows/validate.yml/badge.svg)](https://github.com/wu736139669/goal-instruction-writer/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)

[English](../README.md) · [简体中文](README.zh-CN.md)

> **写 Goal 之前，先把循环摊开。**

AI agent 很少因为“不够努力”失败，更多时候是运行很久后已经偏离了原目标。
<code>goal-instruction-writer</code> 是一个 Codex skill，把“继续改进、直到满意”变成一份能被检查、能被限制、能被暂停、能安全结束的 Goal 指令。

它为长任务补上可观察目标、有界循环、进展证据、漂移检查和明确终态。

## 原理总图

~~~mermaid
flowchart TD
    A["粗糙请求<br/>继续改进，直到满意"] --> B{"先预览？"}
    B -->|长任务 / 高成本 / 不确定| C["循环预览<br/>状态 · 分支 · 证据 · 终止"]
    B -->|短任务 / 可逆| D["生成 Goal"]
    C --> E{"用户确认循环"}
    E -->|修改| C
    E -->|确认| D
    D --> F["Goal Anchor<br/>目标 · 准则 · 范围 · 权限"]
    F --> G["一次迭代<br/>检查 → 选择 → 执行 → 验证"]
    G --> H{"对齐检查"}
    H -->|ON_TARGET| I["记录证据和游标"]
    I --> J{"还有未完成准则？"}
    J -->|是| G
    J -->|否| K["GOAL COMPLETE"]
    H -->|SIDE_QUEST| L["延期并设置回访条件"]
    L --> G
    H -->|DRIFTED| M["暂停并重新对齐"]
    M --> N["GOAL PAUSED: realignment required"]
    G --> O{"阻塞 / 预算耗尽 / 用户停止？"}
    O -->|阻塞| P["GOAL BLOCKED"]
    O -->|预算耗尽| Q["GOAL TIMEBOXED"]
    O -->|取消或超出权限| R["GOAL STOPPED"]
~~~

## 它解决什么问题

| 常见问题 | 技能补上的约束 |
| --- | --- |
| 目标只有“变得更好” | 写成可观察的最终结果和验收证据 |
| 循环只有“继续尝试” | 每轮只选一个最小工作单元，并记录预期变化 |
| 新发现悄悄改变方向 | 用 Goal Anchor 固定目标、准则、范围和权限 |
| 有用的旁支吞掉主线 | 标记 <code>SIDE_QUEST</code>，放入延期清单 |
| Agent 一直运行却没有进展 | 两轮等价无进展后暂停并重新对齐 |
| 外部依赖让任务无限等待 | 用 <code>GOAL BLOCKED</code> 写清依赖和解锁动作 |

## 三层契约

| 层 | 要回答的问题 | 可检查的证据 |
| --- | --- | --- |
| **Goal** | 最终应该存在什么结果？ | 文件、行为、决策或已验证事实 |
| **Loop** | 一轮怎样产生进展？ | 目标准则、预期变化、验证结果、下一游标 |
| **Termination** | 什么时候必须结束？ | <code>COMPLETE</code>、<code>BLOCKED</code>、<code>PAUSED</code>、<code>TIMEBOXED</code>、<code>STOPPED</code> |

长任务还会得到一个 **Goal Anchor**：

~~~text
Goal Anchor: <一个不可悄悄改变的结果>
Success criteria: C1 <...>; C2 <...>; C3 <...>
Frozen scope: <不变量和禁止的副作用>
Allowed authority: <可用工具、文件、系统和审批>
Current phase: <阶段或里程碑>
~~~

## 防漂移流程

~~~mermaid
flowchart LR
    A["Goal Anchor"] --> B["迭代记录<br/>目标准则 · 预期变化 · 范围理由"]
    B --> C["执行并验证"]
    C --> D{"对齐状态"}
    D -->|ON_TARGET| E["保留证据<br/>选择下一游标"]
    E --> B
    D -->|SIDE_QUEST| F["延期<br/>添加回访条件"]
    F --> B
    D -->|DRIFTED| G["暂停<br/>保留检查点"]
    G --> H["经过决策后重新锚定"]
    H --> B
~~~

“做了很多事”不等于进展。只有推进了明确准则，并留下另一个 Agent
可以检查的证据，一轮才算有效。

## 安装

### 推荐：open agent skills CLI

~~~bash
npx skills add wu736139669/goal-instruction-writer \
  --skill goal-instruction-writer -g -a codex -y
~~~

该命令已经针对本仓库验证，可以发现唯一技能：
<code>goal-instruction-writer</code>。

### Git clone 备用方式

~~~bash
SKILL_ROOT="\${CODEX_HOME:-$HOME/.codex}"
git clone https://github.com/wu736139669/goal-instruction-writer.git \
  "$SKILL_ROOT/skills/goal-instruction-writer"
~~~

安装后可以显式调用 <code>$goal-instruction-writer</code>，也可以让 Codex
在符合 Goal 特征的请求中自动发现它。

## 30 秒使用方式

### 1. 先预览长任务或不确定任务

~~~text
Use $goal-instruction-writer in Preview mode.
先不要执行，展示目标、循环步骤、成功/失败分支、证据、漂移检查和终止条件。
~~~

预览应该在任何外部副作用之前把循环展示出来：

~~~text
检查基线 → 选择一个准则 → 做一个有界改动
→ 验证证据 → 标记 ON_TARGET / SIDE_QUEST / DRIFTED
→ 继续、延期、阻塞或重新对齐
~~~

### 2. 确认循环

~~~text
确认这个循环。保留当前范围和终止条件，生成最终 Goal 指令。
~~~

### 3. 执行时使用 Goal

~~~text
每轮开始前说明：目标准则、预期证据、范围理由。
每轮结束后说明：实际证据、对齐标签、剩余差距、下一游标。
如果两轮等价迭代没有新进展，暂停并输出：
GOAL PAUSED: realignment required。
~~~

短小、可逆的任务可以跳过预览：

~~~text
Use $goal-instruction-writer to draft the final Goal for this task.
~~~

## 模式

| 模式 | 什么时候用 | 输出 |
| --- | --- | --- |
| **Preview** | 想先检查循环、分支和终止条件 | 可审阅流程，不立即生成可执行 Goal |
| **Draft** | 只有一个模糊请求 | 完整的可复制 Goal |
| **Refine** | 已有 Goal 但缺字段或边界 | 保留原意的最小修订 |
| **Audit** | 怀疑会漂移、重复或越权 | 问题清单和最小修复 |
| **Convert** | 有 ticket、清单或项目 brief | 不悄悄扩大范围的 Goal 转换 |

## 一个小例子

**模糊请求**

~~~text
把 importer 修好，继续尝试直到它能工作。
~~~

**可审阅 Goal**

~~~text
目标：让 fixtures/quoted_multiline.csv 在现有 record model 中完整导入，行数不漂移。

循环：检查当前失败 → 选择一个解析假设 → 做一个最小改动 → 运行聚焦测试
      → 记录 diff 和结果 → 选择下一个未验证准则。

防漂移：每轮绑定一个准则、预期证据和范围理由；无关清理放入延期清单。

结束：所有验收项通过则 GOAL COMPLETE；两次等价失败则
GOAL BLOCKED: <具体原因>；四轮仍未完成则 GOAL TIMEBOXED: <状态>。
~~~

## 运行时边界

技能负责设计和审查指令契约。运行时访问权限、工具可用性，以及外部副作用的审批，
仍由宿主 Agent 和用户控制。

遇到外部依赖时，应保留证据并写清解锁条件后停止。等待维护者、负责人或缺失数据，
不应该成为凭空发明更多工作的理由。

## 资源

- [技能入口](../SKILL.md)
- [Goal 契约和可复制骨架](../references/goal-contract.md)
- [循环预览格式和流程图](../references/loop-preview.md)
- [漂移检测和恢复](../references/drift-control.md)
- [编码、研究和开源案例](../references/examples.md)
- [发布工具包](launch-kit.md)
- [贡献指南](../CONTRIBUTING.md)
- [GitHub Discussions](https://github.com/wu736139669/goal-instruction-writer/discussions)

## 贡献

如果你有真实用例、令人困惑的预览，或更好的防漂移规则，可以在
[Discussions](https://github.com/wu736139669/goal-instruction-writer/discussions)
提出工作流问题，也可以针对明确改进提交 issue。欢迎小型 PR，但请保持三层契约，
并说明改动原因或附上案例。

提交 PR 前运行：

~~~bash
npx --yes skills add . --list
~~~

同样的打包检查会在 GitHub Actions 中自动运行。

## License

MIT，见 [LICENSE](../LICENSE)。

