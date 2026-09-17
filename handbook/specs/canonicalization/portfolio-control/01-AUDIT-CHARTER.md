# Portfolio audit charter

## Mission

Determine, for every repository and every material cross-repository capability:

1. Why it exists.
2. Which human or accepted product intent supports it.
3. What it owns and explicitly does not own.
4. What is specified, implemented, verified, demonstrated, and operable.
5. Which claims are unsupported, contradictory, stale, or superseded.
6. Whether it is the correct repository boundary.
7. Whether its product or component has a defensible reason to exist against available alternatives.
8. The smallest safe sequence that moves it to a terminal state: retained and complete, absorbed, split, converted to an adapter/fork, archived, retired, or explicitly research-only.

## Units of analysis

The audit must not treat “repository” as the only object. It operates on:

| Object | Purpose |
|---|---|
| Human source | Verbatim prompt, decision, mandate, or constraint |
| User job/journey | Outcome a user or operator wants |
| Product/program | Coherent external or internal value proposition |
| Capability | Stable behavior or outcome independent of current code location |
| Component/package | Implementation unit |
| Contract | API, schema, protocol, CLI, file format, policy, or compatibility promise |
| Repository | Versioning/governance/release container |
| Revision/branch | Historical implementation candidate |
| Test/oracle | Machine-verifiable behavioral expectation |
| Evidence | Reproduction, benchmark, release, deployment, user observation, or trace |
| Consumer | Code, operator, product, or ecosystem member depending on a contract |
| Authority | Canonical writer and source of truth for an entity/domain |
| Disposition | Retain, absorb, split, merge, adapt, incubate, archive, retire, or research |

The capability graph is primary. Repository boundaries are a proposed partition of that graph.

## Scope

All 146 repositories observed under `KooshaPari` are in census and lineage scope regardless of visibility, fork status, or archive state.

Depth is risk-triggered:

- Every repository receives metadata, role, authority, intent, and disposition analysis.
- Active/canonical/product candidates receive current-tree, build, quality, and product-surface analysis.
- Contradictory, duplicated, extracted, regressed, or historically significant repositories receive branch/commit forensics.
- Archives need not be modernized, but their intent, provenance, consumers, and recovery value must be understood before disposal decisions.

## Non-goals

- Producing the same giant documentation tree in every repository.
- Maximizing the number of active projects.
- Minimizing the raw GitHub repository count at any cost.
- Rewriting every product from scratch.
- Requiring public novelty from internal foundations, compatibility adapters, or forks.
- Treating all upstream-derived repositories as original products.
- Trusting source code, docs, or tests without cross-checking the other layers.
- Advancing all repositories in parallel.
- Letting local agents settle cross-repository ownership by editing READMEs.
- Declaring a global final topology before lineage and consumer evidence exists.

## Authority model

### Portfolio adjudicator

The portfolio adjudicator is the only role that may propose or approve:

- Canonical product and capability ownership.
- Repository births, absorptions, splits, mergers, and retirements.
- Cross-repository IDs and event/schema authorities.
- Public brand set and strategic-fork allowance.
- Ecosystem-wide exceptions and policy changes.
- Final current → transition → target map.

### Family lead

A family lead may:

- Investigate a bounded repository family.
- Build semantic and Git lineage maps.
- Compare capabilities and consumers.
- Propose target boundaries and migration alternatives.
- Produce a family pilot and consolidation dossier.

A family lead may not archive siblings or declare a final authority without central review.

### Repository closure agent

A repository agent may:

- Preserve and reconstruct local intent.
- Audit current and historical code in authorized scope.
- Complete missing docs and quality infrastructure after the canonical role is known.
- Implement bounded work packages.
- Produce evidence and a proposed disposition.

It may not invent cross-repo contracts or overwrite richer local SSOT systems merely to conform to a template.

### Independent verifier

The verifier must be separate from the implementing agent for material completion gates. It checks evidence, negative controls, build inclusion, release artifacts, migrations, and pilot fairness.

## Evidence classes

Every material statement uses one class:

| Code | Meaning |
|---|---|
| `HUMAN_SOURCE` | Verbatim human instruction or explicit decision |
| `ACCEPTED_CONTRACT` | Approved requirement, ADR, API, or compatibility commitment |
| `OBSERVED_STATIC` | Present in a specified revision/path |
| `REPRODUCED` | Executed under a recorded environment with retained output |
| `RELEASED` | Present in a published artifact with provenance |
| `OPERATED` | Observed in a real deployment/use flow |
| `VENDOR_CLAIM` | Claim made by an external project/vendor |
| `INFERENCE` | Reasoned conclusion from cited evidence |
| `HYPOTHESIS` | Unverified proposition with a falsification route |
| `UNKNOWN` | Evidence unavailable or unresolved |
| `SUPERSEDED` | Historically valid but no longer authoritative |

“Shipped,” “complete,” and “production-ready” are not evidence classes.

## Claim confidence

Confidence and evidence class are separate. A static source observation can be high-confidence as a source fact while remaining weak evidence that the product works. Use:

- High: multiple consistent primary sources or direct reproducibility.
- Medium: credible but incomplete evidence.
- Low: conflicting, indirect, or environment-dependent evidence.
- Unknown: not investigated.

## Terminal repository states

Every repository must eventually reach one of:

- `CANONICAL_ACTIVE`
- `CANONICAL_MAINTENANCE`
- `STRATEGIC_FORK`
- `ADAPTER_OR_PACKAGING`
- `FOUNDATION_PACKAGE_HOME`
- `APPLIED_PRODUCT`
- `LAB_INCUBATOR`
- `MIGRATING`
- `COMPATIBILITY_BRIDGE`
- `ARCHIVED_PROVENANCE`
- `RETIRED_REDIRECT`
- `BLOCKED_DECISION`
- `UNKNOWN_REQUIRES_FORENSICS`

“Active” without a role is not terminal.

## Change safety

The first portfolio pass is read-only except for generated audit artifacts. Repository mutation begins only after:

1. Observation refs and dirty state are recorded.
2. Canonical role is provisionally approved.
3. Source and target responsibilities are mapped.
4. Migration and rollback plans exist.
5. Consumer and compatibility impact is known.
6. Bounded work packages are issued.

Archives and forks are never deleted as the only remaining provenance.
