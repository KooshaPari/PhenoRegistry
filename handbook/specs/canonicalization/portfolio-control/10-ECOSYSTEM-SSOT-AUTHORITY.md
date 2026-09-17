# Ecosystem SSOT and authority design

## Principle

There must not be one universal database merely to make the portfolio look unified. Each domain retains the authority that matches its transactional and lifecycle needs. The ecosystem shares stable identifiers, event envelopes, and trace relationships.

## Proposed authority separation to adjudicate

| Domain | Candidate authority | What it should own | What it should not own |
|---|---|---|---|
| Live GitHub repository facts | RepoLedger or generated inventory service | Repo IDs, refs, visibility, archive/fork state, topics, releases, packages, observations | Product valuation, specs, human intent |
| Curated ecosystem identity | phenotype-registry | Canonical role, capability ownership, relationships, lifecycle/disposition, public projections | Live Git internals, every product requirement |
| Product-local intent/specs | Product repo + AgilePlus linkage | Human sources, product requirements, feature specs, work packages | Cross-product protocols it does not own |
| Cross-product contracts/RFCs | PhenoSpecs or successor cross-product RFC home | Stable shared schemas, protocols, decisions, compatibility | Copies of every product’s local docs |
| Work lifecycle | AgilePlus | Features, WPs, claims, dependencies, evidence gates, lifecycle | Raw evidence blobs or agent labor economics |
| Agent labor | thegent | Agent workforce, delegation, execution economics, contracts | Canonical product requirements or trace truth |
| Process/compute supervision | ShareCLI and/or future fabric runtime | Host processes, contention, placement/runtime state | Strategic portfolio allocation |
| Trace/evidence | Tracera | Assets, trace links, coverage, impact, evidence, risk | Authoritative source-system state where another system owns it |
| Session operational memory | SessionLedger | Run capture, replay, continuation | Long-term product specs |
| External research | ResearchLedger | Sources, provenance, research assets | Product implementation status |
| Hardware capacity | hwLedger | Fleet inventory, capacity, fit, telemetry, cost observations | Strategic decisions about whether work should happen |
| Portfolio strategy/capital | AGSLAG successor | Mandates, theses, bets, resource allocation decisions | Implementation-level work status |
| Conventions | PhenoHandbook | Reusable patterns, anti-patterns, methodologies | Mandatory enforcement state |
| Enforcement | Active governance/ops authority to decide | Reusable CI/policy baselines, exceptions, control evidence | Product-specific business rules |
| Documentation federation | phenodocs | Searchable/published projections | Canonical source prose when owned elsewhere |

This is a target hypothesis. The audit must inspect current implementations, contracts, and consumers.

## Authority record

```yaml
entity_type: repository
authority:
  system: RepoLedger
  record_id: REP-001
  writers:
    - github-observer
  source_fields:
    - github_repository_id
    - observed_default_ref
projection:
  system: phenotype-registry
  derived_fields:
    - canonical_role
    - disposition
conflict_policy:
  live_fact: latest signed GitHub observation
  curated_role: accepted portfolio decision
```

Every field family needs one rule. “Both files are canonical” is prohibited unless they own different dimensions.

## Projection rules

- Generated files include source version, generation time, and generator version.
- Hand edits to generated projections fail validation.
- Stale projections display a visible warning.
- Consumers read machine data where possible.
- Human narrative links back to stable IDs.
- Local repositories may cache projections but do not become authorities.
- Archived authorities must name a successor or explicitly state that the domain has no active owner.

## ID namespace

Use stable typed IDs, independent of repo names:

- `REP-*` repository.
- `PROD-*` product.
- `CAP-*` capability.
- `JOB-*` user job.
- `INT-*` intent source.
- `FR-*`, `NFR-*`.
- `ADR-*`.
- `CTR-*` contract.
- `WP-*`, `TASK-*`.
- `TEST-*`, `BENCH-*`, `PILOT-*`.
- `EVD-*`.
- `REG-*` regression.
- `RISK-*`.
- `DEC-*` portfolio decision.
- `MIG-*` migration.

Names and repositories can change without breaking trace identities.

## Repository-local artifact relationship

A product repository should keep the information needed to understand, build, verify, operate, and contribute to that product. It references cross-product authorities rather than copying them.

Example:

```text
product repo
├── docs/intent/              local human/product sources
├── docs/specs/               local product/feature contracts
├── docs/adr/                 local architectural decisions
├── docs/sota/                local market/technical analysis
├── docs/verification/        local evidence contracts
├── catalog-info.yaml         identity + authority references
└── generated/
    └── ecosystem-projection  read-only generated context
```

Existing richer layouts remain valid when they satisfy the capability contract.

## Conflict adjudication

When artifacts disagree:

1. Identify field/domain, not whole-file winner.
2. Determine canonical authority at the relevant historical time.
3. Check explicit supersession/decision.
4. Compare source evidence and implementation.
5. Preserve historical record.
6. Issue a `DEC-*` or `REG-*` finding.
7. Update the authority and regenerate projections.
8. Do not silently edit all copies by hand.

## Specific current authority issues

### Registry count and freshness

A current observation service must refresh all 146 repos and drive the narrative map. The existing stale map cannot be used as the sole worker input.

### Product-local versus central specs

PhenoSpecs currently claims broad central specification authority. AgilePlus and major repos also own detailed specs. The likely correction is:

- cross-product protocols/ADRs central;
- product intent and feature specs local;
- AgilePlus owns lifecycle/work state;
- registry owns links.

This requires an explicit migration decision.

### Enforcement

The referenced active governance repo is absent under its current exact name. Enforcement must receive an active canonical owner before agents rely on it.

### AGSLAG

If AGSLAG remains the strategy/capital authority, restore or create a clear current canonical home from archived source and accepted newer architecture. If that job is absorbed elsewhere, publish an explicit supersession. Do not leave the top layer as folklore.

### FocalPoint and Planify

These require field-level authority decisions after history review; a README edit is not sufficient.

## Central adjudication queue

Cross-repo decisions are represented as:

```yaml
id: DEC-ECO-001
question: Which repo is canonical for FocalPoint?
status: INVESTIGATING
candidates:
  - KooshaPari/FocalPoint
  - KooshaPari/phenotype-apps
evidence_required:
  - intent lineage
  - branch ancestry
  - capability matrix
  - consumers
  - build and release reproduction
decision_owner: portfolio-adjudicator
```

Repo agents submit evidence against the decision. They do not resolve it unilaterally.

## Minimal machine interfaces

The future registry should support:

```text
repo get <REP-ID>
capability owner <CAP-ID>
capability search <term>
authority explain <entity/field>
lineage show <repo/component>
decision queue
closure next
consumer graph <repo/package>
projection generate --audience public|developer|operator|history
```

That is more useful to agents than another prose-only map.
