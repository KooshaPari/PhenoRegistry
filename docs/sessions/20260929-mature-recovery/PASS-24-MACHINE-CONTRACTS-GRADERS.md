# Pass 24 — machine contracts and VS-01 graders

Date 2026-09-30.

The provisional semantic baselines are now operationalized into deterministic developer-agent contracts.

## Portage
Baseline `45d574d...`.
Schema `db83a17e0e831e3e4290a682d89a87f9824abe92`.
Machine trace `7121b5b8ce873d45e5de76069bda031217c920a2`.
VS-01 gate `00aafcb531f420357189fbbd40bef53a1b23b8db`.

Blocking trace rows distinguish native-required evidence from schema/static evidence. Automatic red includes skipped/setup failure, wrong candidate, hidden xfail and raw secret leakage.

## PhenoMLX
Baseline `73a5bcc...`.
Schema `3e0fd85254b54ed455c6e0cc5d5daee4ec6252b9`.
Trace `b5a198612f105288e2e2652711684c1957b9384a`.
Gate `27fc2c50a438559d915c0ef5dc07770b7835b746`.

The gate requires two real engines/common exact model, matched workload, quality oracle, explicit observability and lifecycle evidence. Static capabilities, cross-hardware comparisons and fabricated unknowns are automatic red.

## PhenoLab
Baseline `e180048...`.
Schema `d759e91163f67d4b52f0956a2e3a5b6b9bc3cf98`.
Trace `c3268d1a2ecadfd452e237779d8ae80624d3ee4c`.
Gate `4a560bd504f861a6feb3d87652dcd27299b67f6f`.

The gate requires real live-verified EvaluationReport evidence, grader implementation digest, Candidate/Epoch binding, existing hard gates, Assessment/Decision separation, durable restart and malicious false-green controls. Inferred/reported/mock evidence is automatic red.

## Consequence

Developer agents now have:
1. semantic baseline;
2. quality overlays;
3. bounded handoff;
4. JSON Schema;
5. machine-readable obligation→oracle→evidence map;
6. deterministic completion gate.

This is enough to begin bounded VS-01 implementation without relying on chat interpretation.

The next specification-side work should expand mature obligations beyond VS-01 and bind stage/journey/quality relationships, while implementation evidence returns asynchronously through PRs/commits. Native architecture gates remain open until those evidence bundles exist.
