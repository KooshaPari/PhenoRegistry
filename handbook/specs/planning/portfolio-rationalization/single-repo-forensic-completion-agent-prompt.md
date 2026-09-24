# Single-Repository Forensic Recovery, Completion, and Disposition Prompt

Use this prompt unchanged except for the input block.

## Input block

```yaml
repository_of_scope: "<absolute path or owner/repo>"
portfolio_register: "<path to kooshapari-repo-disposition-register.yaml>"
related_repositories:
  - "<owner/repo or local path>"
human_overrides:
  - "<explicit human-approved role, boundary, or decision>"
requested_end_state: "<canonical | narrow | absorb | archive | investigate>"
network_access: "<available | unavailable>"
allowed_write_scope: "<worktree/path>"
```

## Mission

Forensically recover what this repository is, determine what it should be in the portfolio, and take the smallest complete path to one of these honest outcomes:

1. a canonical repository with a Minimum Honest Viable Product;
2. a narrowed repository with an explicit, defensible boundary;
3. a source repository fully absorbed into one or more targets with preserved provenance;
4. a frozen upstream/reference repository;
5. a safely archived historical repository;
6. a forensic hold with precise unresolved evidence—not vague uncertainty.

Do not optimize for the appearance of activity. Optimize for truth, closure, user value, and minimum long-term coordination cost.

## Governing principles

1. **Human-approved decisions outrank stale repository prose.**
2. **Do not trust the README, status badges, progress percentages, issue labels, or prior agent claims.** Treat them as evidence to verify.
3. **Do not infer implementation from specifications.** Label every capability `planned`, `partial`, `implemented-unverified`, `verified`, `released`, or `operational`.
4. **Do not destroy history.** Never delete branches, tags, files, releases, or repositories merely to simplify the picture.
5. **Do not silently move authority.** Every canonical ownership change requires a role decision and migration map.
6. **Do not create a new repository as an escape hatch.** A new repository requires an accepted boundary RFC.
7. **Do not claim completion from a green unit test alone.** Completion includes identity, artifacts, verification, code, operations, evaluation, traceability, and portfolio boundary.
8. **Do not use a model-based judge as the only correctness gate.** Add deterministic assertions for mandatory behavior.
9. **Do not silently skip mandatory checks.** Missing tools, credentials, hardware, or fixtures produce an explicit blocked result.
10. **Do not modify the canonical checkout directly when parallel work or unknown local changes exist.** Use a dedicated worktree and preserve the original state.
11. **No destructive Git operations without explicit human authorization.** No `reset --hard`, forced checkout, branch deletion, history rewrite, or unreviewed clean.
12. **No invented sources, packages, consumers, performance numbers, adoption, releases, or citations.**
13. **Prefer smallest end-to-end closure over broad partial cleanup.**
14. **Record rejected alternatives.** A decision without serious alternatives is not a decision.
15. **Assume the apparent answer is wrong until competing hypotheses are disproven.**

## Required evidence tiers

- **E0:** repository metadata only;
- **E1:** root documentation and declared role;
- **E2:** branches, tags, code, history, provenance, packages, dependencies, consumers;
- **E3:** reproducible clean build/test/quality/security/release evidence;
- **E4:** controlled comparative pilot;
- **E5:** operational/adoption evidence.

Never promote a claim beyond its evidence tier.

---

# Phase A — Safety and immutable baseline

## A1. Capture repository state

Record:

- absolute path and remote URL;
- current branch, HEAD SHA, upstream tracking;
- dirty/untracked/staged state;
- worktrees;
- remotes;
- default branch;
- all local and remote branches;
- tags and releases;
- submodules/subtrees/vendor trees;
- Git LFS;
- repository visibility and GitHub archive state;
- open PRs/issues relevant to role or migration;
- package registries and published artifacts;
- toolchain files;
- secret-bearing or generated/runtime paths that must not be committed.

Create:

```text
docs/audit/
  BASELINE.md
  git-state.txt
  branches-tags.txt
  tree-inventory.txt
  package-inventory.md
  consumer-search.md
  evidence/
```

Do not normalize or “clean up” anything before this snapshot.

## A2. Establish a safe worktree

Create one bounded worktree/branch. Confirm:

- canonical checkout is untouched;
- branch has a single purpose;
- no unrelated changes are imported;
- generated artifacts are separated from source;
- secrets and runtime state are excluded.

## A3. Record uncertainty

Create `docs/audit/HYPOTHESES.md` with at least:

- H1: the repository’s apparent current role is correct;
- H2..HN: plausible alternative roles, absorptions, forks, experiments, or abandoned lineages;
- evidence that would falsify each;
- current confidence.

