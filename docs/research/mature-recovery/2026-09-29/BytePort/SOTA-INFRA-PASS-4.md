# BytePort SOTA infrastructure pass 4 — graph, reconciliation, standalone bare metal

Date: 2026-09-30.

## OpenTofu

OpenTofu builds a dependency resource graph used for plan/refresh and exposes machine-readable planned actions including noop/create/read/update/replace/delete/move plus reasons.

Implications:
- BytePort ReconciliationPlan should use explicit action vocabulary, not opaque adapter steps.
- dependency graph ordering belongs above target adapters.
- replacement is semantically distinct from update.
- reason/provenance for destructive actions is first-class.

Decision: **ADAPT graph/plan semantics, not OpenTofu state format as product identity.**

## Crossplane

Crossplane ManagedResource represents an external provider resource; provider controllers continuously reconcile desired managed resources with external resources.

Implications:
- DesiredResource and RealizedResource separation is strongly validated.
- target/provider adapter owns external API translation.
- continuous/periodic reconciliation is a mature mode, not merely one-shot deploy.
- deletion safety/dependency usage should be explicit.

Decision: **LEARN FROM provider/reconciler contract; avoid mandatory Kubernetes control plane.**

## Pulumi

Pulumi resource providers translate desired resource registrations into provider CRUD operations through plugins.

Implications:
- provider plugin/capability boundary is strong prior art.
- BytePort may support richer programmable generation later, but YAML/declarative UX remains direct user intent.
- provider-specific functionality can remain extension data behind portable resource identity.

Decision: **LEARN FROM provider plugin architecture.**

## Ironic standalone

Ironic can operate directly without the rest of OpenStack. It provides heterogeneous physical-machine provisioning via common/vendor management protocols.

Implications:
- BytePort can integrate Ironic without becoming an OpenStack distribution.
- standalone mode is the leading B09 bootstrap candidate.
- BytePort must supply its own multi-user/policy boundary if using Ironic standalone assumptions.
- adoption/enrollment/provision/deprovision states map naturally into TargetAdapter observations/operations.

Decision: **LEADING INTEGRATE candidate for B09.**

## Bare-metal capability reality

Physical targets differ from VM/cloud resources; e.g. lifecycle operations such as live migration may not exist. Adapter capability declaration therefore gates portable operations.

## Revised generalized reconciliation vocabulary

At minimum:
- NOOP;
- READ/OBSERVE;
- CREATE;
- UPDATE;
- REPLACE;
- DELETE;
- MOVE/REASSOCIATE where meaningful;
- UNKNOWN/DEFER when observation/capability is insufficient.

Every destructive/replace action carries reason and exact desired/realized identities.

## Next comparative work

- MAAS operational footprint/API;
- Bifrost as Ironic installer/standalone packaging;
- Tinkerbell operational footprint;
- NixOS/Colmena for post-provision host configuration;
- determine boundary between BytePort provisioning and configuration management;
- state ownership comparison: BytePort journal/graph vs OpenTofu/Pulumi external state.
