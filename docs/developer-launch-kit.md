# Developer launch material

Original submission copy recorded on 2026-10-17; case-library links added on
2026-10-18. The canonical skill release is v0.2.4. The recorded DevHunt and
Product Hunt submissions use English copy, an English case study, and three
English-only gallery images.

## Shared listing fields

- **Name:** Goal Instruction Writer
- **Tagline:** Keep long-running Codex work tied to one outcome
- **Source and installation:** https://github.com/wu736139669/goal-instruction-writer
- **Pricing:** Free
- **License:** MIT
- **Categories:** AI Coding, AI Agents, Open Source

A free, open-source Codex skill that previews execution loops and writes durable Goals with acceptance evidence, drift controls, focused verification, and clear completion conditions.

## Detailed description

Goal Instruction Writer helps developers turn a request into an inspectable execution contract: an observable outcome, acceptance evidence, a bounded loop, checkpoints, and completion conditions. It supports drafting and auditing Goals for coding, game development, research, and other multi-stage work.

The skill keeps each iteration tied to the original outcome and uses focused checks during development, reusable valid evidence, and broader checks at delivery gates. It is an instruction package; the host agent runtime supplies continuation, permissions, and tools.

The skill supports continuation after time or event triggers through its generated Goal instructions. These preserve the pending criterion, next check time/event, and deadline; independent work can continue while that criterion waits. A host timer, relevant event, or authorized message can provide the next invocation with access to the saved checkpoint. The agent reads that checkpoint and checks limits, querying the pending dependency only when its recorded trigger is met. The host supplies persistence and invocation, including automatic delivery at the requested time; a live wait/resume transition has not yet been validated. See [active work and waiting](../README.md#active-work-and-waiting).

A public English case follows a multi-day Factory Town Idle Godot port through analysis, playable systems, and a local candidate with Mac and Android packages. The maintainer reports an estimated 60+ hour longest workflow. The case documents inspected stages and records that the full Goal was still active at the snapshot.

Free under the MIT license. Latest skill release: v0.2.4.

## Installation

```bash
npx skills add wu736139669/goal-instruction-writer --skill goal-instruction-writer -g -a codex -y
```

## Evidence and English media

- [English case library: implementation, research, SDK delivery, and open-source feedback](https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/cases/README.md)
- [English game-development case](https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/cases/factory-town-idle.md)
- [Verification field notes](https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/field-notes.md)
- [Feedback discussion](https://github.com/wu736139669/goal-instruction-writer/discussions/1)

| Material | PNG | Editable SVG source |
| --- | --- | --- |
| Square thumbnail, 240 x 240 | [Thumbnail](../assets/launch-logo-240.png) | [Logo source](../assets/launch-logo.svg) |
| Larger square logo, 512 x 512 | [Logo](../assets/launch-logo.png) | [Logo source](../assets/launch-logo.svg) |
| Workflow, 1600 x 1000 | [Gallery image 1](../assets/developer-launch/01-workflow.png) | [Source](../assets/developer-launch/01-workflow.svg) |
| Proportional verification, 1600 x 1000 | [Gallery image 2](../assets/developer-launch/02-verification.png) | [Source](../assets/developer-launch/02-verification.svg) |
| Inspected Godot-port stages, 1600 x 1000 | [Gallery image 3](../assets/developer-launch/03-field-case.png) | [Source](../assets/developer-launch/03-field-case.svg) |

These submissions use the new English-only still images. The earlier bilingual
video remains in the release history. The maintainer-reported 60+ hour figure
is a workflow estimate; the case study and gallery identify the inspected
stage deliveries and record that the full project Goal was still active at
the snapshot.

## Console.dev editorial submission

The English submission was emailed to the editorial address published in the
[selection criteria](https://console.dev/selection-criteria). An automated reply
acknowledged the message and said submissions would be reviewed for the next
newsletter. Editorial selection and publication remain pending.

**Subject:** Tool submission: Goal Instruction Writer — durable Goals for Codex

The sender account and private mail identifiers are retained outside this
public repository. Use the English gallery above for new coverage.

## DevHunt

The [free tool page](https://devhunt.org/tool/goal-instruction-writer) has been
created and verified in the browser and by an anonymous HTTP 200 response. It
contains the English description, thumbnail, three gallery images, free pricing,
source links, and maker comment.

The platform assigned the free weekly-promotion queue date **May 13, 2031**.
The permanent page is available now; a near-term weekly launch, newsletter
promotion, and boosts are separate paid options. No paid option was selected.

### Maker comment (731/1000 characters)

I built Goal Instruction Writer to keep long Codex workflows tied to the requested outcome. It previews the loop and writes Goals with acceptance evidence, checkpoints, drift controls, focused verification, and clear completion conditions.

My longest workflow is estimated at 60+ hours. The English case documents stages of a multi-day Godot port through Mac and Android local candidates; the full Goal was still active at that snapshot.

Free, MIT licensed. Your agent runtime supplies continuation, tools, and permissions. Practical feedback is welcome.

Source: https://github.com/wu736139669/goal-instruction-writer
English case: https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/cases/factory-town-idle.md

## Product Hunt

The launch was [successfully scheduled](https://www.producthunt.com/products/goal-instruction-writer/goal-instruction-writer/prelaunch)
for **October 18, 2026 at 12:01 AM Pacific / 07:01 UTC / 15:01 Asia/Shanghai**,
the earliest date offered by the form. The receipt said “Successfully
Scheduled!” and the pre-launch dashboard reports “Scheduled.”

- [Product page](https://www.producthunt.com/products/goal-instruction-writer)
- [Launch preview](https://www.producthunt.com/products/goal-instruction-writer?launch=goal-instruction-writer)
- [Owner edit page](https://www.producthunt.com/posts/goal-instruction-writer/edit)
- [Official launch guide](https://help.producthunt.com/en/articles/17350772-launch-guide)

The required-information checklist reached 100%. The form received a square
thumbnail, three English gallery images, Developer Tools and Artificial
Intelligence tags, open-source and free-pricing selections, the maintainer as
maker, and the English first comment below. Investor-introduction fields were
left blank. A scheduled launch is distinct from being live or featured.

**Tagline (48/60 characters):** Keep long-running Codex work tied to one outcome

**Description (400/500 characters in the inspected form):**

Turn long Codex tasks into durable Goals with observable outcomes, acceptance evidence, checkpoints, drift controls, and clear completion conditions. Preview the loop before execution. Use focused checks during development and broader verification at delivery gates. Free, MIT licensed. Includes an English case study of a multi-day Godot port; the maintainer reports a longest workflow of 60+ hours.

### Maker comment

Hi everyone! I maintain Goal Instruction Writer, the Codex skill I use to plan and review long agent workflows.

The problem that led to it was simple: a task can keep producing activity while drifting away from the requested outcome. Another recurring issue was repeatedly running broad test suites after small changes.

The skill first previews the execution loop, then writes a Goal with an observable outcome, acceptance evidence, scope and authority boundaries, checkpoints, drift controls, and completion conditions. It also makes verification proportional to the change, so focused iteration checks and delivery gates have clear roles.

I've used this approach in multi-day game-development work. My longest workflow is estimated at 60+ hours. The linked English case follows inspected stages of a Factory Town Idle Godot port through Mac and Android local candidate deliveries; the full project Goal was still active at that snapshot.

The repository includes install instructions, examples, field notes, and an English case study. Continuation, tools, permissions, and recovery come from your agent runtime.

I'd love practical feedback: what kinds of long tasks make your agent lose the original goal, and which completion conditions are hardest to express?

Source and installation: https://github.com/wu736139669/goal-instruction-writer
English case study: https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/cases/factory-town-idle.md

## Receipt handling

The [submission status](submission-status.md) records the current outcome for
each destination. Account details and screenshots remain in private local
records; only the intentional public promotional assets are committed here.
