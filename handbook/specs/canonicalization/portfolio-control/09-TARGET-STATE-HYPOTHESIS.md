# Before, transition, and target-state hypothesis

## Before: observed portfolio shape

The current account has 146 owner-affiliated repositories in one flat GitHub namespace. That raw set includes:

- flagship-scale products;
- broad multi-domain monorepos;
- one-crate or one-purpose fragments;
- strategic forks and upstream snapshots;
- duplicate generations and extraction targets;
- empty or near-empty staging repositories;
- public/private variants;
- docs, registries, governance, landings, and release channels;
- archives and historical recovery surfaces;
- labs whose graduation status is unclear.

The failure mode is not simply “too many repos.” It is that the same namespace mixes **product brands, capability authorities, implementation packages, upstream patch queues, temporary workspaces, and immutable history** without one current machine-readable model.

### Current topology symptoms

```text
flat repository namespace
├── product authorities
├── duplicate product names
├── generic shared workspaces
├── tiny one-consumer libraries
├── execution frameworks with overlapping claims
├── several router/gateway/proxy generations
├── docs/spec/registry/enforcement authorities in disagreement
├── upstream-derived forks presented beside original products
├── local shelf/workspace repositories
├── active labs with no TTL
└── archives counted mentally like maintained products
```

### Current operator cost

- Agents cannot reliably determine where a capability belongs.
- A repo-local agent may create a competing SSOT.
- Cross-repo changes require rediscovery and manual reconciliation.
- Public users see multiple names for the same or unclear products.
- Completion percentages and docs may outpace executable evidence.
- Archives and active products compete for attention.
- New focused experiments have no mandatory landing or graduation decision.
- A “complete all repos” campaign risks multiplying inconsistent boilerplate.

## Transition: capability-first portfolio migration

The transition state introduces control without requiring an immediate destructive reorganization.

```text
GitHub inventory
      ↓
RepoLedger/live facts
      ↓
curated capability + authority registry
      ↓
family-level forensic adjudication
      ↓
per-component source→target dispositions
      ↓
closure work packages
      ↓
compatibility and consumer migration
      ↓
terminal repo states
```

### Transition artifacts

- Current machine inventory with immutable observation refs.
- Capability graph and stable IDs.
- Authority/SSOT registry.
- Repo and family dossiers.
- Semantic clone and Git lineage reports.
- Maturity vectors and unsupported-claim register.
- Source-to-target component map.
- Consumer/dependency/co-change graph.
- Repository birth/retirement policy.
- WBS, DAG, PERT, closure queue, and evidence gates.
- SOTA dossiers and controlled pilots.
- Migration and compatibility plans.
- Public portfolio projections generated from canonical state.

### Transition topology

During migration, some temporary duplication is permitted only when explicit:

- old canonical → compatibility bridge;
- target shadow implementation;
- dual-read/write or mirrored package;
- migration deadline;
- owner and removal gate;
- observed consumer adoption.

Unbounded “temporary” duplicate authority is prohibited.

## Target: layered polyrepo with bounded authorities

The final topology should optimize user comprehension, agent context, release independence, and change locality.

### Tier 1 — Portfolio and durable authorities

Likely categories:

- Strategy/resource allocator.
- Governed work/spec lifecycle.
- Labor/agent execution.
- Evidence/trace graph.
- Operational session memory.
- Research source/provenance.
- Repository inventory.
- Hardware/compute capacity.

These may remain separate because their durable state and authority differ, while sharing identifiers and event contracts.

### Tier 2 — Shared foundations

A small set of intentionally boring package homes:

- Protocols, IDs, envelopes, schemas.
- Language SDKs when real external consumers exist.
- Observability.
- Policy/quality/operations automation.
- Plugins/adapters.
- Common platform primitives.
- Journey/evidence tooling.
- Identity/registry clients.

Avoid both one universal `shared` repository and dozens of one-consumer `Kit` repos.

### Tier 3 — Developer/runtime products

