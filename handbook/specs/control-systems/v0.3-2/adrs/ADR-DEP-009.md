# ADR-DEP-009 — Use a tested event predicate and observed deployment watermark

**Status:** proposed

## Decision

Proposed default: changed identity AND (scheduled tick OR new commits > 1 OR authorized force), after qualification gates. Persist the successful observed identity; use environment lease and generation fencing. Do not treat workflow attempts or API acceptance as last deployed.

## Alternatives tested conceptually

- Every push: simpler but does not preserve >1.
- Cron only: ignores requested threshold responsiveness.
- Event predicate with explicit counting basis: preferred.

## Revisit / closure

The exact commit-count convention and missed-tick coalescing are implementation choices proposed here, not historical user-approved policy.

Sources: S032, S033.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