Do not collapse to H1 because it has the nicest README.

---

# Phase B — Forensic source-of-truth recovery

## B1. Recover intent from all evidence

Inspect:

- README and every root planning/status file;
- `docs/`, ADRs, PRDs, specs, requirements, journeys, runbooks;
- agent instructions;
- issues, PRs, discussions, release notes;
- branch names and abandoned branches;
- commit messages and major merge commits;
- package metadata;
- source comments and public APIs;
- examples and fixtures;
- local prompt/worklog artifacts if available;
- related repositories and predecessor/successor claims;
- prior human overrides.

Build `INTENT_RECOVERY.md` with:

- original problem;
- successive role changes;
- explicit human decisions;
- inferred decisions with confidence;
- contradictions;
- unresolved intent;
- source references by file, commit, issue, or PR;
- a timeline.

## B2. Inventory actual implementation

Do not rely on docs. Produce:

- language/module/package/workspace inventory;
- executable and library entry points;
- API/schema/event surfaces;
- persistent data;
- runtime/deployment surfaces;
- external services;
- feature flags;
- stubs, TODOs, dead paths, generated code;
- duplicate implementations;
- vendored/upstream code;
- test and fixture inventory;
- CI/release workflow inventory;
- security-sensitive code paths.

Classify each feature:

```yaml
feature_id: CAP-...
declared_status: ...
actual_status: planned | stub | partial | implemented_unverified | verified | released | operational
evidence:
  - path: ...
  - commit: ...
gaps: []
```

## B3. Recover provenance

For each substantial directory/package/module:

- origin repository/commit;
- upstream license;
- whether copied, vendored, submoduled, subtree-merged, generated, or independently written;
- divergence;
- unique commits/features;
- current consumers;
- intended target.

Create `PROVENANCE.yaml` and a human-readable map.

## B4. Find semantic clones

Use more than filename equality:

- symbol/API similarity;
- schema similarity;
- behavior and fixture similarity;
- commit ancestry;
- dependency and consumer overlap;
- documentation-intent similarity;
- package identity collisions;
- generated or copied code markers.

Classify:

- exact duplicate;
- semantic duplicate;
- fork with maintained delta;
- partial successor;
- complementary component;
- false similarity.

Never merge by name alone.

## B5. Identify contradictions

At minimum check:

- README vs code;
- README vs package registry;
- README vs GitHub lifecycle;
- spec vs tests;
- tests vs actual user journey;
- default branch vs claimed canonical branch;
- current repository vs named successor;
- package version vs release/tag;
- “library-only” vs server/API claims;
- “archived” vs active issue/agent work;
- “published” vs resolvable artifact;
- “complete” vs stubs/TODOs/failing checks;
- license badges vs actual license;
- current links vs nonexistent repositories.

Create `CONTRADICTIONS.md`. Every contradiction must have an owner and disposition.

---

# Phase C — Role and boundary decision

## C1. Define candidate roles

For each plausible role write:

- target user;
- job to be done;
- primary journey;
- owned concepts/contracts;
- explicit non-goals;
- required dependencies;
- consumers;
- deployment/release/security boundary;
- relation to adjacent repositories;
- why this must or must not be a separate repository.

## C2. Apply the boundary calculus

Separate-repo pressure:

- independent release/support cadence;
- distinct security/access boundary;
- distinct runtime/failure domain;
- multiple independent consumers;
- protocol/schema authority;
- different user and journey;
- independent upstream/fork lifecycle;
- independent contributor/legal boundary.

Merge pressure:

- same primary journey;
- high co-change;
- same release train;
- duplicated contracts;
- no independent consumers;
- no deployment/security distinction;
- tiny/no roadmap;
- coordination overhead greater than internal modularity cost.

Also run the context-load test:

Can an agent understand the charter, target capability, breakable contracts, focused build, and focused test without loading unrelated domains?

## C3. Choose one disposition

Allowed dispositions:

- `canonical`;
- `canonical_reset`;
- `canonical_fork`;
- `canonical_lineage`;
- `conditional_canonical`;
- `incubator`;
- `private_ops`;
- `generated_surface`;
- `upstream_reference`;
- `decompose_and_narrow`;
- `absorb_then_archive`;
- `archive_normalize`;
- `forensic_hold`;
- `forensic_quarantine`.

Create `ROLE_DECISION.md` with:

- decision;
- status: proposed or accepted;
- context;
- chosen role;
- scope and non-goals;
- alternatives;
- evidence;
- trade-offs;
- migration consequences;
- rollback;
- human approval needed;
- exact RepoLedger changes.

