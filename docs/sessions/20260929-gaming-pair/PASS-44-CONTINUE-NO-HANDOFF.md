# Pass 44 — execution continues beyond handoff threshold

Date 2026-09-30. Exactly Dino + Civis.

User clarified that handoff occurs only when this chat reaches its context limit. Prior "freeze/handoff" language is corrected: exact candidates remain immutable evidence baselines, but new falsification evidence creates successor candidates and work continues in-session.

## Civis

Source trace proved a new production defect candidate: `CivSaveBundle::load_dir` replaces `sim.state` and explicitly mirrors many WorldState fields, but does not resynchronize public `sim.current_tick`; `phase_belief` directly reads that field. A save at tick N can therefore restore canonical state.tick=N while leaving a divergent live mirror until normal ticking resynchronizes it.

Successor vNext candidate:
- semantic apply now requires semantic tick == loaded world tick;
- then explicitly sets `sim.current_tick = semantic.tick`;
- new controls reproduce production loader divergence, require vNext equality, and reject a semantic component whose tick does not match world_state.

Candidate head `02bd7d5b2becf1e0eba36359b50f4a0167a3f683` pending exact workflow qualification. Historical 17/17 green for `1d6a3182...` remains valid for its older scope and is not rewritten.

## Dino

Spec commit `f3383b82ac33c9c99cb7f2fa3704dd6aee661f84` deepens generation reachability:
- WarfareContentLoader retains eight registries but constructor search found only tests, so it is not admitted as a mounted runtime surface.
- Projectiles have real runtime materialization: ModPlatform enumerates projectile definitions and mutates static BlasterBoltConfig colors; stale-removal/reconcile semantics are therefore required.
- Doctrine domain consumers exist, but live mount remains unresolved.
- Weapons/Squads have loader/domain surfaces but live consumer unresolved.
- Skills advertise ECS mapping, but first search found no production ContentRegistrationService skills case or live mapper; implementation realization is unproven.

No third product.
