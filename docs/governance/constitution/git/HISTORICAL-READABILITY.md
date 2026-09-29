# Git Ledger Clarification — Readability Without Historical Rewrite

**Date:** 2026-09-29  
**Status:** owner clarification; supersedes any interpretation that old commit readability should be repaired by rewriting history.

## Clarification

The existence of a historical commit has value even when its message or integration quality is poor.

Git still preserves:
- added/removed lines;
- parentage;
- ordering;
- tree state;
- authorship/producer metadata;
- later reversions/replacements.

Therefore historical readability is desirable but secondary to preservation.

## Forward rule

For **future** commits:
- prefer coherent transaction boundaries;
- write useful messages;
- link work/decision/product identities where practical;
- preserve evidence/provenance;
- avoid unrelated mega-commits;
- avoid squash/rewrite as normal integration cleanup.

## Historical rule

For **existing** history:
- do not rebase/squash/rewrite merely to improve readability;
- do not mass-edit history to conform to newer conventions;
- preserve ugly or weakly messaged commits as ledger transactions;
- improve interpretation through additive metadata/projections.

Preferred retrospective improvements:
- Genesis/history summaries;
- decision and supersession records;
- commit-range maps;
- regression/recovery dossiers;
- release notes;
- PR/work-item links;
- annotations or Git notes where operationally safe and useful;
- Tracera-derived semantic summaries;
- explicit "introduced by / reverted by / superseded by" relations.

The objective is to make history **legible without changing history**.

## Principle

```text
preservation > cosmetic historical cleanup

future semantic quality > accepting future slop

curated projection + immutable ledger > rewritten ledger
```

A future agent should be able to recover meaning from poor historical commits without pretending those transactions were originally cleaner than they were.
