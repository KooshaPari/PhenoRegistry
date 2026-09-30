# Pass 23 — provisional baselines, quality overlays, developer handoff

Date 2026-09-30.

After repeated semantic attacks yielded only hardening deltas, the current contract chains were consolidated into clean **provisional semantic baselines**. “Provisional” is important: native architecture gates remain open.

## Portage
Baseline `45d574d93aee2331281f8fd102eacfac9e4f3c31`.
Quality overlays `f85155f6c7a1e3ba3002e0d5c79eb38f65474dad`.
VS-01 handoff `aa452f1b8eb9f5392173efa339acd65aad0ef2a2`.

Handoff is a thin real-Harbor evidence envelope, with mandatory artifact/criterion/subject/cancel/regrade/credential/import adversaries. It explicitly forbids rebuilding Harbor primitives.

## PhenoMLX
Baseline `73a5bcc4a7a45e63c54b26bc56106d0d2d7bfb33`.
Quality overlays `66c503ccedaf78fd214aeb771465c0a04e0a1353`.
VS-01 `7baa882475f064b1d45a743fbac7c280af6e3b64`.

Handoff uses existing backend adapters and requires two real engines/common model, explicit observability/unsupported states, matched workload and lifecycle evidence. It forbids engine/cache rewrites absent measured deficiency.

## PhenoLab / PhenoLM
Baseline `e1800487c4f38b0239066981ae77abba83afcacb`.
Quality overlays `5044529b40dd0b232c13a41f697bc1c81276da61`.
VS-01 `da379f8a8c30291b7cc4de52ca7d601414b9416a`.

Handoff mandates reuse of canonical EvaluationReport v0.5, real garden gates, promotion eligibility and risky-action policy. It requires one real live-verified Candidate→Assessment→Decision→application vertical, worker restart and adversarial false-green cases. It explicitly forbids mock/inferred evidence from closing the native gate.

## Meaning of provisional baseline

These baselines may now be used as the semantic spine for:
- further requirement decomposition;
- quality-property binding;
- schema design;
- bounded implementation experiments;
- traceability and oracle generation.

They may **not** be used to claim:
- architecture gate complete;
- existence gate complete;
- CVP complete;
- specification/design 100%;
- native evidence where only static/source evidence exists.

## Next program work

1. expand obligations from the provisional baseline capability-by-capability without target counts;
2. bind quality overlays only where applicable;
3. generate schema drafts + machine-readable trace records for VS-01;
4. continue source-ledger resolution, especially release/security/integration consumers;
5. developer agents can begin VS-01 when their required runtime is available;
6. independently review the resulting real evidence before baseline becomes non-provisional.

This is the first point in the program where a developer-agent handoff is appropriate, but only for the bounded VS-01 experiments—not broad product implementation.
