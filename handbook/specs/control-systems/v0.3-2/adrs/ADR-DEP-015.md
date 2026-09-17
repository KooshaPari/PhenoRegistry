# ADR-DEP-015 — Use one Assessment Dossier with inventory and evaluation phases

**Status:** proposed

## Decision

Phase A captures inventory/applicability/evidence and leaves verdict/score unknown; Phase B binds qualified instruments and records evaluation. Both phases mutate/append the same dossier authority and generate views.

## Alternatives tested conceptually

- Separate inventory database and scorecard database: rejected for identity and drift risk.
- Single flat score sheet: rejected because unknown/applicability/evidence states collapse into misleading scores.

## Revisit / closure

Only if a concrete consumer requires a distinct projection; the canonical dossier remains singular.

Sources: S053, S054.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
