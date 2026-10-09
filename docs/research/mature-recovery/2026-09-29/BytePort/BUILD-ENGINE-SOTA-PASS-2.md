# Pass 5 — BytePort BuildEngine SOTA refinement

Date: 2026-09-30. External documentation retrieved on this date. This is architecture research, not product acceptance.

## BuildKit / Docker build path

Current Docker documentation says BuildKit can attach build attestations to image artifacts. Provenance can include build parameters/environment, VCS/source details and materials consumed during the build. Build attestations are attached to image metadata, and provenance can be emitted using SLSA provenance formats.

Sources:
- https://docs.docker.com/build/metadata/attestations/
- https://docs.docker.com/build/metadata/attestations/slsa-provenance
- https://docs.docker.com/build/metadata/attestations/attestation-storage/

**BytePort consequence:** a Dockerfile/BuildKit BuildEngine adapter can potentially return more than a local image ID: immutable OCI image identity plus attached provenance/SBOM. This directly fits BP-AD-02's BuildArtifact + provenance contract better than treating `docker build` exit 0 as sufficient.

Limit: the current disposable prototype captures a local Docker image ID and live application marker. It does not yet publish/verify a registry digest or provenance attestation, so that experiment cannot establish final artifact-distribution identity.

## Cloud Native Buildpacks

Current CNB documentation defines the lifecycle as transforming application source through analysis/detection/restoration/build/export into a runnable OCI image. The exporter writes `report.toml` with exported image information including digest/manifest size for OCI registry output, plus build BOM information contributed by buildpacks.

Sources:
- https://buildpacks.io/docs/for-platform-operators/tutorials/lifecycle/
- https://buildpacks.io/docs/for-platform-operators/concepts/lifecycle/export/
- https://buildpacks.io/docs/for-platform-operators/concepts/lifecycle/create/
- https://buildpacks.io/docs/for-app-developers/concepts/buildpack/

CNB also distinguishes trusted vs untrusted builders because build phases and registry credentials have different privilege requirements.

Source:
- https://buildpacks.io/docs/for-platform-operators/how-to/integrate-ci/pack/concepts/trusted_builders/

**BytePort consequence:** CNB is a serious BuildEngine adapter candidate for source trees without an explicit Dockerfile. It already has:
- source detection;
- versioned builder/buildpack identities;
- OCI output;
- digest-bearing export report;
- separate build/runtime base-image concepts.

BytePort should not reproduce language/build detection itself unless its manifest semantics genuinely require behavior CNB/another selected engine cannot express.

## Adapter architecture refinement

Do not select one universal builder as product identity.

The BuildEngine interface should expose capabilities such as:
- accepted source/build-plan types;
- immutable output identity mechanism;
- provenance/SBOM support;
- builder/toolchain identity;
- credential requirements;
- cancellation/retry semantics;
- cache semantics;
- target/platform constraints;
- reproducibility characteristics.

Initial adapter candidates:
1. **BuildKit/Dockerfile** — explicit project-supplied build contract; strong provenance/attestation path.
2. **Cloud Native Buildpacks** — convention/detection-based source build to OCI; useful when no Dockerfile is supplied.
3. **External platform/CI** — useful when the user's existing CI already builds/publishes immutable artifacts.

A deployment platform such as Coolify remains a whole-product alternative/falsification baseline, not automatically the internal BuildEngine.

## Provisional dispatch policy to test

- explicit immutable prebuilt artifact → no build; verify and deploy it;
- explicit Dockerfile/build definition → BuildKit-family adapter;
- supported source with no explicit build definition → CNB-family adapter candidate;
- user-selected/existing CI integration → external BuildEngine adapter;
- unknown source/build contract → refuse or require explicit configuration, never guess and return green.

## Required next prototype upgrades

1. upgrade the disposable Docker prototype to emit a registry/OCI digest plus provenance where practical;
2. build the same tiny fixture through a CNB/pack path and compare:
   - configuration required;
   - immutable artifact identity;
   - source/build provenance;
   - latency;
   - cache behavior;
   - secret/credential surface;
   - failure clarity;
3. demonstrate prebuilt immutable artifact bypass;
4. ensure BuildEngine selection itself becomes part of BuildOperation/evidence identity.

No BuildEngine is frozen by this pass.
