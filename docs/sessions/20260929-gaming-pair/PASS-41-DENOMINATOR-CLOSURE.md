# Pass 41 — post-handoff denominator closure

Date 2026-09-30. Exactly Dino + Civis. Implementation candidates remain frozen.

Dino spec commit5ce0e913122e1d86320b5389f721591941de6d6d establishes a generation denominator: ten core RegistryManager domains (Units, Buildings, Factions, Weapons, Projectiles, Doctrines, Skills, Waves, Squads, FactionPatches), known runtime consumer classes, and required classification of non-core generation surfaces such as patch cache/assets/overrides/dependency/disabled-pack state. Unknown domain/consumer cannot participate in a fully-active G2 receipt.

Civis spec commit932288d88d23d323d98492a924421f2f7d9eb6aa defines terminal semantic dispositions for the existing125 Simulation /48 WorldState denominator and prioritizes future-state drivers, reproduced losses, emergence causal state, substrate, then last_tick families. UNKNOWN/SEMANTIC_DECISION/EPHEMERAL_CANDIDATE/etc remain non-terminal. Durable-domain oracle now requires post-restart consequence continuity, not round-trip equality alone.

Both developer handoffs remain active. Neither denominator is closed; no completion percentage assigned. No third product.
