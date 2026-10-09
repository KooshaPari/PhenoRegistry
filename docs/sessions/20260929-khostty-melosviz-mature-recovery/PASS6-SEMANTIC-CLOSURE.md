# Pass 6 — finite tracked-tree denominators, mounted semantics, and handoff split

Observed 2026-09-30. Exactly two products remain in scope: Khostty and Melosviz.

## Handoff state

- **Khostty: READY FOR PARALLEL EXPERIMENTAL IMPLEMENTATION. NOT READY FOR GENERAL DEV HANDOFF.**
  - Ready now: K-E02 and K-E03 in disjoint worktrees. K-E03 now includes the linked-native/CI evidence qualification previously split into redundant K-E01-EMBED.
- **Melosviz: READY FOR EXPERIMENTAL IMPLEMENTATION. NOT READY FOR GENERAL DEV HANDOFF.**
  - M-E01 is ready/in progress.
  - M-E02/M-E03 remain dependency-blocked.

Machine-readable DAGs live in each repo at `docs/specs/mature-recovery-20260929/EXPERIMENTAL-WORK-DAG.json`.

## Khostty

Tracked-tree enumeration is structurally closed at frozen source `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`: 2,117 raw A+B rows are persisted with 62 exact path overlaps, yielding 2,055 unique non-fuzz paths and zero object-ID conflicts, plus an exact structural accounting of the test tree (`fuzz-libghostty`: 4,014 blobs, 4,002 corpus seeds). Counts are navigation only, never requirements or completion weights.

Merge-base ownership at `d4c88d8069912b653d707191388ca98e24751f12` is materially narrower than the earlier 207-ahead topology implies. At top level: 43 identical, 13 added, 6 modified, 0 removed. Entire large trees including macOS, test, include/public API, examples, pkg and vendor are tree-identical at that boundary.

The exported `apprt.ipc` surface is resolved: current `src/apprt/ipc/mod.zig` becomes textually identical to merge-base `src/apprt/ipc.zig` after only correcting the two relative imports caused by its directory move. It remains the inherited three-action Ghostty IPC. Ten adjacent agent-server files are fork additions, but `src/apprt.zig` does not start/export that server stack. Fork-aware search finds no application caller for `AppHost`/`Server.bind`; the frozen protocol separately admits startup is unwired.

CI evidence is not qualifying: substantive language/security jobs are advisory, several commands swallow failure with `|| echo`, macOS build is disabled, and `ci / test` only prints success after lint. Rust native wrapper integration tests are cfg-elided if `libghostty-vt` is absent. Therefore K-E02 and K-E03 can start now in parallel. K-E03 itself must produce the real linked-native sentinel and qualifying CI evidence before it can close.

## Melosviz

Tracked-tree enumeration is closed at frozen source `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`: all top-level trees recursively enumerated untruncated, with 688 exact blob rows persisted. Semantic resolution remains open.

Mounted implementation tracing now reaches CLI, bridge, release desktop, web UI, orchestrator, major adapters, assembly and packaging. Release CI identifies Electrobun as the shipping desktop candidate; Tauri is a separate alternate/non-release surface at the frozen revision.

New blocking findings:
1. Orchestrator iterates per scene but ComfyUI renders the whole RenderSpec on each call; C4D/UE render all matching scenes. Same-backend scenes can therefore trigger duplicated N×N work while receipts pretend each dispatch is one scene.
2. `/api/studio/generate` documents nested `<scene_type>/scene_*` output but scans only flat `out/scene_*`. Its regression test pre-creates that flat directory and mocks the subprocess, so it validates its fixture rather than the real CLI/orchestrator contract.
3. Electrobun and web can disagree about the same run: Electrobun marks all scenes done on CLI return; web can mark scenes missing/error from the empty bridge manifest.
4. Web's “Re-render this scene” sends `re_render=true` without WAV. The bridge forwards the flag; CLI direct requires WAV and returns 2; subprocess wrapper turns that into HTTP 400. Even with WAV, CLI direct only prints a `viz generate` hint and does not launch it despite API/docs claiming it does.
5. Default CLI job IDs are based on Python `hash(out_dir)`, hence process-dependent absent a fixed hash seed; they are not durable restart identities.
6. Cache fingerprints omit stamped reference-image/strength and character-reference/weight inputs that affect rendering. The storyboard `edit_count` comment claiming cache invalidation is misleading because edit_count is not part of the render key.

These findings make M-J-REVISE/M-J-RECOVER contradicted by current source semantics rather than merely untested. M-E01 must reproduce them on a real checkout before M-E02 repairs the scene/result/cache contract.

## General gates

Neither repo is ready for general or general-parallel implementation. Still open: primary authority/supersession, semantic source-family resolution, remaining SOTA/bootstrap decisions, bounded experimental results, complete mature obligations/quality/stages/journeys, bidirectional trace graph, product-bound acceptance oracles, qualifying CI, and fresh independent review.
