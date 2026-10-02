# Tracera Intent

**Status:** mixed — core thesis accepted; ontology/details still being falsified.  
**Recovery grade:** SUBSTANTIVE.  
**Last substantive review:** 2026-09-29.

## Concise definition

Tracera is the **persistent canonical product/system model and product-level control system**.

It represents accepted product meaning through multiple connected projections, relates that meaning to realization and evidence, detects dissatisfaction/drift, supports proposed product changes as graph deltas, and gives humans/agents a measurable view of product state and convergence.

## Why it exists

Product knowledge is fragmented across:
- specs;
- UI;
- source;
- APIs;
- dependencies;
- tests;
- CI;
- releases;
- deployments;
- telemetry;
- tickets;
- people/chats.

Humans cannot economically maintain a complete rigorous cross-product model for ordinary software.

The central economic hypothesis is that agents and deterministic extraction can maintain enough of this model that systems-engineering-grade traceability becomes useful outside highly regulated domains.

That hypothesis remains unproven.

## Canonical object

The canonical object is the **product**, not a ticket, repository, agent session or requirements document.

A product may span:
- many repositories;
- many releases/configurations;
- many deployments;
- external services/dependencies;
- human/manual elements;
- many development efforts.

## Multi-projection product model

Tracera must support multiple useful decompositions over shared identities.

Important candidate projections:
- intent;
- functional;
- experience/UI;
- journeys;
- architecture;
- interfaces/API/data;
- implementation;
- supply chain;
- verification;
- security/risk;
- release/deployment;
- runtime/operation;
- documentation/decisions;
- lifecycle.

No single projection is "the product tree."

## Prescriptive + descriptive

Tracera describes what exists and what evidence says.

It also represents desired changes.

A graph delta can mean a proposed product delta:

```text
accepted state
 → proposed delta
 → impact
 → authorized realization
 → artifacts
 → evidence
 → reconciliation
```

Proposal, work completion, implementation, verification and acceptance are distinct.

## Relationship to AgilePlus

AgilePlus owns durable **development effort/work execution**.

Tracera owns durable **product truth**.

Three identities/lifetimes matter:
1. worker attempt;
2. durable development/change effort;
3. product/configuration.

Workers are replaceable.

A completed work item does not satisfy a product obligation without admissible product evidence.

## Product state

Avoid one mutable status.

Distinguish:
- intended/accepted;
- designed;
- implemented;
- built;
- released;
- deployed;
- observed.

Dissatisfaction often exists in the delta between these states.

## MACE

Tracera is also the long-loop product oracle.

It should expose multidimensional:
- position;
- change;
- trajectory where meaningful;
- regression;
- stagnation;
- thrash;
- uncertainty;
- evidence freshness;
- transition debt.

A single percent complete cannot distinguish a scaffold from a narrow functional product.

## Human role

Humans primarily supply:
- intent;
- authority;
- strategic choice;
- exceptions;
- taste;
- irreducibly subjective judgment.

Machines should increasingly maintain:
- inventory;
- trace links;
- implementation mappings;
- evidence;
- drift;
- coverage;
- impact;
- candidate graph updates.

If sustained expert manual graph curation remains necessary for ordinary software, a central product hypothesis fails.

## Mature horizon

A mature Tracera should allow a human or agent to:
- recover what a product is supposed to be;
- navigate from intent to realization/evidence and back;
- understand exact applicable configuration;
- detect unsupported/stale/contradictory product claims;
- understand usable product shape/stage;
- propose product changes in graph terms;
- understand impact before realization;
- delegate realization without transferring product authority;
- reconcile exact resulting artifacts/evidence;
- preserve historical product truth;
- progressively discover an unknown/brownfield product;
- operate across repos/work systems/workers.

## Core invariants

- stable product identity is not repository identity;
- confidence is not authority;
- missing applicability is not wildcard;
- missing/stale/conflicting evidence is not green;
- work completion is not product acceptance;
- inference cannot silently rewrite accepted intent;
- historical evidence remains historically true in its original context;
- multiple projections share canonical identities;
- stage growth should preserve the mature spine;
- commodity standards/primitives should be integrated rather than gratuitously replaced;
- documentation/rationale is durable product memory.

## Explicit non-goals

Tracera is not intended to become:
- a generic coding-agent runtime;
- the canonical work-execution state machine;
- a replacement Git implementation;
- a proprietary telemetry system;
- a proprietary SBOM/provenance format;
- a parser implementation for every language;
- a document-centric clone of DOORS/Jama/Polarion;
- one giant mandatory graph UI.

## Current unresolved questions

- final ontology;
- configuration/effectivity language;
- safe evidence reuse and dependency-footprint derivation;
- suspect/invalidation rules;
- storage/query architecture after real workload benchmarks;
- exact human projection UX;
- brownfield discovery precision/cost;
- economic ROI outside regulated engineering;
- final stage definitions and mature requirement coverage.

## Deeper reading

- [Genesis](../GENESIS.md)
- [SOTA bulkhead](../sota/README.md)
- [Internal archaeology](../INTERNAL-ARCHAEOLOGY.md)
- repo-local `spec/product/ONTOLOGY_IDENTITY_CONFIG_V0.md`
- repo-local `spec/product/MACE_AUTOGRADER_DOCTRINE.md`
- repo-local `spec/product/VERTICAL_SLICE_CONTRACT.md`
