# Tracera internal archaeology aliases and recovered lineage

**Status:** active research index.
**Updated:** 2026-09-29.

## Search aliases

Historical/internal searches for Tracera MUST include independently:
- Tracera
- Trace RTM / TraceRTM
- TracerTM
- Featuregraph / Feature Graph / feature graph
- product graph
- product-state graph
- semantic/evidence graph
- world model / product-evidence graph
- live product-state control plane
- feature-graph / product-graph terminology without the Tracera name

Do not assume searches for "Tracera" recover the original design discussions.

## Recovered lineage

### 2025-08-21 — original feature-graph conception

The project began from a first-principles desire to decompose even a simple CRUD product into atomic linked views:
- user-facing/product behavior;
- technical/functional behavior;
- UI/wireframe structure;
- WBS/task structure;
- QA/testing.

The graph was intended to be JSON/LLM-readable, self-hosted, deeply linked to code/tests, and useful for implementation/testing/status/scope management.

The defining rule was already present: **the diagram is the product skeleton; editing the graph should edit the product**, either directly through deterministic/codegen transforms or by orchestrating agents.

UI ambitions included robust node editing comparable to React Flow/node-programming tools plus Figma/web-creator style manipulation.

### 2026-06 — graph-first agent development concepts

Related discussions developed task nodes carrying:
- task spec;
- minimal context bundle;
- acceptance contract;
- sandbox/guardrails;
- grading harness;
- action trace.

Agent work was conceived as graph-specialized execution with divergence scoring, persistent repo memory, verification and escalation.

### 2026-07 — Tracera as canonical product state

The concept expanded into a canonical traceable graph for an entire digital software product spanning:
- requirements;
- UI trees;
- APIs;
- SBOM;
- tests;
- contracts;
- architecture;
- implementation;
- evidence.

Important state distinction: declared, implemented, built, tested, deployed and observed are not interchangeable.

Every product-changing operation should originate as, or reconcile into, a versioned graph transition. A graph action is a proposal until realized and reconciled with evidence.

Worker neutrality became explicit: the same desired graph transition may be fulfilled by a human, workflow, agent, or deterministic transform.

### 2026-07-17 — experience/problem projections

The graph expanded to model actor, context, device, journey, interactions, friction, interventions, technical traces, evidence and simulations, with views across time, cost, effort, risk and confidence.

### 2026-08 — shared semantic/evidence and runtime projections

Feature/product graph work was explicitly placed in Tracera's semantic/evidence graph. Cross-links included requirement→feature→component→function→test→evidence and runtime dimensions such as execution, placement, memory, surface, transport, latency, energy and economics.

### 2026-09 — mature-first product oracle

Current clarification adds:
- persistent global scope across repos/devices/releases;
- PLM/ALM/SDLC/configuration-management mining;
- multi-projection product model;
- graph-as-product-editor;
- agent-maintained traceability economics;
- dissatisfaction detection;
- CVP/MVP/GA/mature projections;
- product shape vs raw completion;
- stub-first/minimally-changing growth;
- MACE/ZyBooks-style multidimensional oracle and trajectory.

## Research implication

Internal archaeology is incomplete until searches across all aliases and dates have been exhausted. Historical names are not separate products unless evidence establishes otherwise; they are retrieval keys for the same evolving Tracera thesis.
