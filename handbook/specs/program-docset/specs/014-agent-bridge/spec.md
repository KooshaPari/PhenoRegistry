# Agent bridge and graphical proof

Source: INT-006. This is a proposed implementation contract, not a live engine state.

## PROOF-14-01 — Access inventory
Declare owned, gray and black-box access per boundary and operation.

Acceptance: An unavailable proprietary-state API cannot be marked exercised.

## PROOF-14-02 — Instance binding
Bind actions, observations and captures to the intended artifact/session/window/world.

Acceptance: A wrong process or stale nonce is rejected before input.

## PROOF-14-03 — Separated action modes
Distinguish fixture control, semantic commands and actual user input.

Acceptance: Teleport/state mutation cannot satisfy a click-and-move user-path criterion.

## PROOF-14-04 — Observed completion
Correlate accepted command, domain result, pixels and persistence as applicable.

Acceptance: Acknowledgement without the required effect is non-accepting.

## PROOF-14-05 — Clock and frame identity
Record monotonic/action, simulation, render and capture relationships.

Acceptance: A prior frame from the correct window cannot prove a new action.

## PROOF-14-06 — Private isolation
Use approved private sessions, per-run writable state, limits and entitlements.

Acceptance: Cross-worker capture/data access or missing license cannot be bypassed to pass.

## PROOF-14-07 — Native product path
Test actual installed output as well as embedded/headless diagnostic profiles.

Acceptance: A logic-only run is rejected for a required graphical claim.

## PROOF-14-08 — Bridge fault semantics
Qualify lifecycle, cancellation, missing methods and uncertain outcomes.

Acceptance: Timeout is not successful completion and uncertain side effects are reconciled before retry.

## PROOF-14-09 — Fine visual witnesses
Bind tiny visual features to reviewed regions, camera/scale and independent evidence.

Acceptance: A missing small required icon fails even if full-frame similarity is high.

## PROOF-14-10 — Temporal witnesses
Capture enough frames to test flicker, stutter, LOD and animation behavior.

Acceptance: A lucky still frame cannot satisfy a temporal criterion.

## PROOF-14-11 — Shipping fidelity
Test controlled regression and representative shipping profiles separately.

Acceptance: Disabling the effect under test cannot produce shipping-quality approval.

## PROOF-14-12 — Visual calibration
Use known-good/bad classes, holdouts, model/metric provenance and disagreement rules.

Acceptance: Known-bad subtle examples must be caught at the predeclared required rates.
