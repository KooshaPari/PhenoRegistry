# ADR-DEP-018 — Salvage Emergent Garden Wave 5 before starting another research wave

**Status:** proposed

## Decision

Preserve PR-81 head/payload, reconcile it with current ResearchLedger main, rerun bundle/tests, then land or explicitly supersede it before new corpus expansion. Keep registry projection qualified during the gap.

## Alternatives tested conceptually

- Restart research from YouTube: rejected because substantial validated work already exists.
- Treat merged registry projection as proof the ResearchLedger source landed: rejected; projection and source authority are separate.

## Revisit / closure

After source-authority integration is demonstrably complete.

Sources: S061, S062, S063, S064.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
