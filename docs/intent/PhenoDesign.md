# PhenoDesign — Intent

## Intent Statement

PhenoDesign is the **creativity / design / UX spine** for the Phenotype ecosystem. It is the single canonical home for design tokens, component patterns, art direction, and UX conventions consumed by every frontend repo (phenoAI, phenoData, phenotype-landing, heliosApp). Output: a published `@phenotype/design` package, Figma-aligned token library, and fleet-wide UX governance.

The **asset render pipeline** (Blender, FFmpeg, ImageMagick, Unreal) lives in the peer repo [`<REDACTED>/asset-engine`](https://github.com/KooshaPari/asset-engine), extracted from the former `engine/` subtree (2026-07-20).

## Role

| Layer | Role |
|-------|------|
| **Spine** | `CREATIVITY_DESIGN_UX` (see `docs/spine/SPINE-DEFINITION.md`) |
| **Ecosystem map** | `design-system` + spine member |
| **Disposition** | `LIVE` / `DECLARE_SPINE` — absorption into phenodocs reversed 2026-07-20 |

## Boundary

See [`../boundary/PhenoDesign.md`](../boundary/PhenoDesign.md) for the in-scope / out-of-scope declaration.

Asset pipeline boundary: [`../boundary/asset-engine.md`](../boundary/asset-engine.md).

## Curated prompts

See `_bindings.json` key `PhenoDesign` for the bound prompt-hash list
(per-source counts in `docs/registries.md` section 'Capability & Intent SSOT').

## Provenance

- Spine restoration: 2026-07-20 (GitHub unarchived; registry SSOT updated)
- Prior absorption reversed: phenodocs/packages/design/ was a mirror, not canonical
- Source-of-truth role: `phenotype-registry/ECOSYSTEM_MAP.md` + `BOUNDARY_OWNERS.md`
- Refresh cadence: weekly per ADR-024
