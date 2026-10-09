# Tracera Research Pass 5 — Synthesis Gate and Next Architecture Experiments

**Status:** NOT FINAL; synthesis after Passes 1-4.
**Date:** 2026-09-29.

## 1. What the research has falsified

The following are not sufficient reasons for Tracera to exist:
- requirements management;
- traceability matrices;
- requirements↔code/test/evidence links;
- AI-generated requirements;
- AI-inferred/maintained links;
- change impact;
- baselines/audit;
- variants/configurations;
- software catalog graph;
- code graph;
- runtime telemetry graph;
- SBOM graph;
- agent/MCP access.

Existing systems already provide these individually or in significant combinations.

## 2. Strongest surviving product thesis

Tracera is a **machine-maintained, multi-projection, evidence-reconciled product model and control system**.

Its kernel should make it possible to:
1. represent one product through multiple interoperable projections;
2. preserve stable identity/revision/configuration/applicability across those projections;
3. distinguish accepted intent, proposed change, realized artifacts, deployment and observed behavior;
4. connect claims to exact evidence with authority/confidence/applicability;
5. detect disagreement/dissatisfaction among product states;
6. represent a graph delta as a proposed product delta;
7. compile realization work to external workers/AgilePlus;
8. reconcile resulting artifacts/evidence back into product truth;
9. expose multidimensional MACE position/trajectory to humans and agents;
10. automatically discover/reconcile much of the model from existing artifacts so ordinary products can afford the rigor.

## 3. Candidate kernel objects after research

Not final schema; candidates for prototype/falsification:

- ProductFamily
- Product
- ProductEntity (stable identity)
- Revision
- ProductStructureView / Projection
- Relation
- Applicability / Effectivity
- Configuration
- Baseline
- Claim / Requirement / Constraint / Target
- Design/Interface
- ImplementationArtifact
- BuildArtifact
- Release
- Deployment
- Environment
- Observation
- Evidence
- Attestation
- Assessor/Verifier
- Finding/Dissatisfaction
- ProductChange / GraphDelta
- Decision
- LifecycleState
- Journey
- Criterion/Oracle/Grader
- EvaluationAttempt/ResultVector
- ExternalReference

Prefer standards-backed submodels/adapters where possible.

## 4. Authority lattice

Every fact/relation needs more than confidence.

Candidate authority classes:
- accepted product fact;
- deterministic source-system fact;
- verified observation/evidence;
- authorized human decision;
- agent/inference candidate;
- imported unverified claim;
- superseded/historical fact.

Inference confidence and authority are orthogonal.

A 0.99-confidence inferred edge is still not the same thing as an accepted or deterministic fact.

## 5. Relation semantics

Candidate relation record must support:
- stable relation identity;
- typed source/target;
- projection/view membership;
- applicability/effectivity;
- valid/effective time;
- transaction/record time;
- configuration/baseline context;
- provenance/source;
- authority;
- confidence where inferred;
- status: candidate/accepted/rejected/suspect/superseded;
- validator/last-checked revision.

This is materially richer than the current SWEE edge.

## 6. Suspect/invalidation engine

Borrow the mature ALM insight: a trace link may continue to exist while becoming semantically suspect.

When a linked endpoint changes:
- mark dependent claims/evidence/relations potentially invalid;
- use dependency/applicability rules to determine what can be safely reused;
- schedule deterministic/agent revalidation;
- preserve old evidence against its original configuration.

This should be a core dissatisfaction primitive.

## 7. Configuration resolver

Prototype a resolver inspired by PLM effectivity:
- common overloaded product structure;
- conditional relations/options;
- resolve a product projection for a target context;
- explain why each node/edge is included/excluded;
- determine whether evidence applicability subsumes the target context.

Contexts for software include version, platform, environment, tenant/edition, feature flags, rollout cohort, region, dependency/API versions and time.

## 8. Standards adapter strategy

Prototype adapters before inventing schemas:
- OSLC RM/CM resources/configurations;
- SysML v2 API/model elements;
- CycloneDX BOM + Declarations/Attestations;
- SPDX where relevant;
- in-toto/SLSA provenance;
- OpenTelemetry resources/signals;
- SARIF;
- OpenAPI/AsyncAPI/GraphQL;
- Git/OCI;
- JUnit/coverage formats;
- Backstage catalog entities;
- ReqIF for requirements interchange.

## 9. Product discovery pipeline experiment

Select one ordinary software repo and attempt:
1. deterministic extraction;
2. standard-format imports;
3. LLM candidate mapping;
4. confidence/authority assignment;
5. contradiction/gap detection;
6. minimal human decisions;
7. resulting graph quality measurement.

Measure:
- human minutes required;
- compute/token cost;
- precision/recall of links against manually checked sample;
- unsupported claims;
- useful impact queries;
- maintenance cost after a real change.

This directly tests the economic thesis.

## 10. Alternative stack baseline

A fair "Tracera does not exist" baseline should compose best-of-breed tools rather than one strawman:

- AI-native requirements/traceability (ATOMS or Trace.Space where accessible);
- Jira/Linear or equivalent work system;
- Backstage/catalog;
- GitHub/Git;
- CI/test management;
- SBOM/provenance/security tools;
- OpenTelemetry/observability;
- code intelligence;
- custom glue/agents.

Compare integration/maintenance burden as part of the result.

## 11. Pilot metrics

- time/cost to bootstrap product model;
- ongoing maintenance cost;
- human decisions per change;
- trace-link precision/recall;
- stale/suspect-link detection;
- impact-analysis precision/recall;
- false-green rate;
- regression discovery;
- time to answer product questions;
- agent task success with/without graph context;
- context tokens/cost;
- stage/readiness estimate calibration;
- graph-edit→realization success;
- evidence reuse accuracy;
- recovery after context loss;
- product-model drift;
- ordinary-software ROI.

## 12. Architecture experiments before final schema

A. relational/SQLite logical graph vs embedded graph engine for local-first queries.
B. applicability/effectivity resolver.
C. suspect-link invalidation.
D. multi-projection UI over shared entities.
E. graph-delta impact preview.
F. evidence applicability/subsumption.
G. unknown-repo discovery.
H. MACE product trajectory.
I. standards adapters.
J. worker-neutral AgilePlus handoff/reconciliation.

The mature ontology should be amended from experiment results rather than designed entirely on paper.

## 13. Research still outstanding

Pass 5 does not close Tracera research. Still required:
- more AI-native competitor discovery;
- deeper ATOMS/Trace.Space technical teardown where evidence is available;
- targeted GitHub open-source project/library shortlist after search rate-limit recovery;
- academic paper matrix;
- Teamcenter/3DEXPERIENCE/Aras/Windchill deeper PLM comparison;
- software product-line engineering;
- ReqIF/STEP/AP242 applicability;
- UI graph-editor SOTA;
- graph database/query benchmark;
- explicit current-code migration impact;
- external reviewer/falsification pass.

## 14. Gate

Do not return to "100% specification complete" until:
- outstanding research is either completed or explicitly proven irrelevant;
- build/bootstrap decisions are recorded;
- candidate differentiators survive direct comparison;
- ontology amendments are applied;
- architecture experiments close high-risk unknowns;
- source ledger and semantic requirement catalog are re-run against the amended architecture.
