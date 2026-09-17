# Reusable product dossier template

## Corpus basis and use

Reviewed 2026-09-17: all 34 current dossier files exist under `products/`, including
`products/.github/DOSSIER.md`. File existence is not product acceptance or active-owner status.
The corpus has three heading families: 23 numbered execution dossiers, nine role-specific
qualification dossiers, and two scope/evidence dossiers. No single dossier clearly provides
a uniquely strongest complete structure, so this template consolidates their common obligations.
Existing dossiers need not be rewritten or have their headings renamed.

| Required concern | Numbered execution family | Role-specific family | Scope/evidence family |
|---|---|---|---|
| Identity and preserved boundary | Metadata and section 1 | Role/class and scope notice | Scope |
| Source-grounded atlas | Section 2 | What must be understood | Explanatory atlas |
| Evidence and unresolved obligations | Section 3 | Evidence before a status change | Current evidence and unresolved obligations |
| Reuse and maintenance trade-offs | Section 4 | Maintenance reduction | Reuse and evolution |
| Bounded pilot and measurements | Sections 5–6 | Qualification | Bounded pilot and QA |
| Ownership and next handoff | Section 7 | Coordination | Ownership and coordination |
| Delivery proof and consumer acceptance | Section 8 and ecosystem acceptance | Qualification and ecosystem acceptance | QA and acceptance obligations |

Use the sections below for a new dossier or a targeted update. Link canonical state, pilot,
and proof records rather than duplicating them. Retain historical observation dates and scope
holds. Mark missing evidence UNKNOWN and non-applicability with an explicit rationale.
Follow [START-HERE](../START-HERE.md) and [SSOT authority](../SSOT_AUTHORITY.md).

## 1. Identity, scope and preservation

Record product/capability name, role/class, immutable repository ID or unresolved identity,
source revision, observation date, accepted owner and lifecycle. Link current state and next
activities where available. Define the actual useful acceptance journey and preserved backlog.
A narrow pilot does not authorize deletion, revival, migration, publication or scope reduction.

## 2. Explanatory atlas

List concrete questions and source-bound answers covering build roots, public entrypoints,
packages/symbols, state/configuration ownership, dependencies, consumers and distribution.
Preserve lineage, provenance, constraints and unknown intent. File names and static reachability
alone do not establish purpose, completeness or permission to delete.

## 3. Evidence and carry-forward obligations

Record prior findings with original dates/revisions, accepted requirements, unresolved questions,
and the evidence needed to revalidate or supersede each finding. Separate proposed work from
observed results. Historical failures and successes are not automatically current verdicts.

## 4. Comparator, reuse and maintenance decisions

Version-pin relevant peers and upstreams. Record retain/adopt/patch/wrap decisions per subsystem,
including functional, security, recovery, portability, performance and maintenance trade-offs.
Identify patch ownership and upstream strategy. Test advantage hypotheses rather than assuming them.

## 5. Controlled pilot and measurements

Specify bounded inputs, supported profiles, independent outcome oracles, comparison conditions,
and positive/negative cases. Include interruptions, recovery and isolation where applicable.
Preserve failures, interventions and uncertainty. Define each metric and its independently agreed
required denominator before measurement. A pilot plan is not an executed result.

## 6. Ownership and next deliverable

Assign an existing product owner, independent assurance responsibility and integration owner,
without imposing historical permanent-chat allocations. Name the next bounded task, dependencies,
permissions, expected artifact and exact proof required. Maintain sole write ownership per path.

## 7. Delivery gate and cross-ecosystem acceptance

Bind proof to the revision, artifact and supported profile. Require the applicable clean-install
journey, independent unit/integration/E2E checks, qualified negative controls and real consumer
acceptance. Report failures, skipped checks and missing platforms explicitly. Apply the governing
[assurance contract](ASSURANCE-CONTRACT.md), [metrics](METRICS.md),
[negative controls](NEGATIVE-CONTROLS.md) and
[ecosystem acceptance rules](../architecture/ECOSYSTEM-FIRST-EVOLUTION.md).
Keep inventory, candidate creation, local validation, hosted validation and delivered acceptance
separate. Preserve critical obligations and consumer contracts. Do not equate clean Git status,
file existence or a numerical grade with delivered acceptance.
