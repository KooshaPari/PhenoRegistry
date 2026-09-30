# Pass 9 — experimental implementation candidates

Observed 2026-09-30. Exactly two product programs.

## Melosviz M-E02 candidate

Draft implementation PR: https://github.com/KooshaPari/Melosviz/pull/302
Candidate head after self-review: `67ea65176a5261142b60556ede585230c57f9077`; frozen baseline `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`.

The candidate:
- consumes constructor/render only_scenes with explicit-render precedence and pre-dispatch range validation;
- projects the full RenderSpec to one scene before calling adapters that currently own their own internal loop;
- isolates each outer scene invocation under a dispatch-specific output root;
- keys results by scene index rather than scene type;
- collects accepted real-media artifacts, including qualified cache hits, into ordered assembly input;
- puts typed outcome into done telemetry;
- updates compose dispatch to use its existing assignment index;
- adds focused same-backend/selector/cardinality/assembly/event tests and updates old conductor assertions.

This is deliberately an experimental compatibility break in `per_scene_results`; source review found compose as a real consumer and patched it. Further consumers/tests/serialization must be executed. No product tests have run in this environment, so the candidate remains UNVERIFIED.

## Khostty K-E03 candidate

Draft implementation PR: https://github.com/KooshaPari/Khostty/pull/9
Candidate head after self-review: `695d6f9e56d9e5869467f8ab44733ecbe8e5433b`; frozen analysis baseline `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`.

The candidate:
- adds opt-in `KHOSTTY_VT_REQUIRE_LINK` fail-closed mode to Rust build.rs;
- when an explicit GHOSTTY_VT_LIB is supplied in evidence mode, refuses fallback if that exact file is absent;
- supplies an out-of-tree Rust consumer + direct C comparator harness against the same native artifact;
- records native artifact SHA-256/source SHA and a missing-library negative control.

Self-review caught a potential false negative-control: the original harness could name a missing explicit library but build.rs might fall back to an existing checkout-local library. The candidate was tightened so evidence mode rejects a missing explicit subject instead of falling back.

No native library build or harness execution occurred here. The candidate is UNVERIFIED.

## Handoff state

Developer agents now have concrete candidate PRs to execute rather than greenfield instructions. They should test/falsify these candidates, not rewrite the architecture unless evidence forces it. General developer handoff remains blocked.
