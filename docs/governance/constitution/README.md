# Portfolio Constitution and Knowledge Architecture

**Status:** proposed canonical portfolio governance architecture; inventory incomplete until repository/history/conversation sweep closes.
**Date:** 2026-09-29.

## Purpose

The portfolio has outgrown human working memory.

Repeated conventions, product intent, architecture doctrine, tooling choices, cost constraints, agent-process rules and historical rationale have accumulated across chats and repositories. Repeating them manually causes:
- wording drift;
- accidental policy forks;
- old rules being resurrected;
- new rules failing to reach old repositories;
- product-specific exceptions becoming mistaken global defaults;
- the owner having to reconstruct prior reasoning repeatedly.

The solution is not one giant constitution file. It is a **versioned policy and knowledge hierarchy with inheritance, applicability, supersession and evidence**.

## Knowledge layers

### L0 — Portfolio Constitution

Smallest, strongest set of durable portfolio-wide principles.

Examples:
- user/product outcomes outrank tooling fashion;
- agents are replaceable workers;
- accepted intent/evidence outranks self-reported completion;
- reuse existing primitives where they are superior;
- architecture decisions must expose scope/applicability;
- zero-dollar CI constraint where declared;
- durable product memory is required;
- no hidden weakening of acceptance to manufacture green.

L0 should change rarely.

### L1 — Portfolio Standards

Deep domain-specific policy systems:

```text
standards/
  documentation/
  engineering/
  architecture/
  repository-topology/
  polyglot-toolchains/
  ci/
  testing-verification/
  release-lifecycle/
  dependencies/
  security/
  agents/
  observability/
  product-design/
  frontend/
  data/
  forks-upstream/
  ...
```

Each standard uses bulkhead → modules → evidence.

### L2 — Profiles

A profile resolves standards for a class of repository/product.

Examples:
- Rust service;
- Python package/service;
- TypeScript web app;
- desktop app;
- CLI;
- library/SDK;
- experimental/research repo;
- shared infrastructure;
- multi-app workspace;
- polyglot service;
- fork/derived upstream;
- safety/assurance-sensitive product.

A repo may compose several profiles.

### L3 — Repository Constitution

Each repo declares:
- inherited standards/profile versions;
- applicable rules;
- explicit exceptions;
- local architectural decisions;
- local product contract;
- local evidence.

It should not copy every portfolio rule.

### L4 — Product/Component/Path Overrides

Narrow exceptions or stronger rules for a package/component/path.

Every exception needs:
- reason;
- owner/authority;
- scope;
- date;
- expiry or reevaluation trigger;
- downstream consequences.

### L5 — Work/Attempt Resolution

AgilePlus/agents compile applicable policy into the exact work assignment/context.

Workers should receive the resolved policy needed for the task, not the entire portfolio handbook.

## Policy object

Every enforceable policy should eventually be machine-addressable:

```text
PolicyId
title
statement
rationale
authority
status
effective_from
supersedes / superseded_by
applicability predicate
default severity
exceptions
verification method
evidence
source provenance
last reviewed
review trigger
```

Narrative documentation remains essential, but policy objects allow resolution and drift detection.

## State distinctions

Never conflate:
- user preference;
- accepted portfolio policy;
- recommended default;
- experiment;
- historical rule;
- repo-specific exception;
- external best practice;
- assistant suggestion.

The same sentence can move through these states over time; preserve the transition.

## Supersession

Policy evolution is expected.

Example architecture lineage:
- early microservice-heavy exploration;
- later recognition that service decomposition has operational cost;
- current default: modular monolith/vertical slices with hexagonal seams at real effect/trust/volatility boundaries; extract services when independent scaling, deployment, ownership, failure isolation or other evidence justifies it.

The historical view remains searchable, but only the current policy resolves by default.

## Initial recurring-rule inventory

This is a seed inventory, not an exhaustive claim.

### Toolchain / polyglot

Current qualified direction recovered from repeated discussions:
- `mise` as outer toolchain/version/environment/task coordination where useful;
- native ecosystem managers retain dependency truth;
- Python: `uv` as default project/workspace/package manager; CPython 3.14 free-threaded where compatibility/performance case supports it; Ruff/ty-class tooling where applicable;
- JS/TS: Bun as qualified default package/runtime/tooling layer; native TypeScript; Oxc/Oxlint/Oxfmt-class stack where compatibility and maturity satisfy the repo;
- Rust: Cargo remains native dependency/build authority;
- other ecosystems retain native managers/build systems rather than forcing one universal dependency store;
- shared caches/content-addressed reuse are preferred over mutable shared environments;
- experimental/polyglot languages are allowed when the product/experiment justifies them.

External current docs confirm both uv and Bun support native workspaces; this does not mean all repos should become monorepos.

### Repository topology

Default is **polyrepo with synthetic-monorepo coordination where useful**, not repository-count ideology.

Principles:
- repository != build boundary;
- repository != release boundary;
- co-location does not imply build/test/release all targets;
- multi-app repos require target/component-aware affected execution;
- cross-repo snapshots/dependencies are explicit and versioned;
- shared capabilities should be independently consumable;
- preserve repo autonomy while providing graph-aware portfolio coordination.

