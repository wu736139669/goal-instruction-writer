# Recorded example: a read-only CLI status filter

One request becomes a Goal, a small implementation, and a verified stop.
This is a **maintainer-operated controlled example**, recorded on 2026-10-19.
It is not an external trial or a before/after performance benchmark.

| Starting point | Recorded result |
| --- | --- |
| Python task-list CLI, no dependencies | `--status open\|done\|all` |
| 9 existing tests | 9 unchanged tests + 10 new tests passed |
| Four iterations and 20 minutes allowed | Two actionable iterations; GOAL COMPLETE |
| Read-only JSON input and exact default output | Input hashes and default output bytes preserved |
| Focused checks, then a stable delivery gate | One focused suite and one final full suite by the agent |

## Inspect the real artifacts

- [Original task](task.md) and exact [Draft](prompts/draft.txt) / [Execute](prompts/execute.txt) prompts.
- [Generated Goal](GOAL.md), unchanged during execution.
- [Starter](starter/) and [completed result](result/), including all tests.
- [Readable transcript](evidence/transcript.md), [structured event log](evidence/events.json),
  and [agent progress](evidence/agent-progress.md).
- [Run summary](evidence/run-summary.json) and [SHA-256 manifest](evidence/files.sha256.json).
- [English transcript-backed video source](../../videos/recorded-task-filter/BRIEF.md).

## Reproduce the recorded code checks

Requires Python 3.9+; no packages, account, or model API are needed to check
these artifacts. From the repository root:

```sh
(cd examples/task-filter/starter && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v)
(cd examples/task-filter/result && PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v)
(cd examples/task-filter/result && python3 tasklist.py tasks.json --status open)
```

Expected counts are 9 and 19. The final command lists tasks 1 and 3, in that
order. Inspect [test_status.py](result/tests/test_status.py) for invalid choices,
empty selections, input bytes, UTF-8, original order, and omitted/all equality.

## Try the skill yourself

Use a fresh temporary copy of starter as the agent workspace. Copy task.md to
TASK.md, initialize Git if your host requires it, and install the skill locally.
For an exact skill revision, get the seven runtime files from commit
`a288550a5970f2412f1b4aa15ee4ef0df8c33107` into
`.agents/skills/goal-instruction-writer/`. Keep that copy frozen.

Submit the [Draft prompt](prompts/draft.txt), inspect GOAL.md, then submit the
[Execute prompt](prompts/execute.txt). The recorded run used Codex CLI 0.159.2
with configured model label gpt-6.1-sol, workspace-write, approval never,
no connected MCP servers, and no native Goal runtime. Your host/model may
produce a different contract or implementation.

The sandbox began without a Git HEAD; the agent recovered from that lookup
using hashes. Read the transcript for actual failures and evidence reuse.

## What this example establishes

The recorded agent followed a bounded contract, preserved frozen files, checked
changed behavior, completed the required regression gate, and stopped. A small
stdlib CLI cannot establish reliability across large projects or prove a timing
improvement. Captured Draft and Execute durations were 100.100 and 183.858
seconds, excluding operator preparation and the gap between invocations.
Agent progress uses a separate conservative inspection allowance.

Public evidence replaces local paths, excludes reasoning and host startup
configuration warnings, and fingerprints omitted multilingual support reads.
The video is an edited replay of recorded transcript excerpts, with idle time
condensed; it is not an unedited desktop recording.

[Share a real trial](../../docs/try-it.md) · [Case library](../../docs/cases/README.md)
