# An Android SDK release: evidence, compatibility, and handoff

[Case library](README.md) · [Evidence summary](android-sdk-delivery-evidence.json)

**Recorded milestone:** version 0.7.0 software delivery, October 17, 2026.
The project is anonymized; the inspected engineering records remain private.

The task was to deliver an Android SDK and reference UI with integrity checks,
signed export/recipient verification, controlled voice-operation paths, and
versioned annotations. A usable delivery also needed compatible APIs, an AAR
consumed by a separate host, and packages tied to the checked source.

## The result

The recorded milestone reached `COMPLETE_SOFTWARE_DELIVERY`. Its acceptance
report and receipt identify:

| Delivery evidence | Recorded result |
| --- | --- |
| SDK unit tests | 505 in Debug and 505 in Release; no failures, errors, or skips |
| Reference UI unit tests | 21 per variant; no failures, errors, or skips |
| Python tooling tests | 21 |
| API compatibility | Six historical snapshots preserved; the new snapshot frozen |
| Separate AAR consumer | Debug and R8 builds passed; consumed AAR bytes matched the delivered AAR |
| Source provenance | 303 source, build, and API inputs matched the named source commit |
| Handoff | Eight artifact types, software reports, retained failure logs, and a download-verification receipt |

The integrity checks covered modified or missing originals, altered or
incomplete signed bundles, extra entries, and untrusted signatures. Controlled
voice-operation checks covered permissions, cancellation, session binding,
confirmation, and rejected commands. These are software-path observations.
Android instrumentation APKs were built but not executed; physical-device,
live recognition, and production-service acceptance remained separate.

## What the verification cost actually was

The archive contains both canonical logs and duplicate copies of failed logs.
Counting each identical log once gives:

| Measurement | Observed duration |
| --- | --- |
| Final SDK Debug suite-duration sum | 24.541 seconds |
| Final SDK Release suite-duration sum | 20.073 seconds |
| Final complete root check | 90 seconds |
| Five broad root checks, including one failure | 435 seconds: 7 minutes 15 seconds |
| All 14 recorded Gradle invocations | 572 seconds: 9 minutes 32 seconds |

Suite-duration sums are not wall-clock session time. Debug and Release counts
describe two variants, not twice as many distinct test scenarios.

Some repeated checks followed real compiler, compatibility-checker, and
cancellation fixes. The evidence supports selecting checks by the change; it
does not support declaring every rerun wasteful or claiming a measured speedup.

## A reusable Goal contract

```markdown
Outcome: deliver a compatible SDK and a separate host consuming the same AAR.
Acceptance: affected behavior checks, historical API compatibility, artifact
identity, independent consumer build, and a reviewable handoff.
Loop: choose one failure or unmet criterion, make one bounded correction,
verify its effect, and preserve the remaining delivery cursor.
Verification: use focused checks while editing. Refresh evidence that depends
on changed source or artifacts, including the consumer of a changed AAR.
Delivery gate: complete the required broader checks once implementation is
stable; distinguish software acceptance from pending native/device acceptance.
End: report the verified delivery boundary and any exact remaining dependency.
```

This connects implementation, validation, and packaging to the same outcome.
A later iteration can see which evidence still applies and which input changed,
instead of treating each small edit as a complete new release cycle.

## Evidence

The [sanitized summary](android-sdk-delivery-evidence.json) records the source
identity, aggregate test results, deduplicated build durations, and fingerprints
of the inspected report, receipt, and check archive. This audit read existing
records and did not rerun the SDK. See the
[verification strategy](../../SKILL.md#verification-strategy) for the reusable rule.
