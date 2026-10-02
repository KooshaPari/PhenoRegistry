# FULL FRESH-CHAT HANDOFF — HELIOSCLI + KCODE

Date: 2026-10-02
Owner: Koosha Paridehpour
Program: mature-first product recovery / generic harness convergence

## 0. PRIMARY SCOPE — ABSOLUTE
Exactly two active primary repositories:
1. `KooshaPari/HeliosCLI` — Codex lineage.
2. `KooshaPari/KCode` — jcode lineage.

`KooshaPari/HeliosLite` is **Forgecode sunset/donor evidence**, not product #3. Do not resume primary feature/spec expansion there. Preserve already-gathered research and qualified primitives as donor evidence.

Other repositories/systems (PhenoRegistry, pheno/phenoShared, Agentora history, HeliosLab, Pine, Herdr, current Codex/jcode, research harnesses) are evidence/dependency/consumer/alternative surfaces, not additional primary recoveries.

## 1. CURRENT USER INTENT — AUTHORITATIVE
- HeliosCLI was the first lineage; later forks were not originally planned as permanent parallel products.
- Each later fork was explored because its base appeared better/useful in whole or part.
- HeliosCLI is materially behind modern Codex now. Modern Codex is strategically valuable because upstream is active and contribution is possible.
- KCode/jcode is generally preferred over Forgecode for most uses. User is a jcode contributor. jcode upstream is active and strategically valuable.
- Forgecode/HeliosLite is sunset. Its remaining plausible niche is lightweight ephemeral/headless/light-chat behavior, and even that must survive direct falsification against Codex/jcode + shared harness.
- Desired topology may be segmented Codex/jcode roles or a converged/superset product. Separate products require a durable role boundary, not ancestry.
- The shared harness must decompose client/application semantics so one underlying architecture embeds cleanly in GUI, TUI, CLI, API, SDK, headless/background and distributed use.
- Freyr Kis/shared-harness work requires deep independent research: agent theory, research harnesses, production harnesses, software factories, generic/non-coding workloads, distributed systems, durable execution, ACI, scheduling, memory/context, policy/IAM, evaluation and control planes.
- Coding is the first demanding workload, not the permanent ontology boundary.
- HeliosLab is the GUI-native Codex-app-class workbench: intuitive controlled GUI plus CMux/Herder-class real-time/at-scale performance. It should consume shared runtime/event/state contracts, not parse/wrap a CLI transcript as its primary architecture.
- Pine remains the home for native Windows/POSIX compatibility concerns where needed.

## 2. SOURCE SNAPSHOTS / ACTIVE PRS
### HeliosCLI
- Frozen source: `2adc983bbb105546127250e688774338677ff43a`.
- Recovery branch: `spec/harness-mature-recovery-20260930`.
- Draft PR: #691.
- Current recovery docs: `docs/product-recovery/2026-09-30/`.

### KCode
- Frozen owned source: `046ea2af5e01e84449f65d086510b51152360215`.
- Spec branch: `spec/harness-mature-recovery-20260929`.
- Spec PR: #12.
- Daemon identity candidate #14: `effe7dcb1491e7a9933475c1c57a81e2c40e08d2`.
- Effect recovery candidate #20: `bac23f8885bb4a5f17bad926ca1451581b1a8b51`.
- macOS trust candidate #22: `a9daae12bb102047b3bbb708e516a841af686036`.

### Contemporary upstream baselines
- OpenAI Codex: `60947e234156ac12bdb7fba2477d3965f166bd34` (2026-09-30 19:22:34Z).
- 1jehuang/jcode: `2df1f77e920c01b4eb7830cc3c9f74d735e98087` (2026-10-02 03:35:36Z).
Do not silently move these baselines inside an analysis pass. Record a new dated snapshot when refreshing.

## 3. HELIOSCLI — CURRENT FINDINGS
- The active root Cargo workspace is a homegrown harness/client workspace.
- `codex-rs/` and `codex-cli/` are explicitly excluded vendored reference trees and are not built/tested/linted by root CI.
- Therefore README Codex-like command claims are not implementation evidence unless root Helios mounts equivalent behavior.
- Root `helios` binary currently mounts Run, Checkpoint, Rollback, Status, Enqueue, Record, Ask, Exec and Resume.
- `harness_orchestrator::RootManager` is prototype scaffolding: in-memory task/agent structures, trivial two-task decomposition, synthetic success; no real model/worker/tool dispatch in the inspected execute path.
- `harness_interfaces` currently defines generic Request/Response/Event/Handler/Publisher/Subscriber transport shapes, not a mature generic agent-runtime contract.
- Historical `ARCHITECTURE.md` says stateless library + NDJSON checkpoint/rollback; current mature intent requires durable effort/evidence/recovery and may supersede that design.
- `harness_pyo3` is excluded because its PhenoShared path dependency is broken; shared-layer integration is not cleanly established.
- Propagated intent/boundary docs are placeholders but bind 50 historical prompts. Sampled prompt paths are not co-located in the repo; recover from Registry/history/conversations.
- Registry history contains contradictory canonicalization/absorption records for `helios-cli`, `HeliosCLI`, `heliosHarness`, `helioscope`. Treat these as dated lineage facts, not current authority. `LINEAGE-AUTHORITY.md` establishes conceptual ID `HELIOS-CODEX-LINEAGE` and authority precedence.

