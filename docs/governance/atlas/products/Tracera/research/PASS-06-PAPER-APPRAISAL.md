# Four research claims, qualified

**Status:** primary-text review, not replication. September 29, 2026.
Source IDs and exact versions resolve in [PASS-06-EVIDENCE.json](PASS-06-EVIDENCE.json).

## P1 — Repository Intelligence Graph, arXiv:2601.10112v1

The experiment uses three agents, eight repositories and thirty structural questions per repository. Seven repositories are synthetic; MetaFFI is the real system. Automatic extraction is CMake-specific; other build-system graphs were manually authored. The reported 12.2% accuracy improvement is relative, not percentage points. Time measures the question-answering task, not general feature delivery. Repetition is insufficient for tight confidence intervals.

**Transfer:** represent build/test topology with source evidence; use the paper as a comprehension-baseline design. **Do not transfer:** its headline improvement as Tracera productivity or a claim of ready-made automatic Cargo/npm extraction. The paper links GreenFuze/Spade; code replication remains open.

## P2 — Agent Retrieval Bench, arXiv:2607.24882v1

The diagnostic corpus has 427 samples across 25 repositories, including natural no-gold cases and wrong-repository controls. Retrieval-family rankings depend on task, budget and weighting. File-level exposure is not useful-span localization. The corpus is uneven; Gin supplies 25.5% of positive samples. Main results do not measure patch generation; a seed pilot has one trajectory per sample/arm and no confidence intervals.

**Transfer:** measure budgeted retrieval, abstention and wrong-repository controls separately. **Do not transfer:** Recall@k into accepted-work success or assume an embedding/repo-map family is universally best. Keep lexical and structure-based baselines.

## P3 — TraceDev, arXiv:2607.18886v1

This is direct architectural prior art: a validator builds requirement/design/code links and feeds missing-link feedback into bounded refinement loops. Evaluation covers eTour and SMOS: 125 use cases. Tests are generated with access to use cases and reference code, then filtered to pass on that code. Semantic coverage uses LLM judging; the baselines are ChatDev and MetaGPT, not a complete 2026 product comparison.

**Transfer:** targeted trace-gap feedback and the artifact graph. **Do not transfer:** majority-vote semantic judging as independent acceptance, code volume as quality, or relative improvements as proof of universal superiority. A Tracera pilot needs curated negative controls and independent holdout oracles.

## P4 — TVR, arXiv:2504.15427v1

The work evaluates stakeholder-to-system requirement validation/recovery on automotive diagnostic trouble-code requirements. Its retrieval database contains engineer-verified pairs. Generalization therefore depends on domain and retrieved-label quality, and the authors identify annotation error and external-validity limits.

**Transfer:** separate validating existing links from recovering missing ones; retain explanations and reviewed examples. **Do not transfer:** domain accuracy into whole-product graph correctness or omit the cost of obtaining/maintaining the human-confirmed retrieval corpus.

## Shared pilot amendments — proposed

Freeze repository snapshots, prompts, models, budgets and grader versions. Separate extraction fidelity, inferred-link precision/recall, context quality, task acceptance, durable regression behavior and ongoing human maintenance. Include source-native/lexical/structural alternatives, not only an intentionally weak no-context agent. Count model bootstrapping, indexing, failed runs and reviewer time in cost. Predeclare adjudication for disputed links and deliberately wrong evidence. Report failures and abstentions, not only successful examples.

These four reviews do not close the rest of the earlier academic matrix. Unreviewed or unavailable artifacts stay unresolved rather than inheriting credibility from adjacent citations.
