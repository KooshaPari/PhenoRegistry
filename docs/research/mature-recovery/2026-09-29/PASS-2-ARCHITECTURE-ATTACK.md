# Pass 2 — cross-product existence and architecture attack

Date: 2026-09-29. Scope remains exactly ShareCLI and BytePort. This is research evidence, not a third product program.

## ShareCLI

Canonical FR/trace inspection exposed an acceptance-policy defect: FR-008 is labeled ACCEPTED and scorecards label it COMPLETE while the acceptance surface checks cache mechanics, cwd/env/key modes, semantic argv normalization and strategy routing—not equivalence of actual command inputs. The committed native adversarial test at ShareCLI `f1dd74bfed1f08d4a2cc1ab7deba63b7b3b6b1a9` directly exercises the Rust Hypervisor Git-mode path. Its result must be read from exact-commit CI; model evidence is not substituted.

Existing 88-pillar/comprehensive scorecard outputs are **discovery-only / non-grading** for this mature-recovery program until individually requalified. A mapped filename, test name or percentage cannot close a semantic/journey/evidence gate.

Pass-2 external research reinforces composition:
- system/native process/resource controls should be compared before custom enforcement;
- Bazel-style action/input identity and specialized caches such as sccache demonstrate the value of narrower declared semantic domains;
- generic singleflight/cache mechanics do not solve equivalence identity.

The product's possible differentiation remains heterogeneous agent-aware composition and operator experience, not generic supervision or generic caching.

## BytePort

Authority evidence is now materially stronger. At source `0232cca16fedb7963a8c6f556dc5eee5c8c1674e`, BytePort's June charter, accepted ADRs, PRD, functional requirements and user journeys all retain manifest-driven Git/AWS deployment plus portfolio generation. The charter explicitly reserves mission/tenet changes to executive authority. The September registry local-first/desktop-first prose therefore cannot be treated as an automatic mature-scope replacement without recovering such authority.

Provisional reconciliation:
- mature identity = self-hosted deployment + productization control plane;
- local-first = control-plane placement/default, compatible with cloud targets;
- CLI-first vs desktop-first remains a real unresolved surface conflict;
- portfolio remains first-class mature behavior;
- NanoVMS remains a separate adapter/runtime.

A native handler adversarial test at BytePort `934b0456de5509b5e89294c3adaa046e632a2767` deliberately separates project ID from provider sandbox ID. It is expected to fail current source if the stop handler targets project UUID. No production fix is included.

Pass-2 external research strengthens the alternative stack substantially. Current Coolify docs cover Git/commit source resolution, build methods, Compose, immutable image digests, queued deployment history, logs, health/domain operation and CLI deployment. OCI descriptors provide content identity; AWS documents scoped idempotency; OpenTofu documents state locking; Tauri capabilities scope webview/frontend permissions. Consequently, source-to-running-app control is commodity/contested. BytePort must justify its integrated source→owned deployment→portfolio experience and any custom NVMS DSL/runtime against these primitives.

## Research-source additions

Retrieved 2026-09-29:
- https://coolify.io/docs/core/build-deployment-model
- https://coolify.io/docs/applications/choose-deployment-method
- https://coolify.io/docs/cli/deploy-applications
- https://specs.opencontainers.org/image-spec/descriptor/?v=v1.1.1
- https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html
- https://opentofu.org/docs/language/state/locking/
- https://tauri.app/security/capabilities/
- https://github.com/mozilla/sccache/blob/main/docs/DistributedQuickstart.md

These are current documentation/prior-art sources, not benchmark results. Exact adoption versions, licenses/transitive compatibility, project health, security history and integration cost remain unresolved where not already pinned.

## Gate state

Neither architecture is frozen. Native adversarial CI results, deeper history/conversation authority, full source denominator, alternative prototypes, complete ontology/requirements/oracle enforcement, implementation reachability and fresh independent falsification review remain open. No completion percentage is assigned.
