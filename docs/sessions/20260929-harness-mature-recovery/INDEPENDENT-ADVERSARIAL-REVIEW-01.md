# Independent adversarial review — pass 1

Role: assume the current recovery model is wrong and N alternatives are valid. This review attacks specification completeness; it is not a self-approval.

## Counterexample 1 — One canonical CLI may be the wrong topology
A Codex-lineage client and jcode-lineage client could remain justified if one optimizes rich interactive/App Server semantics and the other provider/runtime extensibility with materially different release cadence or embedding constraints. Current contract can explain this via shared harness + segmented clients. Evidence missing: matched workload/maintenance/performance comparison.

## Counterexample 2 — Two CLIs may both be unnecessary
Modern Codex App Server or jcode SDK could supply all client surfaces, with Helios branding/UX as thin clients. Current contract permits repository death and thin adapters. Evidence missing: full obligation parity.

## Counterexample 3 — Shared harness may not need a single implementation
A protocol/contract plus multiple conforming runtimes (Codex, jcode, embedded Agent SDK, distributed backend) may be superior to one universal kernel. Current normative contract allows backend/runtime ports but ontology language still risks implying one implementation. Keep conformance-first wording.

## Counterexample 4 — Actor/message runtime vs workflow runtime
AutoGen-like actor messaging and Temporal/Durable Task deterministic workflows solve different problems. One may not subsume the other. Specification must permit agent runtime + durable workflow composition rather than forcing one abstraction.

## Counterexample 5 — Durable execution backend cannot guarantee arbitrary external exactly-once
Workflow replay/non-reexecution does not make external systems transactional. External-effect identity/reconciliation remains necessary. Current contract covers this.

## Counterexample 6 — Client interchange can leak semantics
A rich GUI may need high-frequency ephemeral state (partial tokens, terminal frames, cursor/pane state) that should not enter durable event history. Contract must distinguish durable semantic events from ephemeral telemetry/presentation streams.

## Counterexample 7 — Realtime agents
Voice/realtime or game/computer-use agents may require latency/event/cancellation semantics unlike coding turns. Generic harness ontology must support streaming sessions without forcing every delta durable.

## Counterexample 8 — Non-LLM agents
Generic harness may host deterministic planners, rules engines, simulators or human workers. Agent identity/runtime/tool/evidence contracts must not require an LLM generation per step.

## Counterexample 9 — Multi-tenant/fleet security
At-scale runtime may cross user/org trust boundaries. Current security overlay is too high-level; tenancy, isolation, quotas, credential delegation and audit domains need explicit obligations before generic harness finality.

## Counterexample 10 — Offline/local-first
Cloud-dependent tracing/durability cannot be mandatory. Contract must allow fully local backends with equivalent semantics/evidence.

## Counterexample 11 — Event ordering
Distributed workers can produce partially ordered events; demanding a single total order may damage scale. Specify causal/subject ordering and projection rules rather than global total order unless required.

## Counterexample 12 — Long histories
Event-sourced durability can grow without bound. Compaction/snapshot/continue-as-new semantics must preserve authority/provenance and replay equivalence.

## Counterexample 13 — Model nondeterminism
Replaying a model call is not semantic replay. Recorded model/tool results and deterministic orchestration boundaries are needed for reproducible recovery; evaluation reruns are separate experiments.

## Counterexample 14 — Approval races
Approval can arrive after cancellation/replan/replacement. Approval identity must bind operation/effect version and current state; stale approvals rejected.

## Counterexample 15 — Evidence privacy
Full traces/tool outputs may contain secrets/private data. Evidence identity must allow redacted/hashed artifacts with custody/access policy rather than requiring raw content everywhere.

## Findings
Specification is NOT FINAL after pass 1. Add explicit durable-vs-ephemeral event classes, runtime/workflow composability, tenant/security domain, local-first conformance, compaction/replay semantics, stale approval rule, and evidence privacy/custody.