### Architecture

Current portfolio default should be:
- modular monolith / vertical slices first;
- explicit modules and dependency boundaries;
- hexagonal/ports-and-adapters at meaningful volatility/effect/trust/external boundaries;
- microservices only when independently justified by scaling, deployment, ownership, isolation, security or lifecycle needs;
- do not create services merely to appear distributed;
- product-specific architecture may override with evidence.

This supersedes earlier generic microservice-heavy guidance as a portfolio default.

### Code size / decomposition

A recurring owner constraint is to keep source files roughly below 500 lines.

Treat this as a **maintainability trigger/guardrail**, not a semantics-free mechanical splitter:
- generated/vendor/data/schema files require separate treatment;
- a 480-line incoherent file can still be wrong;
- a justified cohesive >500-line file may need an explicit exception rather than destructive fragmentation;
- splitting must preserve coherent ownership and avoid wrapper/file-count slop.

Exact enforcement profile still needs historical/repo audit before finalization.

### CI economics

The portfolio does not intend to incur unbounded GitHub Actions compute billing.

Current policy direction:
- GitHub is source/review/status/control plane;
- public standard GitHub-hosted runners can use GitHub's free public-repo capacity where security/trust model permits;
- private/heavy compute should use self-hosted or other explicitly zero-dollar/already-paid execution;
- no silent paid hosted-runner fallback;
- affected/path filters and concurrency cancellation;
- cheap required gates before expensive suites;
- scratch/experimental repos need not have heavyweight CI by default;
- artifacts/caches must respect storage economics.

Current GitHub documentation confirms standard public hosted usage and self-hosted runner usage are free from GitHub Actions minute billing, while private hosted use consumes plan allowance and can become billable. Security policy must account for untrusted public PRs on self-hosted runners.

### Agent engineering

- agents are replaceable workers, not authorities;
- work should be bounded by exact context, scope, acceptance and evidence;
- isolated branches/worktrees/sandboxes where appropriate;
- immutable/source-backed receipts over agent self-report;
- retry/resume without losing durable progress;
- human review focuses on intent, risk, authority, taste and hard exceptions;
- MACE-style feedback should guide convergence;
- policy should compile into agent context.

### Documentation / memory

- repository + registry docs are durable human and agent memory;
- major domains use bulkhead → focused modules → evidence/raw sources;
- Genesis and raw intent preserve conceptual lineage;
- fresh-human and fresh-agent recoverability are completion gates;
- shallow placeholder docs do not count.

### Shared code

- PhenoShared/shared libraries should expose narrow, independently consumable capabilities;
- avoid central god-libraries and accidental coupling;
- reuse should reduce product-local duplication without making every product move in lockstep.

### Fork/upstream

- upstream is an input, not authority;
- strategic hard forks are legitimate;
- preserve origin/lineage;
- selective sync is explicit;
- extracted/derived components document compatibility and ownership;
- upstream contribution is optional, not assumed.

## External SOTA alignment

The portfolio should periodically revalidate defaults against current external tooling rather than fossilize them.

Examples:
- uv/Bun workspace capabilities;
- GitHub runner billing/security;
- monorepo/polyrepo tooling;
- language/toolchain maturity;
- CI orchestration;
- build graph/caching;
- agent development systems.

External practice informs policy; it does not automatically override owner constraints or product evidence.

## Resolution algorithm

For a repo/task:

```text
L0 Constitution
  + applicable L1 Standards
  + selected L2 Profiles
  + L3 repo decisions
  + L4 scoped overrides
  + current product/work constraints
  = Resolved Policy Snapshot
```

Conflicts resolve by:
1. explicit narrower accepted override;
2. stronger safety/product invariant;
3. newer superseding decision at same authority/scope;
4. otherwise block and request adjudication.

Do not resolve ambiguity by whichever file an agent found first.

## Evidence and enforcement

Policies should declare whether they are:
- narrative only;
- lintable;
- structurally checkable;
- CI-enforceable;
- runtime-observable;
- human-review only.

Examples:
- file-size trigger: static check + exceptions;
- frozen lockfile: CI;
- GitHub paid-runner prohibition: workflow policy check;
- module boundaries: architecture/lint rule;
- documentation bulkheads: structural validator + semantic recovery review.

## Migration program

Do not rewrite every repository blindly.

1. inventory all repositories, including archived/deleted lineage where useful;
2. discover governance/docs/config/tooling;
3. extract candidate rules and provenance;
4. cluster duplicates/contradictions;
5. reconstruct chronology;
6. adjudicate current portfolio policy;
7. define profiles;
8. make repo inheritance explicit;
9. record exceptions;
10. add drift checks;
11. remove duplicated local policy only after inheritance is proven.

## Completion criteria

The portfolio constitution is not complete until:
- all active repos have been inventoried;
- meaningful historical governance sources have been reviewed;
- repeated conversation-level owner rules are indexed;
- contradictions/supersessions are adjudicated;
- every active repo resolves to a policy snapshot;
- unexplained local deviations are zero or explicit;
- fresh agents can determine applicable policy without chat history;
- the owner can recover why a rule exists and how it evolved.

This document establishes the system; it does not claim the inventory is complete.
