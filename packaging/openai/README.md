# Goal Instruction Writer

An OpenAI skills-only plugin for previewing execution loops and writing durable
Goals. It packages the existing v0.2.5 skill and its supporting references.

Use it when a coding, game-development, or research task needs several iterations
with a stable outcome, reviewable evidence, and a recoverable next step.

## Try it

**Preview:**

> Preview a Goal for a playable Godot game slice with save/load and build evidence.
> Show the loop, branches, scope, and stop conditions. Do not execute it.

**Draft:**

> Draft a Goal for fixing a CSV importer that truncates quoted multiline fields.
> Preserve the existing record model, use focused checks, and define completion.

**Audit:**

> Audit this Goal: "Keep improving the app until it is perfect. Run every check
> after each edit, and keep adding useful features." Identify scope drift,
> unbounded work, and unnecessary repeated verification. Propose a bounded revision.

Preview mode produces a reviewable loop and waits for confirmation before the
final Goal. Writing a Goal does not authorize executing the underlying project.

## Runtime boundary

The package contains instructions, references, metadata, and icons. The host
supplies tools, permissions, persistence, and continuation. A future check time
in a Goal is a checkpoint for the host; it does not create a timer. Live
wait/resume behavior remains untested.

The workflow is intended for multi-stage tasks. Ordinary one-shot requests
usually do not need this skill. No account or API key is required by the package.

## Source and evidence

- [Canonical source](https://github.com/wu736139669/goal-instruction-writer)
- [English case library](https://github.com/wu736139669/goal-instruction-writer/blob/main/docs/cases/README.md)
- [English demonstration](https://github.com/wu736139669/goal-instruction-writer/releases/download/v0.2.4/goal-overview-en.mp4)
- [Support](https://github.com/wu736139669/goal-instruction-writer/issues)
- [Privacy and data handling](PRIVACY.md)

`SOURCE.json` records the committed skill revision and the SHA256 of packaged
files. The skill and references are copied byte for byte from that revision.
Repository development tools, demo source, and private submission receipts are
outside this runtime package. MIT license; see `LICENSE`.
