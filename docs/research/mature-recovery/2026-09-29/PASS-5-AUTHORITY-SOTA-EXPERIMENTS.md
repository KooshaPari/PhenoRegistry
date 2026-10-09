# Pass 5 — conversation authority + artifact/equivalence architecture pressure

Date: 2026-09-30. Scope remains exactly ShareCLI and BytePort.

## ShareCLI authority correction

Recovered direct user context materially strengthens the bounded-adapter architecture:

- 2026-08-09: the user explicitly described high-scale agent-harness contention with duplicate Rust/Cargo work, queue/coalesce needs, daemon/socket reuse and pooled resources.
- 2026-08-10: terminal access must remain available; the user rejected a parser-rewrite framing and questioned replacing normal shell execution with redundant parser layers.
- 2026-08-27/28: ShareCLI should remain a standalone adoption wedge rather than absorb the distributed fabric; optimization/distribution granularity should be adaptive/coarsened rather than defaulting to syscall-level remote execution.
- 2026-04-01: central observability/control and isolated worktrees are genuine product outcomes.

Decision consequence: duplicate-work reduction is user-backed, but universal arbitrary-command durable replay is not. The provisional EquivalenceAdapter + unknown→BYPASS model is consistent with direct intent while preserving normal terminal/tool behavior.

## BytePort authority correction

Recovered direct November 2024 user context establishes the portfolio/productization path as mature BytePort behavior:

- deployment to owned AWS runtime;
- generated full project page plus project-list entry;
- fetch existing portfolio templates/components through an API;
- generate structured project content;
- POST completed project representation back;
- keep programmatic Git/server-side publication as fallback;
- configure Portfolio.RootEndpoint/APIKey with Git/AWS/LLM integration;
- monitor projects/instances.

This resolves portfolio ownership as **BytePort projection/publishing integration**, not ownership of the external renderer/CMS.

Historical Slickport evidence is consistent with this: BytePort calls Slickport an example portfolio backend and historical registry inventories once listed `KooshaPari/slickport`; current direct lookup returns 404. Slickport is therefore a historical adapter example, not BytePort identity.

## Current external architecture pressure

### Docker / BuildKit

Current Docker documentation (retrieved 2026-09-30):
- https://docs.docker.com/build/metadata/attestations/
- https://docs.docker.com/build/metadata/attestations/slsa-provenance
- https://docs.docker.com/reference/cli/docker/buildx/build/

BuildKit can emit build provenance describing source/materials/build parameters and can attach provenance/SBOM attestations to OCI image indexes. This strengthens BP-AD-02: BytePort need not invent a provenance format when its build adapter can consume standard artifact identity + attestations.

Limitation: local Docker image IDs and registry OCI digests are different evidence surfaces; the recovery fixture's first local experiment is not sufficient production provenance.

### Coolify

Current Coolify documentation (retrieved 2026-09-30):
- https://coolify.io/docs/core/build-deployment-model
- https://coolify.io/docs/applications/deployments/docker-image
- https://coolify.io/docs/applications/choose-deployment-method

Coolify separates:
- Git source builds;
- Dockerfile/Compose builds;
- deployment of an already-built image;
- mutable tags versus immutable SHA256 digest references;
- deployment queue/history/runtime configuration.

It explicitly notes mutable tags can resolve to different content on later deployment/restart while a digest identifies fixed image content.

Decision consequence: BytePort's source→artifact→runtime model is commodity/contested at the deployment-mechanics level. Differentiation must come from integrated project/source/manifest/evidence/recovery/portfolio outcomes and lower operating burden, not merely “Git deploy.”

### OpenTofu

Current OpenTofu state-locking documentation (retrieved 2026-09-30):
- https://opentofu.org/docs/language/state/locking/
- https://opentofu.org/docs/language/state/backends/

OpenTofu automatically locks writable state where backend support exists and uses a unique lock ID for force-unlock targeting. Remote state backends can preserve state independently from local execution.

Decision consequence: BytePort's proposed OperationID/generation/reconciliation model should be compared to adopting engine-owned state/locking rather than duplicating generic IaC transaction semantics.

## Experiments now executing

### ShareCLI
A native matrix now attacks historical Args/Git/Time modes on:
- cross-workspace identity;
- environment-dependent output;
- external input changes.

A separate experiment tests the precise SC-AD-01 thesis:
- two concurrent equivalent requests should execute once;
- after the in-flight execution completes and an input changes, later invocation must execute again instead of replaying the prior result.

### BytePort
A local delegated-build experiment now:
- hashes a separate experiment manifest;
- builds a tiny OCI/container fixture with source/manifest/nonce markers;
- records an immutable local image identity;
- runs and independently queries the application;
- deliberately replaces a mutable tag with a different build;
- verifies the original immutable artifact remains distinct/runnable.

This is an architecture experiment, not a final BuildEngine implementation. The next step after it passes is to add standards-grade OCI digest/provenance evidence and compare against the best integrated alternative.

## Gate effect

No architecture is frozen yet.

Potential freeze candidates if current experiments survive:
- ShareCLI: explicit equivalence adapters; unknown→BYPASS; split in-flight coordination from durable reuse; delegate to tool-native caches.
- BytePort: delegated build + verified immutable artifact; durable Operation journal/reconciliation; runtime provider adapters; portfolio publisher adapters.

Fresh independent falsification and remaining source denominators are still blocking.
