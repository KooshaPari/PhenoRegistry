# Tracera Research Pass 4 — Research, Open Source and Technical Bootstrap Map

**Status:** INCOMPLETE.
**Date:** 2026-09-29.

## 1. Open-source requirements/traceability substrates

### StrictDoc
Relevant as a repo-friendly structured requirements/document system with source traceability ambitions.
Potential reuse:
- human-readable requirements/spec authoring;
- stable IDs and document structure;
- source markers;
- import/export patterns.
Likely not sufficient as Tracera core: document-centric and narrower ontology.

### Doorstop
Requirements-as-code/YAML, hierarchy and trace validation.
Potential reuse:
- simple repo-local requirement representation/import;
- validation ideas.
Not sufficient for multi-projection product state.

### OpenFastTrace
Lightweight trace tags/spec items and coverage reports.
Potential reuse:
- source-tag import/export;
- simple trace validation.
Not a product graph.

### BASIL / ELISA ecosystem
Worth mining for safety-oriented software traceability, work-item completeness and source/spec relationships.

**Decision direction:** adapters/importers are more attractive than making one of these Tracera's canonical data model.

## 2. Code/property graphs and repository intelligence

Families to study:
- CodeQL;
- Joern/code property graph;
- Sourcegraph-style code intelligence;
- SCIP/LSIF;
- tree-sitter;
- language-server indexes;
- emerging repository knowledge graphs for coding agents.

### Bootstrap principle

Tracera should not parse every programming language itself.

Use established parsers/indexes for:
- symbol identity;
- definitions/references;
- call/import relations;
- source spans;
- type/schema information.

Then relate these engineering facts to product concepts.

SCIP-like stable code-intelligence indexes are particularly relevant as a language-agnostic ingestion boundary.

## 3. Automated trace-link recovery

Academic and industrial work exists on:
- information-retrieval requirement↔code links;
- embedding/LLM-assisted link recovery;
- heterogeneous software knowledge graphs;
- combining semantic and structural signals;
- impact propagation.

### Required Tracera distinction

An inferred edge is not an accepted fact.

Every inferred trace link should carry:
- derivation method/model/version;
- confidence;
- source evidence;
- status (candidate/accepted/rejected/superseded);
- validation history;
- applicability/configuration.

Agent inference proposes graph structure; deterministic/source-system evidence and authorized decisions establish stronger authority.

## 4. Graph storage/query candidates

Do not choose graph technology by product metaphor.

Compare:
- relational adjacency/recursive CTEs;
- PostgreSQL + JSON/graph extensions;
- SQLite local graph tables;
- Neo4j;
- Memgraph;
- Kuzu/embedded graph;
- DuckDB/analytical projections;
- RDF/triplestore/SPARQL where standards interoperability matters.

Evaluation dimensions:
- local-first embedding;
- typed constraints;
- temporal/effectivity queries;
- version/configuration queries;
- provenance;
- traversal latency;
- incremental updates;
- portability;
- operational cost;
- ecosystem/library maturity.

A logical graph API should insulate product semantics from storage choice.

## 5. Knowledge graph / RDF possibility

OSLC and many engineering interoperability standards are RDF/linked-data oriented.

Tracera does not necessarily need an RDF-native core, but should test:
- URI/stable identity conventions;
- typed predicates;
- SHACL-style validation;
- RDF-star/provenance approaches;
- mapping to/from internal typed graph.

Avoid creating an ontology that cannot federate with lifecycle standards.

## 6. Event sourcing vs graph history

Current product ideas mix append-only observations, graph mutations, revisions and historical state.

Need to compare:
- event sourcing;
- bitemporal relational storage;
- immutable graph facts;
- snapshot + delta;
- CRDT/event-log patterns for distributed editing.

Likely architecture:
- authoritative immutable events/changes;
- materialized current graph projections;
- version/configuration snapshots;
- append-only evidence;
rather than treating graph rows themselves as the only history.

This is a hypothesis pending implementation-cost review.

## 7. Evidence and provenance bootstrap

Use existing standards where possible:
- in-toto/SLSA for build/execution provenance;
- CycloneDX/SPDX for supply chain;
- OpenTelemetry for runtime observations;
- SARIF for static-analysis/security findings;
- JUnit/TRX/etc. adapters for test results;
- coverage standard formats;
- Git object identities;
- OCI digests for images/artifacts.

Tracera should normalize references/claims, not invent proprietary replacements for every evidence format.

## 8. Verification/autograder technical lineage

Study and potentially borrow from:
- Gradescope/ZyBooks-style autograders;
- online judges;
- SWE-bench evaluation harnesses;
- property-based testing;
- mutation testing;
- fuzzing;
- model checking/formal verification;
- differential/metamorphic testing;
- CI DAGs;
- benchmark/evaluation harnesses for agents.

Key architectural import:
a grader is a versioned executable measurement with applicability and evidence, not merely a test-file link.

## 9. MACE technical needs

Need first-class data for:
- EvaluationAttempt;
- Grader;
- Criterion;
- Oracle;
- ResultVector;
- FailureClass;
- EvidenceSet;
- ProgressDelta;
- dependency/invalidation graph;
- retry lineage;
- context bundle;
- escalation.

Tracera aggregates these at product scope; AgilePlus owns bounded work-attempt execution.

## 10. Product discovery / brownfield bootstrap

An unknown repository/product should enter Tracera through a discovery pipeline:

```text
raw sources
 -> deterministic inventory
 -> source-system imports
 -> inferred candidate entities/links
 -> confidence/provenance
 -> contradiction/gap analysis
 -> authorized acceptance where needed
 -> continuously reconciled model
```

Potential deterministic inputs:
- repository manifests/lockfiles;
- routes;
- OpenAPI/AsyncAPI/GraphQL schemas;
- database schemas/migrations;
- UI route trees;
- SBOM;
- CI workflows;
- deployment manifests;
- tests;
- docs/ADRs;
- telemetry/resource metadata.

LLMs enrich/interpret; they should not replace deterministic extraction where parsers exist.

## 11. Build-vs-bootstrap direction

### Strong bootstrap/integration candidates
- parsers/code intelligence;
- SBOM/provenance formats;
- runtime telemetry;
- ALM/requirements import;
- SysML/OSLC interchange;
- test result formats;
- Git/OCI identities;
- graph rendering/layout libraries;
- auth/SSO;
- generic search/indexing.

### Likely Tracera-owned semantics
- cross-projection canonical product identity/model;
- accepted vs inferred vs observed authority model;
- graph delta/product edit semantics;
- evidence applicability/invalidation;
- dissatisfaction;
- product-stage/shape grading;
- MACE product trajectory;
- reconciliation across authoritative systems.

## 12. Remaining Pass 4 work

- targeted GitHub repository discovery after API rate limit;
- concrete library/project shortlist with license/health/API analysis;
- academic paper matrix with datasets/metrics/limitations;
- graph-engine benchmarks against Tracera query shapes;
- trace-link recovery benchmark strategy;
- source-language/code-intelligence ingestion architecture;
- UI graph editor/library comparison;
- external schema adapters proof-of-concept plan.

Do not claim technical-bootstrap closure yet.
