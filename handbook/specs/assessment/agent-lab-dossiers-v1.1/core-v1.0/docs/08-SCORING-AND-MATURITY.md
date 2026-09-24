# Scoring and maturity

## Frozen quantities

For the accepted applicable instance set, let P be current verified pass weight, F current verified fail weight and U unresolved outcome weight. Unresolved applicability is A? and is reported separately. N/A weight has an accepted reason; a waiver is not N/A or PASS.

- Assessed pass rate = P / (P + F).
- Assessment coverage = (P + F) / (P + F + U).
- Verified satisfaction within settled applicability = P / (P + F + U).
- Optimistic bound within settled applicability = (P + U) / (P + F + U).

A zero denominator is null, never 100%. These are reporting quantities, not probabilities or calibrated confidence intervals. If applicability is unresolved, do not call the settled-subset score the complete product result. Report catalog survey coverage separately from selected-scope assessment coverage.

Example: 90 passes, 10 failures and 900 unknown unit-weight obligations yield 90% assessed pass rate, 10% assessment coverage and 9% verified satisfaction. The product is not 90% complete. Adding a thousand irrelevant checks would not make that conclusion more precise.

## Effective evidence

PASS/FAIL require completed execution, accepted review, current evidence, adequate instrument qualification, correct subject/assignment bindings and the required observation path. Stale or invalid evidence, errors, disputed leaves, waivers and absent results contribute unresolved outcome. A structurally valid forged record is still a forgery; the reducer's consistency check is not a trust service.

## Gates

Critical gates are conjunctive and non-compensating. Every required member must pass at the required assurance level. High documentation quality cannot compensate for an authorization or integrity failure. The reference kernel reports FAIL for a valid required failure, BLOCKED for unresolved or unlocked requirements, PASS only for a satisfied bounded gate, and NOT_EVALUATED when no qualifying gate was defined. Gate calculation is not publication permission.

Weights come from the accepted assignment, not the catalog's length. Do not count aliases or duplicate framework mappings twice. The reference kernel rejects repeated obligation keys. A richer grouping design must preserve fixed group weights when splitting criteria.

## Maturity vector

Report concept, feasibility prototype, integrated prototype, slice MVP, supported product and validated/expanding product as scoped labels with explicit gate definitions. A slice MVP means the intended beneficiary can obtain the minimum promised outcome through a complete journey with mandatory safeguards and a feedback path. It need not have externally demonstrated product-market fit.

Keep DESIGN_READY, PIPELINE_VERIFIED, PRODUCT_VERIFIED, PUBLISHED_VERIFIED and OPERATED_VERIFIED separate. Track value evidence as untested, internal/dogfood, external pilot, repeated benefit or sustained use. Preserve agent readiness separately from product usefulness. Cross-repository maturity needs an integrated BOM and real consumer journey.

## Changing baselines

Decompose score changes into product, evidence, scope, evaluator and policy deltas. Preserve both old and new baseline scores when feasible. Discovering a new obligation can lower a score while increasing understanding. Easier requirements can raise a score without improving the implementation. Never present either as an unexplained productivity trend.
