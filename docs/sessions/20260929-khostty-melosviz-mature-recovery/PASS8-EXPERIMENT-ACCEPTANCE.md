# Pass 8 — critical experimental acceptance contracts

Observed 2026-09-30.

## Melosviz

Further source tracing confirms assembly is disconnected from rendering. `collected_paths` is initialized from caller-supplied `segment_paths` and never appended/extended by live render or cache-hit artifacts. Mounted generate supplies no segment_paths. Fixing result keys alone would therefore leave assembly broken.

Done events also do not carry the already-computed typed outcome. A malformed/placeholder/job-spec/unavailable adapter result can still emit the same done state. Done must be treated as execution telemetry, never acceptance.

M-E02 now has eight critical acceptance dimensions: selector, iteration cardinality, result identity, artifact identity, assembly connectivity/order, execution-vs-acceptance events, structured bridge/UI propagation, and restart/edit R2 evidence. Required mutation controls are specified product-locally.

## Khostty

Rust wrapper build semantics create a verification trap: build.rs intentionally allows a missing native libghostty-vt during cargo check, warning and omitting link directives. Therefore check/typecheck green cannot qualify wrapper integration.

Go/Rust defaults are also checkout-relative; Python discovers/loads an existing library; WASM builds via the repo Zig project. Standalone package consumption is not established merely by wrapper source/tests.

K-E03 now requires exact native library identity, linked consumer execution, ABI/use-after-close controls, direct-upstream comparator, and a clean out-of-tree consumer. Rust is first; four language wrappers are not four independent reasons to own a terminal fork.

## Gate

Both products remain READY FOR EXPERIMENTAL IMPLEMENTATION, NOT GENERAL DEV HANDOFF. The experimental contracts are now strong enough that implementation agents should not need to invent acceptance semantics for M-E02 or K-E03.
