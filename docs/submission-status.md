# Directory submission status

Recorded on 2026-10-17 for
[Goal Instruction Writer](https://github.com/wu736139669/goal-instruction-writer),
version 0.2.2. Submission copy and the case-study links are in English.

| Destination | Verified state | Evidence / next gate |
| --- | --- | --- |
| [OpenAgentSkill](https://www.openagentskill.com/submit) | Saved for human review | Receipt `63bac6ed`; page explicitly distinguishes review from publication |
| [Skillboard](https://www.skillboard.lol/submit) | Submitted for review | Visible confirmation: “Thanks – submitted for review.” |
| [agentskill.sh](https://agentskill.sh/submit) | Import not completed; rate limited | Actual response: “Too many submissions. Please try again in an hour.” |
| [SkillMD.ai](https://skillmd.ai/skills/goal-instruction-writer/) | Published as a free skill | Public page and six-file download verified; all six files match the canonical source bytes |
| [Agent Skill Source](https://agentskillsource.com/submit.php) | Submission unavailable from the current region | Actual response: “Your country is not allowed to access this resource” |
| [awesome-codex-skills #337](https://github.com/composio-community/awesome-codex-skills/pull/337) | Existing PR remains open | Updated the existing description with v0.2.2, the English case study, and the demo; no duplicate PR |

OpenAgentSkill's review notes flag executable/script files, package scan bounds,
and command execution for deeper review. This is a saved review request, not an
automatic listing or safety approval. The runtime skill consists of Markdown
instructions and references; the repository also contains editable demo media
and supporting development files.

SkillMD's initial GitHub submission created a draft containing a description and
source link rather than the complete runtime. Before publication, its contents
were replaced with the canonical `SKILL.md`, all four `references/*.md` files,
and the MIT license (`LICENSE.md` in that package). The downloaded ZIP contains
exactly those six files, with the original source bytes preserved. The public
page returned HTTP 200 and the expected title without account cookies.

Screenshots and the private tracking link are retained locally. Private tracking
tokens and contact-account data are excluded from this public record.

The existing [distribution guide](distribution.md) describes the entry points.
Curated lists with adoption or repository-age gates remain separate from these
direct submissions.
