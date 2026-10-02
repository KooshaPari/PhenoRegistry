# Product Dossier Standard — Durable Human + Agent Memory

**Version:** 0.1 proposed  
**Applies to:** portfolio product/repository programs.  
**First pilots:** Tracera and AgilePlus.

## Purpose

A dossier is the durable recovery surface for a product whose development spans chats, humans, agents, repositories and years.

It is not a compliance folder. Its acceptance criterion is:

> A future human owner or fresh capable agent can reconstruct the product's identity, intent, history, rationale, architecture, state and next frontier without replaying years of conversations.

## Required dossier zones

### 00 START HERE
Reading map for:
- 5-minute recovery;
- 30-minute recovery;
- deep reconstruction;
- agent work entry;
- research/SOTA entry;
- implementation/verification entry.

### 01 GENESIS
High-fidelity conceptual lineage:
- motivating pain;
- original formulation;
- historical names;
- chronology;
- user-authored intent milestones;
- major conceptual pivots;
- stable invariants;
- rejected/misleading framings;
- relationship to external inspirations;
- unresolved philosophical questions.

### 02 INTENT
Current accepted product meaning:
- concise definition;
- deep definition;
- jobs/outcomes;
- actors;
- product ownership boundary;
- explicit non-goals;
- mature horizon;
- economic/product thesis;
- invariants.

### 03 ARCHAEOLOGY
Evidence-indexed recovery:
- aliases/search terms;
- conversation/source index;
- repo/history sources;
- predecessor/sibling relationships;
- lost/regressed/stranded capabilities;
- contradictory evidence.

### 04 SOTA + ALTERNATIVES
- competitor classes;
- direct competitors;
- adjacent fields;
- standards;
- research;
- open-source primitives;
- build/buy/bootstrap decisions;
- falsified differentiation;
- surviving differentiation;
- alternative stack.

### 05 PRODUCT MODEL / ONTOLOGY
- canonical entities;
- projections/views;
- identity/version/configuration;
- relations/authority/provenance;
- lifecycle;
- glossary.

### 06 STAGES
- CVP/MVP/Beta/GA/Mature or product-appropriate stages;
- stage outcomes;
- required journeys/features;
- transition debt;
- why each stage is usable and non-disposable.

### 07 JOURNEYS
Actor-to-outcome journeys with dependencies and closure rules.

### 08 REQUIREMENTS + QUALITY
Canonical detailed contract and applicable quality overlays. Count is derived, never targeted.

### 09 ARCHITECTURE + DECISIONS
Current architecture plus ADR/decision lineage:
problem → alternatives → evidence → decision → consequences → supersession.

### 10 MACE / VERIFICATION
- grading ontology;
- acceptance/oracles;
- evidence identity;
- progress vector/trajectory;
- anti-Goodhart rules;
- negative controls;
- verification gaps.

### 11 IMPLEMENTATION MAP
What exists, where, whether mounted/persisted/tested/evidenced, and historical/regressed implementations.

### 12 CURRENT STATE
Evidence-bound current shape, stage readiness, blockers, uncertainties and transition debt. Never a self-reported single percent.

### 13 WORK / FRONTIER
Current valid work frontier, dependencies, blocked decisions and safe agent entry points. Work system remains authoritative for execution state.

### 14 PILOT / CASE STUDIES
Post-build comparisons against the best realistic alternative stack and no-product/status-quo baseline.

### 15 LIFECYCLE
Release/deployment/operation/deprecation/LTS/retirement and compatibility/migration semantics as applicable.

### 16 RAW INTENT INDEX
Durable index of high-value user-authored prompts/dumps and their curated syntheses. Preserve source distinction:
- raw/verbatim source where legally/technically practical;
- faithful summary;
- extracted invariant;
- affected decisions/specs.

### 17 GLOSSARY
Names, aliases, domain language and terms whose meaning changed over time.

### 18 COMPLETION / RECOVERY TESTS
- source coverage;
- semantic completeness;
- broken-link/schema validation;
- fresh-human recovery test;
- fresh-agent recovery test;
- unresolved blockers.

## Document quality levels

A file/folder is:
- MISSING
- STUB
- PARTIAL
- SUBSTANTIVE
- RECOVERY_GRADE
- VERIFIED_RECOVERY_GRADE

Only the last two are eligible for product-program completion, and VERIFIED requires an actual fresh-context recovery exercise.

## Anti-slop rules

Do not:
- create empty headings to satisfy the schema;
- paste chat transcripts without synthesis;
- replace rationale with a conclusion;
- erase superseded decisions;
- mix user intent and assistant inference without labels;
- duplicate volatile truth across registry/repo without authority rules;
- call a dossier complete from file presence.

## Genesis quality bar

Genesis is unusually important. It should read like a technically rigorous product history, not marketing.

A good Genesis lets the owner recover **why they believed the product should exist before remembering all the details themselves**.

It should preserve prerequisite reasoning:
- the pain/event that triggered an idea;
- observations that made the naive idea plausible;
- what later research changed;
- what survived those changes.

## Storage boundary

PhenoRegistry stores the portfolio-level dossier/index/lineage and durable research pointers.

The product repo stores detailed current product contract, architecture, requirements and executable verification.

Raw conversation source may remain in its original durable archive when copying it would create unnecessary duplication; the dossier must still provide enough provenance to retrieve it.

## Change discipline

Every major new user intent dump triggers:
1. raw-intent/index update;
2. Genesis/Intent impact review;
3. decision/architecture impact review;
4. requirements/journey impact review;
5. current-state/frontier update where applicable.

This should eventually be automatable, but human/agent review remains required for semantic fidelity.
