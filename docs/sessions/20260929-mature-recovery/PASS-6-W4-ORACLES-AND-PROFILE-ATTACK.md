# Pass 6 — W4 oracle witnesses and PhenoMLX profile attack

Date 2026-09-29.

## PhenoLab native-source oracle witnesses

Specification branch now contains `tests/recovery/test_mature_recovery_oracles.py` at commit `92f47286fcd76080fff08c74f96a858550cac7d9`, with strict expected-failure witnesses for:
- empty suite accepted as passed;
- success→exception stale-result reuse;
- configured verifier bypass;
- missing/blank reference heuristic acceptance;
- unknown verifier silently falling back to heuristic.

The strongest implementation finding is structural: current TournamentRunner stores `self.verifier` but its “L2 Verify” block reduces task statuses directly and does not call the configured verifier.

These tests are committed native-source oracles, **not executed native evidence**. No new commit-associated Actions run was returned immediately; existing PR CI has a pre-step infrastructure blocker.

Detailed receipt: PhenoLab `31dcebed9b8cc2e67d514b766b06dcd5854b2b4a`.

## Portage native-source reward oracles

Specification branch now contains `tests/recovery/test_mature_recovery_reward_oracles.py` at commit `4cb72d590279eac7ecd603aca23510177ca8d345`.

Strict xfail witnesses cover empty reward map and accidental bool-as-number semantics. Positive controls preserve rejection of non-finite and string rewards. They call the real parser method with a real temporary reward file but do not execute provider/environment/job consumers.

This is deliberately narrower than the product oracle. Required-artifact failure, regrade identity, cross-candidate replay and terminal presentation remain W4 work.

Detailed receipt: Portage `6abe78a8175762d6ab30c685ae7ee56de4c20dc6`.

## PhenoMLX cache/profile SOTA attack

Current MLX-LM already exposes prompt-cache persistence and KV quantization controls. Current vLLM exposes hybrid cache groups, group-aware capacity/concurrency, automatic prefix caching, cache isolation salt, FP8 KV quantization, selective skip layers, CPU/tiered offload and hybrid/Mamba cache controls.

This falsifies generic “quantized/prefix/hybrid cache exists” as PhenoMLX differentiation and raises the burden on custom cache work. The source-recorded 1.375× Qwen3.5 cache result is especially important: storing packed state while retaining full decoded state is not a credible memory win merely because packed bytes are smaller.

The surviving PhenoMLX thesis is increasingly **qualified cross-engine runtime profiles + measured extensions**, not a universal homegrown cache/engine.

Detailed receipt: PhenoMLX `680381593ce01f487fd2dc2fd6582f908f0947fa`.

## Next critical execution

1. Get a runnable PhenoLab environment and execute the recovery tests before repair; preserve failing output.
2. Decide verifier authority/adaptation semantics, then repair separately.
3. Get Portage dependencies installable and execute parser witnesses; then trace required artifact/regrade to terminal acceptance.
4. Finish PhenoMLX SOTA across SGLang/TensorRT-LLM/llama.cpp and pin one realistic native comparison profile.
5. Only after these architecture-risk results freeze mature ontologies.

No production repair or merge was performed.
