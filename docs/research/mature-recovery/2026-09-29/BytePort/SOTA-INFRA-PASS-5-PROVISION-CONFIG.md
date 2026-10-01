# BytePort SOTA infrastructure pass 5 — provisioning vs host configuration

Date: 2026-10-01.

## MAAS

MAAS exposes bare-metal/VM discovery, commissioning, OS deployment, network/storage configuration and API-driven lifecycle. It is designed to make physical machines behave more like cloud instances.

Decision:
**SERIOUS B09 bootstrap candidate**, alongside standalone Ironic/Metal3 and Tinkerbell.

Relative posture:
- MAAS: integrated operational product with networking/storage/image lifecycle;
- Ironic: lower-level provisioning service with broad hardware drivers and standalone viability;
- Tinkerbell: workflow-oriented provisioning stack.

BytePort should benchmark operational footprint, API fit, adoption/inspection, destructive semantics and deployment assumptions rather than choosing by feature count.

## NixOS / Colmena

NixOS declaratively owns post-install host/system configuration. Colmena is a thin stateless deployment layer over Nix tooling and supports parallel deployment to hosts.

Nix documentation explicitly distinguishes system configuration from initial bare-metal intake/provisioning.

Decision:
**SEPARATE HostConfigurationAdapter family**, not primary BareMetalProvisioner.

This boundary prevents BytePort from forcing:
- BMC/PXE/disk provisioning;
- OS image deployment;
- post-boot package/service/configuration convergence

into one provider abstraction.

## Revised target stack

A physical-host lifecycle may compose:
1. BareMetalProvisioner — discover/inspect/adopt/provision/clean/power;
2. HostConfigurationAdapter — converge OS/services/configuration after boot;
3. RuntimeAdapter — deploy application/workload resources;
4. Observation adapters — verify each layer.

Examples:
- Ironic or MAAS -> Nix/Colmena -> process/container/runtime;
- Tinkerbell -> Nix/other config manager -> runtime.

Not every target requires all layers.

## State ownership

BytePort owns desired graph, cross-layer operation identity, relationships and evidence.
External engines may own their native state; BytePort stores ExternalOperationRef/RealizedResource identities and reconciles rather than copying provider internals as authoritative truth.

## Next comparison

Score Ironic/MAAS/Tinkerbell on:
- standalone footprint;
- API stability;
- hardware coverage;
- inspect/adopt;
- networking/storage;
- image/provision;
- cleaning/destruction;
- event/observation model;
- idempotency/reconciliation;
- auth/multi-tenancy;
- licensing/health;
- local lab feasibility.

Separately compare Nix/Colmena/Ansible-like configuration adapters after provisioning.
