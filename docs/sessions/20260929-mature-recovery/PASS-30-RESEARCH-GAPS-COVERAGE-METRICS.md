# Pass 30 — research-gap closure + source metrics

Date 2026-09-30.

## PhenoLab statistical/causal methodology

Receipt `f5b74c6a73943a4c3ea5f0744ac06720fe72b0db`.

The doctrine now separates:
1. replacement decision;
2. effect estimation/uncertainty;
3. causal attribution.

A multi-layer candidate may be a valid replacement while causal attribution remains UNKNOWN. Replicates must declare experimental unit, dependence, stopping policy and failed runs; adaptive optimizer search creates winner's-curse/holdout risks; environment drift can force rebaseline/incomparability. No single statistical test is hard-coded across all experiment types.

This closes a major conceptual gap in L-OB-031/032/037 while implementation remains open.

## PhenoMLX engine matrix

Receipt `45f4e2b79cacd60b76a29fa97d94eb7610de94ee`.

Current external evidence (2026-09-30) confirms active mature baselines:
- vLLM current releases list v0.30.0; Apache-2.0.
- SGLang releases list v0.5.20; Apache-2.0.
- TensorRT-LLM active 2026 source, package marked Beta; Apache-2.0 with bundled third-party notices.
- llama.cpp continuous release/build stream, broad platforms; MIT.
- MLX-LM current release list includes v0.31.3; MIT.
- oMLX active Sept 2026, project Alpha, pins MLX 0.32.2/nanobind ABI; Apache-2.0.

These are bootstrap/health facts, not profile qualification. Exact VS-01 versions must be captured at runtime.

## Source-coverage metrics

Closed-family fractions are now machine-readable and explicitly **not product completion**:

- Portage: 4/16 CLOSED = 25.0%; 6 HIGH-but-not-closed; 5 partial/open; 1 bounded unavailable. Receipt `4d51c2aa5e6016181a1ebdbf3de4b34c2300b1c2`.
- PhenoMLX: 2/15 CLOSED = 13.3%; 6 HIGH-but-not-closed; 6 partial/open; 1 bounded unavailable. Receipt `1c92c2034a810d3311e4795958ab622b422341d7`.
- PhenoLab: 6/17 CLOSED = 35.3%; 5 HIGH-but-not-closed; 5 partial/open; 1 bounded unavailable. Receipt `7e9c41e8b3902a65be68af9c7d22c7c2ce566dc6`.

Only CLOSED participates in the numerator. These low fractions are expected under the strict definition and demonstrate why prior “we inspected most things” language is not a completion metric.

## Next

1. use the metrics to target closure rather than inflate counts;
2. Portage: package/install authority + semantic fork delta;
3. PhenoMLX: current profile persistence/request lifecycle + exact two-engine runtime evidence;
4. PhenoLab: durable store/API/UI + statistical doctrine machine schema/oracles;
5. continue current cross-repo API inspection where evidence exists;
6. VS-01 native experiments remain the baseline promotion gate.
