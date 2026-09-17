# Recovery work plan

## Stage 0 — Freeze and identify

- Record remote object IDs, default branch, advertised refs, releases, packages, issues/PRs, and acquisition timestamp.
- Preserve mirrors read-only. Generate a second hash manifest before any repair experiment.
- Search for forks, renamed repositories, submodules, package registries, CI artifacts, and local-only exports.

**Exit:** evidence perimeter documented; known gaps explicitly listed.

## Stage 1 — Repository-local forensic reconstruction

For each scoped repository:

- construct first-parent and all-parent timelines;
- classify merges, reverts, force-push discontinuities, mass rewrites, generated bursts, and deletions;
- diff every branch tip against merge base and default;
- trace capabilities through code, tests, docs, and build definitions;
- identify the last reproducibly valid point for each capability, not one global “good commit.”

**Exit:** capability-by-commit matrix and contradiction ledger exist.

## Stage 2 — Cross-repository reconciliation

- Resolve runtime, package, CLI, API, schema, protocol, and workflow edges.
- Detect duplicated ownership and version skew.
- Determine whether `helios-cli`, `heliosLab`, `forgecode`, and `Agentora` are products, packages, experiments, or layers; do not infer roles from names.
- Build one ecosystem graph and one responsibility matrix, while retaining per-repo evidence.

**Exit:** every boundary has an accepted owner or an explicit unresolved decision.

## Stage 3 — Competing target-state candidates

Build at least three coherent candidates where evidence permits:

- conservative current-default hardening;
- maximal valid capability recovery;
- clean-room target architecture preserving only validated contracts.

Score each on intent coverage, verified behavior, migration cost, security, maintainability, and reversibility. Reject candidates with recorded evidence.

**Exit:** target-state ADR accepted; dissenting evidence preserved.

## Stage 4 — Isolated replay and repair

- Create recovery branches from immutable bases.
- Replay capability slices in dependency order, not chronological bulk merges.
- Add characterization tests before behavior-changing repairs.
- Regenerate lockfiles and generated assets only through documented commands.
- Keep one change class per commit and embed evidence IDs.

**Exit:** build/test matrix passes or every failure is classified and accepted.

## Stage 5 — SSOT generation

- Generate canonical docs from adjudicated decisions and verified implementation.
- Backlink every normative requirement to code/tests and every implementation claim to evidence.
- Mark planned behavior distinctly from implemented behavior.
- Install drift checks in CI.

**Exit:** a new contributor can reproduce the verified state and explain rejected alternatives without oral history.

## Stage 6 — Integration proposal

- Produce patches/PRs; do not rewrite remote history.
- Include migration, rollback, compatibility, and release plans.
- Require explicit authorization before merges, deletions, archival, or branch cleanup.
