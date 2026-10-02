# BytePort SOTA infrastructure pass 6 — lifecycle policy and configuration boundary

Date: 2026-09-30.

## MAAS lifecycle

MAAS explicitly separates machine discovery/commissioning, allocation, deployment and release. Machine ownership/allocation is a real provider-side state, not just an API call.

Decision consequence:
A BytePort MAAS adapter must preserve MAAS machine identity and lifecycle state through ExternalOperationRef/RealizedResource observations rather than duplicating them as invented BytePort states.

## Crossplane lifecycle-policy lesson

Crossplane supports management/deletion policies ranging from full management to observe-only and orphan-on-delete behavior.

Decision consequence:
BytePort DesiredResource needs an explicit lifecycle/management policy distinct from resource config:
- ObserveOnly;
- CreateObserve;
- Manage;
- OrphanOnRemove;
- DestroyOnExplicitIntent.

Default must be conservative for imported/adopted resources.

## NixOps / Colmena boundary

NixOps demonstrates stateful deployment identity and persisted deployment state.
Colmena intentionally presents a thinner/stateless NixOS deployment layer over already running hosts.

Decision consequence:
BytePort should separate:
1. infrastructure provisioning/realization;
2. post-provision host configuration.

For NixOS hosts, a Colmena/Nix/deploy-rs style configuration adapter may be better than BytePort inventing a host-config DSL.

BytePort manifest can reference a configuration artifact/adapter while DesiredResourceGraph retains host identity and lifecycle.

## State ownership

BytePort owns:
- desired graph revision;
- cross-target Operation identity;
- RealizedResource references;
- observations/evidence;
- reconciliation decision history.

Provider engine owns:
- provider-internal workflow/state machine;
- low-level hardware/cloud operation details.

Configuration adapter owns:
- configuration artifact semantics and host activation details.

BytePort stores references/receipts rather than pretending to be authoritative over provider internals.

## A07 domain consequence

Add lifecycle policy to DesiredResource.
Imported/adopted existing resources should default to conservative observe/orphan semantics unless explicitly promoted to managed ownership.

Destructive reconciliation requires both:
- lifecycle policy permitting destruction;
- explicit authorized DestructionIntent for the exact resource.
