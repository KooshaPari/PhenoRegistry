# Pass 21 — qualification boundaries and state denominator

Date 2026-09-30. Exactly Dino + Civis.

## Dino

The isolated SDK generation architecture remains strongly supported:
- production reload path: 3 reproduced reds;
- architecture/control-plane: 7 candidate-bound greens on run 36700623226, artifact11089727636, sha256 8f62449d0e2a8c59fb05952de36f7353e9a9c48964c94296e50526eb5357806d;
- later SDK-only run36701768268 on candidate046b03c9f0fdc91f7702e63f5472379701ecfd04 reproduced the same split and artifact11090312122 sha256659d61cca6cb4e6316a5e91abdf680c4e1993866d9610bcfc0634442798a95ae.

Attempted real Runtime consumer test was correctly blocked by environment/build target: when GameInstalled=false the Runtime csproj removes Unity/ECS sources from the CI assembly. The source files do exist, but absence from that assembly is intentional. The game-only probe is quarantined from SDK CI rather than widening production build rules or mocking Unity to manufacture a green.

Mounted first consumer denominator: PackUnitSpawner, WaveInjector, AerialSpawnSystem, BuildMenuInjector plus HotReloadBridge migration surface. Economy/Scenario/UI/Warfare facades retain registries but are not added to the live ACK denominator until a mounted caller is proven.

## Civis

Mechanical state denominator at concurrent source54d5758970249c8d1f24688ea45920b530e77299:
- Simulation:125 fields;
- WorldState:48 fields.

Persisted at product-local STATE-MANIFEST-v0.json. Initial recovery classifications include:
- 47 Simulation fields still UNKNOWN before latest probes;
- 42 EPHEMERAL_CANDIDATE rather than assumed ephemeral;
- reproduced omissions: research_cache, economy_policy, policy, market_state;
- source-derived omission candidates pending execution: tutorial_progress, religious_profiles, active_caravans.

Evidence for those candidates:
- TutorialProgress is explicitly described by existing tests/docs as persistence-facing; no active CivSaveBundle/replay restore path found.
- religious_profiles is dashboard-visible and consumed by emergence/tutorial/culture; persistence code was found only in orphan/unmounted save.rs, not active CivSaveBundle.
- active_caravans represents in-transit future-affecting trade state; no active save/replay path found.

Recovery workflow was narrowed to civ-engine --lib and path filters repaired to the actual recovery files. Branch-scoped concurrency now prevents future recovery pushes from accumulating additional redundant recovery runs. Existing older runs created before that policy may still drain normally.

## Authority/evidence rule

SOURCE_DERIVED_OMISSION_CANDIDATE != reproduced failure.
ORACLE_PENDING != red.
Prototype green != product green.
SDK architecture green != Unity/game journey qualification.
Unknown denominator rows remain unknown until classified semantically.
