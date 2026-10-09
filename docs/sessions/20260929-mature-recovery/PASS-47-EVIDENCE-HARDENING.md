# Pass 47 — evidence-hardening for EXP-L1 and EXP-M1

Date 2026-10-01.

## PhenoMLX true speculative TrialReceipt
Schema `3410abbb4dd60be977cfc76837e70d072ec611a1`.
Adversarial tests `a8535380a9868ebd66d0af3fd7225320c94f94ff`.
Telemetry hook map `0a38ef3bff376e56cbd62cf2f000a5268fd8cc99`.

Qualifying evidence now requires runtime activation proof plus measured proposed/accepted token counts and quality pass. Startup flags or throughput uplift alone cannot manufacture acceptance. Unknown engine fields remain null/unknown.

Collector order: custom/MLX direct counters → one instrumentable serving engine → second engine → broad adapters.

## PhenoLab baseline integrity and target freeze
Population tests `ef51ca77f1817ed5d8b885a1900b5b59b13ac563`.
Target-freeze algorithm `a029cc780ad9e0baa7b5f34fa8c3e53ae974c276`.

Header/manifest/raw-row/aggregate n must agree. Target is frozen only after valid baseline, using distribution/uncertainty + minimum practically relevant improvement and current alternatives. Candidate observations cannot set or relax the target. Target changes create a new epoch/program revision.

## Experiment-boundary consequence
The historical Qwen n-gram negative control is useful precisely because it stays negative. The lab must retain it; the runtime layer must explain whether the method was actually active before interpreting performance.

## Next
1. define a concrete TrialReceipt instrumentation work unit for the MLX/custom path;
2. define baseline-run work unit for Qwen3.5-0.8B;
3. add Portage portable-task conformance receipt and P1-C0/C1 execution work units;
4. runtime execution still depends on suitable hosts/backends.
