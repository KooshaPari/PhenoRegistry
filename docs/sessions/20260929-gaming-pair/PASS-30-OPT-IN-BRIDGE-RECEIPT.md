# Pass 30 — opt-in bridge and receipt identity advance

Date 2026-09-30. Exactly Dino + Civis.

## Dino PR491

Pure production-shaped GenerationStore is admitted green on candidate e267db309f4ca0cbc3bdef41d93741afa60a48d9, run36715187076:4/4, artifact11096300343 sha256 b43844c7314a57c7bb76b9ec99c047450b0ad6f63d93c4bf50b4be7c38ff2c6f.

Materialized BuildMenu/Aerial source adapters now fail closed as RESTART_REQUIRED; host proof remains mandatory.

ReloadResult protocol on experiment branch now has backward-compatible optional identity fields:
requestedPath, resolvedPath, desiredGeneration, activeGeneration, fullyObserved, activationDisposition. This does not fix runtime path handling yet; it creates a receipt schema capable of representing the truth once handler/GenerationStore integration exists.

Quality/receipt requalification run36716275644 queued.

## Civis PR1569

Implementation candidate now includes an opt-in SemanticBundleBridge layered over unchanged CivSaveBundle:
- save_opt_in writes existing bundle + required semantic-state component;
- load_opt_in requires/validates semantic component;
- caller supplies a resolved mod environment;
- compatibility check occurs before semantic state application;
- default CivSaveBundle load remains available for comparison.

Tests explicitly require:
- opt-in bridge turns reproduced economy-policy/research loss green;
- default loader still loads a bundle without semantic-state;
- opt-in bridge refuses that same bundle rather than silently downgrading.

This is migration scaffolding, not final vNext transactionality. Experiment run36716259872 queued.

No third product, no default-path replacement, no merge authorization.