Do not continue feature implementation while the repository has an unresolved role collision unless the work is necessary to resolve it.

---

# Phase D — Artifact-complete red state

## D1. Create or repair the canonical artifact set

Use semantic roles; do not create empty ceremonial files.

Required where applicable:

- `CHARTER.md`;
- `README.md`;
- `PRD.md`;
- `SPEC.md`;
- `ARCHITECTURE.md`;
- `FUNCTIONAL_REQUIREMENTS.md`;
- ADRs;
- `SOTA.md`;
- threat model;
- compatibility matrix;
- migration/rollback plan;
- operations/runbooks;
- release/deprecation policy;
- `TRACEABILITY.yaml`;
- fork `UPSTREAM.md`, `DELTA.md`, `SYNC.md`, `EXIT.md`;
- research/model/dataset cards;
- case-study plan.

## D2. Distinguish planned and real behavior

Every user-facing matrix or roadmap must encode status as data. Never use decorative percentages.

Required statuses:

- planned;
- specified;
- test_defined;
- implemented_unverified;
- verified;
- released;
- operational;
- deprecated;
- removed.

A generated status page may summarize these; it may not invent them.

## D3. Build the traceability graph

Use the chain:

```text
JOB -> CAP -> REQ -> ADR -> API/SCHEMA/EVENT -> TEST/CHECK/JOURNEY
    -> CODE -> TELEM -> EVID -> RELEASE -> CASE
```

Every mandatory requirement needs:

- a canonical definition;
- at least one executable validator;
- implementation link;
- risk link;
- evidence output path;
- current status.

Add a machine validator that fails on:

- orphan mandatory requirements;
- tests referencing nonexistent requirements;
- implemented public APIs without contracts;
- public claims without evidence;
- broken predecessor/successor links.

## D4. Perform current SOTA research

Use primary/official sources. Record:

- retrieval date;
- version/commit;
- supported claim;
- exact comparator scope;
- unknowns;
- changed assumptions.

At minimum compare:

- strongest direct incumbent;
- composition of primitives;
- current manual/no-op workflow;
- internal predecessor.

Do not create a feature checklist that treats every feature as equally valuable. Map features to user jobs and risks.

---

# Phase E — Quality-infrastructure red state

## E1. Define quality profile

Select and justify the repository class:

- library/SDK;
- CLI;
- service/gateway;
- desktop/mobile;
- game/mod;
- agent runtime;
- infrastructure/IaC;
- research;
- generated documentation/site;
- private operational source;
- reference fork.

## E2. Wire machine checks

At minimum where applicable:

- formatting;
- lint/static analysis;
- compile/typecheck;
- unit tests;
- integration tests;
- contract/conformance tests;
- journey/E2E tests;
- negative and failure-injection tests;
- property/fuzz/mutation tests;
- performance regression tests;
- dependency/license review;
- secret scanning;
- SAST;
- SBOM/provenance/signature;
- package/release verification;
- docs build/link check;
- traceability validation.

Mandatory gates fail loudly. A skipped tool is a blocked result, not green.

## E3. Test the tests

Prove the gate detects failure:

- inject controlled faults or use mutation testing;
- break one requirement and show its test fails;
- break package/release metadata and show verification fails;
- break a security invariant and show the gate fails;
- break a journey assertion and show the evidence is rejected.

Store command, environment, exit code, and output.

---

# Phase F — Green implementation

## F1. Implement only against accepted requirements

Prioritize:

1. critical correctness/security/data gaps;
2. the primary HMVP journey;
3. compatibility and migration;
4. operational and recovery behavior;
5. performance;
6. nonessential breadth.

Do not implement speculative features merely because an old roadmap lists them.

## F2. Maintain architecture discipline

Audit and correct:

- god objects/modules;
- global mutable state;
- circular dependencies;
- layer violations;
- duplicated domain logic;
- hidden side effects;
- blocking calls in async paths;
- unbounded queues/caches/retries;
- weak cancellation/timeout behavior;
- shell injection/path traversal;
- insecure defaults;
- error swallowing;
- fake adapters and silent fallbacks;
- generated code drift;
- configuration only adjustable at startup when runtime control is required.

Use KISS, DRY, YAGNI, SOLID, and hexagonal boundaries as tools, not slogans. Prefer the smallest design that satisfies current requirements and keeps the next likely change cheap.

## F3. Reproduce from a clean environment

Document and execute:

- fresh clone;
- toolchain install;
- dependency install;
- build;
- focused tests;
- full tests;
- lint/type/security;
- package;
- install;
- launch;
- primary journey;
- rollback/uninstall.

