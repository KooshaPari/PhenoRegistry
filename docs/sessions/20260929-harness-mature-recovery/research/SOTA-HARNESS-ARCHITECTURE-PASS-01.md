# SOTA harness architecture — pass 1

Date: 2026-10-01. Research is evidence, not adopted architecture.

## Findings

### Small agent kernels are viable
OpenAI Agents SDK deliberately centers a small primitive set: agent, tools, handoffs/agents-as-tools, guardrails, sessions/HITL and tracing. Its runner owns turns/tool dispatch/session behavior; tracing distinguishes task/agent/turn/generation/tool/guardrail/handoff spans. Consequence: the canonical kernel does not need to own fleet scheduling or durable workflow infrastructure.

### Session state != workflow durability
Microsoft Agent Framework distinguishes conversation/session state from workflow checkpoints. Its Durable Task extension can add persistent sessions, checkpointed orchestration, distributed workers and long waits without changing core agent logic. Durable Task itself is framework-neutral. Consequence: model/agent session, durable effort/workflow and worker process are distinct contracts.

### Harness != orchestrator != control plane
OpenHands explicitly presents harness (agentic loop), orchestrator (execution environments) and control plane (routing/policy/budget/secrets/visibility) as separate pillars. Treat this as one useful decomposition to test, not terminology authority.

### Durable execution should be pluggable
Temporal and Durable Task both demonstrate durable execution as infrastructure beneath/around agent logic. We should specify a DurableExecutionPort rather than hand-roll universal workflow persistence in each client. Candidate adapters may target a local event log, Temporal, Durable Task or another engine.

### Event streams are projections, not authority
A2A separates Task, Message and Artifact; it explicitly warns streaming clients may miss status messages and messages should not carry task outputs. Consequence: client event streams must be reconstructable projections from durable state/evidence where correctness depends on them.

### Agent-computer interface is semantic
SWE-agent research established that the agent-computer interface materially affects software-agent performance. Tool/workspace/environment design therefore belongs in the harness research and evaluation program, even when the client UI is separate.

### Resource scheduling is not an agent graph
Ray models resource requirements, atomic placement groups, PACK/SPREAD strategies, actor/task retries and control-plane durability. Our scheduler needs explicit CPU/GPU/RAM/IO/model/provider/lease/budget/QoS constraints and must not infer capacity from graph topology.

## Provisional boundary model to falsify

1. AgentDefinition — instructions/policy/model capability requirements, no worker identity.
2. Attempt — ephemeral execution incarnation.
3. Session — model/conversation working context.
4. DurableEffort — persistent work intent, graph, state, receipts and decisions.
5. ToolCapability — typed callable capability and authorization requirements.
6. Effect — externally observable mutation with reconciliation identity.
7. Artifact — durable product/output object distinct from messages.
8. Workspace — filesystem/process/environment substrate and isolation.
9. Scheduler — resource/lease/priority/backpressure placement.
10. DurableExecutionPort — checkpoint/replay/timer/external-event semantics.
11. PolicyPort — authz/approval/secrets/guardrails.
12. Evidence — verifier-bound observation of exact subject/candidate/config.
13. EventProjection — reconstructable client stream; not sole authority.
14. Grader — independent acceptance policy/result.
15. ControlPlane — fleet policy/observability/routing/budget/operator surface.
16. ClientAdapter — GUI/TUI/CLI/API/SDK projection.

## Explicit non-equivalences

Attempt != AgentDefinition.
Attempt != DurableEffort.
Session != DurableEffort.
Checkpoint != Evidence.
Message != Artifact.
Event != durable truth.
Tool result != confirmed external effect.
Trace confidence != authority.
Graph node != worker.
Agent graph != resource schedule.
Work completion != product acceptance.
Client state != product state.

## Research consequence for HeliosCLI/KCode

Neither root Helios harness crates nor KCode/jcode runtime types become canonical shared contracts by default. Map them into this provisional ontology, record gaps, and prefer adapters/extraction over cross-client wrapping. The ontology remains provisional until non-coding workloads and independent review fail to falsify it.
