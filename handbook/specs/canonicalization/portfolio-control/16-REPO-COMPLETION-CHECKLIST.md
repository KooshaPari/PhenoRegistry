# Repository completion checklist

This is a gate checklist, not a substitute for project-specific requirements.

## G0 — identity and evidence

- [ ] Stable repo ID assigned.
- [ ] Observed ref/commit and timestamp recorded.
- [ ] Visibility, archive, fork/upstream and default branch recorded.
- [ ] Worktree/dirty/local-history limitations recorded.
- [ ] Exact available human intent preserved.
- [ ] Current, historical, proposed and superseded claims separated.
- [ ] One-sentence role hypothesis plus alternatives written.
- [ ] Consumers and authority conflicts identified.
- [ ] Historical-depth tier selected.

## G1 — docs and design

- [ ] Product users/jobs/journeys defined.
- [ ] Scope, non-goals and success/failure defined.
- [ ] FR/NFR/system requirements have stable IDs.
- [ ] Acceptance conditions and evidence methods exist.
- [ ] Domain/data/authority model exists.
- [ ] HLD/ALD/LLD cover applicable concerns.
- [ ] Material choices have ADRs with alternatives.
- [ ] SOTA includes direct, adjacent and no-build options.
- [ ] Critical parity floors, tradeable dimensions and wedge proposed.
- [ ] Research unknowns have hypotheses and experiments.
- [ ] Security, privacy and threat model exist.
- [ ] API/protocol/schema/versioning/migration specified.
- [ ] Operations/install/release/upgrade/rollback/support designed.
- [ ] WBS/DAG/PERT/work packages exist.
- [ ] Risks and decision queue exist.
- [ ] Trace links have no critical orphan.
- [ ] Existing richer docs/provenance systems preserved.
- [ ] Canonical docs do not contradict each other.

## G2 — red quality envelope

- [ ] Reproducible toolchain and lockfile.
- [ ] Format/lint/type/static checks.
- [ ] Characterization tests.
- [ ] Requirement-bound acceptance/contract tests.
- [ ] Unit/property/fuzz coverage where applicable.
- [ ] Negative controls or mutation evidence.
- [ ] Security/dependency/license/secret/provenance checks.
- [ ] Compatibility and migration harness.
- [ ] Performance/scale/resource/contention harness.
- [ ] Reliability/fault/soak harness.
- [ ] Docs/schema/link validation.
- [ ] Package/install/upgrade/rollback smoke.
- [ ] CI selects checks and propagates failures.
- [ ] Blocked platform/credential cases are not marked pass.

## G3 — green implementation

- [ ] Critical implementation is reachable in default/release build.
- [ ] No required behavior is mock/stub/fixture/document-only.
- [ ] Required feature/platform flags are built in CI.
- [ ] G2 quality envelope passes.
- [ ] Negative tests still fail when behavior is broken.
- [ ] Performance/resource floors met or exception accepted.
- [ ] Migrations and compatibility verified.
- [ ] Release artifact passes first-value journey.
- [ ] Public claims match evidence.
- [ ] Deferred horizon is explicit.

## G4 — pilot

- [ ] Bounded representative job selected.
- [ ] Closest alternatives and direct baseline selected.
- [ ] Same inputs and acceptance oracle.
- [ ] Versions/environment/resource budget fixed.
- [ ] Setup, DX, UX, semantics, runtime and operations measured.
- [ ] Failed runs and raw evidence retained.
- [ ] Critical floors evaluated.
- [ ] Trade ledger completed.
- [ ] Must-win wedge validated or rejected.
- [ ] Counterexamples documented.
- [ ] Product/repo disposition reconsidered.

## G5 — productization

- [ ] Installable/publishable artifact.
- [ ] Accurate quickstart and onboarding.
- [ ] Version/support/compatibility policy.
- [ ] Upgrade and rollback.
- [ ] Observability and incident response.
- [ ] Security disclosure and provenance/SBOM.
- [ ] Supported platform matrix evidenced.
- [ ] User-facing errors and accessibility.
- [ ] Case study or operational dogfood.
- [ ] Maintenance ownership and cost understood.

## G6 — ecosystem terminal state

- [ ] Canonical role and authority accepted.
- [ ] Registry updated from machine source.
- [ ] Duplicate claims removed or layered.
- [ ] Consumers and dependencies verified.
- [ ] Compatibility bridges owned and expiring.
- [ ] History/provenance preserved.
- [ ] Public brand/fork/archive status correct.
- [ ] Migration/tombstone complete if applicable.
- [ ] Repo birth/survival criteria satisfied.
- [ ] Terminal disposition recorded.
