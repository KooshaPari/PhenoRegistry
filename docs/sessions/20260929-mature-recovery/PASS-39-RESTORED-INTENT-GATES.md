# Pass 39 — restored-intent architecture gates reopened

Date 2026-09-30.

## Portage portability gate
Receipt `b7b0a1ca03998660b7861263db5dd1a15bfb44da`.

Modern Harbor has a broad environment family, so the original Portage problem cannot be evaluated against old Harbor. But current provider breadth is not synonymous with backend-neutral execution: current Modal implementation, for example, can run Docker daemon/Compose inside the sandbox (or VM runtime). The reopened gate now tests ISA/multi-arch, true bare metal, OCI alternatives, sandbox substitutability, primitive parity and Windows/Linux/macOS behavior.

Possible outcome remains that modern Harbor absorbs most original Portage value; that is not assumed.

DeepSea peer-fork delta remains an explicit archaeology target with unknown exact repo/alias.

## PhenoMLX vs Unsloth Studio
Receipt `b6f611645e74c7e17d3d2e81ee224a619f197f08`.

Current Unsloth Studio source directly overlaps restored intent. It supports native Windows installer plus Linux/WSL/macOS, selectable llama.cpp CPU/CUDA/ROCm/Vulkan, Apple MLX, multi-GPU and rich model runtime controls. Its inference state already tracks requested-vs-applied MLX KV quantization, refusal reasons, speculative modes, GPU placement, chat-template overrides and fallback reasons.

Therefore typed requested/realized profile state is partly **commodity/table-stakes**, not sufficient differentiation.

PhenoMLX must justify deeper research-grade experimentation, novel decoding/quantization/kernel work, reproducible cross-engine qualification or lower-level runtime innovation beyond what Studio exposes.

## PhenoLab target-driven ontology
Receipt `89f521c7bace94a9b26186917bfbb4d2139fc0ac`.

ExperimentProgram(ModelSystem + Harness/Workload → Objective Target under Constraints) is now the top-level product object.

Prompts, kernels, quantization variants, runtime patches, topology changes, fine-tunes and other generated work are InterventionSet/artifacts. They become durable reusable components only if evidence/maintenance envelope justifies promotion.

This better matches the scratch-R&D origin and prevents historical generated work from inflating product ontology.

## Baseline consequence
The provisional baselines are no longer sufficient as final mature candidates:
- Portage baseline must add portable execution thesis as a first-class alternative.
- PhenoMLX baseline must restore experimental runtime/studio thesis and treat typed qualification as infrastructure, not sole identity.
- PhenoLab baseline must elevate ExperimentProgram/ObjectiveTarget above conventional candidate workflow.

Existing evidence/authority/state-machine work remains reusable.

Next:
1. revise provisional baselines to vNext with restored-intent alternatives;
2. deepen Portage competitor/backend primitive matrix + recover DeepSea alias;
3. deepen Unsloth Studio persistence/benchmark/plugin architecture and compare with other studios/runtimes;
4. derive PhenoLab target/objective/experiment-program requirements and journeys;
5. keep native VS-01 packages but mark them as infrastructure slices, not proof of whole-product thesis.
