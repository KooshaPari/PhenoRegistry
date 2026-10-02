# Academic evidence — pass 1, methods qualification open

Read date 2026-09-29. A paper title, abstract, benchmark headline or source docstring does not qualify a product claim. Empty fields below mean uninspected, not zero or not applicable.

## GEPA

Source: https://arxiv.org/abs/2507.19457v2 . Exact version: arXiv 2507.19457v2, revised 2026-02-14. Title: GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning. Inspected extent: abstract and bibliographic record. Full HTML retrieval attempt for v1 exceeded tool response size; full methods and appendices have not been reviewed.

| Required field | What is known / limit |
|---|---|
| Task | Reflective optimization of one or more prompts in an LLM system; broader product transfer unestablished |
| Dataset | Abstract mentions AIME-2025 and six evaluated tasks; complete datasets/versions not inspected |
| Sample size | Per-task and total examples, seeds and trial counts uninspected; six tasks is not sample size |
| Baseline | Abstract names GRPO and MIPROv2; exact configurations/budgets not inspected |
| Metric | Task-dependent reported quality/accuracy and rollout use; definitions/uncertainty not inspected |
| Evaluator | Exact scoring implementations and independent validation not inspected |
| Limitations | Full limitations, contamination/holdout, model dependence and variance uninspected |
| Establishes here | A credible existing method to investigate before hand-rolling reflective prompt optimization |
| Does not establish | Performance for this user's full model/harness/tool/memory/guardrail/topology/kernel system or superior product outcomes |
| Decision | Candidate bootstrap/research lead only; no numerical gain imported into PhenoLab forecasts |

## Required follow-up literature families

Portage: agent evaluation validity, task isolation, benchmark contamination, trajectory standards, reproducibility and negative-control design. PhenoMLX: current KV representations, quantization quality, fused attention/dequantization, hybrid recurrent/attention state and real allocation/concurrency accounting. PhenoLab: reflective/constrained optimization, agent-system configuration search, causal experiment design, held-out acceptance, evaluator calibration and reward gaming.

For every accepted research result add exact task, data revision/sample size, baseline, metric, evaluator, limitations, inspected sections, independent replication status and consequence for a specific product/profile. Native product measurements belong in their own evidence register, not relabelled as peer-reviewed research. Research-family coverage remains open.
