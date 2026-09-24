# ADR-DEP-001 — Preserve the Podman / WSLC preference

**Status:** accepted_user_constraint

## Decision

Preserve the preference exactly; qualify distinct implementations. Docker Engine remains an exception candidate, not the default.

## Alternatives tested conceptually

- Treat WSLC as shorthand for WSL2: rejected because identity differs.
- Default to Docker for ecosystem convenience: not authorized by the direct constraint.

## Revisit / closure

An operator-approved exact-workload capability or benchmark exception.

Sources: S001, S013.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
