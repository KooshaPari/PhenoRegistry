# Pass 18 — targeted external architecture research

Date 2026-09-30. Scope remains exactly Dino + Civis. This pass follows reproduced failures; it is not generic competitor research.

## Dino — configuration generations and consumer acknowledgement

### Envoy xDS
Primary source: https://www.envoyproxy.io/docs/envoy/latest/api-docs/xds_protocol.html (accessed 2026-09-30).

Relevant mechanism:
- configuration responses carry version identity;
- clients ACK or NACK a version;
- on NACK the client reports error detail and retains its prior accepted version rather than pretending the new version was fully applied.

Adopt conceptually:
- distinguish desired generation from fully active/observed generation;
- retain prior active generation while a required consumer NACKs;
- bind acknowledgement to exact generation identity.

Reject copying:
- DINOForge does not need xDS wire protocol, gRPC, or Envoy resource taxonomy.

### Nix generations
Primary source: https://wiki.nixos.org/wiki/Generation and Nix profile rollback documentation (accessed 2026-09-30).

Relevant mechanism:
- changes create a new generation rather than mutating the current environment in place;
- current generation is switched explicitly;
- earlier generations remain available for rollback.

Adopt conceptually:
- immutable candidate generation;
- publication/switch rather than append-in-place;
- last accepted generation remains recoverable.

Reject copying:
- no Nix store/evaluator is justified for DINOForge pack loading.

### Kubernetes generation / observed generation
Primary-source family: Kubernetes API/controller conventions and Server-Side Apply docs (accessed 2026-09-30).

Relevant mechanism:
- desired resource generation and controller-observed state are not the same thing;
- ownership/removal semantics matter when fields disappear from the desired configuration.

Adopt conceptually:
- per-runtime-consumer observed generation;
- removing content in new desired generation must remove it from effective state unless another accepted owner retains it.

## Civis — multi-component snapshot, version and atomicity

### SQLite atomic commit
Primary source: https://www.sqlite.org/atomiccommit.html (accessed 2026-09-30).

Relevant mechanism:
- a multi-write transaction must appear all-or-nothing even across crash/power loss;
- rollback journals preserve enough prior state to restore a sane committed state;
- multi-file atomic commit requires an explicit coordination boundary.

Adopt conceptually:
- do not treat sequential component writes as a committed save;
- preserve the prior accepted save until the new component set + outer manifest are durable;
- detect/repair interrupted publication.

Reject copying:
- Civis save data need not be moved wholesale into SQLite merely to obtain atomicity; SQLite may still be a valid implementation option if measured tradeoffs support it.

### TUF consistent snapshots
Primary source: https://theupdateframework.github.io/specification/draft/ and v1 consistent-snapshot section (accessed 2026-09-30).

Relevant mechanism:
- metadata is versioned;
- consistent snapshot mode prevents combining metadata/files from different repository states;
- clients reject version rollback relative to trusted state.

Adopt conceptually:
- one outer save manifest identifies a coherent set of component versions/digests;
- mixed-world/mixed-tick components fail;
- deleting the version selector must not silently downgrade a modern save.

Reject copying:
- save games do not require TUF's trust-role/signing system unless a separate adversarial authenticity requirement is accepted.

### Cap'n Proto schema evolution
Primary source: https://capnproto.org/language.html (accessed 2026-09-30).

Relevant mechanism:
- schema evolution is explicit and field ordinals preserve compatibility;
- new fields can be added without changing old field identity.

Adopt conceptually:
- stable component/schema identities and additive migrations;
- never infer compatibility from field names alone.

Reject copying:
- no serializer switch is justified yet. Current JSON/component bundle can implement explicit version/migration semantics first.

## Decision consequence

The external work supports, but does not by itself prove, the same architectures the local falsification produced:
- Dino: immutable desired generation + exact identity + ACK/NACK/observed generation + rollback.
- Civis: explicit component manifest + strict version classifier + coherent snapshot commit boundary + migration/recovery.

Local executable evidence remains the stronger product-specific basis. External prior art is used to avoid inventing weaker versions of already-known lifecycle patterns.
