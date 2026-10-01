# SOTA research pass 2 — harness decomposition and durability

Date: 2026-10-01. Research inputs, not automatic architecture decisions.

## Modern Codex
OpenAI documents Codex core as the shared harness powering CLI, IDE, web and macOS app, with App Server as a long-lived bidirectional JSON-RPC bridge. One client request can yield many UI-ready event notifications, and the server can initiate approval/input requests. Codex also exposes exec/SDK/MCP embedding options.
Consequence: the old HeliosCLI architecture that severed Codex and kept it as excluded vendored reference is no longer a competitive baseline. Current Codex core/App Server + extensions is a primary alternative.

## Durable execution
Microsoft Durable Task's Agent Framework extension provides persistent sessions, checkpointed multi-agent workflows, distributed scaling and recovery without changing core agent logic; completed calls are not re-executed during recovery.
Temporal provides self-hostable durable execution with event history, workers/task queues, HITL, retries and integrations across multiple agent frameworks. Its architecture treats nondeterministic I/O (LLM/tool/API) as recorded activities and deterministic workflow code as durable orchestration.
Consequence: durable effort is a port/backend boundary. Building a bespoke durable engine requires evidence against these alternatives, especially for local latency, embedding footprint, event/evidence semantics, licensing/operations and extreme concurrency.

## Agent-computer interface
SWE-agent experimentally showed that agent-computer interface design materially changes software-engineering agent performance. Its reported SWE-bench pass@1 was 12.5% and HumanEvalFix 87.7% in the 2024 study; those historical numbers do not establish current SOTA, but the causal design lesson remains relevant.
Consequence: coding ACI/workspace/tool ergonomics are first-class architecture and evaluation subjects, not merely UI polish.

## Evaluation
Agent evaluation literature emphasizes planning, tool use, reflection/memory, application benchmarks, generalist benchmarks, cost efficiency, safety and robustness.
Consequence: MACE grading should remain multidimensional and include cost/safety/robustness rather than a single task-success score.

## OpenHands
Current OpenHands SDK describes a stateless event-driven Agent responsible for reasoning-action loop, tool orchestration, context management and security validation, while Agent Canvas explicitly does not execute actions or provide sandboxing and instead talks to Agent Server/runtime services.
Consequence: another independent implementation supports separating client presentation from agent/runtime services.

## Decisions after pass 2
- USE/LEARN: modern Codex App Server model as key client-projection prior art.
- EVALUATE/INTEGRATE: Temporal and Durable Task as durable-effort backend candidates.
- LEARN: SWE-agent ACI methodology; do not copy historical benchmark claims as current performance.
- LEARN/COMPARE: OpenHands client/server and agent boundaries.
- CUSTOM only after gap evidence: shared authority/evidence/MACE semantics and any latency/scale primitives external systems cannot supply.