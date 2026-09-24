# ADR-DEP-013 — Protect foreground work with reservation and preemption policy

**Status:** proposed

## Decision

Model foreground reserves and dynamic host modes as placement inputs. Background workloads are admitted only from allocatable capacity and may be drained/preempted according to declared policy.

## Alternatives tested conceptually

- Pause one runner when Parsec appears: rejected as application-specific and incomplete.
- Static CPU/RAM limit only: rejected because GPU, thermal, battery and interactive latency can dominate.

## Revisit / closure

Measured workload interference data may simplify or specialize the policy per node class.

Sources: S052, S056, S057, S077.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
