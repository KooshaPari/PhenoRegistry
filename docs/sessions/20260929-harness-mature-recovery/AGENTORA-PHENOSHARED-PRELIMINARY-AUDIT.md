# Agentora -> PhenoShared preliminary audit

Date: 2026-09-30
Frozen PhenoShared: `b00cc44b67f00ecac0f7e549e5a259bf589fd1fd`

## Finding

The earlier assumption that PhenoShared contains only scattered Agentora descendants is too weak. The live Cargo workspace contains a substantial agent/runtime substrate:

- substrate / substrate-core / substrate-app;
- engine-spec plus Forge, Codex, Claude, A2A and AgentAPI engines;
- runtime-process and supervisor;
- substrate-schedule, substrate-dag, substrate-memory, substrate-skills, substrate-trace;
- orchestrator;
- driver-cli, driver-http, driver-argv, driver-mcp;
- file and SQLite stores;
- A2A, MCP and dispatch bridges;
- context-budget;
- policy/observability infrastructure from absorbed PhenoInfra;
- multiple cloud dispatch adapters.

This is strong evidence that a shared client-independent harness/runtime already exists in meaningful form.

However, PhenoShared's own `Agentora-capability` dossier explicitly says semantic absorption is not qualified and requires inventory of exported framework/state/model/storage/consumers, lineage recovery, build inclusion, consumer validation and comparison against external SDKs.

Therefore status is:

**SUBSTANTIAL_SHARED_SUBSTRATE_PRESENT / AGENTORA_SEMANTIC_PARITY_UNVERIFIED**

Do not create a new canonical harness kernel until this substrate is audited against the mature generic-harness research mandate.

## Required parity matrix

For each historical Agentora/mature harness obligation classify:
PRESENT_EQUIVALENT / PRESENT_CHANGED / PARTIAL / ABSENT / SUPERSEDED / REJECTED / UNKNOWN.

Minimum subjects:
agent lifecycle; runner/turn loop; model/provider abstraction; tools/capabilities; sessions; durable effort; checkpoint/recovery; external effects; cancellation; retries; handoffs/delegation; DAG/workflows; multi-agent; memory/context; approvals/HITL; IAM/policy; sandbox/workspace; event streaming; client projections; tracing/replay; evidence/grading; scheduler/QoS; distributed workers; plugin/extensibility; MCP/A2A; stores; versioned contracts.

For every PRESENT claim require:
source path + built workspace membership + public API + at least one real consumer or explicit library-only qualification + tests/evidence.

## Immediate architecture consequence

HeliosCLI's homegrown harness crates should be treated as historical/prototype donors until compared with PhenoShared substrate. KCode/jcode and modern Codex should integrate through engine/client adapters where feasible rather than each owning duplicate generic orchestration semantics.

This is a hypothesis to validate, not an architecture freeze.
