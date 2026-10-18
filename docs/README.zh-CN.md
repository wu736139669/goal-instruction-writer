# Goal Instruction Writer（简体中文）

[![Latest release](https://img.shields.io/github/v/release/wu736139669/goal-instruction-writer?display_name=tag)](https://github.com/wu736139669/goal-instruction-writer/releases)
[![GitHub stars](https://img.shields.io/github/stars/wu736139669/goal-instruction-writer)](https://github.com/wu736139669/goal-instruction-writer/stargazers)
[![Validate skill](https://github.com/wu736139669/goal-instruction-writer/actions/workflows/validate.yml/badge.svg)](https://github.com/wu736139669/goal-instruction-writer/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](../LICENSE)

[English](../README.md) · [简体中文](README.zh-CN.md)

> **让长时间运行的 Agent 始终朝着同一个结果推进。**
>
> 先预览循环，让进展可检查，最后凭证据交付。

![Goal 技能动态演示](../assets/goal-overview.gif)

[观看完整演示](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.0/goal-overview.mp4) · [真实使用与证据](field-notes.md) · [技能投稿指南](distribution.md)

AI agent 很少因为“不够努力”失败，更多时候是运行很久后已经偏离了原目标。
<code>goal-instruction-writer</code> 是一个 Codex skill，把“继续改进、直到满意”变成一份能被检查、能被限制、能被暂停、能安全结束的 Goal 指令。

它为长任务补上可观察目标、有界循环、进展证据、漂移检查和明确终态。

## 循环推进与等待后接续

技能支持生成“时间或事件触发后接续”的 Goal 指令。同一个 Goal 可以在主动迭代与等待之间
切换；目标和验收准则保持一致，下一步取决于当前有什么工作能实际推进。

| 当前情况 | 生成的 Goal 会要求 Agent 怎么做 |
| --- | --- |
| 有可推进且已授权的工作 | 检查、执行、验证、记录证据，再选择下一个有界工作单元 |
| 某个准则依赖未来时间或外部回复 | 保存待办准则、下次检查时间或相关通知、截止时间；继续其他可推进的工作，或保留检查点并交还控制权 |
| 任务再次被启动 | 先读回检查点、检查限额；只有满足原定时间或事件条件时才查询待办依赖，再核实结果、接着做 |

等待是同一个 Goal 的一个分支。约定时间到达或收到相关通知，都可以触发下一次检查。
正常等待和按时查到“仍未回复”不计为失败尝试；实际查询、截止时间和宿主总预算仍然有效。

技能约定保存哪些状态、何时允许再次检查，以及怎样接续。宿主定时任务、相关事件，或一条
再次启动 Agent 的授权消息，都可以提供下一次调用；宿主负责状态存取和任务调用，包括
在约定时间自动投递消息。宿主无法自动唤醒时，也可以在后续获授权的启动中读回检查点。
目前尚未做真实等待与恢复测试。
详见[等待规则](../references/drift-control.md#scheduled-external-waits)和
[English example](cases/open-source-feedback.md#how-the-waiting-branch-becomes-concrete)。

## 从真实长任务中提炼

一个具体案例是 **Factory Town Idle 的 Godot 重做**：项目记录覆盖 10 月 13 日的分析与
架构准备、10 月 14 日的可玩系统，以及 10 月 17 日交付的 **0.49 本地候选与 Mac、Android
安装包**。生产、建设、研究、跨镇效果、保存恢复和下一工作游标，经过多轮开发仍能接续。
可查看[Case study and delivery timeline](cases/factory-town-idle.md)。

维护者估计，自己最长的一次游戏开发工作流超过 **60 小时**。已核查记录能支持跨多日
推进和具体阶段交付，没有单独测量 Agent 不间断计算的时长；案例快照中的完整复刻
Goal 仍在继续。实际工作由 Agent、引擎、素材工具和人的决策共同完成，技能提供连接
这些工作的指令契约。

| 实际场景 | Goal 要守住什么 | 可用证据 |
| --- | --- | --- |
| 游戏开发 | 可玩结果、连贯成长、运行检查和构建交付 | [Factory Town Idle case study](cases/factory-town-idle.md)、维护者的 60 多小时经历，以及另行标明来源的[公开游戏实录](field-notes.md#game-development) |
| Android SDK 交付 | 功能、兼容、集成和制品来源，同时控制反复全量验收 | 本地日志核查：14 次 Gradle 合计 9 分 32 秒，最终 SDK 单测约 45 秒；[核查方法与边界](field-notes.md#android-sdk-delivery) |
| 开源技能发布 | 可安装、单一反馈入口、有界跟进、外部维护者门槛 | 已公开的[两轮独立评估](evaluations/2026-10-11-independent-goal-evaluation.zh-CN.md) |

## 用上之后，工作方式有什么变化

- **先把需求写成契约：** 明确结果、范围、证据和结束条件，再启动长任务。
- **每轮都有明确下一步：** 指定一个验收项、预期变化和可恢复的游标。
- **跨轮次还能接续：** Goal Anchor 和决策记录帮助后续回合或接手的 Agent 找回目标。
- **验证有范围、有触发条件：** 修改中定向检查，阶段收尾完成必需的全面验收，复用仍有效的结果。
- **达标就交付：** 准则与交付物满足后结束，阻塞和限额如实报告。

适合游戏开发、功能交付、迁移、调研和发布等多轮任务。短小的一次性请求通常直接写
普通提示即可。技能本身不增加权限，也不负责让宿主一直运行；续跑、工具和上下文恢复
由你的 Agent 运行环境提供。

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
    M --> N["GOAL REALIGNMENT REQUIRED"]
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
| Agent 一直运行却没有进展 | 两次等价的实际尝试既无验收进展也无新证据时，停止并重新对齐 |
| 小改动反复触发全量检查和打包 | 每轮定向检查、阶段交付门槛，以及有效证据复用 |
| 外部依赖让任务无限等待 | 记录下次检查条件和等待检查点；无法恢复时写清阻塞与解锁动作 |

## 三层契约

更多实际工作记录见[英文案例库](cases/README.md)，包括研究交接、SDK 软件交付和开源反馈改进。

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

对于反馈、推广、试点、发布或验证类 Goal，要在执行前明确什么算证据：一个反馈入口、至少
<code>N</code> 条非作者回复，或一个明确的用户群体。同时写出反馈窗口；除非 Goal 明确选择，
作者自己的评论不算真实反馈。

Goal 还会明确**验证策略**：迭代中运行定向检查，实现稳定后集中完成必需的全面检查，
并将结果绑定到相关输入和制品。改动或新证据使结果失效时，重跑受影响的检查；仅修改
报告或回执可复用仍有效的运行结果。耗时检查需有合适的限额，超时的验收项保持未验证。
用户和项目明确要求的验收、发布门槛仍然适用。

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
等待外部条件时，保存待办准则、下次检查时间或事件，以及截止时间。
条件未到时继续其他工作，或交还控制权；下次启动先读回检查点、检查限额，再查询。
正常等待和按时查到“仍未回复”不计为失败尝试。
如果两次等价的实际尝试既无验收进展，也没有相关新证据，停止并输出：
GOAL REALIGNMENT REQUIRED。
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

## 用游戏开发任务试一次

~~~text
用 $goal-instruction-writer 先预览一个 Godot 可玩游戏切片的 Goal。
先展示结果、范围、一轮循环、证据和停止条件。
纳入可玩的核心循环、一条连贯成长路径、实际运行试玩证据、存档读档和可复现构建交付。
固定游戏概念与平台，无关新功能放入延期清单。
迭代中运行定向检查，交付阶段完成要求的全面验收。
跨回合保留 Goal Anchor 和下一游标。
等我确认循环并要求执行后，再开始开发。
~~~

预览确认后，生成可粘贴 Goal，再交给宿主支持的长任务工作流运行。
Goal 是指令契约；启动、恢复和状态命令取决于具体宿主。

## 运行时边界

技能负责设计和审查指令契约。运行时访问权限、工具可用性，以及外部副作用的审批，
仍由宿主 Agent 和用户控制。

遇到外部依赖时，记录未完成准则、证据、下次检查时间或事件，以及截止时间或解锁条件。
条件未到时继续其他可推进的工作，或保留检查点并交还控制权。正常等待不消耗无进展尝试次数；
实际查询和经过的时间仍受宿主总预算约束。详见[等待规则](../references/drift-control.md#scheduled-external-waits)。

## 资源

- [技能入口](../SKILL.md)
- [Goal 契约和可复制骨架](../references/goal-contract.md)
- [循环预览格式和流程图](../references/loop-preview.md)
- [漂移检测和恢复](../references/drift-control.md)
- [编码、研究和开源案例](../references/examples.md)
- [独立 Goal 测试报告](evaluations/2026-10-11-independent-goal-evaluation.zh-CN.md)
- [真实使用、游戏实录与证据边界](field-notes.md)
- [技能分发与投稿指南](distribution.md)
- [可编辑演示视频与来源](../videos/goal-overview/BRIEF.md)
- [Independent Goal evaluation（English）](evaluations/2026-10-11-independent-goal-evaluation.md)
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
