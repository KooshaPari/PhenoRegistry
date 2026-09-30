# Pass 9 — experimental implementation candidate review

Observed 2026-09-30. Exactly two product programs. This supersedes the earlier pass-9 snapshot as branch candidates changed during review.

## Melosviz M-E02 candidate — draft #302

Baseline remains `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`. The branch is an UNVERIFIED/DO-NOT-MERGE implementation candidate.

Structurally implemented on the candidate:
- effective only-scenes filtering and validation;
- scene-indexed result identity;
- one-scene RenderSpec projection so existing whole-spec adapters receive one scene per conductor invocation;
- isolated per-dispatch roots;
- live/cache result outcome + artifact digest;
- accepted worker-render artifacts collected in storyboard dispatch order for assembly;
- equal-size cache target is overwritten rather than size-trusted;
- structured CLI manifest and bridge consumption rather than filesystem guessing;
- focused tests for selector/cardinality/assembly/cache/event identity.

### Adversarial review corrections

Review found two additional candidate bugs not present in the initial PR description:
1. Electrobun queue entries are 1-based while conductor `scene_index` is 0-based. The candidate directly mapped them, shifting/missing scene results.
2. Both UIs mapped worker `outcome=render` to `done`, which would recreate a false green: worker-produced media is not independent acceptance.

The branch was amended. Electrobun now maps `entry.index - 1`; both human surfaces distinguish `produced` from `accepted`; acceptance progress counts only explicit accepted state. No candidate path currently mints accepted by itself. Reviewed file blobs after correction:
- Electrobun view: `885ce0fe80bc890899a3cd3746571325909d4c70`;
- web StudioConsole: `9bc020a139adde0b660cd8d94447627eba895cc6`.

GitHub PR metadata lagged these branch writes during review, so an older PR head must not be used as the reviewed candidate identity until refreshed. Re-read branch/head + file blobs before execution.

### Still blocked

No focused/existing suite execution in this environment, real renderer, mounted bridge, independent oracle against the exact candidate, R1→edit/restart→R2, or mutation campaign. Worker-side artifact validation/provenance remains non-acceptance. CI/qgate/DCO observations from the earlier review remain historical until rerun against the current candidate.

## Khostty K-E03 candidate — draft #9

Recovery baseline: `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`. PR base has advanced to `882d6cd4aa7b5f9f9bffc5fb0a8b4d70460c90e6`; execution receipts must bind recovery baseline, actual PR base/head and native artifact source independently.

The fail-closed `KHOSTTY_VT_REQUIRE_LINK` mode remains directionally correct. The out-of-tree harness now exercises Rust wrapper create/write, resize, render-state dimensions, search, snapshot encode/restore, a missing-library fail-closed control, and a compile-fail lifetime misuse control. Current reviewed harness blob: `4abe3b48a60df79f7e3942869d174a9c923485f5`.

The compile-fail ownership test is intentionally preferred over manufacturing native use-after-free UB.

### Still blocked

- Direct C and Rust use the same supplied library artifact, so this isolates wrapper overhead rather than comparing separately built upstream-vs-Khostty native libraries.
- `library_source_sha` / origin remain caller claims until authenticated by build receipts.
- Linker invocation based on directory + `-lghostty-vt` still needs runtime-loaded-artifact identity proof where sibling libraries could exist.
- ABI drift and clean standalone package/install evidence remain.
- No native harness execution in this environment.

## SOTA / architecture implication

The candidate work does not change the earlier external-bootstrap decisions: OTIO remains an editorial interchange/projection candidate, USD a spatial/hybrid projection candidate, and existing terminal/libghostty/control stacks remain Khostty alternatives. Candidate patches solve local orchestration/binding evidence defects; they do not themselves pass either product existence gate.

## Handoff gate

Both candidates are now real, bounded implementation candidates under adversarial review. Neither is accepted or merge-ready. Experimental developer handoff remains active; general developer handoff remains blocked.
