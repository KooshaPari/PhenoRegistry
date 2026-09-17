# Repository boundary and portfolio topology policy

## Objective

Partition the capability graph into repositories that minimize total coordination and cognitive cost while preserving real lifecycle, security, licensing, release, deployment, consumer, and ownership boundaries.

The objective is not “fewest repositories.”

A useful conceptual cost function is:

\[
J =
\alpha W +
\beta D +
\gamma X +
\delta U +
\epsilon R +
\zeta A +
\eta B
\]

Where:

- `W`: portfolio width—number of active authorities an operator/agent must discover and monitor.
- `D`: repository depth—semantic breadth, context size, internal coupling, and build scope.
- `X`: cross-repository change cost and release choreography.
- `U`: duplicated implementations, contracts, documentation, and authority.
- `R`: independent release/CI/dependency overhead.
- `A`: authority ambiguity and conflicting product claims.
- `B`: blast radius from overly broad repositories.

Hard constraints include licensing, access, trust, independent deployment, upstream lineage, and compatibility obligations.

“Cubeifying” the portfolio means balancing width, depth, and coupling—not forcing a geometric count.

## Five counts to manage

The registry must publish:

```yaml
counts:
  raw_repositories: 146
  non_archived_repositories: <observed>
  operational_repositories: <audited>
  canonical_authorities: <audited>
  public_product_brands: <audited>
  active_incubators: <audited>
  strategic_forks: <audited>
  archive_lineage_repositories: <audited>
```

The target applies primarily to operational and canonical counts. Historical GitHub URLs can remain.

## Independent repository survival test

A repository has a strong reason to remain independent when one hard boundary or several strong soft boundaries exist.

### Hard boundaries

- Incompatible license or third-party provenance.
- Distinct public upstream/fork relationship requiring independent sync and patch history.
- Separate security/access-control or trust domain.
- Independently deployed service with incident and rollback isolation.
- Separate legal/compliance/data-residency obligations.
- Public protocol/schema authority used across products.
- External community or governance that cannot share a release process.

### Strong soft boundaries

Score each 0–3:

| Dimension | Question |
|---|---|
| User job | Does it solve a coherent, independently explainable job? |
| Adoption | Can a user discover, install, and value it independently? |
| Release | Does it need independent semantic versioning/support? |
| Consumers | Are there multiple real consumers outside its parent? |
| Deployment | Is it independently deployed/scaled/operated? |
| Churn | Does its change rate materially differ from neighbors? |
| Ownership | Is there distinct ownership or contributor community? |
| Build scale | Does isolation materially reduce build/test burden? |
| Platform | Does a platform-specific lifecycle justify isolation? |
| Reuse | Is reuse contractual rather than speculative? |

Penalties:

| Penalty | Question |
|---|---|
| Duplicate authority | Does another repo claim the same canonical job? |
| Coupled change | Do most meaningful changes require synchronized PRs elsewhere? |
| No consumers | Is “shared” code consumed only by one parent? |
| Brand noise | Does independent presentation confuse users? |
| Release theater | Are versions/releases produced without independent compatibility meaning? |
| Generic scope | Does the repository have no defensible boundary beyond “common,” “AI,” or “utils”? |

A score can guide investigation, but never override a hard boundary or consumer evidence.

## Repository role taxonomy

Every surviving repository gets one primary role:

- `FLAGSHIP_PRODUCT`
- `APPLIED_PRODUCT`
- `DEVELOPER_PRODUCT`
- `RUNTIME_OR_SERVICE`
- `SDK`
- `PROTOCOL_OR_SCHEMA_AUTHORITY`
- `FOUNDATION_PACKAGE_HOME`
- `PLUGIN_OR_ADAPTER_COLLECTION`
- `STRATEGIC_UPSTREAM_FORK`
- `PACKAGING_OR_DISTRIBUTION`
- `OPERATIONS_OR_INFRASTRUCTURE`
- `GOVERNANCE_OR_REGISTRY`
- `DOCUMENTATION_PORTAL`
- `LEDGER_OR_DURABLE_AUTHORITY`
- `LAB_OR_INCUBATOR`
- `ARCHIVE_OR_PROVENANCE`

Secondary roles are permitted, but one role must explain why the repository boundary exists.

## Disposition taxonomy

At component granularity, select:

- `RETAIN_AND_REFOCUS`
- `ABSORB_WHOLE`
- `SPLIT_ACROSS_TARGETS`
- `MERGE_WITH_SEMANTIC_PEER`
- `EXTRACT_SHARED_LIBRARY`
- `EXTRACT_PROTOCOL_OR_SDK`
- `PRODUCTIZE`
- `CONVERT_TO_STRATEGIC_FORK`
- `CONVERT_TO_ADAPTER_OR_PACKAGING`
- `REIMPLEMENT_BEHIND_CONTRACT`
- `PRESERVE_AS_REFERENCE`
- `ARCHIVE_WITH_TOMBSTONE`
- `INTENTIONALLY_RETIRE`
- `INCUBATE_WITH_TTL`
- `RESEARCH_OR_UNRESOLVED`

Repository-level disposition is derived from its components; it is not assumed to be one-to-one.

## Rules for generic repositories

Names such as `shared`, `common`, `core`, `AI`, `kit`, `utils`, or `pheno` are warning signals, not automatic failures.

A generic foundation home is valid when:

