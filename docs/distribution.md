# Sharing and submitting this skill

Checked on 2026-10-17. The public GitHub repository is the source of truth;
directories help people find it. A GitHub release alone does not mean a
third-party curator has accepted the skill.

## 1. Direct installation

```bash
npx skills add wu736139669/goal-instruction-writer \
  --skill goal-instruction-writer -g -a codex -y
```

This path does not need a directory listing. Keep `SKILL.md`, the referenced
files, license, install instructions, and versioned releases available.

## 2. skills.sh

The [official FAQ](https://www.skills.sh/docs/faq) says skills are listed through
anonymous CLI installation telemetry. Publish the GitHub source, share the
installation command, and let real users install it. Rankings reflect tracked
installations. There is no separate listing submission required by that FAQ.

Do not manufacture installs to move a ranking. Discoverability and adoption
should come from real use and useful feedback.

## 3. Curated GitHub collections

An existing submission is already open:
[composio-community/awesome-codex-skills #337](https://github.com/composio-community/awesome-codex-skills/pull/337).
It links to this repository in Meta & Utilities and includes installation
instructions. As of the check date it is open, not merged. A maintainer owns
the acceptance decision; do not open a duplicate PR.

For another curated collection:

1. Read its current README and contribution instructions.
2. Check whether it already lists this skill and whether it accepts external
   repository links or expects a copied skill directory.
3. Add one concise entry in the right category; include the source and license.
4. Follow its validation requirements, then submit one focused PR.
5. Record the PR URL and follow up only for new information or a review request.

Suggested entry:

```markdown
- [goal-instruction-writer](https://github.com/wu736139669/goal-instruction-writer) — Preview agent loops and draft durable Goals with acceptance evidence, drift control, proportional verification, and clear stop conditions. Used in multi-hour game-development and software-delivery workflows.
```

## 4. Other discovery sites

[SkillsMP](https://skillsmp.com/) describes itself as an index of public GitHub
skills. Indexing does not imply certification. Its public home page does not
document a universal manual submission endpoint; check its current author/docs
surface before assuming that a form, star threshold, or publishing API exists.
This release does not claim a SkillsMP listing.

## Submission material

| Material | Location |
| --- | --- |
| Source and installation | [README](../README.md) |
| 中文介绍 | [README.zh-CN.md](README.zh-CN.md) |
| Real use cases and evidence limits | [Field notes](field-notes.md) |
| Short animated preview | [GIF](../assets/goal-overview.gif) |
| Full demonstration | [v0.2.0 video](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.0/goal-overview.mp4) |
| Release | [v0.2.0](https://github.com/wu736139669/goal-instruction-writer/releases/tag/v0.2.0) |
| Feedback | [Discussion #1](https://github.com/wu736139669/goal-instruction-writer/discussions/1) |

## 中文：怎么投到第三方

- **直接分发：** 发 GitHub 链接和上面的安装命令，用户无需等待合集收录就能安装。
- **skills.sh：** 按官方 FAQ，通过真实 CLI 安装的匿名统计自动进入目录和排行。
- **Awesome 合集：** 读规则、确认未重复收录、按分类改 README 或加入目录，再提一个聚焦 PR。
  本技能已经有 #337，等待维护者处理即可。
- **其他市场：** 先确认它是自动索引还是明确投稿；没有核实的入口，不写成已经提交或收录。

准备材料时，把实际效果、演示、安装和证据放在同一个页面。60 多小时经历标明是维护者
的使用报告；游戏实录和流程示意分开标注，方便别人理解和复现自己的工作流。
