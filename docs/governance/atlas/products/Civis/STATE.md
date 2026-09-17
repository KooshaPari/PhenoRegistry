# Civis — bounded current-state evaluation

**Observation date:** September 16, 2026. **Repository ID:** `1164684442`. **Default branch:** `main`. **One owner chat:** user-reported, not observed here.

**Sampled commit:** `8650471500928f047370585d8fe5c43275b18aaf` (2026-09-16T09:35:26Z). This is the latest default-history item returned at that repository read, not an atomic portfolio tip or a view of all branches/local state.

## What moved

New persistence changes cover riot/migrant accumulators, scenario taxation, era progression, emergence samples and significance. A new acceptance report for older 264359af explicitly records that the gameplay precheck failed before gameplay ran.

**Assessment:** `SOURCE_CONFIRMED_BUILD_TARGET_GAP`. This is a bounded next-proof assessment, not a percentage or certification.

## Risks and unknowns

- Current game-e2e workflow selects --bin civ-standalone but later expects civ-server. Package selection does not select that second executable.
- The report infers a cache race without establishing the artifact was emitted and recommends cargo clean --release after building. That would remove release outputs; do not follow it.
- No captures plus passing library tests cannot justify near-100% visual polish.
- Older evidence may remain useful, but changed persistence behavior needs a current impact-based rerun.

## Parent outcome

A visually credible installed Civis game preserves and advances the same meaningful world through play, intervention and return.

## Consumer and authority boundary

Coordinate rendering/data contracts with PhenoShared and capture/asset owners without letting shared-library cleanup erase game semantics.

## Evidence limits

Native product suites, actual owner-chat/worktree state, installed artifacts, all required hosted checks and full history were not inspected here. Commit/PR/handoff descriptions are author claims unless explicitly source-confirmed. No pilot winner, product completion or migration authorization is inferred. A quiet branch is not proof that the worker is idle. Return a current receipt before choosing work based on this snapshot.

## Sources

- `CUR-1164684442-S01` — https://github.com/KooshaPari/Civis/blob/8650471500928f047370585d8fe5c43275b18aaf/.github/workflows/game-e2e.yml
- `CUR-1164684442-S02` — https://github.com/KooshaPari/Civis/blob/5d66e2bacd41e694591d0f8a8aea4a69518623e3/docs/reports/native-runtime-acceptance-264359af.md
- `CUR-1164684442-S03` — https://github.com/KooshaPari/Civis/commit/8650471500928f047370585d8fe5c43275b18aaf
- `CUR-1164684442-S04` — https://doc.rust-lang.org/cargo/commands/cargo-build.html
- `CUR-1164684442-S05` — https://doc.rust-lang.org/cargo/commands/cargo-clean.html
