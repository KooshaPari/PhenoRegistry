# ADR-DEP-007 — Separate routing incident evidence from deployment design

**Status:** proposed

## Decision

Preserve sampled routing observations, add request/attempt instrumentation and bounded failover tests, and avoid attributing failures to ingress or model sync without a joined trace.

## Alternatives tested conceptually

- decisions=99 means 99 retries: unsupported.
- HTTP 200 proves useful model output: unsupported.

## Revisit / closure

Exact config/code revision, trace correlation and reproducible failing fixture.

Sources: S001.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