## 4. KCODE — CURRENT FINDINGS / QUALIFIED EVIDENCE
### Qualified daemon identity
#14 exact candidate passed real main readiness socket test: version, git hash, PID and executable SHA-256. Earlier zero-test/debug-socket failures are preserved negative controls.

### Qualified external-effect foundations
- Standalone state-machine contract green.
- Separate-process Attempt-A/Attempt-B replacement oracle green.
- #20 exact candidate green for optional Write effect hook, committed-effect/failed-confirmation -> UNCERTAIN and pure Write reconciliation decisions.
- Status: `QUALIFIED_CANDIDATE_PRIMITIVE / REACHABILITY_OPEN` because no intended production durable-effort consumer mounts it yet.

### macOS trust
- Frozen KCode had fork-specific unconditional startup xattr stripping + forced ad-hoc re-sign.
- #22 makes startup repair explicit opt-in; native macOS policy workflow + daemon regression + governance green.
- Signed-release/local-build before/after digest/codesign/xattr/read-only/missing-tool/repeated-launch provenance experiment remains open.

### Existence pressure
- Owned KCode is far behind contemporary jcode.
- Audit/docs and zero-line skeleton crates are excluded from behavioral differentiation.
- `jcode-auto-dream` is a stub at action boundary.
- ForgeCode provider and Herdr integration are adapter-shaped; current upstream external-provider composition weakens deep-fork justification.
- ForgeCode adapter still needs golden system/history/tool/cancel/resume/error/auth fidelity tests.
- Continue semantic classification of all meaningful divergent commits; do not use crate names as differentiation.

## 5. AGENTORA / SHARED-HARNESS CORRECTION
Historical Agentora intent recovered from Registry:
- originated inside McpKit, extracted 2026-06-19;
- owned message routing, task dispatch, cancellation protocol, backpressure;
- explicitly excluded LLM calls (thegent), tool implementations (McpKit-derived libs), persistent queues (phenoEvents).

July absorption record says target was **`pheno/crates/agentora`**, not PhenoShared. Therefore the statement “Agentora was merged into PhenoShared” is currently not established and is partly contradicted by historical evidence. Trace later migrations and active consumers before selecting canonical ownership.

Current Freyr/shared-harness intent is broader than historical Agentora. Do not simply resurrect Agentora API and call it final.

## 6. GENERIC HARNESS RESEARCH — REQUIRED BEFORE ARCHITECTURE FREEZE
`CANONICAL-HARNESS-RESEARCH-MANDATE.md` is canonical working mandate.

Research independently across:
- agent loop/theory/planning/reflection/delegation;
- ACI/environment design;
- tools/capabilities/MCP/A2A/interoperability;
- context, memory, retrieval, compaction, caching;
- durable execution/checkpoint/retry/idempotency/effect reconciliation;
- scheduling/concurrency/backpressure/distributed fleet execution;
- workspaces/sandboxes/process/container/VM abstractions;
- provider/model routing and capability negotiation;
- IAM/secrets/policy/approvals/trust;
- streaming/events/client-independent state projection;
- observability/tracing/replay;
- MACE/evaluation/grader control loops;
- HITL/human-agent collaboration;
- cancellation/failure/worker replacement;
- resource/cost/QoS budgets;
- identity: worker attempt vs durable effort vs product state;
- extensibility/plugins;
- production control planes;
- coding-specific repo/worktree/build/test primitives;
- non-coding workloads specifically to falsify coding-derived ontology.

Initial external research signal only, not adopted architecture:
- OpenAI Agents SDK uses a deliberately small core around Agent/Runner/tools/handoffs/guardrails/sessions/HITL/tracing and now deterministic testing utilities.
- OpenAI tracing distinguishes workflow/task/turn/agent/generation/tool/guardrail/handoff spans.
- Tool guardrails and approval ordering demonstrate policy placement is semantic, not presentation.
- Prior research found Microsoft durable-agent separation, OpenHands harness/orchestrator/control-plane distinction and SWE-agent ACI evidence. Re-verify from primary sources in fresh chat before canonical decisions.

## 7. CANDIDATE HARNESS DECOMPOSITION — HYPOTHESIS ONLY
Attack this decomposition; do not assume it:
1. Agent Kernel
2. Model/Provider Runtime
3. Tool/Capability Runtime
4. Context/Memory
5. Workspace/Environment Runtime
6. Durable Effort / Workflow Orchestrator
7. Scheduler/Fleet Runtime
8. Policy/Approval/IAM
9. Evidence/Evaluation/Grader
10. Event/Projection API
11. Control Plane
12. Client/Application adapters

Alternatives may combine/split these differently. Architecture freeze requires falsification.