- It has a deliberately boring internal-package role.
- Dependency direction is clear.
- Packages have stable owners and consumers.
- It does not claim a broad user-facing brand.
- It does not become a dumping ground.
- Extraction rules prevent circular dependencies.
- Independent packages can be versioned or released appropriately.

Decompose a generic repository when it contains distinct user jobs, release cadences, security boundaries, or mutually unrelated capability communities.

Absorb it when it is mostly one consumer’s internal code.

Rename/refocus it when the implementation is coherent but the current name hides the boundary.

## Rules for tiny repositories

Small size is not sufficient reason to absorb.

Keep a tiny repo when it owns a stable public protocol, schema, independently versioned SDK, packaging channel, strategic fork, or high-leverage multi-consumer contract.

Absorb a tiny repo when:

- It has one real consumer.
- Releases have no independent compatibility meaning.
- It duplicates utility code.
- It exists only because an agent wanted an isolated work area.
- Its changes routinely require a parent change.
- Discovery and CI overhead exceed isolation benefit.

A package workspace with clear directories is preferable to dozens of one-crate repos when they share ownership and release semantics.

## Incubator repository policy

Standalone incubation is allowed because focused context can accelerate uncertain work. It is not a permanent default.

Every new incubator must include:

```yaml
incubator:
  hypothesis: <what is being learned or built>
  sponsor_product: <likely parent or "independent candidate">
  expected_landing_zone: <repo/path or decision date>
  birth_date: <date>
  review_dates: [30d, 60d, 90d]
  maximum_initial_budget: <compute/time/cost>
  graduation_criteria:
    - independent user job
    - evidence of reuse or adoption
    - stable release/security boundary
  absorption_criteria:
    - one dominant consumer
    - shared lifecycle with parent
  termination_criteria:
    - hypothesis falsified
    - no owner or consumer
  status: ACTIVE_INCUBATOR
```

Rules:

- Incubators do not become public flagships automatically.
- The registry limits simultaneous active incubators.
- A 90-day review must result in graduation, absorption, extension with evidence, or archive.
- The expected landing zone is recorded at birth.
- Source history is preserved when absorbed.

## Strategic fork policy

A fork is not portfolio clutter when it has a deliberate function. Each maintained fork needs:

- Upstream repository and pinned base.
- Original versus upstream-derived capability map.
- Patch queue and divergence register.
- Sync cadence and conflict policy.
- Security/advisory intake.
- Compatibility target.
- Release naming that does not imply false authorship.
- Exit conditions: upstream acceptance, replacement, permanent divergence, or archive.
- Tests against both upstream compatibility and local differentiators.

Forks are counted separately from original product brands.

If upstream synchronization is intentionally severed and the project becomes a distinct product, document the lineage and new contract. Do not retain ordinary “fork” documentation forever after semantics have changed.

## Archive and provenance policy

Archives remain in lineage scope but not necessarily operational count.

Archive only when:

- Replacement or terminal rationale exists.
- Consumers and package references are migrated or explicitly unsupported.
- History and release artifacts are preserved.
- README/tombstone identifies successor and last supported state.
- Security and data implications are handled.
- Registry status is updated.

Deletion is exceptional. It requires redundant provenance, no meaningful external URL or consumer value, no license/attribution need, and explicit authorization.

## Collection and register-style repositories

A collection repo is legitimate when its members share:

- one audience;
- one governance model;
- compatible release lifecycle;
- common tooling and quality gates;
- clear internal boundaries;
- no need for independent public identity.

Examples might include plugin packs, language-specific SDK families, infrastructure modules, or related micro-tools.

A registry repo should own metadata and identity, not silently vendor every implementation. Generated indexes must clearly identify source authorities.

## Monorepo versus polyrepo decision

Use a monorepo/workspace when:

- components change together;
- a shared release or atomic refactor is valuable;
- consumers are internal;
- one security/ownership domain applies;
- build tooling can preserve scoped work and caching.

Use separate repos when:

- release, security, licensing, deployment, upstream, or external-user boundaries dominate;
- independent adoption matters;
- consumers require stable contracts and decoupled cadence.

Agents can work effectively in a large repo only when ownership, paths, interfaces, tests, and build targets permit narrow context. A large repo without enforceable internal boundaries is not solved by telling agents to focus on one folder.

## Target count hypothesis

Before detailed adjudication, use this range as a planning prior:

| Tier | Hypothesis |
|---|---:|
| Public product/brand repositories | 10–20 |
| Core platform and durable authorities | 8–15 |
| Shared foundations/SDK homes | 8–15 |
| Strategic forks/adapters/packaging | 6–12 |
| Applied products outside the central platform | 8–15 |
| Active labs/incubators at one time | 3–6 |
| Canonical active/maintenance total | 45–70 |
| Archived/provenance repositories | Separate; raw count may remain much higher |

The previous 32-plus-forks hypothesis is a useful lower-bound alternative, while the user’s 50–100 range is a useful operational constraint. Neither is accepted until component, consumer, and lifecycle evidence is complete.

## Repository birth RFC

No new repository after registry freeze without:

1. Proposed role and one-sentence contract.
2. Why a package/branch/worktree in an existing repo is insufficient.
3. Sponsor and expected consumers.
4. Release/security/licensing boundary.
5. Expected landing zone if incubating.
6. 30/60/90-day decision schedule.
7. CI, ownership, archive, and provenance plan.
8. Impact on public brand count and dependency graph.
9. Central approval ID.

This preserves focused experimentation without recreating uncontrolled width.
