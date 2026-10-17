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
| [SkillBazaar](https://skillbazaar.ai/skills/goal-instruction-writer) | Published as a free skill | Anonymous public access verified; all seven runtime files in the GitHub-backed download match the canonical source bytes |
| [SkillRepo](https://skillrepo.dev/skills/wu736139669/goal-instruction-writer) | Published as a free skill, v0.2.2 | Anonymous public access and seven-file package verified; platform analysis reports grade A, score 89 |
| [Agent Skill Source](https://agentskillsource.com/submit.php) | Submission unavailable from the current region | Actual response: “Your country is not allowed to access this resource” |
| [awesome-codex-skills #337](https://github.com/composio-community/awesome-codex-skills/pull/337) | Existing PR remains open | Updated the existing description with v0.2.2, the English case study, and the demo; no duplicate PR |
| [MCP.Directory](https://mcp.directory/submit-skill) | Existing submission confirmed in the review queue | Actual response: “This skill has already been submitted. We'll review it soon!” |
| [Awesome Skills](https://www.awesomeskills.dev/en/skill/wu736139669-goal-instruction-writer) | Published public directory entry | English detail page, complete instruction body, GitHub-backed install command, and canonical source link verified in the browser |
| [Agent Skill Exchange #119](https://github.com/agentskillexchange/skills/pull/119) | New PR open; awaiting maintainer review | Seven-file skill directory submitted; focused local checks passed; GitHub Actions awaits maintainer approval |
| [Skills Directory](https://skillsdirectory.com/skills/wu736139669-goal-instruction-writer) | Published public directory entry | Live receipt and public detail page verified in the native browser; platform automatic analysis reports grade A, score 100/100 |
| [AI Agents Listing](https://aiagentslisting.com/submit/goal-instruction-writer/success) | Submitted for review | Visible confirmation: “goal-instruction-writer is in the review queue”; repository-only Skill route completed |
| [AI Agent Skill](https://ai-agent-skill.com/contact) | English request prepared; not submitted | Required Turnstile component reports an error after a reload; no submission receipt |
| [Console.dev](https://console.dev/selection-criteria) | English editorial submission sent | Sent-mail recipient, subject, and body verified; editorial selection and publication are pending |
| [DevHunt](https://devhunt.org/login) | English free-listing package prepared; not submitted | GitHub sign-in is waiting for confirmation of the new read-only email authorization; no listing receipt |
| [Product Hunt](https://www.producthunt.com/) | English launch package prepared; not submitted | Cloudflare verification completed; GitHub sign-in is waiting for read-only email and profile authorization; no platform draft or public launch receipt |

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

SkillBazaar imported the public GitHub repository. Its English introduction
includes the maintainer-reported 60+ hour workflow, the inspected stage-delivery
limits, the English game-development case study, and the 36-second demo. The
download contains 60 repository files, including all seven runtime, metadata,
and license files with their canonical source bytes. The optional API-key-based
analysis was not requested.

SkillRepo received the minimal seven-file runtime ZIP: `SKILL.md`, `LICENSE`,
`agents/openai.yaml`, and four reference files. Its published version is 0.2.2.
The platform's automatic analysis reported grade A and score 89. Publication
metadata adds the MIT license, Codex compatibility, source version, homepage,
case-study link, and demo link. The instruction body matches the canonical
source, and all six supporting files match byte for byte.

SkillBazaar and SkillRepo returned HTTP 200 with the expected skill content
without account cookies. Each was explicitly published after import and account
setup.

MCP.Directory received the direct canonical `SKILL.md` URL and reported that the
skill had already been submitted and would be reviewed. This confirms an existing
review entry; it does not establish a new public listing or a second submission.

Awesome Skills now has a public English detail page after the human-verification
handoff. The page includes the instruction body, proportional-verification rules,
a GitHub-backed installation command, and the canonical `SKILL.md` source link.
The directory generates its own agent labels; the canonical package and upstream
installation instructions remain the source of truth for Codex use.

Agent Skill Exchange received a focused PR containing the instruction body and
six supporting files from v0.2.2. The instruction body and supporting-file bytes
are preserved; the entry adapts frontmatter to the catalog schema and appends
canonical Codex installation, usage, and English evidence links. Format, source,
installation-content, and 79-pattern security checks passed locally. The
[upstream validation workflow](https://github.com/agentskillexchange/skills/actions/runs/39006588308)
explicitly awaits maintainer approval before running. Merging the PR and
publishing it to the marketplace are separate maintainer steps.

Skills Directory received the canonical GitHub repository and the explicit root
`SKILL.md` path. After analyzing the source, its authenticated submission page
returned “Skill submitted” and “It’s live in the directory,” with the public
entry linked above. The public detail page was also opened in the native browser
and reports the platform's automatic grade A and score 100/100. The directory's
default installation example targets Claude Code; use the upstream README for
the Codex installation command. The initial GitHub callback returned
`state_mismatch`; a fresh sign-in attempt completed and exposed the form.

AI Agents Listing accepted the canonical public repository through its Agent
Skill tab. The receipt explicitly says the skill is in the review queue and
will become editable once live. The optional email-updates checkbox was left
unchecked. The initial sign-in route was blank; the site's alternate login
entry restored the form and sign-in completed before submission.

AI Agent Skill has a complete English catalog-request draft with the slug, MIT
license, Codex use case, canonical source, case study, and demo. Its required
human-verification component displayed “Turnstile error (often hostname not
allowed). Add this domain in Cloudflare Turnstile.” The error persisted after
one reload. A working verification component is needed to complete this request.

Screenshots and the private tracking link are retained locally. Private tracking
tokens and contact-account data are excluded from this public record.

Console.dev received an English editorial request at the submission address
published in its selection criteria. The sent-mail record contains the expected
recipient, subject, and complete message body. This verifies sending and does
not establish delivery, an editor reply, selection, or publication.

The [developer launch kit](developer-launch-kit.md) contains the English DevHunt
and Product Hunt fields, source, installation command, evidence links, and maker
comment. DevHunt's public FAQ permits a free permanent listing and separately
offers paid launches and boosts; no paid option has been authorized. The
prepared package is not a completed submission. Product Hunt's human verification
has completed. Its GitHub sign-in requests read-only email and profile access;
authorization is the next step before the publishing flow can be used. DevHunt
separately requests read-only email access. Both authorization pages are retained
for the user to review, with screenshots stored privately.

The existing [distribution guide](distribution.md) describes the entry points.
Curated lists with adoption or repository-age gates remain separate from these
direct submissions.
