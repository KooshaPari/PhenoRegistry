# Pass 10 — experimental execution failures are now evidence

Observed 2026-09-30.

## Melosviz M-E02

PR #302 exact head `fb17f09b50e665039583082a2e89656b05c29621`, dedicated run 36741126607:
- web-delta PASS;
- desktop-delta PASS;
- backend focused contract: 12/13 PASS, one FAIL;
- mounted/backend-regression steps skipped due to fail-fast.

Raw log proves the sole failure was R2 cache invalidation. The synthetic adapter output depended on `marker`; the test changed marker only. SceneCacheKey intentionally fingerprints declared common render inputs + `cache_extra`, not arbitrary scene fields. Thus candidate cache reuse matched its declared contract and the test's expectation was under-specified.

Reviewer correction commit `64115866783383c4be6f94bbbcce02f628cdab2d` changes a real keyed input (`prompt`) plus marker. It does not broaden the cache key or weaken a negative control. New dedicated run 36744451604 is queued.

Architectural follow-up: adapter-specific output dependencies must be declared into cache identity (for example cache_extra or a future adapter dependency projection). A plugin that silently consumes arbitrary unkeyed fields makes selective rerender unsound.

## Khostty K-E03

PR #9 exact head `3c749be20f5a5489dc963d74daf3b8690819577d`, dedicated run 36741131134:
- pinned Zig install PASS;
- Rust toolchain PASS;
- harness syntax PASS;
- exact candidate native `libghostty-vt.a` build PASS;
- native artifact SHA-256: `baf8e58b30f60d12a705a613849e05d338618bdcdc22aaa3b2fda2a35e044250`;
- candidate harness step FAIL;
- upstream build/comparison skipped.

The failure is a harness receipt typo: execution environment sets `KHOSTTY_VT_LINK_KIND`; receipt serialization read `GHOSTTY_VT_LINK_KIND`. The exception occurred at receipt construction after the Rust/direct-C/lifetime/ABI subprocess calls, but because outputs were captured and no receipt was written, their results cannot be reconstructed and receive no credit.

Reviewer correction commit `1edff1a00d6b68cbb297d97926e30030c8844b82` changes only that receipt key. New dedicated run 36744824103 is queued.

This run is still valuable: it proves the exact candidate can build the native static VT artifact under the pinned workflow. It does not prove wrapper correctness, direct-C parity or upstream equivalence.

## Independent grader authority

Melosviz reviewer-owned grader code/policy is stored on the specification branch and pins candidate SHA. GitHub did not automatically schedule the newly introduced workflow from that non-default branch. No independent execution is claimed. A supported external/reviewer runner or default-branch approved workflow entrypoint remains needed for cryptographically/operationally separated grading.

## Status

Experimental failures are preserved rather than rewritten into greens. Both candidates remain unverified. No merge or general developer handoff.
