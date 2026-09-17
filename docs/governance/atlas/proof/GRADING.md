# An evidence-backed percentage and grade

## Yes: calculate a literal grade

The program must provide a numerical result for a declared assignment, not only a qualitative narrative or traffic light. The assignment is a versioned product scope, rubric, support profile and candidate artifact. No score claims to measure every possible future feature or all subjective quality. Numerical grading is now explicitly required; it does not weaken critical gates or evidence honesty.

The following defaults are proposed program policy, not an accepted industry standard. Resolve them through the existing scorecard owner instead of launching a competing grading project. Preserve richer accepted rubric definitions and import them through adapters.

## Freeze the denominator and weighting

Select applicable categories for the product role. A proposed GUI/game profile is: intent/design 12; specification/architecture 10; real behavior 20; independent assurance 18; user experience/rendering 14; safety/recovery/security 12; ecosystem reuse/composition 5; delivery/operations 5; documentation/research 4. Weights sum to 100. Infrastructure or CLI profiles differ explicitly; do not force a graphical denominator onto an API library.

Within category k, split its weight among declared criteria i. Let a_i be the normalized within-category weight, with sum a_i = 1. Let x_i be the earned fraction from an admissible evaluator receipt, between 0 and 1. Missing, stale, wrong-scope, unexecuted or inadmissible evidence earns zero, while remaining visible as unknown/blocked rather than a demonstrated behavioral failure.

    category_k = sum(a_i * x_i)
    score = sum(category_weight_k * category_k)

The score is between 0 and 100. This is not the percentage of tests passing, percentage of lines visited, percentage of files documented or percentage of a real-world truth discovered. Each is a separate possible metric with its own denominator.

Proposed letter mapping: A >= 95; B >= 85; C >= 70; D >= 50; F < 50. A production profile may set stricter limits. Display the value and letter WITH the gate state: '96.2 / A - BLOCKED: save-corruption invariant failed'. Do not hide the blocker in a tooltip or cap the arithmetic invisibly. A grade never grants merge, release, deployment or delete authority.

## Critical gates cannot be traded away

Every critical obligation needs full credit and all required modalities/action paths. Other mandatory checks satisfy their declared thresholds. Independent unit/integration/E2E 85% floors are separate mandatory cells; preserve higher accepted floors. High unit coverage does not compensate for low integration coverage. Documentation cannot compensate for a required launch, consent, persistence or isolation failure.

A missing required measurement makes acceptance UNASSESSED/UNVERIFIED; an established violated mandatory threshold makes it BLOCKED. Empty, not-run, skipped, errored or infrastructure-blocked checks never count as passes. A pass on a direct domain API cannot satisfy a required user-input interaction without that evidence channel.

## Honest state beneath the number

Return at least: score and grade; gate state and failed/missing mandatory IDs; evidence-assessed weight; unknown/inadmissible weight; category vector; target/source/profile/rubric identifiers; timestamp; reference constraints and authenticated-authority status.

The optional 'known-score to all-unknown-perfect' range is an arithmetic bound over unassessed criteria, NOT a confidence interval or probability. A known failure stays a known failure in that range. Statistical intervals for stochastic benchmarks belong to their native metric reports. Do not multiply by the agent's claimed confidence.

Separately show current-CVP and full-horizon scope scores, design readiness, verified implementation, delivery readiness and operational evidence where required. They are projections over declared criteria, not an excuse to cherry-pick a higher headline. Product/library/CLI scores are comparable only under compatible rubric profiles and support boundaries.

## A synthetic worked example

Assume the category vector (in the order above) is 0.95, 0.90, 0.85, 0.82, 0.70, 0.90, 0.80, 0.75, 0.90. With the proposed weights the score is 84.11 / C. If a mandatory save/load invariant fails, the status is BLOCKED regardless of the average. This is arithmetic illustration, not any repository's grade.

If newly discovered requirements enlarge the accepted scope, show scope revision N and N+1 and recompute a same-scope comparison where possible. Do not call a denominator change an implementation regression, and do not hide it to keep the score rising. Breakdowns should expose removed/added criteria, waived scope, invalidated evidence and actual behavior changes.

## Prevent grading games

Fix category weights before measurement. Adding 500 easy tests cannot dilute a hard visual failure. Refactoring code into more files cannot raise purpose coverage merely by record multiplication. A criterion split conserves parent weight. Aliases and duplicate evidence are not new independent obligations. Critical status and N/A/exemption decisions are externally reviewed and versioned. Expired waivers reopen gates.

Do not accept arbitrary latest reports: bind candidate digest, source, support profile, oracle version and execution. A successful unit test of the reporter is not product evidence. Reject canned scores, screenshot paths without accessible media, test lists without execution, success-after-collection-error and automatically accepted baseline refreshes. Keep an adversarial holdout corpus and audit the grader independently from the implementer.

## Qualitative and emergent properties

Some perceptual, creative and game-design goals use anchored model-assisted rubrics, user studies or human adjudication. These can produce useful repeatable grades when calibrated and labelled; they are not infallible machine proofs of fun, accessibility or taste. A machine-only proxy that is not qualified for a critical decision leaves that gate unresolved. Use actual media, specific judged criteria, multiple cases and explicit disagreement handling.

White-box products can supply deep structural measurements. Gray/black-box host-game internals are outside owned-source denominators under an approved profile, while the full observable user contract remains in scope. Do not pretend to measure inaccessible engine-line coverage or mark all graphical behavior N/A.

## Reference implementation boundary

[grade.py](grade.py) computes weighted scores and selected admission checks against local JSON receipts/artifact files. It verifies source/artifact/profile/oracle identity, age, permitted action modes, required modalities, counts, unique IDs and hashes. It cannot independently certify that a producer executed honestly, that a screenshot depicts the right scene, that a semantic judge is accurate, or that approval references are authentic.

All bundled examples use a synthetic subject. Output always states `product_qualified=false`, `producer_authenticity_verified=false`, and `release_authorized=false`. Integrate trusted runner attestation, independent review, calibration and the existing real rubric/engine before treating production scores as accepted. The grader is a small reference adapter, not a new SSOT service or a replacement for native validators.
