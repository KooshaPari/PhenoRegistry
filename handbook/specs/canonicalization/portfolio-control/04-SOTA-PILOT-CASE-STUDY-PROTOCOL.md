# SOTA, pilot, and comparative product-evidence protocol

## Purpose

The SOTA dossier answers:

- What problem or workflow existed before this project?
- What direct and indirect alternatives exist now?
- Which jobs are already solved adequately?
- Where does this product intend to match, trade, or win?
- Which claims can be evaluated before implementation?
- Which differentiators survive a fair executable pilot?
- Is maintaining this product worth its complexity and opportunity cost?

Written comparison is a planning gate. A pilot is an evidence gate. Neither substitutes for the other.

## Alternative taxonomy

For each product/capability family, distinguish:

1. Direct competitors.
2. Adjacent products that solve the user’s job differently.
3. Libraries/frameworks.
4. Protocols and platform primitives.
5. Internal/manual workflows.
6. Build-versus-buy/no-build options.
7. Research systems.
8. Upstream projects and forks.
9. Deprecated/legacy prior art.
10. Ecosystem combinations that outperform any single product.

Do not pad a “25 competitors” count with irrelevant primitives. Search broadly, then label the class. When fewer than 25 genuinely relevant candidates exist, document the bounded search and exclusion rationale rather than claiming a universal maximum.

## Evidence levels

| Level | Meaning |
|---|---|
| `S0 Inventory` | Candidate identified and classified |
| `S1 Source-backed` | Current primary documentation/source inspected |
| `S2 Semantic comparison` | Same job/capability mapped across alternatives |
| `S3 Reproduced` | Installed/executed under recorded conditions |
| `S4 Controlled pilot` | Same bounded problem and acceptance oracle |
| `S5 Operational case study` | Representative real workflow over time |

Vendor benchmarks remain `VENDOR_CLAIM` until reproduced.

## Written SOTA dossier

Before code closure, produce:

- User-job and workflow map.
- Direct/adjacent/primitive alternative inventory.
- Current versions, maintenance, platform, license, and source provenance.
- Feature/capability matrix with semantic definitions.
- Architecture and extension model.
- Setup and adoption friction.
- Security, privacy, trust, and deployment model.
- Interoperability and migration.
- Performance/scaling claims with exact measurement boundaries.
- Failure/recovery and operational burden.
- Pricing/cost when relevant.
- Strengths worth copying.
- Weaknesses worth avoiding.
- Constraints the target intentionally accepts.
- No-build and composition alternatives.
- Proposed must-not-lose floors and must-win wedge.
- Hypotheses and experiments for unresolved claims.

Do not score vague labels such as “easy,” “fast,” or “enterprise-ready” without operational definitions.

## Replace the impossible Pareto rule

The original aspiration—never worse in any way and not identical in every way—should become four enforceable policies.

### 1. Critical parity floor

For each target journey, define dimensions where regression is unacceptable. Examples:

- Data loss.
- Core correctness.
- Security boundary.
- Supported platform required by the target user.
- Latency deadline for a real-time workflow.
- Installation or recovery path essential to adoption.
- Compatibility contract already promised.

The target must meet or exceed the floor with evidence.

### 2. Explicit trade ledger

A disadvantage is acceptable only when:

- The dimension is classified tradeable.
- The magnitude is measured or bounded.
- The compensating user value is explicit.
- The affected user segment is identified.
- A fallback or migration exists where needed.
- The decision is recorded and can be revisited.

### 3. Must-win wedge or distinct job

A user-facing product must have at least one of:

- A material capability competitors lack.
- A substantially better end-to-end outcome.
- A valuable integration/composition competitors do not provide.
- A different target user or workflow.
- A lower total cost/risk/operational burden.
- A defensible platform-specific depth advantage.

“One more implementation of the same abstraction” is not enough.

### 4. Strategic-component exception

A shared library, adapter, fork, internal runtime, packaging repo, or compliance component can be justified by:

- Compatibility.
- Control.
- Reuse.
- Security.
- Cost.
- Supply-chain independence.
- Operational leverage.
- Upstream patch management.

It need not be novel as a standalone public product.

## Pilot selection

Choose a pilot that is:

- Representative of the project’s claimed value.
- Bounded enough to implement in multiple alternatives.
- Difficult enough to expose meaningful differences.
- Measurable with a common acceptance oracle.
- Free of irrelevant product-specific advantages.
- Reproducible on declared hardware/software.
- Useful even if the target loses.

A pilot should not be a toy hello-world when the product claims orchestration, scale, reliability, or developer experience.

## Pilot contract

Every pilot records:

```yaml
pilot:
  id: PILOT-<FAMILY>-001
  user_job: <bounded job>
  target: <repo/ref/version>
  alternatives:
    - <name/version/ref>
  environment:
    hardware: <declared>
    os: <declared>
    toolchains: <declared>
    network: <declared>
  inputs: <fixed fixture/workload>
  acceptance_oracle: <same for all>
  repetitions: <declared>
  warmup: <declared>
  resource_limits: <declared>
  dimensions:
    - correctness
    - time_to_first_value
    - implementation_effort
    - runtime_latency
    - throughput
  confounders: []
  failure_policy: <declared>
  raw_evidence_path: <path>
```

