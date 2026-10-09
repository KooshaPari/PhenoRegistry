# Melosviz SOTA / bootstrap gate — pass 6 update

Research date: 2026-09-29. Internal frozen subject: `KooshaPari/Melosviz@1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`. This update changes bootstrap decisions; it does not accept a product architecture.

## Editorial timeline / interchange

**OpenTimelineIO (OTIO)**: official release `v0.18.1` (2025-11-09; wheel-fix release after 0.18.0). The project describes itself as an API/interchange format for editorial cut information: order/length of cuts and references to external media, explicitly not a media container. Current core source identifies Apache-2.0 licensing; current releases after 0.16 separate many legacy adapters into independently installed plugins. The project remains active in 2026.

**Decision: INTEGRATE as an editorial projection/interchange candidate, not canonical Melosviz product truth.** Do not hand-roll a generic EDL/timeline interchange layer unless a concrete accepted semantic cannot round-trip through OTIO. Melosviz-specific project/scene revision, musical intent, accepted overrides, renderer provenance and evidence identity remain outside OTIO and should reference it rather than be encoded by abusing generic metadata.

Required spike before freeze: three-scene R1/R2 sequence with rational time, transitions, media references and stable Melosviz scene IDs → OTIO → round-trip → second adapter/serialized form. Prove frame/time mapping and identify every lossy field. Adapter versions must be separately pinned because adapter packaging is not the same lifecycle as OTIO core.

Sources: https://github.com/AcademySoftwareFoundation/OpenTimelineIO/releases ; https://github.com/AcademySoftwareFoundation/OpenTimelineIO ; https://github.com/AcademySoftwareFoundation/OpenTimelineIO/blob/main/setup.py .

## Spatial / hybrid-scene composition

**OpenUSD 26.08**: current documentation describes composition/assembly of assets into scenes/shots/worlds, non-destructive overrides and references/variants. This is relevant to Melosviz's photo/mesh/splat/performer/hybrid projection problem. Licensing correction: current OpenUSD source is released under the **Tomorrow Open Source Technology License 1.0 (TOST 1.0)**, which differs from Apache-2.0 in Section 6 trademarks; do not record it as plain Apache-2.0.

**Decision: ADAPT/COMPOSE only as an optional scene projection until a fidelity spike earns the dependency.** USD is not automatically the canonical product ontology and does not by itself model scanner/music/evidence semantics. Avoid introducing it on the CVP spine merely because it is a mature scenegraph.

Required spike: one hybrid scanner scene with two representations, camera transform, material/visibility override, external asset reference and R2 GUI override → USD layer/reference/variant projection → round-trip. Measure lost semantics, package/runtime cost and actual DCC interoperability. If the projection is lossy or too heavy, keep a smaller canonical scene model and export USD at the boundary.

Sources: https://openusd.org/release/ ; https://openusd.org/dev/tut_referencing_layers.html (tutorial tested with USD 26.08); https://github.com/PixarAnimationStudios/OpenUSD/blob/dev/LICENSE.txt .

## Generative runtime

**ComfyUI** upstream is now `Comfy-Org/ComfyUI`; master observed at `9d80841aa1990305cc7a280c5ea505f317efcc2d` on 2026-09-29. `pyproject.toml` reports version `0.38.0`, Python >=3.10. Root LICENSE is GPLv3. Current `server.py` exposes a prompt queue/job model, WebSocket server, job status/cancel imports and its own loopback/origin security middleware.

**Decision: INTEGRATE as an external renderer runtime over its API/process boundary; do not make ComfyUI's queue/history the Melosviz product-state or acceptance store.** Pin ComfyUI revision/version plus workflow JSON, custom nodes, models and relevant runtime settings into each render receipt. GPLv3 makes an external-process/API boundary especially preferable unless a future distribution/legal review deliberately chooses tighter incorporation.

Melosviz's bridge loopback bug should learn from current ComfyUI's `is_loopback`: it parses IP literals and resolves hostnames, rejecting a resolved non-loopback address rather than treating arbitrary strings as loopback.

Sources inspected through upstream GitHub: `Comfy-Org/ComfyUI@9d80841aa1990305cc7a280c5ea505f317efcc2d`; LICENSE blob `f288702d2fa16d3cdf0035b15a9fcbc552cd88e7`; `server.py` blob `de0076a761db98a683c1ab1746f9c5914d1a8b52`; `pyproject.toml` version 0.38.0.

## Music-video generation/editing prior art

- **AutoMV (arXiv:2512.12196)** already covers automatic full-song music-video generation with music analysis, screenwriter/director agents, shared character state, generation and a verifier. Its paper evaluates 30 curated professional YouTube songs across four languages and explicitly reports that automatic multimodal judges still lag expert humans. Generic 'multi-agent full-song MV generation + verifier' is not differentiation.
- **MVAA / Let Your Video Listen to Your Music! (arXiv:2506.18881)** tackles automatic editing of existing video to a music track: beat-aligned motion keyframes followed by rhythm-aware video inpainting. Its task differs from Melosviz's structured multi-tool creation pipeline, but it directly contests custom beat-alignment/editing machinery and is a useful synchronization baseline.
- **MusicInfuser (arXiv:2503.14505)** adapts existing video diffusion with lightweight music-video cross-attention + LoRA for music-synchronized dance generation and proposes Video-LLM quality evaluation. It is a renderer/model prior, not a durable editable-production architecture.

**Decision consequence:** Melosviz's thesis must stay above any one generation model. Keep renderer/model backends replaceable; differentiation, if it survives, is structured music/editorial intent + hybrid scene projections + operator revision/recovery + exact provenance/evidence across heterogeneous tools. Evaluate beat/sync and creative quality separately; do not inherit a paper's automatic judge as the acceptance authority.

Sources: https://arxiv.org/abs/2512.12196 ; https://arxiv.org/abs/2506.18881 ; https://arxiv.org/abs/2503.14505 .

## Updated custom-build burden

| Capability | Pass-6 direction | What must be proven before custom work |
|---|---|---|
| Editorial timeline/interchange | INTEGRATE OTIO projection | lossless-enough round-trip of accepted scene identity/timing; adapter availability/version |
| Hybrid spatial projection | EXPERIMENT OpenUSD projection | scanner/representation/override fidelity plus dependency/license/operational cost |
| ComfyUI render queue | INTEGRATE external runtime | job/cancel/recovery behavior and exact config identity; never product acceptance truth |
| Durable Melosviz project/job/evidence | BUILD MINIMAL DOMAIN SPINE unless existing durable executor materially reduces burden | restart/replay/idempotency experiment; avoid distributed-workflow platform by default |
| Beat-alignment/editing | LEARN FROM / benchmark MVAA and MIR primitives | annotated-track accuracy and editorial timing, separate from generative motion sync |
| Creative renderer/model | INTEGRATE replaceable backend | held-out creative evaluation; model provenance and rights |
| Automated creative judge | AUXILIARY only | calibration to human raters, disagreement reporting, never average away deterministic correctness |
| Generic media probing/decode | USE FFprobe/FFmpeg | candidate-bound identity and expected stream/timebase checks around the primitive |

## What is still open

Exact MIR library choice/benchmark; durable local-execution alternatives (small SQLite/job log versus Temporal/Prefect-class systems); color-management/audio-delivery standards; commercial-tool automation/licensing; model/custom-node licenses; OTIO/USD fidelity spikes; independent creative-evaluator calibration. No custom subsystem is approved merely by this document.
