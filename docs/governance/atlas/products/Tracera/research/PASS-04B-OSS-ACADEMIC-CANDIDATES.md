# Tracera Research Pass 4B — Concrete Open-Source and Academic Bootstrap Candidates

**Status:** active supplement to Pass 4.
**Date:** 2026-09-29.

## Concrete candidates discovered

### Repository/context graph layer

**agentforge-graph**
- typed repository graph for symbols, calls/imports, API routes, ORM models, architecture decisions and Git history;
- provenance-tracked;
- MCP-served;
- supports federated workspaces.
**Decision direction:** study as ingestion/context substrate or reference implementation; this category is not Tracera differentiation.

**ContextGraph**
- tree-sitter based scope-correct code graph;
- local SQLite;
- MCP;
- resolved call edges/blast radius;
- ingests docs, PDFs, SQL schemas/config.
**Decision direction:** strong reference for deterministic brownfield discovery and one-call agent context.

**CodeGraphAgent**
- code graph optimized for agent calls;
- filesystem remains source of truth;
- watcher/resilience concerns for multiple coding agents.
**Decision direction:** useful for context API ergonomics and stale-index semantics.

**Vellis / Bibliotek**
- typed local-first reified graph for agents;
- explicit schema, validation, migration, deterministic query, audit, snapshots/replay, MCP.
**Decision direction:** investigate reusable graph/controller components and authority/migration patterns; not product-specific enough to replace Tracera.

### Graph database layer

**LadybugDB (formerly Kuzu)**
- embedded property graph;
- Cypher;
- full-text/vector;
- columnar storage;
- serializable ACID;
- Rust bindings;
- Wasm.
**Important project-health finding:** original Kuzu repository was archived; Ladybug is the continuation. Do not adopt old Kuzu merely from historical popularity.

**zu**
- very new Rust embedded graph design with native/SQLite/S3 engines and one query processor;
- currently early/not usable.
**Decision direction:** research inspiration only, not production dependency yet.

Need later benchmark against PostgreSQL/SQLite logical graph and Neo4j.

### Variability / product-line engineering

**Universal Variability Language (UVL)**
- 2025 JSS standardization effort;
- Boolean/Arithmetic/Type levels;
- human-readable pivot language;
- open parsers/tooling;
- FeatureIDE/flamapy ecosystem.
**Decision direction:** evaluate UVL as interchange/constraint language for Tracera variant/configuration projection rather than inventing a proprietary feature-model language.

Feature-model evolution research also demonstrates that configurations and feature models evolve over time and can require constraint/soundness reasoning. Tracera's applicability/configuration resolver should learn from this literature.

## Academic findings

### Automated requirement→code trace recovery

2026 Information and Software Technology work combines LLM-driven augmentation with an encoder and reports material improvements over multiple baselines. Key lesson: automated trace recovery is an active ML problem and inferred links need calibrated evaluation, not product claims based on anecdotal LLM success.

**Tracera implication:** maintain benchmark datasets/precision-recall for inferred links; store derivation method/version/confidence; inference never silently becomes accepted authority.

### Digital thread / knowledge graph

Recent digital-thread work repeatedly emphasizes:
- heterogeneous lifecycle integration;
- standardized semantics;
- ontology;
- storage;
- access;
- end-to-end traceability;
- interoperability;
- model/version/configuration management.

A 2026 framework explicitly decomposes digital thread into integration, ontology, storage and access subsystems. This is a useful architecture review lens for Tracera.

2020+ knowledge-graph digital-thread research demonstrates fusing heterogeneous standards-based lifecycle views rather than replacing them with one proprietary format.

### Software product lines

UVL and SPL literature reinforce:
- feature commonality/variability;
- cross-tree constraints;
- configuration derivation;
- evolution over time;
- lifted analyses that reason over product families without brute-force enumerating every variant.

**Tracera implication:** evidence/impact analysis should eventually support family-level reasoning and avoid evaluating every possible configuration individually when reusable symbolic/lifted analysis is available.

## New anti-hand-roll decisions

Unless later evidence reverses these:
- DO NOT hand-roll language parsers/code graphs where tree-sitter/LSP/SCIP/repository-graph tools suffice.
- DO NOT invent a feature-model/variability language before evaluating UVL.
- DO NOT assume Neo4j is necessary merely because the domain is a graph.
- DO NOT invent proprietary runtime/supply-chain/test evidence formats.
- DO NOT treat inferred trace links as facts.
- DO NOT make repository indexing the Tracera moat.

## Remaining concrete evaluation

For each candidate:
- license;
- project health;
- API/embedding model;
- Rust/TS/Python integration cost;
- incremental update behavior;
- provenance/identity semantics;
- scale/performance;
- migration/export;
- whether it can be consumed as a library vs service;
- fit with offline/local-first requirement;
- security/trust boundary.

No dependency adoption is approved by this supplement alone.
