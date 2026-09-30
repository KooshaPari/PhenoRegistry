# Pass 11 — held-out red test and same-family architecture prior art

Observed 2026-09-30.

## Melosviz

The pass-9 held-out generative cache/evidence concern is now an executable reproduction, isolated from the green deterministic M-E02 candidate.

Branch experiment/m-e02-generative-identity, draft PR #303, is based on the demonstrated deterministic spine. Workflow run 2 (36752692502) at 43c195f410e4464ab83aa433e7d7342128e52a78 actually executes the held-out tests:
- no backend identity on a comfyui_image scene: FAIL as intended; second run is accepted from cache, adapter call count 1 instead of required 2;
- explicit cache_extra.renderer_identity: PASS, including invalidation when identity changes.

Run 1 is excluded because pytest was absent; it did not execute the product assertion.

This is now a clean RED developer-agent handoff. Do not globally disable cache. Preserve ComfyUI's existing prompt_id/history execution receipt, hash the canonical submitted workflow, and bind adapter/model/custom-node/deployment identity. If sufficient identity is unavailable, generative cache reuse must fail closed. The deterministic video_export run 45 remains separately green and must not regress.

## Khostty

Ghoztty source at fd3838acfa834c29e99616cdc8500c0208a13a09 was inspected beyond README. Its macOS IPC server receives socket requests off-main but dispatches terminal/window operations to DispatchQueue.main/MainActor and synchronizes response. handleSendKeys writes PTY input on main; handleRead reads terminal state on main. It bakes both owning socket path and pane identity into child environments, using caller-pane identity as a stable default anchor instead of current focus.

This is direct same-family prior art for K-E02a and strengthens the bootstrap decision: adapt/learn from a runtime-thread bridge rather than directly exposing Khostty AppHost to connection threads. Stable caller-pane targeting and PTY-vs-parser separation are also not novel Khostty concepts.

K-E03 run 19 further demonstrated a real downstream packaging burden: direct C with explicit rpath executes, while the Rust downstream consumer cannot find libghostty-vt.so.0 merely from the dependency build script. The harness now sets the platform loader path explicitly and records that burden; the upstream origin-token bug is fixed. Exact run 23 is active and remains unaccepted until both receipts pass.

## Handoff

- Melosviz PR #303: **READY FOR DEVELOPER AGENT EXPERIMENTAL IMPLEMENTATION, RED TDD TARGET.**
- Khostty K-E02a: **READY FOR DEVELOPER AGENT EXPERIMENTAL IMPLEMENTATION**, app-thread bridge only.
- Khostty K-E03: active comparison, not accepted.
- General handoff: NO for both products.
