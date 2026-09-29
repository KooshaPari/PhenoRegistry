# Melosviz SOTA / existence / bootstrap gate — pass 1

Research retrieved 2026-09-29 against internal source 1aec20a2ba41a01ed557d1c7f63f9a0089f842cf. Status: OPEN. This is a scoped first pass, not a claim to have surveyed the entire 2026 field.

## Constituent problems and direct sources

| Primitive / source | What inspection establishes | Version and limitation | Initial disposition |
|---|---|---|---|
| OpenTimelineIO — https://opentimelineio.readthedocs.io/en/latest/ | Editorial clips, timing, tracks, transitions, markers, metadata and external media references; adapter/plugin model | Page labels 0.19.0.dev1, not a selected stable runtime; adapter fidelity untested | INTEGRATE editorial projection/interchange, not a new generic EDL |
| OpenUSD — https://openusd.org/release/intro.html | Scene composition, layering and overrides across assets | Documentation 26.08; does not establish lossless music/scanner/GUI semantics for our adapters | ADAPT/COMPOSE a hybrid-scene projection; experiment before making it canonical |
| ComfyUI — https://docs.comfy.org/development/comfyui-server/comms_routes | Prompt submission, queue/history, object information and websocket-facing runtime routes | Mutable docs, deployed source and custom nodes/models unpinned; history is not an independent acceptance store | INTEGRATE renderer runtime, persist external job identity and immutable local receipts |
| FFprobe — https://ffmpeg.org/ffprobe.html | Stream/frame inspection and frame counting are available | Mutable docs; probe result alone does not verify intended audio/scene identity or perceptual quality | USE DIRECTLY with decoding and subject-bound checks; reject existence-only media acceptance |
| TouchDesigner Python — https://derivative.ca/UserGuide/Python | Official scripting documentation located | Detailed API/host/headless/license behavior not qualified | Investigate existing live/hybrid workflow rather than hand-roll a full DCC |
| AutoMV / AgentMV | Direct music-video system prior art; see separate academic matrix | Study-specific and abstract-only limitations respectively | LEARN FROM; evaluate as product-absent alternatives before claiming differentiation |

Blender command-line/API documentation fetch attempts failed in this session. Existing repository Blender/C4D/Unreal/Adobe/Resolve adapters are source leads, not independently qualified integrations. Commercial license terms, automation rights and production host requirements remain unverified; no paid service calls were made.

## Strong product-absent alternatives

For the studio horizon: a human director combines an existing audio-analysis/annotation tool, ComfyUI generation workflows, an established DCC or editor for refinement, OpenTimelineIO where interoperable, and FFmpeg-based inspection/assembly. Add AutoMV/AgentMV as automated orchestration comparisons after reproducibility review. Compare against this usable composition, not isolated text-to-video generation. Exact audio-analysis and editing components still require qualification, so the stack is a serious candidate—not a completed existence gate.

For hybrid/live scenes: an existing scripted live/DCC workflow with explicit music cues, external media and scene descriptions is the baseline. The narrow question is whether Melosviz materially improves canonical edit round-trip, timing, portability and recovery—not whether existing tools can render visuals at all.

## Differentiation ledger

COMMODITY / CONTESTED: timeline and media composition, node-graph rendering, basic beat-reactive graphics, multi-agent video planning, tool adapters and ordinary prompt-to-video. FALSIFIED AS UNIQUE: generic multi-agent music-video generation. CANDIDATE: retained structured intent across script/GUI edits; exact audio/timebase constraints through heterogeneous tools; hybrid spatial scene semantics; independently qualified deliverables and recovery. UNVERIFIED: lower intervention/cost, higher creative quality, reliable character continuity, guaranteed synchronization or greater operator productivity than the best stack.

## Build/bootstrap decisions (proposed, not frozen)

| Capability | Preferred research direction | Witness required before custom build |
|---|---|---|
| Editorial timeline | OTIO plus a small product-specific intent model | Round-trip two edited shots, rational timing and media references without lost meaning |
| Hybrid asset / scene composition | USD or existing DCC representations as projections | Scanner/occlusion/material transition and GUI override survive export/import; document any lossy fields |
| Generative runtime | Existing ComfyUI/tool APIs | Stable workflow/node/model pins, job identity, failures, cancellation and resumption |
| Audio analysis | Compare mature MIR primitives and manual annotation before bespoke analyzer | Relevant tracks, annotated beats/sections, estimator uncertainty and measured synchronization—not JSON shape parity |
| Orchestration | Thin durable project/job/receipt model over existing tools | Same-backend multi-scene accounting, restart, invalidation and independent validation outperform simpler scripts |
| Media acceptance | ffprobe + decode + content/contract checks | Malformed, stale, wrong-audio and wrong-scene fixtures cannot yield acceptance |
| Creative judging | Human rubric plus calibrated automated critique | Held-out tracks, inter-rater agreement and evaluator bias; critical correctness cannot be averaged away |

Every custom subsystem needs an accepted unmet obligation and evidence that USE/INTEGRATE/FORK/ADAPT/COMPOSE alternatives are insufficient. Reproducibility requires tool/model/workflow/input/environment identities; a source checkout and seed alone are not accepted guarantees.

Remaining research: exact licenses/releases/health, storage and durable execution alternatives, workflow security, live clock standards, color/audio/delivery standards, commercial competitors, academic dataset/evaluator details, integration cost and high-risk prototypes. SOTA/design gate precedes the later comparative pilot; neither is complete.
