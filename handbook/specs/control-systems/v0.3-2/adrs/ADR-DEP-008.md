# ADR-DEP-008 — Preserve local dev and use typed delivery profiles

**Status:** proposed

## Decision

Default the requested dev backend to the qualified local target. Separate environment names from resource targets and workload types. Implement this in the existing API/automation ownership path, leaving BytePort as the product GUI.

## Alternatives tested conceptually

- Render-for-all: contradicts local placement and makes provider quota a hidden requirement.
- One container deploy for all repos: misclassifies packages, desktop releases and documentation.
- Local and managed profiles through one validated contract: preferred design.

## Revisit / closure

Confirm target/module ownership and application profiles before mutation; source placement is explicit but the implementation is not accepted.

Sources: S032, S033, S040.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
