# Pass 44 — session-limit handoff checkpoint

Date 2026-10-03. Exactly Dino + Civis remain active.

This pass exists because the chat reached the user-defined handoff boundary. Fresh-chat continuation must keep exactly these two active products and continue autonomously; developer-handoff readiness is NOT a stopping condition.

## Exact current heads

- Dino spec PR490: 98590128671620e7b10b573fe2abb8f9dde164c4
- Dino impl PR491: 0e83223966cb21c4b7149becf3d8772db0f1a56d
- Civis spec PR1567: 2a25080096202236d727ba0d885a104a10650557
- Civis impl PR1569: c829fc373ab6a020036337a6cbd0f973788a39ef
- PhenoRegistry PR596: 7ee9f976cd57d7efa7f9164b339236b8c83b28da

## Latest Civis exact candidate evidence

Current candidate c829fc373ab6a020036337a6cbd0f973788a39ef run36935760670 completed success:
-23 passed /0 failed /882 filtered;
-artifact11200571611;
-sha256 9e12190fa6b05fb0be8308e4e4eda79ce4ef1261356a55367228d7039cee4285.

This includes multiple current_tick restoration/resynchronization controls, orphan guest-memory compatibility, policy/research restoration, staged generation publication and reconciliation. Therefore the vNext candidate has repaired the source-proven state.tick/current_tick split; update spec machine state in fresh chat.

## Last denominator findings

Civis P0 manifest pass:
- current_tick was source-proven mirror with production load-resync defect; vNext now green.
- next_civilian_id monotonic no-reuse allocator: persist or proved deterministic rebuild.
- pending_damage boundary-sensitive queue.
- economy_state partially derived but ledger authority separate.
- settlement_food_stocked strong durable canonical candidate.
- settlement_housing_capacity/crime_pressure durable-or-external-binding decisions.
- distinguish building allocator from economy/order allocator.

Dino:
- FactionSystem is second materialized faction owner.
- Buildings have mixed BuildMenu/Aerial/ProductionCalculator consumers.
- WarfareContentLoader retains eight typed registries + ArchetypeRegistry; trace lifetime under generation swap.
- ModPlatform materializes ProjectileDefinition.BoltColor into global BlasterBoltConfig: projectile generation consumer.
- DoctrineDefinition feeds DoctrineEngine/BalanceCalculator/WarfarePlugin; trace mounted runtime lifecycle.
- SkillDefinition claims ECS mapping but mounted application is unproven.
- SquadDefinition retained/loaded but gameplay consumer unproven.
- unknown consumer never counts as fullyObserved.

Inactive lineage only: WSM3D, Civic Warfare/Civic Survival, phenotype-gfx. Do not activate third product.