Independent only when they have coherent adoption or lifecycle:

- Agent SDK/framework.
- Agent labor/orchestration runtime.
- OS-adjacent process/compute supervisor.
- Coding-agent clients/workbenches.
- Provider routing/gateway.
- MCP framework/server products.
- Deployment/runtime products.
- Distributed compute/I/O fabric.

### Tier 4 — Applied products

Products can share a design philosophy without being forced into one runtime graph or brand:

- Civic.
- Focus/productivity.
- World/game/graphics.
- Music/creative.
- Deployment or other tools.
- Portfolio/career products where independently valid.

This is the **semantic ecosystem**: consistent principles, evidence discipline, local-first/control-oriented design, traceability, and agent-operable workflows. Literal dependencies are optional.

### Tier 5 — Controlled exceptions

- Strategic upstream-derived forks.
- Packaging/distribution repositories.
- Active labs/incubators.
- Immutable archives/provenance.

These have separate visual treatment and counts.

## Provisional numeric target

A reasonable initial target for active/canonical management is **45–70 repositories**, not a hard 50 and not the raw GitHub count.

Illustrative—not approved—distribution:

| Group | Range |
|---|---:|
| Portfolio/evidence authorities | 7–10 |
| Shared foundations and SDK homes | 8–14 |
| Developer/runtime products | 8–14 |
| Applied products | 10–18 |
| Strategic forks/adapters/packaging | 6–12 |
| Active labs | 3–6 |
| Total, with overlap removed | about 45–70 |

Public brand count should be lower: roughly **10–20 memorable products**, with foundations and forks clearly subordinated.

Archives can leave the raw account above 70. The operator UI and registry should default to canonical/active views so provenance does not become daily cognitive load.

## Why not force the prior 32-repository model

A prior whitepaper proposed 32 canonical repositories plus up to six forks. That may still be a valuable aggressive-consolidation alternative, but it predates the current 146-repository inventory and newer product/fork/lab distinctions. It should be evaluated against:

- independent applied products;
- strategic fork requirements;
- language SDK consumers;
- agent context size;
- build/release coupling;
- security/license boundaries;
- the new distributed compute/I/O work;
- actual co-change and consumer evidence.

A 32-repo target that creates five enormous ambiguous repos is worse than 60 coherent repos.

## Why not accept 100 active repositories

One hundred active authorities would still leave severe navigation and maintenance cost unless most are genuine independent products or forks. The current inventory contains obvious duplicate/staging/generic families, so a meaningful reduction should be achievable without destroying valid boundaries.

## Target repository contract

Every canonical active repository should be explainable in one sentence:

> `<Repo>` is the canonical `<role>` for `<bounded job/capability>`, consumed by `<audience/consumers>`, versioned/deployed `<independently or with stated group>`, and explicitly does not own `<neighboring scopes>`.

It also needs:

- primary role;
- authority entities;
- public surfaces;
- consumers;
- release/support lifecycle;
- dependency direction;
- non-goals;
- first-value journey;
- maturity gate;
- upstream/provenance;
- future extraction triggers.

## Public map versus engineering map

Do not expose one 60-node engineering graph as the public story.

### Public product map

Show user jobs and a small brand set.

### Developer platform map

Show APIs, SDKs, runtimes, integrations, and dependencies.

### Operator map

Show authorities, state, releases, health, and migration.

### Historical map

Show predecessors, forks, archives, and provenance.

All are generated projections of the same canonical registry.

## Exit measures

The target is reached when:

- Every repo has a terminal role/disposition.
- Every material capability has one canonical authority or explicit shared contract.
- No public duplicate product name remains unexplained.
- Operational repo count and public brand count meet accepted bounds.
- New repo births follow policy.
- Agent navigation can resolve owner/path/contract from machine data.
- Cross-repo change and duplicate-code rates fall.
- A retained product reaches its appropriate maturity gate.
- Forks and archives are clearly separated from original product claims.
- The portfolio can be understood by users, contributors, agents, and the operator through different generated views.
