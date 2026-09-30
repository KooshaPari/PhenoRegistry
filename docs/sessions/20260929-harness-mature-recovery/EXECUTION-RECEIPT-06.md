# Execution receipt 6 — false-green control and differentiation pressure

Date: 2026-09-30. Program remains OPEN.

HeliosLite exact candidate `8451b952...` remains qualified for H-F001..H-F004 by an 8/8 dedicated oracle run plus clean exact-head platform/CVP/security/CI workflows. Canonical state records these findings as resolved for that candidate only.

KCode's prior green native workflow was rejected after log inspection showed its target command executed zero tests. CI now contains an explicit anti-zero-test guard and candidate `5a15dd86...` is rerunning. This demonstrates the program rule that a workflow-level green is not sufficient evidence when the intended criterion did not execute.

Existence-gate pressure increased: Pine/native Windows is not currently a demonstrated KCode fork differentiator; current upstream has substantial Windows/platform handling and frozen KCode did not surface a Pine subsystem. Pine remains an accepted external consumer/integration constraint.

HeliosLite owned `forge_agileplus`, `forge_tracera` and `forge_sharecli` crates are real implementation surfaces absent by name from the pinned upstream control, but their placement in core is unproven. They are now adapter-vs-core architecture experiments rather than automatic retained patches.

No product retirement, rebase, merge or architecture freeze is authorized.
## Extended pass

KCode run at `54b0e012...` later compiled cleanly and executed exactly one test. It failed because the test used the debug socket, whose Pong intentionally carries no runtime identity. Candidate `effe7dcb1491e7a9933475c1c57a81e2c40e08d2` moves the identity test to the actual main accept/readiness socket and retargets CI; new run queued. Debug/keepalive Pong remains non-attesting.

Exact KCode current-upstream crate-set comparison identified 11 owned-only crate names. Source inspection classifies auto-dream as an explicit stub, Claude CLI runtime as deprecated, ForgeCode/HERDR as real adapter-shaped integrations, and the remaining cache/compaction/permission/session/shell/terminal/tool-search crates as candidate behaviors needing semantic upstream and mountedness proof.

Exact HeliosLite crate-set comparison found 29 owned-only names. High-impact inspection plus caller/manifest tracing confirms mounted AgilePlus and Tracera implementations and dependencies on sandbox/DBD/shell surfaces. `forge_agileplus` is a top-level command engine; `forge_tracera` is best-effort telemetry that deliberately swallows delivery/config failures. Therefore Tracera telemetry cannot qualify product acceptance, and the mounted AgilePlus engine creates a duplicate-authority/custody question.

Registry now also contains `MATURE-JOURNEYS-INTERFACES-PASS.md`, `ARCHITECTURE-VALIDATION-MATRIX.md`, `AUTHORITY-CUSTODY-CANDIDATES.md`, and `TRACE-SKELETON.md`. These establish concrete worker-attempt/durable-effort/product-evidence/external-effect/runtime-identity interfaces and falsifying experiments.

Candidate custody direction: AgilePlus durable effort and Tracera accepted product/evidence authority stay external; Helios may project/adapter them. Pine owns translation/compatibility semantics while runtimes own adapters/native execution. Client SDKs do not automatically replace Agentora/general framework scope.
## Current extension
KCode retained-patch comparison is now decomposed at file-family level: 300 changed files versus current upstream, including 96 historical audit artifacts excluded from behavioral value and 188 crate files. Name-level novelty is explicitly non-evidence; upstream behavioral descendants exist for multiple fork-named cache/compaction/memory/discovery/permission surfaces. Current KCode spec state is bound to the latest candidate and marks the daemon-identity native rerun as still open.
