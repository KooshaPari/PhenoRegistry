# Agentora / PhenoShared absorption audit — pass 1

PhenoShared frozen evidence snapshot: `b00cc44b67f00ecac0f7e549e5a259bf589fd1fd`. Supporting dependency only; not a third primary product.

## Historical authority
- Agentora intent: extracted agent-orchestration runtime from McpKit; message routing, task dispatch and cancellation; primary consumers historically thegent and OmniRoute.
- Historical boundary: routing/dispatch/cancellation/backpressure in scope; LLM calls, tool implementations and persistent queues elsewhere.
- 2026-07-17 absorption justification: status QUEUED, disposition ABSORB, proposed target `crates/agentora/`, confidence 0.8.
- Later capability dossier explicitly says the contemplated Pheno consolidation is not established by the package and requires source/build/consumer evidence.

## Current descendant/candidate surfaces
- `crates/pheno-agent/`: broad framework charter/PRD covering lifecycle, skills, orchestration, multi-agent, context, security/observability.
- `crates/pheno-agent/phenotype-daemon/`: language-agnostic skills daemon/protocol/client-shim work.
- `crates/harness-native/`: scheduling/packing strategies including queue, throttle, coalesce, speculative, load-balance, circuit-breaker, retry, jobserver and hypervisor-lane.
- `agents/phenoagent/phenotype-agent-core/`: additional architecture/governance lineage.
- `crates/hexa-kit/python/pheno-agents/`: migrated Python descendant.
- historical Agentora dossiers/absorption material and benchmark/eval artifacts.

## Contradictions
1. Proposed absorption target `crates/agentora/` is not established here as the canonical current implementation.
2. Old Agentora boundary was deliberately narrow; current pheno-agent charter is much broader. This may be evolution, parallel lineage or scope inflation—do not equate them without provenance.
3. PhenoAgent docs claim active core runtime/planning, but document claims require implementation/build/consumer mapping before acceptance.
4. phenotype-daemon is primarily a skills-registry IPC daemon by its spec, not automatically the generic agent runtime.

## Required parity audit
For each accepted shared-harness obligation classify PRESENT_EQUIVALENT / PRESENT_CHANGED / PARTIAL / ABSENT / SUPERSEDED / REJECTED across Agentora lineage and current PhenoShared surfaces. Record build inclusion, exported API, tests, active consumers and performance/evidence.

## Current decision
DO NOT create another generic harness implementation yet. Treat PhenoShared as a candidate pool requiring consolidation audit. The canonical shared contract may reuse, refactor or retire these pieces after SOTA comparison.

## Immediate high-value checks remaining
- root workspace membership/package graph for pheno-agent/harness-native/daemon;
- active consumers of pheno-agent and daemon;
- actual runtime/tool/memory/planning implementations vs docs;
- harness-native relationship to the user's high-concurrency scheduling intent;
- licensing/publication/versioning boundaries;
- matched comparison with AutoGen/OpenAI Agents SDK/Microsoft Agent Framework/Temporal/Durable Task and Codex/jcode cores.