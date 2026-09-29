# Pass 12 — runner status and hot-reload surface

Date 2026-09-29.

## Dino

Recovery candidate: `8cfc998678d14bca3329083efa93f741aa5c7f5e`.
Recovery run: `36628553200`, in progress at capture.

The isolated oracle project now deliberately uses assembly identity `DINOForge.Tests` because SDK internals are already friend-exposed to that assembly. This does not widen production API visibility.

The hot-reload surface is source-confirmed:
- `IPackReloadService` is internal;
- `ContentLoader` implements it explicitly;
- `IPackReloadService.ReloadPack(packDirectory)` simply returns `LoadPack(packDirectory)`.

Therefore the reload-generation oracle is testing the actual watcher-facing reload path, not a synthetic alternate implementation. The mature contract question remains whether `LoadPack` is allowed to append into persistent registries or must replace the prior generation.

## Civis

Recovery candidate: `eb74d0724163f9958e93c16c4deeb18344882246`.
Recovery run: `36628556544`, queued at capture.

Both orphan-mod identity assertions now use the current `manifest.meta.id` API. No semantic persistence result is inferred until compile and execution steps complete.
