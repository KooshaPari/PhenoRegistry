# Melosviz editorial/timebase bootstrap — pass 6

Research date: 2026-09-30. Product snapshot: `KooshaPari/Melosviz@1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`.

Status: SOTA/bootstrap research, not an adopted dependency.

## Current product behavior

The mounted composition model stores scene `start`, `end`, `beat_aligned_start`, transition names and total duration as floating seconds inside dicts. `assemble_render_plan` snaps starts to nearest beat, rounds the aligned start to four decimals, validates coverage using float differences, and later media assembly uses separate path lists.

This is workable internal logic, but it combines:
- musical analysis time;
- editorial clip placement;
- render frame time;
- media identity;

without a first-class rational editorial projection.

The candidate product-state spine separately requires stable scene/revision and artifact identities. Time representation should attach to those identities rather than become another source of scene identity.

## OpenTimelineIO prior art

OpenTimelineIO is an Academy Software Foundation project for editorial timeline interchange. Current docs describe:
- Timeline/Track/Clip/Transition/Marker/metadata objects;
- external MediaReferences rather than embedded media;
- `RationalTime(value, rate)` and `TimeRange`;
- clip `source_range` distinct from media `available_range`;
- native `.otio` JSON as lossless for the OTIO model;
- adapters/plugins for AAF, CMX 3600, Final Cut XML and other interchange formats, with explicit warning that non-native adapters may be lossy.

That matches Melosviz's editorial projection unusually well but does **not** model the whole product: music-analysis activations, scanner fields, prompts, character continuity, evidence or acceptance remain Melosviz semantics.

## Bootstrap decision

**ADAPT / INTEGRATE as an editorial projection. Do not make OTIO the entire canonical product model.**

Candidate mapping:

| Melosviz | OTIO projection |
|---|---|
| ProjectRevision | Timeline metadata namespace with immutable Melosviz project/revision IDs |
| ordered SceneRevision | Clip order + Melosviz scene/revision metadata |
| accepted rendered Artifact | ExternalReference / MissingReference before media exists |
| desired scene duration | Clip source/timeline range using RationalTime |
| cut/crossfade | Track order / Transition |
| beat/downbeat/section markers | Marker metadata where useful for editor interchange |
| scene type/backend | namespaced metadata, not OTIO schema identity |
| evidence/acceptance | remains outside OTIO, referenced by IDs/digests in metadata only |

Do not put large evidence blobs or model activations into OTIO metadata. Store references/digests.

## Timebase doctrine

Maintain distinct clocks:
1. source audio sample clock;
2. MIR observation time;
3. editorial rational time/frame rate;
4. renderer/tool-specific timebase;
5. decoded output timestamps.

Conversions must be explicit and evidence-bearing.

For an output rate `fps = p/q`, editorial frame N corresponds to rational time `N*q/p` seconds. Avoid repeated float round-trip as the canonical value. A beat estimated at a floating timestamp remains an observation with uncertainty; snapping it to an editorial frame is a separate authorized/algorithmic decision recorded as such.

The verifier should compare decoded timestamps against the accepted rational projection with an explicit tolerance. This does not mean every beat must land on an integer video frame: the product contract decides whether the cut, effect envelope or visual motion must align and at what tolerance.

## OTIO spike: M-EDIT-01

Construct a 3-scene project using the same fixture as the executable oracle.

1. Create canonical Melosviz project/scene revision objects.
2. Project them to an OTIO Timeline/Track/Clips with RationalTime/TimeRange and namespaced metadata.
3. Serialize `.otio`, read it back, and verify project/scene IDs, order, durations and media references.
4. Reorder S1/S2 in OTIO while keeping IDs; import as an editorial override and produce a new ProjectRevision rather than changing IDs.
5. Replace S2 media reference with a newly accepted R2 artifact; S1/S3 references remain unchanged.
6. Export through at least one non-native adapter only as a lossiness experiment; never assume third-party adapter round-trip is lossless.
7. Verify exact rational frame mapping at 24, 25, 30, 30000/1001 and 60 fps.

Measure integration LOC, schema glue, lost metadata, adapter fidelity and whether custom timeline code becomes smaller/clearer.

## Reject conditions

Do not integrate OTIO if:
- it forces Melosviz intent or evidence into opaque metadata blobs;
- supported Python/runtime packaging materially conflicts with the product;
- required edit round-trips lose stable scene identity;
- a minimal internal rational-time model is demonstrably simpler for the accepted interchange surface.

Do not hand-roll another general EDL/timeline library before this spike fails.

## Sources inspected

- Current OpenTimelineIO documentation, 0.19.0.dev1 pages: overview, adapter system, serialized RationalTime/TimeRange.
- OpenTimelineIO adapter-writing guide: native OTIO representation is lossless for its own model; other adapters vary in fidelity; MediaReference and source_range semantics.
- Melosviz frozen `analysis/models.py` and `compose/assemble.py`.
