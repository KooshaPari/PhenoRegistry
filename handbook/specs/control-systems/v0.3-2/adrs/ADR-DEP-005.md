# ADR-DEP-005 — Route classes and streaming transport

**Status:** proposed

## Decision

Separate private administration from anonymous public sites and authenticated machine routes. Exclude Quick Tunnels from required SSE paths; qualify the full named-tunnel or private path.

## Alternatives tested conceptually

- Funnel grants visitor identity: false.
- Put browser Access login in front of every webhook: incompatible unless the caller supports it.

## Revisit / closure

Verified hostname ownership, protocol tests, auth policy and origin-bypass tests.

Sources: S022, S023, S024.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
