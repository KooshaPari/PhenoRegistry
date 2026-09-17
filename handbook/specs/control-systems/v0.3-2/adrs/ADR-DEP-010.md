# ADR-DEP-010 — Quarantine the recovered pilot as evidence, not a deployment template

**Status:** proposed

## Decision

Keep the recovered snapshots read-only for regression tests. Replace defects through reviewed patches in the resolved owner; do not execute this transcript or promote the old ready claim. Require source-mode binding, supported workflow locations, exact check mappings, secret isolation and recovery acceptance before rollout.

## Alternatives tested conceptually

- Commit and run the old pilot: known semantic and safety defects.
- Discard the old pilot: loses useful provenance and regression fixtures.
- Preserve evidence and repair narrowly: preferred.

## Revisit / closure

A clean current revision, settings receipt and disposable end-to-end proof can supersede the historical findings.

Sources: S032, S033, S034, S035, S036, S037, S038, S039.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
