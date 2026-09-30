# Pass 44 — executable mirror continuity + deeper Dino mountedness

Date 2026-09-30. Exactly Dino + Civis remain active. No handoff; work continues in-session.

## Civis

Source tracing proved a new persistence defect candidate beyond the prior nine controls:
- CivSaveBundle::load_dir restores `sim.state` from world_state.json and explicitly mirrors many persisted fields back to live Simulation;
- it does not resynchronize `sim.current_tick`;
- Simulation::tick normally sets `current_tick = state.tick`;
- engine integration tests and phase code establish current_tick as live runtime state, including direct phase consumers.

vNext candidate now has two new controls:
1. default production loader after saving at tick7 must demonstrate `state.tick=7` while `current_tick != state.tick`;
2. SemanticBundleBridge must restore both to7.

A mixed semantic component with tick6 over world tick5 must also be rejected rather than silently overwriting one identity with the other.

Candidate commits5d3885d17808939fa1d427623d24fe70fa1df5ed / d3a8b10627ebce24ab0835caba0045be8e474125; workflow head ad0db26028f0572c5565cf4e734d9bf4c4245fa6 run36770479281 queued. Previous17/17 evidence remains valid only for candidate1d6a3182... and is not transferred.

## Dino

Deeper source tracing on the frozen revision corrects the shallow "no .Get consumer" result:
- Projectiles are production-mounted through ModPlatform -> BlasterBoltConfig, a materialized/static secondary owner.
- WarfareContentLoader retains eight warfare registries but exact constructor search finds it only in tests; it is implemented domain machinery, not a recovered production-mounted consumer.
- DoctrineEngine/BalanceCalculator are implemented/tested domain machinery, but mounted gameplay consumption remains unproven.
- Weapons and Squads are supported declarative/domain surfaces with live realization open.
- Skills are a stronger realization-gap candidate: RegistryManager + model/schema claim ECS mapping, but first pass found no mounted ingestion/materializer.
- Existing PASS-44-RUNTIME-CONSUMERS-2.md on Dino spec branch already contains and corrects this mountedness distinction; it is preserved rather than overwritten.

This materially supports the mature universal-modding question: tested DTO/registry/domain code does not establish that a mod can change the actual host game.

No third product.
