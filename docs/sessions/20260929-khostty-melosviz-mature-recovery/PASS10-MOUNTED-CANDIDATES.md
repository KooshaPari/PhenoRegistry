# Pass 10 — mounted consumer propagation candidates

Observed 2026-09-30.

## Melosviz candidate #302

Head `0af1e6df103f9f107ac990d012db76f8c4295313`.

The experimental repair now reaches the mounted consumers rather than stopping at conductor internals:
- conductor: selector, scene-indexed results, one-scene adapter projection, accepted artifact collection, typed done outcome;
- compose: assignment index drives exact conductor scene;
- CLI: structured scene outcomes and `assembly_state=produced_unverified|not_attempted`; old `assembly_ok` object-existence green removed;
- bridge: returns CLI structured manifest; flat filesystem glob removed;
- web StudioConsole: maps by scene_index/outcome/artifact, rejects non-render outcomes; SSE bare done without render outcome becomes error/review rather than green;
- release Electrobun view: parses CLI manifest and no longer marks every queue entry done merely because subprocess returned.

Focused tests cover same-backend cardinality, selector precedence/range, assembly inputs and done outcome; bridge test no longer pre-creates the output it claims to verify.

Candidate remains unverified. GitHub CI for the latest head is queued/pending. An earlier intermediate head showed several successful noncritical workflows, but studio-pipeline was still queued and DCO failed; cancellations/successes on superseded heads are not candidate acceptance.

## Khostty candidate #9

Head `695d6f9e56d9e5869467f8ab44733ecbe8e5433b`.

Evidence-mode native-link guard and Rust-vs-C out-of-tree harness remain the candidate. Current Khostty main advanced beyond the frozen analysis snapshot, but the touched existing files checked here (`khostty-vt/build.rs`, `examples/screen_dump.rs`) have identical Git blobs between frozen source and current main. This reduces, but does not eliminate, base-drift risk.

CI is pending; Nix skipped is explicitly not a green. Native harness execution is still required.

## Gate

These are real implementation candidates, not developer instructions alone. Neither is accepted until exact-head execution and independent grading. No merge/release was performed.