## Common comparison dimensions

Use the applicable subset, with definitions:

### User/product

- Time to understand the mental model.
- Time to install and first successful outcome.
- Number and severity of setup decisions.
- Error recovery.
- Discoverability.
- Accessibility.
- Documentation task success.
- Upgrade/migration friction.
- Platform and deployment reach.
- Workflow completeness.
- Trust and transparency.
- Offline/local-first behavior.
- Collaboration/multi-user behavior.

### Developer experience

- Lines/files/configuration required for the same outcome.
- Number of concepts and abstractions introduced.
- Type safety and schema quality.
- Debuggability and trace clarity.
- Testability and determinism.
- Extension/plugin ergonomics.
- API stability and compatibility.
- Dependency weight.
- Build and feedback-loop time.
- Failure locality.
- Refactor cost.
- Quality of defaults versus escape hatches.

LOC is not automatically better when lower; generated, declarative, and hidden complexity must be accounted for.

### Functional and semantic

- Exact capability coverage.
- State model.
- Concurrency and cancellation.
- Tool/resource composition.
- Persistence and recovery.
- Streaming.
- Human-in-the-loop and policy.
- Multi-agent/multi-user semantics.
- Versioning and migration.
- Interoperability.
- Observability and provenance.
- Security/permission model.
- Edge cases and unsupported states.

### Runtime and resource

- Correctness rate.
- Median and tail latency.
- Throughput under declared concurrency.
- CPU/GPU/NPU/memory/disk/network use.
- Startup and warmup.
- Scaling efficiency.
- Contention sensitivity.
- Thermal and energy behavior.
- Failure/retry amplification.
- Cost per accepted outcome.

### Operations and ecosystem

- Packaging and deployment.
- Release cadence and maintenance.
- Vulnerability response.
- License and vendor lock-in.
- Community/ecosystem.
- Integration availability.
- Monitoring and incident response.
- State portability.
- Support burden.
- Total ownership cost.

## Fairness rules

- Same user job and acceptance oracle.
- Same input data and comparable quality settings.
- Same or clearly normalized hardware/resource budget.
- Versions and configuration retained.
- Optimization effort budget declared for each alternative.
- Failed runs retained.
- Warm/cold behavior distinguished.
- Median, tails, variance, and confidence intervals where appropriate.
- Human setup/evaluation rubric defined before results.
- Target authors do not silently tune only their implementation.
- Missing competitor features are represented as unsupported, not zero-time successes.
- Alternative combinations are allowed when that is what a rational user would deploy.

## Agentora example

A serious Agentora/agentkit pilot would not merely instantiate one agent.

Candidate pilot: build a coding-agent service that:

- accepts a repository task;
- uses tools;
- maintains short and durable session state;
- streams progress;
- supports cancellation and retries;
- records traces and cost;
- runs N concurrent tasks;
- recovers from one tool/provider failure;
- emits a machine-verifiable patch and test result.

Implement the same bounded contract using:

- Agentora/agentkit.
- OpenAI Agents SDK.
- LangGraph/LangChain.
- CrewAI or another closest peer.
- A minimal direct SDK implementation as the no-framework baseline.

Measure developer effort, abstraction count, correctness, concurrency, observability, failure recovery, latency, cost, extension burden, and maintainability. A Codex clone is a larger later case study; the first pilot should isolate framework value without rebuilding an entire product.

## Pilot disposition outcomes

- `VALIDATED_WEDGE`: proceed and publish evidence.
- `PARITY_WITH_STRATEGIC_VALUE`: acceptable for internal/foundation/fork role.
- `TRADEOFF_ACCEPTED`: proceed with explicit segment and decision.
- `NO_DISTINCT_VALUE`: absorb, narrow, or retire.
- `TARGET_LOSES_CRITICAL_FLOOR`: block release or redesign.
- `INCONCLUSIVE`: define next experiment; do not market the claim.
- `ALTERNATIVE_COMPOSITION_WINS`: adopt/integrate instead of hand-rolling.
- `NEW_JOB_DISCOVERED`: redefine the product and rerun the comparison.

## Case-study package

Each qualifying product should eventually publish or retain:

```text
case-study/
├── README.md
├── contract.yaml
├── target/
├── alternatives/
├── fixtures/
├── acceptance/
├── measurements/
├── raw/
├── analysis.md
├── tradeoff-ledger.md
├── reproduction.md
└── decision.md
```

The product-facing article is a projection of this evidence, not the source of truth.

## Approval gate

A product is not approved for independent flagship treatment solely because it has a rich specification. It needs:

1. A distinct user job or validated wedge.
2. Critical floors met.
3. An executable or operational evidence path.
4. A maintenance and adoption case.
5. A boundary that survives the repository policy.

If the target is still research, retain the vision but label the repo as a lab/incubator rather than a completed product.
