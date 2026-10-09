# Pass 41 — vNext obligations, primitive/gap matrices, product-vs-infra gate

Date 2026-09-30.

## vNext capability deltas
Portage `dee9924249cba8f8be89049e94529447c48a9421`: 15 portability-specific obligations.
PhenoMLX `592f9785ee3fcf52ebb11603302276a10c1f4651`: 15 research-runtime obligations.
PhenoLab `c2c3aeee2ca93fa93a8a8174c496891871c8d1d4`: 16 target-program obligations.

Counts are decomposition outputs only.

PhenoLab ExperimentProgram schema `2dfcf6afc23fa53f6e44552c5bc7743ca2e8d812` now encodes model/harness/workload, objective roles/target forms, durable budget, baseline gap and allowed intervention/stop policy.

## Portage backend primitive matrix
Receipt `d435d806b196d23dcd5f2b2eb464a89899e49713`.

Current Harbor BaseEnvironment already supplies a substantial backend abstraction and capability validation. Apple Container proves ARM64/Apple-Silicon support exists, but still consumes Dockerfile/image semantics. Modal direct mode uses provider sandbox execution yet materializes from Dockerfile/registry; multi-container uses DinD Compose.

The likely remaining original-intent gap is therefore narrower and more precise:
**substrate-neutral TaskEnvironmentDefinition/materialization + native/bare-metal/non-Docker adapters**, not wholesale replacement of BaseEnvironment.

EXP-P1 should attempt this through Harbor extension seams first.

## PhenoMLX Unsloth gap ledger
Receipt `b0b6a6fc3c14ffb30e822f8ea9b0c2373e1dbf45`.

Studio is stronger prior art than earlier assumed: persistent subprocess orchestration, cross-backend packaging, requested/applied state, speculative modes, MLX KV/TurboQuant, VRAM coordination and side-by-side comparison.

A concrete open gap exists: September 2026 Unsloth issue requests speculative target/draft acceptance-rate measurement because current serving cannot tell whether a draft is worthwhile before deployment. This is a strong candidate EXP-M1 research question: predict/measure acceptance and expected speedup, then validate against realized serving.

Other candidate gaps (experiment history, arbitrary hypothesis harness, cross-engine mechanism comparability, negative-result retention) remain to be falsified against deeper Studio source.

Studio code inspected is AGPL-3.0, so architecture learning and direct reuse have different licensing implications.

## Infrastructure vs product gate
Portage `fe7f35996e547f33b3826f9c5d39a910255e55cd`.
PhenoMLX `3b1bc779a6058ff426f2763acbe5848e74e0655f`.
PhenoLab `5d048e701913d26a78dbf7b2d79f028a4c2a9632`.

Infrastructure readiness and product-thesis validation are now independent gate dimensions. A perfect INFRA-01 can only yield INFRA_READY_PRODUCT_UNVALIDATED until EXP-P1/M1/L1 executes.

## Next
1. machine-trace the vNext obligations to EXP/INFRA evidence;
2. Portage TaskEnvironmentDefinition schema + conformance oracle;
3. PhenoMLX EXP-M1 speculative-qualification experiment schema;
4. PhenoLab InterventionSet + progress/distance-to-target schema/oracles;
5. deepen Unsloth experiment persistence/history falsification;
6. recover DeepSea fork alias/delta.
