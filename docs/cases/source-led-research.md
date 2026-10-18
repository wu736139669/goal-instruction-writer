# From a research brief to an implementation-ready handoff

[Case library](README.md) · [Evidence summary](source-led-research-evidence.json)

**Recorded milestone:** October 13, 2026, analysis of a local Factory Town Idle
macOS demo identified in the project as 1.3.6a. This is the research stage of
the same project covered by the [later Godot case](factory-town-idle.md).

The original request needed more than a description of the game's interface:
an implementation effort needed dependable rules, data relationships, source
identities, and a clear account of what still required runtime comparison.
The developer's [public demo page](https://easmussen.itch.io/factory-town-idle-demo)
is the source entry point; the inspected local analysis archive remains private.

## The delivered research artifact

The work produced a searchable local review interface, structured inventories,
definition tables, method-inspection records, and an implementation handoff.
The final report and verification summary record:

| Evidence layer | Recorded result |
| --- | --- |
| Method inventory | 4,920 indexed methods: 4,825 with bodies and 95 without bodies |
| Rule definitions | 160 registered default recipes and 158 research definitions |
| Serialized-object coverage | All 13,875 inventoried Unity objects had extraction records |
| Source preservation | 113 data files matched the original downloaded archive |
| Research tools | Searchable rule/code views, a recipe calculator, and local media catalogs |
| Runtime boundary | Title/main menu observed; complete gameplay and long-run comparison remained open |

The categories answer different questions and are not a combined test total.
The research also distinguished definitions present in the demo package from
features actually reachable in that demo.

## A bounded response to a tool limit

The initial all-members inspection encountered a 64 MiB bound. The next step
changed the work unit: read by declaring type using the same unmodified parser
modules, keeping the original per-batch bound. The project retained the failed
attempt and identified the resulting orchestration as its own output.

That preserved a meaningful next action without silently rewriting the source
or treating a partial scan as full coverage. The handoff also kept static
findings separate from gameplay evidence. An implementation task could then
start from specific rule and save-behavior questions.

## A reusable Goal contract

```markdown
Outcome: hand off an inspectable model of the selected build for implementation.
Acceptance: identify the source build, inventory the selected scope, retain
parsing failures, preserve source bytes, and name unresolved runtime questions.
Loop: inspect one rule or data family, link its evidence, resolve conflicts,
then select the next uncovered family.
Tool failure: change the work unit within the existing resource bound and
retain the failed attempt; do not label partial coverage as complete.
Handoff: provide a searchable artifact, coverage summary, open questions,
and one concrete implementation or runtime-comparison cursor.
End: finish the research milestone when its evidence is reviewable; keep
full gameplay validation and later implementation as separate criteria.
```

The benefit illustrated here is a precise research deliverable with a usable
continuation point. The later game-development timeline supplies separate
implementation evidence; this research checkpoint does not establish a
completed recreation or a skill-specific performance gain.

## Evidence

The [sanitized summary](source-led-research-evidence.json) contains selected
coverage counts, source identities, verification gaps, and input fingerprints.
This public case adds no extracted game code, assets, or raw analysis archive.
