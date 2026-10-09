# Pass 44 — continued execution, not handoff stop

Date 2026-09-30. Exactly Dino + Civis remain active.

Program behavior correction: developer-handoff readiness is not a stopping boundary. Work continues in this chat until context limits require continuity handoff.

## Civis

Source tracing found a live-state authority gap candidate: CivSaveBundle::load_dir replaces sim.state from world_state and explicitly mirrors many persisted fields back to Simulation, but does not explicitly rebind sim.current_tick. Simulation::tick normally enforces current_tick=state.tick and culture/belief phases read current_tick directly.

vNext candidate now explicitly sets loaded.current_tick=loaded.state.tick after semantic application and adds a save/load test requiring equality before post-load phases. New candidate3b53de0176da99a83bb73aad2808cf5d29e2338c run36764426589 queued. Prior green candidate1d6a3182... remains immutable historical evidence.

This is not yet a reproduced production red: replay reconstruction may coincidentally leave the same tick. The defect class is authority ambiguity / missing explicit restore invariant until a discriminating fixture proves divergence.

## Dino

Deeper domain tracing:
- Projectiles have a production-mounted secondary materialization: ModPlatform enumerates RegistryManager.Projectiles and writes bolt colors into BlasterBoltConfig; generation removal/replacement must reconcile this global state.
- Weapons/Squads/Doctrines have substantial implemented domain machinery but mounted gameplay realization remains unproven.
- Skills are advertised as typed registry + DINO Components.Skills ECS mapping, but no mounted ingestion/materializer was found.
- Crucially, WarfareContentLoader constructor search finds only tests; repository orphan analysis records WarfarePlugin prod_refs=0. These are implemented but apparently unmounted domain machinery, not runtime consumer evidence.

Dino spec correction commit6066b43d8a10ad75bd61b0e33c32c7ace0229639. This strengthens the product-husk finding: broad tested domain code does not establish an author-to-host modding journey.

No third product.
