# Pass 31 — migration and machine-receipt controls

Date 2026-09-30. Exactly Dino + Civis.

## Dino PR491

Candidate7209b21024427f9ff4b286efa669c1dc9a502b45 requalified GenerationStore core in run36716275644:4/4 passed, artifact11096248237 sha256 cf80efda079d3735d1094df4eb123b6d9b75536213331cee10577a25241ddf9b.

ReloadResult optional path/generation truth fields are now compiled into the integration candidate and a pure test binds requested/resolved path, desired/active generation, fullyObserved=false and restart-required disposition. This proves DTO representational capacity only; HandleReloadPacks still requires host/runtime integration to actually populate truthful values and honor requested path.

Receipt-contract run36716747784 queued.

## Civis PR1569

Opt-in SemanticBundleBridge migration controls expanded:
- adding semantic-state.json to an existing v5/current directory must not rewrite world_state.json bytes;
- future semantic schema fails before default bundle load/application;
- missing semantic component remains valid for default loader but invalid for opt-in bridge;
- policy/research reproduced losses are expected green through opt-in bridge.

Default CivSaveBundle remains unchanged. Run36716733597 queued. Earlier queued runs superseded by this exact candidate and receive no transferred credit.

No third product.
