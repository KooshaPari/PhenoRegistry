# Tracera Genesis

**Status:** substantive reconstruction, still incomplete pending exhaustive alias/conversation archaeology.  
**Last substantive review:** 2026-09-29.  
**Canonical product:** Tracera.  
**Historical retrieval names:** Trace RTM, TraceRTM, TracerTM, Featuregraph, Feature Graph, feature graph, product graph, product-state graph, semantic/evidence graph, world model/product-evidence graph, live product-state control plane.

## Why this document exists

Tracera spans more than a year of evolving first-principles product thinking, multiple names, implementations and external research programs. The owner should not have to remember the prerequisite reasoning that produced the current product definition.

This document preserves the conceptual lineage. It is not a substitute for detailed requirements or architecture.

## Origin — before "Tracera"

The original idea did **not** begin as an attempt to modernize DOORS, Jama, Polarion, ATOMS.tech or another requirements tool.

It emerged from the owner's own difficulty building products and keeping a complete mental model of them.

The naive question was essentially:

> Can we graphify a product?

The important leap was that a software product can be decomposed in several simultaneously valid ways, and those decompositions can be connected.

By August 2025 the Feature Graph conception included, at minimum:
- user-facing/product behavior;
- technical/functional structure;
- UI/wireframe structure;
- WBS/task structure;
- QA/testing;
- JSON/LLM-readable representation;
- deep links to code and tests;
- visual manipulation inspired by graph/node editors and Figma/web-creator tools.

A defining early principle was already:

> **The diagram is the product skeleton. Editing the graph should edit the product**, directly where deterministic transforms are possible or by dispatching realization work.

This predates the later deep PLM/ALM research and should not be retroactively described as derived from those systems.

## Contemporary ATOMS experience — related context, not origin

The owner was working with ATOMS.tech in a capstone context around the period the graph idea developed.

ATOMS reinforced the value of rigorous traceability, but the owner considered its then-current framing too centered on a human requirements engineer and a Notion/Word/Excel-like authoring interface with AI assistance.

The stronger hypothesis that emerged independently was that agents change the **economics** of traceability.

Historically, DOORS/Jama/Polarion-class rigor was rational mainly in regulated or very complex environments because humans had to continuously maintain requirements, links, evidence and state.

If machines can maintain most of that bookkeeping, rigorous traceability may become economically rational for:
- ordinary software;
- consumer products;
- SaaS;
- small teams;
- solo builders;
- agent-built products.

Humans can concentrate on intent, decisions, exceptions, strategy and taste.

This is a hypothesis to test, not an assumed market truth.

## From Feature Graph to persistent product model

The concept broadened beyond a diagram or RTM.

A product needed persistent identity and multiple projections over shared meaning:

### Experience
Product → application/surface → page/screen → region/section → interaction/action/state → observable behavior.

### Functional
Product → domain/pillar → capability → feature → sub-feature → requirement/constraint.

### Architecture/runtime
System → service/application → package/module → interface/API/event → implementation → artifact/deployment/runtime.

### Supply chain
Product/release → package/component → dependency → version/license/vulnerability/provenance.

### Verification
Requirement/quality property → criterion → oracle → test/measurement → run → evidence.

### Intent/documentation
Product → accepted baseline → requirement/spec/ADR/design/doc → revisions/provenance.

The important property is that these are **projections over one product**, not unrelated inventories.

An interaction can implement a capability, invoke an API, be realized by source artifacts, be documented by a spec and be verified by tests/evidence.

## Prescriptive graph

Tracera was never intended to be only a reverse-engineered knowledge graph.

The graph is both descriptive and prescriptive.

A graph delta can represent a desired product delta:

```text
accepted product graph
 → proposed graph delta
 → impact
 → authorization
 → realization work
 → implementation/artifacts
 → evidence
 → reconciliation
 → new accepted/observed product state
```

The worker can be:
- human;
- agent;
- deterministic transform;
- workflow;
- external organization.

Worker identity must not define product truth.

## Separation from AgilePlus

As the ecosystem evolved, a clean distinction became important.

**AgilePlus** owns durable development/change execution:
- working change intent;
- specification evolution;
- plans/work packages;
- execution claims/leases;
- attempts/workers;
- review;
- work completion;
- execution receipts.

**Tracera** owns persistent product truth:
- product identity;
- accepted product intent;
- product structures/projections;
- configuration/baselines;
- realized/observed state;
- evidence interpretation;
- dissatisfaction;
- product-stage interpretation.

An agent attempt is ephemeral.

An AgilePlus development effort is durable across attempts.

Tracera product state is durable independently of AgilePlus.

Work completion is evidence/context, not product acceptance.

## Dissatisfaction and continuous improvement

The graph became more valuable when treated as a computable model of disagreement between what the product should be and what evidence says it is.

Important distinctions emerged:
- accepted intent;
- designed;
- implemented;
- built;
- released;
- deployed;
- observed.

A product can disagree with itself across these axes.

Dissatisfaction includes:
- missing capabilities;
- failed proof;
- stale proof;
- contradictory proof;
- trace gaps;
- regressions;
- quality failures;
- realization drift.

