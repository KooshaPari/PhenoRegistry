# ADR-DEP-002 — One deployment actuator and existing ownership spine

**Status:** proposed

## Decision

Reuse the existing logical owners; reconcile current module locations before allocating implementation. Do not create a new controller or registry.

## Alternatives tested conceptually

- Independent BytePort and PaaS reconcilers: reject for duplicate writes.
- Assume consolidation is complete because a README says so: reject without receipts.

## Revisit / closure

Current ownership ADR, consumer graph and migration receipt review.

Sources: S002, S003, S004, S005, S006, S007.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
