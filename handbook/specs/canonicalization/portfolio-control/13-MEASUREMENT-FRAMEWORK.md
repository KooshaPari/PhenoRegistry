# Portfolio measurement framework

## Why measure

Without operational measures, consolidation becomes aesthetic and “completeness” becomes document count. Metrics must expose whether the portfolio is becoming easier to understand, safer to change, more useful, and more truthful.

## Count metrics

| Metric | Definition | Direction |
|---|---|---|
| Raw repos | All GitHub repos | Informational |
| Operational repos | Repos requiring active CI/dependency/triage/release work | Down unless justified |
| Canonical authorities | Independent durable product/protocol/state/policy owners | Down where duplicated, not minimized blindly |
| Public brands | Products a user must distinguish | Down to memorable set |
| Active incubators | Repos inside TTL window | Bounded |
| Strategic forks | Maintained upstream patch queues | Bounded and explicit |
| Unclassified repos | No terminal role | To zero |
| Authority conflicts | Same capability/entity with competing writers | To zero |
| Orphan capabilities | No owner | To zero |
| One-consumer shared repos | Shared claim with one verified consumer | Down |

## Width/depth/coupling measures

### Width

- Number of active repos in operator dashboard.
- Number of repos an agent must inspect to resolve one task.
- Median and p95 dependency fan-out.
- Number of independent release workflows.
- Number of stale dashboards/registries.

### Depth

- Number of distinct product jobs in one repo.
- Component/package count.
- Build/test time by scoped target and full repo.
- Context footprint for a representative task.
- Percentage of files required to understand a bounded change.
- Internal dependency cycles.
- Number of owners/security domains/licenses.

### Coupling

- Cross-repo PRs per feature.
- Co-change frequency.
- Lockstep releases.
- Duplicate contract/schema definitions.
- Circular dependencies.
- Broken consumers after release.
- Compatibility bridges past expiry.

Use these to evaluate “cubeification.”

## Completion measures

- Repos by G0–G6.
- Critical capabilities by weakest dimension.
- Unsupported public claims.
- Requirements without tests.
- Tests without requirement/behavior rationale.
- Implementations without current intent.
- Features present only in non-default branches.
- `N/A` entries lacking rationale.
- Research hypotheses without experiments.
- ADRs without status/reconsideration.
- Release artifacts without smoke evidence.

## Quality measures

- CI selection completeness.
- Negative-control pass rate: expected bad change is caught.
- Mutation score on critical logic.
- Flake rate.
- p50/p95 feedback-loop time.
- Platform matrix actually run.
- Dependency/security/license policy freshness.
- Packaging/install/upgrade/rollback journey success.
- Performance regression budget and variance.
- Soak/fault-recovery evidence age.

A green checkmark is not the metric; confidence in the oracle is.

## SOTA and pilot measures

- SOTA source freshness.
- Alternatives classified versus merely listed.
- Claims separated into vendor/reproduced/hypothesis.
- Pilots by evidence level.
- Products with defined critical floors.
- Products with validated wedge.
- Products with no distinct value.
- Total cost per accepted outcome.
- Counterexamples documented.
- Pilot reproducibility.

## Closure measures

- Terminal closure units per week.
- Median time from claim to independent verification.
- WIP age.
- Reopened terminal decisions.
- Migration bridges created/retired.
- Consumer adoption completion.
- Repos moved from ambiguous active to terminal state.
- Number of parallel partial initiatives.
- Work packages blocked by central decisions.

Optimize closure throughput, not commit volume.

## Truth-hygiene measures

- Registry observation age.
- Narrative projection age.
- Contradictory status statements.
- Broken/nonexistent cross-repo links.
- README versus manifest/release divergence.
- Fork attribution completeness.
- Archive successor coverage.
- Public “shipped” claims lacking released/reproduced evidence.
- Generated files edited by hand.
- Human-source provenance coverage.

## Agent-operability measures

- Time for a fresh agent to answer “where does capability X belong?”
- Percentage of tasks automatically routed to correct repo/package.
- Scope violations per agent run.
- Duplicate files/repositories created.
- Required context tokens/files for a bounded task.
- Handoff schema validity.
- Evidence rejected by verifier.
- Stale local projections.
- Mean time to resume from checkpoint.

## Public portfolio measures

- Time for a new user/recruiter to identify primary products.
- Successful install/first-value journeys.
- Number of pinned proof points with reproducible evidence.
- Public product names with overlapping descriptions.
- Forks clearly attributed.
- Case studies published.
- Product status accuracy.
- Support/maintenance expectations visible.

## Resource and economics

- CI minutes and dependency-update burden per active repo.
- Agent tokens/cost per closure.
- Reviewer hours.
- Build cache reuse.
- Storage and artifact cost.
- Maintenance cost by product.
- Compute assigned versus evidence/value produced.
- Opportunity cost of retained duplicate systems.

These metrics can eventually feed AGSLAG, but measurement authority should remain in the relevant systems.

## Initial dashboard

The first dashboard should show:

```text
146 raw
117 non-archived (initial metadata capture)
29 archived
? operational
? canonical authorities
? public products
? active incubators
? strategic forks
146 unadjudicated dispositions
12 central decisions open
```

Do not fill unknowns with guesses. The purpose of the audit is to resolve them.

## Success thresholds for the first program cycle

- 100% census with immutable observed refs.
- Zero stale-count claims presented without warning.
- One accepted authority map.
- First three contradiction families reach staged terminal decisions.
- New-repo birth gate active.
- At least one product reaches a fair G4 pilot disposition.
- At least one small foundation consolidation is completed with consumers passing.
- Closure WIP remains within policy.
- No source history is destroyed.
