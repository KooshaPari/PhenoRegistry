# Validation report

**Generated:** 2026-09-01  
**Package:** `phenotype-portfolio-control`  
**Status:** PASS

## Scope

This validates the portfolio-control artifact package. It does **not** validate the implementation, history, builds, consumers, or product completeness of the 146 repositories.

## Results

| Check | Status | Detail |
|---|---|---|
| JSON parsing | PASS | 8 files parsed; errors=[] |
| JSON Schema meta-validation | PASS | 4 schemas checked; errors=[] |
| Inventory count | PASS | count=146 |
| Unique repository names | PASS | unique=146 |
| Unique repository IDs | PASS | unique=146 |
| Cluster assignment covers inventory | PASS | cluster_rows=146, unique=146, missing=set(), extra=set() |
| Decision IDs unique | PASS | count=12 |
| Task IDs unique | PASS | count=34 |
| Task predecessors exist | PASS | missing=[] |
| Task DAG acyclic | PASS | topological_count=34 |
| PERT calculations | PASS | errors=[] |
| No empty files | PASS | empty=[] |
| Internal Markdown links | PASS | checked=34, broken=[] |

## Artifact metrics before checksum manifests

- Files: 42
- Approximate words across text/JSON artifacts: 38,387
- Repository records: 146
- Provisional family assignments: 146
- Central decisions: 12
- Initial work tasks: 34
- JSON schemas: 4
- Dependency-only PERT critical path: 605.00 agent-hours

## Coverage completed

- Connected-account census.
- Stable repository IDs.
- Initial visibility/archive capture.
- Provisional family routing.
- Portfolio audit and boundary policies.
- Completeness and maturity gates.
- Forensic escalation policy.
- SOTA/pilot protocol.
- Current/transition/target maps.
- Initial decision queue.
- Initial WBS, PERT and DAG.
- Worker prompts, schemas and templates.

## Coverage not completed

- Immutable current tip SHA for every repository.
- Fork/upstream discovery for every repository.
- Description/language/package/release inventory for every repository.
- Local-only refs, worktrees, reflogs and unpushed branches.
- Current-tree code/doc/CI audit for every repository.
- Deep historical and semantic clone analysis.
- Consumer/co-change graph.
- Per-repository G0–G6 assessment.
- Final source→target disposition.
- Executed migrations.
- Product pilots.

These are the work governed by this package. They must not be inferred from the census.

## Reproduction

A validator should:

1. Parse all `*.json`.
2. Meta-validate `schemas/*.json` as JSON Schema Draft 2020-12.
3. Assert 146 unique repository records and IDs.
4. Assert every repository is assigned exactly once in the provisional routing map.
5. Assert unique decision and task IDs.
6. Assert every task predecessor exists.
7. Topologically sort the task graph.
8. Recompute PERT values.
9. Check relative Markdown links.
10. Check empty files and checksums.

## Honesty statement

The package is an **audit program and initial portfolio map**, not the completed 146-repository audit. Initial role and target statements are labeled hypotheses. No repository has been archived, merged, migrated, or declared complete by this artifact.
