# Contributing

Thanks for helping make long-running agent work easier to keep on target.

## Start with a use case

Before changing the wording, describe the task that exposed the problem:

- What was the original request?
- Where did the agent loop, drift, or stop incorrectly?
- What evidence would have made the next action reviewable?

Use [Discussions](https://github.com/wu736139669/goal-instruction-writer/discussions)
for questions and broad design ideas. Use an issue for a reproducible bug or a
focused improvement.

## Change guidelines

- Keep the three-layer contract intact: observable Goal, bounded Loop, legal
  Termination.
- For long-running workflows, preserve the Goal Anchor and drift controls.
- Prefer a small rule or example that fixes a real decision over generic advice.
- Do not silently expand the skill's authority or add external side effects.
- Update the relevant reference or example when changing the entrypoint.

## Review checklist

- The frontmatter name and description remain valid.
- Preview mode still stops before emitting the final Goal.
- Every new acceptance rule has observable evidence.
- Drifted, blocked, paused, and timeboxed work remain distinguishable.
- Markdown links and code fences render correctly.
