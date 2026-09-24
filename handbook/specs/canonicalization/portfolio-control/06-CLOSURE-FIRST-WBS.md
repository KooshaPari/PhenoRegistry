# Closure-first portfolio work breakdown structure

## Delivery philosophy

The program should produce **terminally useful repositories**, not broad activity.

Bad pattern:

```text
146 repos × 10% improvement = 146 unfinished repos plus coordination debt
```

Target pattern:

```text
authority prerequisites
  + smallest high-leverage closure units
  + bounded family waves
  → progressively fewer unfinished authorities
```

The program uses two parallel lanes:

- **Lane A — control spine:** inventory, IDs, policy, registry, work/evidence contracts.
- **Lane B — closure factory:** close one repo or one inseparable family at a time.

Lane A prevents agents from producing incompatible local truths. Lane B prevents governance work from becoming an endless meta-project.

## Definition of a closure slice

A closure slice is the smallest bounded unit that produces a terminal outcome:

- A retained repo reaches its declared gate and has a working first-value journey.
- A duplicate family receives an approved authority and migration map.
- A tiny repo is absorbed with history/provenance and consumers migrated.
- A fork receives a valid upstream/divergence contract.
- A lab receives an explicit hypothesis, TTL, and next decision.
- An archive receives a truthful tombstone and successor.
- A product receives a pilot disposition.
- A blocked repo receives a precise decision/evidence gate rather than vague “work remains.”

A PR that adds generic docs but leaves role and ownership unresolved is not closure.

## Prioritization score

Use for queue order, not final authority decisions:

\[
Priority =
\frac{
3U + 3E + 2C + 2R + 2D + L
}{
W + 2X + 2M + H
}
\]

Where:

- `U`: immediate user value unlocked.
- `E`: ecosystem dependency unblock.
- `C`: credibility/truth-hygiene gain.
- `R`: repository-count/authority reduction.
- `D`: degree of near-completion.
- `L`: learning or reusable migration leverage.
- `W`: remaining work.
- `X`: uncertainty.
- `M`: migration/conflict risk.
- `H`: required historical depth.

Also apply hard ordering dependencies. A tiny cleanup that depends on an unresolved authority does not leap ahead simply because it is easy.

## WIP limits

At any time:

- 1 portfolio authority wave.
- 2 family adjudications.
- 3 repository closure implementations per family.
- 1 major pilot per family.
- 1 independent verification queue.

Do not launch 146 free-running agents.

## Phase 0 — Observation freeze and portfolio control

### P0.1 Confirm inventory

- Produce the exact 146-repository machine catalog.
- Capture visibility/archive/fork/default-branch/ref metadata.
- Identify inaccessible local-only histories.
- Assign stable `REP-*` IDs.
- Record observation timestamp and source.
- Reconcile GitHub reality against existing registry files.

**Done when:** the catalog is reproducible and stale projections are labeled.

### P0.2 Freeze repository births

- Require birth RFC for new repos.
- Register current incubators.
- Establish expiry/graduation/absorption dates.
- Exempt emergency security and upstream fork mirrors with explicit reason.

### P0.3 Establish central schemas

- Capability records.
- Repository assessments.
- Evidence and claim records.
- Disposition decisions.
- Agent handoffs.
- Work and trace IDs.

### P0.4 Create the adjudication board

- Portfolio adjudicator.
- Family leads.
- Repository closure agents.
- Independent verifiers.
- Human-decision queue.

## Phase 1 — Repair the authority spine

This is the critical path because every later agent needs a reliable index and contract.

### P1.1 Registry reconciliation

Scope:

- `phenotype-registry`
- current GitHub inventory
- `RepoLedger`
- historical ecosystem maps
- repository catalog generators

Decide whether `RepoLedger` owns live repository facts while `phenotype-registry` owns curated canonical roles and relationships. Avoid two writable inventories of the same facts.

### P1.2 Specification authority

Scope:

- `PhenoSpecs`
- per-repo specs/AgilePlus bundles
- `AgilePlus`
- `phenotype-traceability-spine`

Likely principle:

- Product-local requirements/specs stay with the product or AgilePlus authority.
- Cross-product protocols and decisions live in a cross-ecosystem RFC/spec home.
- The central registry indexes; it does not copy every product spec.

This remains to be adjudicated.

### P1.3 Conventions and documentation

Scope:

- `PhenoHandbook`
- `phenodocs`
- product-local docs
- `phenoDesign`
- `phenotype-landing`

Likely principle:

- Handbook owns reusable conventions.
- Phenodocs federates/publishes and is not source authority.
- Product docs remain with product.
- Design-system authority needs explicit ownership.
- Landing/portfolio sites are projections.

### P1.4 Enforcement authority

