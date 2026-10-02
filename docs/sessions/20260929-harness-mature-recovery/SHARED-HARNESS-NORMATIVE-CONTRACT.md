# Shared harness normative contract — non-code baseline

Date: 2026-10-01. Applies to HeliosCLI and KCode clients and any future shared harness implementation.

## Lifetimes
WorkerAttempt: disposable execution process/model/tool/sandbox lease.
DurableEffort: persistent assignment/change intent/plan/work packages/effect receipts/review/grader history.
ProductState: accepted product intent/config/artifacts/releases/evidence/observed behavior.

No identifier from one lifetime silently substitutes for another.

## Authority classes
ACCEPTED_INTENT > AUTHORIZED_DECISION > VERIFIED_OBSERVATION > DETERMINISTIC_SOURCE_FACT > IMPORTED_ASSERTION > AGENT_INFERENCE > HISTORICAL_SUPERSEDED.

Confidence never promotes authority.

## Core identities
ProductRef; ContractRef/version; DurableEffortRef; WorkerAttemptRef; ThreadRef; TurnRef; ToolCallRef; EffectRef; CandidateRef; ConfigurationRef; EnvironmentRef; VerifierRef/version; EvaluationRef; EvidenceRef.

## Effect rule
Side effects have durable intent/dispatch/outcome/reconciliation state. UNKNOWN/UNCERTAIN is not failure or success. Retry requires explicit policy/reconciliation/idempotency guarantee.

## Evidence rule
Evidence binds subject + contract + candidate + config + environment + verifier/version + run + time + raw provenance. Missing/skipped/collector failure/wrong candidate/stale evidence is not green.

## Client rule
GUI/TUI/CLI/API/SDK clients project shared state. A client may cache presentation state but cannot redefine durable effort, effect outcome, approval provenance or acceptance.

## Event rule
Events are typed, versioned and attributable. At minimum lifecycle, model, tool, effect, approval, workspace, evidence, grader, resource and error families. Ordering/causality semantics must be explicit; reconnect supports a defined replay/resume boundary.

## Capability rule
Provider/model/tool/runtime capabilities are negotiated. Unsupported semantics produce explicit degraded/unsupported state, never silent dropping.

## Grader rule
Worker may know rubric. Grader policy/version and evidence are independent of implementation. Critical dimensions cannot be averaged away. Implementation cannot weaken its own acceptance policy and self-green.

## Durability backend
Durable execution is an interface/port. Backends may be in-process/local, Temporal, Durable Task or another proven engine. Backend choice cannot change externally observable contract semantics without a versioned capability declaration.

## Scheduling
Scheduling/resource policy is separable from agent reasoning. Queueing, priorities, quotas, fairness, backpressure, cancellation and leases are observable and testable.

## Genericity falsification
Every proposed core abstraction must be tested against at least one non-coding workflow. Coding-only semantics belong in specialization layers unless evidence proves generality.

## Event durability classes
Events are classified as DURABLE_SEMANTIC, REPLAYABLE_DERIVED, or EPHEMERAL_PRESENTATION/TELEMETRY. Token deltas, terminal frames and UI cursor/pane state need not enter durable history unless a product contract requires them. Causal/subject ordering is specified; no global total order is assumed by default.

## Runtime + workflow composition
Agent runtime/message routing and durable workflow/orchestration are orthogonal ports and may be composed. An implementation may collapse them, but the contract does not require actor semantics to implement durability or workflow semantics to implement agent identity/routing.

## Tenancy and trust domains
Every durable effort/worker/effect/credential/evidence subject belongs to an explicit trust/tenant domain. Scheduling, quotas, secrets, approvals and event visibility enforce that boundary. Cross-domain delegation is explicit and auditable.

## Local-first conformance
Core semantics must have a fully local/self-hostable conformance path. Cloud services may provide richer implementations but cannot be required merely to preserve accepted state/evidence semantics unless a product stage explicitly chooses that dependency.

## History compaction and replay
Snapshots/compaction/continue-as-new may bound history, but must preserve authoritative state, causal provenance and references to immutable/raw evidence needed for audit. Model/tool nondeterminism is recorded as results/evidence; recovery does not silently re-invoke nondeterministic steps as though replay were equivalent.

## Approval freshness
Approval binds the exact effort, operation/effect version, policy and actor. Cancellation, replan, mutation or supersession invalidates incompatible pending approvals. Late/stale approvals are rejected.

## Evidence privacy and custody
Evidence may contain sensitive content. Contract supports access-controlled raw artifacts plus redacted/hashed attestations. A digest without retrievable/authorized custody is not automatically sufficient for criteria requiring semantic inspection; custody policy is criterion-specific.
