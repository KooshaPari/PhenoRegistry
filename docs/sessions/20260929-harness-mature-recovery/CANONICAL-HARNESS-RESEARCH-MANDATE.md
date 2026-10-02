# Canonical harness intent and research mandate

Date: 2026-09-30.
Authority: user clarification / accepted mature intent.

## Mature intent

The target shared system is a **generic, dynamically composable agent harness**, with coding/software-engineering agents as the first demanding workload rather than the ontology boundary.

The harness must be embeddable with aligned semantics into:
- GUI;
- TUI;
- CLI;
- API/service;
- SDK/library;
- headless/background execution;
- distributed/at-scale execution.

Client/application layers must not own or redefine core agent semantics merely because a capability first appeared in a CLI fork.

The canonical architecture should decompose application/client presentation away from agent/harness semantics so HeliosLab, a canonical CLI, services and other consumers can use the same underlying execution model without terminal wrapping, transcript scraping, or CLI-to-GUI projection as the primary integration mechanism.

## Current lineage implications

- Codex upstream is active and materially evolved; Helios CLI is historically useful but currently behind modern Codex. Codex lineage remains strategically valuable because upstream development continues and contribution is possible.
- jcode upstream is active and generally preferred by the user over Forgecode for most use cases. The user is now a jcode contributor. jcode lineage therefore has strategic upstream/contribution value in addition to local implementation value.
- Forgecode/HeliosLite remains attractive for lighter ephemeral/headless/light-chat use because of its smaller/lighter character, but Forgecode upstream is effectively sunset relative to the two active upstream lineages. HeliosLite survives as a standalone product only if a role exists that Codex/jcode plus the shared harness cannot satisfy cleanly.
- The mature topology may be segmented clients/runtimes with justified roles or a superset/converged product. Fork ancestry alone does not justify segmentation.

## Agentora / PhenoShared hypothesis

Historical intent assigned Agentora the product-neutral agent SDK/runtime layer: lifecycle, graph/workflow, tools, memory/checkpoints, provider ports, approvals, events, cancellation, retries, tracing/replay and versioned contracts. UI/presentation/branding/packaging and product-specific persistence are outside that core.

Prior archaeology found Agentora-related descendants in PhenoShared (including pheno-agent / daemon / skills surfaces) but did not prove complete SDK absorption, build inclusion, semantic parity or active consumers.

Therefore:
**Do not assume Agentora is merged into PhenoShared. Audit it.**
Classify every Agentora obligation as PRESENT_EQUIVALENT, PRESENT_CHANGED, PARTIAL, ABSENT, SUPERSEDED, or REJECTED, and trace active consumers.

## Research mandate

Do not derive the canonical harness merely by extracting common code from Codex, jcode and Forgecode.

Run an independent SOTA program across:
1. agent theory / decision processes / planning / reflection / memory / tool use / delegation;
2. agent-computer interfaces and environment design;
3. single-agent and multi-agent orchestration;
4. durable execution / checkpointing / retries / idempotency / effect reconciliation;
5. scheduling, concurrency, backpressure and distributed execution;
6. sandbox/workspace/process/container/VM abstractions;
7. context construction, compaction, caching, memory and retrieval;
8. provider/model routing and capability negotiation;
9. tools, MCP/A2A/other interoperability and typed capability systems;
10. permissions, policy, approvals, secrets/IAM and trust;
11. streaming/event semantics and client-independent state projection;
12. observability, tracing, replay, evaluation and MACE/autograder control loops;
13. human-agent collaboration and intervention;
14. failure semantics, cancellation, worker replacement and recovery;
15. cost/resource budgets and QoS;
16. agent identity, durable effort, product state and evidence authority;
17. extensibility/plugin systems;
18. production control planes and fleet management;
19. coding-agent-specific ACI, repository/worktree/build/test semantics;
20. generic non-coding workloads to falsify coding-specific ontology assumptions.

Research production systems, research harnesses, papers, benchmarks and adjacent distributed-systems/workflow literature. For every major primitive decide USE / INTEGRATE / ADAPT / FORK / LEARN / REJECT / CUSTOM with evidence.

## Initial external architecture signals — 2026 pass 1

- OpenAI Agents SDK deliberately exposes a small core around agents, runner-managed turns/tools, handoffs/agents-as-tools, guardrails, sessions, HITL and tracing. Its trace model explicitly spans workflow/task/turn/agent/generation/tool/guardrail/handoff events.
- Microsoft Agent Framework separates agent programming from a Durable Task extension that supplies persistent sessions, checkpointing, recovery and distributed scaling; its orchestration layer offers sequential/concurrent/handoff/group-chat/magentic patterns.
- OpenHands explicitly describes three layers for software-agent systems: harness, orchestrator and control plane.
- SWE-agent research provides direct evidence that the agent-computer interface itself changes software-agent performance; environment/interface design is therefore a first-class harness concern, not presentation polish.

These are research inputs, not adopted architecture.

## Required decomposition gate

Before choosing the canonical CLI base or HeliosLab runtime, define and experimentally validate boundaries among:
- Agent Kernel;
- Model/Provider Runtime;
- Tool/Capability Runtime;
- Context/Memory;
- Workspace/Environment Runtime;
- Durable Effort / Workflow Orchestrator;
- Scheduler/Fleet Runtime;
- Policy/Approval/IAM;
- Evidence/Evaluation/Grader;
- Event/Projection API;
- Control Plane;
- Client/Application adapters.

Assume this decomposition is wrong and actively search for alternative decompositions. Do not freeze it from terminology alone.

## Program scope

The two active primary repository subjects remain HeliosLite and KCode. Codex/Helios CLI, Agentora/PhenoShared, HeliosLab and external harnesses are evidence/donor/alternative surfaces in this pair program, not additional primary repository recoveries.
