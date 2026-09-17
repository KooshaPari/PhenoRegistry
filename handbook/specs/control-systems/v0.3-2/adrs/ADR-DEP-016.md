# ADR-DEP-016 — Extend the existing review/GitOps controller with a quota-aware broker

**Status:** proposed

## Decision

Provider adapters expose live quota/trigger/cost/capability state. A risk-tier scheduler assigns the smallest sufficient semantic reviewer set, coalesces reruns, normalizes findings, and reserves capacity for final review.

## Alternatives tested conceptually

- Every provider on every PR: rejected for quota waste, duplicate noise and observed rate-limit failures.
- One fixed reviewer everywhere: rejected for outages, quota exhaustion and blind spots.
- New review product/repository: reject unless current controller ownership cannot absorb the capability.

## Revisit / closure

Measured marginal-yield and reliability data may change default provider weights.

Sources: S052, S065, S067, S068, S069, S070, S071, S072, S074.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
