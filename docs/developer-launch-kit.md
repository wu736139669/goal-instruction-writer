# Developer launch material

Prepared on 2026-10-17 for Goal Instruction Writer v0.2.2. All public submission copy and examples in this file are in English.

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

A public English case follows a multi-day Factory Town Idle Godot port through analysis, playable systems, and a local candidate with Mac and Android packages. The maintainer reports an estimated 60+ hour longest workflow. The case documents inspected stages and records that the full Goal was still active at the snapshot.

Free under the MIT license. Latest skill release: v0.2.2.

## Installation

```bash
npx skills add wu736139669/goal-instruction-writer --skill goal-instruction-writer -g -a codex -y
```

## Evidence and media

- [English game-development case](https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/cases/factory-town-idle.md)
- [Verification field notes](https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/field-notes.md)
- [36-second workflow demo](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.0/goal-overview.mp4)
- [Animated preview](../assets/goal-overview.gif)
- [Social preview](../assets/social-preview.png)
- [Feedback discussion](https://github.com/wu736139669/goal-instruction-writer/discussions/1)

The demo is a workflow illustration with a separately identified gameplay clip.
The maintainer-reported 60+ hour figure is an estimate of a long workflow.
The linked case identifies inspected stages and records that the full project
Goal was still active at the snapshot. It is not a measured claim about
uninterrupted runtime or a completed full-game recreation.

## Console.dev editorial submission

The English submission was emailed to the editorial address published in the
[selection criteria](https://console.dev/selection-criteria). The sent-mail
record confirms sending; editorial acceptance and publication remain separate
steps.

**Subject:** Tool submission: Goal Instruction Writer — durable Goals for Codex

The submission links to the source, case study, demo, and verification field
notes. The sender account and private mail identifiers are retained outside
this public repository.

## DevHunt

The [official FAQ](https://devhunt.org/faq) distinguishes a free permanent tool
listing from a paid launch. Use the free listing for this submission. Paid
launches, boosts, and sponsorships have not been requested.

The shared fields, detailed description, and existing media above form the
submission package. See the [submission status](submission-status.md) for the
actual receipt and current platform gate.

## Product Hunt

Use the [official launch guide](https://help.producthunt.com/en/articles/17350772-launch-guide)
for the current fields and publishing flow.

**Tagline (48/60 characters):** Keep long-running Codex work tied to one outcome

**Description (192/260 characters):**

Write durable Goals for Codex: preview the loop, preserve acceptance evidence, control drift, use focused verification, and define clear completion conditions. Free, open source, MIT licensed.

### Maker comment

Hi everyone! I maintain Goal Instruction Writer, the Codex skill I use to plan and review long agent workflows.

The problem that led to it was simple: a task can keep producing activity while drifting away from the requested outcome. Another recurring issue was repeatedly running broad test suites after small changes.

The skill first previews the execution loop, then writes a Goal with an observable outcome, acceptance evidence, scope and authority boundaries, checkpoints, drift controls, and completion conditions. It also makes verification proportional to the change, so focused iteration checks and delivery gates have clear roles.

I've used this approach in multi-day game-development work. My longest workflow is estimated at 60+ hours. The linked English case follows inspected stages of a Factory Town Idle Godot port through Mac and Android local candidate deliveries; the full project Goal was still active at that snapshot.

The repository includes install instructions, examples, field notes, and a 36-second workflow demo. Continuation, tools, permissions, and recovery come from your agent runtime.

I'd love practical feedback: what kinds of long tasks make your agent lose the original goal, and which completion conditions are hardest to express?

### Publication state

Review the source and media labels before publishing. A prepared package is
distinct from a saved platform draft or a public launch.
