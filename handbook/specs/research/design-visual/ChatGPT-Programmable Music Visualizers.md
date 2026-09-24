# Programmable Music Visualizers

**User:** Anonymous  
**Created:** 4/18/2026 15:56:36  
**Updated:** 5/30/2026 16:57:21  
**Exported:** 6/29/2026 18:30:45  
**Link:** [https://chatgpt.com/c/69e40bfa-43a4-83ea-a7dd-119c8868dc58?mweb_fallback=1](https://chatgpt.com/c/69e40bfa-43a4-83ea-a7dd-119c8868dc58?mweb_fallback=1)  

## Prompt:
4/18/2026, 3:56:35 PM

visualizers for music that we can program? e.g. many canvas loops in Spotify and other GFX only music videos are kinda ugly because they are not built with the music 100% in mind in terms of sync, whereas a programmed viz could guarantee this in a sort of procedural gen given input wav?

## Response:
4/18/2026, 3:56:36 PM

Yeah-what you’re noticing is real: most “loop visuals” (like on Spotify Canvas) are **hand-authored animations loosely aligned to the vibe**, not to the actual signal. If you want tight sync, you need to drive visuals **directly from the audio signal** (or a structured representation of it).  

There are a few serious paths depending on how deep you want to go:

---

# 1) Real-time programmable audio-reactive engines
These take raw audio (WAV/stream) → extract features → drive visuals.

## Heavy-duty / pro tools
- TouchDesigner  
  → Probably the best “no compromise” option  
  → Node-based, GPU accelerated, insane control  
  → Can ingest FFT, beat detection, MIDI, etc.

- Notch  
  → Used in concerts / live visuals  
  → Very polished but less open than TD

- Resolume Arena  
  → More performance-focused but scriptable with plugins

👉 These are ideal if you want **visual fidelity + real-time control**, but they’re not “code-first” unless you embed logic.

---

## Code-first real-time stacks
If you want procedural generation fully tied to the waveform:

- **Web stack (fast iteration)**
  - Three.js + WebGL
  - Web Audio API (FFT, time-domain data)
  - Shader-based visuals (GLSL)

- **Creative coding frameworks**
  - Processing
  - openFrameworks
  - p5.js

- **Game engines**
  - Unity (AudioSource + FFT + shaders)
  - Unreal Engine (Niagara + audio analysis)

👉 These give you **full procedural control**, which is what you’re after.

---

# 2) Offline “perfect sync” pipeline (what you actually want)
Real-time is good, but if you want **100% deterministic sync**, don’t do it live.

### Instead:
1. Preprocess the WAV
2. Extract structure:
   - Beat grid (tempo, downbeats)
   - Spectral energy (bass/mids/highs)
   - Onsets/transients
   - Sections (verse/drop/etc.)
3. Generate visuals **from this data timeline**

Tools:
- librosa
- Essentia

Then:
- Feed into shaders / render pipeline
- Render frames offline → encode video

👉 This is how you get:
- exact beat alignment  
- zero drift  
- reproducibility  
- ability to “compose” visuals like music

---

# 3) Shader-first approach (best for modern aesthetic)
Most good visualizers today are basically:

- full-screen fragment shaders
- driven by audio uniforms

Example inputs:
```text
u_bass_energy
u_mid_energy
u_high_energy
u_beat_phase
u_time
```

Then visuals:
- raymarching
- fractals
- fluid sims
- signed distance fields

Stack:
- WebGL / Three.js
- Vulkan / Metal (if native)
- Shadertoy-style pipeline

---

# 4) Beat-perfect synchronization techniques (this is the key)
Most systems fail here. Do this instead:

### A. Beat grid locking
- Detect BPM + beat positions
- Quantize animation cycles to beats

### B. Phase-driven animation
Instead of time:
```text
phase = (current_time % beat_duration) / beat_duration
```

Everything animates on **phase**, not time.

### C. Multi-band mapping
Split audio:
- bass → scale / camera
- mids → deformation
- highs → detail / particles

### D. Event triggers
- kick → pulse
- snare → flash
- hi-hat → micro jitter

---

# 5) Generative choreography (this is where it gets interesting)
Instead of “reactive,” go **compositional**:

- Build a **visual score** from audio analysis
- Define “visual motifs” per section
- Transition based on structure (drop, buildup)

Think:
> audio → symbolic representation → visual compiler

---

# 6) If you want bleeding-edge (your direction)
Given your background, the real play is:

### Build an “audio → latent visual program” system
- Audio → embedding (CLAP / similar)
- Map to visual parameter space
- Generate shader graphs or scene graphs

Or even:
- Diffusion / NeRF conditioned on audio features
- Temporal consistency via latent trajectory

---

# Straight answer to your question
Yes-**fully programmable, perfectly synced visualizers are absolutely doable**, and the reason most existing ones suck is:

- they’re authored, not generated  
- they use amplitude only (not structure)  
- they don’t precompute timing  
- they don’t treat visuals as a function of music  

---

# If you want a concrete starting stack (best balance)
Do this:

- Audio analysis: Python + librosa
- Output: JSON timeline (beats, energy, sections)
- Renderer:
  - Three.js + GLSL shaders (fast)
  - or Unity if you want more scene complexity
- Drive everything from:
  - beat phase
  - spectral bands
  - event triggers

---

If you want, I can:
- design a full architecture (agent-driven, zero HITL compatible)
- give you a repo scaffold (analysis → render → encode)
- or go full deeptech and design a latentMAS-style visual synthesis system tied to audio  

Just pick the direction.

## Prompt:
4/18/2026, 3:57:15 PM

Needs good DX\AX, scripting\API first so I can talk with an Agent but still have heavy GUI backing for review and small manual adjustments

## Response:
4/18/2026, 3:57:18 PM

I’m narrowing this to tools that are actually viable for an agent-first workflow, not just pretty VJ toys. The key filter is: scriptable core, stable automation surface, and a GUI that is useful for inspection rather than mandatory for creation.

> **Thinking longer for a better answer**
>
> 
>
> **Searching for current software with scripting APIs**
>
> [TouchDesigner Documentation](https://docs.derivative.ca/)
> [Everything in Notch 2026.1](https://manual.notch.one/2026.1/en/docs/whats-new/everything/)
> [The Unreal Python API Documentation](https://dev.epicgames.com/community/learning/tutorials/l0Z6/unreal-engine-the-unreal-python-api-documentation)
> [Scriptable audio pipeline](https://docs.unity3d.com/6000.3/Documentation/Manual/audio-scriptable-processors.html)
> [The Great Inversion | Derivative - TouchDesigner](https://derivative.ca/community-post/great-inversion/74207)
> [Product roadmaps](https://unity.com/roadmap/detail)
>
> Thought for 14s

Yes. Given your constraints, I’d rank them like this:

**1. TouchDesigner**
Best fit for **agent-first + GUI-backed review**. It has a mature Python scripting surface, built-in Python examples, support for external Python environments, and the GUI is actually useful for inspecting node graphs, parameters, textures, CHOP signals, and timelines instead of fighting the code path. It also has OSC/TUIO/network operators, which makes it easy to let an agent drive it from outside if you do not want the agent directly editing the project file. ([Derivative](https://docs.derivative.ca/?utm_source=chatgpt.com))

**2. Unreal Engine**
Best if you want a **serious editor, proper scene tooling, sequencer/cinematic control, and strong extensibility**. The weak point for your use case is that it is not as naturally “visualizer-native” as TouchDesigner, but it does give you Python editor scripting, audio tooling, Blueprints, and a heavyweight GUI for review and manual polish. It is better when the visualizer starts becoming a full product or world rather than a pure signal-reactive art pipeline. ([Epic Games Developers](https://dev.epicgames.com/community/learning/tutorials/l0Z6/unreal-engine-the-unreal-python-api-documentation?utm_source=chatgpt.com))

**3. Unity**
Best if you want a **cleaner codebase and easier software engineering discipline** than TD, while still keeping a GUI editor. Unity currently has a scriptable audio pipeline, Timeline, and visual scripting, so it can support an API-first workflow reasonably well. The downside is that, for high-end procedural music viz, it tends to feel more like “a game engine you bent into a visualizer” than a tool built for audiovisual work. ([Unity Documentation](https://docs.unity3d.com/6000.3/Documentation/Manual/audio-scriptable-processors.html?utm_source=chatgpt.com))

**4. Notch**
Strong visually, and it now has JavaScript scripting in current docs and release notes, plus dedicated sound and scripting nodes. But for your exact requirement, I still put it behind TouchDesigner because the ecosystem and mental model are less attractive for an agent-driven software-style workflow. It looks better as a polished show/graphics tool than as the core of an agent-operated programmable viz platform. ([Notch Manual 2026.1 / 1.0](https://manual.notch.one/2026.1/en/docs/whats-new/everything/?utm_source=chatgpt.com))

My blunt take:

- If you want **best DX/AX** for “agent generates systems, you inspect and nudge them,” use **TouchDesigner**.
- If you want **best long-term product engineering**, use **Unreal** or **Unity**.
- If you want **best visual-tool feel** but weaker agent/software ergonomics, use **Notch**.

The architecture I’d recommend is not “put all intelligence inside the GUI tool.” Do this instead:

**Use a split system.**
- **Core brain:** your own repo, code-first, versioned, testable.
- **Renderer/editor:** TouchDesigner or Unreal as the review/manipulation front-end.
- **Bridge:** OSC, WebSocket, REST, shared JSON timelines, or direct Python hooks.
- **Workflow:** agent edits source-of-truth specs/code → bridge updates scene/graph → you review in GUI → minor manual adjustments get exported back into structured data, not trapped in the editor file.

That gives you:
- reproducibility
- agent operability
- GUI review
- manual override without turning the project into mush

For your exact music-viz case, I would build it as:

**Recommended stack**
- **Audio analysis + orchestration:** Python
- **Intermediate format:** beat grid, section map, onset events, spectral bands, motif/state timeline in JSON
- **Renderer:** TouchDesigner
- **Live control path:** OSC/WebSocket
- **Offline render path:** deterministic frame render from the same timeline
- **Manual edits:** parameter overrides saved as structured patches, not hand-only scene tweaks

That avoids the common failure mode where the editor project becomes the only truth and agents become useless.

My actual recommendation:
**Start in TouchDesigner, but keep the logic outside it.** Treat TD as a programmable viewport/runtime/editor, not the brain.

If you want, I’ll map out a concrete repo structure and control protocol for an agent-first TouchDesigner visualizer system.

## Prompt:
4/18/2026, 4:00:22 PM

I have an idea of a 3d scene, lets just say a splat or other advanced sort of a physical image where depth is perceived in someway, whether as a deformed ball where there isn't say  possibility of a "scanner" hitting an object but there's something behind it, or a situation of true 3d splat that does contain such vs the equivalent of 1 radar scan.

The music video would have materials change, e.g. say this environment is a 360 video of a DJ in a club, whole env can change to say mesh, real photo, etc for aesthetic affect, and this supposed scanner (say programmed to a discoball in the scene) would be Abel to similarly "sweep around" in x way, and have a splat area of effect that changes to x material, say real or mesh.  other advanced items, e.g. rotoscoping etc, might be wanted, effectively both for advanced music videos and true gfx gen?

## Response:
4/18/2026, 4:00:24 PM

I’m checking current toolchains that actually support this kind of hybrid scene representation—radiance fields, splats, segmentation/rotoscoping, and programmable material swaps—so I can give you a grounded stack instead of hand-wavy “use a game engine.”

> **Formulating conceptual answer and gathering info**
>
> I need to provide a conceptual explanation, possibly mentioning tools and architecture. Since the user could benefit from updated information after 2025, I’ll search the web to get the latest niche details. Not sure if an image carousel is needed, but I’ll gather factual citations.
>
> **Searching for 2026 Gaussian splatting and multimedia tools**
>
> [Gaussian Splatting | Derivative - TouchDesigner](https://derivative.ca/community-post/asset/gaussian-splatting/69107)
> [3D Gaussian Splatting for Real-Time Radiance Field ...](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
> [Runway | Building AI to Simulate the World](https://runwayml.com/)
> [[Release] SHARP for TouchDesigner: Gaussian Splat from a ...](https://www.youtube.com/watch?v=scedl0UdE6Y)
> [3D Gaussian Splatting for Real-Time Radiance Field ...](https://github.com/graphdeco-inria/gaussian-splatting)
> [3D Gaussian Splatting for Real-Time Radiance Field ...](https://arxiv.org/abs/2308.04079)
> [Runway](https://app.runwayml.com/)
> [Gaussian Splatting options - Pipeline & Plugins](https://forums.unrealengine.com/t/gaussian-splatting-options/1907745)
> [Free Gaussian Splatting Workflow! : r/TouchDesigner](https://www.reddit.com/r/TouchDesigner/comments/1qfh26s/free_gaussian_splatting_workflow/)
> [3DGUT](https://research.nvidia.com/labs/toronto-ai/3DGUT/)
> [Radiance Fields (Gaussian Splatting and NeRFs)](https://radiancefields.com/)
> [Runway AI Review 2026: Features, Pricing & Gen-4 Video ...](https://max-productive.ai/ai-tools/runwayml/)
> [All-In-One Plug-In For Unreal Engine 5 To Gaussian Splatting](https://80.lv/articles/all-in-one-plug-in-for-unreal-engine-5-to-gaussian-splatting)
> [3D Gaussian Splatting for Realistic Physical AI Simulations](https://www.nvidia.com/en-us/on-demand/session/siggraph25-s07/)
> [Runway AI: Free AI Video Generator](https://invideo.io/make/runway-ai/)
> [Introduction to Gaussian Splatting in UNREAL Engine](https://dev.epicgames.com/community/learning/tutorials/V2Y2/realityscan-introduction-to-gaussian-splatting-in-unreal-engine)
> [Real-Time GPU-Accelerated Gaussian Splatting with ...](https://developer.nvidia.com/blog/real-time-gpu-accelerated-gaussian-splatting-with-nvidia-designworks-sample-vk_gaussian_splatting/)
>
> **Searching for rotoscoping and segmentation sources**
>
> I need to include citations throughout my answer. Since the user asked about how a scanner might hit behind objects, I might mention 3DGUT for secondary rays. I’ll also look for official info on rotoscoping and segmentation, checking sources like Adobe or Blackmagic, instead of Runway, for better guidance.
>
> **Searching official sources for rotoscoping and 3DGUT**
>
> [Use Next-Gen Roto Brush 3](https://helpx.adobe.com/after-effects/using/video/roto-brush-refine-matte-video.html)
> [DaVinci Resolve Magic Mask Guide | Effortless Rotoscoping ...](https://www.youtube.com/watch?v=k0pY1jr7oLg)
> [3DGUT](https://research.nvidia.com/labs/toronto-ai/3DGUT/)
> [Python - Derivative - TouchDesigner Documentation](https://docs.derivative.ca/Python)
> [Use rotoscoping to cut moving objects from video](https://www.adobe.com/products/aftereffects/rotoscoping.html)
> [3DGUT: Enabling Distorted Cameras and Secondary Rays ...](https://www.researchgate.net/publication/387141344_3DGUT_Enabling_Distorted_Cameras_and_Secondary_Rays_in_Gaussian_Splatting)
> [Introduction to Python Tutorial | Derivative - TouchDesigner](https://derivative.ca/UserGuide/Introduction_to_Python_Tutorial)
> [Davinci Resolve Studio - Magic Mask initial thoughts](https://www.artstation.com/blogs/jurandm/y1D64/davinci-resolve-studio-magic-mask-initial-thoughts)
> [Magic Mask used to enhance manual rotoscoping](https://forum.blackmagicdesign.com/viewtopic.php?f=33&t=147271)
> [3DGUT: Enabling Distorted Cameras and Secondary Rays in Gaussian Splatting](https://arxiv.org/abs/2412.12507)
> [Using Multipoly (Rotoscoping) with Magic Mask?](https://www.reddit.com/r/davinciresolve/comments/1eiguxy/using_multipoly_rotoscoping_with_magic_mask/)
> [nv-tlabs/3dgrut: Ray tracing and hybrid rasterization of ...](https://github.com/nv-tlabs/3dgrut)
> [Python in TouchDesigner](https://matthewragan.com/teaching-resources/touchdesigner/python-in-touchdesigner/)
> [Insider Tips: Using Roto Brush for Rotoscoping in After ...](https://blog.frame.io/2024/06/12/insider-tips-after-effects-roto-brush/)
> [TouchDesigner Python Cheat Sheet for Developers](https://interactiveimmersive.io/blog/python/python-cheat-sheet-for-touchdesigner-developers/)
>
> Thought for 14s

Yes. What you’re describing is coherent, and it splits into **two materially different classes** of scene representation:

**A. “Single-surface depth illusion”**
A deformed shell, displacement field, depth mesh, or layered billboard setup. It looks 3D from many angles, but it is not truly volumetric in the sense of “a scan ray can pass through one thing and hit another deeper thing.” This is cheaper, easier to art direct, and often enough for stylized music video work.

**B. “True volumetric / radiance-field-like scene”**
A Gaussian splat or related radiance-field representation where the scene is not just one displaced surface. In that world, occlusion and visibility are part of the representation, and newer research has pushed beyond basic rasterized splats into support for distorted cameras and even secondary rays for reflections/refractions. That is much closer to your “scanner hits one thing, maybe something exists behind it” idea. ([Inria Repository](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/?utm_source=chatgpt.com))

That distinction matters because your “discoball scanner sweeping materials across the environment” can be built in either mode, but the implementation changes a lot.

What you want is basically a **hybrid scene graph**:

- a **base scene representation**: 360 capture, photogrammetry mesh, NeRF/3DGS, or layered depth/video
- one or more **material domains**: photo-real, mesh/wireframe, splat cloud, toon/roto, edge map, particleized, etc.
- a **sweep operator**: your discoball/scanner field
- a **masking/transition logic** that decides where the sweep reveals or replaces one domain with another
- an **audio timeline/control layer** so it is musically locked rather than “reactive slop”

That is very doable.

The clean way to think about it is not “the scanner changes the object,” but:

**the scanner writes into a field**  
and that field controls:
- which representation is visible
- how strongly it blends
- whether geometry is reframed as splat, mesh, photo, or roto layer
- what extra effects are emitted at the transition boundary

So your disco-ball scanner is really a moving **volumetric mask generator**.

For example:

- outside the scan cone: photoreal club capture
- inside the cone: Gaussian splat rendering
- near the edge of the cone: mesh/wireframe + chromatic breakup
- on beat hits: transition edge blooms, fragments, or crystallizes
- for vocals: rotoscoped performer pops to a separate material regime
- for drops: the whole room converts from photo to point-cloud or reflective glass-shell

That is the right mental model.

On the “is it real 3D or fake 3D?” question:

For **music videos**, fake 3D is often enough and usually easier to control.  
For **true graphics generation**, camera freedom, occlusion consistency, and deeper lighting tricks push you toward real 3D representations.

Bluntly:

- If you want **reliable production output**, use mesh + depth + segmentation + shader tricks first.
- If you want **novel look / deeper research path**, add Gaussian splats / radiance fields as one of the material domains.
- If you want **scanner logic that meaningfully interacts with hidden/occluded structure**, you eventually want true 3D or a hybrid with true volumetrics.

A good stack for this is:

**Authoring / review / live control:** TouchDesigner  
It is Python-scriptable, has lots of built-in Python examples, and is already used for audio-reactive and Gaussian-splat workflows. ([Derivative](https://docs.derivative.ca/Python?utm_source=chatgpt.com))

**Core logic outside the GUI:**
- Python orchestration
- structured scene/timeline spec
- audio analysis
- transition-field generation
- export of parameter timelines / masks / cues

**Representation layers:**
- photogrammetry mesh or 360/depth-derived shell
- Gaussian splat asset(s)
- optionally performer roto layers
- optional point/particle reinterpretation

**Rotoscoping / subject isolation:**
For the performer or foreground figures, use dedicated roto tools rather than trying to solve that purely inside your viz runtime. Adobe’s current Roto Brush 3 is explicitly built for object selection and tracking over time, including harder edges like hair/transparencies. ([Adobe Help Center](https://helpx.adobe.com/after-effects/using/video/roto-brush-refine-matte-video.html?utm_source=chatgpt.com))

That lets you do stronger things like:
- DJ stays photoreal while room flips to splat
- DJ turns into wireframe only under the scanner
- crowd becomes abstract silhouettes on certain sections
- different subjects receive different material mappings

The most important architectural choice is this:

## Don’t store the creative truth only in the editor project

You want a **spec-first system**:

- `scene spec` = what assets exist and what domains they support
- `audio spec` = beat grid, sections, transients, vocal phrases
- `transition spec` = scanner paths, cones, falloffs, blend curves
- `look spec` = mappings from field values to materials/effects

Then TouchDesigner or Unreal is just the runtime/editor for review and fine nudging.

That gives you the DX/AX you asked for:
- agent can reason over structured specs
- GUI remains strong for inspection
- small manual changes are possible
- changes can round-trip back into structured data instead of dying inside a giant binary project file

Technically, your scanner can be represented as any of these:

- sphere field
- cone field
- swept line or spline field
- rotating lobe field tied to the disco ball
- multi-ray scan bursts
- beat-quantized scan planes

And those fields can drive:
- material replacement
- opacity
- point density
- mesh displacement
- reflectivity
- color palette
- bloom/fog
- particle emission
- local camera distortion

If you want the more advanced version, you can even let the scanner be **semantic**, not just geometric:
- “hit walls first”
- “prefer human silhouettes on vocals”
- “pull reflective materials during high-hat sections”
- “convert only mid-depth geometry during the bridge”

That is where this stops being just a visualizer and becomes a real graphics system.

My recommendation for MVP vs full version:

## MVP
- captured club scene
- mesh/depth proxy or simple splat asset
- discoball-driven sweep mask
- two to three material domains: photo, wireframe/mesh, splat/particles
- one performer roto layer
- beat-locked transitions

## Full version
- hybrid radiance-field + mesh scene
- semantic performer/object masks
- multiple scanner types
- volumetric transition logic
- offline deterministic renders
- procedural camera choreography
- per-section visual motifs and state machine

So yes: this is viable both as **advanced music-video tooling** and as **true graphics generation** infrastructure.

My blunt recommendation:
Start with a **hybrid fake-real pipeline** rather than chasing “perfect volumetric everything” on day one. Use real 3D where it buys you occlusion and camera movement, fake it where it buys you control. Then add splats/radiance fields as a first-class material domain, not as the only scene representation.

If you want, I’ll turn this into a concrete system design with:
- repo layout
- spec schema
- runtime architecture
- TouchDesigner bridge
- asset pipeline for mesh/splat/roto/audio timelines

---

**Sources:**

- [3D Gaussian Splatting for Real-Time Radiance Field ...](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/?utm_source=chatgpt.com)
- [Python - Derivative - TouchDesigner Documentation](https://docs.derivative.ca/Python?utm_source=chatgpt.com)
- [Use Next-Gen Roto Brush 3](https://helpx.adobe.com/after-effects/using/video/roto-brush-refine-matte-video.html?utm_source=chatgpt.com)

## Prompt:
4/18/2026, 4:01:35 PM

yes,

## Response:
4/18/2026, 4:01:37 PM

I’m turning it into a concrete build plan now: source-of-truth specs, asset pipeline, runtime/editor split, and how the scanner/material system should actually be represented so an agent can operate it cleanly.

> **Thinking longer for a better answer**
>
> 
>
> **Browsing for TouchDesigner and After Effects documentation**
>
> [Script CHOP - TouchDesigner Documentation](https://docs.derivative.ca/Script_CHOP)
> [Next Devices, Protocols and Tools to Support in TD](https://forum.derivative.ca/t/next-devices-protocols-and-tools-to-support-in-td/961393)
> [Roto Brush and Refine Matte in After Effects](https://helpx.adobe.com/after-effects/using/roto-brush-refine-matte.html)
> [GLINT: Modeling Scene-Scale Transparency via Gaussian ...](https://arxiv.org/html/2603.26181v1)
> [Point Cloud Surface Deformer .V1 | Derivative - TouchDesigner](https://derivative.ca/community-post/asset/point-cloud-surface-deformer-v1/71841)
>
> Thought for 9s

Here’s the concrete system design.

## Core stance

Do **not** make TouchDesigner the source of truth. Use it as the runtime/editor. TouchDesigner is strongly scriptable with Python, including DAT/CHOP/TOP scripting, event-triggered scripts, and Python-generated images via Script TOP, which makes it a good GUI-backed runtime rather than just a manual-only editor. ([Derivative](https://docs.derivative.ca/Python?utm_source=chatgpt.com))

Your system should be:

**spec-first, agent-operated, GUI-reviewed, offline-renderable, live-capable**

And yes, the scene side should be hybrid. Classic 3D Gaussian Splatting gives you real-time high-fidelity novel views, but newer work also makes clear that plain 3DGS has limitations around transparency and special optics, while recent papers are already extending it toward transparency handling, reflective surfaces, and fisheye input. That matters because your “discoball scanner” concept gets much stronger if the underlying scene is not just a flat texture trick. ([arXiv](https://arxiv.org/html/2603.26181v1?utm_source=chatgpt.com))

---

## Recommended architecture

### 1) Control plane repo
This is the real product.

It owns:
- scene spec
- audio analysis
- transition/scanner definitions
- look presets
- render jobs
- exports to TD
- round-trip overrides from TD

Suggested structure:

```text
musicviz/
  README.md
  pyproject.toml
  src/
    core/
      models/
      timeline/
      scanner/
      materials/
      transitions/
      export/
      ingest/
    audio/
      analyze.py
      beats.py
      sections.py
      stems.py
    scene/
      mesh_pipeline.py
      splat_pipeline.py
      depth_pipeline.py
      masks_pipeline.py
    td_bridge/
      osc_client.py
      websocket_client.py
      tox_export.py
      td_patch_io.py
    render/
      offline.py
      preview.py
      ffmpeg_encode.py
    cli/
      main.py
  specs/
    scenes/
    songs/
    looks/
    shots/
  assets/
    source/
    processed/
    caches/
  td/
    runtime.toe
    components/
    scripts/
  tests/
```

### 2) TouchDesigner runtime project
This contains:
- loaders for processed assets
- live preview comps
- scanner field visualizer
- material-domain mixers
- beat/section monitors
- override controls
- final output nodes

TouchDesigner remains the GUI surface for:
- review
- scrubbing
- node-level debugging
- quick visual adjustments
- performance inspection

Because it supports Python and scripted operators, you can keep the runtime mostly data-driven instead of hand-wired. ([Derivative](https://docs.derivative.ca/Python?utm_source=chatgpt.com))

---

## Representation model

Your scene should support multiple concurrent representations of the same world.

### Scene domains
Each shot/scene can expose some or all of:

- `photo_domain`
  - equirect 360 imagery
  - projected video
  - photogrammetry texture
- `mesh_domain`
  - triangle mesh
  - depth shell
  - wireframe
  - normal/depth views
- `splat_domain`
  - Gaussian splat scene or point-cloud-like proxy
- `performer_domain`
  - DJ/subject mattes
  - roto-isolated subject passes
- `fx_domain`
  - particles
  - edge maps
  - stylized shader reinterpretations

This is the crucial abstraction:
you are not “changing the environment.”
You are switching or blending **representation domains** over regions of space and time.

---

## Scanner model

The disco-ball scanner is a field emitter.

It should not be hardcoded as a visual effect. It should be a first-class object in the spec.

### Scanner schema
```yaml
scanner_id: disco_main
type: rotating_cone
origin:
  anchor: scene.discoball_01
direction_mode: spline_orbit
shape:
  cone_angle_deg: 18
  falloff: smoothstep
  max_distance: 22.0
rotation:
  bpm_locked: true
  beats_per_rotation: 8
  phase_offset: 0.15
noise:
  edge_wobble: 0.08
  beat_pulse_gain: 0.35
occlusion_mode: scene_depth
write_channels:
  - reveal_splat
  - hide_photo
  - boost_wireframe
  - edge_emission
```

### Scanner outputs
A scanner writes into spatial masks such as:
- `reveal_splat`
- `reveal_mesh`
- `reveal_photo`
- `performer_only`
- `edge_energy`
- `reflectivity_boost`
- `particle_spawn`
- `distortion_strength`

This gives agents something clean to reason about.

---

## Material system

Each domain should expose multiple material looks.

### Example material families
For `mesh_domain`:
- clean PBR
- chrome
- glass-like
- wireframe emissive
- contour-only
- voxelized

For `splat_domain`:
- full radiance
- point halo
- density-only
- monochrome cloud
- strobe quantized

For `photo_domain`:
- raw real image
- high-contrast monochrome
- posterized
- edge-extracted
- CRT/compression damaged

Then transitions are just mappings like:

```yaml
when:
  mask: reveal_splat > 0.5
do:
  photo_domain.opacity: 1.0 - reveal_splat
  splat_domain.opacity: reveal_splat
  splat_domain.material: cloud_chrome
  fx_domain.edge_emission: edge_energy * 1.4
```

---

## Audio pipeline

You said you want it synced, not generic slop. So the audio path has to be precomputed, not just live FFT.

### Audio outputs
Generate:
- BPM
- beat timestamps
- downbeats
- bar/phrase positions
- section labels
- onset events
- low/mid/high band envelopes
- transient confidence
- optional stem activity

Then export a canonical timeline JSON.

### Timeline schema
```json
{
  "track_id": "dj_club_cut_01",
  "sample_rate": 48000,
  "duration_sec": 214.3,
  "beats": [0.43, 1.01, 1.60],
  "downbeats": [0.43, 2.76, 5.10],
  "sections": [
    {"name": "intro", "start": 0.0, "end": 24.0},
    {"name": "build", "start": 24.0, "end": 48.0},
    {"name": "drop_1", "start": 48.0, "end": 80.0}
  ],
  "bands": {
    "bass": [[0.00, 0.11], [0.02, 0.10]],
    "mid":  [[0.00, 0.05], [0.02, 0.07]],
    "high": [[0.00, 0.02], [0.02, 0.09]]
  },
  "events": [
    {"t": 48.03, "type": "kick", "strength": 0.94},
    {"t": 48.29, "type": "snare", "strength": 0.82}
  ]
}
```

Then scanner speed, material swaps, and camera moves lock to this timeline.

---

## Asset pipeline

### A) Environment capture options
You likely want to support more than one acquisition mode.

#### Tier 1: easiest
- 360 video
- optional depth estimation
- projected onto sphere or shell

Good for:
- music videos
- fast iteration
- stylized output

Bad for:
- deep parallax
- true occlusion logic

#### Tier 2: practical hybrid
- photogrammetry / mesh reconstruction
- texture projection
- roto subject layers
- depth masks

Good balance for production.

#### Tier 3: advanced
- Gaussian splat or radiance-field style scene
- converted to runtime-friendly assets or custom renderer path

Good for:
- free camera movement
- more convincing reveal effects
- richer space reinterpretation

Recent work shows 3DGS is being extended for harder cases like transparency, reflectance, and fisheye capture, so this path is moving fast rather than being a dead end. ([arXiv](https://arxiv.org/html/2603.26181v1?utm_source=chatgpt.com))

### B) Performer isolation
Do this separately from the scene.

Use roto/object matte tooling to extract:
- DJ
- hands
- crowd silhouettes
- key props

Adobe’s current Next-Gen Roto Brush 3 is explicitly aimed at object selection/tracking through time and is meant to handle harder cases like overlapping limbs, hair, and transparencies; current release notes show After Effects 26.2 in April 2026, so that tooling is current rather than stale. ([Adobe Help Center](https://helpx.adobe.com/after-effects/using/roto-brush-refine-matte.html?utm_source=chatgpt.com))

Export:
- alpha mattes
- clean plates
- ID masks
- optional depth ordering hints

---

## TouchDesigner runtime layout

Inside `runtime.toe`, I’d structure it like this:

```text
/project1
  /io
    osc_in
    ws_in
    file_watch
  /timeline
    audio_clock
    beat_chops
    section_dat
    event_router
  /scene
    mesh_loader
    splat_loader
    photo_loader
    performer_loader
  /fields
    scanner_1
    scanner_2
    global_noise
    mask_composer
  /materials
    photo_materials
    mesh_materials
    splat_materials
    performer_materials
  /mix
    domain_blend
    edge_fx
    particles
    bloom_grade
  /camera
    camera_rig
    shot_controller
  /ui
    review_panel
    overrides_panel
    debug_views
  /output
    preview_out
    render_out
```

### Important rule
Manual GUI changes must be exportable back to structured overrides.

So if you tweak:
- cone angle
- blend curve
- edge glow
- section timing offset
- material preset

those changes should serialize to something like:

```yaml
overrides:
  scanner.disco_main.shape.cone_angle_deg: 21
  looks.drop_1.edge_emission_gain: 1.8
  shots.bridge.camera.path_id: cam_orbit_b
```

Not just remain trapped in the `.toe`.

---

## Agent workflow

### Agent-facing operations
Your agent should be able to issue commands like:

- “Create a new look preset where drop_1 transitions from photo to chrome splat over 4 bars.”
- “Make the scanner orbit twice as fast during high-energy sections.”
- “Isolate the DJ and keep them photoreal while the room becomes wireframe.”
- “Export preview shot 03 from 00:48 to 01:02.”
- “Find all manual overrides that diverge from canonical spec.”

That means you need a real API, not vague editor automation.

### Suggested command surface
CLI:
```bash
viz ingest scene club_scan_01
viz analyze audio track.wav
viz build shot dj_drop_01
viz push td
viz render preview dj_drop_01
viz diff overrides
viz apply overrides overrides.yaml
```

Service API:
- `POST /analyze/audio`
- `POST /build/scene`
- `POST /sync/touchdesigner`
- `POST /render/preview`
- `GET /state/current`
- `GET /diff/manual-overrides`

---

## Live mode vs offline mode

You want both.

### Live mode
- OSC/WebSocket control
- TD preview updates
- lower-res assets if needed
- interactive tweaking

### Offline mode
- deterministic frame rendering
- fixed timeline
- final encode
- no drift
- reproducible outputs

This split is mandatory if you want both music-video quality and runtime playfulness.

---

## Data contracts

Use explicit schemas.

### Main spec files
- `scene.yaml`
- `track_timeline.json`
- `lookbook.yaml`
- `shot_plan.yaml`
- `overrides.yaml`

### Example shot plan
```yaml
shot_id: dj_drop_01
scene: club_scan_01
track: dj_mix_a
time_range:
  start: 48.0
  end: 80.0

camera:
  mode: orbit_target
  target: performer.dj_01
  radius: 4.5

active_scanners:
  - disco_main
  - crowd_sweep

look_states:
  default: photo_club
  on_drop:
    section: drop_1
    apply:
      photo_domain.opacity: 0.2
      splat_domain.opacity: 0.8
      mesh_domain.wireframe_boost: 0.4

performer_rules:
  performer.dj_01:
    preserve_domain: photo_domain
    edge_glow: 0.35
```

---

## Research-forward extensions

Once the MVP works, add these:

### Semantic scanner
Scanner prefers:
- humans on vocals
- reflective surfaces on hats/highs
- architecture on bass
- signage on snare hits

### Multipass field logic
Different scanner lobes write different channels:
- lobe A reveals splats
- lobe B reveals mesh
- lobe C only affects performer matte edges

### Reflection/refraction-aware domains
Recent 3DGS-related work is explicitly targeting transparency and reflective surfaces, which lines up with your disco-ball/chrome/glass ideas. ([arXiv](https://arxiv.org/html/2603.26181v1?utm_source=chatgpt.com))

### Fisheye / 360-native capture
There is current work on enabling fisheye input in Gaussian-splatting pipelines, which is directly relevant if you want to build from club 360 or immersive capture instead of plain narrow-FOV footage. ([arXiv](https://arxiv.org/html/2604.00648v1?utm_source=chatgpt.com))

---

## What I’d build first

### Phase 1: MVP
- one club scene
- one track
- one scanner
- 3 domains: photo / mesh / splat-like proxy
- one performer matte
- beat-locked timeline
- TD preview + exportable overrides

### Phase 2: production
- full shot planner
- multiple scanners
- real splat assets
- per-section lookbooks
- offline render pipeline
- better subject segmentation

### Phase 3: advanced
- semantic scanner
- multi-actor rules
- transparency/reflection-aware scenes
- procedural camera intelligence
- automatic motif generation from audio structure

---

## Tool choice

For your exact constraints, I’d still start with:

- **TouchDesigner** for runtime/editor because the Python scripting surface and scriptable operators make it workable as a GUI-backed programmable system. ([Derivative](https://docs.derivative.ca/Python?utm_source=chatgpt.com))
- **Python control plane** outside TD
- **After Effects roto stage** for performer extraction because current Roto Brush 3 is materially better than trying to fake this inside a general runtime. ([Adobe Help Center](https://helpx.adobe.com/after-effects/using/roto-brush-refine-matte.html?utm_source=chatgpt.com))
- **Hybrid scene assets** rather than betting the whole project on one representation

## Blunt recommendation

Do not chase “perfect true volumetric everything” for v1.  
Build the system so:
- the scene can be fake where that helps control,
- real where that helps depth/occlusion,
- and swappable between representations.

That gets you the DX/AX you asked for without turning the whole thing into brittle researchware.

Next I should turn this into the actual artifact set: PRD, FRD, repo tree, YAML/JSON schemas, and the TouchDesigner bridge contract.

---

**Sources:**

- [Python - Derivative - TouchDesigner Documentation](https://docs.derivative.ca/Python?utm_source=chatgpt.com)
- [GLINT: Modeling Scene-Scale Transparency via Gaussian ...](https://arxiv.org/html/2603.26181v1?utm_source=chatgpt.com)
- [Roto Brush and Refine Matte in After Effects](https://helpx.adobe.com/after-effects/using/roto-brush-refine-matte.html?utm_source=chatgpt.com)

## Prompt:
4/18/2026, 4:03:35 PM

for more basic programmed gfx think as advanced as lyric driven music gfx video, and toolroom style canvas loops

## Response:
4/18/2026, 4:03:36 PM

Good-this is a *different tier* than the splat/3D system. Think of this as a **2D/2.5D programmable motion graphics engine** that’s:

- fully deterministic (beat/lyric locked)
- shader-driven
- typography-aware
- loop-friendly (for Canvas)
- agent-operable
- GUI-reviewable

Most existing “toolroom-style” loops fail because they’re:
- timeline-keyframed manually
- not phase-locked to music
- not parametric (can’t regenerate cleanly)

You want the opposite: **procedural + spec-driven motion graphics**.

---

# 🔧 Core idea (don’t miss this)

Treat the entire video as a **function of time + audio + lyrics**

```text
frame(t) = F(audio_features(t), lyric_state(t), phase(t), look_params)
```

NOT:
- keyframes
- baked animations
- timeline scrubbing as source of truth

---

# 🧠 System architecture (lightweight version of what we designed before)

## 1. Inputs

### Audio timeline
- beats
- bars
- sections
- phase (0 → 1 per beat)

### Lyrics timeline
```yaml
- word: "feel"
  start: 12.43
  end: 12.88
  emphasis: strong
- word: "the"
  start: 12.88
  end: 13.02
- word: "bass"
  start: 13.02
  end: 13.40
  emphasis: peak
```

### Derived signals
- `beat_phase`
- `bar_phase`
- `energy_bass/mid/high`
- `transient_hits`

---

## 2. Visual primitives (your building blocks)

You don’t build “videos.” You build **reusable primitives**:

### Geometry primitives
- circles / rings
- lines / rays
- grids
- text glyphs
- noise fields
- particles

### Motion primitives
- oscillation (sin/cos)
- phase rotation
- radial expansion
- pulse
- noise drift
- quantized jumps (for beat snapping)

### Visual effects
- blur
- chromatic aberration
- glitch slicing
- threshold/posterize
- displacement
- feedback loops

---

## 3. Shader-first rendering (this is key)

Everything should ultimately be driven by shaders.

Typical inputs:
```text
u_time
u_beat_phase
u_bar_phase
u_energy_bass
u_energy_mid
u_energy_high
u_word_progress
u_word_index
```

This lets you do:
- perfectly looping animations
- deterministic renders
- extreme visual density with low CPU

---

# 🎵 Beat-perfect animation model

This is where most systems fail.

### NEVER animate directly on time

Instead:

```text
phase = (t - beat_start) / beat_duration
```

Then everything uses `phase`.

---

### Example: pulsing ring

```text
radius = base + sin(phase * 2π) * amplitude
```

Now it:
- always syncs
- loops perfectly
- scales with BPM changes

---

### Example: stutter/glitch on transients

```text
if transient:
    displacement = random_jump
else:
    displacement = smooth_decay
```

---

# 🔤 Lyrics-driven visuals (this is where it becomes powerful)

## Word-level control

For each word:
```text
progress = clamp((t - start) / (end - start), 0, 1)
```

Use that to drive:
- text reveal
- scale
- distortion
- emission

---

## Example: “bass” word hit

- word appears
- expands with bass energy
- explodes on transient
- dissolves into particles

---

## Typography as geometry

Treat text as:
- SDF (signed distance field)
- mesh
- particles

Then apply:
- noise distortion
- wave displacement
- slicing/glitching

---

# 🎨 Toolroom-style loop system

These are short, seamless loops.

## Requirements:
- perfect looping (no seams)
- visually dense but simple
- hypnotic repetition
- subtle variation

---

## Loop strategy

Use **phase cycles**, not time:

```text
loop_phase = fract(t / loop_duration)
```

Everything depends on `loop_phase`.

---

## Example loop components

- rotating radial lines
- pulsing center circle
- orbiting particles
- subtle noise deformation
- color cycling

---

## Add variation without breaking loop

Use:
- low-frequency modulation
- quantized randomness per cycle

---

# 🧱 Spec system (this is what your agent edits)

## Example look spec

```yaml
look_id: toolroom_loop_01

loop_duration_beats: 8

primitives:
  - type: radial_lines
    count: 64
    rotation_speed: 1.0
    thickness: 0.002

  - type: center_ring
    base_radius: 0.2
    pulse:
      source: bass
      amplitude: 0.1

  - type: particles
    count: 2000
    orbit_speed: 0.3
    noise: 0.05

color:
  palette: monochrome
  accent_on: snare

effects:
  chromatic_aberration: 0.01
  bloom: 0.4
```

---

## Example lyric scene spec

```yaml
scene_id: chorus_01

background: dark_gradient

text:
  font: bold_sans
  align: center

behavior:
  per_word:
    enter:
      scale: [0.8, 1.2]
      duration: 0.2

    on_peak:
      distortion: 0.4
      glow: 1.0

    exit:
      dissolve: particles
```

---

# 🖥️ Runtime options (best fits your constraints)

## Best balance

### TouchDesigner
TouchDesigner

- shader support
- Python control
- real-time preview
- strong GUI for tweaking

Use it as:
- renderer
- debugger
- preview system

NOT as source of truth

---

## Code-first option

- Three.js + WebGL
- GLSL shaders
- Web Audio API

Pros:
- easier automation
- easier agent control
- easier deployment

Cons:
- weaker GUI

---

## Hybrid (best long-term)

- Python control plane
- TouchDesigner runtime
- GLSL shader core
- JSON/YAML specs

---

# 🧠 Agent workflow

Your agent should be able to:

- “Generate a toolroom-style loop synced to 128 BPM”
- “Make the chorus typography more aggressive”
- “Add glitch on snare hits only”
- “Increase visual density without breaking loop”
- “Export 6s Spotify canvas version”

That means:
- everything must be parametric
- everything must be spec-editable
- no manual-only timelines

---

# 🚀 MVP you should actually build

Don’t overbuild.

### Build this first:

1. Audio → beat/phase extractor
2. Shader-based renderer (TD or WebGL)
3. 3 primitives:
   - radial lines
   - pulsing circle
   - particles
4. Basic lyric sync (word timing)
5. Spec-driven config system
6. Loop export (6-8 sec perfect loop)

---

# 🧠 Hard truth

What you’re trying to do already exists in pieces, but:

- VJ tools = too manual  
- game engines = too heavy  
- shaders = too low-level  
- lyric video tools = too dumb  

So you’re basically building:
> a **procedural audiovisual compiler**

Which is exactly why it’s worth doing.

---

If you want next step, I’ll give you:
- exact shader templates (GLSL)
- TouchDesigner node graph blueprint
- spec schema (formal)
- CLI + agent command surface
- sample lyric-driven scene implementation

Just say and I’ll drop it clean.

## Prompt:
4/18/2026, 4:04:19 PM

yes

## Response:
4/18/2026, 4:04:22 PM

I’m turning this into a concrete starter kit: shader/core contracts, node graph blueprint, spec schema, and the command surface an agent would use.

> **Considering whether to browse for niche design info**
>
> I’m wondering if I need to browse for niche information. The user asked for design/templates, which might not need web browsing, but the system suggests it's necessary for technical details. I’ll search official docs like TouchDesigner for specifics, but avoid browsing too much unless necessary.
>
> **Browsing official documentation for TouchDesigner and Spotify**
>
> [Script TOP - TouchDesigner Documentation](https://docs.derivative.ca/Script_TOP)
> [Canvas guidelines](https://support.spotify.com/us/artists/article/canvas-guidelines/)
> [Canvas](https://artists.spotify.com/canvas)
>
> Thought for 13s

Here’s the clean starter kit for the **basic programmed GFX** tier: lyric-driven videos and Toolroom-style Canvas loops.

The core technical choice is to keep the **source of truth outside TouchDesigner** and use TouchDesigner as the live preview/runtime/editor. That fits well because TouchDesigner gives you GPU TOPs, GLSL TOPs for fullscreen shader rendering, Script TOPs for Python/NumPy image generation, CHOPs for time-varying signals, and Execute/CHOP Execute/DAT Execute operators for event-driven scripting. ([Derivative](https://docs.derivative.ca/GLSL_TOP?utm_source=chatgpt.com))

For Spotify Canvas specifically, design around an **8-second vertical loop**. Spotify’s artist docs say Canvas is a short looping visual in the Now Playing view, with 3-8 second duration, vertical 9:16 format, and uploadable as MP4 or JPG; if you target 1080×1920 MP4 you are in the safe zone. ([Spotify](https://support.spotify.com/us/artists/article/canvas-guidelines/?utm_source=chatgpt.com))

## What to build

Build a small compiler-like system:

- **input**: audio, lyric timings, look spec
- **processor**: beat/phase/event extraction
- **renderer**: shader scenes + text layers + FX
- **runtime**: TouchDesigner project for live preview/tweaks
- **export**: deterministic loop/video render

The mental model is:

```text
frame(t) = scene(phase_signals(t), lyric_state(t), look_params)
```

Not:
- hand-keyframed timeline soup
- manual node spaghetti as the only truth

## Repo shape

```text
lyricviz/
  pyproject.toml
  README.md
  src/
    cli/
      main.py
    core/
      spec_models.py
      timeline.py
      phases.py
      easing.py
    audio/
      analyze.py
      beats.py
      sections.py
      events.py
    lyrics/
      parse_lrc.py
      align.py
      states.py
    looks/
      presets.py
      validators.py
    render/
      uniforms.py
      build_payload.py
      export_jobs.py
    td_bridge/
      push_json.py
      osc_client.py
      overrides.py
  specs/
    tracks/
    looks/
    scenes/
    exports/
  td/
    runtime.toe
    shaders/
      radial_loop.frag
      lyric_reveal.frag
      particles.frag
    scripts/
      load_spec.py
      on_frame.py
      export_overrides.py
  assets/
    audio/
    fonts/
    palettes/
    logos/
  tests/
```

## Minimal spec schema

Use three core files.

### 1) Track timeline
```json
{
  "track_id": "toolroom_demo_01",
  "duration_sec": 180.0,
  "bpm": 128.0,
  "beats": [0.000, 0.469, 0.938],
  "downbeats": [0.000, 1.875, 3.750],
  "sections": [
    {"name": "intro", "start": 0.0, "end": 16.0},
    {"name": "drop", "start": 16.0, "end": 48.0}
  ],
  "events": [
    {"t": 16.000, "type": "drop", "strength": 1.0},
    {"t": 16.469, "type": "kick", "strength": 0.91}
  ]
}
```

### 2) Lyrics timing
```json
{
  "track_id": "toolroom_demo_01",
  "words": [
    {"text": "feel", "start": 12.430, "end": 12.880, "emphasis": "strong"},
    {"text": "the",  "start": 12.880, "end": 13.020, "emphasis": "normal"},
    {"text": "bass", "start": 13.020, "end": 13.400, "emphasis": "peak"}
  ]
}
```

### 3) Look spec
```yaml
look_id: toolroom_loop_01
canvas_mode: true
loop_beats: 8

background:
  kind: radial_gradient
  vignette: 0.45

primitives:
  - id: rays
    type: radial_lines
    count: 96
    thickness: 0.003
    rotation_per_loop: 1.0
    pulse_source: bass

  - id: ring
    type: center_ring
    radius: 0.22
    pulse_amp: 0.08
    pulse_source: kick

  - id: particles
    type: orbit_particles
    count: 1400
    orbit_speed: 0.2
    jitter: 0.03

text:
  font: Inter-Bold
  mode: lyric_word
  reveal: wipe
  distortion_on_peak: 0.25

post:
  bloom: 0.35
  chroma: 0.01
  grain: 0.04
```

## Agent command surface

Give the agent operations at the spec level.

```bash
viz analyze-audio assets/audio/demo.wav
viz import-lyrics assets/audio/demo.lrc
viz build-look specs/looks/toolroom_loop_01.yaml
viz sync-td
viz preview --scene chorus_01
viz export-canvas --scene loop_01 --out out/canvas.mp4
viz export-video --scene chorus_01 --range 00:48-01:12
viz diff-overrides
```

This matters because the agent should edit:
- specs
- shader parameters
- timing rules
- scene composition

Not drag nodes around blindly.

## TouchDesigner runtime blueprint

TouchDesigner is best here as a GPU-backed runtime plus GUI review surface. GLSL TOP is the right place for fullscreen shader passes, Script TOP is useful for Python-generated imagery or masks, and Execute/CHOP Execute/DAT Execute are the glue for runtime updates from changing channels/tables/specs. ([Derivative](https://docs.derivative.ca/GLSL_TOP?utm_source=chatgpt.com))

Inside `runtime.toe`:

```text
/project1
  /io
    spec_table
    dat_execute_spec_reload
    osc_in
  /timeline
    audio_clock
    beat_phase_chop
    bar_phase_chop
    lyric_state_dat
    event_bus
  /scene
    bg_glsl
    rays_glsl
    ring_glsl
    particles_glsl
    text_comp
  /mix
    composite_1
    grade_1
    feedback_1
    out_null
  /ui
    controls
    debug
    override_export
  /export
    moviefileout1
```

### Runtime data flow

1. Python side writes `spec.json`
2. DAT Execute notices file/table change
3. Python script updates operator parameters / uniforms
4. CHOPs provide time-varying phase signals
5. GLSL TOPs render passes
6. Composite and export

That’s a clean split:
- Python/specs = intelligence
- TD = render/runtime/editor

## Uniform contract

Your shaders should all consume a common base contract.

```glsl
uniform float uTime;
uniform float uBeatPhase;
uniform float uBarPhase;
uniform float uLoopPhase;
uniform float uBass;
uniform float uMid;
uniform float uHigh;
uniform float uWordProgress;
uniform float uWordActive;
uniform float uWordPeak;
uniform vec2  uResolution;
```

Then every visual primitive can be musically locked without per-scene reinvention.

## Phase math

Use phase, not raw time, for anything that should sync.

```python
def phase(t: float, start: float, duration: float) -> float:
    if duration <= 0:
        return 0.0
    return max(0.0, min(1.0, (t - start) / duration))

def loop_phase(t: float, loop_dur: float) -> float:
    return (t % loop_dur) / loop_dur
```

For beat-based loops:

```python
seconds_per_beat = 60.0 / bpm
loop_dur = loop_beats * seconds_per_beat
uLoopPhase = loop_phase(t, loop_dur)
```

That guarantees clean loop closure if the animation is periodic on `uLoopPhase`.

## Shader 1: Toolroom-style radial loop

Use this as the base background/motion layer.

```glsl
// radial_loop.frag
out vec4 fragColor;

uniform float uTime;
uniform float uBeatPhase;
uniform float uLoopPhase;
uniform float uBass;
uniform float uHigh;
uniform vec2  uResolution;

float hash(float n) { return fract(sin(n) * 43758.5453123); }

void main() {
    vec2 uv = (gl_FragCoord.xy * 2.0 - uResolution.xy) / min(uResolution.x, uResolution.y);
    float r = length(uv);
    float a = atan(uv.y, uv.x);

    float rays = 0.0;
    float rayCount = 96.0;
    float sweep = a + uLoopPhase * 6.28318530718;
    float stripe = abs(sin(sweep * rayCount * 0.5));
    rays = smoothstep(0.92, 1.0, stripe);

    float ring = smoothstep(0.26 + uBass * 0.03, 0.24 + uBass * 0.03, abs(r - (0.20 + 0.04 * sin(uBeatPhase * 6.28318530718))));
    float glow = 0.02 / max(abs(r - 0.2), 0.001);

    float highSpark = smoothstep(0.96, 1.0, sin((a * 24.0) + uTime * 8.0 + uHigh * 2.0));

    vec3 col = vec3(0.0);
    col += vec3(0.85) * rays * (0.20 + 0.35 * uBass);
    col += vec3(1.0) * ring;
    col += vec3(0.7) * glow * 0.25;
    col += vec3(1.0) * highSpark * 0.07;

    float vignette = smoothstep(1.4, 0.2, r);
    col *= vignette;

    fragColor = vec4(col, 1.0);
}
```

What it gives you:
- rotating radial energy
- center ring pulse
- clean monochrome club aesthetic
- easy loop closure with `uLoopPhase`

## Shader 2: lyric word reveal/distortion

This assumes you feed a text texture into a second input and distort/reveal it.

```glsl
// lyric_reveal.frag
out vec4 fragColor;

uniform sampler2D sTD2DInputs[1];
uniform float uWordProgress;
uniform float uWordPeak;
uniform float uBass;
uniform vec2  uResolution;

void main() {
    vec2 uv = gl_FragCoord.xy / uResolution.xy;

    float wobble = sin(uv.y * 30.0 + uWordProgress * 6.28318530718) * 0.003 * (0.2 + uWordPeak);
    wobble += sin(uv.x * 18.0) * 0.002 * uBass;

    vec2 duv = uv + vec2(wobble, 0.0);
    vec4 tex = texture(sTD2DInputs[0], duv);

    float wipe = smoothstep(uWordProgress - 0.08, uWordProgress + 0.02, uv.x);
    tex.rgb *= wipe;

    float edgeBoost = smoothstep(0.6, 1.0, tex.a) * uWordPeak * 0.6;
    tex.rgb += edgeBoost;

    fragColor = tex;
}
```

This gives you:
- word wipe-on
- mild waveform-like distortion
- emphasis boost on peak words

## Python side: lyric state resolver

```python
from dataclasses import dataclass

@dataclass
class Word:
    text: str
    start: float
    end: float
    emphasis: str = "normal"

def word_state(words: list[Word], t: float) -> dict:
    active = None
    for i, w in enumerate(words):
        if w.start <= t <= w.end:
            active = (i, w)
            break

    if not active:
        return {
            "word_index": -1,
            "word_text": "",
            "word_progress": 0.0,
            "word_active": 0.0,
            "word_peak": 0.0,
        }

    i, w = active
    dur = max(w.end - w.start, 1e-6)
    p = max(0.0, min(1.0, (t - w.start) / dur))
    peak = 1.0 if w.emphasis in {"strong", "peak"} else 0.5

    return {
        "word_index": i,
        "word_text": w.text,
        "word_progress": p,
        "word_active": 1.0,
        "word_peak": peak,
    }
```

## TouchDesigner glue example

Use a DAT Execute or Execute DAT to reload spec-driven settings when your spec table or file changes, and a CHOP Execute to push live beat/phase channel changes into parameters or trigger stateful events when needed. That is exactly what those operators are for in TD. ([Derivative](https://docs.derivative.ca/DAT_Execute_DAT?utm_source=chatgpt.com))

Pseudo-pattern:

```python
# td/scripts/load_spec.py
import json

def load_spec(path):
    with open(path, "r") as f:
        spec = json.load(f)

    op("scene/bg_glsl").par.resolutionw = spec["resolution"][0]
    op("scene/bg_glsl").par.resolutionh = spec["resolution"][1]

    op("ui/controls").store("look_spec", spec)
    return spec
```

## Scene recipes

### Recipe A: Toolroom loop
Use for Canvas and lightweight club visuals.

- background radial shader
- pulsing ring
- orbit particles
- no lyrics or one center tag line
- low color count
- perfect 8-beat loop

### Recipe B: lyric chorus
Use for lyric-driven promo clips.

- restrained animated background
- center or lower-third text
- word-by-word reveal
- transient distortions on key words
- section-based palette shifts

### Recipe C: typography assault
Use for drop or climax.

- stacked repeated words
- feedback trails
- threshold/posterize
- grid/ray background
- kick-synced flash wipes

## Export rules

For Spotify Canvas:
- hard-target **8.0 seconds**
- vertical **9:16**
- no dependency on full lyric comprehension because Spotify itself notes Canvas clips are only 3-8 seconds and advises against talking/singing/rapping footage since they will not sync to lyrics in that format. ([Spotify](https://support.spotify.com/us/artists/article/canvas-guidelines/?utm_source=chatgpt.com))

So for Canvas, prioritize:
- loop purity
- motion identity
- brand/aesthetic imprint
- maybe 1-3 words max, not full lyric storytelling

For lyric videos outside Canvas, use longer-form scene chaining.

## Manual override strategy

Do not let manual tweaks die inside the TD file. Export them.

```yaml
overrides:
  looks.toolroom_loop_01.primitives.rays.count: 120
  looks.toolroom_loop_01.post.bloom: 0.42
  scenes.chorus_01.text.distortion_on_peak: 0.33
```

That gives you:
- diffability
- agent awareness
- reproducibility

## What to build first

First, get these 5 things working:

1. audio analysis → beat/bar/loop phase
2. one radial GLSL scene
3. one text reveal scene
4. TouchDesigner spec loader
5. 8-second MP4 export

That alone is enough to start generating decent Toolroom-style loops and lyric micro-scenes.

After that, add:
- particles
- palette systems
- section-aware scene switching
- feedback and glitch passes
- better typography layout rules

## Hard recommendation

For this tier, do **not** start with splats, volumetrics, or complex 3D.  
Build a **2D/2.5D shader-typography engine** first. It is closer to the actual aesthetic target, faster to iterate, much easier for agents to control, and still maps cleanly onto TouchDesigner’s strengths as a GPU/runtime tool. ([Derivative](https://docs.derivative.ca/GLSL_TOP?utm_source=chatgpt.com))

I can turn this into an actual project scaffold next, either as a canvas doc or as files in a zip-like artifact structure.

---

**Sources:**

- [GLSL TOP - TouchDesigner Documentation](https://docs.derivative.ca/GLSL_TOP?utm_source=chatgpt.com)
- [Canvas guidelines](https://support.spotify.com/us/artists/article/canvas-guidelines/?utm_source=chatgpt.com)

## Prompt:
5/30/2026, 4:56:44 PM

A couple examples that the program would need to be able to automatically derive from the same given "preset"\config seeds

Pop-progressive dance house track, typical of early to mid 2020s place

lead at start is a solo chord stab, then followed with a high pitched vocal chop BG, soft female voice lead, later on stronger w\ kick add in and doubling of voice, eventually clap and very very mild hihat to the point where lack of focus will assume still the intermediary kick + clap rather than full house step

before typical pop progressive buildup -> chord becomes a saw w\ kick ride step flow

the airy \ warm sort of quasi euphoric feel needs to be picked up by the system somehow, such that the stabs at the start can be viewed as a sort of translucent stained glass shard, euphoric + airy -> rather than a vector\2d like a typical tech house track would get insstead a 3d render with that translucent\glassmorphic feel -> euphoric pink\purples pallete

this would be the drop described below. it will bounce on beat when in midair + other effects like shapeshifts or effectively travelling (forward\backwards axis, wormhole like effects)

this drop is not 100% of the scenes but typically just for intro buildup and extended mix final builddown.
sunrise\sundown effects done in many ways also highly important. 

for a tech house scene or very heavy clubby tech progressive\melodic house\techno ball becomes big and heavy as does the vibe, lots of sillouhettes\night urban scenes + other items like sillhouete dancing. 3d allowed in very artistic y2k\streety ways. as described before.

There is typically a sort of water drop aesthetic that comes in my mind for all house driven tracks (imagine AFTER impact at peak of the counter splash where there is a sort of ball at the top seperate from the cone structure below it, the viz ,may never show the cone structure\water surface w ripples, or it may quickly before hanging on the droplet, not importnat.

What is imortnat is the concept of a decelerating rise -> perhaps hang -> slow accelerate to quick drop -> riser plays effectively buildup to match the literal drrop -> flash when done.

im not sure what makes me sort of hyperfocus on thematic variations of this (typically just a circle with vector graphhicy theme effects in my head, sometimes somethign else like this glass shard), but it seems to always mesh very wellw ith audio when drafted. 

background colors\pallets should definietly shake and flash change on EACH beat, then one of or mix of 1\2\4\8 bars. 

i

## Response:
5/30/2026, 4:56:47 PM

This is a useful example because it shows the system cannot just map “house = circle pulse.” It needs a layered inference model: genre/energy/timbre/emotion/arrangement all feeding different visual decisions.

Yes. The program needs to derive **visual grammar**, not just effects.

Your examples imply a system like:

```text
audio + seed preset
→ inferred track identity
→ visual archetype
→ motif selection
→ scene progression
→ beat/bar-locked animation
→ render
```

## 1. Separate “what it hears” from “what it draws”

The system should infer these layers:

```yaml
track_analysis:
  genre_family: house
  substyle: pop_progressive_dance
  energy_curve: soft_intro_to_euphoric_build
  timbre:
    lead: chord_stab
    texture: airy_vocal_chop
    vocal: soft_female
    drums: kick_then_clap_then_light_hat
  emotion:
    warmth: high
    euphoria: high
    darkness: low
    heaviness: low
    club_pressure: medium
  arrangement:
    intro: sparse_stabs
    build: vocal_chop_layers
    pre_drop: saw_chord_riser
    drop: kick_ride_progressive_flow
```

Then visuals derive from that.

Not:

```yaml
genre: house
visual: circle_pulse
```

That would be trash.

---

## 2. Example: pop-progressive dance house mapping

For your airy/euphoric example:

```yaml
visual_archetype:
  world: glassmorphic_sunrise_space
  primary_motif: translucent_stained_glass_shard
  secondary_motif: floating_orb_droplet
  palette:
    base: warm_pink_purple
    accents: sunrise_gold
    shadows: soft_violet
  material:
    transparency: high
    refraction: high
    bloom: high
    edge_hardness: medium
  camera:
    motion: forward_backward_float
    depth: strong
  beat_behavior:
    every_beat: palette_flash_soft
    every_2_bars: shard_reorientation
    every_4_bars: background_sun_shift
    every_8_bars: camera_tunnel_push
```

The chord stabs become **glass impacts** or **floating shards**.

The vocal chop becomes:
- airy mist
- small refracted echoes
- vertical particle glints
- soft halo trails

The kick entering makes the shard:
- bounce downward/upward on beat
- pulse in scale
- refract harder
- briefly “solidify”

The buildup saw chord becomes:
- forward acceleration
- widening tunnel
- growing brightness
- shard stretching into a prism/saw blade form

---

## 3. Example: tech house / heavy club mapping

For heavier tech/prog/techno:

```yaml
visual_archetype:
  world: night_urban_pressure
  primary_motif: heavy_black_orb
  secondary_motif: water_drop_mass
  palette:
    base: black_steel_blue
    accents: sodium_orange_or_neon_green
    flash: white_or_red
  material:
    transparency: low
    weight: high
    roughness: high
    metallic: medium
  environment:
    silhouettes: true
    city_depth: true
    club_fog: true
  beat_behavior:
    every_beat: hard_palette_shake
    every_1_bar: silhouette_cut
    every_4_bars: street_scene_jump
    every_8_bars: orb_mass_event
```

Here the ball should feel **heavy**, not floaty.

So animation changes:
- slower acceleration
- harder impacts
- less bloom, more contrast
- squash/stretch feels massive
- camera shake is tighter and more violent
- silhouettes and night scenes become acceptable

Same motif class, different physics.

---

## 4. Your “water droplet” motif is important

This should become a reusable **house drop primitive**.

Call it:

```yaml
motif: suspended_drop
```

It has a built-in motion grammar:

```text
decelerating rise
→ hang/suspension
→ tension stretch
→ fast accelerating fall
→ impact flash
→ ripple/scene transition
```

That maps insanely well to house builds because “drop” is both musical and physical.

### Motion curve

```yaml
suspended_drop:
  phases:
    rise:
      curve: ease_out_cubic
      duration_beats: 4
    hang:
      curve: hold_with_micro_jitter
      duration_beats: 1
    fall:
      curve: ease_in_expo
      duration_beats: 1
    impact:
      duration_beats: 0.25
      effects:
        flash: high
        palette_swap: true
        shockwave: true
```

This can become:
- glass shard
- liquid droplet
- chrome orb
- black techno sphere
- logo mark
- lyric word
- particle cluster

Same timing skeleton, different material/scene skin.

That is exactly how you get reusable configs that still feel custom.

---

## 5. Beat/bar flash system

You’re right that color/palette should move on multiple rhythmic levels.

Use a hierarchy:

```yaml
rhythm_modulation:
  beat:
    palette_flash: 0.15
    brightness_pulse: 0.20
    camera_jolt: 0.04

  bar_1:
    background_shift: 0.20
    shape_rotation_snap: true

  bar_2:
    palette_variant_step: true

  bar_4:
    scene_layer_swap: true

  bar_8:
    major_transition: true
```

So every beat breathes, but the viewer also feels longer musical structure.

That avoids the “random audio reactive screensaver” problem.

---

## 6. Preset seeds should be abstract, not literal

A bad preset seed:

```yaml
preset: pink glass shard
```

A good preset seed:

```yaml
preset_seed:
  emotion: euphoric
  weight: light
  material_family: glass
  spatiality: deep_3d
  motif_family: suspended_object
  world_time: sunrise
  rhythmic_density: medium
```

Then the system can derive:

```yaml
derived_visual:
  object: stained_glass_shard
  background: sunrise_gradient_wormhole
  motion: floating_bounce
  beat_response: soft_flash
```

For tech house:

```yaml
preset_seed:
  emotion: dark
  weight: heavy
  material_family: liquid_metal
  spatiality: urban_2_5d
  motif_family: suspended_object
  world_time: night
  rhythmic_density: high
```

Derived:

```yaml
derived_visual:
  object: black_chrome_droplet
  background: night_city_silhouettes
  motion: heavy_rise_drop
  beat_response: hard_flash
```

Same system. Different result.

---

## 7. The real “intelligence” layer

You need a visual semantic mapper.

Something like:

```text
airy + female vocal + euphoric + sparse intro
→ glass / mist / sunrise / floating / pink-purple / soft bloom

heavy + tech + dark + dense kick
→ black orb / silhouettes / urban / hard contrast / low camera / strobe

saw buildup + riser + increasing kick density
→ acceleration / tunnel / object stretch / rising tension

drop impact
→ fall completion / flash / material swap / camera hit
```

This can start rule-based.

Do **not** start with ML for this. Hard-code the grammar first.

Later, an LLM/agent can help choose mappings, but the renderer needs deterministic primitives.

---

## 8. The system should output a scene plan

For your first example, the program should generate something like:

```yaml
scene_plan:
  intro:
    motif: glass_shard
    state: suspended
    material: translucent_pink_violet
    background: soft_sunrise_gradient
    motion:
      beat_bounce: low
      forward_drift: slow

  vocal_chop_section:
    add_layers:
      - vocal_glints
      - mist_particles
    motion:
      shard_echoes_on_chops: true

  kick_entry:
    beat_bounce: medium
    palette_flash_each_beat: true
    shard_refraction_pulse: true

  buildup:
    transform:
      shard_to_saw_prism: true
    camera:
      wormhole_push: increasing
    tension:
      suspended_drop_rise: active

  drop:
    impact_flash: true
    object_fall_complete: true
    background_palette_swap: true
    beat_bounce: high
```

For tech house:

```yaml
scene_plan:
  intro:
    motif: black_orb
    state: low_hover
    background: night_urban_silhouette
    motion:
      beat_bounce: heavy_low

  groove:
    add_layers:
      - dancer_silhouettes
      - street_grid
      - fog_rays
    palette_flash_each_beat: hard

  buildup:
    suspended_drop_rise:
      material: liquid_metal
      camera: low_angle
      tension: high

  drop:
    fast_fall: true
    impact_flash: white_red
    shockwave: hard
    silhouettes_cut_on_clap: true
```

---

## 9. Core primitives to implement first

You do not need 100 effects. You need the right primitives.

Build these:

1. **Suspended object**
   - circle/orb/shard/logo/word
   - rise/hang/fall/drop timing

2. **Beat palette flasher**
   - every beat
   - every 1/2/4/8 bars

3. **Material families**
   - glass
   - chrome
   - liquid
   - matte black
   - neon vector
   - paper/poster

4. **World backdrops**
   - sunrise gradient
   - night urban
   - tunnel/wormhole
   - club silhouettes
   - abstract grid

5. **Vocal texture emitters**
   - mist
   - glints
   - waveform ribbons
   - text fragments

6. **Build tension controller**
   - scale increase
   - camera push
   - object rise
   - brightness ramp
   - frequency/strobe increase

That gets you most of the way.

---

## 10. Blunt product insight

The reason your droplet/circle motif keeps working is probably because it is a **universal tension/release symbol**:

- rise = buildup
- hang = anticipation
- fall = drop
- impact = musical release
- circle/orb = simple enough to adapt to any subgenre
- material/palette carries the emotional identity

So the system should absolutely treat it as a core reusable motion archetype.

Not as “one effect.”

More like:

```yaml
archetype: tension_release_body
```

Then skin it per track.

That’s the difference between a generic visualizer and a programmable music video engine.



---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)