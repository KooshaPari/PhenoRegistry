# Pass 43 — first denominator closure after handoff

Date 2026-09-30. Exactly Dino + Civis remain active. Frozen implementation candidates are unchanged.

## Civis

Spec commit `dfc9a54daef09764d26255e411568c56be2206d4` resolves the first P0 durable-state rows more precisely:

- `current_tick`: mirror of `state.tick`, but source search found no explicit load-side resynchronization after state replacement; candidate restore-gap oracle required.
- `next_civilian_id`: monotonic birth allocator with explicit no-reuse intent; persist or formally rebuild from authoritative IDs.
- `pending_damage`: boundary-sensitive queue; military appends, tactics drains, replay can reconstruct; save-boundary semantics determine durability.
- `economy_state`: budget/tick are partially derived from WorldState, but ledger semantics require separate authority.
- `settlement_food_stocked`: strong durable-canonical candidate because it mutates across trade and affects future mood/market.
- `settlement_housing_capacity` / `settlement_crime_pressure`: durable-or-external-binding decisions; silent empty/default restore is not accepted.
- allocator family split: Simulation's building allocator is distinct from civ_economy's stateful order allocator.

STATE-MANIFEST-v0.json updated at `a4eaba00331c91cf9acea8446d62e876add9b9a0`; no denominator count changed, only row semantics.

## Dino

Spec commit `c0cf7c4311408be37096ac7e11d8dc0b735cb9c4` extends the generation denominator:
- Factions have a second materialized runtime owner in FactionSystem, so RegistryManager.Factions alone cannot ACK the domain.
- Buildings have mixed consumers: BuildMenu/Aerial materialization plus economy ProductionCalculator lookup.
- exact first-pass searches found no direct .Get consumers for Weapons/Projectiles/Doctrines/Skills/Squads; these remain UNKNOWN, not generation-independent or covered.

A global `fullyObserved=true` must eventually be backed by domain-consumer evidence for every supported surface, or an explicit declarative-only/orphan/generation-independent classification.

No implementation candidate changed; no third product started.
