# Execution receipt 15 — Helios call identity corrected; attempt-B contract pinned

Date: 2026-09-30. Program remains OPEN.

## HeliosLite identity plumbing
Source tracing found stable call identity already exists above execution: ToolRegistry receives `ToolCallFull.call_id`, ToolResult preserves it, and `ToolCallId::generate()` exists for providers that omit IDs. The mature design therefore reuses this identity rather than creating a second effect-call namespace.

Candidate #333 now propagates or generates ToolCallId in ToolRegistry before `call_inner`, stores it in a cloned ToolCallContext, and derives protected Write effect identity from durable_effort_ref + ToolCallId rather than file path. This removes the repeated-write/path aliasing defect. Generated fallback IDs must ultimately be persisted with durable intent so attempt B reuses the same ID rather than generating a new effect.

Current candidate head: `60c7863ac110c25effaabdf6ca6a0621c3537a83`; all new checks are queued. Adapter injection remains deliberately unmounted until the primitive/call-ID plumbing qualifies.

## KCode attempt-B contract
The spec now pins replacement semantics: load durable effect record before fresh dispatch; Write reconciler compares expected persisted content/hash with actual target; match => RECONCILED_SUCCESS/no write, provable absence => RETRY_ALLOWED, conflicting/unknowable => STILL_UNCERTAIN. Missing transcript ToolResult never authorizes retry.

KCode #20 effect-hook CI remains queued. No attempt-B implementation is credited yet.

## Qualified foundations retained
Both standalone external-effect contract diagnostics remain green. KCode #14 daemon identity and #22 macOS policy primitive remain qualified at their exact candidates/runs.

No merge or completion verdict.