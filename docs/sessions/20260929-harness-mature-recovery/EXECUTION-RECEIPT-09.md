# Execution receipt 9 — external-effect crash window promoted to blocking contract

Date: 2026-09-30. Program remains OPEN.

## Source-backed crash windows
HeliosLite H-F008: ToolExecutor performs side-effecting service operations (Write/Patch/Remove/Shell/Fetch) inside `call_internal` before any first-class durable external-effect receipt is visible in the inspected path. ToolCallContext carries presentation/metrics/conversation metadata, not durable effect state.

KCode K-F008: the agent persists assistant ToolUse before local execution, calls `registry.execute`, adds ToolResult afterward, and persists tool results later. This creates a concrete post-effect/pre-result crash window where transcript intent can survive but external outcome can be ambiguous.

These are ambiguity findings, not claims of observed duplicate production effects.

## Contract and diagnostic
Both repositories now own `EXTERNAL-EFFECT-ADAPTER-CONTRACT.md` with INTENT_RECORDED, DISPATCHED, CONFIRMED, UNCERTAIN, RECONCILED and ABANDONED states, tool side-effect classifications and fail-closed retry policy.

Both spec branches also contain `diagnostics/effect_recovery_probe.py` plus a targeted `External Effect Recovery Contract` workflow. The probe uses real subprocess termination, atomic/fsync'd receipt writes, a real append-only side-effect log, idempotent/queryable and non-queryable cases, and asserts that uncertain non-queryable effects are not retried. CI runs are queued at receipt time; this validates contract semantics only, not production runtime integration.

## KCode existence pressure
Current upstream's external-provider composition root weakens `jcode-provider-forgecode-runtime` as a deep-fork justification. The owned ForgeCode runtime is now candidate `CONTRIBUTE UPSTREAM / EXTERNAL RUNTIME ADAPTER`; its translation remains subject to golden system/history/tool/cancel/resume fidelity tests.

## Gate state
HeliosLite H-F001..H-F004 and KCode responder identity remain exact-candidate qualified. H-F008/K-F008 are new blocking findings. Product-integrated crash-boundary experiments, durable-effort adapter wiring, source/existence/journey/trace completion and independent review remain open.