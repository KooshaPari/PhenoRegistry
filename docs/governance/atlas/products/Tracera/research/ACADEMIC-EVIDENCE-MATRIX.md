# Tracera Academic Evidence Matrix — Agent Context, Trace Recovery and Closed-Loop Verification

**Date:** 2026-09-29.
**Status:** research evidence, not direct product proof.

| Work | Problem | Relevant result | Tracera implication |
|---|---|---|---|
| Repository Intelligence Graph (2026) | deterministic repository architecture context for coding agents | reported +12.2% mean accuracy and -53.9% completion time across evaluated agents/repos; larger multilingual gains | deterministic graph context can materially help agents; include comparable no-graph baseline in pilot |
| Agent Retrieval Bench (2026) | repository context retrieval | no single retrieval family dominates; logged trajectories miss all gold files on 27–35% of samples; oracle context leaves large headroom | product graph/context compiler must measure retrieval quality and abstention; graph presence alone is insufficient |
| SWE-Explore (2026) | agent repository exploration | line-level coverage and efficient ranking remain differentiators; exploration metrics track repair behavior | MACE should include context/retrieval efficiency where it affects work |
| TraceDev (2026) | requirement→design→code/test multi-agent traceability | heterogeneous traceability graph used as validator/context; reported substantial success-rate gains over evaluated baselines | direct adjacent competitor/research baseline for AgilePlus+Tracera loop; reproduce/compare methodology |
| Synergistic requirement→code RTLR (2026) | automated trace recovery | strong gains over baselines but strict cross-project recall only ~50.7%; prompt strategy matters greatly | inferred links remain uncertain; confidence/authority and benchmark precision/recall are mandatory |
| ML traceability SLR (2025) | automated software traceability literature | 59 studies/170 datasets; data scarcity, imbalance, missing true links and benchmark limitations remain key gaps | do not claim universal auto-trace; build benchmark corpus and human-reviewed sample |
| Code Gradients (2024) | tracing LLM-generated code to requirements | preliminary gradient-based trace/rewrite loop | generation-time provenance may supplement post-hoc link recovery; investigate where model APIs permit |
| Requirements→Code developer study (2025) | how developers use requirements with LLM coding | requirements often too abstract; developers decompose tasks and add design/architecture context | reinforces AgilePlus context compiler/spec decomposition role |
| LLM unit-test context study (2026) | automated test generation | behavioral/docstring context materially improved coverage/compilation; richer sequential prompting improved mutation score at higher cost | acceptance/behavior context quality matters to grader/test generation; pilot cost-quality tradeoff |
| Closed-loop embedded-agent evaluation (2026) | iterative coding agents with build/test/repair feedback | evaluates multiple feedback regimes across hundreds of runs | MACE should benchmark feedback regime, not just final model |
| Verification-evasion taxonomy (2026) | agent behavior under verification pressure | identifies patterns such as unsupported completion claims/placeholders/stopping behavior | direct anti-Goodhart/MACE input; grader must require machine evidence and detect evasion |

## Research decisions

1. Add retrieval/context quality as a measurable subproblem, not assume perfect graph-to-agent context.
2. Benchmark inferred trace links with precision/recall/F1 and abstention/calibration.
3. Preserve deterministic source extraction separately from probabilistic semantic links.
4. Compare Tracera context against no-graph, lexical, embedding, repo-map and oracle-context baselines where feasible.
5. Compare MACE feedback regimes and cost, not only final pass rate.
6. Include verification-evasion detectors/negative controls in AgilePlus grader research.
7. Study TraceDev as a direct academic adjacent architecture rather than only commercial competitors.