The documented active `phenotype-org-governance` authority is absent under that exact active name. Decide whether enforcement belongs in:

- a restored/new governance repo;
- `.github`;
- `phenotype-ops`/`phenotypeActions`;
- `phenotype-tooling`;
- or a layered combination with one canonical policy owner.

Do not leave references pointing to an archived name.

**Phase 1 exit:** one authority map, one generated current catalog, no unexplained writable duplicates.

## Phase 2 — Rapid contradiction closures

These deliver immediate reduction and establish migration patterns.

### P2.1 Monitoring/proxy micro-family

Scope:

- `vibe-monitor`
- `vibeproxy-monitoring`
- `vibeproxy-monitoring-unified`
- `vibeproxy`
- archived `zz-archive-phenoRouterMonitor`

Tasks:

- Determine whether these are source, deployment, dashboards, or empty staging.
- Preserve useful history.
- Select one monitoring home or absorb into routing/observability.
- Tombstone empty/superseded repos.
- Verify consumers and deployment references.

### P2.2 Planify lineage

Scope:

- `Planify`
- `Planify2`
- AgilePlus UI integrations
- upstream Plane lineage

Tasks:

- Compare refs, upstream bases, local patches, licenses, consumers, and release intent.
- Select one maintained fork or a deliberately vendor-snapshot strategy.
- Preserve patch lineage.
- Remove duplicate product naming.
- Decide whether the landing site belongs in a generic site home.

### P2.3 FocalPoint lineage

Scope:

- `FocalPoint`
- `phenotype-apps`
- relevant historical fitness/focus repos

Tasks:

- Recover exact product and extraction history.
- Determine which repo contains strongest code, docs, prompts, tests, releases, and current consumers.
- Select canonical product home.
- Forward-port unique capabilities.
- Repair names, build claims, and registry.
- Keep public URLs/compatibility where worthwhile.

### P2.4 Shelf/meta repositories

Scope:

- `pheno`
- `KooshaPari`
- local workspace/shelf repos
- archived workspace snapshots

Tasks:

- Separate local checkout orchestration from public product code.
- Replace vendored/misaligned shelf claims with manifest tooling or workspace config.
- Decide whether a meta repo has a real operational role.
- Avoid a repository pretending to contain independent Git repos when the canonical source is elsewhere.

## Phase 3 — Foundation compression

Audit and consolidate small/generic libraries by consumer and capability rather than name.

Candidate set includes:

- Configra/Conft.
- Logify/pheno-tracing/PhenoObservability.
- PhenoContracts/event/schema packages.
- phenoUtils/HexaKit/phenokits-commons/rich-cli-kit/clap-ext.
- AuthKit/DataKit/Apisync/Stashly/ResilienceKit/PolicyStack.
- PhenoVCS.
- PhenoPlugins and plugin utilities.
- language SDKs.

For each:

1. Find actual consumers across refs.
2. Determine release and license boundary.
3. Compare APIs and duplicate implementations.
4. Select package home.
5. Create compatibility re-exports if needed.
6. Migrate consumers in dependency order.
7. Archive/tombstone sources only after evidence.

Prefer several coherent foundation homes over one universal `shared` repo or dozens of one-consumer repos.

## Phase 4 — Execution and agent family adjudication

### P4.1 Labor and orchestration authority

Compare:

- thegent.
- Agentora/agentkit.
- substrate.
- Tasken.
- Sidekick.
- PhenoProc.
- ShareCLI.
- agentapi-plusplus.
- context-mode-plusplus.

Provisional role hypothesis to test:

- `thegent`: agent labor/orchestration and execution economics.
- `Agentora/agentkit`: reusable agent SDK/framework and contracts, only if independent pilot/consumers justify it.
- `ShareCLI`: standalone OS-adjacent process/agent workload supervisor.
- `substrate`: runtime/adapters only if not duplicate of thegent/Agentora.
- smaller surfaces: absorb or become packages/adapters.

Do not merge until capability and consumer maps establish the layers.

### P4.2 Helios family

Use known intended roles as hypotheses:

- HeliosLab: internal desktop coding-agent workbench.
- forgecode: terminal-first coding-agent CLI/TUI.
- helios-cli: headless automation, harness, recording/replay.
- Agentora: underlying agent framework.

Investigate semantic overlap and the historical consolidation branch. Preserve distinct repos only when user job, release, or upstream lineage supports them.

### P4.3 MCP family

Compare:

- MCPForge.
- PhenoFastMCP.
- PhenoMCPServers.
- mobile-mcp.
- substrate MCP components.
- phenoAI MCP code.
- upstream-derived implementations.

Separate framework, server collection, routing/runtime, SDK, and app-specific adapters. One repository per layer may be valid; multiple claims per layer are not.

## Phase 5 — Routing, gateway, and strategic fork family