Record all deviations and platform limits.

---

# Phase G — Pilot and differentiation

## G1. Define mandatory and tradeable dimensions

Mandatory by default:

- correctness;
- data integrity;
- security;
- privacy;
- contractual compatibility;
- truthful failure behavior.

Candidate tradeable dimensions:

- latency;
- throughput;
- memory/CPU/GPU;
- monetary cost;
- setup complexity;
- LOC/API complexity;
- extensibility;
- portability;
- observability;
- maintenance/change amplification;
- UX and operator interventions.

## G2. Build a fair corpus

Use identical:

- tasks;
- acceptance criteria;
- model/provider/version;
- hardware;
- budgets;
- retry/timeout rules;
- cache state;
- data;
- evaluator;
- repetitions.

## G3. Failure injection

Include:

- provider/network failure;
- invalid/malicious inputs;
- tool timeout;
- cancellation;
- process crash;
- partial state;
- corrupted/migrated data;
- rate limit;
- resource exhaustion;
- incompatible version;
- unavailable optional dependency.

## G4. Report honestly

Create:

```text
case-studies/<case-id>/
  PLAN.md
  environment.json
  corpus/
  raw/
  results.csv-or-json
  analysis.md
  limitations.md
  reproduce.sh-or-task
  evidence-manifest.json
```

A pass requires:

- no mandatory regression;
- quantified trade-offs;
- one material target-user advantage;
- reproducibility;
- attribution to the product rather than different model/hardware/evaluator.

---

# Phase H — Disposition execution

## H1. Canonical or narrowed repository

Complete:

- accepted role decision;
- truthful README;
- machine status;
- HMVP evidence;
- package/release truth;
- RepoLedger update;
- generated docs/profile refresh;
- remaining backlog only for non-HMVP work.

## H2. Absorption

Before source retirement:

- source-to-target file/symbol/contract map;
- preserved provenance;
- compatibility bridge;
- source and target fixture parity;
- consumer migration;
- package deprecation;
- rollback;
- immutable evidence.

## H3. Reference fork

Complete:

- upstream URL and exact pin;
- delta inventory;
- sync cadence;
- allowed local changes;
- contribution policy;
- exit strategy;
- no unsupported first-party product claims.

## H4. Archive

Complete:

- unique branches/tags/issues/releases/artifacts inventoried;
- successor exists;
- consumers migrated;
- license/provenance retained;
- secrets/runtime data reviewed;
- tombstone with exact recovery path;
- GitHub archive state reconciled;
- removed from active queues.

Deletion is not implied.

---

# Required outputs

At repository root or under `docs/audit/`, produce:

1. `BASELINE.md`
2. `HYPOTHESES.md`
3. `INTENT_RECOVERY.md`
4. `IMPLEMENTATION_INVENTORY.yaml`
5. `PROVENANCE.yaml`
6. `CONTRADICTIONS.md`
7. `ROLE_DECISION.md`
8. `BOUNDARY.md`
9. repaired canonical artifacts
10. `TRACEABILITY.yaml`
11. `QUALITY_PROFILE.yaml`
12. `MIGRATION.md` or `DEPRECATION.md` when applicable
13. pilot plan/results when E4 is in scope
14. `repo-audit-result.yaml`
15. command/evidence bundle
16. exact RepoLedger patch

Validate `repo-audit-result.yaml` against `repo-audit-result.schema.json`.

---

# Final report format

## Decision

- repository:
- commit audited:
- evidence tier reached:
- current role:
- selected role:
- disposition:
- target authority:
- confidence:
- human decisions required:

## Truth table

| Claim | Declared | Actual | Evidence | Action |
|---|---|---|---|---|

## Blocking contradictions

Rank by correctness, security, user harm, migration risk, and authority damage.

## Boundary verdict

Explain why the repository survives, narrows, merges, archives, or remains on hold. Include rejected alternatives.

## Completion vector

| I | A | V | C | O | E | T | B |
|---:|---:|---:|---:|---:|---:|---:|---:|

No average. Explain every score.

## Commands reproduced

Include environment, command, exit code, result, and evidence path.

## Migration/closure state

- complete:
- incomplete:
- rollback:
- consumer status:
- package status:
- GitHub/RepoLedger reconciliation:

## Next smallest tasks

List only independently closable tasks in dependency order. Do not produce a generic backlog.

## Honesty statement

State exactly what was not inspected or reproduced. Never use “done,” “complete,” “production-ready,” or “canonical” beyond the evidence.
