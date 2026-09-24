# Validation — federation amendment v1.3

## Completed checks

- The full inherited reference suite plus 35 added federation schema/consistency tests: **238 tests passed**. These are documentation/reference-tooling tests, not product suites.
- Two explicitly synthetic reciprocal plans pass selected shape/reference invariants. Their outputs state `activation_authorized: false`, `grant_authenticity_checked: false`, and `product_behavior_verified: false`.
- New negative cases reject missing/unknown fields, fabricated live results/approval, artifact-lock mismatches, missing products/providers, wrong principal/workspace, wrong authority/contracts, missing grant references, invalid host slots/adapters and startup/mount cycles.
- The 56 proposed requirements are linked to 56 planned acceptance scenarios, SPEC-12, source INT-005 and the main work/traceability registries. All product-evidence arrays remain empty.
- The 12 new work packages form an acyclic dependency graph and carry no mutation authority. Existing-owner federation packets cover all 24 IDs in the inherited snapshot; no live inventory refresh or session observation is implied.
- All 17 pages of the generated PDF were rendered and visually inspected. No out-of-page text blocks were found by the geometric check. PDF is a reading edition, not a tagged-accessibility conformance claim.
- Existing input archives and earlier exact prompts remain unchanged; the latest exact visible user message and the inspected v1.2 input archive have recorded SHA-256 identities.
- Full-package JSON/schema/reference/link checks and final ZIP/manifest integrity checks are performed during packaging; their machine reports accompany this file.

## Limits

The checker is intentionally **not a production resolver or permission engine**. It does not verify real publisher signatures, actual grants/entitlements, native identities, package installation, interface behavior, semantic version compatibility, UI rendering, performance, sandbox strength or data recovery. A forged but internally consistent synthetic record can pass. Native acceptance requires real artifacts, qualified adapters, trusted receipts and independent review.

The legacy applet schema is retained and still has a free-text federation-policy field. New illustrative profiles are additive and restricted to examples; no old record becomes executable by inference. No new vendor runtime or generic UI toolkit is mandated.

All product scenarios and comparative pilots remain **PLANNED_NOT_EXECUTED**. There is no measured product advantage, new released app, automatic installed integration, App Center, GitHub change, DNS change, repository migration or source decontamination performed by this packaging exercise.

See `reference-test-result.json`, `reference-tests.log`, `package-validation.json`, `example-plan-results.json` and `input-artifact-review.json` for reproducibility. Run from docs/: `python scripts/validate_package.py .`, `python federation/check_plans.py`, and `python -m unittest discover -s tests -v` in a suitable environment with the declared dependencies.
