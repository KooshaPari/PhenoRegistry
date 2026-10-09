# Pass 17 — architecture discrimination and expanded reds

Date 2026-09-30.

## Dino

Candidate a4409d25f71b23d92d51a55c5925bb9e48df1a84; run36687869773; artifact11084821466; sha2564f278d7cb617a30e64716a5c9b385d59d9bfb65f1f88a5bd69dd8ffe7d215126.

All 3 production generation controls remain red. All 3 fresh-generation prototype controls pass. This is strong isolated architecture discrimination, not runtime integration proof.

Next prototype adds per-consumer observed-generation acknowledgement because PackUnitSpawner, WaveInjector, AerialSpawnSystem and BuildMenuInjector retain registry references. Product prototype commit36932b5b4575e18bfd730ff0dd5923ac9a804ce7.

## Civis

Candidate ed8d8bbbffc4883ecbb7fa382c28aeb43ab60b14; run36687813616; artifact11085881640; sha2566ccfa7439c3f75158a4fb68133500179c5365a2978d3271600979f4df335d84f.

10 recovery tests executed:4 green,6 red. Both semantic-manifest prototype tests green. Production reds: economy PolicyInput reset; research loss; orphan guest memory; control Policy kind capitalist→noop; MarketState price lost; freshly-written v5 bundle with metadata removed silently loads through downgrade path.

Prototype expanded at4e8c39b13920bff1b565e6a9d13c2e494f78335e to include control policy kind and MarketState in addition to economy policy/research/mod identities. Outer format downgrade remains a separate classifier problem, not solved by semantic manifest.
