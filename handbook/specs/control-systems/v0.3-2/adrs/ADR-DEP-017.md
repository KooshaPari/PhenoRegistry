# ADR-DEP-017 — Reconcile historical review findings after merge

**Status:** proposed

## Decision

A merged/closed PR finding is revalidated against current main. Valid surviving defects create a remediation item/new PR; fixed/stale/duplicate/false-positive findings receive evidence-backed dispositions. Old thread state is not treated as code truth.

## Alternatives tested conceptually

- Bulk resolve all old threads: rejected because unresolved can still mean real defect.
- Automatically open a fix PR for every old bot comment: rejected because stale/duplicate/false-positive findings create churn.

## Revisit / closure

After historical backlog reaches a stable SLA and can move to continuous reconciliation.

Sources: S052, S065, S066, S070.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
