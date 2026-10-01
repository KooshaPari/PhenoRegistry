# Pass 44B — continued execution beyond handoff threshold

Date 2026-10-01. Exactly Dino + Civis active. Handoff remains reserved for context-limit continuity.

Civis: source tracing proves CivSaveBundle::load_dir restores sim.state and many mirrors but does not resynchronize Simulation.current_tick. Since normal tick assigns current_tick=state.tick and phases read current_tick directly, this is a continuity defect candidate. Experiment adds a nonzero-tick save/load oracle and vNext repair setting current_tick from canonical state.tick. Spec commit4fbbba08ae831915cbc8794b3b0eeaf922e260cd. Exact new experiment head b2a3ffa6c6548bcc31605c3ba078331160dbe4da requires fresh candidate execution; prior17/17 does not transfer.

Dino: deeper consumer archaeology falsifies the simplistic "no .Get hit means unused" interpretation. Spec commit c594c180ca9996ac53da70a41961939aef113541 records:
- WarfareContentLoader retains8 warfare registries but production construction is unproven;
- Projectiles are materially applied by ModPlatform into global BlasterBoltConfig, with cached live material layer still to qualify;
- Doctrine consumers exist, lifetime/mounting unresolved;
- Skills declare ECS mapping but mounted applicator remains unproven;
- Weapons/Squads remain declarative with production runtime effect unproven.
Every mod surface now needs four separate realization states: definition accepted, production mounted, runtime effect proven, generation transition proven.

No third product.
