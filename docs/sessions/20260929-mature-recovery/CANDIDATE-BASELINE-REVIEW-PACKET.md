# Candidate semantic baseline review packet — trio

Date: 2026-09-30.

This packet does not award a baseline. It makes the gate inspectable.

| Dimension | Portage | PhenoMLX | PhenoLab/PhenoLM |
|---|---|---|---|
| direct intent recovery | substantial / residual | substantial | strong / old spec bounded missing |
| historical lineage | residual blocker | accessible refs classified | bounded missing old spec |
| SOTA/alternative attack | strong first pass | strong engine first pass | strong optimizer first pass |
| existence thesis | thin layer unproven | typed profile unproven | typed control layer unproven |
| ontology falsification | v1+ survived subsequent attacks | v1+ survived | v1+ survived |
| obligations/journeys | v0+v1 mapped | mapped | mapped |
| state-machine prototype | PASS_STATIC | PASS_STATIC | PASS_STATIC |
| real-class integration | PASS_SOURCE/STATIC | PASS_SOURCE/STATIC | PASS_SOURCE/STATIC |
| persistence/restart | PASS_STATIC | PASS_STATIC | PASS_STATIC |
| native oracle execution | BLOCKED_INFRA | NOT_RUN | BLOCKED_INFRA |
| real vertical architecture experiment | BLOCKED/OPEN | OPEN | OPEN |
| source coverage | high-partial | high-partial | high-partial |
| contradictions blocking semantics | none known after v0.3/Portage v0.4 delta | none known | none known |
| baseline decision | BLOCKED | BLOCKED | BLOCKED |

## Promotion rule

A candidate semantic baseline may be promoted only when:
1. consolidated contract covers all accepted obligations/journeys with no unresolved semantic contradiction;
2. major alternative architectures are represented or rejected with evidence;
3. high-risk architecture hypothesis has at least one real integration/vertical result, not only static model tests;
4. source coverage blockers are bounded and non-semantic residuals are explicitly carried;
5. native evidence identity is trustworthy enough that false green cannot be manufactured by missing/skipped setup.

Current failure is primarily #3/#5, plus product-specific existence/source-boundary blockers.

## What baseline promotion would mean

It would freeze the semantic spine as the working denominator for exhaustive decomposition and implementation mapping. It would **not** mean product implementation complete, CVP complete, or design 100%.

## Immediate remaining native verticals

Portage: execute a real Harbor trial and transform TrialConfig/TrialResult/ArtifactManifest into Portage envelopes; adversarially fail a required artifact and wrong-subject binding.

PhenoMLX: on one actual environment, pin two available engines + common model, capture versions/realized profiles, run a small matched workload, record explicit unsupported/unknown fields and lifecycle.

PhenoLab: run one existing suite to canonical EvaluationReport, bind Candidate/Epoch, pass through evidence gate + evaluate_gates, persist Assessment/Decision, restart worker/process and reload; include malicious policy change as new epoch.

Until then: **no baseline promotion**.
