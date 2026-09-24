# Release state, concurrency and data safety

**Proposed domain contract. Implement inside the resolved existing controller; this is not a request for another database or orchestration product.**

## State machine

| State | Entry evidence | Allowed next state |
|---|---|---|
| Draft | Application intent exists | Planned, Rejected |
| Planned | Pinned candidate, capabilities, state/migration plan | Verified, Rejected |
| Verified | Actual complete fresh required-check set | Approved, Superseded, Rejected |
| Approved | Authenticated candidate-bound authorization | Applying, Expired, Superseded |
| Applying | Lease acquired; generation precondition still holds | Probation, Failed, Recovery-required |
| Probation | Intended generation observed; semantic health being assessed | Active, Failed, Rolling-back, Recovery-required |
| Active | Health and required consumer checks pass | Superseded, Degraded, Rolling-back |
| Rolling-back | Authorized rollback plan and data compatibility evidence | Probation, Recovery-required |
| Recovery-required | State, side effects or data integrity uncertain | Human-reviewed recovery plan only |

Expired, rejected and superseded candidates retain evidence but cannot be promoted. Failed health does not implicitly authorize a dangerous data rollback. Revert to a previous artifact only when the approved rollback policy covers the current data schema and state.

## Concurrency and replay

Use an environment-scoped exclusive lease and generation precondition in the authoritative store. Persist operation identity before mutation where feasible; record partial outcomes. Lease loss or target-generation conflict must stop further writes. A retry uses the same idempotency identity and observes existing effects before deciding whether a step needs re-execution.

Exactly-once external side effects cannot be assumed merely because the controller has a database transaction. If a provider performed the operation but the receipt write failed, recovery needs an external resource/operation correlation key or an explicit uncertain-state disposition. Duplicate approval, webhook delivery and worker rescheduling are expected test cases, not exceptional excuses to bypass checks.

## Event envelope

Each transition receipt should identify event ID, previous event/reference, candidate digest, source revision, policy generation, operation/idempotency ID, environment and target generation, actor/producer, wall-clock timestamp, measured monotonic duration when available, outcome and evidence references. Do not put secrets, entire prompts or unrestricted raw provider bodies into the envelope.

Append-only means prior evidence is not silently edited to make a later state look cleaner. Corrections append a superseding record. Tamper-evidence and authentication are separate from append-only storage; use the ecosystem’s actual evidence and auth mechanisms rather than claiming an unsigned file is a secure ledger.

## Desired versus observed

Desired state is what the accepted candidate requests. Observed state is what a fresh runtime/provider inspection reports. Reconciled state means the required observations match the intended generation and its health contract. API acceptance is merely one event in that process.

At minimum display `candidate`, `desired_generation`, `observed_generation`, `observation_time`, `health_contract`, `authorization_state`, `drift`, and `last_operation`. Unknown or expired observations must not render as green. Deleting a failed attempt from a dashboard must not delete its audit record.

## Stateful deployment preflight

Record data owner, storage location, mount/UID expectations, backup method, retention, encryption/credential custody and restore target. Make a consistent snapshot or application-aware backup; prove restore in a disposable environment using the application’s own integrity checks. Operator-approved RPO and RTO are still unresolved and must not be fabricated.

For every migration choose: **backward-compatible**, **forward-fix only**, **backup restore required**, or **unknown/blocking**. The choice applies to application code plus data schema and dependencies, not an image alone. Verify that the previous application version can actually consume current data before allowing automatic artifact rollback.

## Release probation

Use readiness and liveness separately from semantic acceptance. Examples: an API returns the expected authenticated response; a database-backed write survives process restart; an SSE route emits useful events and correctly terminates; the expected consumer can reach the new generation. The operator/application owner must set timeout and failure thresholds for the workload. This document defines the evidence fields, not arbitrary universal SLO numbers.

## Recovery after control-plane loss

Inspect observed runtime objects and leases, correlate external operation IDs, verify current artifact/config/data identity and reconstruct the last trustworthy transition. Quarantine ambiguous generations from automatic promotion. Resume only under the existing approval policy or an explicitly scoped recovery authorization. Do not “fix” ambiguity by deleting unknown volumes, resetting an IaC backend, or force-running the latest plan.

Motivating sources: S001, S004, S007, S012, S027. Detailed mechanisms above are proposed design requirements, not claims that an existing repository already implements them.
