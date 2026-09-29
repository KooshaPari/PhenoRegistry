# Internal archaeology — findings and source obligations

All references use SNAPSHOTS.json revisions. Date: 2026-09-29. This pass is bounded; a file read is not source resolution.

## I-01: preserve the intended topology without deciding the winner

Retrieved Aug 29 user context distinguishes an app, two CLI lineages and a general agent SDK. Sep 18 context explicitly identifies HeliosLite/HeliosCLI/KCode overlap and asks for reconciliation. Therefore neither a three-way merger nor permanent retention of every runtime is accepted simply because each exists. The current two-primary cap is honored while family-level dependencies remain part of the inquiry.

## I-02: Shared custody records conflict

Registry `BOUNDARY_OWNERS.md` retains June-era directions that phenoShared is interim staging and not a final boundary owner. Shared `docs/atlas/products/Agentora-capability/DOSSIER.md` describes proposed agent-framework capability custody after absorption; it explicitly says identity and actual exported source/consumers require investigation. Later user context assigns Shared preservation and SDK shaping. Current user assignment includes PhenoShared.

Immediate operating consequence: preserve and inspect Shared as directed; do not execute the older deletion recommendation. Unresolved consequence: exact accepted SDK/capability homes and consumer contracts still require source/history reconciliation. This pass does not globally rewrite historical boundary policy or pretend that a proposed dossier proves a functioning SDK.

## I-03: old atlas states are intentionally bounded, not current scorecards

Registry `docs/governance/atlas/products/HeliosLite/STATE.md` (also mirrored under handbook/specs/program-docset) records Sep 16 at source `6de2d161d8a44f0b65ef7fbd243f2a287257aecc`; KCode's counterpart references `88a996e030c203e776b31ca61720d09b362d787a`. Those are not the Sep 29 sampled sources. Preserve source date and extent rather than carrying grades forward. Mirrored dossier authority needs reconciliation.

## I-04: imported absorption evidence has weak links

`audits/org-audits/airlock-decisions/2026-07-14-26ffbedabd25-heliosHarness-absorbed-into-helios-cli.md` is authored by an automated Forge pass. It references June workspace and KLA/harness_recorder absorption, old short commits and unavailable local airlock mirrors. It even cites a branch name as an absorption manifest. That is evidence to investigate, not proof of complete capability transfer. Full useful history, semantic parity, mounted consumers and preservation refs remain open.

## I-05: current dependency pin is a separate source identity

HeliosLite Cargo.toml pins phenotype-health/observability/telemetry to Shared `b2d06d5376c1e94e207c679f402597103a5a10a4`, not the separately observed Shared default `d24b13ed...`. The pinned agileplus-cache manifest lacks a package table despite a repair claim in its commit message. This is a source inconsistency; selected dependency reachability and Cargo behavior must be tested before claiming a HeliosLite build failure. Do not silently update dependencies or substitute newer evidence.

## Source coverage delegation

Detailed primary-family ledgers are in each repository's `docs/product-contract/20260929-harness-recovery/SOURCE-COVERAGE-LEDGER.md`. Both remain OPEN. Registry research sources also remain partial: AGENTS read; BOUNDARY_OWNERS read in bounded sections; atlas sample/alias search; one airlock decision read; Shared Agentora dossier read; conversation summaries retrieved. Complete Registry useful history, duplicates, accepted ADRs and source-authority reconciliation are not finished.

## Priority falsification experiments

HeliosLite: run native adversarial benchmark fixtures demonstrating empty checks, missing output, timeout propagation, validation-failure exit and signalled verifier; reconcile lock/build graph and restart semantics. KCode: bind a newly built client to old versus new isolated daemon; validate install/update delivery; inspect startup signing on supported macOS configurations; reproduce historically reported failure cases against the pinned candidate. Shared: trace actual exported framework/source consumers, not just names or absorbed-folder parity.

Independent fresh review has NOT occurred. This author's adversarial analysis is not mislabeled independent review.
