# Recorded task-filter storyboard

flow: automation
storyboard: no

Six short scenes authored inline. All terminal text is sourced in data.json.

## Frame 1

status: built
frame_id: frame01
src: compositions/frames/frame01.html
start: 0
duration: 14
blueprint: none; composed from waterfall-entry and GSAP discrete timeline sets
reference: transcript-scroll-artifact-reveal (evidence-to-artifact arc; no camera moves)
beat: One request. A checkable finish. A read-only Python CLI. Add one status filter while preserving the default output and the input file.
source: examples/task-filter/task.md

## Frame 2

status: built
frame_id: frame02
src: compositions/frames/frame02.html
start: 14
duration: 15
blueprint: none; composed from waterfall-entry and GSAP discrete timeline sets
reference: transcript-scroll-artifact-reveal (evidence-to-artifact arc; no camera moves)
beat: The agent writes the contract. The generated Goal names acceptance evidence, permitted files, focused checks, a delivery gate, and explicit stop states.
source: examples/task-filter/GOAL.md

## Frame 3

status: built
frame_id: frame03
src: compositions/frames/frame03.html
start: 29
duration: 16
blueprint: none; composed from waterfall-entry and GSAP discrete timeline sets
reference: transcript-scroll-artifact-reveal (evidence-to-artifact arc; no camera moves)
beat: Keep the implementation small. The existing loader and formatter stay in place. The agent adds status choices, filtering, and focused coverage.
source: examples/task-filter/result/tasklist.py

## Frame 4

status: built
frame_id: frame04
src: compositions/frames/frame04.html
start: 45
duration: 15
blueprint: none; composed from waterfall-entry and GSAP discrete timeline sets
reference: transcript-scroll-artifact-reveal (evidence-to-artifact arc; no camera moves)
beat: Check the changed behavior first. The agent runs the focused status-filter suite once and compares default/all output with the captured original bytes.
source: examples/task-filter/evidence/focused-check.json

## Frame 5

status: built
frame_id: frame05
src: compositions/frames/frame05.html
start: 60
duration: 15
blueprint: none; composed from waterfall-entry and GSAP discrete timeline sets
reference: transcript-scroll-artifact-reveal (evidence-to-artifact arc; no camera moves)
beat: Run the delivery gate once. 9 unchanged tests plus 10 new tests. Source and tests retain the focused-check hashes; report-only edits reuse valid results.
source: examples/task-filter/evidence/delivery-check.json

## Frame 6

status: built
frame_id: frame06
src: compositions/frames/frame06.html
start: 75
duration: 15
blueprint: none; composed from waterfall-entry and GSAP discrete timeline sets
reference: transcript-scroll-artifact-reveal (evidence-to-artifact arc; no camera moves)
beat: Deliver the result. Then stop. 2 of 4 iterations used. Inspect the request, Goal, code, tests, and transcript. Try one real task and share what happened.
source: examples/task-filter/evidence/operator-review.json + final agent message


# Visual revision 2 — 2026-10-19

User note: "Do these pictures/videos look a bit ugly?"
Diagnosis: six repetitive text-heavy layouts with little hierarchy or momentum.
Change: reduce 90s to 48s; display headlines 106–184px; one evidence focus per
scene; switch between dark, paper, and lime using one palette. Keep all public
text English and retain real artifact provenance. Earlier frames remain as the
published v1 source; the following frames are the current cut.

## Frame 7

status: animated
frame_id: v2-hook
src: compositions/v2/v2-hook.html
start: 0
duration: 6
blueprint: none; rules: waterfall-entry, svg-path-draw, css-marker-patterns
beat: Give your agent a finish line
source: Editorial hook; no performance or adoption claim

## Frame 8

status: animated
frame_id: v2-contract
src: compositions/v2/v2-contract.html
start: 6
duration: 8
blueprint: none; rules: waterfall-entry, svg-path-draw, css-marker-patterns
beat: Turn a request into a contract
source: examples/task-filter/GOAL.md C1, C7, execution loop

## Frame 9

status: animated
frame_id: v2-code
src: compositions/v2/v2-code.html
start: 14
duration: 10
blueprint: none; rules: waterfall-entry, svg-path-draw, css-marker-patterns
beat: One small change
source: examples/task-filter/result/tasklist.py actual selected source lines

## Frame 10

status: animated
frame_id: v2-proof
src: compositions/v2/v2-proof.html
start: 24
duration: 8
blueprint: none; rules: waterfall-entry, svg-path-draw, css-marker-patterns
beat: Focused first. Full suite last
source: examples/task-filter/evidence/focused-check.json; delivery-check.json

## Frame 11

status: animated
frame_id: v2-result
src: compositions/v2/v2-result.html
start: 32
duration: 9
blueprint: none; rules: waterfall-entry, svg-path-draw, css-marker-patterns
beat: Goal complete
source: Operator review actual stdout + final captured agent report; separate sources

## Frame 12

status: animated
frame_id: v2-close
src: compositions/v2/v2-close.html
start: 41
duration: 7
blueprint: none; rules: waterfall-entry, svg-path-draw, css-marker-patterns
beat: Try one real task
source: Repository identity and existing public install command
