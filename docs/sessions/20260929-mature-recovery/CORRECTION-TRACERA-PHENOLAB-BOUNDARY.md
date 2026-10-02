# Product-boundary correction — Tracera and PhenoLab

Date: 2026-09-30.
Authority: direct user correction.

## Correct model

**Tracera** is a product-as-graph / feature-graph / traceability product.

**PhenoLab / PhenoLM** is an LLM-oriented experimentation and R&D system.

There is **no product-authority, canonical-state, promotion-target, or semantic ownership relationship between them.**

## Archaeology reconciliation

PhenoLab currently contains historical/operational Tracera integration code and docs:
- trace-store adapter;
- dual-write bridge;
- runtime/configuration;
- evidence/telemetry ingestion.

Those surfaces establish only that PhenoLab can send/store traces through Tracera-compatible infrastructure. They do not establish:
- Tracera as PhenoLab's canonical product state;
- Tracera as promotion authority;
- PromotionRecord/Application targeting Tracera;
- PhenoLab as a Tracera subsystem;
- any requirement that PhenoLab use Tracera.

Treat those sources as **integration/telemetry implementation evidence**, not normative product-boundary evidence.

## Correct PhenoLab ownership

PhenoLab owns its own experiment/R&D state:
AssignmentEpoch, experimental subject/baseline, CandidateLineage, trials/evidence, optimizer feedback, Assessment, Comparison, Decision, experiment persistence, observation and learning.

If an experiment applies a candidate to some external target, that target is generic and experiment-specific. The target may be a repository, model artifact, harness configuration, runtime configuration, deployment, etc. It is **not Tracera by default**.

## Correction to prior recovery work

All earlier recovery artifacts that inferred:
`PhenoLab experimental truth → PromotionRecord/Application → Tracera canonical product truth`
are superseded on that point.

The valid general concept, if retained, is:
`PhenoLab Decision → optional TargetApplication(target_ref)`
with no Tracera-specific semantics.

Historical Tracera trace adapters remain preserved; do not delete them merely because they are not product authority.
