# Pass 16-18 — expanded counterexamples, consumer semantics and catalog authority

Date2026-09-30. Exactly Dino + Civis.

## Dino

Reproduced controls remain:
- stale removed content;
- identical reload conflict accumulation;
- stale patched YAML after patch removal.

Fresh-generation architecture experiment first combined run executed6 tests: all3 production red controls failed as expected; 2/3 prototype tests passed. The failed prototype was the patch fixture, which did not exactly match the repository's patch-only integration fixture. It has now been aligned to the canonical PatchApplicatorIntegrationTests shape and rerun is active. This is prototype-fixture repair, not production repair.

Runtime-consumer tracing now shows generation publication must handle:
- PackUnitSpawner: lookup-on-demand for future spawns;
- WaveInjector: materializes WaveDefinition into active waves, so active G1 waves can legitimately outlive G2;
- FactionSystem: one-time materialized static dictionary and skips re-initialization; naive rebuild risks losing mutable runtime state;
- AerialSpawnSystem: one-shot building sweep, currently feature-gated off;
- BuildMenu/stat/assets/domain consumers: further classification required.

Therefore a stable RegistryManager facade/generation view plus per-consumer observed-generation disposition is favored over swapping manager references.

## Civis

Added two new semantic persistence counterexamples:
- high-level control policy kind (`Box<dyn Policy>`) distinct from economy PolicyInput;
- market_state prices exposed to clients/future economy.

The test-only semantic manifest prototype now covers:
- economy PolicyInput;
- control-policy kind;
- ResearchCache;
- market prices;
- active mod id/version/API identity;
- orphan guest-memory detection.

This is still deliberately narrower than the full authoritative-state denominator.

Current main drift to590fad06 is docs-only (+ one 339-line audit). The audit independently demonstrates catalog corruption modes: synthetic155-ID emergence range, dead substrate counted as implementation, docs-only scanner blind spots, namespace collisions and unresolved authority for root FUNCTIONAL_REQUIREMENTS.md/design catalogs/civlab run-management surface. Those catalogs are quarantined from mature grading pending authority recovery.

## User-intent archaeology

Recovered prior user anchors were persisted product-locally:
- Dino framework-first/full DINO modding, agent-driven real-game validation, reusable/adapted assets with provenance.
- Civis broad coupled politics/economics/war + hybrid macro/detail simulation. Older assistant deterministic replay proposal is superseded by May no-global-replay charter.

## No completion claim

Architecture prototypes are evidence about possible spines, not product fixes. Source denominators, SOTA, host/user journeys, catalog authority and independent review remain open.
