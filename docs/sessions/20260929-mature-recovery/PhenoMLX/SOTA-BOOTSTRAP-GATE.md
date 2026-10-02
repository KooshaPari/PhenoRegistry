# PhenoMLX — SOTA/bootstrap pass 1

Observed 2026-09-29; target source `1ab4ed250e6b3a1ed9025a674d4814339d32fcd3`. **Architecture/existence gate OPEN.** External descriptions are current documentation reads, not pinned installed builds or independent benchmarks.

## Realistic absence stack

For an accepted Apple profile: upstream oMLX over MLX-LM, or MLX-LM directly where its library/CLI is sufficient. For a non-Apple profile: compare an appropriate established engine such as llama.cpp; the broader engines named by repo policy require their own supported-profile study. Existing experiment tooling supplies qualification. Do not force all profiles through one engine merely to make a simple comparison table.

| Capability / primary source | Inspected evidence | Bootstrap disposition under review | Open technical costs |
|---|---|---|---|
| Serving/admin/cache: https://github.com/jundot/omlx | README documents batching, tiered KV caching, model management and app/admin surfaces | USE DIRECTLY / INTEGRATE; FORK only for a demonstrated delta | Actual fork ancestor, compatible app/CLI/extension protocol, build/profile support, license notices and upgrade/rollback |
| Generation and adaptation: https://github.com/ml-explore/mlx-lm | README describes generation/streaming, fine-tuning, prompt caching and cache/prefill tradeoffs | USE DIRECTLY or ADAPT extension points before custom runtime code | Correct model/tokenizer/quantization, cache lifecycle, quality/memory tradeoffs and API/version drift |
| Other engine profiles: https://github.com/ggml-org/llama.cpp | Repository discovery; mechanism/compatibility study incomplete | Candidate COMPOSE alternative, not a certified replacement | Hardware/model support, runtime lifecycle, resource accounting, interoperability and maintenance |
| CUDA block cache: target latest commit and byte_breakdown report | Source-recorded full-allocation result contradicts a memory-saving interpretation for one profile | REJECT a saving/speedup claim for that recorded implementation/profile; preserve experiment | Raw run custody, reproduction, quality gate and full allocation/performance controls |
| Fused kernel or new cache core | No justified custom implementation decision in this pass | BUILD CUSTOM only after profiling and attainable end-to-end benefit; LEARN FROM existing methods first | Existing primitive coverage, integration complexity, driver/runtime portability and enduring maintenance |

## Differentiation ledger

Commodity/contested: a local inference server, model selector, prompt cache, administrator UI or microbenchmark viewer alone. Falsified for the source-recorded CUDA profile: interpreting packed bytes as total resident savings while retaining the entire decoded prefix. Candidate differentiation: a narrowly qualified extension with real quality/resource or workflow advantage. Unverified: cross-engine performance, broad support, reliable deployment, superiority of custom kernels and long-context/concurrency gains. One negative experiment is not a verdict on the whole product.

The root MIT/current upstream Apache-2.0 labels trigger ancestor/file-notice inspection; they are not sufficient to allege a license violation. Alternative project health, exact versions, security, integration/operating cost and any commercial comparison remain open.

Next passes: full model/backend/kernel/state map; current native cache/attention primitives and literature; matched cold/warm and quality controls; clean-install/upgrade behavior; raw benchmark methods and license provenance. Repo experiments M-X01 through M-X05 are specified but not executed natively. No performance envelope or mature contract is frozen.
