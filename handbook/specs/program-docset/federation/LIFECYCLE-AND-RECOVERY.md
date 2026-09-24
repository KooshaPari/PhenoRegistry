# Installation, activation, upgrade and removal

## State model

Track installation status separately from binding status and instance status. A package can be installed while no integration is allowed or running. A failed binding does not prove the package is absent.

Binding states include DISCOVERED, INCOMPATIBLE, FORBIDDEN, AWAITING_CONSENT, RESOLVED, PREPARING, ACTIVE, DEGRADED, QUIESCING, DETACHED and FAILED_RECOVERABLE. Every transition records scope, plan revision, cause and actual operation outcome. These are proposed state names, not fabricated deployed APIs.

## Co-install reconciliation

1. Observe a verified package event or bounded inventory change in the correct principal/environment.
2. Read manifests without executing providers. Distinguish partial inventory from an empty installation set.
3. Resolve qualified recipes and required capabilities using pinned policy and current grants.
4. Present one meaningful approval when needed; auto-activate only inside a previously authorized envelope.
5. Prepare scoped service endpoints and UI contributions without exposing a half-initialized feature as ready.
6. Commit a locally durable plan and activate ready contributions. Mark required versus optional failures correctly.
7. Retain a recovery record and explicit detach operation. Probe readiness instead of inferring it from process existence.

Package watchers are at-least-once observations, not a promise of exactly-once callbacks. Stable event/operation IDs, expected versions and idempotent reconcile operations prevent duplicate services/menus/jobs. Repeating an unknown external action with a new ID is prohibited until its result is reconciled.

## Transaction limits

The planner may transactionally update its own state. It cannot honestly promise a global ACID transaction over unrelated apps, stores, package managers and remote services. Prepare/commit where providers support it; otherwise use a recoverable sequence with explicit compensation and partial-state reporting. Keep domain data migration outside implicit co-install setup.

If the process dies after a provider accepted an action but before the host saw its receipt, recover by operation ID. A compensating action may not erase an irreversible external result; surface that limitation. Do not label all rollback scripts successful merely because they exited zero.

## Hot update and version skew

Pin the active composition. Validate candidate versions and capabilities without swapping underneath an in-flight edit or live audio/game path. Quiesce at a safe boundary; drain or explicitly cancel work; checkpoint owned state; atomically swap local routing where supported; then verify readiness and retain rollback artifacts.

True hot unload is optional and must be advertised. Some native libraries, processes or plugin environments require a restart. Display that requirement rather than freeing an in-use pointer, hanging the host or promising no interruption. Allow side-by-side provider versions when their scope and state formats permit it. A new schema version needs an explicit compatibility/migration plan, not blind downgrade on rollback.

## Detach versus uninstall

Detaching B from A removes that binding and its UI contribution, revokes the grants specific to that relation, releases leases and preserves B's data. It does not uninstall B or affect its unrelated consumers.

Uninstalling B must identify dependent bindings and distinguish base-required from optional capabilities. Required workflows become blocked with a repair route; optional enhancements disappear gracefully. Stop instances only when no valid leases remain. A package manager's removal hook cannot be assumed to run reliably; stale registration cleanup must be idempotent and recoverable.

Data deletion is a separate explicit decision with export/retention rules. The federation system may remove its own stale cache and grants, not delete the provider's authoritative user data. Reinstallation under a new principal must not inherit another person's old access grants. Same publisher name is not sufficient to trust a replacement artifact.

## Multi-window and background operation

A user can close a host window without terminating a provider job that has an accepted background policy. Closing the last UI lease is not always cancelling the job lease. Conversely, providers cannot remain indefinitely active without a permitted owner and budget.

Startup reconstructs the current perspective and resolves still-valid object references. It does not blindly replay UI actions. Launching both A and B must not start duplicate migrations, schedulers, capture services or notifications. Inactive user sessions and remote nodes advertise availability honestly.

## Recovery evidence

For each stage, test abrupt termination, repeated events, stale plans, permission revocation, provider crash, dependency disappearance, update skew, disk-full conditions and lost acknowledgments. Attach actual source/package/profile identities and logs. Success means the world is in a known recoverable state and no protected data/action was duplicated—not that every error was suppressed.
