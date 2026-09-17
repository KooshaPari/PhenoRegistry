# ADR-DEP-014 — Make human, agent and automation parity a platform tenet

**Status:** accepted_user_constraint

## Decision

All product surfaces share one typed capability/control/evidence model. Humans may get richer presentation, agents structured operations, and automations event/idempotency support, but none receives a second source of truth.

## Alternatives tested conceptually

- GUI-first with private backend state: rejected by the direct requirement.
- Agent-only API with human UI as an afterthought: rejected because humans remain first-class.

## Revisit / closure

Only by explicit user change to the global product tenet.

Sources: S052.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
