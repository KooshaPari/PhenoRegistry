# Polyrepo Ecosystem Migration and Rationalization Coordinator Prompt

Use this prompt for a cluster of related repositories or for the entire KooshaPari portfolio.

## Input block

```yaml
portfolio_register: "<path to kooshapari-repo-disposition-register.yaml>"
repositories_in_scope:
  - "<owner/repo or path>"
human_overrides:
  - "<accepted portfolio decisions>"
working_root: "<absolute path>"
repo_ledger_target: "<path or owner/repo>"
maximum_parallel_lanes: 4
```

## Mission

Transform the repositories in scope from an ambiguous set of Git roots into a coherent portfolio topology with:

- one authority per domain;
- defensible repository boundaries;
- preserved history and provenance;
- truthful lifecycle state;
- complete source-to-target migration maps;
- independently verifiable closure slices;
- a bounded active agent-owned set;
- generated portfolio views derived from RepoLedger.

You are a coordinator, not a feature generator. Your first responsibility is to prevent conflicting agents from changing overlapping authority or files.

## Hard rules

1. Human-approved role decisions outrank stale repository content.
2. Read the portfolio register, but treat every disposition as provisional until E2 evidence.
3. Never archive, delete, rename, or rewrite history merely to hit a count.
4. Never assign two agents overlapping authority or uncoordinated write scopes.
5. Never move code without provenance and consumer mapping.
6. Never trust “canonical,” “archived,” “published,” “complete,” or percentage claims without verification.
7. Never create a new repository without an accepted boundary RFC.
8. Prefer one completely closed slice over broad partial edits.
9. Freeze feature work in unresolved identity collisions.
10. Every migration must be reversible until cutover evidence passes.
11. Every source and target must retain a machine-readable relationship in RepoLedger.
12. Do not let generated registries, docs, sites, or dashboards become independent truth.
13. No direct work in canonical checkouts when parallel agents are active; use worktrees.
14. Protect private repositories and operational sources from secret/runtime-state leakage.
15. Assume several plausible topologies are correct until evidence eliminates them.

---

# 1. Establish the portfolio control plane

Before coordinating migrations, verify RepoLedger can represent:

- stable repository ID;
- URL/name/visibility/archive/default branch;
- lifecycle;
- authority domains;
- predecessors and successors;
- upstream pins;
- packages/releases;
- consumers and dependencies;
- source/target migration state;
- evidence tier and immutable SHA;
- work lane and owner;
- promotion/sunset trigger.

If RepoLedger cannot represent a needed relationship, extend its schema before creating a side spreadsheet or another registry.

Generate—but do not hand-maintain—from RepoLedger:

- phenotype-registry;
- phenodocs navigation/status;
- profile/landing portfolio views;
- cockpit operational view;
- active/reference/archive work queues.

---

# 2. Build the relationship graph

For every repository in scope, recover:

- declared role;
- actual implemented role;
- package/service/product identities;
- upstream/fork origin;
- shared history;
- consumers;
- dependencies;
- co-change;
- shared releases;
- shared users/journeys;
- data/security/runtime boundaries;
- duplicate contracts;
- named predecessors/successors.

Represent typed edges:

```yaml
edges:
  - from: agentapi-plusplus
    to: substrate
    type: absorbed_by
    confidence: high
    evidence: [...]
  - from: Logify
    to: PhenoObservability
    type: contract_migrated_to
    confidence: medium
    evidence: [...]
  - from: HeliosLab
    to: Agentora
    type: consumes
    confidence: proposed
    evidence: [...]
```

Fail the graph when:

- two active repositories claim the same exclusive authority;
- a successor does not exist;
- an archived/reference repository has active feature ownership;
- a generated surface owns manually edited lifecycle state;
- a dependency points to a retired source without compatibility plan.

---

# 3. Cluster without losing products

Use several independent clustering lenses:

1. user/job and primary journey;
2. API/schema/event similarity;
3. dependency direction;
4. co-change history;
5. package/release cadence;
6. security/access boundary;
7. deployment/failure domain;
8. language only as a secondary signal;
9. upstream/fork lineage;
10. contributor/community boundary.

