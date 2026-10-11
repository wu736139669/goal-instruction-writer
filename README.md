# Goal Instruction Writer

一个帮助 AI agent 写出可执行 Goal 指令的 Codex skill。它把模糊任务整理成三层契约：

1. **目标（Goal）**：要交付什么可观察结果，如何验收。
2. **循环（Loop）**：每轮如何检查、选择、执行、验证并记录进展。
3. **结束（Termination）**：什么时候完成，什么时候阻塞、暂停、超时或停止。

这样可以避免“继续做下去”“直到满意”这类没有边界的指令，也能让另一个 agent 从最后的游标继续工作。

## 先看循环，再生成 Goal

对于长任务，可以先让技能只输出循环预览，不直接生成最终指令：

```text
Use $goal-instruction-writer in Preview mode. 先展示循环的具体步骤、分支、
防偏航检查和结束条件，等我确认后再生成最终 Goal。
```

预览会展示起始状态、一次迭代、成功/失败/旁支/偏航分支、证据、阶段闸门和终态。
用户确认后，技能才把预览转成可执行 Goal；预览阶段不会执行外部操作。

## 长任务如何防止偏航

技能会为长循环建立一个不可静默修改的 **Goal Anchor**，并要求每轮写清楚：

- 这轮推进哪个验收标准；
- 预期会出现什么新证据；
- 为什么仍在允许范围内。

每轮结束标记为 `ON_TARGET`、`SIDE_QUEST` 或 `DRIFTED`。旁支任务进入 deferred list，
不直接扩张 Goal；连续两轮没有验收进展、目标/范围被悄悄改变，或无法说明下一步如何服务
Anchor 时，暂停并要求重新对齐。技能还会在每 3–5 轮、阶段边界和高风险操作前执行 phase gate。
详细流程见 [`references/drift-control.md`](references/drift-control.md)。

## 安装

把 `goal-instruction-writer` 目录复制到 Codex 技能目录：

```bash
cp -R goal-instruction-writer "${CODEX_HOME:-$HOME/.codex}/skills/"
```

然后可以显式调用：

```text
Use $goal-instruction-writer to turn this task into a clear goal with a bounded loop and explicit stop conditions.
```

技能默认支持自动发现。`SKILL.md` 是运行时入口；详细字段契约在
[`references/goal-contract.md`](references/goal-contract.md)，示例在
[`references/examples.md`](references/examples.md)。

## 设计原则

- **结果优先**：目标描述交付物、行为、决策或已验证事实，而不是活动清单。
- **证据绑定**：每个验收标准都要对应可复核证据。
- **有界循环**：每轮都产生可观察进展，并有时间、预算、尝试次数或工作单元上限。
- **拒绝空转**：同一失败没有新信息就不重复；重复阻塞要报告原因和解锁条件。
- **防止偏航**：每轮绑定验收标准和预期证据；旁支任务延后；阶段闸门重新读取 Anchor。
- **先审循环**：长任务先展示循环和分支，再根据确认结果生成最终 Goal。
- **终态明确**：完成、阻塞、暂停、超时/预算耗尽、停止分别处理。
- **不越权**：技能只整理用户已经授权的范围，不会凭空增加权限或外部副作用。

## 输出结构

技能通常会返回：

1. 简短设计说明、假设和高价值待确认项；
2. 一段可直接粘贴使用的 Goal 指令；
3. 对已有指令的审计意见（如果用户要求 refine 或 audit）。

## License

MIT，见 [`LICENSE`](LICENSE)。
