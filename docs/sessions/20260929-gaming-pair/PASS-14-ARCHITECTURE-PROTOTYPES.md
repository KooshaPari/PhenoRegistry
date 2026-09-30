# Pass 14 — architecture prototypes against reproduced reds

Date 2026-09-30. Exactly Dino + Civis.

## Dino

Current recovery controls have three reproduced failures:
1. removed content remains effective;
2. identical reload accumulates a conflict;
3. removed patch leaves stale patched YAML (150 HP instead of new disk value200).

Refined stale-patch run: `36673414046`, candidate `86f62e506defd46b05a0bab25c581eb2de43e55f`, artifact `11078932618`, sha256 `49c0902129b70932a293de7270b725d42baa07fe3c38a914490150363910ad31`.

Prototype commits `2ceabff476268b4133f7d957d544bb020986c3bc` / `d22724e9d36eb91973001fe1fa1784b3a512a4c5` implement test-only fresh-generation construction and publish-on-success. No production path changed. Prototype cases cover removal convergence, patch removal/current bytes, and failed candidate retaining prior published generation.

Workflow head `5727cae4367b805ca813d534324d80a2f9751e48`, run `36686256615`, queued at receipt. Filter runs both red controls and generation-prototype tests.

## Civis

Current recovery controls have three reproduced failures:
1. economy policy resets to default;
2. research cache loses progress;
3. guest memory can survive without corresponding loaded mod identity.

Test-only prototype commits `4d9a4d1b4977527b23bcd57f1d88bb624451acdf` / `6441a9720af2f68ee8016c2307992dd437819ecb` add a semantic state manifest containing economy policy, research state and active mod id/version/API identity. It restores policy/research into a fresh Simulation and detects guest-memory IDs not declared by the active mod set. It does not modify CivSaveBundle or production save format.

Workflow head `0d6fd4c809b030654553880847a041425503fc67`, run `36686311329`, queued at receipt. Filter runs both reproduced red controls and prototype tests.

## Interpretation rule

A passing prototype does not close the product defect. It establishes only that the proposed architectural boundary can satisfy the isolated counterexample without modifying the current production path. Migration, integration, failure atomicity, mounted user journey and independent review remain separate gates.
