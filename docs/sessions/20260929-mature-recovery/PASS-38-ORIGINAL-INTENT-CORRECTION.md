# Pass 38 — authoritative original-intent correction

Date 2026-09-30.

Direct user clarification materially corrects the recovery program.

## Portage
Original Harbor fork thesis was portability first: Harbor was effectively Docker/x86 constrained for the user's needs; Portage sought ARM64, bare metal and interchangeable container/sandbox/runtime backends. Later user scope included competitor integrations and useful changes from peer DeepSea's fork. Agents also had broad autonomy to add enhancements.

Therefore the recent thin-evidence model is only one **2026 survival candidate**, not the recovered original intent. Existence research must compare portable Harbor superset vs thin layer given modern Harbor's expanded provider/environment support.

## PhenoMLX
Original thesis was runtime rewrite/extension for experimentation and dashboards, including hand-rolled extended speculative decoding, quantization and other LLM runtime features. Later ambition expanded to Windows/Linux and CUDA/Vulkan/ROCm/other platforms.

The prior recovery over-collapsed this into typed profile qualification. Correct existence alternatives now include:
A experimental runtime rewrite;
B cross-platform LLM runtime/studio;
C typed qualification/control layer;
D hybrid: mature engines + custom experimentally justified runtime extensions.

Unsloth Studio is now a primary SOTA/existence attack because current official materials overlap Windows/Linux/macOS, NVIDIA/AMD, Vulkan, MLX, multi-GPU, local run/train/export and recent MLX/KV-cache optimization.

## PhenoLab
Original repo was scratch/R&D with many agents generating kernels/other experiments toward a target for a model+harness (speed, accuracy or another objective).

The mature product thesis should therefore be the reliable experiment/control/evidence loop that moves a model+harness toward a declared target, while generated kernels/optimizations may remain ephemeral experiment outputs.

## Process correction
All three now require separate fields:
ORIGINAL USER INTENT / LATER USER EXPANSION / AGENT-AUTONOMOUS EXPANSION / CURRENT IMPLEMENTATION / CURRENT COMMODITY / SURVIVING DIFFERENTIATION.

This prevents mature-first pruning from rewriting the history of why a fork existed.

Repo receipts:
Portage `5c733d6f03f493590af4a150c97584e62f3b8da2`.
PhenoMLX `2a26876fa8bbb2fa7ec36cdbe87efe22b58ae35d`.
PhenoLab `8c6b78495354eeca8a0075732d2063d85b8b442e`.
Unsloth research gate `9183b5baa25118d2e3782b7a54ffe6f2480111fb`.

## Immediate next work
1. re-open Portage SOTA around portable execution/sandbox backends + DeepSea fork, not just evidence envelopes;
2. perform deep Unsloth Studio + adjacent cross-platform runtime architecture research for PhenoMLX;
3. reframe PhenoLab ontology around target-driven model+harness experiment loops and distinguish ephemeral generated artifacts from durable lab machinery;
4. revise provisional baselines where original-intent restoration changes mature alternatives;
5. do not discard prior semantic/evidence work—it remains useful infrastructure, but no longer defines the whole product thesis.
