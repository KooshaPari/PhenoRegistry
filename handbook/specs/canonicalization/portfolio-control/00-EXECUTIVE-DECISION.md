# Executive decision: from 146 repositories to a governable capability portfolio

**Status:** Program charter v0.1  
**Observation date:** 2026-09-01  
**Inventory scope:** 146 repositories owned by `KooshaPari`, including public, private, active, archived, original, forked, staging, and lineage repositories.

## Decision in one paragraph

The portfolio will not be optimized by deleting repositories until an arbitrary count is reached. It will be rebuilt around a canonical **capability and authority graph**. Every repository will receive an evidence-backed role, maturity state, source-of-truth boundary, and disposition. Every material capability will be traceable across human intent, product contract, architecture, code, machine-verifiable quality, empirical evidence, operations, and market alternatives. Cross-repository decisions will be made centrally; repository agents will collect evidence and close bounded work but will not independently declare a sibling obsolete. The initial target hypothesis is **45–70 canonical active repositories**, **10–20 public product brands**, a bounded set of strategic forks/adapters, and a separately counted archive/lineage tier. This is a hypothesis to validate, not a quota.

## What is wrong with the current mental model

### Repository count is not the actual unit of complexity

At least five counts must be tracked:

| Metric | Meaning |
|---|---|
| Raw repository count | Every GitHub repository, including archives and provenance |
| Operational repository count | Repositories that demand maintenance, CI, dependency updates, triage, or releases |
| Canonical authority count | Repositories that own a product, protocol, schema, policy, or durable state |
| Public product count | Brands and adoption surfaces a user is expected to understand |
| Active incubator count | Temporary experiments receiving current development attention |

A raw archive can remain indefinitely without imposing the same cost as an active release authority. Conversely, two repositories that both claim the same capability create severe cost even if the total count is small.

### Unix philosophy does not imply one Git repository per micro-program

The durable idea is small, composable interfaces. Repository separation is justified by independent lifecycle, versioning, consumers, deployment, security, licensing, ownership, or adoption—not by implementation size alone. A focused package inside a coherent workspace can be more Unix-like than twenty tiny repositories with circular releases.

### “Not worse in any single way” is not a viable approval rule

Real products trade latency against quality, portability against platform depth, simplicity against extensibility, and control against convenience. The replacement policy is:

1. Define **must-not-lose** dimensions for the target user and journey.
2. Require explicit evidence that hard floors are met.
3. Permit a disadvantage on a tradeable dimension only when it buys material compensating value and is documented.
4. Require at least one meaningful must-win wedge or a distinct user job.
5. For internal libraries, forks, adapters, and operational tools, strategic leverage, compatibility, reuse, or cost reduction can justify existence without product novelty.

The prohibition is not “never worse.” It is **no hidden regression, no accidental inferiority on a critical dimension, and no product with neither a distinct job nor a defensible value wedge**.

### “Represent everything in every layer” should mean traceability, not duplication

A requirement should not be rewritten independently in eight places. A capability record should link the relevant evidence in each layer:

```text
human source
  → product outcome
  → requirement
  → architecture/decision
  → implementation
  → test/quality oracle
  → runtime or pilot evidence
  → release/operations
  → SOTA/competitive baseline
```

A layer may be `N/A`, but only with a rationale. The objective is complete explainability and machine-verifiable coverage, not repetitive documentation.

## Immediate evidence-backed concerns

These are triage signals, not final repository dispositions.

1. **The ecosystem index is stale by its own admission.** The narrative map reports an older 111-repository taxonomy and points to an 88-repository machine catalog, while the connected account now exposes 146 owned repositories. Registry repair is therefore prerequisite work.
2. **FocalPoint authority is contradictory.** `phenotype-apps` presents a large FocalPoint product, while `FocalPoint` currently describes itself as “Phenotype-org dependency management.” The two histories and branches require forensic reconciliation.
3. **Planify has two competing homes.** Both `Planify` and `Planify2` call themselves Planify; one is an upstream-style Plane fork and the other claims to be the consolidated fork. A lineage and consumer decision is required.
4. **The governance spine points to a missing active authority.** Current documentation names `phenotype-org-governance`, while the observed account contains an archived `zz-archive-phenotype-org-governance` rather than an active exact-name authority.
5. **`pheno` is a shelf encoded as a repository.** Its own README describes a directory containing independent repositories. That may be useful locally, but it is not automatically a product or canonical code authority.
6. **Generic foundations have overlapping ownership.** `phenoAI` claims model routing, MCP plumbing, and embeddings while several dedicated router, gateway, MCP, and SDK repositories exist.
7. **The agent execution family has duplicate surface claims.** `thegent`, `Agentora/agentkit`, `substrate`, `Tasken`, `Sidekick`, `PhenoProc`, and ShareCLI all touch execution, agents, processes, or orchestration. They may represent layers, but the current boundaries are not self-evident.
8. **Archived AGSLAG sources leave a strategic-authority question.** Prior architecture treats AGSLAG as the portfolio allocator, but current visible lineage is primarily in archived `zz-agslag` material and adjacent specifications.

## Program invariants

- No repository is deleted merely to improve a count.
- No historical repository is treated as irrelevant; archives participate in lineage and intent recovery.
- No README, badge, completion percentage, test count, or recent timestamp is accepted as proof by itself.
- No agent may approve its own cross-repository authority claim.
- No richer local intent/docs system is replaced with a weaker standard tree. The common contract is a minimum capability schema, not a forced folder layout.
- No project is declared complete because documentation exists.
- No quality suite is trusted until negative controls or mutation evidence show that it can fail.
- No pilot is accepted unless the compared implementations solve the same bounded problem under declared conditions.
- No new repository is permanent by default. Incubators require an expected landing zone, review date, and graduation/absorption criteria.
- No consolidation is complete until consumers, history, releases, URLs, data, documentation, and compatibility obligations are handled.

## Target-state hypothesis

The expected shape is a **polyrepo of bounded products and boring foundations**, not one monorepo and not 146 equally prominent projects:

```text
Portfolio governance and evidence
├── strategy/resource authority
├── governed work/specification authority
├── labor/agent execution authority
├── trace/evidence authority
└── specialized ledgers

Shared foundations
├── protocol and identifiers
├── SDKs by stable consumer boundary
├── observability
├── plugins/adapters
├── operations and CI
└── registry/catalog

Developer and runtime products
├── coding-agent workbench/CLI family
├── process and compute runtime
├── provider routing/gateways
├── MCP products
└── deployment/compute tooling

Applied products
├── civic
├── focus/productivity
├── worlds/game/graphics
├── creative/media
└── other independently justified products

Controlled exceptions
├── strategic upstream-derived forks
├── active labs/incubators
└── immutable archives/provenance
```

The audit must determine the exact members and boundaries.

## First program move

Create one current machine-readable inventory and capability registry, then freeze new repository births except through an explicit incubation record. Run two lanes in parallel:

- **Authority lane:** repair registry, governance, cross-repo IDs, and output schemas.
- **Closure lane:** finish obvious small contradictions and duplicate families to terminal decisions.

Do not begin 146 independent “improve docs” agents before those contracts exist. That would amplify inconsistency.
