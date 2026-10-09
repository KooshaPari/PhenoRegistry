# Pass 2 — authority resolution, lineage and fresh CI

Date 2026-09-29. This is additive to REC-20260929-TRIO-01. Product source snapshots remain frozen; specification branches advanced only with research documents.

## Portage

**Resolved more strongly:** the April 24 `portage` package/dependency-management audit is retained as a superseded historical classification. It contains only that classification and scorecard. The later stable-ID Portage dossier (`1165351720`) defines a Harbor-derived evaluation runner/environment-adapter role and an evaluation-specific acceptance horizon. No evidence inspected in the April record carries package-manager semantics into the current stable-ID product.

**New lineage evidence:** current Portage PR Actions reach Git operations that report a stranded `benchmarks/heliosbench` submodule path with no matching URL in `.gitmodules`. This makes HeliosBench source/history archaeology mandatory and directly corroborates the conversational lineage lead without proving its full contract.

**Fresh CI:** Portage PR #579 obtained actual Windows/Linux runners. Test jobs failed during dependency installation before test execution; Ruff reached lint and reported 37 fixable import-order errors. Native product tests therefore have no pass/fail receipt from this run. CI cleanup also hits the stranded HeliosBench record.

**New source contradiction:** root README advertises a `portage` CLI and named `litellm`/`llm` extras; frozen root `pyproject.toml` exposes `harbor`/`hr`/`hb` scripts and does not declare those named extras. Packaging/build indirection still needs tracing before choosing authority.

Repo-local receipt: Portage specification head `d03a8363e9b0765f9a4db83e370384d807a33485`, `PASS-2-AUTHORITY-AND-CI.md`.

## PhenoMLX

**Resolved more strongly:** `docs/guides/CANONICAL_REPO_CUTOVER.md` explicitly identifies tmp/temp and zz-archive variants as historical supersets and the canonical oMLX stack as the only active development home. They are predecessor evidence, not alternative current candidates. Registry's separately listed `PhenoMLX-temp` ID still needs stable-ID relationship confirmation before equating names.

No commit-associated PR workflow runs were returned for the first specification commit; absence is not green.

Repo-local receipt: PhenoMLX specification head `263a2ba8e45b7e4c59e766e5043fc652e0900f25`, `PASS-2-LINEAGE.md`.

## PhenoLab / PhenoLM

**Resolved more strongly:** Registry `projects/pheno-harness.json` records an operator decision on 2026-09-09: rename pheno-harness → PhenoLab, reverse the June absorption, retain as an active experimentation lab. The July 17 absorption record independently documents why the proposed generic tooling absorption was structurally invalid.

Inside the current repository, canonical root `SPEC.md` defines **PhenoLM** as the living LLM policy/eval/trace/reward/self-improvement layer in this repo. `PHENOLM_MIGRATION.md` says it is the target state and should not become a separate runtime service yet. `GARDEN_LOOP.md` supplies a fail-closed managed self-improvement doctrine with append-only ledger, rollback plans, holdout/regression/safety/budget/reproducibility/stability gates, consecutive green windows and human approval.

Thus repository identity and internal product/control-layer identity should not be collapsed: **PhenoLab is the retained repository/lab; PhenoLM is a documented product/control-layer identity living inside it.** The remaining authority question is semantic: the Sept. 9 “not a product” phrase may constrain external packaging while current canonical SPEC calls PhenoLM a living layer. Preserve both until the intended mature packaging is source-resolved.

The proposed EvaluationReport contract contains strong provenance ideas but explicitly labels itself proposed/not-yet-accepted, so it remains proposal evidence.

**Oracle gap strengthened:** existing tournament tests cover always-throw exceptions, not success-then-throw stale-result reuse; constructor storage of a verifier, not its invocation; and explicitly note that `run_tournament` ignores `n`. A stale cumulative-delta comment conflicts with the newer rerun source. Test presence is therefore not oracle completeness.

**Fresh CI:** nine PR #184 workflows completed failure; sampled ci/mutation/benchmark jobs have no recorded steps. This supports a current pre-execution/runner-infrastructure blocker, but does not establish the old suspected billing/quota cause and does not constitute native test failure.

Repo-local receipt: PhenoLab specification head `9e4bdb4bfb92864051f5a3957bbdb9cf32984c4d`, `PASS-2-AUTHORITY-ORACLE-CI.md`.

## Gate movement

Alias/history archaeology advanced materially for all three, but remains OPEN: Portage needs HeliosBench gitlink/predecessor recovery and exact fork delta; PhenoMLX needs predecessor stable-ID/delta comparison; PhenoLab needs the retained-lab versus PhenoLM product-packaging authority reconciled and old pheno-specs sources recovered.

Native oracle gate remains OPEN. Portage's runner executed setup but never tests; PhenoLab sampled jobs never reached steps; PhenoMLX has no returned PR-run receipt. No product receives a green, completion percentage or architecture freeze from this pass.

No fourth product, production implementation, merge, release, archive restore or destructive operation was started.
