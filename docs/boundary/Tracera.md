---
repo: "Tracera"
product_id: "PRD-TRACERA"
role: canonical-product-system-model
status: active
last_boundary_review: 2026-09-29
contract: TRC-MATURE-V1
in_scope:
  - "Persistent product identity and accepted intent baselines"
  - "Product pillars, features, sub-features, requirements and stage projections"
  - "Canonical product/evidence graph and bounded traversal"
  - "Bidirectional traceability to implementation, tests and evidence"
  - "Deterministic assessment and dissatisfaction discovery"
  - "Product shape, VP readiness, closure, survivability and transition grading"
  - "Human and agent views over canonical product state"
  - "History, provenance and impact reasoning"
  - "External work references without owning work execution"
out_of_scope:
  - capability: "Canonical work planning/execution state machine"
    lives_in: "AgilePlus"
  - capability: "Generic agent runtime"
    lives_in: "AgentMCP/agent runtime owners"
  - capability: "Generic source-code search"
    lives_in: "HeliosLab / source-search owner"
  - capability: "Git object/source authority"
    lives_in: "source repository"
---

# Boundary — Tracera

Tracera owns **product truth and product-state interpretation**, not every system it can observe.

## Core boundary

```text
accepted product intent
 -> canonical product hierarchy/graph
 -> links to source/work/test/evidence facts
 -> assessment
 -> dissatisfaction
 -> stage/shape/product-state projection
```

Trace/session ingest, memory, SWEE, optional stores, analytics and platform adapters are supporting/enabling surfaces when they serve this boundary.

## Work-system boundary

AgilePlus owns execution. Tracera may project work items, resolution references and completion observations, but work completion MUST NOT itself satisfy a product requirement. Re-verification is required.

## Source/evidence boundary

Source repositories own exact source revisions. Verifiers own measurement results. Tracera records stable references, provenance and interpretation; it is not a replacement Git store or verifier.

## Stage boundary

CVP/MVP/GA/Mature are projections over one mature contract. A capability can be core to mature Tracera while not required for CVP.

## Auxiliary work

UX polish, optimizations, maintenance and optional integrations can add value without increasing core functional completion unless they satisfy accepted FRs.

## Growth boundary

Prefer mature-shaped stable boundaries with minimal real implementations that enrich in place. Throwaway implementations are allowed only with explicitly bounded replacement/migration cost.

## Supersession

The 2026-09-20 boundary centered trace-link graph + memory distillation as Tracera's identity. Those remain supported candidate capabilities but no longer define the top-level product boundary.
