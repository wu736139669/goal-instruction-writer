# Goal Instruction Writer English demonstration

A 36-second, silent, English-only overview. All titles, supporting explanations,
case labels, and footers are English. The editable source is included so the
demonstration can be inspected and updated alongside the skill.

## Watch

- [Full English MP4](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.4/goal-overview-en.mp4)
- [English README animated excerpt](../../assets/goal-overview-en.gif)
- [Four-scene contact sheet](../../assets/goal-overview-en-contact-sheet.jpg)

## Edit or render

Requirements: Node.js 22+, FFmpeg, and the pinned HyperFrames CLI. From this
directory:

```bash
npm run check -- --strict
npm run render -- --quality delivery --fps 30 --workers 2 --output renders/goal-overview-en.mp4
```

`index.html` mounts the four scene templates in `compositions/frames/`. Edit
scene type, layout, and reveals in the corresponding template. Timelines are
seekable and use local fonts and GSAP; no voice, music, or network asset service
is needed. Keep every visible word English when updating this composition.

| Frame | Time | Content |
| --- | --- | --- |
| 01-long-run | 0–8s | Attributed 60+ hour maintainer estimate and evidence boundary |
| 02-game | 8–18s | Illustrated Factory Town Idle checkpoints and local stage delivery |
| 03-loop | 18–28s | Clearly labeled Goal workflow illustration |
| 04-verify | 28–36s | Verification strategy and repository CTA |

The README GIF excerpts seconds 1–7, 13.8–17.8, 25–27.8, and 33–36 from the
full render, without speeding those ranges up. It is a 15.8-second overview
of all four scenes, not a time-lapse of a long agent run.

## Evidence and asset rights

Read [PROVENANCE.md](PROVENANCE.md) and the repository's
[field notes](../../docs/field-notes.md). The case timeline summarizes audited
records; the full game recreation Goal was still active at its checkpoint.

The bilingual v0.2.0 video remains in the release archive. Its separately
identified Moonlit Kingdom source clip and Chinese font subset remain unused
historical assets and are not mounted in the English composition. That game
material is not separately relicensed under the skill's MIT license.

Fonts were downloaded from Google Fonts and stored locally with their OFL
licenses in `assets/fonts/`; `sources.json` records URLs and SHA256. GSAP 3.14.2
is vendored with its original license header; see the
[GSAP standard license](https://gsap.com/standard-license/).

[validation.json](validation.json) records the checks actually performed.
