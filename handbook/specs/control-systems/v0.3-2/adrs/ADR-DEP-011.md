# ADR-DEP-011 — Represent local machines as a qualified BytePort provider

**Status:** proposed

## Decision

Extend BytePort with a local-fleet provider whose node daemon exposes capabilities and executes desired state. Do not build another PaaS GUI or global controller.

## Alternatives tested conceptually

- Separate private-cloud product: rejected for duplicate control/state surfaces.
- Treat GitHub self-hosted runners as the local-cloud abstraction: rejected because they do not model databases, services, volumes or lifecycle semantics.
- Full Kubernetes/OpenNebula-style private cloud on every personal node: retain only as a dedicated-host option, not the default laptop/desktop contract.

## Revisit / closure

Current owner/module reconciliation or evidence that BytePort cannot host the required provider semantics.

Sources: S052, S058, S059, S060.

This record does not authorize mutation. ADR-DEP-001 and ADR-DEP-014 record stated user constraints.
