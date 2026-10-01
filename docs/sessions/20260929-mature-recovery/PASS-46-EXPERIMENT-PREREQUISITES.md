# Pass 46 — baseline manifest, speculative instrumentation gap, ARM64 feasibility

Date 2026-10-01.

## PhenoLab fresh baseline manifest
Receipt 2c838c6f6619af7aa00174b578c20546dd474cf3.

Machine schema now requires exact model/tokenizer, harness commit/config, runtime version/effective config, hardware/environment, population digest with declared_n == evidence-consistent observed_n, raw runs and live-verified non-synthetic evidence. This directly prevents the historical run-v5 population mismatch from recurring.

## PhenoMLX speculative instrumentation gap
Receipt a605f4615d50e49cad56304e9bbf38a74c3646d4.

Existing PhenoLab specdec_trial.py is reusable orchestration but not qualifying telemetry:
- n-gram is explicitly indirect and changes prompt;
- EAGLE/MTP trials assume engine-side activation;
- no method-active proof, true accepted/proposed counts, draft/verify timing, quality/resource evidence or exact build/profile identity.

PhenoMLX should provide the richer runtime TrialReceipt; PhenoLab consumes it.

Existing measured negative control is useful: qwen35_ngram_simple_3090 has equal output hashes but baseline ~106.86 tok/s vs ngram ~103.75 tok/s. Retain as negative learning, not product success.

## Portage ARM64 feasibility
Receipt 9c2c07b4e7846abebe381eaca892a82832b1a3c9.

C0 reward-kit environment has no obvious task-source ISA pin; actual Ubuntu/uv image manifests still need runtime verification.

C1 DeepSWE tomlkit semantic workload is Python/pinned source; likely portability risk is the prebuilt ECR/base image architecture. If x86-only, rebuild arm64-equivalent environment from source recipe and record debt. Any required semantic dependency/test change is evidence against transparent portability.

## DeepSea
No additional identity evidence this pass.

## Next
1. add population-consistency and speculative TrialReceipt schemas/tests;
2. inspect image manifests at runtime/web if accessible;
3. derive exact baseline target-freeze algorithm from fresh Qwen evidence;
4. identify engine telemetry hooks for accepted/proposed speculative tokens;
5. continue peer-fork history only with provenance.
