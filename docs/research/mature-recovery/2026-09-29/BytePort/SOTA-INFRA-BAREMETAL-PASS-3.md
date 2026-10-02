# BytePort SOTA pass 3 — generalized infrastructure / bare metal

Date: 2026-09-30.
Scope: corrected direct-user thesis.

## Metal3 + Ironic

Observed primitives:
- BareMetalHost desired-state resource;
- hardware inspection/inventory;
- BMC-backed power/boot control;
- image provisioning;
- cleaning/deprovisioning;
- adoption of externally/already provisioned hosts;
- explicit provisioning state machine;
- Kubernetes desired state remains authoritative while Ironic performs hardware actions;
- Redfish/IPMI/vendor support through Ironic.

Decision consequence:
**INTEGRATE/ADAPT before custom bare-metal implementation**.
BytePort should model bare metal as a TargetAdapter capability family and initially delegate low-level BMC/provisioning to Ironic/Metal3 where deployment assumptions fit.

Important lesson:
control-plane restart/reconciliation and adoption are already central bare-metal lifecycle problems; BytePort's Operation/RealizedResource model aligns well.

## Tinkerbell

Observed primitives:
- declarative/API-centric bare-metal provisioning;
- DHCP/iPXE;
- metadata service;
- installation environment;
- workflow server/worker;
- optional BMC services;
- Cluster API integration.

Decision consequence:
**COMPARE as second bootstrap candidate**, especially where a lighter workflow engine is preferable to Kubernetes+Ironic assumptions.

## Architecture implication

BytePort should not own:
- raw IPMI/Redfish vendor drivers;
- PXE/iPXE implementation;
- disk imaging machinery;
- hardware cleaning implementation

unless experiments establish a gap worth owning.

BytePort should own:
- DesiredResourceGraph;
- target-neutral lifecycle intent;
- target capability negotiation;
- exact target/resource identity;
- durable operation/reconciliation;
- policy/authorization;
- adapter selection;
- cross-target user experience;
- evidence;
- repository/manifest-to-infrastructure projection.

## Bare-metal adapter candidate contract

Capabilities:
- discover/inspect;
- adopt;
- provision image;
- configure boot/power;
- observe;
- update/reprovision;
- deprovision/clean;
- destroy inventory record;
- provider-specific extension set.

Destructive semantics must distinguish:
deprovision/clean, power-off, remove inventory record, and BytePort local uninstall.

## Next research

- MAAS;
- OpenStack Ironic standalone/Bifrost;
- Cluster API provider contracts;
- Crossplane provider/resource reconciliation;
- Terraform/OpenTofu/Pulumi state/plan semantics;
- Nix/NixOS/Colmena-style host configuration;
- Nomad and other non-Kubernetes target schedulers;
- secrets/network/storage lifecycle across target families.
