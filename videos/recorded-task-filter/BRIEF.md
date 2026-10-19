> Current delivered cut: **visual revision 2, 48 seconds**. The 90-second brief below
> is preserved as history; the dated revision section describes the current cut.

# Recorded task-filter demo

A 90-second, silent, English-only 1920×1080 video for the public GitHub README.
It replays excerpts from a real maintainer-operated Codex CLI run on 2026-10-19.
It is **an edited transcript replay with condensed idle time**, not an unedited
screen recording or a speedup benchmark. Operator review is labeled separately.

The original skill is pinned to a288550a5970f2412f1b4aa15ee4ef0df8c33107.
[Case and evidence](../../examples/task-filter/README.md) are the source of truth.
The example ends after one focused suite and one final full suite; it does not
establish independent usage or general reliability on large tasks.

The older 36-second overview illustrates the concept. This new video presents
actual artifacts and captured check output. Commands appear intact; no invented
terminal runs or simulated agent output are used. Line reveals are editorial
replay cues. Scene 6 is the separate maintainer CLI review plus the agent's
recorded terminal state. Local paths are normalized in the linked evidence.

## Source and reproduction

The visual terminal markup/token styles adapt the HyperFrames registry
`code-terminal-run` component, installed with hyperframes@0.8.174. Typing,
generic sample commands, random cadence, and panel drift were removed. Each
scene uses explicit deterministic output cues, with provenance in data.json.
No remote images, audio, or paid generation services are used.

```sh
npm run check -- --strict
npx --yes hyperframes@0.8.174 preview --background
```

Keep the Studio preview running for final review. Final MP4 export follows
preview approval. The expected duration is 90 seconds; verify the exported
file with ffprobe before publishing. No MP4 is claimed until that check passes.

[Version 1 preview validation](validation-v1.json): strict checks passed, including
300 motion samples, six layout samples, and 74 contrast checks. A source-selector
mismatch was repaired before the final passing check.


## Visual revision 2 — 2026-10-19 (approved cut)

User feedback: the images/video look unattractive. This revision replaces the
uniform documentation slides with a 48-second visual cut in the same project.
The earlier 90-second brief and validation-v1.json remain historical records;
index.html and data-v2.json now describe the current cut. The approved MP4 export is linked below.

The story uses a strong typographic hook, three contract boundaries, actual
source close-up, test-count evidence, a full-frame result, and one install/Star
CTA. Complete logs remain in the public case. This is still an edited record
replay, not an unedited screen recording. The code-line highlight adapts the
installed HyperFrames registry code-highlight measured-band pattern, with
transforms instead of a width tween. It does not simulate typing or execution.

Revision 2 [strict validation](validation.json) passed: lint, runtime, layout,
motion, and contrast. Source/example behavior was unchanged; no code tests or
agent run were repeated for the visual revision.


## Approved export — 2026-10-19

The maintainer approved visual revision 2 and its direct use. The delivered
English-only, silent MP4 is 48.000 seconds, 1920×1080, H.264 at 30fps with
1,440 frames. HyperFrames 0.8.174 used drawelement capture with hardware GPU.
The actual decoded frames at 3, 19, 37, and 45 seconds were visually reviewed.

[Watch the delivered MP4](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.4/goal-recorded-task-filter-en.mp4) · [Media checksums and verification](render-result.json).

The README GIF is derived from this verified MP4 at 960×540 and 15fps, preserving
the full 48-second duration. The poster comes from its 3-second frame. These
assets are in ../../assets/. The earlier 36-second conceptual overview remains
available in release history. The recorded case and its runtime evidence stay
unchanged apart from their new media entry points.
