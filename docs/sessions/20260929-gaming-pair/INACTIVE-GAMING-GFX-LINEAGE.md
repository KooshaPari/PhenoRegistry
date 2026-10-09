# Gaming / graphics family — inactive lineage and genesis pointers

Date: 2026-09-30.
Authority: USER INTENT + ARCHAEOLOGY POINTERS.
Program rule: **Dino and Civis remain the only active mature-first recovery repositories.**
The entries below do not activate repository #3 or #4.

## WSM / WorldSphereMod / WSM3D

Status: INACTIVE — GENESIS ARCHAEOLOGY REQUIRED BEFORE RECOVERY.

User-intent summary:
- originated from the initial WSM mod/concept;
- goal was to adapt/extend it into a complete 3D and substantially enhanced rendering experience;
- examples explicitly recalled by the user include ray tracing where appropriate, proper LUT/color handling, and broader rendering/graphics enhancement.

Historical pointer:
- prior portfolio archaeology preserved WorldSphereMod as a meaningful hard fork with rendering delta/provenance.
- search aliases independently when activated: WSM, WSM3D, WorldSphereMod, worldsphere, original mod name(s), rendering feature terminology.

Do not infer the final modern architecture yet. In particular, determine how much should live in WSM3D versus shared phenotype-gfx primitives.

## Civic Warfare

Aliases: Civic Warfare; user previously remembered "Civic Strike"; related lineage pointer: Civic Survival.
Status: INACTIVE — GENESIS + FAILED-IMPLEMENTATION ARCHAEOLOGY REQUIRED.

User-intent summary:
- rebuild an inadequate/vibe-built warfare mod attempt into a proper warfare modification for Cities: Skylines;
- broader 2026-08-19 umbrella intent for this family emphasized deep economy, warfare, mechanics, nested supply chains and grand-to-granular play;
- Civic Survival was identified by the user as a warfare basis in that earlier discussion.

When activated, existing code has weak authority merely because it exists. Recover original intent, predecessor mod/fork, failure modes and accepted design before preserving architecture.

## phenotype-gfx

Status: SUPPORT/DEPENDENCY REPOSITORY, NOT AN ACTIVE PRODUCT RECOVERY TARGET.

User-intent summary:
- generalized graphics-library/dependency repository;
- should support both modding and game development;
- shared graphics-specific primitives may live here; genuinely cross-domain primitives may instead belong in PhenoShared.

Boundary hypothesis to falsify later:
- phenotype-gfx: renderer/GPU/material/shader/lighting/post-processing/color/LUT and graphics-extension primitives;
- PhenoShared: generic non-graphics lifecycle/resource/plugin primitives.

Do not promote this boundary hypothesis to accepted architecture without repo/genesis evidence.

## Active-program guard

Current active products remain exactly:
1. DINOForge
2. Civis

WSM3D and Civic Warfare may have lineage/index records only. No source-coverage ledger, SOTA program, requirements decomposition, implementation branch, or recovery PR should begin for them until the active pair passes its program gate or the user explicitly changes the two-repository constraint.
