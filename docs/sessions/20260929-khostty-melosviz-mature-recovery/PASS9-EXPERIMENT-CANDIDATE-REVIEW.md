# Pass 9 — experimental candidate review

Observed 2026-09-30. Exactly two product programs.

## Melosviz M-E02 candidate

Draft experiment PR #302 exists and remains UNVERIFIED. It was based on frozen source `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`.

Review found the branch already implemented most of the pass-8 structural contract: scene-indexed results, selector filtering, one-scene RenderSpec projection, isolated output roots, ordered assembly collection, structured CLI/bridge/UI results and focused tests.

Adversarial review then found three additional defects and repaired them on the experimental branch:
1. cache materialization still trusted same-size target bytes; it now replaces from the content-addressed blob rather than treating size equality as identity;
2. cache-hit done events omitted outcome, causing the updated UI to classify valid cached renders as errors; cached outcome is now propagated;
3. cache key identity expected `seg.scene_index`, but storyboard segments generally obtain their index from enumeration. The conductor now projects scene_index/name into the per-scene segment before cache lookup/store/adapter work.

Structured scene results now also carry SHA-256 of accepted artifacts and CLI propagates it. This is evidence identity metadata, not authentication.

No repository test suite or real renderer was executed in this ChatGPT environment. PR #302 must remain draft. The worker-side artifact helper is not promoted into the independent grader.

## Khostty K-E03 candidate

Draft experiment PR #9 exists and remains UNVERIFIED. Branch source was created from frozen Khostty `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`.

Existing candidate adds fail-closed `KHOSTTY_VT_REQUIRE_LINK` and an out-of-tree Rust-vs-direct-C smoke harness. Review tightened the receipt:
- explicit claimed library source revision and origin;
- native artifact SHA-256;
- descriptive wrapper/direct-C LOC and unsafe-token metrics;
- clear statement that both consumers in one run use the same library artifact.

This is important: a single harness run isolates wrapper overhead but is **not** an upstream-vs-Khostty native-library comparison. Separate independently built artifacts/build receipts are required. The current consumer covers create + VT write only; snapshot/search/resize/read/use-after-close/ABI drift/standalone packaging remain open.

Khostty main advanced after the frozen analysis; PR #9 currently targets a newer main. The experiment head remains descended from the frozen source. Any rebase/merge would require fresh semantic/regression review and is not authorized by mergeability.

## Handoff

These are now real draft experimental PRs:
- Melosviz #302: structural M-E02 candidate, source-reviewed but execution-unverified.
- Khostty #9: fail-closed K-E03 evidence harness, source-reviewed but native-unverified.

Neither may merge based on this review. General developer handoff remains blocked. The next highest-value evidence is CI/native execution of these exact heads plus independent oracle/adversarial results.
