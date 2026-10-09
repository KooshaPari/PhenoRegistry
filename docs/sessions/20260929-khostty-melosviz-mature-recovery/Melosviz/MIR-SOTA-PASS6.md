# Melosviz MIR SOTA / bootstrap pass 6

Research date: 2026-09-30. Product snapshot: `KooshaPari/Melosviz@1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`.

Status: architecture research. No dependency or model adoption is authorized by this document.

## Current implementation being challenged

Frozen `backend/src/melosviz/analysis/audio.py` currently composes multiple heuristics/tools:
- librosa beat tracking in a child process, with a pure-numpy fallback;
- downbeats derived as every fourth beat when no stronger tracker is used in the inspected path;
- section boundaries from librosa spectral novelty;
- section labels from hand-coded feature/position heuristics;
- optional Demucs stems, otherwise spectral/HPSS approximations;
- chroma-based harmonic/key estimates;
- dense keyframes derived from these outputs.

This is a valid fallback-oriented engineering approach. It is **not** evidence that these individually hand-composed estimators remain the optimal primary MIR architecture.

## Strong candidate: All-In-One music structure analysis

Original research:
- Paper: Kim & Nam, *All-In-One Metrical And Functional Structure Analysis With Neighborhood Attentions on Demixed Audio*, WASPAA 2023, arXiv 2307.16425.
- Exact original repository inspected: `mir-aidj/all-in-one@18e78903c0365147a2c5d4e5e57ebf88cb7d800e`.
- Root license: MIT.
- The model jointly predicts tempo, beats, downbeats, functional segment boundaries and labels from demixed audio.

The paper's Harmonix Set table reports for its 300K-parameter All-In-One model:
- beat F1 0.958;
- downbeat F1 0.915;
- segmentation HR.5F 0.660;
- functional-label pairwise F-measure 0.738.

The authors compare against multiple task-specific baselines on Harmonix and report improvements on their representative metrics. That evidence establishes strong performance **on Harmonix under that study's protocol**. It does not establish Melosviz accuracy on the user's music distribution, exact frame-lock suitability, or superiority to newer 2026 methods outside that benchmark.

The implementation exposes 100 Hz activations for beat/downbeat/segment/label and four-stem embeddings. Its docs specifically recommend normalizing MP3 to WAV because decoder-dependent offsets around 20–40 ms can matter relative to common beat tolerances. That aligns directly with Melosviz's WAV-first contract.

### Original-project integration risk

The original repo's main commit is from 2023 and its documented stack requires NATTEN plus a GitHub-installed madmom. This is meaningful maintenance/install risk in a 2026 desktop product.

## 2026 packaging alternative: all-in-one-infer

Pinned source:
- `openmirlab/all-in-one-infer@5589ea9d0baa1e43c82ab43047c63ade48db14a8`
- root LICENSE blob `e4cd60d0b445d6420121df27f151534685c5e217`, MIT with upstream attribution.

Current project documentation says v3.x retains the original research/model/checkpoints while modernizing the runtime:
- pure-PyTorch neighborhood attention, removing mandatory legacy NATTEN;
- `demucs-infer` for source separation;
- `madmom-infer` for the used spectrogram/DBN surface;
- PyPI-friendly packaging;
- activation frame rate exposed in results;
- direct/precomputed stem inputs and reusable session/model loading.

Its July 2026 release notes report end-to-end compatibility checks against real songs for the packaging substitutions. Those are **project-maintainer claims**, not independent Melosviz evidence.

## Alternatives and disposition

| Approach | Disposition | Reason |
|---|---|---|
| Existing Melosviz librosa + heuristic stack | KEEP as fallback/baseline | Lightweight, understandable, no model download required; useful failure fallback and comparison |
| Original `all-in-one` | LEARN FROM / benchmark | Strong published evidence, but stale install surface |
| `all-in-one-infer` | **INTEGRATE SPIKE** | Same research task fits Melosviz unusually well; 2026 packaging removes much of original integration friction |
| madmom direct | KEEP only where independently useful | Established beat/downbeat decoders but current packaging friction and older task specialization |
| librosa segmentation | KEEP fallback / feature primitive | Useful deterministic structural primitives; not functional-section semantic SOTA by itself |
| custom new MIR model | REJECT until alternatives fail | No evidence justifies training/owning a new model |

## Required integration experiment: M-MIR-01

Use a small corpus that is legally usable and representative of the intended product, with reviewer-owned timing/structure annotations where possible. Do not evaluate only generated sine fixtures.

Compare:
1. frozen Melosviz analyzer;
2. all-in-one-infer pinned candidate;
3. optional hybrid using All-In-One structure + Melosviz additional spectral/harmonic features.

Measure separately:
- beat F1 and timing error;
- downbeat F1/timing error;
- section-boundary metrics at explicit tolerances;
- functional-label agreement where labels exist;
- analysis wall time CPU/GPU;
- model warm/cold start;
- memory/VRAM;
- install/package footprint;
- offline model-availability failure;
- deterministic/stable output under repeated runs;
- exact source-audio/timebase identity.

Do not average these into one score. Beat timing may be critical while section-label quality is a softer creative aid.

## Candidate architecture if the spike survives

```
WAV identity
   ↓
qualified MIR provider interface
   ├── all-in-one-infer (primary candidate)
   └── librosa/lightweight fallback
   ↓
MIREvidence
  raw provider outputs + provider/model/version +
  uncertainty/activations + explicit timebase
   ↓
accepted editorial anchors / scene suggestions
```

MIR output is an observation/inference, not authorized edit truth. A model saying “chorus” does not make that label authoritative; users/director logic may accept or override it. Preserve original output and override provenance.

Melosviz-specific features not supplied by All-In-One—spectral trajectories, custom mood features, lyrics, harmonic/chord cues, visual-control mappings—remain separate composable analysis passes rather than reasons to duplicate beat/downbeat/structure inference.

## Decision gate

Do not freeze `all-in-one-infer` as a mandatory dependency until:
- the pinned package installs in the actual supported desktop/backend environments;
- model/checkpoint acquisition/offline policy is acceptable;
- benchmark evidence on Melosviz-relevant audio exists;
- its timing output maps losslessly into the product's rational audio/editorial timebase;
- license/weights provenance and redistribution/download policy are resolved.

Until then: **INTEGRATE SPIKE, not adopted architecture.**
