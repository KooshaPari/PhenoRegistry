# Pass 3 — mechanism replacement evidence and source-identity model

Date: 2026-09-29. Scope remains ShareCLI + BytePort.

## ShareCLI — specialized equivalence beats generic replay

Additional current prior art materially sharpens SC-F01.

Mozilla sccache documents compiler-specific cache keys rather than an arbitrary argv cache. For Rust it includes source-file digests plus rustc executable, host triple, sysroot/shared-library identity, dependency readers and parsed compiler arguments. For C/C++ it hashes preprocessed source. Its Rust support also has explicit unsupported/caveat cases. Distributed execution packages toolchains and uses sandboxing/authentication rather than assuming the local command string defines a portable task.

Sources retrieved 2026-09-29:
- https://github.com/mozilla/sccache/blob/main/docs/Caching.md
- https://github.com/mozilla/sccache/blob/main/docs/Rust.md
- https://github.com/mozilla/sccache/blob/main/docs/DistributedQuickstart.md
- https://github.com/mozilla/sccache/blob/main/docs/Configuration.md

Nix derivations likewise model reproducible work as a function of declared executable/input configuration and isolate outputs. Source: https://wiki.nixos.org/wiki/Derivations, retrieved 2026-09-29.

**Decision consequence:** ShareCLI should not attempt to discover one generic cache key that makes arbitrary shell commands replay-safe. Mature architecture should expose an equivalence-adapter interface:
- tool-native delegation when an established cache exists;
- product adapters for bounded command families whose relevant inputs can be identified;
- optional in-flight duplicate suppression where lifetime/side effects make it safe;
- explicit bypass when equivalence cannot be established.

A historical Git/Args/Time key can remain compatibility behavior only if its accepted semantic domain is narrower than arbitrary command correctness. Otherwise it is transition debt.

## BytePort — deployment identity should be a chain, not one UUID

Current Coolify documentation distinguishes:
- application identity;
- selected Git branch/commit or other deployment input;
- built/pulled image;
- queued deployment operation and history;
- runtime container/server configuration;
- immutable SHA256 image references when desired.

Sources retrieved 2026-09-29:
- https://coolify.io/docs/core/build-deployment-model
- https://coolify.io/docs/applications/deployments/overview
- https://coolify.io/docs/applications/deployments/docker-image
- https://coolify.io/docs/cli/deploy-applications

OpenTofu separately records bindings from declared resource instances to remote-object identities and uses state locking; force unlock requires a unique lock ID to target the intended lock. Sources:
- https://opentofu.org/docs/language/state/
- https://opentofu.org/docs/language/state/locking/

**Decision consequence:** BytePort's mature identity chain should minimally distinguish:
`Project → SourceSnapshot/ManifestRevision → BuildArtifact → DeploymentIntent/Operation → ProviderResourceIdentity → Observation`.

One UUID cannot safely stand for all six. The current project/provider stop mismatch is therefore an ontology defect, not merely a typo.

## Alternative-stack pressure

Coolify already covers much of Git→build/pull→queue→running-container→history/logging/health. This strengthens the “commodity/contested” classification of BytePort deployment mechanics. BytePort differentiation must survive comparison on integration/portfolio/evidence/ownership/usability, not feature presence.

sccache/Nix similarly cover specialized correct work reuse better than a generic ShareCLI cache. ShareCLI differentiation must survive comparison on cross-tool agent-aware composition and operator outcomes, not “has caching.”

No external performance claim is imported as product evidence. Exact version/license/security/maintenance/integration-cost review remains open.
