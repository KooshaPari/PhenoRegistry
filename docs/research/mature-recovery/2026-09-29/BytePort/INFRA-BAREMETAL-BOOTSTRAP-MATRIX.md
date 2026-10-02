# BytePort infrastructure / bare-metal bootstrap matrix — v0.2

Date: 2026-10-02.
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


## 2026-10-02 current-docs evidence update

### Ironic standalone

Current Ironic documentation continues to support direct standalone operation without Nova/Keystone/Neutron/Glance. Standalone automation can drive the Bare Metal API directly; authentication can be noauth or HTTP Basic, and current deployment-scenario guidance also documents JSON-RPC as an option to avoid a full message-queue dependency. Ironic retains the strongest explicit bare-metal state machine of the candidates: enrollment/preparation, allocation, deploy/undeploy, rescue, servicing, and driver-specific BMC control.

Implication for BytePort:
- strongest candidate for an exact provider-state / exact host-identity adapter;
- BytePort should reference Ironic node/allocation/provision state rather than copy its internal state machine;
- standalone mode is suitable for a disposable adapter experiment without making OpenStack itself part of BytePort identity.

Sources:
- https://docs.openstack.org/ironic/latest/install/standalone.html
- https://docs.openstack.org/ironic/latest/install/deployment-scenarios.html
- https://docs.openstack.org/ironic/2026.2/user/index.html

### Bifrost

Current Bifrost documentation still positions it as Ansible automation for installing standalone Ironic and deploying base images to known hardware. This reinforces the earlier boundary: Bifrost is an excellent **bootstrap/test harness** for an Ironic adapter, but it should not become BytePort's target lifecycle abstraction.

Source:
- https://docs.openstack.org/bifrost/2026.1/

### MAAS

Current MAAS documentation makes its lifecycle semantics more compelling than the earlier shorthand suggested:

- commissioning discovers and validates hardware and transitions a machine toward Ready;
- allocation reserves a machine so another process cannot deploy it concurrently;
- deploy installs the selected OS/configuration;
- machine identity is exposed as a stable `system_id`;
- observation includes machine status/power state and optional deployed-hardware synchronization;
- release returns the machine to the pool and may perform explicit disk erase.

Implication for BytePort:
- MAAS is a serious adapter candidate, not merely an operationally easier Ironic alternative;
- its explicit allocation boundary maps well to BytePort operation/admission identity;
- release/erase must remain an exact destructive action and cannot be inferred from desired-state absence;
- integrated networking/storage/inventory may reduce BytePort hand-rolling, but BytePort must avoid inheriting MAAS's whole control-plane identity.

Sources:
- https://canonical.com/maas/docs/latest/explanation/commissioning-machines/
- https://canonical.com/maas/docs/latest/explanation/deploying-machines/
- https://canonical.com/maas/docs/latest/how-to-guides/manage-machines/
- https://canonical.com/maas/docs/latest/reference/cli-reference/machine/
- https://canonical.com/maas/docs/latest/reference/api-reference/api-v2-generated/

### Tinkerbell

Current Tinkerbell documentation models a Workflow as a Kubernetes CRD combining a Hardware reference with a Template reference plus a hardware map. That is attractive for custom provisioning workflows and explicit hardware-template binding, but it also means BytePort would be adopting a Kubernetes/controller-shaped provider surface.

Implication for BytePort:
- retain as the strongest workflow-flexibility comparator;
- explicitly test how stable hardware identity, restart reconciliation, workflow status, and cleanup behave;
- do not let Workflow/Template CRDs become BytePort's canonical product graph.

Source:
- https://tinkerbell.org/docs/v0.22/concepts/workflows/

### Crossplane lifecycle lesson retained

Current Crossplane managed-resource documentation still separates Observe/Create/Update/Delete/LateInitialize policies and explicitly avoids automatically deleting/recreating an external resource merely because an immutable field changes. This supports BytePort's current design:
- observation and mutation authority are separate;
- replacement is an explicit action;
- desired-state drift alone does not authorize destruction.

Source:
- https://docs.crossplane.io/latest/managed-resources/managed-resources/

## B09 executable evaluation order

The research-only ordering remains:

1. **Ironic standalone bootstrapped with Bifrost**
2. **MAAS**
3. **Tinkerbell**

But this is an experiment order, not a frozen provider winner.

For each candidate, the disposable fixture must prove the same BytePort-owned contract:

`discover/adopt exact host -> capabilities -> provision -> observe -> restart/reconcile -> immutable-change behavior -> exact authorized release/undeploy/destroy`

