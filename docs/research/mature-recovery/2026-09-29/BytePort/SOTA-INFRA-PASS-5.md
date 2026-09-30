# BytePort SOTA infrastructure pass 5 — bare-metal engines and state ownership

Date: 2026-09-30.
Scope: generalized infrastructure/bare-metal thesis.

## MAAS

Sources: Canonical MAAS lifecycle/deployment/API docs.
Observed lifecycle:
New → Commissioning → Ready → Allocated → Deploying → Deployed → Releasing → Ready.

Capabilities:
- PXE/network enlistment;
- hardware inventory/commissioning;
- allocation/ownership;
- OS deployment;
- storage/network configuration;
- release/wipe;
- rescue/broken states;
- API-driven lifecycle.

Decision:
**COMPARE seriously with Ironic as B09 provider**, especially where MAAS provides more integrated inventory/network/storage/ownership UX.

Tradeoff:
MAAS carries stronger opinionated control-plane semantics; BytePort must not duplicate or conflict with MAAS allocation/ownership state.

## Ironic standalone + Bifrost

Sources: current Ironic/Bifrost docs.
Observed:
- Ironic runs standalone without Nova/Neutron/Keystone;
- direct bare-metal API;
- optional HTTP Basic/noauth standalone auth;
- standalone networking available;
- Bifrost automates standalone Ironic installation and known-hardware OS deployment with relatively few external requirements.

Decision:
**Ironic remains leading low-level engine; Bifrost is leading bootstrap/install path for experiments.**

Security consequence:
Standalone Ironic is not a BytePort authorization boundary. BytePort needs its own target credentials/policy and must never expose noauth Ironic broadly.

## Tinkerbell

Sources: current Tinkerbell docs.
Observed:
- Hardware + Template → Workflow;
- Kubernetes CRDs/controller;
- DHCP/iPXE (Smee), metadata, HookOS, workflow server/worker;
- optional BMC services;
- Cluster API integration.

Decision:
**Second engine candidate**, particularly where workflow customization matters.
Operationally heavier than simply linking to an API because its provisioning stack owns network boot and workflow components.

## Crossplane lesson

ManagedResource vs external resource strongly validates BytePort DesiredResource vs RealizedResource separation.
Crossplane also demonstrates lifecycle-policy modes where external deletion/management can be disabled or observe-only.

Decision consequence:
BytePort should model lifecycle policy separately from desired config:
- observe-only;
- create/observe;
- manage;
- orphan-on-remove;
- destroy-on-explicit-intent.

Do not overload local object deletion with provider destruction.

## Provider-state ownership alternatives

### BytePort-owned durable truth
Pros:
- consistent cross-target UX;
- exact operations/evidence;
- target-neutral reconciliation.
Risk:
- stale duplicate state vs provider engine.

### Adapter/provider-owned operation state
Pros:
- less duplication;
- leverage provider lifecycle.
Risk:
- inconsistent semantics and retention.

Decision:
Keep BytePort product Operation/DesiredResource/RealizedResource identities, but reference ExternalOperationRef/provider state rather than copy provider internals. Observations are refreshed from provider authority.

## Post-provision boundary

Bare-metal provisioning and host configuration are distinct.
Candidate boundary:
- BytePort/Ironic/MAAS/Tinkerbell: inventory, image/provisioning, lifecycle, target identity;
- NixOS/Colmena/cloud-init/Ansible-like adapters: host configuration after provisioning.

Do not force BytePort core to become a configuration-management DSL. The manifest may reference configuration artifacts/adapters.

## Bootstrap ranking — provisional

1. Ironic standalone + Bifrost for low-level API/lifecycle breadth.
2. MAAS for integrated inventory/commissioning/deployment UX.
3. Tinkerbell for workflow-driven provisioning and Kubernetes-adjacent environments.

No winner frozen until disposable comparison measures setup burden, API fit, lifecycle coverage, restart/reconciliation, hardware requirements and cleanup.
