# BytePort infrastructure / bare-metal bootstrap matrix — v0.1

Date: 2026-09-30.
Scope: generalized repository+manifest → heterogeneous infrastructure lifecycle.

| System | Strong primitives | Constraints / risks | BytePort decision |
|---|---|---|---|
| OpenTofu | dependency graph; plan; explicit create/update/replace/delete; broad provider ecosystem | state/provider model can become product identity; CLI/state coupling | **ADAPT graph/plan semantics; consider provider interop later** |
| Crossplane | desired ManagedResource vs external resource; continuous reconciliation; management/deletion policies | Kubernetes control-plane dependency | **LEARN FROM reconciler/provider/lifecycle-policy model**, no mandatory K8s |
| Pulumi | provider plugin model; broad resource coverage; programmable desired state | programming-language UX conflicts with single-YAML primary interaction | **LEARN FROM provider plugin architecture** |
| Ironic standalone | heterogeneous physical-machine inspection/provision/deprovision; BMC drivers; direct standalone API | standalone auth/multi-tenancy limitations; infra footprint | **LEADING bare-metal engine candidate** |
| Bifrost | automates standalone Ironic installation; known-hardware OS deployment; useful test environment | Ansible/install-oriented, not target lifecycle abstraction itself | **LEADING bootstrap/test harness for Ironic** |
| MAAS | discovery, commissioning, inventory, allocation, deploy, storage/network config, release/wipe, rescue | opinionated control plane/ownership/networking; larger integrated system | **SERIOUS comparator / possible adapter** |
| Tinkerbell | API/declarative Hardware+Template+Workflow; DHCP/iPXE; metadata; HookOS; optional BMC | Kubernetes/controller + provisioning stack footprint; workflow ownership | **SECOND engine candidate**, strong custom workflow fit |
| NixOps | declarative multi-machine deployment + explicit deployment state | NixOS/Nix-specific; overlaps provisioning/state domains | **LEARN FROM state/deployment separation; possible Nix target integration** |
| Colmena | thin/stateless parallel NixOS configuration deployment | assumes existing NixOS hosts; not provisioning | **POST-PROVISION CONFIG ADAPTER candidate**, not bare-metal engine |
| current NanoVMS | already live provider integration | current selected-app identity/lifecycle defects; narrower runtime | **RETAIN as Runtime/TargetAdapter candidate**, not product identity |

## Product boundary

BytePort owns:
- SourceSnapshot / ManifestRevision;
- DesiredResourceGraph;
- Target identity + capabilities;
- ResourcePlan / ReconciliationPlan;
- product Operation;
- RealizedResource references;
- observations/evidence;
- cross-target lifecycle policy;
- user-facing lifecycle UX.

Target/provider owns:
- low-level provider workflow/state;
- vendor-specific BMC/cloud operations;
- imaging/PXE internals;
- provider-native operation identity.

Post-provision config adapter owns:
- configuration artifact semantics;
- host activation/package/service details.

BytePort references provider/config receipts rather than copying their internal state as authoritative truth.

## Provisional B09 experiment ranking

1. **Ironic standalone + Bifrost** — broad low-level lifecycle and minimal need to hand-roll hardware drivers.
2. **MAAS** — compare operational footprint, integrated inventory/network/storage, allocation semantics.
3. **Tinkerbell** — compare workflow flexibility and Kubernetes/provisioning-stack burden.

## Comparison criteria

- install/bootstrap effort;
- disposable VM testability;
- inventory/inspection fidelity;
- adoption of existing hosts;
- BMC/power coverage;
- image/provision coverage;
- network/storage lifecycle;
- exact external identity;
- API/event/reconciliation quality;
- restart behavior;
- cleanup/destruction semantics;
- authentication/multi-user boundary;
- operational footprint;
- license/project health;
- provider lock-in;
- integration code required.

No provider winner is frozen before this experiment.