## 8. PRODUCT-FAMILY ALTERNATIVES — ALL LIVE
A. One converged/superset CLI/runtime on best base.
B. Codex-lineage + jcode-lineage segmented into stable distinct roles.
C. One canonical CLI plus the other as provider/runtime/adapter rather than user product.
D. Shared generic harness with thin Codex/jcode clients where upstream contribution paths remain valuable.
E. Forgecode-derived lightweight role only if it survives direct performance/operational falsification and cannot be expressed cleanly through A-D.

Do not choose based on sunk work or current repository count.

## 9. STRICT NON-CODE FINALITY
See `NON-CODE-FINALITY-GATE.md`.
Current verdict: **NOT FINAL**.

Non-code finality is blocked by 18 denominators, especially:
- full Helios intent/history resolution;
- contemporary Codex+jcode deep comparison;
- Agentora ownership/consumer trace;
- independent Freyr SOTA research;
- harness ontology falsification;
- Helios root reachability;
- KCode full semantic delta classification;
- KCode signed-release provenance + adapter golden tests;
- family capability lineage/mature destinations;
- topology decision;
- HeliosLab client contract;
- mature ontologies/requirements;
- journeys/stages;
- quality/security/performance/QoS;
- MACE/evidence/grader custody;
- bidirectional trace validation;
- release/migration/sunset contracts;
- independent fresh adversarial review.

Do not report 100% until every architecture-changing denominator is closed.

## 10. IMMEDIATE FRESH-CHAT EXECUTION ORDER
Do not start with a plan-only response. Execute.

1. Read this handoff + `NON-CODE-FINALITY-GATE.md`, `CANONICAL-HARNESS-RESEARCH-MANDATE.md`, `HARNESS-LINEAGE-CONVERGENCE-CORRECTION.md`.
2. HeliosCLI #691: recover the 50 bound prompts from Registry/history/conversations; create a provenance-classified intent matrix.
3. Freeze/confirm contemporary Codex+jcode baselines above; inspect architecture, current CLI/runtime/client protocols, sessions, tools, multi-agent/subagents, app-server/SDK surfaces, persistence, security, release and performance.
4. Audit Agentora absorption from source repo/history -> pheno/crates/agentora -> any later phenoShared descendants; map every historical obligation and active consumer.
5. Run structured SOTA research passes and persist multiple matrices, not one giant document.
6. Build first family capability-lineage matrix with columns: capability, first known appearance, user intent, source lineage, current Codex, current jcode, KCode delta, HeliosLite donor, shared-harness candidate, mature destination, evidence, uncertainty.
7. Continue KCode divergent-commit semantic classification and signed-release provenance design.
8. Build topology alternatives with explicit transition debt, maintenance cost, contribution strategy and client/harness boundary.
9. Only after research/lineage stabilizes: derive mature ontology, requirements, journeys, quality overlays and stage projections.
10. Complete MACE/autograder/evidence/trace/release/migration/security/operations docs.
11. Run independent fresh review attempting to falsify completeness.
12. If non-code finality is genuinely reached, mark it with evidence. Otherwise update the gate honestly and hand off again.

## 11. DO NOT
- Do not resume HeliosLite as primary product.
- Do not begin HeliosLab/Pine/Agentora as third primary recovery.
- Do not count vendored Codex as mounted HeliosCLI implementation.
- Do not infer capability from crate/file names.
- Do not treat a passing test as product acceptance without subject/candidate/config/evidence identity.
- Do not equate transcript persistence with external-effect truth.
- Do not claim exactly-once where downstream semantics cannot support it.
- Do not choose a requirement count.
- Do not force one ontology tree.
- Do not freeze architecture before SOTA/alternatives/falsification.
- Do not merge implementation candidates merely because their narrow gates are green.

## 12. KEY FILES
PhenoRegistry branch `spec/harness-mature-recovery-20260929`:
- `SESSION-END-HANDOFF-20260930.md` — older handoff, superseded by this file where conflicting.
- `HARNESS-LINEAGE-CONVERGENCE-CORRECTION.md`.
- `CANONICAL-HARNESS-RESEARCH-MANDATE.md`.
- `NON-CODE-FINALITY-GATE.md`.
- `TRACE-SKELETON.md`.
- `ARCHITECTURE-VALIDATION-MATRIX.md`.
- `EXTERNAL-EFFECT-RECOVERY-PASS.md`.
- `ATTEMPT-REPLACEMENT-ORACLE.md`.
- execution receipts 01..24+.

HeliosCLI PR #691:
- `docs/product-recovery/2026-09-30/SOURCE-COVERAGE-LEDGER.md`.
- `CURRENT-STATE.json`.
- `SEMANTIC-FINDINGS.md`.
- `LINEAGE-AUTHORITY.md`.

KCode PR #12:
- `docs/product-contract/20260929-harness-recovery/` including source ledger, semantic findings, retained-patch ledger, current state, effect adapter/recovery experiment docs.

## 13. FINAL STATE OF THIS CHAT
This chat did **not** reach absolute non-code finality, and it must not claim otherwise. It did establish the corrected primary scope, exact snapshots, several qualified high-risk primitives, the generic-harness research mandate, strict finality denominator, and a defensible restart path.

Continue autonomously until the non-code gate genuinely closes or a real user/authorization blocker is reached.