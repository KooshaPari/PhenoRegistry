# Pass 40 — corrected mature baselines and existence experiments

Date 2026-09-30.

## Baselines rewritten from restored intent

Portage `464d1d47b93d40e8baa8afccdf706dfbbae7fda3`: portable execution/compatibility is first-class; evidence envelope is supporting infrastructure.

PhenoMLX `1ddb1440206d903cb3080172bfbc7bffd5fd6881`: experimental runtime/research studio is first-class; typed profiles are foundational but partly commodity.

PhenoLab `dfdb602f98c9150071afbf4b70a50672b9120a6e`: ExperimentProgram(model+harness/workload→target) is top-level; generated kernels/prompts/runtime patches are lab artifacts unless evidence promotes them.

## Corrected existence experiments

Common experiment document committed:
Portage `8a8b2c343203886011563759396e288c827ab46a`.
PhenoMLX `f357e88e4c6a1fd32dc482cdadf30131abc5137c`.
PhenoLab `0216079c458df9a81cbcf5ea6c1cc61fc001054f`.

- EXP-P1: same TaskContract across Docker/reference and materially different ARM/native/non-Docker substrate.
- EXP-M1: one novel runtime mechanism vs best Unsloth/engine-native baseline; wrapper/dashboard alone cannot pass.
- EXP-L1: one real model+harness target program with multiple interventions, durable failures/learning and worker replacement; defensible failed search is a valid outcome.

Prior VS-01s are conceptually renamed INFRA-01.

## External research update

Unsloth Studio current source makes the PhenoMLX existence attack stronger:
- explicit CPU/CUDA/ROCm/Vulkan llama.cpp installer selection;
- inference state models unknown/lower-bound memory, MLX requested/applied KV quantization, TurboQuant vocabulary, speculative modes, tensor parallel, placement and fallback reasons;
- startup probes check llama.cpp MTP capability/freshness;
- Studio UI is AGPL-3.0 while core Unsloth package is Apache-2.0.

Thus several PhenoMLX ideas are reusable prior art or commodity; custom work must justify itself experimentally.

## Program consequence

The recovery is now back on the correct mature-first track:
original intent is preserved; modern alternatives can still falsify the original fork form; infrastructure work survives but cannot substitute for existence evidence.

Next:
1. derive capability/requirement deltas from vNext baselines;
2. deepen EXP-P1 backend primitive matrix;
3. inspect Unsloth Studio experiment persistence/plugin/benchmark gaps for EXP-M1;
4. machine-schema ExperimentProgram/ObjectiveTarget/InterventionSet for EXP-L1;
5. update completion gates so INFRA-01 cannot accidentally close product architecture.
