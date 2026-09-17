# PhenoDesign Scene Experiences v3

Scene-driven experience design for the PhenoDesign ecosystem. This package defines a direction for dynamic, interactive, multidimensional, fourth-wall-aware web experiences resembling a life-size diorama.

**Status:** v3.0 — implementation direction proposed for PhenoDesign.

## What This Is

A set of design documents, ADRs, contracts, evidence, and references that establish:

- **Scene grammar** — how experiences are structured as scenes with purpose, camera, lighting, objects, input, and continuity
- **Design direction** — the north star, governing qualities, and formal requirements
- **Capability matrix** — 30 capabilities across narrative, runtime, art, interaction, 2D, 3D, time, hybrid, quality, evidence, and architecture
- **Media routing** — choosing the right renderer per scene (DOM, SVG, Canvas, Rive, Three.js, video, hybrid, native)
- **Choreography primitives** — 19 compositional tools with dramatic purpose and failure criteria
- **Acceptance and review** — critique rubric, hard gates, performance budgets, and negative cases
- **Repository integration** — how this package fits into the existing PhenoDesign repo structure

## Repository Structure

```
├── docs/
│   ├── adr/                          Architecture Decision Records
│   │   ├── 001-scene-first.md
│   │   ├── 002-one-state-many-renderers.md
│   │   ├── 003-agency-and-rest.md
│   │   ├── 004-no-new-proof-owner.md
│   │   └── 005-consolidate-deliberately.md
│   ├── DESIGN-DIRECTION.md           North star, qualities, requirements (primary)
│   ├── CAPABILITY-MATRIX.md          30 capability rows with ownership and acceptance
│   ├── CHOREOGRAPHY-AND-PRIMITIVES.md Timing, lighting, camera, 19 scene primitives
│   ├── MEDIA-ROUTING.md              Renderer selection matrix and production routes
│   ├── SCENE-GRAMMAR.md              Scene contract, evaluation model, state/time
│   ├── E2E-AND-CROSS-MEDIA.md        Vertical slices and native worker contract
│   ├── REVIEW-AND-ACCEPTANCE.md      Critique rubric, gates, budgets, negative cases
│   ├── REPO-INTEGRATION.md           Ownership map, integration plan, delivery gates
│   └── REFERENCE-STUDY.md            Reference sources and capture protocol
├── contracts/
│   └── experience.schema.json        JSON Schema for authored scene experience documents
├── evidence/
│   └── browser/film-frames/          Browser capture frames (PNG sequence)
└── DOCS-REVIEW.md                    Documentation quality review
```

## Key Documents (Read in Order)

1. **DESIGN-DIRECTION.md** — Start here. Defines the north star, five governing qualities, scene as design unit, reference discipline, 24 formal requirements, and definition of done.
2. **SCENE-GRAMMAR.md** — The scene contract, evaluation model (`frame = evaluate(progress, interactionState, rendition)`), coordinate systems, and journey harness hooks.
3. **CAPABILITY-MATRIX.md** — 30 capabilities (C01–C30) with production source, owner, delivered state, and acceptance criteria.
4. **CHOREOGRAPHY-AND-PRIMITIVES.md** — 19 scene primitives with dramatic purpose, composition input, and failure-to-reject criteria. Timing language and lighting/camera review.
5. **MEDIA-ROUTING.md** — Which renderer to use when. Decision table, production tool ownership, and challenge cards.
6. **REVIEW-AND-ACCEPTANCE.md** — Critique rubric (12 dimensions, 0–4), hard gates, performance budgets, required negative cases.
7. **E2E-AND-CROSS-MEDIA.md** — Vertical slices for vector, raster, spatial, motion, and interactive vector. Remotion integration.
8. **REPO-INTEGRATION.md** — How this fits into PhenoDesign. Ownership map, delivery gates M0–M8.

## ADRs

| ADR | Decision |
|-----|----------|
| 001 | Adopt scene treatment additively; preserve existing design system |
| 002 | One bounded state evaluator; multiple renderers |
| 003 | Meaningful agency required in flagship; rest is valid |
| 004 | Evidence authority stays with existing journey/verifier system |
| 005 | Consolidate by ownership, not folder count |

## Schema

`contracts/experience.schema.json` defines the authored document format (schemaVersion 1.0). Required top-level fields: `schemaVersion`, `id`, `subject`, `task`, `concept`, `assets`, `scenes`, `renditions`, `evidenceOwner`.

Each scene requires: `id`, `purpose`, `range`, `camera`, `lighting`, `objects`, `input`, `semantic`, `continuity`, `fallback`, `acceptance`.

## Integration Boundaries

This package lives at `creative-production/scene-experiences/` inside PhenoDesign. It does not modify Remotion, root package.json, locks, CI, exported APIs, tokens, or AGENTS.md. It is additive.

## References

External references [R01–R13] are documented in REFERENCE-STUDY.md and DESIGN-DIRECTION.md. Sources include Apple iPhone product pages, makemepulse Nomadic Tribe, Nike Reactland, GSAP, Remotion, and others.
