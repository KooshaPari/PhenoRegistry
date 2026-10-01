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
