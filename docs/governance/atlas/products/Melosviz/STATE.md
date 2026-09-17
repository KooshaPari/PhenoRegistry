# Melosviz — bounded current-state evaluation

**Observation date:** September 17, 2026 (supersedes 2026-09-16 snapshot). **Repository ID:** `1262466303`. **Default branch:** `main` (verified). **One owner chat:** Jcode (this session).

**Version:** v0.1.0 released 2026-09-17T03:00:57Z. **Latest sampled commit:** `f082aa5` — chore(desktop): enable macOS bundle targets for .app and .dmg output (2026-09-16 19:48:48 local).

## What moved since the September 16 snapshot

1. **v0.1.0 released** with two published artifacts:
   - `Melosviz-v0.1.0-macos-arm64.tar.gz` (4.8 MB, sha256 `1c5881…`)
   - `Melosviz_0.1.0_aarch64.dmg` (4.8 MB, sha256 `294690…`)
   - Release link: https://github.com/KooshaPari/Melosviz/releases/tag/v0.1.0
2. **Web test suite green: 243/246**, 3 skipped spec-first. Residual failures from the Sept 16 snapshot fixed in `390b859` (fix(web): resolve all test failures — 243/246 passing).
3. **Desktop bundle target enabled** (`f082aa5`): `cargo tauri build` now emits `Melosviz.app` + `Melosviz_0.1.0_aarch64.dmg` after a clean rebuild.
4. **Backend suite: 1448/1450.** This count is carry-forward evidence from a prior validated run. The backend tests were not re-run for this snapshot.

## Assessment vs atlas concerns

| Concern | State | Evidence |
|---------|-------|----------|
| Audio import/analysis/timing | Working | Backend + web suites green |
| Scene/preset generation vs fixtures | Working (editor + fixtures) | Web suite |
| Real render backend & editor | PARTIAL — offline placeholder pipeline only | Director/storyboard + FFmpeg placeholder clips |
| Native/web shell | Working (Tauri .app + .dmg build) | `f082aa5`, clean build |
| Export, reopen, output validation | PARTIAL | Ship path produces archive; reopen/recovery not fully exercised |
| Release/install proof | Artifact published; clean install not yet qualified | Release assets; NEXT-ACTIONS item 4 |

## Risks and unknowns

- The offline smoke is **PIPELINE_REHEARSAL_NOT_PRODUCT_PROOF**: placeholders are explicitly labeled, not real render output.
- Live creative backend (ComfyUI et al.) not yet product-proven.
- Clean-machine install smoke and interrupted-render recovery still outstanding.
- Reported test counts are local run receipts, not a fresh independent audit in this snapshot.

## Parent outcome (unchanged)

The installed product produces and edits a real useful synchronized visualization, with honest backend modes.

## Consumer and authority boundary

Reuse FFmpeg/Blender and licensed tools; do not handroll codecs or pass fixture output off as production. One owner chat: Jcode.

**Observation date:** September 16, 2026. **Repository ID:** `1262466303`. **Default branch:** `main`. **One owner chat:** user-reported, not observed here.

**Sampled commit:** `edbbd40016680bc430d26fb0d4a2a73999cd8ba5` (2026-09-16T10:01:17Z). This is the latest default-history item returned at that repository read, not an atomic portfolio tip or a view of all branches/local state.

## What moved

New director/storyboard tests accompany an offline pipeline that creates solid-colour placeholder MP4 clips via FFmpeg, then assembles/masters/ships them. The source explicitly labels the generation as placeholder.

**Assessment:** `PIPELINE_REHEARSAL_NOT_PRODUCT_PROOF`. This is a bounded next-proof assessment, not a percentage or certification.

## Risks and unknowns

- The offline smoke is useful integration rehearsal, not proof of visual quality or a functioning live creative backend.
- On placeholder generation failure the adapter can return workflow JSON; downstream contracts must distinguish metadata from playable media.
- Reported 13/13 E2E results were not rerun here.

## Parent outcome

The installed product produces and edits a real useful synchronized visualization, with honest backend modes.

## Consumer and authority boundary

Reuse FFmpeg/Blender/available licensed tools and shared design/capture contracts; do not handroll codecs or copy fake-success adapters.

## Evidence limits

Native product suites, actual owner-chat/worktree state, installed artifacts, all required hosted checks and full history were not inspected here. Commit/PR/handoff descriptions are author claims unless explicitly source-confirmed. No pilot winner, product completion or migration authorization is inferred. A quiet branch is not proof that the worker is idle. Return a current receipt before choosing work based on this snapshot.

## Sources

- `CUR-1262466303-S01` — https://github.com/KooshaPari/Melosviz/commit/31f19056f429718c6e8303e4fd0c64ca56e5374a
- `CUR-1262466303-S02` — https://github.com/KooshaPari/Melosviz/commit/edbbd40016680bc430d26fb0d4a2a73999cd8ba5
