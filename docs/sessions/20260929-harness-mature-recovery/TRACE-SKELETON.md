# Trace skeleton — mature recovery pass 1

Date: 2026-09-30. This is intentionally a skeleton over accepted/high-confidence obligations; it is not a generated requirement catalog.

| Trace ID | Accepted intent / obligation | Design subject | Implementation candidate/surface | Verification/evidence | State |
|---|---|---|---|---|---|
| H-T01 | Missing/empty/skipped acceptance cannot green | strict benchmark oracle | Helios #322 `8451b952...` | run 36627763151, 8/8; exact workflow head | QUALIFIED_CANDIDATE |
| H-T02 | Timeout is terminal and cannot pass on partial output | executor + CLI terminal policy | Helios #322 | same oracle + exact-head platform/CI | QUALIFIED_CANDIDATE; descendant fixture still open |
| H-T03 | Signalled verifier cannot masquerade as exit 0 | shell verifier result model | Helios #322 | signal adversarial test in 8/8 suite | QUALIFIED_CANDIDATE |
| H-T04 | Fork/upstream identity coexistence | packaging/config/runtime identity | historical packaging spec + current fork surfaces | install/update side-by-side E2E | OPEN |
| H-T05 | Durable effort authority external to worker | AgilePlus adapter boundary | current mounted `forge_agileplus` conflicts with candidate boundary | consumer/ADR + adapter E2E | CONTRADICTION_OPEN |
| H-T06 | Product evidence failure cannot be hidden as telemetry success | acknowledged evidence adapter | current `TraceraTelem` is best-effort and swallows errors | collector-failure negative control | CONTRADICTION_OPEN for evidence use; telemetry itself acceptable |
| K-T01 | Evidence identifies actual serving daemon | Ping runtime identity | KCode #14 `effe7dcb...` | run 36686592906: main-socket native test 1/1 pass; version/git/PID/exe SHA | QUALIFIED_CANDIDATE |
| K-T02 | Empty/zero-test workflow is non-green | CI evidence harness | #14 workflow | earlier zero-test green rejected; workflow now explicit | QUALIFIED_CONTROL |
| K-T03 | Runtime identity test targets actual readiness endpoint | main accept loop, not debug socket | #14 `effe7dcb...` | run 36686592906: `main_accept_loop_reports_exact_runtime_identity` ok | QUALIFIED_CANDIDATE |
| K-T04 | Deep fork must beat current upstream + overlay | retained-patch ledger | 136 divergent commit search space; fork-only crates | semantic upstream comparison + matched journeys | OPEN / historical broad claims falsified |
| K-T05 | Windows differentiation is POSIX-oriented native semantics, not Windows checkbox | Pine adapter/native runtime boundary | current upstream Windows support + owned utilities | clean Windows command/path/env/PTY/signal suite | OPEN |
| X-T01 | Worker attempt != durable effort != product state | adapter/evidence ontology | both runtime products | crash/replacement/effect reconciliation vertical slice | OPEN |
| H-T07 | Side effect cannot become ambiguous across worker death | external-effect adapter contract | H-F008: ToolExecutor side effect precedes durable effect receipt in inspected path | contract crash-boundary probe + later product-integrated fixture | BLOCKING / CONTRACT_DIAGNOSTIC_QUALIFIED |
| K-T06 | Persisted ToolUse cannot be mistaken for known side-effect outcome | external-effect adapter contract | K-F008: ToolUse save precedes registry.execute; ToolResult save follows execution | contract crash-boundary probe + later product-integrated restart fixture | BLOCKING / CONTRACT_DIAGNOSTIC_QUEUED |
| X-T02 | Uncertain external effects are reconciled before retry | external effect receipt + durable effort adapter | no obvious first-class named abstraction found in frozen primary-source searches | kill-before/after-dispatch fixture with and without downstream idempotency | DESIGN_DEFINED / CONTRACT_DIAGNOSTIC_QUEUED |

Authority classes remain explicit: direct current user mission = accepted intent; historical docs = historical/proposal unless reconciled; source = deterministic implementation fact; CI/runtime = observation bound to exact candidate; assistant architecture choices = proposal until accepted/reconciled.