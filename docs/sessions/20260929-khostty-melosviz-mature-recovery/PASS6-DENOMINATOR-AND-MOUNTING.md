# Pass 6 execution — denominator closure and mounted-source falsification

Observed 2026-09-30. Exactly two product subjects: Khostty and Melosviz.

## Closed sub-gates

### Melosviz tracked tree
Frozen source `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`.
Every top-level Git tree was recursively enumerated with untruncated responses. 688 exact blob rows are persisted product-locally. This closes tracked-file enumeration only.

### Khostty tracked tree + fork ownership
Frozen source `a29aa9c6553d9f42aa68e2919116c0f6d53f329d`; merge base `d4c88d8069912b653d707191388ca98e24751f12`.
Every top-level Git tree was enumerated. 2,138 exact non-fuzz rows are persisted; the inherited fuzz family is separately bounded at 4,014 blobs / 4,002 corpus seeds. Top-level ownership is 43 identical, 13 added, 6 modified, 0 removed.

## Khostty new evidence

The public `apprt.ipc` export points to `src/apprt/ipc/mod.zig`. That file and upstream merge-base `src/apprt/ipc.zig` are the same 253-line implementation after only the relative import paths are normalized for the directory move. The new JSON agent-control implementation is ten adjacent fork-owned files, not the exported legacy IPC implementation.

Repository code search found `AppHost`, `Server.bind`, pane manager and event-publish hooks only within the new subsystem and documentation/recovery records, not a native app lifecycle caller. This materially strengthens K-F02/K-F11: primitives exist, mounted agent-control journey does not.

## Melosviz new evidence

### Double iteration / wrong work unit
The orchestrator dispatches per scene but passes the entire RenderSpec into the adapter. ComfyUI explicitly renders every scene in that spec. C4D and Unreal loop all matching scenes. The orchestrator and adapters therefore both own iteration; same-backend scenes can cause repeated whole-set work while per-scene events claim isolated work.

### Bridge output contract mismatch
`/api/studio/generate` documents nested `<out>/<scene_type>/scene_*` output but scans only flat `<out>/scene_*`. The real orchestrator gives adapters `<out>/<scene_type>`, and adapters create their `scene_NNN` children there. The existing bridge test pre-creates a flat scene directory and mocks the subprocess, so it validates the fixture rather than the mounted producer/consumer contract.

### Conflicting human-interface truth
Release CI packages Electrobun on macOS and Windows. Electrobun's Director console can mark all queued scenes done after CLI return. The web StudioConsole consumes the bridge manifest and can mark scenes error when the manifest is empty. Tauri is a real alternate scaffold consuming web/dist but is not the frozen release workflow's desktop target.

## External architecture consequence

Current ComfyUI's API exposes explicit job/prompt identities, terminal status, execution timestamps and structured outputs/assets. That is useful prior art for Melosviz's repair: preserve backend execution identity and structured outputs rather than inferring completion from a process exit plus filesystem glob. This is an integration pattern to evaluate, not proof that ComfyUI alone solves Melosviz.

## Handoff movement

Both product-local DEVELOPER-HANDOFF files now say not to redo tree inventory.

Khostty next experiment: native lifecycle spike proving unmounted baseline then minimal real server bind/host/event integration + nonce and stale-target controls; separately one wrapper-vs-direct-upstream consumer.

Melosviz next experiment: two same-backend scenes, count real adapter calls/media writes/event identities, exercise bridge generate without pre-seeding output, preserve failures, then repair so iteration has one owner and UI consumes structured scene results.

General developer handoff remains blocked. Experimental implementation is ready and more tightly bounded than pass 5.