Required evidence for comparison:
- exact provider host/resource identifier survives restart;
- ambiguous create/provision outcome does not duplicate provisioning;
- stale/unknown observation cannot trigger cleanup;
- provider lifecycle state is referenced, not copied as BytePort authority;
- destructive release/undeploy requires explicit exact identity;
- provider restart/controller restart does not lose operation reconciliation;
- clean/erase semantics are separately visible from ordinary release;
- target capability gaps remain explicit rather than emulated silently;
- disposable VM or nested-virtualization fixture is reproducible enough for CI/lab automation.

The first implementation experiment should therefore remain **Ironic standalone + Bifrost**, with MAAS immediately behind it as the operational/integrated-control-plane comparator.


## B09 executable experiment contract — Ironic + Bifrost testenv

Current Bifrost documentation provides a concrete disposable VM route suitable for BytePort's first B09 adapter experiment:

1. create virtual bare-metal nodes with `bifrost-cli testenv`;
2. install standalone Ironic into the test environment with `bifrost-cli install --testenv`;
3. select an emulated BMC path:
   - IPMI via VirtualBMC; or
   - Redfish via sushy-tools;
4. enroll the generated node inventory;
5. drive provisioning through Ironic/Bare Metal API identity;
6. verify the node reaches an explicit `active` provision state;
7. restart the BytePort adapter/control process and re-observe the same node;
8. reconcile without provisioning a second machine;
9. undeploy/unprovision the exact node;
10. delete the test node and destroy the libvirt test environment.

Bifrost's own local CI/test flow already creates VMs, provisions them, connects to them, unprovisions them, and deletes them from Ironic. This makes it a strong substrate for a BytePort adapter fixture rather than a hypothetical integration.

### Required BytePort identities

The experiment must persist and distinguish:

- BytePort `RuntimeOperationID`;
- BytePort desired host/resource ID;
- Ironic node UUID;
- provider allocation/provision operation identity where exposed;
- libvirt test-VM identity only as fixture infrastructure, never as product resource identity;
- observed provision state + timestamp/freshness;
- image/artifact identity used for deploy;
- exact destruction/undeploy intent.

### Required counterexamples

The fixture is not green unless it demonstrates:

1. **lost deploy response**
   - provider mutation may have succeeded;
   - BytePort records UNKNOWN/reconciling;
   - restart observes the existing Ironic node;
   - no second deploy is issued.

2. **delayed provider visibility**
   - first observation may be incomplete;
   - absence/unknown does not authorize a second provision or cleanup.

3. **wrong node identity**
   - a valid Ironic node UUID belonging to another desired resource cannot satisfy the operation.

4. **immutable-image change**
   - provider capability determines replace/redeploy behavior;
   - BytePort must not invent in-place UPDATE.

5. **undeploy without explicit intent**
   - desired absence by itself cannot undeploy/release the node.

6. **exact authorized undeploy**
   - explicit destruction intent + exact desired/realized/provider identity performs one undeploy.

7. **controller restart**
   - BytePort process restart during deployment retains sufficient operation/provider identity to reconcile.

8. **BMC driver parity**
   - run the same core identity/reconciliation checks with VirtualBMC/IPMI and sushy-tools/Redfish where practical;
   - driver-specific capability differences remain explicit.

### Fixture resource expectations

Current Bifrost troubleshooting guidance says test VMs are typically about 1 vCPU, ~3 GB RAM and ~11 GB virtual storage each. Current 2026.1 release notes also note increased test-VM memory requirements due to larger DIB-based IPA ramdisks. The first BytePort experiment should therefore use **one disposable VM**, not a multi-node cluster, until the lifecycle semantics are proven.

Sources:
- https://docs.openstack.org/bifrost/latest/contributor/testenv.html
- https://docs.openstack.org/bifrost/latest/install/index.html
- https://docs.openstack.org/releasenotes/bifrost/2026.1.html

## Tinkerbell disposable comparator note

Tinkerbell also has a current Vagrant/libvirt playground that provisions an Ubuntu VM and supports full cleanup with `vagrant destroy`. Its Workflow state exposes PREPARING/PENDING/RUNNING/POST and terminal SUCCESS/FAILED/TIMEOUT states, making it suitable for the *same* ambiguity/restart comparison after Ironic/MAAS.

The key distinction is architectural: Tinkerbell binds Hardware + Template in a Workflow CRD and requires its Kubernetes-shaped control plane (although current docs also describe an embedded standalone binary). That should be measured as provider footprint, not treated as a disqualifier by assumption.

Sources:
- https://tinkerbell.org/docs/v0.22/setup/getting_started/
- https://tinkerbell.org/docs/v0.22/concepts/workflows/
- https://tinkerbell.org/docs/v0.22/setup/install/
