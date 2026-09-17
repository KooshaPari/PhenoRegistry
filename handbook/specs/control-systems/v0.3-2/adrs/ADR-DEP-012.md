# ADR-DEP-012 — Use immutable pull delivery for personal compute nodes

**Status:** proposed

## Decision

CI builds/tests/publishes immutable artifacts; the controller authorizes desired state; an outbound/private node daemon pulls exact artifacts and reports observed identity.

## Alternatives tested conceptually

- CI SSH/push directly into personal machines: rejected as a broad credential and lifecycle boundary.
- Mutable latest-tag deployment: rejected because tested bytes are not bound to observed runtime bytes.

## Revisit / closure

A substrate with equivalent authenticated content-addressed pull and stronger attestation.

Sources: S052, S058.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
