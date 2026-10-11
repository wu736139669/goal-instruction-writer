# Goal Instruction Writer

一个帮助 AI agent 写出可执行 Goal 指令的 Codex skill。它把模糊任务整理成三层契约：

1. **目标（Goal）**：要交付什么可观察结果，如何验收。
2. **循环（Loop）**：每轮如何检查、选择、执行、验证并记录进展。
3. **结束（Termination）**：什么时候完成，什么时候阻塞、暂停、超时或停止。

这样可以避免“继续做下去”“直到满意”这类没有边界的指令，也能让另一个 agent 从最后的游标继续工作。

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
- **终态明确**：完成、阻塞、暂停、超时/预算耗尽、停止分别处理。
- **不越权**：技能只整理用户已经授权的范围，不会凭空增加权限或外部副作用。

## 输出结构

技能通常会返回：

1. 简短设计说明、假设和高价值待确认项；
2. 一段可直接粘贴使用的 Goal 指令；
3. 对已有指令的审计意见（如果用户要求 refine 或 audit）。

## License

MIT，见 [`LICENSE`](LICENSE)。
