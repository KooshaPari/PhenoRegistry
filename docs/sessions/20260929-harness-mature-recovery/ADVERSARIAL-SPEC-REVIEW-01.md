# Independent-style adversarial specification review — pass 1

Reviewer stance: assume the current ontology/topology is wrong and produce counterexamples.

## Attack A — Session and DurableEffort might be one object
Counterexample: a durable operations effort invokes two providers with separate server-side sessions and later a human-only wait. One effort therefore spans multiple/no active sessions. Distinction survives.

## Attack B — WorkGraph and scheduler could be unified
Counterexample: same fan-out graph may run locally sequentially under resource pressure or gang-scheduled across GPUs. Conversely unrelated graph nodes may need co-location. Distinction survives.

## Attack C — Event log could be sole truth
Counterexample: A2A explicitly allows missed streaming messages; client reconnect must recover task/artifact state. Event projection cannot be sole authority unless it is itself the durable authoritative log with replay guarantees. Contract needs backend capability declaration. Strengthen.

## Attack D — Checkpoint proves side effect state
Counterexample: process dies after remote mutation but before checkpoint. Checkpoint cannot establish outcome. Effect ledger/reconciliation distinction survives.

## Attack E — One CLI is obviously enough
Counterexample: Codex may offer first-party ecosystem/app-server UX while jcode offers multi-provider/native performance/subscription behavior that cannot be upstreamed/configured equivalently. Segmentation remains an empirical gate, not assumption.

## Attack F — Two CLIs are obviously justified
Counterexample: shared harness + modes/plugins may reproduce all role differences while cutting maintenance. Dual-client topology remains unproven.

## Attack G — Generic harness can ignore UI semantics
Counterexample: approvals, elicitation, streaming and multi-session projection require client-independent typed interactions; SWE-agent also shows ACI affects performance. Client presentation is separate, interaction semantics are not.

## Attack H — Generic harness should own durable execution
Counterexample: Temporal/Durable Task provide mature generic durability and scaling. Canonical contract should own semantics/conformance, not necessarily engine implementation.

## Attack I — Agentora should simply be restored
Counterexample: historical Agentora boundary may be right conceptually but current SOTA and new generic requirements may supersede its APIs. Recover obligations, not source authority.

## Attack J — ProductState can be derived from DurableEffort
Counterexample: deployed release/runtime observations continue independently after development effort closes; multiple efforts modify one product state. Distinction survives.

## New gaps found
1. Need explicit Command/Mutation object between client request and Effect so approvals bind immutable action digest.
2. Need CapabilitySnapshot/version negotiation object for provider/tool/client skew.
3. Need StoreTrust/Integrity semantics because checkpoints/evidence are trust boundaries.
4. Need clock/order model for distributed events and approvals; wall-clock alone insufficient.
5. Need ownership/tenancy identity for fleet fairness, secrets and workspace isolation.
6. Need retention/deletion/redaction lifecycle for traces/evidence/artifacts, especially privacy-sensitive data.
7. Need schema migration/version compatibility contract for durable state.

Result: specification is **not final** after pass 1. Add these objects/constraints, then rerun adversarial review.
