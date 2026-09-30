# Pass 23 — implementation-candidate separation

Date 2026-09-30. Exactly Dino + Civis.

## Dino

The isolated architecture threshold is now bound to candidate0124edd7aff871ca63d8f92fc4cd959bd3cbb5f4, run36706610552, artifact11091884496 sha25621578ca478df3651f1911e1d41826c60c9ce39b6c1f4bd5630e949233b186302:12 tests =9 architecture/real-consumer-semantics greens vs3 unchanged production reload reds.

A separate implementation experiment branch was created from the spec branch, not main:
- branch experiment/generation-store-20260930
- draft PR https://github.com/KooshaPari/Dino/pull/491
- current head99dfa33e7ea966d6a506292b3894ceec1dfe4a1e
- base spec/mature-recovery-20260929
- adds production-shaped Runtime.Generation.GenerationStore and isolated integration-candidate tests
- does NOT wire ModPlatform/live consumers yet
- no merge authorization.

This preserves source snapshot/specification branch/implementation candidate as distinct identities.

## Civis

Exact expanded semantic-state candidate d990d704e4850ef2760fcf3faa12af512586944a is queued in Recovery Oracles run36711269740. This is the first admissible run intended to qualify the tutorial/religion/caravan expansion on that exact candidate. Until completion, those added prototype domains remain pending.

Latest admitted older architecture evidence remains candidate e7295934..., run36705777195:11 prototype/guard greens vs9 production reds.

No third product.
