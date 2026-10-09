# Pass 27 — VS-02 schemas, v2 oracle matrices, ownership closure

Date 2026-09-30.

## VS-02 schema-only work

Permitted by the slice DAG and now committed:

- Portage schema `32c66b04fc1b278c82798f8402505c613c6fc565`: subject/export schema versions, migration policy, redaction tombstone refs and Harbor compatibility state.
- PhenoMLX `ec39d89abab4f872b3041fbb31b4aaba983cd8b1`: capability state + authority/version/model scope, exact model/tokenizer/template compatibility and fallback policy.
- PhenoLab `dbdc8630f13305aedfa1eae7f371f45b65d0da2d`: EvaluationReport compatibility, intended intervention vs dirty paths, baseline freshness, uncertainty/incomparability and feedback authority.

No runtime-dependent VS-02 claim is made.

## V2 oracle matrices

Portage `624c480c61471000b67a3325c9970bb8ad06753a`.
PhenoMLX `f6fb6d1497b55ab59d06fa0e133df2ced7edc837`.
PhenoLab `ff101077440029fc3ccad721cc4f9264c3867a1c`.

Every newly added mature obligation now has positive, negative/adversarial and mutation-style oracle ideas plus required evidence class. This enables future test generation from the semantic graph rather than implementation-shaped assertions.

## Ownership source closure

Recovered historical ecosystem context strengthens two previously provisional boundaries.

### PhenoMLX
Historical architecture repeatedly treats hwLedger as the resource/capacity oracle (VRAM/GPU/KV/bandwidth/TTFT/throughput/cache/thermal/power/fleet economics), with runtime/router layers consuming infrastructure facts. This supports hwLedger hardware truth → PhenoMLX LLM runtime qualification → routing selection.

Receipt `5487cb09a56d708da59ddca4f02e3bf89ef51ff8`.

Still require current hwLedger/OmniRoute schema inspection before CLOSED.

### PhenoLab / Tracera
Historical user constraints and architecture strongly place Tracera as canonical evidence/acceptance/provenance/product graph while sibling execution systems remain separate. This supports PhenoLab experimental truth → explicit PromotionRecord/Application → Tracera canonical product truth, without silent capability import.

Receipt `c34b1172c95cea027214a90a64d8cf67315a1ac2`.

Ownership principle is HIGH confidence/source support; concrete current bridge remains OPEN.

## Next

1. machine-trace v2 obligations and connect them to slice DAG nodes;
2. produce schema migration/compatibility fixtures for the allowed VS-02 work;
3. inspect current hwLedger/OmniRoute and Tracera integration schemas if accessible through repo context;
4. continue statistical/causal research for PhenoLab and engine license/health/version matrix for PhenoMLX;
5. keep runtime-dependent implementation gated.
