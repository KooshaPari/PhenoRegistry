# Pass 43 — product experiment adversaries and non-toy subjects

Date 2026-09-30.

## Adversarial experiment fixtures
Portage `441b38ebedd37a19ee300ebcff7ea9806d945b7e`: missing primitive fail-fast, materializer != task identity, native isolation truthfulness, backend-specific task edits as portability debt.

PhenoMLX `7e455adae06dcdb7f0e8888c477a8e8d510c9cac`: quality regression beats speedup, bad prediction falsifies hypothesis, practically insignificant speedup rejected, negative drafter pair retained.

PhenoLab `8cdf766016c1d818dfbb29beaa69f0a0ed67b1be`: budget-exhausted failure is valid termination, worker replacement preserves budget/target, one observation yields no velocity/confidence, failed intervention retained.

## Non-toy experiment subjects
Candidate subject receipt committed to all three:
Portage `66462be7ad14e0e35ccfc88bda01a2d925834445`.
PhenoLab `244f20410a76e4e5155bcbe7e3f8e6c7e99235dd`.
PhenoMLX `e83e67ecd98eeda7f1a51cda09305631d5ccc761`.

Portage primary probe: an existing meaningful Harbor task on Docker/reference vs Apple Container ARM64. This is valuable because Apple Container is a real different runtime but still consumes Dockerfile/image semantics, directly probing the suspected materialization debt. Native/bare-metal remains the stronger secondary test.

PhenoLab primary: pinned Qwen3.5-0.8B + existing stock-vs-ours/performance harness. Repo already has real comparison/perf machinery and documented non-comparability/failures, making it a non-toy target-driven R&D program. Freeze target only after baseline evidence; prefer quality non-inferiority + meaningful runtime/resource improvement.

PhenoMLX: speculative qualification can likely use Qwen-family work but exact target/drafter must follow backend support/runnable evidence.

## DeepSea
Portage receipt `d4d2e5b4dc94911b940a9e3efaa9000c983f5b1a`.

Current Portage/Registry text search for DeepSea/deepsea/"Deep Sea" recovered no alias. Identity remains UNKNOWN/OPEN; no repo is guessed. Closure should use conversation memory, historical remotes/merge commits/deleted registry or user recollection if necessary.

## Next
1. use personal-context/conversation archaeology specifically for DeepSea alias and original Portage portability discussions;
2. identify exact existing Harbor task suitable for Apple Container probe;
3. derive Qwen baseline evidence and freeze a defensible EXP-L1 target;
4. select runnable target/drafter for EXP-M1 from supported speculative paths;
5. do not execute until environment/evidence prerequisites are available.
