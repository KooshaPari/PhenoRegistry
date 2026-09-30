# Session-end handoff — harness mature recovery

Date: 2026-09-30

## Corrected primary scope

Exactly two active primary repositories:
1. **KooshaPari/HeliosCLI** — Codex lineage, frozen source `2adc983bbb105546127250e688774338677ff43a`, recovery draft PR #691.
2. **KooshaPari/KCode** — jcode lineage, frozen owned source `046ea2af5e01e84449f65d086510b51152360215`, spec draft PR #12 plus bounded implementation candidates.

**HeliosLite is sunset Forgecode donor/reference evidence. Do not continue it as a third primary repository.** Existing HeliosLite research/qualified recovery primitives remain useful donor evidence.

## Accepted mature family intent

- Generic dynamically composable agent harness, coding-first but not coding-bound.
- Harness semantics must embed cleanly in GUI/TUI/CLI/API/SDK/headless/distributed clients.
- Separate client/application semantics from agent kernel/runtime/orchestration/evidence/control-plane semantics.
- HeliosLab is a GUI-native Codex-app-class workbench with CMux/Herder-class attention to real-time/at-scale performance; it consumes shared harness primitives and must not parse a CLI transcript as its primary architecture.
- Codex and jcode are active upstreams with strategic contribution value. User is a jcode contributor and is open to contributing to Codex.
- HeliosLite/Forgecode is sunset unless its lighter ephemeral/headless role survives a falsification test against Codex/jcode + shared harness.
- Agentora may have descendants in PhenoShared, but complete absorption/semantic parity/active consumers are not proven. Audit before relying on it.

## HeliosCLI current evidence

Frozen: `2adc983...`; PR #691.

Initial high-value findings:
- active root harness workspace is distinct from excluded vendored `codex-rs/` and `codex-cli/`; vendored Codex is not built/tested/mounted.
- README's broad Codex-like commands are not implementation evidence for root Helios.
- active root binary mounts Run/Checkpoint/Rollback/Status/Enqueue/Record/Ask/Exec/Resume.
- current RootManager orchestration is prototype scaffolding: in-memory tasks/agents, synthetic success, no actual worker/model/tool execution.
- current harness_interfaces is generic request/response/pubsub, not a mature agent-runtime contract.
- architecture's historical “stateless library + NDJSON checkpoint” decision conflicts with current durable-effort/evidence/recovery intent and must be re-evaluated.
- intent/boundary propagated docs are placeholders but bind 50 historical prompts; sampled prompt paths are not co-located and must be recovered from Registry/history/conversations.
- harness_pyo3 is excluded due broken PhenoShared path, evidence of incomplete shared-layer integration.

Next HeliosCLI work:
1. recover all 50 bound prompts + earlier Codex/Helios discussions and classify USER INTENT vs assistant suggestion;
2. inventory/trace every root harness crate and mounted helios command; mark stubs/scaffolds/unreachable surfaces;
3. freeze current OpenAI Codex revision and build exact upstream delta/feature/architecture matrix;
4. audit root tests/CI/release/security/persistence/performance evidence;
5. audit Agentora -> PhenoShared obligation parity and consumers;
6. build chronological capability lineage: old HeliosCLI -> modern Codex -> KCode/jcode, with HeliosLite as sunset donor;
7. independent SOTA harness research before architecture freeze.

## KCode current evidence

Primary spec PR #12. Key qualified candidates:
- #14 daemon identity candidate `effe7dcb...`: exact main-socket runtime identity primitive qualified.
- #20 effect recovery candidate `bac23f88...`: hook + daemon regression + governance green; QUALIFIED_CANDIDATE_PRIMITIVE / REACHABILITY_OPEN.
- #22 macOS trust candidate `a9daae12...`: native macOS policy + daemon regression + governance green; signed-release provenance still open.
- standalone effect state-machine and separate-process attempt replacement oracles are green.
- retained-patch denominator reduced: audit corpus and zero-line skeleton crates excluded; ForgeCode provider increasingly looks like upstream/external adapter rather than deep-fork justification.
- KCode remains far behind current jcode; current upstream + thin overlay is a serious alternative, but family-level decision must also satisfy recovered HeliosCLI/Codex obligations and generic harness architecture.

Next KCode work:
1. finish signed-release macOS provenance experiment;
2. semantically classify all meaningful 136 divergent commits against current jcode;
3. golden-test ForgeCode adapter system/history/tools/cancel/resume fidelity;
4. classify HERDR/cache/compaction/memory/permissions/shell behavior against upstream;
5. map mounted interfaces/persistence/security/release source families to resolved state;
6. construct thin-upstream alternative and compare maintenance/behavior;
7. do not close effect recovery until a real durable-workflow consumer mounts the qualified primitive.

## Cross-family research program

Persisted in `CANONICAL-HARNESS-RESEARCH-MANDATE.md`.
Research agent theory, ACI, tools, context/memory, durable execution, scheduling/distribution, sandboxes, provider routing, interoperability, IAM/policy, event semantics, observability/replay, MACE/evaluation, HITL, recovery, QoS, identity/evidence authority, plugins, control planes, coding-specific primitives and non-coding falsification workloads.

Candidate decomposition to attack, not assume:
Agent Kernel / Provider Runtime / Tool Runtime / Context+Memory / Workspace Runtime / Durable Effort / Scheduler+Fleet / Policy+IAM / Evidence+Grader / Event Projection / Control Plane / Client Adapters.

## Completion discipline

No percentages unless denominators are known. No third primary repo. No architecture freeze until SOTA + alternatives + lineage + high-risk experiments close. No repo survives because of sunk work. A capability may survive while its repository dies.

## Immediate next-session first actions

1. Continue HeliosCLI #691 archaeology from bound prompts and root harness reachability.
2. Freeze current Codex upstream and current jcode upstream revisions on the same date.
3. Audit Agentora/PhenoShared before designing new shared harness APIs.
4. Continue KCode retained-patch semantic reduction and macOS provenance.
5. Start structured external harness research passes and bootstrap decision ledger.
6. Build the first family capability-lineage matrix with mature destination per capability.
