# Pass 25 — mature semantic decomposition v2

Date 2026-09-30.

With VS-01 now machine-gradeable, specification work proceeds outward from the provisional baselines. New obligations were added only where mature journeys expose distinct behavior/lifecycle semantics; quality adjectives were not cloned.

## Portage
Mature obligations v2 `fe58810bce65a136c92966d1d51012d13e3923cf`.

Adds schema migration/export compatibility, evidence validity/freshness/custody, multi-step criticality, resource/network comparability, explicit N/A semantics, redaction referential integrity, Harbor-version compatibility and deterministic aggregation.

Next slice candidates:
- VS-02 schema/export compatibility;
- VS-03 multi-step/resource comparability;
- VS-04 freshness/custody/aggregation.

## PhenoMLX
v2 `ff2961311606989da6d5af96bb96742b27d1de1a`.

Adds profile schema migration, capability authority/version scoping, model-tokenizer/template compatibility, scheduler identity, cache warmth, resource collector scope, structured unsupported state, explicit degradation/fallback, workload population identity, support limitations, extension bounds and explainable selection/incomparability.

Next slices:
- VS-02 profile/capability compatibility;
- VS-03 measurement rigor;
- VS-04 support/extension/selection.

## PhenoLab
v2 `da309cec30e14009c9433294ab997ed765e604ec`.

Adds EvaluationReport compatibility, intended-vs-dirty candidate diff, baseline freshness, search-feedback laundering prevention, replicate completeness, explicit uncertainty/incomparability, durable budget across worker restart, optimizer proposal provenance, decision quorum/conflicts, idempotent target application, contemporaneous observation baseline, negative-learning equivalence and training-artifact lineage.

Next slices:
- VS-02 evidence/candidate/comparison integrity;
- VS-03 budget/replicate/proposal durability;
- VS-04 decision/application/observation governance;
- VS-05 learning/adaptation provenance.

## Count discipline

Counts are incidental outputs of decomposition:
- Portage gained 10 obligations;
- PhenoMLX gained 12;
- PhenoLab gained 13.

These numbers are recorded only for inventory; they were not targets and do not indicate completion.

## Next
Generate machine trace rows for v2, identify dependency ordering among slices, and continue source-ledger closure. Do not start VS-02 implementation before VS-01 evidence unless a slice is demonstrably independent and read-only/schema-only.
