# Pass 5 — architecture-risk convergence

Date: 2026-09-30. Scope remains exactly ShareCLI + BytePort.

## Native evidence delta

### ShareCLI
SC-F01 is now native-reproduced on the real Hypervisor. Git-mode durable result reuse returned stale first-edit output after relevant file bytes changed to second-edit while the key's HEAD/status shape remained equivalent.

This is sufficient to reject Git HEAD+porcelain as a generic durable result-equivalence relation. It is not sufficient to choose the final adapter architecture by itself.

An expanded native matrix now attacks:
- Git + changed bytes;
- Time + changed file bytes;
- Args + identical argv across different workspaces;
- Git + execution-relevant environment change.

The matrix is executed separately and is not pre-scored in this record.

### BytePort
BP-F03 and BP-F04 now both have native evidence:
- ProjectID was used instead of persisted ProviderResourceID on stop.
- Provider deploy can succeed while local Project persistence fails, leaving no local row and no compensating stop in the exercised path.

The first BP-F04 probe was invalid because it broke DB access before provider execution; it remains explicitly non-evidence. The corrected probe injects only Project-create failure after provider success.

## ShareCLI architecture convergence

Current source fuses durable TTL replay, advisory-lock concurrent sharing and speculative pre-execution behind the same command key.

Decision candidates now split:
- `InFlightCoordinator` — execution-lifetime duplicate suppression;
- `ResultReuseStore` — optional durable reuse requiring stronger adapter identity;
- `EquivalenceAdapter` — explicit, versioned eligibility decision; unknown domains bypass;
- tool-native cache delegation where stronger semantics already exist.

Generic arbitrary-command durable replay is rejected as the default architecture pending contrary evidence.

## BytePort architecture convergence

Two independent native failures support explicit product state:
- durable Operation identity before external side effects;
- ProviderResource binding distinct from Project;
- reconciliation after unknown/partial outcomes.

The leading build architecture is delegated build + verified immutable artifact, not a custom general build engine.

Current external prior art strengthens this:
- OCI descriptors define digest as content identity and require digest/size verification for referenced content.
- Coolify documents deployment from existing immutable SHA256 image digests as well as Git/build paths; this proves a realistic alternative can separate build from runtime deployment.
- Coolify's CLI/API exposes application/resource UUID separately from deployment UUID, reinforcing operation/resource identity separation.
- OpenTofu state exists specifically to bind declared resource instances to remote-object identities; state locking uses unique lock identity and refuses unsafe concurrent writes.

Sources retrieved 2026-09-30:
- https://specs.opencontainers.org/image-spec/descriptor/
- https://coolify.io/docs/applications/deployments/docker-image
- https://coolify.io/docs/cli/deploy-applications
- https://coolify.io/docs/api/endpoints/deployments/deploy-by-tag-or-uuid
- https://opentofu.org/docs/language/state/
- https://opentofu.org/docs/language/state/locking/

No external product is treated as automatically superior. These sources constrain which mechanisms are commodity and provide falsification baselines.

## Vertical fixture

BytePort now contains `tests/fixtures/mature-recovery-app`, a standard OCI fixture that embeds SourceSnapshot/ManifestRevision experiment markers into a runtime probe endpoint. It intentionally does not define the canonical BytePort manifest schema. It exists to compare candidate build engines and runtime adapters against one identical subject.

## Gate delta

ShareCLI:
- generic Git durable replay: falsified natively;
- split in-flight/durable architecture: provisional;
- adapter model: provisional;
- expanded matrix: pending;
- queue/FUSE/ownership: open.

BytePort:
- provider identity defect: native reproduced;
- external-side-effect persistence window: native reproduced;
- operation journal/reconciliation: provisional;
- delegated build + immutable artifact: provisional;
- vertical fixture: committed;
- actual alternative prototype: not yet run.

Neither product is architecture-frozen or specification-complete.
