# Pass 9 — implementation candidate review

Observed 2026-09-30. Exactly two product programs.

## Melosviz M-E02 candidate

Draft PR #302, head `0af1e6df103f9f107ac990d012db76f8c4295313`, source baseline `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`.

The candidate is directionally aligned with the recovered contract: scene-indexed results, effective selector filtering, one-scene RenderSpec projection, isolated output roots, accepted-artifact collection, typed live-render done events, and structured bridge/UI consumption.

It is **BLOCKED**, not accepted:
1. cache materialization still treats equal byte size as identity, so the OLD!/NEW! counterexample survives;
2. cache-hit done events omit outcome while the new UI treats done-without-render-outcome as error;
3. malformed nonempty media remains accepted by the old size/WAV-only helper;
4. focused tests do not yet execute the independent media oracle, cache mutation, restart/edit R2, or all critical mutations;
5. qgate baseline run 36712427824 failed during coverage generation; DCO run 36712427295 failed Signed-off-by; studio/CI were not complete at review time.

This is exactly why work completion/PR existence does not equal product acceptance.

## Khostty K-E03 candidate

Draft PR #9, head `695d6f9e56d9e5869467f8ab44733ecbe8e5433b`. It was created from source `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`; current main at review is `882d6cd4aa7b5f9f9bffc5fb0a8b4d70460c90e6`, so the candidate is 2 commits behind and 3 ahead.

Useful changes: fail-closed `KHOSTTY_VT_REQUIRE_LINK`; out-of-tree Rust consumer; direct C comparator; missing-library negative control; supplied native artifact SHA-256 in receipt.

It is **BLOCKED**:
1. evidence hashes `GHOSTTY_VT_LIB`, but build.rs turns that into parent-directory + `-lghostty-vt`; it does not prove the exact named file is what the linker/runtime loaded when siblings are present;
2. consumer covers only create/write/free, not the full wrapper contract;
3. direct C uses the same supplied library, useful for wrapper overhead but not a separately built current-upstream comparator;
4. candidate must reconcile current main before qualification;
5. no native K-E03 receipt exists and CI/Test were pending.

## SOTA implication for Melosviz

Fresh official OTIO documentation still positions OTIO as editorial cut/interchange with clips, timing, tracks, transitions, markers and metadata; canonical OTIO JSON is lossless while other adapters may be lossy. This strengthens the prior decision to use OTIO as an editorial projection/interchange rather than invent a generic EDL or force it to own Melosviz's full product truth.

Fresh OpenUSD documentation describes references/layers as compositional scene-description mechanisms with overrides and explicit composition semantics. That remains appropriate for a hybrid/spatial projection experiment, not evidence that USD should replace music/editorial/product state.

Neither external primitive repairs the immediate M-E02 execution/evidence defects; those remain product-specific orchestration responsibilities.

## Handoff gate

Both candidates are now real implementation candidates with exact heads and explicit failing criteria. Neither is accepted. Developer agents should repair/falsify the listed blockers on the candidate branches, not start a new architecture or weaken the grader.
