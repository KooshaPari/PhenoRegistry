# Execution receipt 9 — mountedness corrections, integration custody, and new implementation candidates

Date: 2026-09-30. Program remains OPEN.

## KCode qualified/candidate work
- #14 `effe7dcb...` remains qualified for exact main-socket daemon identity (version/git/PID/executable SHA-256).
- #16 targets a mounted ForgeCode provider whose current subprocess flags are incompatible with pinned official ForgeCode. It now fails closed unless the executable declares a versioned `jcode-forgecode-machine-contract-v1` marker plus required structured flags. Focused native CI is queued.
- #18 removes fork-specific unconditional macOS startup xattr stripping/ad-hoc re-signing. Native macOS `cargo check --bin jcode` plus runtime-mutation source guard passed at `f18881a...`; signed-release install/launch identity remains a separate gate.

## Helios integration custody
Issues #323/#324/#325 now track ShareCLI process ownership, AgilePlus canonical authority, and Tracera telemetry-vs-evidence. Accepted AgilePlus adoption does not imply Helios owns a duplicate AgilePlus engine. Tracera lifecycle telemetry is genuinely mounted at startup but explicitly best-effort/silent on failure, so it cannot qualify acceptance evidence.

ShareCLI #328 is a real implementation candidate: one `serve` process owns the hub; `publish`, `topics`, and `attach` use the running relay instead of disconnected process-local hubs. Focused cross-process CI is queued.

## Helios daemon corrections
`forge_dbd` stale comments were falsified: actual frozen source wires it through `DaemonConversationRepository` when `FORGE_DBD_ENABLED` is true. It is default OFF. Its Unavailable-vs-Indeterminate delivery certainty is valuable and retained as internal prior art. The default direct path already uses WAL, 30s busy timeout, NORMAL sync and a dedicated checkpoint thread, so #326 requires a matched existence experiment before daemon-mode promotion.

`forge_daemon` is different: no `forge_main`/`forge_app` caller or dependency surfaced; its consumer is the dedicated benchmark. That benchmark compares parallel fork+exec with sequential daemon dispatch on `/usr/bin/true`, so it does not establish product speedup. #327 classifies it experimental/unmounted pending a matched real-workload existence test.

## External-effect recovery
Repo-local contracts now make tool-call identity explicitly insufficient for crash-safe external effects. KCode's process-local RAII inflight map disappears on process loss; Helios tool-call IDs may be absent/provider/generated. Durable effect states and crash-boundary reconciliation remain the next cross-product vertical slice.

No merge, product retirement, architecture freeze or mature-product completion is authorized.