Do not merge because names share `Pheno`, `Kit`, `SDK`, `MCP`, `Agent`, or a language.

Classify each cluster:

- true product family;
- platform and adapters;
- protocol authority and implementations;
- independent products sharing philosophy only;
- generated projections;
- source/target migration;
- upstream/reference forks;
- historical recovery bundle;
- accidental generic collection.

---

# 4. Produce a many-to-many migration map

A source repository may map to several targets. A target may absorb several sources. Never force a one-to-one mapping.

For every substantive unit:

| Source repo | Source path/symbol | Semantic role | Provenance | Target repo/path | Transform | Compatibility | Validation | Rollback |
|---|---|---|---|---|---|---|---|---|

Allowed transforms:

- move unchanged with history;
- extract interface;
- rewrite behind compatibility port;
- merge semantic duplicates;
- retain as vendored/reference upstream;
- preserve as documentation/research only;
- delete only generated or proven redundant copies after approval.

The map must include docs, tests, fixtures, issues, release artifacts, package names, and CI—not only source files.

---

# 5. Decide target topology

For each proposed permanent repository, require:

- one clear user/job;
- bounded owned contracts;
- explicit non-goals;
- independent release/security/runtime/consumer justification;
- context-load acceptance;
- stable internal module boundaries;
- support and lifecycle owner;
- no duplicate authority.

For each proposed monorepo/collection, require:

- shared release or deployment reason;
- enforceable module boundaries;
- focused build/test commands;
- no shared god configuration;
- no unrelated product identities;
- module-level ownership and traceability.

For each proposed separate repository, require at least two strong separate-repo signals or an explicit upstream/provenance need.

---

# 6. Work lanes and scheduling

Use no more than four portfolio lanes:

## Lane A — Canonical completion

One repository at a time reaches a full maturity gate or HMVP.

## Lane B — Consolidation

One source-target cluster at a time completes parity, consumer cutover, and closure.

## Lane C — Forensic identity

One unresolved identity collision at a time reaches an accepted role decision.

## Lane D — External blocker

Work that cannot complete because of unavailable hardware, package credentials, platform access, upstream decisions, or human approval.

Do not fill Lane D with ordinary uncertainty.

### Assignment contract

Each agent receives:

- one repository or one source-target slice;
- exact worktree;
- read and write scopes;
- accepted authority decision;
- artifacts to produce;
- checks to run;
- evidence tier target;
- stop conditions;
- RepoLedger patch responsibility.

No agent is assigned “clean up the ecosystem.”

---

# 7. Recommended execution waves

## Wave 0 — Control plane and freeze

- snapshot all 146 repositories;
- gate new repository creation;
- make RepoLedger authoritative;
- add drift checks;
- generate work queues.

## Wave 1 — Lifecycle normalization

Close repositories already archived or self-declared retired, after consumer/provenance checks.

## Wave 2 — Declared absorptions

Complete parity-backed migrations such as:

- agentapi-plusplus → substrate;
- Logify/pheno-tracing → PhenoObservability;
- phenotypeActions → phenotype-fleet-ops;
- phenoForge → Tasken;
- kmobile/mobile extraction → Eidolon.

## Wave 3 — Identity collisions

Resolve:

- FocalPoint / phenotype-apps;
- HeliosLab role;
- Eventra / missing phenoEvents;
- nanovms / PhenoCompose / phenotype-infra / thegent;
- Grapheon / Tracera;
- hwLedger / phenotype-omlx;
- Planify / Planify2;
- Apisync;
- Python/Go SDK successor fiction.

## Wave 4 — Generic umbrella decomposition

Dismantle or narrow:

- pheno;
- PhenoDevOps;
- phenokits-commons;
- phenoAI;
- phenotype-tooling;
- HexaKit;
- pheno-harness;
- phenoUtils;
- Sidekick;
- thegent.

## Wave 5 — HMVP closure

Finish small, high-leverage canonical repositories and then flagship products.

## Wave 6 — Comparative pilots

