# SOTA pass 5 — sandbox enforcement bootstrap

Retrieved 2026-09-30. Scope: HeliosLite sandbox architecture, not a third product.

## Linux filesystem confinement
Current `landlock` crate documentation (latest observed 0.4.7) provides a maintained safe abstraction over Landlock syscalls, path-beneath helpers, compatibility policies and explicit enforcement status. Its documentation recommends verifying `RulesetStatus::FullyEnforced` when full enforcement is required. This directly replaces the rationale in frozen `forge_sandbox` for leaving a custom no-op stub because the API was considered unstable.

OpenAI Codex current source is relevant prior art: it uses the maintained Landlock crate for filesystem restrictions and separately installs seccomp for network/process-sensitive syscall restrictions. Decision consequence: do not pretend one Landlock ruleset implements Helios's full hostname/network policy. Split filesystem and network/process enforcement into explicit qualified dimensions.

## Bootstrap disposition
- Filesystem isolation: INTEGRATE maintained `landlock`; do not hand-roll raw syscalls.
- Network: evaluate seccomp/proxy/network-namespace or another maintained primitive based on required policy; Landlock network support is port-oriented and does not make hostname allowlists magically reliable.
- Enforcement identity: record backend/version/kernel support + actual enforcement status in `SandboxOutput`/evidence; unsupported/partial cannot be called fully sandboxed.
- Windows: current placeholder is not enforcement; separately research Job Objects + restricted/AppContainer-style isolation or reuse a maintained execution sandbox.
- macOS: current Seatbelt/sandbox-exec path needs current-platform availability and escape tests; executable presence alone is not sufficient qualification.

## Required negative controls
Read outside allowed root; write to read-only root; execute child/grandchild; symlink/path traversal; network denied/allowed profile; unsupported kernel; setup failure; child pre-exec failure; backend unavailable. Every case must distinguish refusal, unsandboxed fallback, and fully-enforced execution.

Source references: rust-landlock docs/current crate and current OpenAI Codex Linux sandbox implementation. Exact dependency pin/license/project-health must be frozen before implementation ADR.
