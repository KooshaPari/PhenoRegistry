# Before, transition, and after maps

## Before: flat namespace with mixed semantics

```mermaid
flowchart TB
  O[KooshaPari GitHub account<br/>146 repositories]

  O --> P[Products and applications]
  O --> F[Shared foundations and Kits]
  O --> R[Agent runtimes and routers]
  O --> U[Upstream-derived forks]
  O --> D[Docs, specs, registry, governance]
  O --> L[Labs, staging and extraction repos]
  O --> A[Archives and recovery snapshots]

  P --> X1[Duplicate product names]
  F --> X2[Generic and one-consumer shared code]
  R --> X3[Overlapping execution ownership]
  U --> X4[Unclear upstream/local value]
  D --> X5[Stale and conflicting authorities]
  L --> X6[No TTL or landing decision]
  A --> X7[Provenance mixed into daily mental load]
```

This view does not say every repository is bad. It shows that a flat namespace provides no reliable semantics.

## Transition: capability and authority control plane

```mermaid
flowchart TB
  GH[GitHub observations] --> RF[Live repository facts]
  RF --> REG[Curated repo/capability registry]

  INT[Human intent and accepted contracts] --> CAP[Capability graph]
  REG --> CAP
  HIST[Branches, commits, releases, upstreams] --> CAP
  CONS[Consumers and co-change] --> CAP
  TEST[Quality and runtime evidence] --> CAP
  SOTA[SOTA and pilots] --> CAP

  CAP --> DEC[Central decision queue]
  DEC --> MAP[Component-level source-to-target map]
  MAP --> WBS[Closure WBS / DAG / PERT]
  WBS --> STAGE[Isolated migration and implementation]
  STAGE --> VERIFY[Independent verification]
  VERIFY --> TERM[Terminal repository states]
  TERM --> REG
```

## After: layered bounded polyrepo

```mermaid
flowchart TB
  subgraph Authority["Portfolio and durable authorities"]
    STRAT[Strategy / capital]
    WORK[Governed work / specs]
    LABOR[Agent labor]
    TRACE[Trace / evidence]
    LEDGERS[Specialized ledgers]
  end

  subgraph Foundations["Shared foundations"]
    PROTO[Protocols / identifiers]
    SDK[SDK homes]
    OBS[Observability]
    OPS[Policy / CI / operations]
    PLUG[Plugins / adapters]
    CATALOG[Registry / projections]
  end

  subgraph Developer["Developer and runtime products"]
    AGENT[Agent framework/runtime]
    CLIENTS[Coding-agent clients]
    ROUTER[Provider routing/gateway]
    MCP[MCP framework/servers]
    COMPUTE[Compute/data/I-O fabric]
    DEPLOY[Deployment/runtime tooling]
  end

  subgraph Applied["Independent applied products"]
    CIVIC[Civic]
    FOCUS[Focus/productivity]
    WORLDS[World/game/graphics]
    MEDIA[Creative/media]
    OTHER[Other validated products]
  end

  subgraph Exceptions["Controlled exceptions"]
    FORKS[Strategic forks]
    INC[TTL incubators]
    ARCH[Archives/provenance]
  end

  Authority --> Foundations
  Foundations --> Developer
  Foundations --> Applied
  Developer --> Applied
  CATALOG -.generated views.-> Authority
  FORKS --> Developer
  INC -.graduate/absorb.-> Developer
  INC -.graduate/absorb.-> Applied
  ARCH -.lineage.-> CATALOG
```

## Audience projections

```mermaid
flowchart LR
  SSOT[Canonical capability / authority graph]

  SSOT --> PUBLIC[Public map<br/>10–20 product brands]
  SSOT --> DEV[Developer map<br/>SDKs, APIs, runtimes, dependencies]
  SSOT --> OPS[Operator map<br/>health, releases, work, cost]
  SSOT --> AGENT[Agent routing map<br/>owner, path, contract, task]
  SSOT --> HIST[History map<br/>forks, predecessors, archives]
```

## Repository lifecycle

```mermaid
stateDiagram-v2
  [*] --> Proposed
  Proposed --> Incubator: approved hypothesis
  Proposed --> Canonical: hard boundary / proven role
  Proposed --> Rejected

  Incubator --> Canonical: graduation
  Incubator --> Absorbing: one dominant parent
  Incubator --> Archived: hypothesis fails / expires
  Incubator --> Incubator: evidence-backed extension

  Canonical --> Maintenance
  Canonical --> Migrating
  Maintenance --> Migrating
  Migrating --> Canonical: target survives
  Migrating --> Bridge: compatibility window
  Bridge --> Archived: consumers migrated
  Maintenance --> Archived: supported retirement
  Archived --> [*]
  Rejected --> [*]
```

## Capability maturity

```mermaid
flowchart LR
  G0[G0 identity/evidence] --> G1[G1 docs/design]
  G1 --> G2[G2 red quality]
  G2 --> G3[G3 green implementation]
  G3 --> G4[G4 pilot evidence]
  G4 --> G5[G5 productization]
  G5 --> G6[G6 ecosystem terminal state]

  G4 --> N[No distinct value<br/>narrow/absorb/retire]
  G2 --> R[Research blocker<br/>hypothesis/experiment]
  G3 --> R
```

## Key structural effect

The target reduces daily complexity in three ways:

1. Archives and forks remain discoverable but leave the default active-product view.
2. Shared capabilities have one authority, even when several implementations/adapters exist.
3. Large repositories expose enforced internal packages and scoped build/test targets so an agent can own a bounded area without loading the entire repo.