This moved Tracera from "traceability database" toward a continuous product improvement/control system.

## MACE / ZyBooks influence

The strongest shared inspiration for Tracera and AgilePlus is educational autograding, particularly the experience of ZyBooks-like systems.

The useful property is not merely automated tests. It is a visible target and rapid feedback loop:

```text
attempt
 → independent grade
 → localized failure
 → correction
 → new attempt
 → measurable convergence
```

The owner does not regard workers optimizing toward an oracle as inherently bad. The goal is to construct an oracle whose green state is difficult to obtain without actually improving the accepted outcome.

For Tracera this becomes a product-level MACE loop:
- multidimensional position;
- delta;
- slope/trajectory where statistically meaningful;
- regressions;
- stagnation;
- oscillation/thrashing;
- uncertainty;
- evidence freshness;
- transition debt.

A raw percentage is insufficient.

"30% complete" must distinguish a scaffold, broad husk, closed vertical slice and narrow usable product.

## Mature-first stages

Another stable principle is that CVP/MVP/etc. are not disposable products invented sequentially.

Start from the mature intended product contract.

Stages are projections over it.

Early stages should be encapsulated and usable while preserving a spine that survives later growth:

> **Stub the breadth; mature the spine.**

A CVP that must throw away its core identity/state model to become MVP is architecturally worse than one that grows primarily by enrichment/addition.

## External research changed the semantics, not the origin

Deep 2026 research into ALM, PLM, MBSE, configuration management, digital thread, software catalogs, provenance and AI-native requirements systems revealed that many Tracera capabilities are not novel individually.

Not differentiators by themselves:
- requirements management;
- trace matrices;
- AI-generated requirements;
- requirement↔code/test links;
- AI-maintained trace links;
- impact analysis;
- baselines;
- variants;
- graph visualization;
- agent/MCP access.

PLM/ALM also exposed underdeveloped semantics:
- stable identity vs revision vs artifact version;
- configuration;
- effectivity/applicability;
- product variants;
- as-intended/as-designed/as-built/as-deployed/as-observed;
- suspect links;
- change objects;
- lifecycle/release/support/retirement.

These should refine Tracera rather than turn it into a clone of enterprise ALM/PLM.

The surviving thesis is closer to:

> **A machine-maintained, multi-projection, evidence-reconciled model and control system for a product, where proposed graph changes can represent proposed product changes and agents can use measurable product state to drive verified improvement.**

## Bootstrap philosophy

Tracera should not become a parser farm or proprietary replacement for every lifecycle standard.

Prefer integrating/adapting:
- Git/code intelligence;
- OpenAPI/GraphQL/AsyncAPI;
- SBOM/provenance standards;
- CycloneDX/SPDX;
- in-toto/SLSA;
- OpenTelemetry;
- SARIF;
- test-result formats;
- OSLC/ReqIF/SysML interchange;
- software catalogs;
- authentication.

Custom effort should concentrate where the product thesis actually lives:
- cross-projection canonical identity/semantics;
- accepted vs inferred vs observed authority;
- applicability/configuration-aware evidence;
- graph-delta/product-change semantics;
- dissatisfaction;
- product-stage/shape grading;
- MACE trajectory;
- reconciliation across authoritative systems.

## Current conceptual frontier

The present program is testing:
- ontology/identity/configuration v0;
- typed effectivity;
- evidence reuse/subsumption;
- compatibility certificates;
- criterion dependency footprints;
- suspect/invalidation propagation;
- one real vertical product-truth slice through persistence, machine interface and human projection.

These experiments may still invalidate parts of the current ontology.

## Stable invariants recovered so far

1. The product—not tickets—is the canonical object.
2. Multiple product decompositions must remain connected.
3. Editing the graph can represent editing the product.
4. Product truth must survive workers, chats, devices and work systems.
5. Work completion is not product acceptance.
6. Evidence must bind to what was actually evaluated.
7. Missing/unknown/stale/conflicting proof cannot silently green.
8. Agents should maintain most traceability bookkeeping if the economic thesis is to succeed.
9. Human judgment remains important for intent, authority, taste and irreducibly subjective decisions.
10. Progress must expose usable shape and multidimensional convergence, not merely activity or one percentage.
11. External standards/primitives should be reused when they already solve commodity subproblems.
12. Historical rationale must itself be preserved as product memory.

## What could still falsify Tracera

- agent-maintained graph cost exceeds the value it creates for ordinary software;
- inferred links create too much noise/human review;
- configuration/effectivity semantics become too expensive outside regulated products;
- a composition of existing ALM/catalog/code-graph/evidence tools provides the same value with lower integration cost;
- product graph editing does not improve realization/verification;
- MACE metrics encourage gaming rather than durable improvement;
- the canonical ontology cannot represent heterogeneous products without becoming unusably generic.

These belong in the eventual pilot, not hidden as assumptions.

## Recovery note

This Genesis is SUBSTANTIVE, not yet VERIFIED_RECOVERY_GRADE.

Remaining work includes deeper alias/conversation archaeology, exact provenance links for more historical milestones, and a fresh-human/fresh-agent recovery exercise.
