# phenoDesign — Creativity / Design / UX Spine Boundary

**Status**: `LIVE` / `DECLARE_SPINE` (2026-07-20)  
**Source**: `github.com/KooshaPari/phenoDesign`  
**Spine role**: `CREATIVITY_DESIGN_UX` (see `docs/spine/SPINE-DEFINITION.md`)  
**Peer repo**: `github.com/KooshaPari/asset-engine` (asset pipeline; formerly `engine/`)

## Description

phenoDesign is the **canonical spine** for creativity, art, design, and UX across the Phenotype ecosystem. It owns:

- Design tokens (`@phenotype/design`, W3C DTCG format)
- CSS keycap palette and VitePress theme integration
- Component patterns and style-guide documentation
- UX conventions consumed by frontend repos (phenoAI, phenoData, phenotype-landing, heliosApp)

## In scope

| Slice | Location | Notes |
|-------|----------|-------|
| Design tokens | package root / `tokens/` | Published as `@phenotype/design` |
| VitePress theme | theme integration files | Consumed by phenodocs and fleet docsites |
| UX / art direction docs | `docs/` | Spine-level conventions |
| Brand consistency hooks | token generators, CSS | Teal/midnight palette SSOT |

## Out of scope (owned elsewhere)

| Slice | Owner | Notes |
|-------|-------|-------|
| Asset render pipeline | **`asset-engine`** | Blender/FFmpeg/ImageMagick/Unreal legs |
| Docs site hosting | `phenodocs` | May consume tokens; does not own design spine |
| Graphics SDK (voxel/terrain) | `phenotype-gfx` | 3D substrate, not design tokens |

## Absorption reversal (2026-07-20)

A 2026-07-17 absorption copied token files into `phenodocs/packages/design/` and archived the source repo. That absorption is **reversed**:

- phenoDesign restored as LIVE spine (GitHub unarchived 2026-07-20)
- Registry disposition: `DECLARE_SPINE`, not `ABSORBED`
- phenodocs may mirror tokens as a downstream consumer; phenoDesign remains canonical

## Verification

| Check | Result |
|-------|--------|
| GitHub repo LIVE | unarchived 2026-07-20 |
| CODEOWNERS | `@<REDACTED>` |
| Asset pipeline split | `asset-engine` seeded from `engine/` |
| Registry SSOT updated | `projects/phenoDesign.json`, disposition-index |

## Cleanup

- [x] Absorption reversed in registry SSOT
- [x] GitHub unarchived
- [x] Asset engine extracted to `<REDACTED>/asset-engine`
- [ ] Fleet consumers repoint token deps to phenoDesign canonical (follow-up)
