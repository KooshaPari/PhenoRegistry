# Execution receipt 17 — real process-death replacement gate pinned

Date: 2026-09-30. Program remains OPEN.

## Process model
Registry now owns `ATTEMPT-REPLACEMENT-ORACLE.md`. The gate explicitly forbids fake restart tests that reuse one in-memory object graph. Attempt A and attempt B are separate child processes; durable receipt, target and attempt evidence live in a temporary directory outside either worker.

Attempt A persists intent/dispatch, executes the real Write path, then dies after the file effect but before durable confirmation. Attempt B loads the same effect ID from disk and reconciles before any redispatch. Matching target => RECONCILED_SUCCESS/no write. Negative controls cover missing target/retry, conflicting target/fail closed, corrupt receipt, changed effect ID and repeated attempt B.

## Current candidates
KCode #20 `69a86ab...`: effect hook plus pure Write reconciliation decisions; targeted CI still queued.
HeliosLite #333 `46342ac...` at the last implementation receipt, subsequently advanced with stable ToolCallId plumbing and Write reconciler; current checks remain queued. Adapter reachability is intentionally not claimed yet.

## Closure semantics
H-F008/K-F008 cannot move to candidate-qualified until the exact process-death oracle passes against a product candidate. Even then, full closure additionally requires intended durable-workflow reachability and independent adversarial review.

No merge or completion verdict.