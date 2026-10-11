# Goal Instruction Writer 独立评估

## Test input

> 帮我让这个开源技能获得第一批真实反馈。先不要发消息，先预览循环；之后再生成一个可执行 Goal。需要考虑 README、GitHub Discussion、上游收录 PR，但我没有其他社区账号，不能注册新账号，也不能无限重复催促。

测试按 Preview-first 规则执行：先产出循环设计，再模拟用户确认，生成可粘贴的 Goal。评估只模拟两轮只读检查，不发消息、不创建账号、不修改仓库或 GitHub 状态。

## Skill references used

- [SKILL.md](https://github.com/wu736139669/goal-instruction-writer/blob/main/SKILL.md)：Preview-first、三层契约、漂移分类、限额和终态。
- [references/goal-contract.md](https://github.com/wu736139669/goal-instruction-writer/blob/main/references/goal-contract.md)：Objective、Anchor、证据、循环和终态字段。
- [references/drift-control.md](https://github.com/wu736139669/goal-instruction-writer/blob/main/references/drift-control.md)：每轮对齐记录、Phase Gate、无进展阈值。
- [references/loop-preview.md](https://github.com/wu736139669/goal-instruction-writer/blob/main/references/loop-preview.md)：预览顺序、分支和交接规则。
- [references/examples.md](https://github.com/wu736139669/goal-instruction-writer/blob/main/references/examples.md)：外部维护者门槛案例。

## Preview

### 暂定结果与假设

暂定结果是：只使用现有 GitHub 仓库、Discussion 和上游收录 PR，让技能达到可真实试用、可收集反馈、且状态可审计的状态。这里把“第一批真实反馈”定义为至少一条来自非作者的具体回复；作者自己的评论不算反馈。上游 PR 的合并权属于维护者，不能假设可获得。

### 起始状态与 Goal Anchor

- **Baseline**：仓库 `main` 当前提交 `df22ba2`；README 已为英文主文档并有中文翻译；CI 最近一次运行成功。
- **目标标准**：C1 文档和安装路径可验证；C2 有一个公开反馈入口；C3 上游 PR 状态和确切外部依赖已记录；C4 至少一条非作者具体反馈。
- **冻结范围**：一个技能仓库、一个 GitHub Discussion、现有上游 PR；不注册新账号、不 mass posting、不重复催促、不把维护者权限当作已有权限。
- **首个游标**：只读检查仓库、Actions、Discussion 和 PR 的当前状态。

### 一轮循环

1. **Inspect**：读取仓库修订、文档入口、CI、Discussion、PR 和上一次游标。
2. **Select**：只选择一个未验证标准，写明目标标准、预期证据变化和范围理由。
3. **Act**：在测试中只做只读检查；在获准执行时，最多做一个聚焦的文档或反馈入口更新。
4. **Verify**：记录链接、提交、Action 结果、PR 状态或反馈正文。
5. **Classify**：标记为 `ON_TARGET`、`SIDE_QUEST` 或 `DRIFTED`。
6. **Record**：保存本轮证据、剩余差距、决定和下一游标。

### 分支、门禁和终止

- C1/C2/C3 证据增加：`ON_TARGET`，继续选择下一个未验证标准。
- 发现有价值但不属于四个标准的推广渠道：`SIDE_QUEST`，记录后延期。
- 无法指出当前动作推进哪个标准、范围静默扩大、或连续两轮没有标准进展：停止并输出 `GOAL PAUSED: realignment required`。
- PR 可合并但仍为 open：记录 `upstream maintainer review required`，不重复催促。
- 没有非作者回复：在一次有界的反馈窗口后输出 `GOAL TIMEBOXED: awaiting first external feedback`，不把作者评论算作反馈。
- 所有标准和证据满足：`GOAL COMPLETE`。
- 每 3 轮、每个里程碑以及任何公开发布/消息前重读 Anchor；本测试两轮后执行一次终态门禁。
- 测试上限为 2 次只读迭代；可执行 Goal 上限为 3 次工作单元、1 个 Discussion、最多 1 次有实质变化的维护者跟进。

### 模拟确认

模拟用户确认以上循环，并接受“至少一条非作者具体回复”作为 C4；随后生成最终 Goal。预览阶段不执行外部副作用。

## Final Goal

以下是确认后生成的可执行 Goal：

```markdown
# Goal: Collect the first external feedback without scope drift

## Objective
Using only the existing GitHub repository and account, make the skill easy to try,
keep one public feedback path reviewable, capture at least one concrete response
from someone other than the author, and record the current status of the existing
upstream listing PR. Do not create accounts, mass-post, or repeatedly ping
maintainers.

## Goal anchor
- Outcome: the skill has a usable feedback path, at least one non-author
  feedback response is captured, and the upstream PR status has a durable record.
- Criteria: C1 documentation/install evidence; C2 one feedback entry point;
  C3 upstream PR status and unblock; C4 one non-author concrete response.
- Frozen scope: this repository, one GitHub Discussion, and the existing upstream
  PR only; no new accounts, channels, or silent scope expansion.
- Current phase: baseline and first feedback.

## Baseline and scope
- Baseline: `main` at `df22ba2`, current README/docs, CI run, Discussion #1,
  and upstream PR #337.
- Allowed scope: inspect the named GitHub surfaces; edit this repository's
  README/docs if a focused gap is found; maintain the existing Discussion; read
  or update the existing PR only when the host explicitly authorizes an outbound
  message.
- Authority: Preview is read-only. Do not create accounts or merge the upstream
  PR. A public message requires separate explicit outbound authorization.

## Acceptance criteria
- [ ] C1. README and install path are clear and verified by a repository link and
      successful CI/validator evidence.
- [ ] C2. One public Discussion or equivalent existing feedback thread explains
      what to try and how to report a concrete result.
- [ ] C3. The existing upstream PR has a recorded URL, state, mergeability, and
      exact maintainer unblock; do not claim merge without maintainer evidence.
- [ ] C4. At least one non-author reply records a concrete use case, result,
      defect, or improvement with a link or timestamp. An author-only comment
      does not satisfy C4.

## Execution loop
Repeat one bounded work unit at a time:
1. Inspect the named surfaces and the last durable cursor.
2. Select exactly one open criterion, its expected evidence delta, and its scope reason.
3. Act within the allowed scope and authority.
4. Verify the result and capture the evidence link, revision, or status.
5. Classify the iteration as `ON_TARGET`, `SIDE_QUEST`, or `DRIFTED`.
6. Record the delta, remaining gap, decision, and next cursor.

## Drift control
- Re-read the Goal Anchor before any public message, version change, or new
  submission, and at every phase gate.
- Park unrelated channels, promotional ideas, and feature work in a deferred list.
- If no criterion moves for two equivalent iterations, or the Anchor/scope changes
  without owner approval, stop with `GOAL PAUSED: realignment required`.
- If the only remaining action is an upstream maintainer merge, stop contacting
  the maintainer and preserve the exact unblock.

## Limits and no-op rule
- Use at most 3 work units, 1 existing Discussion, and 1 targeted follow-up
  only when new evidence or an explicit owner decision justifies it.
- Do not repeat a message, submission, or check without material new evidence.
- If the feedback window closes with no non-author response, stop; do not invent
  feedback or claim completion.

## Termination
- `GOAL COMPLETE` when C1-C4 are all verified and the report is available.
- `GOAL BLOCKED: upstream maintainer review required` when the clean PR is the
  only remaining dependency and the exact unblock is recorded.
- `GOAL TIMEBOXED: awaiting first external feedback` when the bounded feedback
  window ends before C4; report the existing evidence and the PR dependency.
- `GOAL PAUSED: realignment required` after a drift trigger or owner pause.
- `GOAL STOPPED: authority boundary` if the next action would require an
  ungranted account, message, merge, or other external permission.

## Reporting
After each iteration and at termination, report the label, target criterion,
expected and actual evidence, remaining gap, deferred side quests, and next
cursor or exact unblock.
```

## Iteration log

| Iteration | Target / expected delta | Read-only evidence | Classification | Decision |
| --- | --- | --- | --- | --- |
| 1 | C1; prove the current README/install path is reviewable and the package is validated. | `main` is clean at `df22ba2`; README is English-first with a Chinese document; validation run `38112648047` completed successfully. | `ON_TARGET` | Keep C1 verified. The existing Discussion was also observed as a feedback entry point, but no external reply was counted. |
| 2 | C3; record PR state and exact external unblock. | Upstream PR #337 is `OPEN`, `mergeable=true`, `mergeable_state=clean`, with one author comment and no review comments. Only the upstream maintainer can merge. Discussion #1 still has only the author's comment, so C4 is open. | `ON_TARGET` | Record the maintainer gate; do not repeat a follow-up. End at the two-iteration test limit. |

No iteration was classified as `SIDE_QUEST` or `DRIFTED`; the test did not perform any action outside the frozen read-only scope.

## Evidence

- Repository: [wu736139669/goal-instruction-writer](https://github.com/wu736139669/goal-instruction-writer), `main` at `df22ba2`; local status was `main...origin/main`.
- CI: [Validate skill run 38112648047](https://github.com/wu736139669/goal-instruction-writer/actions/runs/38112648047), completed with `success`.
- Release: [v0.1.0](https://github.com/wu736139669/goal-instruction-writer/releases/tag/v0.1.0).
- Feedback entry point: [Discussion #1](https://github.com/wu736139669/goal-instruction-writer/discussions/1). It asks users for a redacted example or proposed loop; its only current comment is by the repository author.
- External gate: [awesome-codex-skills PR #337](https://github.com/composio-community/awesome-codex-skills/pull/337), open and clean, awaiting maintainer review/merge.

## Terminal result

Primary test terminal:

`GOAL TIMEBOXED: awaiting first external feedback`

The external submission carries a separate dependency:

`GOAL BLOCKED: upstream maintainer review required`

The test must not claim `GOAL COMPLETE`: the repository has a public feedback path, but no non-author response is currently evidenced, and the upstream PR is not merged.

## Strengths

- Preview mode makes the loop, branches, evidence, drift gates, and terminal states reviewable before execution.
- The Goal Anchor freezes the outcome, criteria, scope, authority, and phase.
- Every iteration names a target criterion, expected evidence delta, and scope reason.
- `ON_TARGET`, `SIDE_QUEST`, and `DRIFTED` have distinct follow-up behavior.
- External maintainer ownership is represented as a blocker instead of an invitation to retry indefinitely.
- The final Goal preserves the user's account and no-repeat constraints and leaves a durable cursor/report.

## Gaps and smallest fix

The phrase “第一批真实反馈” is ambiguous between “a public feedback entry point exists” and “a non-author response exists.” The current skill provides the fields needed to resolve it but does not force a numeric feedback threshold. The smallest improvement is to add a required Preview decision:

`Feedback evidence: entry point only | at least N non-author responses`

Then copy that decision into C4 and the terminal rule. This evaluation chose `N=1`. Without that explicit choice, a run could incorrectly mark the existing author-only Discussion as complete.


