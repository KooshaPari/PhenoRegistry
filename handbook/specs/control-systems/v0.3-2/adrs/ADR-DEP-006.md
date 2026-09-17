# ADR-DEP-006 — Portability by contract, not provider sameness

**Status:** proposed

## Decision

Define target capability differences and state migration explicitly. Do not switch IaC language/tool or assume WASI/native compatibility without a demonstrated need and approved boundary.

## Alternatives tested conceptually

- One IaC provider model equals universal portability: reject.
- WASM as an automatic fallback for arbitrary native binaries: reject.

## Revisit / closure

Real workload inventories and current IaC/code ownership audit.

Sources: S025, S026, S027, S028, S029, S030, S006.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
