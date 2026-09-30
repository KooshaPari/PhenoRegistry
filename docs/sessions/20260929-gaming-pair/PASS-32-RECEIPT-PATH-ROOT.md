# Pass 32 — receipt green and path-root cause

Date 2026-09-30. Exactly Dino + Civis.

Dino PR491 candidate1c177fe7125ce4439335be3e0a60c3a9517a50de run36716747784 is green; artifact11095883461 sha2567321072aebdc88fe30e3999bfad7ddb6e7c9f4251338762126af47c519d62a09. Pure integration candidate now qualifies GenerationStore plus ReloadResult path/generation representational fields. Runtime path truth remains open. Root cause is traced end-to-end: client sends path -> handler ignores parameters -> ModPlatform.LoadPacks() -> LoadPacksImpl hardcodes _packsDirectory.Value, despite ContentLoader.LoadPacks(root) supporting explicit roots. Spec commit5d4ca8dd3afc5cee828082f34af3ff4973f6e8ec requires a shared path-aware ModPlatform load entry before GenerationStore/handler integration.

Civis PR1569 exact opt-in bridge candidate run36716733597 remains queued/superseded by newer run36716733597? Latest candidate222dab8e... was queued as run36716733597; newer bridge head now222dab8e plus later code, fresh run36716733597 is not transferred if head differs. Current newest workflow run36716733597/36716259872 must be treated candidate-specifically; no bridge green claimed in this pass.

No third product.