Run controlled E4 case studies only after E3 truth is stable.

## Wave 7 — Public projection

Generate coherent portfolio pages from RepoLedger.

---

# 8. Cutover protocol

For every migration:

## Prepare

- freeze conflicting feature work;
- capture immutable source/target baseline;
- inventory consumers and packages;
- define compatibility and rollback;
- define parity corpus and mandatory dimensions.

## Implement

- migrate in smallest semantic units;
- preserve history/provenance;
- add compatibility adapters;
- keep source behavior testable;
- update docs and traceability with each unit.

## Verify

- run source and target corpus;
- compare API/schema/behavior;
- run clean build/install;
- run security and failure tests;
- validate package and release identities;
- verify all consumers.

## Dual-run where risk warrants

- emit from both paths;
- compare results;
- prohibit source retirement while material divergence remains;
- record divergence and resolution.

## Cut over

- switch consumers;
- publish migration/deprecation;
- update RepoLedger;
- regenerate portfolio views;
- monitor rollback window.

## Close

- tombstone source;
- archive GitHub repository;
- remove active agents/issues;
- retain recovery instructions and immutable evidence.

---

# 9. Portfolio priority

Rank closure units with:

```text
(user value
 + closure probability
 + dependency unblocking
 + authority ambiguity removed
 + repository reduction value)
/
(effort
 + evidence uncertainty
 + migration risk
 + external blockers)
```

Do not use repository size alone.

The highest-priority units generally are:

1. RepoLedger;
2. zero-code lifecycle contradictions;
3. declared absorptions with small parity surface;
4. identity collisions blocking multiple repos;
5. narrow published tools that can reach HMVP quickly;
6. flagship product vertical slices;
7. broad speculative platforms.

---

# 10. Coordinator outputs

Produce:

```text
portfolio/
  CURRENT_STATE.md
  TARGET_STATE.md
  AUTHORITY_GRAPH.yaml
  REPOSITORY_RELATIONSHIPS.yaml
  MIGRATION_MAP.yaml
  DECISION_LOG/
  WORK_QUEUES.yaml
  RISKS.md
  EVIDENCE/
```

Update the canonical disposition register and RepoLedger.

## CURRENT_STATE.md

Include:

- exact repository count;
- lifecycle/visibility counts;
- authority collisions;
- nonexistent successors;
- duplicate package identities;
- active work in archived/reference repos;
- generic umbrellas;
- strongest products/tools;
- evidence limitations.

## TARGET_STATE.md

Include:

- target active/hold/reference/archive counts;
- authority map;
- repository boundaries;
- generated surfaces;
- literal and semantic ecosystem graph;
- accepted trade-offs.

## WORK_QUEUES.yaml

Every task:

```yaml
task_id: PORT-...
lane: consolidation
source_repos: [...]
target_repos: [...]
authority_domain: ...
prerequisites: [...]
write_scope: [...]
evidence_target: E3
acceptance: [...]
rollback: ...
status: ready
owner: null
```

No task may be “review repository” or “improve docs.” It must end in a falsifiable state change.

---

# 11. Completion checks

The coordinator may close the program only when:

- all repositories have E2 role decisions;
- one authority exists per domain;
- all links resolve;
- GitHub lifecycle matches RepoLedger;
- all migrations preserve provenance and pass parity;
- active agent-owned repositories fall within the accepted target band;
- references and historical repos have no standing feature agents;
- every canonical repo has HMVP or an explicit transition state;
- incubators have promotion/sunset conditions;
- public views are generated;
- no claim exceeds evidence.

---

# Final coordinator report

## Portfolio verdict

State the target count and why alternatives were rejected.

## Decisions accepted

List canonical, narrowed, generated, reference, and retired groups.

## Unresolved decisions

Only evidence-bounded holds, each with the exact next experiment or human decision.

## Closure accomplished

For every source: target, parity evidence, consumer status, archive state, rollback.

## Active work queues

Order by smallest complete closure and dependency leverage.

## Evidence honesty

State what was not inspected, built, run, or measured. Do not present the register as more mature than it is.
