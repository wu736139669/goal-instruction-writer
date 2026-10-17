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

A second submission is open at
[Agent Skill Exchange #119](https://github.com/agentskillexchange/skills/pull/119).
Its [contribution guide](https://github.com/agentskillexchange/skills/blob/main/CONTRIBUTING.md)
requires a complete `skills/<slug>/` entry with catalog metadata, installation
instructions, and a source-backed use case. The seven-file entry starts at the
`listed` tier; maintainers handle review, workflow approval, merging, and
marketplace publication. PR creation alone does not complete those steps.

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

## 4. Direct submission portals

These submission pages were inspected on 2026-10-17. The current receipts and
outstanding platform gates are recorded in [submission status](submission-status.md).

| Portal | Submission method | Requirements shown by the portal |
| --- | --- | --- |
| [OpenAgentSkill](https://www.openagentskill.com/submit) | Scan a GitHub repository and submit selected skills to a review queue | Valid `SKILL.md`; zero-star repositories and anonymous submissions accepted |
| [Skillboard](https://www.skillboard.lol/submit) | Suggest a public GitHub repository or skill directory | Valid frontmatter and a license permitting indexing/attribution |
| [agentskill.sh](https://agentskill.sh/submit) | Import a GitHub repository or direct `SKILL.md` URL | Import must finish successfully; platform rate limits apply |
| [SkillMD.ai](https://skillmd.ai/submit/) | Submit a GitHub source, Markdown, or ZIP, then review and publish the resulting draft | Contact email; inspect the generated files before publishing |
| [SkillBazaar](https://skillbazaar.ai/dashboard/new) | Import a public GitHub skill, review the English listing, category, and tags, then publish | Author account; valid `SKILL.md`; optional AI analysis does not gate ordinary publication |
| [SkillRepo](https://skillrepo.dev/for-publishers) | Upload the runtime ZIP, save it, then publish the private skill to the public catalog | Free Publisher account; valid frontmatter; complete platform analysis and explicit Publish step |
| [Agent Skill Source](https://agentskillsource.com/submit.php) | Submit metadata, source URL, execution type, runtime, and contact details | Public GitHub source; supports Prompt Only and OpenAI Codex |
| [MCP.Directory](https://mcp.directory/submit-skill) | Submit the direct GitHub `SKILL.md` URL with a name, category, short description, and contact email | Description limit is 300 characters; an existing-submission response means review is pending |
| [Awesome Skills](https://www.awesomeskills.dev/en/submit) | Submit a GitHub repository or skill-directory URL | Complete the Cloudflare human-verification challenge before submitting; the separate newsletter prompt is optional |
| [Skills Directory](https://app.skillsdirectory.com/submit) | Sign in, submit a GitHub repository, and optionally specify the `SKILL.md` path | Public repository with a valid skill; platform analyzes metadata and bundle files, then reports publication after validation |
| [AI Agents Listing](https://aiagentslisting.com/submit) | [Sign in](https://aiagentslisting.com/auth/login), choose Agent Skill, and submit the GitHub URL; see the [official guide](https://aiagentslisting.com/blog/how-to-submit-your-ai-agent) | Public GitHub repository or skill folder; repository-only route; review is separate from submission |
| [AI Agent Skill](https://ai-agent-skill.com/contact) | Send an English catalog request to the editors with the public skill URL and use case | Contact name, email, role, request type, and working human verification |

Submitting a source is distinct from a completed import, public listing, or
maintainer acceptance. Preserve the actual receipt and report its state.

## 5. Other discovery sites

[SkillsMP](https://skillsmp.com/) describes itself as an index of public GitHub
skills. Indexing does not imply certification. Its public home page does not
document a universal manual submission endpoint; check its current author/docs
surface before assuming that a form, star threshold, or publishing API exists.
This release does not claim a SkillsMP listing.

## Developer-tool launches and editorial review

- [Console.dev](https://console.dev/selection-criteria) accepts developer-tool
  submissions by email at the editorial address published on that page. It
  selects a small number of tools for review; a sent email does not imply
  selection or publication.
- [DevHunt](https://devhunt.org/faq) supports a free permanent tool listing after
  sign-in. Its weekly launch, boosted launch, and sponsorships are separate paid
  options. Use the free listing unless a paid option is explicitly requested.
- [Product Hunt](https://help.producthunt.com/en/articles/17350772-launch-guide)
  supports a maker-led launch with a tagline, description, gallery, demonstration,
  and maker comment. Review the current account and publishing requirements;
  prepared copy, a saved draft, a scheduled launch, and publication are distinct
  states.

The [English developer launch kit](developer-launch-kit.md) provides reusable
submission fields and evidence links. Actual receipts and remaining gates are
recorded in [submission status](submission-status.md).

## Submission material

| Material | Location |
| --- | --- |
| Source and installation | [README](../README.md) |
| 中文介绍 | [README.zh-CN.md](README.zh-CN.md) |
| Real use cases and evidence limits | [Field notes](field-notes.md) |
| Short animated preview | [GIF](../assets/goal-overview.gif) |
| Full demonstration | [v0.2.0 video](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.0/goal-overview.mp4) |
| Release | [v0.2.2](https://github.com/wu736139669/goal-instruction-writer/releases/tag/v0.2.2) |
| Submission receipts and platform gates | [Submission status](submission-status.md) |
| Developer-tool listings and launch copy | [Developer launch kit](developer-launch-kit.md) |
| Feedback | [Discussion #1](https://github.com/wu736139669/goal-instruction-writer/discussions/1) |

## 中文：怎么投到第三方

- **直接分发：** 发 GitHub 链接和上面的安装命令，用户无需等待合集收录就能安装。
- **skills.sh：** 按官方 FAQ，通过真实 CLI 安装的匿名统计自动进入目录和排行。
- **Awesome 合集：** 读规则、确认未重复收录、按分类改 README 或加入目录，再提一个聚焦 PR。
  本技能已经有 #337，等待维护者处理即可。
- **其他市场：** 先确认它是自动索引还是明确投稿；没有核实的入口，不写成已经提交或收录。

准备材料时，把实际效果、演示、安装和证据放在同一个页面。60 多小时经历标明是维护者
的使用报告；游戏实录和流程示意分开标注，方便别人理解和复现自己的工作流。
