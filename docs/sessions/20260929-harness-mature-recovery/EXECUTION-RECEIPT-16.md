# Execution receipt 16 — attempt-B write reconciliation primitives added

Date: 2026-09-30. Program remains OPEN.

## KCode #20
Candidate advanced to `69a86ab777f491652e6df6e5e32775b884563f81`. A pure fail-closed Write reconciler now maps actual postcondition to ConfirmedSuccess, RetryAllowed or StillUncertain. Tests cover matching content => no redispatch needed, known absence => retry allowed, conflicting content => still uncertain. This is the attempt-B decision primitive; durable adapter invocation/replacement-worker orchestration remains open. Targeted CI queued.

## HeliosLite #333
Candidate advanced to `46342ac1dd0aeaaf1b9994a1f8aa8cf22da97cff`. Stable effect identity now reuses ToolCallFull.call_id propagated/generated in ToolRegistry and carried in ToolCallContext; path-based aliasing is removed. A matching fail-closed Write reconciliation primitive/test is added. Adapter injection remains unmounted until primitive/call-ID plumbing qualifies. New checks had not yet appeared at receipt time.

## Shared semantics
For both products, matching expected postcondition means the uncertain prior effect is reconciled as success and must not be repeated. Known absence is the only first-case retry authorization. Conflicting/unreadable state remains uncertain. Transcript absence is not retry permission.

## Still open
Neither product yet demonstrates a real attempt-A process death followed by attempt-B loading a durable receipt and invoking the reconciler through the product runtime. The standalone crash contract is green, but H-F008/K-F008 remain blocking until that integrated journey closes.

No merge or completion verdict.