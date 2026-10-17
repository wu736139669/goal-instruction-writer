# Goal Instruction Writer demonstration

A 36-second, silent, bilingual product demonstration for v0.2.0. English titles,
Simplified Chinese supporting captions, and real Moonlit Kingdom footage.
The editable source is included so the demonstration can be inspected and
updated alongside the skill.

## Watch

- [Full MP4](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.0/goal-overview.mp4)
- [README animated excerpt](../../assets/goal-overview.gif)
- [Four-scene contact sheet](../../assets/goal-overview-contact-sheet.jpg)

## Edit or render

Requirements: Node.js 22+, FFmpeg, and the pinned HyperFrames CLI. From this
directory:

```bash
npm run check
npm run render -- --quality high --fps 30 --workers 2 --output renders/goal-overview.mp4
```

`index.html` mounts the four scene templates in `compositions/frames/` and owns
the gameplay video at global seconds 8–18. Its geometry matches the empty
media stage in frame 2. Edit media timing or placement in `index.html`; edit
scene type, layout, and reveals in the corresponding template. Timelines are
seekable and use local assets; no voice or music service is needed.

| Frame | Time | Content |
| --- | --- | --- |
| 01-long-run | 0–8s | Attributed 60+ hour maintainer report |
| 02-game | 8–18s | Separately identified real gameplay excerpt |
| 03-loop | 18–28s | Clearly labeled Goal workflow illustration |
| 04-verify | 28–36s | Verification strategy and repository CTA |

The README GIF is a ten-second editorial excerpt: seconds 2–8 followed by
seconds 8–12 from the full render. Gameplay inside the full MP4 stays at the
source recording's original speed.

## Evidence and asset rights

Read [PROVENANCE.md](PROVENANCE.md) and the repository's
[field notes](../../docs/field-notes.md) for the distinction between the
maintainer's duration report, recorded gameplay, and the workflow illustration.

Fonts were downloaded from Google Fonts and stored locally. Each family ships
its OFL license in `assets/fonts/`; `sources.json` records URLs and SHA256.
The Noto Sans SC file is a Google Fonts text subset containing the Chinese
captions. GSAP 3.14.2 is vendored with its original license header; see the
[GSAP standard license](https://gsap.com/standard-license/). Gameplay remains
the maintainer's project material; its inclusion is for this demonstration
and does not separately relicense the game or its art under the skill's MIT
license.

[validation.json](validation.json) records the checks actually performed.
