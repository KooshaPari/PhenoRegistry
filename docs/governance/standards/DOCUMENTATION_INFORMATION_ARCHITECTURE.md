# Documentation Information Architecture Standard

**Status:** proposed portfolio standard; required for recovery-grade dossiers.  
**Date:** 2026-09-29.

## Core pattern: bulkhead → modules → evidence

Every major documentation concern is a **directory with a strong top-level bulkhead**, not a lone markdown file.

Example:

```text
docs/
  intent/
    README.md                 # bulkhead
    product-thesis.md
    actors-and-jobs.md
    boundaries.md
    invariants.md
    non-goals.md
    economic-thesis.md
    mature-horizon.md
    raw-intent/
      README.md
      ...
  sota/
    README.md                 # bulkhead
    landscape.md
    direct-competitors/
    adjacent-fields/
    standards/
    academic/
    open-source/
    technical-comparisons/
    bootstrap-decisions/
    differentiation/
    alternative-stack.md
    unresolved.md
  genesis/
    README.md                 # bulkhead
    chronology.md
    origin.md
    aliases.md
    conceptual-pivots.md
    surviving-invariants.md
    rejected-framings.md
    provenance/
  architecture/
    README.md
    system-model.md
    ontology/
    decisions/
    experiments/
    alternatives/
  verification/
    README.md
    mace.md
    oracle-model.md
    evidence.md
    negative-controls.md
    progress-model.md
  ...
```

The exact hierarchy is product-specific. Do not create empty directories merely to mirror this example.

## Bulkhead contract

A bulkhead is intentionally concise relative to its subtree, but still substantive.

It must answer without opening child files:

1. What is this documentation domain?
2. Why does it matter to this product?
3. What are the current accepted conclusions?
4. What remains proposed/uncertain?
5. What changed recently?
6. What are the strongest invariants/decisions?
7. Where should I go for each deeper question?
8. What source/evidence backs the summary?
9. What is stale/incomplete?
10. What downstream product decisions depend on it?

The bulkhead is **not**:
- a table of contents with no content;
- an executive summary that omits caveats;
- a duplicate of every child file;
- a dumping ground for all details.

## Progressive disclosure

Target three useful depths.

### Level 0 — dossier / product bulkhead
5–10 minute whole-product recovery.

### Level 1 — domain bulkhead
5–15 minute recovery of one domain such as intent, SOTA, architecture, verification, lifecycle.

### Level 2+ — focused modules/evidence
Deep work: competitor teardown, paper appraisal, ontology object, experiment, decision, raw intent, source receipt.

A reader should be able to stop at any level and still receive a truthful picture.

## Bidirectional navigation

Every focused module should link upward to its bulkhead.

Bulkheads link downward by **question**, not merely filename.

Example:

- "Why does this product exist?" → origin/economic thesis.
- "What would we use instead?" → alternative stack.
- "Which competitor invalidated this differentiator?" → differentiation ledger.
- "Why is this schema field present?" → ontology decision/experiment.
- "Where did this user intent come from?" → raw-intent provenance.

## Avoid duplication drift

Facts have canonical homes.

Other documents summarize and link.

Examples:
- detailed competitor evidence lives under `sota/direct-competitors/`;
- `sota/README.md` summarizes conclusions;
- dossier summarizes only product-level consequences.

When a fact must be repeated for readability, label the canonical source or generate the projection automatically.

## Domain status header

Every bulkhead should expose machine-readable or consistently structured metadata:

```text
Status: accepted | proposed | mixed | historical | incomplete
Recovery grade: missing | stub | partial | substantive | recovery-grade | verified
Last substantive review:
Source/product revision:
Supersedes:
Known stale zones:
Blocking gaps:
```

## Intent subsystem

`docs/intent/README.md` is the authoritative current-intent bulkhead.

Suggested modules:
- thesis;
- problems/pains;
- actors/jobs/outcomes;
- scope/boundaries;
- invariants;
- non-goals;
- economic thesis;
- mature horizon;
- terminology;
- raw-intent index;
- unresolved questions.

Genesis explains **how intent got here**. Intent explains **what is accepted now**.

## SOTA subsystem

`docs/sota/README.md` answers:
- landscape;
- strongest alternatives;
- what is commodity;
- what remains differentiated;
- what we reuse;
- what we custom-build and why;
- major unresolved research questions.

Depth should split by:
- competitor family;
- direct competitor;
- adjacent discipline;
- standard;
- academic paper/topic;
- open-source implementation;
- technical architecture;
- build/buy/bootstrap decision;
- pilot baseline.

A single giant `SOTA.md` is not acceptable for a research-heavy product.

## Genesis subsystem

`docs/genesis/README.md` should make conceptual history recoverable while remaining readable.

Depth can include:
- chronological eras;
- historical aliases;
- major raw-intent events;
- pivots;
- external-context relationship;
- abandoned interpretations;
- invariant lineage;
- provenance index.

## Architecture subsystem

Separate:
- current accepted architecture;
- candidate/proposed architecture;
- ontology/data model;
- ADRs/decision records;
- architecture experiments;
- rejected alternatives;
- migration/transition plan.

Do not make readers infer accepted architecture from a pile of ADRs.

## Requirement/specification subsystem

Large products need navigable requirement domains rather than one huge file.

Bulkhead explains:
- product hierarchy;
- requirement semantics;
- source coverage;
- quality overlays;
- stages;
- traceability;
- unresolved gaps.

Requirements remain machine-addressable and can be generated/projected into human views.

## Current-state subsystem

Keep current state small and frequently refreshed.

It should link to durable history rather than accumulating it.

Answer:
- what exists now;
- usable shape;
- verified state;
- current blockers;
- active experiments;
- next frontier;
- what changed since prior checkpoint.

## Raw intent subsystem

Raw intent is high-value evidence but should not swamp curated docs.

Store/index:
- date;
- source conversation/file;
- speaker/authority;
- aliases/topics;
- faithful summary;
- extracted invariants;
- unresolved questions;
- affected canonical docs/decisions;
- incorporation status.

## Automated validation opportunities

Eventually validate:
- every bulkhead exists for an active deep domain;
- no orphan modules;
- child→parent links;
- broken links;
- stale revision references;
- status metadata;
- raw intent incorporation status;
- decision supersession links;
- source/evidence references;
- duplicate canonical claims.

Semantic quality still requires human/agent review.

## Recovery test

A fresh reader gets only the product dossier bulkhead.

They must be able to:
1. understand the product;
2. choose the correct domain bulkhead;
3. descend to the needed depth;
4. recover evidence/rationale;
5. return to the current work frontier.

If successful recovery requires repository-wide grep or chat archaeology, the documentation IA has failed.
