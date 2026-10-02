# Tracera PLM Change-Semantics Addendum

**Date:** 2026-09-29.
**Status:** candidate architecture import.

## Mature PLM pattern

PLM systems commonly separate:

```text
Problem / finding
  -> Change Request
     (change desired; does not itself modify product)
  -> authorized Change Order / Directive
     (approved implementation intent + affected items/effectivity)
  -> Change Actions / execution
  -> implementation verification/audit
  -> released/revised/obsolete product items
```

Aras explicitly distinguishes Problem Report, Engineering Change Request, and Engineering Change Notice/Order; Windchill similarly separates configuration-level Change Directives, Change Actions and Design Solutions with effectivity.

## Mapping to Tracera + AgilePlus

```text
Tracera Finding / Dissatisfaction
  -> Tracera ProductChange proposal / GraphDelta
  -> authorized product-change contract
  -> AgilePlus realization work
  -> exact artifacts + execution receipts
  -> Tracera independent verification/reconciliation
  -> new accepted/released product revision/configuration
```

## Important invariant

- Finding is not change.
- Proposed change is not authorized change.
- Authorized change is not implementation.
- Implementation is not verification.
- Work completion is not released product truth.
- Release does not erase prior configuration/evidence.

This separation should become explicit in the ontology and autograder.

## What not to import

Do not copy mandatory change boards, fixed human roles or document-heavy enterprise workflow into ordinary software. Authority and risk determine required review depth; agents/deterministic systems may perform many activities.

## Useful PLM semantics to retain

- affected-item set;
- impact analysis;
- add/change/delete/revise/release/obsolete actions;
- effectivity of a change;
- implementation plan;
- validations before transition;
- independent verification;
- revision/lifecycle update after successful reconciliation;
- rollback/rework/re-execution paths.
