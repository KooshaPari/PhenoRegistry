# Mature journey and interface contract — pass 1

Date: 2026-09-30. This is a cross-product research projection; repository-local contracts remain canonical. It does not merge the products.

## Shared architectural rule
HeliosLite and KCode are replaceable coding-worker/runtime products. Neither owns durable development-effort truth or accepted product truth. External systems integrate through versioned interfaces. Product-local session state may optimize/resume work but cannot become the sole record of assignment, acceptance or evidence.

## H-J01 / K-J01 — bounded coding change
Actor supplies repository/worktree, accepted assignment/criterion reference, provider/model/config and allowed capabilities. Runtime identifies itself, executes a bounded edit/tool sequence, persists its own resumable session, and emits a terminal result plus exact candidate/config/run evidence. Independent grader checks the actual repository outcome. A worker saying done, zero tests, missing collector, stale candidate, or report-only exit zero cannot close the journey.

## J-02 — worker replacement/recovery
Attempt A belongs to durable effort E. Before/after an external side effect, A may die. Attempt B attaches to E using an adapter-provided effort ID plus runtime session/resume token. Product must distinguish known-not-executed, known-executed, and uncertain external effect. B reconciles uncertain effects before retry. Session continuity without effect reconciliation is insufficient.

## J-03 — machine/headless caller
Caller submits bounded work over the product's supported machine interface. Capability negotiation identifies cancel/resume/progress support. Caller can cancel; terminal status is typed and non-ambiguous. Transport disconnect is not automatically task cancellation. Product evidence includes live runtime identity; durable task handles, if adopted, remain distinct from product acceptance.

## J-04 — fork/upstream coexistence and update
Owned product and upstream control may be installed side-by-side without binary/config/data/update-channel collision. Upgrade/rollback preserves supported sessions or explicitly migrates them. Runtime evidence proves which binary/daemon actually served the request. KCode must reject stale/wrong daemon identity; HeliosLite must not silently execute upstream Forgecode when fork identity is required.

## J-05 — external development/evidence integration
AgilePlus-like durable effort system supplies work-package identity/state through an adapter; Tracera-like product graph receives accepted evidence/trace edges through an adapter. Runtime may emit telemetry but cannot declare product acceptance or recreate the external system's canonical ontology. Adapter failure is explicit and retryable; local execution success does not forge an external green.

## J-06 — native shell/platform boundary
On supported Windows and POSIX profiles, command, cwd/path, environment, quoting, PTY/TTY, signals/cancel, process-tree termination and exit status preserve declared semantics. Pine may supply translation/compatibility as a separate adapter. PowerShell/CMD/WSL presence is not itself failure; the accepted requirement is that POSIX-oriented workflows need not be rebuilt around those substrates when a supported native path exists.

## J-07 — provider/harness composition
Provider adapters preserve user/system/tool/history semantics and report unsupported transformations. A subprocess provider (for example ForgeCode-as-provider) must bind child binary/version/config, isolate tool authority, propagate cancellation/timeouts and never present translated partial history as lossless without evidence. Provider breadth is not differentiation by itself.

## Interface boundaries
- **WorkerAttempt**: attempt_id, runtime product/candidate/config, lease, runtime session token, start/end reason.
- **DurableEffortRef**: external effort/work-package ID, accepted assignment baseline, adapter/version; no runtime ownership.
- **ProductEvidenceEnvelope**: product, subject, contract/criterion, source/build/runtime candidate, configuration/environment, verifier/policy, run/time, raw artifact/provenance, status/reason.
- **ExternalEffectReceipt**: effect ID, operation/target, authorization, attempted/known outcome/uncertain state, provider receipt, reconciliation state.
- **RuntimeIdentity**: installed executable/daemon identity appropriate to product; identity is observation, not trust authority.

## Negative controls required for every product where applicable
Wrong worktree; wrong daemon/binary; stale contract; empty validation; skipped required check; collector crash; denied tool; provider failure; partial output before timeout; child process surviving cancellation; disconnect/reconnect; duplicate external effect; incompatible session migration; adapter unavailable; external system rejects evidence; worker modifies grader; upstream/fork config collision.

These journeys are mature-contract projections. Stage closure still requires repository-local applicability decisions and source reconciliation.