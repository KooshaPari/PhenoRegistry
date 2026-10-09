# Tracera + AgilePlus Locked-Pair Forward Program

**Date:** 2026-09-30  
**Status:** active; no completion claim.

## Tracera — immediate technical critical path

### T1. Dependency-footprint soundness
Complete EXP-11:
- deterministic vs accepted vs inferred dependencies;
- false-negative controls;
- generated artifacts;
- dynamic config/flags;
- stale indexes;
- certificate revocation;
- transitive invalidation;
- provenance/version binding.

Exit:
an inferred absence cannot establish independence.

### T2. Suspect/invalidation propagation
Define and test:
- endpoint revision change;
- relation remains physically present but becomes suspect;
- evidence invalidation;
- configuration-specific impact;
- certificate revocation fanout;
- revalidation and restoration;
- historical evidence preservation.

### T3. Real current-Rust witness
Before code correction:
- two products;
- overlapping capability labels;
- distinct baselines;
- conflicting evidence;
- fixed evaluation time.

Observe real current behavior of assessment/query helpers.

Then repair/refine only based on evidence.

### T4. Vertical slice VS-01..VS-04
- typed identities/repository contract;
- SQLite persistence/restart;
- PostgreSQL semantic parity;
- exhaustive assessment truth table.

### T5. Mount the product
- narrow product-native HTTP API;
- explicit invalid input;
- exact snapshot vs historical query;
- bounded product graph;
- product assessment.

### T6. Cross-layer trace
Bridge product obligations into SWEE/code/test/evidence without making SWEE the full ontology.

### T7. Human projection
Recover useful existing Featuregraph/PageDecomposition/GraphView work.

Mount it against canonical product state.

Do not treat mock/local renderer state as product truth.

### T8. Work boundary
Link one AgilePlus/external durable work effort.

Close it.

Prove Tracera remains non-green until qualifying evidence arrives.

### T9. Reverify
New candidate/configuration evidence changes current product state while prior proof remains historical.

### T10. MCP parity
Expose the same application semantics through MCP.

No second source of product truth.

## Tracera — semantic/documentation program

In parallel:
- finish source ledger;
- raw-intent index;
- Genesis provenance;
- SOTA subtree;
- architecture/ontology subtree;
- decisions/supersession;
- semantic requirement decomposition;
- journey/stage derivation;
- current-state bulkhead;
- fresh recovery tests.

Only let architecture experiments feed accepted ontology/requirements after review.

## AgilePlus — full deep pass

### A1. Internal archaeology
Search:
- AgilePlus;
- older project/spec/workflow names;
- prior discussions on SDD;
- agent workflow;
- WBS/DAG;
- assignments;
- orchestration;
- claims;
- worktrees;
- graders;
- MACE;
- related repos.

### A2. SOTA methodology teardown
At minimum:
- OpenSpec;
- Spec Kit;
- BMAD;
- Kiro;
- Tessl;
- Spec Kitty;
- GSD;
- Ralph loops;
- Superpowers/skills;
- coding harnesses;
- agent orchestration;
- context retrieval;
- autograder systems.

For each behavior:
KEEP / ADAPT / MERGE / CONDITIONAL / REJECT.

### A3. Adaptive-depth compiler
Derive rigor from:
- complexity;
- risk;
- novelty;
- uncertainty;
- blast radius;
- reversibility;
- security;
- migration;
- number of affected systems.

### A4. Durable development model
Explicitly distinguish:
- DevelopmentId;
- AttemptId;
- worker identity;
- claim/lease;
- branch/worktree;
- accepted spec revision;
- result/evidence.

### A5. Assignment ontology
Each assignment can carry:
- objective;
- rationale;
- prerequisites;
- requirements/scenarios;
- invariants;
- allowed/forbidden surfaces;
- dependencies;
- fixtures;
- oracle;
- evidence;
- rubric;
- retry;
- escalation.

### A6. Context compiler
Generate minimum sufficient next context from:
- accepted assignment;
- repo/product graph;
- architecture decisions;
- relevant files;
- current failures;
- prior attempts;
- policy snapshot.

### A7. Execution topology

```text
durable development effort
 → work DAG/frontier
 → lease/claim
 → worker attempt
 → independent grade
 → retry / replan / spec revision / HITL
```

### A8. MACE short loop
Preserve:
- verified sub-results;
- failure classification;
- progress trajectory;
- regression;
- grader identity;
- exact candidate;
- anti-Goodhart protection.

### A9. Specification evolution
No prompt drift.

Explicit:
- proposed spec change;
- accepted revision;
- supersession;
- impact;
- changed grader/criteria.

### A10. Tracera boundary
AgilePlus returns:
- execution state;
- artifacts;
- receipts;
- evidence references.

It cannot mutate Tracera accepted product truth merely by saying Done.

### A11. Real vertical witness
One durable effort:
- worker A starts;
- attempt fails/dies;
- worker B continues;
- prior verified work preserved;
- invalid lease not inherited;
- final evidence produced;
- work completed.

### A12. Comprehensive semantic contract
Then derive:
- hierarchy;
- requirements;
- journeys;
- stages;
- implementation mapping;
- oracle design;
- dossiers;
- red-team completion gate.

## Shared pair E2E gate

Run:

```text
Tracera dissatisfaction / ProductChange
        ↓
AgilePlus DevelopmentId
        ↓
Attempt A
        × fails/dies
Attempt B
        ↓
artifact + evidence
        ↓
AgilePlus work complete
        ↓
Tracera independent assessment
        ↓
accepted/rejected/reverified product state
```

Adversarial cases:
- stale evidence;
- conflicting evidence;
- wrong configuration;
- wrong baseline;
- wrong candidate;
- work complete but no proof;
- scope revision mid-work;
- grader revision;
- rejected product realization;
- partial rollout;
- rollback;
- agent replacement;
- restart;
- dependency change.

## Shared governance track

Allowed in parallel because it is not a third product:
- portfolio constitution archaeology;
- policy lineage;
- repo profile resolution;
- CI/toolchain standards;
- Git ledger policy;
- documentation standards;
- drift inventory.

## Final gate

Do not leave the pair until:
- research is sufficient to defend architecture;
- source coverage closes;
- mature semantic contracts close;
- vertical witnesses pass;
- traceability is valid;
- documentation is recovery-grade;
- fresh human/agent recovery succeeds;
- red-team review has zero blocking findings;
- PhenoRegistry and repo-local truth agree.