Scope:

- OmniRoute.
- bifrost.
- cliproxyapi-plusplus.
- vibeproxy.
- phenotype-router.
- phenotype-gateway.
- homebrew-omniroute.
- archived omniroute-rust.
- adjacent monitoring.

Deliver:

- Upstream/lineage map.
- Route/gateway/proxy semantic model.
- Original differentiator inventory.
- One canonical public routing product hypothesis.
- Adapter/fork roles and packaging.
- Compatibility and migration plan.
- Performance, reliability, provider, and developer-experience pilot.

Because these repositories are large and upstream-derived, do not treat them as quick merges.

## Phase 6 — Compute, fleet, inference, and virtualization

Scope:

- hwLedger.
- phenotype-omlx.
- phenotype-unsloth-studio.
- turboquant.
- hfscope.
- model-conductor-hub.
- localbase3.
- nanovms.
- phenotype-fleet-ops.
- NetWeave.
- local-ops.

Map:

- Hardware/capacity ledger authority.
- Inference runtime/fork.
- Model training/studio.
- Quantization.
- Fleet orchestration.
- Sandbox/VM runtime.
- Network/fabric.
- Marketplace/remote capacity experiments.

Use the distributed compute/I/O fabric specification as a target input, but do not force every experiment into one repo before boundaries and maturity are proven.

## Phase 7 — Applied-product families

Run independently after shared authority is stable.

- Civic: Civis/CivicSurvival-public.
- Focus/productivity/mobile: FocalPoint family, PlayCua, mobile tooling, eyetracker history.
- Worlds/game/graphics: Dino, DINOForge, WorldSphere, Compound Spheres, QuadSGM, graphics substrate.
- Creative/media: Melosviz, Frostify, Synthia/Diffuse/Eidolon as applicable.
- Deployment/platform: BytePort and related infra.
- Other standalone products after role discovery.

Each product needs G1→G5 closure and a pilot/case study, but applied products need not be mechanically integrated into the synthetic-enterprise runtime to belong to the broader semantic ecosystem.

## Phase 8 — Public portfolio and retirement

- Select 6–12 primary proof repos for profile/pinning.
- Select 10–20 public product brands.
- Correct all public claims and upstream attribution.
- Publish ecosystem map by audience, not one overwhelming graph.
- Archive/redirect completed migrations.
- Enforce repo-birth and duplicate-authority checks.
- Measure operational count and agent navigation burden.

## First closure queue

Provisional, subject to dependency verification:

| Order | Closure unit | Why first |
|---:|---|---|
| 1 | Machine inventory + registry authority | Prerequisite for all agents |
| 2 | vibe monitoring micro-family | Small, obvious duplication/staging signal |
| 3 | Planify/Planify2 | Same public name and clear fork lineage problem |
| 4 | FocalPoint/phenotype-apps | Severe public authority contradiction |
| 5 | `pheno` shelf/meta role | Removes a misleading pseudo-product boundary |
| 6 | governance/spec/docs spine | Makes later outputs canonical |
| 7 | small foundation cluster 1 | High repo-count reduction with bounded consumers |
| 8 | Helios family | High user value and known role intent |
| 9 | Agentora pilot | Tests whether independent SDK role is deserved |
| 10 | thegent/substrate/Tasken family | Larger consolidation after contracts/pilot |

## Repository HMVP closure

For a retained product repo, the earliest meaningful terminal slice generally includes:

- Honest README and one-sentence boundary.
- Reproducible install/build.
- One end-to-end user journey.
- G1 docs for that slice.
- G2 red harness and G3 green implementation for that slice.
- Release artifact or local package smoke.
- Clear deferred horizon.
- Registry/authority entry.
- No critical contradictory claim.

It need not implement every future idea. It must be usable, truthful, and extensible without lying about completeness.

## Work package contract

Each work package includes:

```yaml
id: WP-...
closure_unit: <repo/family/capability>
goal: <terminal outcome>
predecessors: [...]
source_refs: [...]
target_refs: [...]
bounded_paths: [...]
decisions_required: [...]
tasks: [...]
acceptance:
  docs: [...]
  quality: [...]
  implementation: [...]
  pilot: [...]
evidence: [...]
negative_tests: [...]
consumer_migrations: [...]
rollback: [...]
abort_conditions: [...]
status: READY|BLOCKED|CLAIMED|REVIEW|DONE
```

## Agent scheduling

Schedule by dependency and closure value, not raw repo order.

- Central authority tasks run first.
- Independent easy closures run parallel.
- Family agents receive disjoint scopes.
- Cross-family decisions queue to the adjudicator.
- Independent verifier reviews terminal states.
- Failed or inconclusive pilots can reduce scope or retire a repo; they are useful outcomes.
