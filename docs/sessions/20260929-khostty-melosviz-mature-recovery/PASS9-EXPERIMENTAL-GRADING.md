# Pass 9 — experimental candidates under independent grading

Observed 2026-09-30. Exactly two product programs.

## Melosviz M-E01 baseline is now executable evidence

Diagnostic PR #301 at `d8f75ed78f4dfb7c8078725009276eb8a21f0bd8` ran dedicated workflow 36705844469 successfully. Its baseline job installed the backend and executed `backend/tests/recovery/test_mounted_scene_baseline.py`: **3 passed**. These tests intentionally reproduce the frozen broken contracts (double iteration/shared output and bridge layout mismatch). A passing baseline workflow means reproduction succeeded, not product correctness.

## Melosviz M-E02 candidate

Draft #302 is an untrusted implementation candidate, not accepted work. Independent source review initially failed it because fake MP4 bytes still qualified as render, cache trusted historical outcome metadata, and web assigned a removed `done` state.

The candidate was repaired after that review:
- video-like media must parse through ffprobe or becomes non-production/malformed; malformed WAV is blocked;
- cached historical render labels are revalidated against materialized bytes;
- positive focused fixtures use real decodable WAV;
- web render outcome maps to `produced`, not `accepted`.

A new hard-gate workflow `Experiment - M-E02 contract verification` runs focused contract tests, existing conductor/bridge regressions, and web/desktop TypeScript without continue-on-error. Current candidate head `1f801487871a9d43b2e2a25c51e6c28e2a82ca0e`; workflow 36719757382 queued at observation time.

DCO fails because the experiment branch's many historical commits lack Signed-off-by trailers. That is a contribution-policy failure, not evidence that the product behavior is wrong. History will not be force-rewritten without explicit authorization.

## Khostty K-E03 prior run produced an infrastructure finding

Diagnostic PR #8's dedicated linked-wrapper workflow 36706051964 failed before native build. The checksum-pinned Zig download and checksum verification succeeded, but the composite action wrote the install directory to `GITHUB_PATH` and then called bare `zig version` in the same step. GitHub applies GITHUB_PATH to subsequent steps, so the install step failed with `zig: command not found`. Native build/tests were skipped.

This is an infrastructure failure, not a wrapper failure and not green evidence.

## Khostty K-E03 current candidate

Draft #9's harness was independently reviewed and repaired:
- direct C now exercises the same create/write/resize/render/search/snapshot behavior class as Rust;
- existing ABI-layout and FFI-coverage tests are part of the harness;
- out-of-tree install steps and exact artifact digest are recorded;
- missing-library and lifetime controls remain fail-closed.

The Zig installer now invokes the exact installed binary by absolute path within its install step. A dedicated `Experiment - K-E03 wrapper vs direct C` workflow builds the checksum-pinned candidate native library and executes the harness. Current head `2321282191b30d0862a9864a2096009d0c9a7066`; workflow 36719693538 queued at observation time.

Even a green candidate run is only half of K-E03: a separately built upstream artifact/run and provenance-authenticated comparison remain required.

## Handoff

Experimental implementation is active and independently graded. General developer handoff remains blocked. No experiment branch is authorized to merge from self-authored tests or CodeRabbit status.
