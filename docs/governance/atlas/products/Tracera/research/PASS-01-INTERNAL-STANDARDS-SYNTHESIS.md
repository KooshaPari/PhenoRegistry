# Tracera research corpus — Pass 1 synthesis

**Status:** INCOMPLETE / research pass 1.
**Date:** 2026-09-29.
**Purpose:** durable synthesis of internal archaeology + current repo evidence + external primary-source SOTA. This document is not a final architecture decision.

## 1. Internal research already present in PhenoRegistry

A June 10, 2026 archived research conversation (`handbook/specs/research/ecosystem/ChatGPT-Software Project Traceability Tools.md`) already surveyed:
- DOORS/ELM, Polarion, Jama, Codebeamer-class ALM;
- StrictDoc, Doorstop, OpenFastTrace, BASIL;
- QA/test management;
- BDD;
- API/contract testing;
- formal/model-based specification;
- software/code/knowledge graphs.

It reached an early conclusion that the missing primitive was not simple RTM but a repo/product-native graph coupling intent/spec/requirements/contracts/models/tests/code/runtime evidence/agent work into an executable oracle.

The same archive recovered:
- the multi-view product knowledge graph interpretation;
- SBOM, threat model, ADR, DFD, observability, runbook, compliance and agent artifacts as graph peers;
- four broad evidence roles: Intent / Design / Implementation / Evidence;
- the graph-as-authoritative/prescriptive-product idea;
- unknown-repository inspection as graph discovery;
- the Gradescope/ZyBooks asymptotic position+slope framing;
- Claim as a candidate central object: a statement the system should/does/continues to satisfy, backed by validator/evidence/confidence/status.

This prior work must be reconciled rather than repeated.

## 2. Standards/primitives that appear directly reusable

### OSLC family

OSLC RM defines open REST/RDF resources for requirements and collections. OSLC AM links architecture resources with change requests, tasks, requirements and tests. OSLC Configuration Management defines versions/configurations across linked-data resources from multiple lifecycle domains.

**Potential Tracera import:** do not invent every cross-tool lifecycle vocabulary/protocol. Evaluate OSLC resource/link/configuration semantics as an interchange and federation layer while keeping Tracera's richer internal ontology.

### SysML v2 / KerML / Systems Modeling API

SysML v2 now has formal semantics, textual + graphical syntax, explicit requirements/behavior/structure/analysis/verification modeling, standard API/services, model libraries and machine-readable schemas. Its API explicitly supports access, navigation and operation on models plus interoperability with engineering/enterprise tools.

**Potential import:** views/viewpoints, structure/behavior/requirement/constraint separation, allocations/interfaces, model libraries, standard model API patterns. Do not turn Tracera into SysML; map useful semantics into software/product projections.

### CycloneDX 1.7 / Attestations

CycloneDX now models much more than dependency inventory: configuration, evidence, formulation, attestations, threat models, adversary models, risk assessments, claims/counterclaims, assessors, targets, mitigation, confidence and evidence.

**Major implication:** parts of Tracera's Claim/Evidence/Target/Assessor ontology may be standardizable or directly representable through CycloneDX instead of custom schema.

### in-toto / SLSA

in-toto provides signed layouts describing intended supply-chain steps/functionaries and signed link metadata recording commands/materials/products. SLSA defines increasing provenance trust levels.

**Potential import:** exact execution/candidate provenance and authorization evidence; avoid inventing weaker build/step receipt formats.

### OpenTelemetry

OpenTelemetry provides standardized semantic conventions for traces, metrics, logs, profiles and resources.

**Potential import:** runtime-observation projection should ingest/relate OTel semantics rather than create a rival telemetry ontology.

### OpenFeature

OpenFeature formalizes feature-flag evaluation context across global/client/invocation scopes.

**Potential import:** configuration/effectivity projection should understand feature-flag evaluation and context instead of representing flags as static booleans.

### Backstage catalog

Backstage already defines software entities, references, relations, statuses, entity lifecycle, graph views and extensibility.

**Potential import:** catalog/entity reference patterns and ingestion; Tracera should not hand-roll commodity service-catalog discovery where Backstage-compatible metadata exists.

## 3. Emerging architectural hypothesis

Tracera should not attempt to replace every lifecycle source system.

A stronger architecture is a **canonical product model + projection/federation/reconciliation engine**:

```text
accepted product claims / model
            |
   canonical identity + relations
            |
  +---------+----------+----------+----------+
  |         |          |          |          |
SysML/MBSE OSLC ALM  Git/code   CycloneDX  OTel/runtime
  |         |          |          |          |
  +---------+----------+----------+----------+
            |
      normalized projections
            |
    assessment / dissatisfaction
            |
      proposed product delta
            |
         AgilePlus
            |
       realized artifacts
            |
       evidence/reconcile
```

The internal ontology must support native software/consumer-product semantics while adapters preserve authoritative external formats and identities.

## 4. Product graph dimensions now requiring explicit ontology review

- identity and aliases;
- product structures/projections/viewpoints;
- requirements/claims/constraints/targets;
- UI/experience/journey/action/state;
- architecture/system/service/component/module/interface;
- API/schema/event/data flow;
- source/code symbols;
- dependencies/SBOM/licenses/vulnerabilities;
- configuration/variant/effectivity/feature flags;
- build/artifact/release/channel;
- deployment/environment/runtime;
- telemetry/SLO/incident/problem;
- tests/verification/validation/oracles/results;
- evidence/attestation/provenance/confidence/counterevidence;
- threat/risk/control/mitigation;
- docs/ADR/decision/rationale;
- lifecycle/revision/baseline/change;
- external work references;
- agent/human actions as provenance, not canonical product truth.

## 5. Key distinction to preserve

The original Feature Graph thesis remains broader than classic ALM:
- multiple projections over one product;
- graph is prescriptive as well as descriptive;
- editing the graph can propose/edit the product;
- machine-maintained links make rigor economically viable outside regulated engineering;
- product state is reconciled from evidence, not work-item status;
- the primary consumer can be an agent.

External systems should improve Tracera's semantics, not collapse it back into document-centric requirements engineering.

## 6. Open research questions for Pass 2+

1. Can CycloneDX Attestations satisfy enough Claim/Evidence semantics to adopt it as a first-class interchange?
2. How much SysML v2/KerML should be mapped vs reused directly?
3. Is OSLC Configuration Management sufficient for cross-domain baseline/configuration semantics?
4. What PLM concepts are still missing after OSLC/SysML: effectivity, BOM views, as-designed/as-built/as-maintained, change orders, variants?
5. What is the correct temporal model: valid time, transaction time, baseline revision, observed time, effectivity interval, or combination?
6. How should inferred/agent-proposed edges differ from accepted/manual/deterministic edges?
7. How are confidence, contradiction and counterevidence represented without letting probabilistic inference rewrite facts?
8. Which graph engine/query model best supports typed multi-projection traversal plus temporal/effectivity semantics?
9. What external AI-native requirements competitors (ATOMS, Trace.Space and broader set) already implement from this list?
10. What should the post-build alternative stack contain for a fair pilot?

## 7. Coverage state

Pass 1 is NOT complete:
- external GitHub discovery hit a search-rate limit and needs targeted continuation;
- direct ATOMS/Trace.Space competitor teardown still needs a dedicated pass;
- PLM vendor/standard semantics need deeper primary-source study;
- academic software knowledge-graph/trace-recovery literature needs a dedicated paper pass;
- internal alias archaeology is improved but not exhausted;
- current Tracera source tree still has unresolved source-ledger rows.

Do not use this document to claim SOTA closure.
