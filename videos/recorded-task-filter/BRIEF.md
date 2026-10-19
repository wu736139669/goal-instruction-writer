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

[Recorded preview validation](validation.json): strict checks passed, including
300 motion samples, six layout samples, and 74 contrast checks. A source-selector
mismatch was repaired before the final passing check.
