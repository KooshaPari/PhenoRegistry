# Tracera Pass 08 — Ontology and Evidence Applicability Receipt

**Status:** architecture proposal, not accepted mature schema.  
**Tracera commits:** ontology `6dfb3f0e7f2770116aa5502be2a6704984c4902d`; experiment `a92c11b6c66285d47f58cdae447a1a8480ff3656`.

## Architecture changes proposed

Current `ProductId + BaselineRevision` is retained as useful primitive/compatibility state but is insufficient for mature identity.

Pass 08 separates:
- stable product/entity identity;
- entity revision;
- concrete artifact identity/version;
- product configuration;
- frozen accepted baseline;
- deployment;
- observation;
- durable product change;
- external development and attempt identities.

SWEE is treated as an engineering-evidence projection, not expanded into the entire product ontology.

Relations become assertions with authority, provenance, applicability/effectivity, temporal/configuration context and semantic validity state.

## PLM transfer

Aras Effectivity Services is used as concrete prior art for:
- conditions on structure relationships;
- scoped variables;
- resolving a structure for criteria;
- distinguishing an overloaded structure from a configured/resolved view.

Tracera adapts the principle to software dimensions such as release, platform, environment, feature flags, tenant/edition, region and dependency/API/schema versions.

No manufacturing-specific process is imported merely because PLM uses it.

## Evidence reuse rule

Evidence reuse is a proof obligation. Missing applicability dimensions are Unknown, not wildcard.

The first experiment deliberately limits predicates to exact/set/range/time/explicit-any/compatibility-certificate forms. General arbitrary Boolean effectivity syntax is deferred until demonstrated necessary.

The experiment must compare:
1. exact-match-only;
2. typed subsumption;
3. typed subsumption plus explicit compatibility certificates.

It measures safe reuse, forced rechecks, false reuse, unknown rate and required human compatibility decisions.

## Falsification gate

The ontology is not accepted until it can represent product variants, feature flags, coexisting canary/stable deployments, historical-but-no-longer-applicable evidence, suspect relations, cross-projection entities, worker replacement and partially realized/abandoned product changes without destructive history or identity conflation.

No mature completion percentage is derived from this receipt.
