# SOTA pass 2 — academic evidence matrix

Retrieved 2026-09-29. **Abstract-level screening only; paper methods/code/data review remains OPEN.** Numeric claims below are attributed to authors and are not current comparative results for either owned repository. No PDF was analyzed in this pass.

| Paper / exact version and inspected extent | Task; dataset; sample | Baseline; metric; evaluator | What it supports / does not establish | Decision consequence |
|---|---|---|---|---|
| [SWE-bench, arXiv:2310.06770](https://arxiv.org/abs/2310.06770), original 2023 abstract; revision-specific methods not inspected | Edit a repository to resolve an issue; 2,294 issue/PR problems across 12 Python repositories | Abstract reports proprietary models and SWE-Llama; issue resolution fraction; detailed evaluator protocol not inspected | Supports repository-level outcome tasks as prior art. Does not prove cross-platform shell correctness, long-running daemon recovery, our provider behavior or current model ranking | LEARN/ADAPT task construction; inspect tests, environments, contamination and task applicability before importing |
| [SWE-Proof, arXiv:2609.21190v2](https://arxiv.org/abs/2609.21190v2), revised 2026-09-22, abstract and version metadata | Formally qualify real coding issues using known correct patches; 500 SWE-bench Verified issues | v2 describes Claude Opus 4.8 with/without specification assistance; formally qualified resolution; generated specifications, callee axioms, mechanical/adversarial admission | Authors report specification faithfulness problems. Does not establish that generated specifications express this user's full mature contract, or that axioms/evaluation transfer to our runtime/platform cases | LEARN FROM adversarial specification audit; examine methods, axioms and independent evaluation before any formal-verification adoption |

## Version discipline

The unversioned SWE-Proof search excerpt differed from the opened v2 abstract in model scope and reported audit rates. The retained reference is explicitly v2; no mixed-version headline numbers are used as a decision premise. This is a concrete reminder that evidence must bind the exact evaluator/paper revision, not just its title.

## Required next screening fields

For each retained paper, resolve exact task/dataset and exclusions, experimental sample size, baselines and configurations, metric definition, evaluator independence, repetition/variance, threats to validity, artifact availability/license and replication cost. Mark absent information unknown rather than supplying guesses. Separate benchmark design evidence from evidence that our architecture or product thesis works.

## Open literature coverage

Terminal and multi-language agent benchmarks; process supervision and crash consistency; adversarial/mutation and metamorphic tests; formal specification faithfulness; long-horizon agent evaluation; tool authorization; memory/state reconstruction; human usability and intervention measurement. No literature-completeness claim is made.
