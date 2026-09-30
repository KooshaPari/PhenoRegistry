# Specialist Program — Portfolio Constitution & Policy Archaeology

## Mission

Reconstruct the portfolio's durable engineering constitution across all KooshaPari repositories, historical Git state, PhenoRegistry, prior ChatGPT conversations/memories, and current external best practices.

This is **shared governance research**, not a third product-recovery program.

Do not take ownership of Tracera or AgilePlus product specification. Those remain in their dedicated pair program.

## Primary objective

The owner has repeated many engineering/process rules so often that repetition itself is becoming a failure mode.

Examples include:
- uv;
- Bun;
- Oxc/Oxlint/Oxfmt;
- mise;
- Lefthook;
- FastMCP;
- ~500 LOC source-file guidance;
- GitHub Actions billing/runner policy;
- polyrepo + synthetic-monorepo strategy;
- affected/component-aware builds;
- polyglot dependency/toolchain principles;
- modular-monolith vs microservices evolution;
- hexagonal architecture;
- shared-library philosophy;
- agent isolation/resumability/evidence;
- release lifecycle;
- fork/upstream policy;
- Git history preservation.

The goal is to ensure the owner never has to reconstruct these from memory again.

## 1. Evidence sources

Use:
- all active repositories;
- useful archived repositories;
- useful deleted-repo recovery evidence if available;
- Git history;
- old governance/docs/config;
- PhenoRegistry;
- conversation history/memory;
- README/AGENTS/CLAUDE files;
- CI workflows;
- task runners;
- package/tool configs;
- architecture docs;
- release scripts;
- historical migrations;
- external primary documentation and standards.

Do not infer portfolio policy from one repository.

## 2. Reconstruct policy lineage

For every candidate rule, recover:
- earliest known owner statement;
- important later restatements;
- implementation evidence;
- contradictions;
- superseding guidance;
- current external state;
- current recommended interpretation.

Preserve evolution.

Example form:

```text
POL-ARCH-001

2025:
  microservice-positive exploration

2026-H1:
  stronger hexagonal/polyrepo separation

2026-H2:
  modular monolith / vertical slices default
  extract services only with evidence

Current:
  accepted default

Historical formulations:
  preserved, not deleted
```

## 3. Distinguish policy states

Each claim must be one of:
- OWNER_ACCEPTED_POLICY;
- OWNER_PREFERENCE;
- RECOMMENDED_DEFAULT;
- EXPERIMENT;
- HISTORICAL;
- SUPERSEDED;
- REPO_EXCEPTION;
- EXTERNAL_BEST_PRACTICE;
- ASSISTANT_PROPOSAL;
- UNKNOWN.

Do not promote assistant suggestions into owner policy.

## 4. Build the hierarchy

Produce:

```text
constitution/
  README.md

standards/
  engineering/
  architecture/
  repository-topology/
  polyglot/
  python/
  js-ts/
  rust/
  ci/
  testing/
  release/
  dependencies/
  agents/
  documentation/
  forks-upstream/
  security/
  observability/
  ...

profiles/
  rust-service/
  python-package/
  typescript-web/
  desktop/
  cli/
  sdk/
  shared-library/
  multi-app-workspace/
  polyglot-service/
  research-experiment/
  fork/
  ...

repos/
  <repo>/
    resolved-policy.json
    exceptions.md
    drift.md
```

Do not create empty structure merely for completeness.

## 5. Policy schema

Every accepted machine-addressable policy should eventually include:

```text
PolicyId
title
statement
rationale
authority/source
status
applicability
effective_from
supersedes
superseded_by
default severity
verification method
exceptions
source provenance
last reviewed
review trigger
```

## 6. Git-specific doctrine

Treat Git as append-oriented transaction history.

Preserve:
- commits;
- ancestry;
- bad experiments;
- reverts;
- regressions.

Future commit quality should improve.

Historical readability should be improved with additive indexes/annotations, not SHA rewriting.

Fast-forward is good.

Squash and shared-history rebases are disfavored.

## 7. Repo sweep deliverable

For every active repo classify:
- language/toolchain profile;
- build targets;
- release targets;
- current CI;
- policy files;
- architecture style;
- deviations;
- stale rules;
- missing inheritance;
- exceptions;
- Git merge/rewrite settings where observable.

Do not confuse repository with build target.

Multi-app repos require target-level analysis.

## 8. External research

Verify current state of:
- uv;
- Bun;
- Oxc;
- mise;
- GitHub Actions billing/runners/security;
- monorepo/polyrepo tooling;
- affected-build tools;
- task runners;
- hooks;
- language managers;
- modern CI;
- release automation;
- agent coding workflows.

External practice informs policy but does not automatically override owner constraints.

## 9. Drift analysis

For each accepted policy identify:
- compliant repos;
- explicit exceptions;
- accidental drift;
- unknown/uninspected.

Do not auto-fix all drift.

First produce evidence and a migration plan.

## 10. Output quality

Documentation must use bulkhead → focused module → evidence.

Create fresh-human and fresh-agent recovery tests for the constitution itself.

The final success condition is:

> A fresh agent can enter any repository, resolve the applicable portfolio policy without asking the owner to repeat established doctrine, explain why those rules apply, identify explicit exceptions, and avoid resurrecting superseded policy.

## 11. Do not

- rewrite shared Git history;
- blindly standardize every repo;
- create a monorepo;
- begin another product-recovery program;
- turn preferences into universal hard gates without scope analysis;
- replace native dependency managers with a universal store;
- declare audit completeness from repository count alone.

## First execution

Begin with a source inventory and lineage matrix, then create/update the PhenoRegistry constitution branch with evidence-backed policy families.

Do not answer with a plan-only response. Start the archaeology.
