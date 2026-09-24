"""Original candidate predicates; no historical-count or certification claim."""
DOMAINS = [
 ('D01','Intent and value'),('D02','Research and decision quality'),('D03','Scope and capabilities'),
 ('D04','Architecture and tradeoffs'),('D05','Implementation and maintainability'),('D06','Test and assurance quality'),
 ('D07','Developer experience'),('D08','Agent experience'),('D09','User experience'),
 ('D10','Accessibility and internationalization'),('D11','Visual and interaction polish'),('D12','Performance and resource use'),
 ('D13','Reliability and operations'),('D14','Security and trust'),('D15','Data stewardship'),
 ('D16','Distribution and adoption'),('D17','Governance and evidence integrity'),('D18','Viability and lifecycle')]
PILLARS=[]
def add(d,title,mode,scope,method,items):
 rows=[s.strip() for s in items.strip().split('\n') if s.strip()]
 assert len(rows)==10,(d,title,len(rows))
 PILLARS.append(dict(domain_id=d,title=title,mode=mode,applicability=scope,procedure=method,predicates=rows))

add("D01","Mandate and delegated authority","SEMANTIC","all subjects","Resolve actual host permissions and parent mandates; compare each selected action with explicit scope and counterexamples outside that scope.", '''
The current work has an identifiable source of delegated authority.
The mandate distinguishes permitted observation from permitted mutation.
Resource limits remain cumulative across replacement agent sessions.
Subdelegation does not enlarge the delegating actor's actual permissions.
Reserved sponsor decisions are distinguishable from routine agent decisions.
Expiration or revocation of authority has an actionable stop condition.
Conflicting mandates have an explicit precedence resolution.
External effects have permissions separate from local experimentation.
The permitted subject set excludes unrelated repositories and devices.
An agent can proceed with independent authorized work when another action is blocked.
''')
add("D01","Beneficiary and problem hypothesis","SEMANTIC","all subjects","Trace the problem to observations or explicitly hypothetical consumers; compare the proposed outcome against current behavior and the no-build alternative.", '''
The proposed beneficiary is distinguishable from the builder role.
The beneficiary's current problem is stated as observable friction.
Evidence status distinguishes a hypothesized problem from an observed problem.
The frequency of the problem has a declared observation basis.
The consequence of leaving the problem unsolved is articulated.
The expected beneficiary context matches the intended deployment context.
Conflicting beneficiary needs remain visible rather than averaged away.
An internal agent consumer is identified by a real workflow or a labeled proposed workflow.
The problem statement does not assume the proposed implementation is necessary.
A refutation condition exists for the problem hypothesis.
''')
add("D01","Value and outcome contracts","SEMANTIC","all subjects","Create a before/after outcome contract with baseline, unit, observation window and disconfirmation; distinguish evidence collection from benefit.", '''
The intended improvement is expressed in beneficiary-observable terms.
The baseline includes the existing workaround where one exists.
Success thresholds have a stated rationale rather than arbitrary round numbers.
Outcome measurements have explicit observation windows.
Benefits and costs use comparable scope and units.
A technically passing result can still be classified as value-unproven.
Negative consequences of the proposed improvement are considered.
The outcome contract identifies conditions under which improvement would not generalize.
An outcome owner can obtain the required observation without relying on builder testimony.
The outcome hypothesis names a practical discriminating experiment.
''')
add("D01","Agent-derived intent and repository genesis","SEMANTIC","subjects created or materially reshaped by agents","Reconstruct lineage without inventing history; compare repository separation to a module, package, existing owner, upstream reuse and no build.", '''
Intent authorship is recorded separately from intent acceptance.
Derived intent links to its parent capability or mandate.
An absent historical origin is reported as a provenance gap.
The repository boundary has an explicit consumer-facing responsibility.
Separate release cadence is justified when used to motivate a new repository.
Cross-boundary coupling costs are included in the decomposition decision.
An existing-owner alternative was evaluated before creating duplicate authority.
The repository has an absorption or reversal trigger.
The proposed repository name is not used as evidence of product necessity.
Accepted current intent is not falsely attributed to the original creation event.
''')
add("D01","Alternatives and non-goals","SEMANTIC","all subjects","Compare feasible competing approaches against the same outcome and constraints; preserve rejection reasons and counterevidence.", '''
The no-action alternative is evaluated on the same outcome as building.
An upstream or off-the-shelf alternative is considered when relevant.
A smaller scope alternative is considered before adding infrastructure.
Non-goals exclude concrete tempting work rather than vague categories.
Rejected alternatives retain the evidence supporting rejection.
The chosen approach has identifiable conditions under which another alternative wins.
Tradeoffs include ongoing maintenance rather than construction alone.
Constraints are distinguished from inherited preferences.
New evidence can reopen a previously rejected alternative.
A brainstorm is not promoted to a mandatory requirement without a decision.
''')
add("D01","Feedback and intent amendments","SEMANTIC","subjects receiving sponsor, consumer or agent feedback","Classify feedback, preserve its source, apply actual authority, and compare prior and amended intent without rewriting observed facts.", '''
Feedback is classified as instruction, preference, observation, question, brainstorm or override.
The original feedback and its operational interpretation are distinguishable.
A preference change does not retroactively alter historical test observations.
Binding scope changes identify the assignment epochs they invalidate.
Ambiguous reversible ideas can become bounded experiments without fabricated certainty.
Ambiguous authority for irreversible actions remains unresolved.
Conflicting feedback is reconciled using explicit priority and evidence.
A major intent change preserves the previous accepted version.
Amendments identify consumers affected by the change.
The amendment record separates changed goals from newly learned facts.
''')

add("D02","Source provenance and acquisition","STRUCTURAL","subjects using research or external evidence","Inspect source records against accessible originals; verify identity, retrieval scope, versions and rights without fabricating unavailable content.", '''
Each material research claim has an identifiable source record.
Source records distinguish primary evidence from secondary interpretation.
Retrieval timestamps are recorded separately from publication dates.
Versioned software evidence identifies the inspected revision or release.
Unavailable or access-blocked sources remain explicit acquisition gaps.
Quoted passages preserve the meaning of their source context.
Source acquisition preserves the original content digest when permitted.
Mirrors and reposts are not counted as independent corroboration.
Rights restrictions are recorded before redistributing source material.
Search coverage limitations accompany claims of research completeness.
''')
add("D02","Claim analysis and contradictory evidence","SEMANTIC","subjects using research to justify decisions","Extract claims with source anchors; seek counterexamples and evaluate at least the serious alternatives supported by the decision context.", '''
Material claims are small enough to be independently supported or refuted.
The cited evidence supports the exact claim rather than a related topic.
Uncertainty in a source is preserved in the derived claim.
Contradictory sources remain visible in the synthesis.
Correlation is not silently promoted to a causal explanation.
A source's experiment population is not silently broadened.
A lack of evidence is not represented as evidence of absence.
Author speculation is distinguished from reported observations.
An alternative explanation accompanies high-impact causal claims.
The decision can be reconstructed without reading an entire transcript.
''')
add("D02","Research freshness and source drift","STRUCTURAL","subjects relying on time-sensitive external facts","Compare current retrieval metadata with frozen source versions; record changed claims and invalidate only affected decisions.", '''
Time-sensitive sources have claim-specific review triggers.
A changed source does not silently replace the historical source version.
Broken links have a retained identifier or an explicit provenance failure.
Framework-version changes identify affected local mappings.
Current status claims do not rely solely on an old publication date.
Source corrections propagate to dependent claims.
An unchanged URL is not treated as proof of unchanged content.
Research refresh records distinguish no change from failed retrieval.
Expired evidence cannot satisfy a current time-sensitive gate without justification.
Refresh effort is bounded by material impact rather than every source on every run.
''')
add("D02","Experiment design","SEMANTIC","subjects containing material untested assumptions","Construct an experiment with competing hypotheses, observable discriminators, controls, budget and an explicit interpretation table.", '''
The experiment states the uncertainty it is intended to resolve.
Competing hypotheses predict distinguishable observations.
The experimental unit is defined before data collection.
Success and failure conditions are specified before examining results.
Controls distinguish the proposed mechanism from a plausible confounder.
The environment is representative of the claim being tested.
Sample selection includes unsuccessful or incomplete attempts.
The experiment has a finite resource and stopping rule.
A negative result can change the planned next action.
The planned measurement is sensitive enough to detect the relevant difference.
''')
add("D02","Analysis and reproducibility","DYNAMIC","subjects reporting measurements or experimental results","Recompute reported quantities from retained observations; repeat a bounded run and test a deliberately perturbed input.", '''
Reported summary statistics can be recomputed from retained observations.
Units are consistent across inputs and outputs.
Missing observations are disclosed rather than replaced with successful ones.
Outlier exclusion follows a recorded rule.
Uncertainty is reported where sampling variability is material.
Censored or timed-out attempts are retained in analysis.
Repeated observations are not falsely treated as independent when they share state.
Comparisons use matched workload and environment conditions.
Analysis code identifies the input dataset revision.
A small deliberate data change produces the expected report change.
''')
add("D02","Research-to-action decisions","SEMANTIC","subjects making engineering or portfolio decisions from research","Trace each adopted idea to the actual problem, bounded experiment, consumer and rejected alternatives; permit justified no-op conclusions.", '''
The proposed adoption addresses a demonstrated or explicit hypothetical local problem.
Analogy limits are stated before transferring a mechanism across domains.
An implementation recommendation includes a smallest useful test.
Research findings identify the repository that actually owns the concern.
A dependency recommendation distinguishes feature donation from permanent adoption.
Research that does not apply can terminate with a no-op decision.
The expected benefit is compared with integration and maintenance cost.
A decision identifies which assumption would reverse it.
Research corpus size is not used as a substitute for decision quality.
The chosen action has an observable post-adoption review condition.
''')

add("D03","Capability inventory","STRUCTURAL","all subjects","Enumerate actual entrypoints, exports, jobs, assets and dependencies using parsers and observed behavior; label inference and collection limits.", '''
The inventory identifies actual externally reachable entrypoints.
Exported library interfaces are distinguished from internal helpers.
Scheduled and background capabilities are included in the subject inventory.
Experimental capabilities are labeled separately from supported capabilities.
Capability existence claims identify their observation method.
Undocumented implemented behavior is retained as a discovery.
Declared but absent capabilities remain visible as gaps.
Generated files are distinguishable from their authoritative inputs.
Submodule and vendored boundaries are not silently merged into owned scope.
The inventory declares inaccessible or uninspected subject areas.
''')
add("D03","Requirement quality","SEMANTIC","all assigned subjects","Review each requirement against its parent outcome, acceptance oracle and scope; use counterexamples to expose ambiguity or conjunction.", '''
Each accepted requirement has a stable identity and revision.
The requirement specifies an observable result.
Material ambiguous terms have operational definitions.
Conjunctive requirements are split or intentionally treated as one indivisible outcome.
The requirement identifies the beneficiary or consuming component.
Acceptance conditions do not depend only on a preferred implementation detail.
Requirement conflicts are exposed before release acceptance.
Requirements have explicit applicability to the selected slice.
The source of a requirement is distinguishable from its acceptance decision.
A removed requirement retains a recorded disposition and affected consumers.
''')
add("D03","Journeys and user-slice completeness","DYNAMIC","subjects with user, operator or programmatic consumer journeys","Execute the bounded journey from a realistic starting state through its final effect, including recovery and verification by a consumer.", '''
The selected journey begins from the intended user's actual starting state.
Required onboarding steps are included in journey scope.
Every mandatory transition is executable through a supported interface.
The final outcome is verified beyond an intermediate success message.
A interrupted journey has an explicit continuation or recovery path.
Required data survives the journey's supported restart boundary.
The journey identifies the exact beneficiary slice being evaluated.
Adjacent unsupported slices are not promoted by the tested slice.
The journey includes relevant permission-denied behavior.
Cross-repository dependencies are pinned consistently for the journey.
''')
add("D03","Applicability and scope selection","SEMANTIC","all assessments","Construct a capability-based applicability matrix; challenge both unjustified inclusion and convenient exclusions before freezing the epoch.", '''
All selected criteria have explicit applicability decisions or unresolved states.
Non-applicability has a subject-specific reason.
Product form alone does not exempt capability-created obligations.
A new capability triggers review of related risk obligations.
Missing evidence is not used as a reason to declare a criterion inapplicable.
Scope weights are frozen before results are aggregated.
An unreviewed exclusion cannot improve the verified score.
Criteria outside the bounded assessment remain visible as unassessed catalog coverage.
Mandatory parent obligations survive subdivision into smaller work packages.
The assessment distinguishes a partial survey from a complete selected-scope assessment.
''')
add("D03","Open-world gap discovery","SEMANTIC","all products under discovery or reassessment","Compare declared, implemented, exercised and beneficial views; examine failures, implied obligations and credible alternatives within a finite frontier.", '''
Promised-but-absent behavior is classified as an implementation gap.
Implemented-but-unverified behavior is classified as a verification gap.
Capability-implied obligations are considered even when undocumented.
Speculative enhancements are separated from accepted delivery debt.
Unexpected behavior is checked for security or integrity consequences.
Unused capabilities are evaluated for removal rather than automatic expansion.
Failure and recovery paths are examined during discovery.
Discovery records the frontier it did not inspect.
Feature parity with competitors is not treated as an automatic obligation.
Each material gap identifies the kind of action needed to resolve it.
''')
add("D03","Delivery decomposition and backlog quality","SEMANTIC","subjects with planned or active work","Trace work packages to accepted outcomes and dependencies; compare completion evidence with parent obligations and integration boundaries.", '''
Each work item resolves an identified obligation or experiment.
Work acceptance includes a demonstrable outcome rather than document production alone.
Dependencies distinguish true blockers from optional improvements.
A work item names the actual owning repository or component.
Split tasks preserve responsibility for inherited defects.
A task cannot close its parent outcome solely by closing its own narrow scope.
The backlog separates proposed opportunities from committed work.
Blocked work names the next action and wakeup condition.
The work package fits the remaining resource envelope.
The plan contains an end-to-end integration step for independently delivered components.
''')

add("D04","Boundaries and canonical ownership","SEMANTIC","multi-component or multi-repository subjects","Map responsibilities, state stores, consumer paths and changes; compare decomposition alternatives using actual coupling and ownership evidence.", '''
Each authoritative data object has one designated owner.
Generated projections identify their source of truth.
Tool implementation repositories do not own unrelated live portfolio state.
Cross-component dependencies have documented direction.
Duplicate implementations have a justified coexistence or consolidation decision.
A repository split has a consumer or operational benefit beyond naming.
Changes crossing boundaries identify integration responsibility.
A boundary can be removed without losing unique historical evidence.
Private deployment configuration is separated from generic tool source.
An ownership dispute cannot be hidden by publishing a second authoritative record.
''')
add("D04","Interfaces and contracts","DYNAMIC","subjects exposing component boundaries","Exercise actual producers and consumers against versioned contracts, including malformed, older and partial messages.", '''
Required interface fields have explicit meanings.
Producers emit data conforming to the selected contract version.
Consumers reject invalid mandatory fields predictably.
Unknown optional fields follow the declared compatibility rule.
Error responses are distinguishable from successful empty results.
Interface timeouts have documented observable behavior.
Idempotency guarantees are exercised where duplicate requests are possible.
Cancellation propagates across the intended interface boundary.
A compatible older consumer is exercised when backward compatibility is promised.
Contract drift between documentation and runtime behavior is detected.
''')
add("D04","Quality-attribute scenarios and ATAM-derived analysis","SEMANTIC","subjects with material architecture decisions","For each important quality attribute record stimulus, environment, affected artifact, response and response measure; compare alternatives and risk themes.", '''
Architecture scenarios connect to actual mission or consumer drivers.
Each scenario specifies a concrete stimulus.
The scenario names the environment in which the stimulus occurs.
The scenario identifies the affected architectural element.
Expected responses are stated separately from their measurement thresholds.
Architecture alternatives are evaluated against the same scenarios.
Sensitivity points identify assumptions whose changes materially alter outcomes.
Tradeoff points expose improvements that worsen another attribute.
Risk themes link multiple observations to a common architectural concern.
An automated adaptation is labeled ATAM-derived rather than claiming unperformed formal review.
''')
add("D04","Failure domains and resilience structure","DYNAMIC","subjects with interacting services, processes or devices","Inject isolated failures in disposable environments and observe propagation, containment, degradation and recovery across boundaries.", '''
A failed optional dependency does not disable unrelated mandatory capability.
A hung worker cannot indefinitely monopolize shared capacity.
Failure propagation matches the declared isolation boundary.
Fallback behavior is distinguishable from full-function operation.
Loss of network connectivity has a bounded local effect.
A poison message cannot permanently block unrelated queue work.
Recovery does not duplicate an already completed irreversible effect.
Resource exhaustion in one tenant or project is contained as promised.
Failure diagnostics identify the causal boundary rather than only a downstream symptom.
The system can rejoin a recovered component without corrupting shared state.
''')
add("D04","Modifiability and evolutionary design","SEMANTIC","subjects expected to evolve","Walk concrete change scenarios through code, contracts, tests and consumers; measure the minimal affected surface and compare simpler designs.", '''
A representative feature change has a traceable impact set.
A replaceable backend is not coupled through undocumented implementation details.
Configuration changes avoid unnecessary rebuilds where runtime change is promised.
Interface versioning permits the intended migration cadence.
A domain rule has a designated implementation location.
Architectural abstractions have actual consumers or a bounded validation plan.
Circular dependencies have an explicit removal or containment strategy.
Migration paths preserve required historical data and behavior.
The design documents where a simpler solution was rejected and why.
Architecture decisions have review triggers tied to changed assumptions.
''')
add("D04","Polyrepo composition and integration baselines","DYNAMIC","products composed from multiple repositories","Assemble the selected product from a pinned bill of materials; execute its cross-repository journey and deliberately mismatch one contract.", '''
The integrated product identifies all required component revisions.
Build artifacts map back to the selected source revisions.
The release baseline excludes unintended unmerged local changes.
A cross-repository contract mismatch is detected before promotion.
Component-level passes do not substitute for an integrated journey pass.
Shared schema changes identify every affected consumer.
Integration tests exercise the actual selected transport and storage paths.
A partially unavailable component has an honest blocked or degraded state.
Version skew behavior is tested for supported rollout orders.
An integration failure has a designated owner and reproducible baseline.
''')

add("D05","Core correctness and domain invariants","DYNAMIC","implemented code","Execute representative, boundary and invalid inputs against domain predicates justified independently of the implementation.", '''
The core operation produces the required result for a representative valid input.
Empty input follows the declared domain behavior.
Boundary values do not violate the selected invariant.
Invalid input cannot silently produce a valid-looking corrupt result.
Numeric overflow or precision loss is handled within the domain contract.
Ordering-sensitive operations preserve the required order.
Repeated operations respect the declared idempotency semantics.
Concurrent operations preserve the required state invariant.
Error handling does not silently discard mandatory work.
Unsupported inputs receive a distinguishable unsupported outcome.
''')
add("D05","Error semantics and defensive behavior","DYNAMIC","implemented code","Trigger expected failure classes at public boundaries; inspect emitted errors, preserved state and the caller's recovery options.", '''
Expected validation failures use stable distinguishable error categories.
Unexpected exceptions do not leak secret internal data.
Error paths preserve the last accepted durable state.
Partial success is distinguishable from complete success.
Retriable failures are distinguishable from permanent failures.
A failed cleanup does not hide the original failure.
Cancellation is not misreported as successful completion.
Timeout errors identify the operation that exceeded its budget.
Fallback behavior does not mask an unmet mandatory obligation.
The caller can determine the next supported action from the error contract.
''')
add("D05","Static quality and maintainability","STRUCTURAL","source-bearing subjects","Run the actual configured parser, type checks and linters; inspect relevant findings and sampled code structures rather than configuration presence.", '''
Source files parse under the declared language version.
Selected type checks execute on the intended production paths.
Lint suppressions identify a specific justified exception.
Unreachable or dead code is tracked when it obscures supported behavior.
Public interfaces avoid unintentionally exposing internal types.
Repeated domain logic has an explicit consolidation decision.
Generated code is not manually edited without changing its generator.
Complexity hotspots link to behavior or maintainability risks.
Formatting checks are reproducible in a clean environment.
Deprecated code paths identify their supported removal conditions.
''')
add("D05","Dependency and toolchain hygiene","STRUCTURAL","subjects with dependencies or build tools","Resolve dependency metadata and selected toolchain state; compare lockfiles, actual installed versions and supported upgrade boundaries.", '''
The build identifies the toolchain version actually used.
Resolved dependencies match the retained lock or equivalent resolution record.
Direct and transitive dependencies are distinguishable.
Unused dependencies have a removal or retention decision.
A local path dependency does not silently replace a declared release dependency.
Dependency upgrades identify potentially affected consumers and tests.
Unsupported toolchain versions fail with a useful diagnostic.
Vendored modifications retain upstream identity and local delta.
Dependency overrides have an owner and expiration or review condition.
Offline or restricted-network builds report unresolved dependencies honestly.
''')
add("D05","Configuration semantics","DYNAMIC","configurable products","Exercise precedence, validation, reload and failure behavior using synthetic secrets and isolated environments.", '''
Configuration precedence matches the documented order.
Invalid configuration is rejected before unsafe side effects.
Missing required configuration is distinguishable from an optional disabled feature.
Effective nonsecret configuration can be inspected by an authorized operator.
Secret values are redacted from configuration diagnostics.
Runtime changes take effect without restart when that behavior is promised.
A failed configuration reload preserves a known valid state.
Environment-specific defaults do not accidentally enable production effects.
Configuration migrations preserve intended prior settings.
The configuration fingerprint excludes raw secrets while identifying material changes.
''')
add("D05","Concurrency and resource lifetime","DYNAMIC","subjects using parallelism or long-lived resources","Stress bounded concurrent operations with cancellation and injected failure; observe race safety, cleanup and stable resource counts.", '''
Shared mutable state is protected under supported concurrency.
Cancellation releases resources owned by the canceled operation.
Retries cannot create unbounded background workers.
Resource handles are closed after both success and failure.
A task cannot use another task's temporary working directory.
Lock acquisition has bounded behavior under contention.
A crashed owner cannot indefinitely retain a recoverable lease.
Backpressure prevents unbounded queue growth.
Shutdown waits for or safely terminates in-flight mandatory work.
Concurrent cleanup cannot delete another active worker's state.
''')

add("D06","Test inventory and behavioral coverage","STRUCTURAL","subjects with executable behavior","Map tests to obligations and actual selected execution; distinguish source coverage, assertion coverage and consumer behavior.", '''
The test inventory identifies which accepted obligations each suite exercises.
Required test selection includes the intended packages and platforms.
Source coverage is reported separately from behavioral coverage.
Tests contain assertions about meaningful outcomes.
Skipped tests are visible in the assessment denominator.
A zero-test run cannot satisfy a required test obligation.
Uncovered mandatory behavior remains a blocker despite aggregate coverage.
Test-only helper behavior is not counted as product behavior coverage.
Coverage reports identify the exact subject and instrument revision.
Independent coverage floors are not combined to hide a failing family.
''')
add("D06","Oracle and grader qualification","DYNAMIC","all evaluation instruments","Run a valid witness and targeted invalid witnesses through the exact evaluator; preserve false-positive and false-negative observations.", '''
The grader accepts a valid solution that differs from its reference implementation.
The grader rejects an empty or no-op implementation for nonempty behavior.
A forced-success exit status cannot override failed outcome assertions.
A corrupted expected artifact is detected.
The grader distinguishes a product failure from a runner failure.
A wrong subject revision is rejected as mismatched evidence.
The oracle's expected result has a justification outside the candidate output alone.
Grader inputs cannot be silently rewritten by the implementation worker.
Known grader limitations constrain the claims it may support.
A grader update has its own version and qualification record.
''')
add("D06","Integration and end-to-end assurance","DYNAMIC","products with integrations or end-to-end workflows","Execute real supported boundary paths in a disposable composition and inspect durable effects using an independent observer.", '''
The integration suite exercises the actual protocol boundary.
Mock-only tests are labeled separately from real integration tests.
External side effects are verified rather than inferred from a success message.
The suite exercises permission-denied responses from a real boundary.
A broken dependency connection causes the relevant integration test to fail.
Required database behavior is exercised on each supported backend.
Clean installation precedes the intended end-to-end smoke test.
The end-to-end test starts without privileged developer leftovers.
Failure recovery is included in the required journey suite.
Evidence identifies synthetic fixtures separately from production observations.
''')
add("D06","Property, mutation and fuzz assurance","DYNAMIC","subjects whose risk justifies generative or adversarial testing","Generate inputs under justified invariants, retain seeds and shrinking results, and measure whether meaningful code mutations are detected.", '''
Property tests state independently justified invariants.
Generated input ranges include relevant boundaries.
Failing generated cases retain reproducible seeds or minimized inputs.
Mutation results distinguish killed, surviving and unexercised mutants.
Equivalent or invalid mutants have reviewed exclusion reasons.
Fuzz campaigns use an explicit resource and termination budget.
Crashes are triaged separately from intended validation failures.
A discovered counterexample becomes a retained regression case.
Metamorphic relations are justified for the actual domain.
Differential comparisons identify the reference and its known limitations.
''')
add("D06","Test isolation and repeatability","DYNAMIC","subjects with repeatable tests","Repeat and reorder tests in clean environments; deliberately contaminate one trial to verify isolation and reset behavior.", '''
Tests do not depend on undocumented execution order.
A fresh trial resets state required for independence.
Clock-sensitive tests use a controlled or explicitly observed clock.
Randomness affecting results is recorded.
A failed test cannot contaminate an unrelated subsequent test.
Temporary resources are uniquely scoped per trial.
Parallel test execution preserves declared invariants.
Flaky outcomes remain visible rather than rerun until hidden.
A repeated test uses the same artifact and relevant environment inputs.
Fixture setup failure cannot be reported as a passing product test.
''')
add("D06","Regression and assurance change control","DYNAMIC","subjects with accepted baselines","Compare prior and candidate behavior under a frozen baseline; exercise a seeded regression and inspect baseline-update permissions.", '''
A new capability does not silently remove prior mandatory coverage.
Accepted behavior has retained regression cases.
A seeded regression fails the intended gate.
Test expectation changes are reviewed as evaluator changes when they alter meaning.
A baseline update preserves the previous baseline identity.
Regression waivers have scope, owner and expiry.
Reopened defects are visible in progress reporting.
Required failures cannot be hidden by changing suite aggregation.
Release acceptance uses the actual integrated artifact rather than only a premerge candidate.
A measurement defect can be corrected without mislabeling it as product improvement.
''')

add("D07","Clean checkout and setup","DYNAMIC","source-bearing products","Start from a clean authorized checkout on the supported platform; execute the documented setup without developer caches or undeclared credentials.", '''
A clean checkout identifies the minimum required tools.
Setup does not depend on an undocumented local path.
Required dependency installation completes under the declared environment.
Setup detects an unsupported platform before destructive changes.
Missing credentials produce a scoped actionable blocker.
Development setup avoids modifying unrelated user configuration.
A repeat setup is idempotent or clearly reports existing state.
The first useful verification command is discoverable from the entry documentation.
Uninstalling setup-owned resources leaves unrelated resources intact.
The setup duration is measured under a declared cache condition.
''')
add("D07","Inner-loop feedback","DYNAMIC","actively developed code","Measure edit-to-feedback for representative changes and deliberately introduce known syntax, type and behavior failures.", '''
A small source edit can trigger a relevant verification path.
Known syntax errors are reported at the responsible source location.
Type errors are distinguishable from dependency-resolution failures.
A targeted test can be run without executing unrelated expensive suites.
Incremental builds actually reuse eligible prior work.
Watch-mode changes are not missed under the supported filesystem.
A failed background check cannot be mistaken for the previous successful run.
Feedback includes the command and environment needed to reproduce it.
The inner loop has measured wall-clock latency for a representative change.
Shared-machine contention is included when it is part of the development contract.
''')
add("D07","Debugging and diagnostics","DYNAMIC","products that developers or operators debug","Reproduce representative faults and follow supported diagnostics from symptom to cause using permitted evidence.", '''
A failure can be reproduced from its diagnostic record.
Errors include a stable correlation identifier when operations span components.
Debug builds preserve useful source mapping or stack information.
Diagnostic verbosity can be changed without exposing raw secrets.
A crash report identifies the artifact revision.
A developer can inspect effective nonsecret runtime configuration.
A failed dependency call identifies its relevant boundary and status.
Logging volume remains bounded during repeated failures.
Diagnostic commands are usable without granting unnecessary production authority.
The debugging guide includes a tested path for a common failure.
''')
add("D07","Documentation and examples","DYNAMIC","products with developer-facing documentation","Execute documented commands and examples from a clean consumer context; distinguish explanation quality from observable execution.", '''
The primary quickstart reaches a real useful outcome.
Documented command flags match the installed interface.
Code examples compile or execute under the stated version.
Examples identify required environment assumptions.
Broken internal documentation links are detected.
Documentation distinguishes supported features from planned features.
An example handles at least one relevant failure path.
Generated API documentation maps to the actual exposed interface.
Private or credential-bearing examples are excluded from public publication.
A changed interface triggers review of affected examples.
''')
add("D07","Contribution and review workflow","DYNAMIC","subjects accepting changes from multiple sessions or contributors","Follow a bounded contribution through claim, isolated change, review, integration and rollback; inject a conflict to test coordination.", '''
A contributor can identify the accepted target branch and baseline.
Local work is isolated from another contributor's dirty tree.
Change scope identifies the requirement or finding it addresses.
Required checks are discoverable before submission.
A conflicting concurrent change is detected rather than overwritten.
Review feedback links to a concrete claim or failure.
The integration path identifies who may accept the change.
A rejected change preserves useful evidence or hypotheses.
The accepted commit is distinguishable from a review-ready candidate.
Rollback instructions identify the actual integrated change.
''')
add("D07","Library and SDK consumer experience","DYNAMIC","libraries, SDKs and reusable packages","Build a separate consumer project against the distributed package; test discoverability, compatibility and error handling without source-tree shortcuts.", '''
A separate consumer can install the released package.
The documented import or initialization path works outside the repository.
Public types expose enough information for correct use.
A common operation needs no undocumented internal access.
API errors provide a caller-recoverable contract.
The supported version matrix includes the actual consumer runtime.
A minimal consumer example exercises a real library capability.
Breaking changes are distinguishable from compatible additions.
Optional dependencies are not forced onto consumers that do not use them.
Package contents exclude development-only secrets and unrelated artifacts.
''')

add("D08","Machine-facing discovery and interfaces","DYNAMIC","products consumed by agents","Use an unprimed authorized agent or scripted consumer to discover operations and parse outcomes; perturb arguments and schemas.", '''
Available operations are discoverable through a documented machine-facing surface.
Machine-readable success outputs conform to a stable schema.
Machine-readable failures distinguish actionable error categories.
Human decoration does not corrupt structured output streams.
Help output describes required arguments and side effects.
Capability discovery identifies unsupported operations honestly.
Interface versions can be determined before invoking risky operations.
Large outputs support bounded retrieval or pagination.
A successful empty result is distinguishable from a failed query.
Tool descriptions do not claim capabilities absent from the installed implementation.
''')
add("D08","Headless execution and sandboxing","DYNAMIC","agent-operated workflows","Run the actual workflow outside the foreground desktop under constrained native sandbox or VM permissions and synthetic fixtures.", '''
The required workflow can run without interactive prompts when headless mode is promised.
Credential input does not require unsafe plaintext command arguments.
The worker cannot write outside its authorized workspace.
Network access follows the declared egress policy.
A sandbox escape attempt is blocked by an actual boundary rather than prompt text alone.
Temporary environments start from a known reset state.
Teardown removes resources owned by the completed session.
The capture environment does not interfere with the user's foreground input.
A missing virtualization or capture capability is reported as an environment blocker.
The workflow supports the permitted native no-Docker path when required by the fleet.
''')
add("D08","Claims, leases and parallel work","DYNAMIC","work shared across multiple agents","Simulate concurrent claims, expiration, crash and takeover with unique worker identities; verify ownership and fencing at side-effect boundaries.", '''
Two workers cannot both acquire the same exclusive work claim.
Lease expiry is observable by the current owner and scheduler.
A stale worker is fenced from committing protected side effects.
Heartbeat failure has a bounded recovery policy.
A reclaimed task retains the previous attempt's evidence.
Shared resource capacity cannot be oversubscribed beyond the accepted policy.
Workers can cancel a queued claim without leaking its reservation.
A worker crash does not permanently orphan recoverable work.
Conflict resolution preserves both candidate changes until adjudication.
Claim renewal cannot silently reset the cumulative task budget.
''')
add("D08","Restart, replay and durable memory","DYNAMIC","long-running or replaceable agent sessions","Terminate a worker at a controlled point and resume in a fresh session using only durable records and actual permissions.", '''
A fresh session can locate the accepted assignment epoch.
The restart packet identifies the actual current subject revision.
Previously rejected hypotheses retain reproducible evidence.
The packet distinguishes accepted baseline from unmerged candidates.
A restarted worker does not repeat a known rejected approach without changed conditions.
Replay preserves the relevant original inputs and environment identity.
Restarting cannot enlarge the worker's permissions.
Restarting cannot reset the remaining cumulative resource budget.
A compact summary links to evidence rather than replacing it.
Dirty or incomplete work is explicitly handed off rather than silently assumed committed.
''')
add("D08","Harness and tool qualification","DYNAMIC","agent harnesses and installed tools","Invoke the actual installed tool against valid, invalid, denied and timed-out cases; inspect raw effects and normalize only supported semantics.", '''
Tool invocation records the actual installed version or source revision.
Declared tool arguments match the callable interface.
A tool failure is not normalized into an empty successful result.
Timeout and cancellation propagate to owned child work.
A credential denial remains distinguishable from product malfunction.
A tool producing forged success text cannot satisfy an independent outcome check.
Output truncation is visible to the consuming agent.
A changed tool schema invalidates incompatible cached assumptions.
The harness preserves tool-call and artifact causality.
A named tool in documentation is not reported as adopted without a working receipt.
''')
add("D08","Agent behavior and evaluation reliability","DYNAMIC","stochastic agents or autonomous systems","Run a frozen task set with independent reset, retained trials and outcome-based grading; report trial reliability separately from best-of-attempt success.", '''
The evaluated subject includes the model, harness, tools and configuration.
Trials preserve both successful and failed outcomes.
Success within several attempts is reported separately from repeated-request reliability.
The agent observes declared resource limits during task execution.
The agent can abstain when required evidence is unavailable.
A task's outcome is checked beyond the agent's narrative claim.
A repeated failure triggers diagnosis rather than unbounded identical retries.
Prompt injection in retrieved content cannot expand actual tool authority.
Model or prompt changes identify which baseline they invalidate.
Agent performance comparisons include total verification and rework cost.
''')

add("D09","Onboarding and first value","DYNAMIC","human-facing products","Use a clean intended-user account and representative starting state; follow the first-value path without developer-only shortcuts.", '''
A new intended user can identify the primary purpose.
The first required action is distinguishable from optional exploration.
Onboarding requests only information needed at that stage.
The user can reach a real first-value outcome.
Prerequisite failures are explained before the user reaches a dead end.
Progress through multi-step onboarding is preserved as promised.
The user can recover from an invalid onboarding input.
Demo data is distinguishable from the user's actual data.
An onboarding dismissal does not make required setup undiscoverable.
The first-value journey has a measured completion result for the selected slice.
''')
add("D09","Navigation and information architecture","SEMANTIC","human interfaces with multiple destinations","Inspect task-oriented navigation using representative goals and rendered states; validate navigation effects through actual interaction.", '''
Primary navigation labels predict their destinations.
Related tasks are grouped by user purpose rather than internal implementation names.
The current location is discernible within the product.
Back navigation preserves expected context.
Deep links resolve to the intended authorized state.
A nonexistent destination produces a recoverable state.
Search or filtering exists where the accepted information volume requires it.
Navigation does not expose unauthorized resources.
Repeated destinations use consistent terminology.
The user can return from a secondary workflow to the main task.
''')
add("D09","Task execution and interaction correctness","DYNAMIC","interactive products","Execute representative tasks through supported controls and verify state changes independently of visual confirmation.", '''
Primary controls perform their labeled action.
Disabled controls cannot still trigger the forbidden operation.
Submitting a form twice does not duplicate protected effects.
Required validation occurs before invalid data is committed.
A successful interaction updates the actual underlying state.
Keyboard submission behaves consistently with pointer submission.
Selection state persists through the supported task transitions.
The user can cancel a reversible task before commitment.
Destructive actions communicate the affected scope.
The interaction remains correct under a slow response.
''')
add("D09","Loading, empty and failure states","DYNAMIC","interfaces with asynchronous or data-dependent behavior","Exercise empty, loading, partial, offline, permission-denied and failed states with controlled backend responses.", '''
Loading state is distinguishable from empty state.
An empty result explains the next useful user action.
Partial data is not presented as complete data.
An offline state does not masquerade as a successful refresh.
A failed operation provides a recoverable next step where one exists.
A retry does not duplicate an already completed effect.
Stale displayed data is identified when freshness matters.
A denied operation does not reveal inaccessible resource details.
Long-running operations expose meaningful progress or a bounded waiting state.
Error messages do not erase recoverable user input.
''')
add("D09","Control, recovery and trust","DYNAMIC","products that change user state or perform consequential actions","Exercise undo, cancellation, confirmation, session expiry and permission changes; inspect what the user can understand and recover.", '''
The user can determine whether an operation actually completed.
Undo restores the promised prior state for supported reversible actions.
A canceled operation stops its future side effects within the declared boundary.
Session expiry preserves recoverable work as promised.
Permission changes take effect in the visible interaction state.
Confirmation text identifies the real consequence rather than a generic warning.
A background operation remains discoverable after leaving its initiating screen.
The interface identifies simulations and conceptual demonstrations.
The user can inspect or export a receipt for consequential completed work where required.
A failed recovery does not claim the original state has been restored.
''')
add("D09","UX content and usability evidence","SEMANTIC","human-facing text and workflows","Review language against actual user tasks and evaluate task outcomes using appropriately labeled user or simulation evidence.", '''
Terminology is consistent across labels, help and errors.
Instructions describe user actions rather than unexplained internal concepts.
Error text identifies what the user can change.
Critical information is not hidden behind decorative content.
Confirmation messages reflect actual completed effects.
Copy distinguishes tentative recommendations from facts.
Usability observations identify who or what performed the task.
Synthetic users are not represented as independent human-user evidence.
Reported task success has an observable completion definition.
A usability finding links to a specific affected journey and improvement hypothesis.
''')

add("D10","Keyboard and focus access","DYNAMIC","keyboard-operable human interfaces","Traverse the actual interface without a pointer using the selected accessibility target; inspect focus, activation and escape behavior.", '''
All required interactive controls are reachable by keyboard.
Keyboard focus remains visibly identifiable.
Focus order follows the intended task sequence.
Opening a modal places focus in the intended context.
Closing a modal returns focus to a meaningful location.
The user can escape a nonessential keyboard trap.
Keyboard shortcuts do not unexpectedly override essential input behavior.
Offscreen or hidden controls do not capture focus inappropriately.
Re-rendering does not lose focus during a required task.
A skip mechanism bypasses repeated navigation where the selected target requires it.
''')
add("D10","Semantic and assistive-technology access","DYNAMIC","human interfaces exposing an accessibility tree","Inspect the actual accessibility tree and exercise representative assistive-technology journeys against the declared conformance scope.", '''
Interactive controls expose an accessible name.
Control roles match their actual behavior.
Current state changes are represented in the accessibility surface.
Form errors are associated with the relevant input.
Content headings describe the document structure.
Meaningful images have an appropriate text alternative.
Dynamic status updates are announced without unnecessary interruption.
Decorative content does not create misleading semantic noise.
Custom controls expose the interaction semantics required for their use.
An assistive-technology user can complete the selected core journey.
''')
add("D10","Visual access and adaptable presentation","DYNAMIC","visual human interfaces","Test selected text scaling, zoom, contrast, reflow and user-preference conditions on real rendered states.", '''
Required text remains readable at the selected scaling target.
Content reflows without losing essential actions at the selected narrow viewport.
Text contrast meets the explicitly selected target for the tested state.
Nontext control boundaries remain distinguishable under the selected target.
Information is not conveyed by color alone.
Focus indicators remain visible against actual backgrounds.
High-contrast or forced-color mode preserves required meaning where supported.
Text enlargement does not hide error messages or confirmation controls.
Reduced-motion preferences are respected by nonessential motion.
Flashing or rapidly changing content is evaluated against the selected accessibility requirement.
''')
add("D10","Audio, timing and alternate input","DYNAMIC","products with audio, video, timed or gesture-based interactions","Exercise the selected media and input alternatives; verify actual information equivalence and timing controls rather than asset presence.", '''
Required prerecorded speech has an accurate accessible alternative.
Essential visual media information has an appropriate nonvisual alternative.
Playback controls are operable through the required input methods.
Audio does not start in a way that prevents user control under the chosen target.
Time-limited tasks provide the required extension or exception handling.
A complex gesture has an accessible alternative where required.
Pointer target sizes meet the selected task and accessibility target.
Orientation changes preserve required function where orientation is not essential.
Speech-only input has an alternative when the selected user slice requires it.
Captions and transcripts correspond to the actual media revision.
''')
add("D10","Localization and internationalization","DYNAMIC","products supporting multiple locales or claiming locale robustness","Run representative locale, script, timezone and formatting cases against real data exchange and rendered interfaces.", '''
User-visible strings are not unintentionally hard-coded outside the localization path.
Long translations do not obscure required controls.
Right-to-left layouts preserve logical navigation when supported.
Dates are interpreted using the declared locale and timezone semantics.
Numeric formatting does not corrupt stored numeric values.
Pluralized messages reflect the supported language's rules.
Unicode input survives supported storage and round-trip operations.
Sorting follows the declared locale or explicit invariant order.
Fallback locale behavior is visible and predictable.
Localized errors preserve the machine-readable error category.
''')
add("D10","Accessibility assurance and scope honesty","SEMANTIC","subjects making accessibility claims","Review conformance scope, instruments and actual journey evidence; identify automated coverage limits and required unavailable evaluations.", '''
The accessibility target identifies the applicable standard or explicit product requirement.
Automated findings are not represented as complete conformance evidence.
The tested pages or surfaces are explicitly listed.
Dynamic and error states are included in the declared evaluation scope.
Known accessibility defects have affected journeys and severity.
A waiver does not convert an accessibility failure into a pass.
Required expert or user evaluation gaps remain visible.
Accessibility evidence identifies the tested artifact and assistive environment.
A component pass is not generalized to an untested composed screen.
The public accessibility claim matches the strength and scope of retained evidence.
''')

add("D11","Design system and visual coherence","SEMANTIC","products with a visual presentation","Inspect rendered examples across the selected product states; compare actual component usage to an accepted visual system and intentional exceptions.", '''
Repeated components use consistent visual semantics.
Color roles distinguish emphasis, state and decoration.
Typography establishes a discernible information hierarchy.
Spacing relationships remain coherent across related screens.
Corner, border and elevation treatments follow an intentional pattern.
Icon meanings remain consistent across contexts.
An intentional visual exception has a user-facing purpose.
Dark and light presentations preserve the same semantic priorities when both are supported.
Brand assets match the actual product identity.
A design-token file alone is not accepted as evidence of rendered consistency.
''')
add("D11","Layout and responsive craft","DYNAMIC","visual interfaces across declared viewport or display sizes","Capture actual rendered states at the selected sizes and content extremes; assert geometry and inspect task-preserving behavior.", '''
Primary content has no unintended horizontal overflow at supported widths.
Controls do not overlap under realistic long content.
Important actions remain visible without accidental clipping.
Layout changes preserve task hierarchy across supported sizes.
Empty content does not collapse the page into a broken geometry.
Dense content has an intentional spacing and grouping strategy.
Display scaling does not blur or misalign critical interface elements beyond the accepted target.
Text truncation provides access to essential hidden meaning.
Split panes and resizable regions respect declared minimum usable sizes.
Responsive behavior is verified in the actual runtime rather than a static design mock.
''')
add("D11","Interaction feedback and motion","DYNAMIC","interfaces with interactive feedback or animation","Trigger interactions under normal and delayed execution; inspect feedback timing, interruptions and reduced-motion behavior.", '''
An activated control provides timely perceptible feedback.
Pressed and selected states reflect actual interaction state.
Animations do not conceal required information during a task.
A canceled transition does not leave the interface in an invalid state.
Motion duration and easing follow the accepted interaction language.
Repeated clicks during an animation do not queue unintended actions.
Reduced-motion mode preserves task understanding without nonessential animation.
Loading transitions do not cause avoidable disruptive layout shifts.
Audio or haptic feedback is proportionate and user-controllable where present.
A visual success transition occurs only after its required effect is established.
''')
add("D11","Content density and visual hierarchy","SEMANTIC","information-rich human interfaces","Review real representative data with task goals; distinguish deliberate density from hidden actions, weak hierarchy or decorative noise.", '''
The most important task information is visually distinguishable.
Metadata is subordinate to the decision or action it supports.
Dense views preserve readable grouping and alignment.
Empty decorative space does not force unnecessary navigation.
Long-form content remains scannable through meaningful structure.
Tables distinguish headers, units and exceptional values.
Status colors have labels or other redundant meaning.
Competing calls to action have an explicit priority.
Progressive disclosure does not hide mandatory information.
Visual hierarchy remains coherent with realistic rather than idealized content.
''')
add("D11","Media, screenshots and product proof","STRUCTURAL","subjects producing demonstrations or public assets","Trace media to its capture or authorship source; compare claims with raw masters and verify allowed redactions and rights.", '''
Product screenshots originate from the actual rendered subject when presented as proof.
Conceptual visuals are explicitly labeled as conceptual.
Evidence masters are preserved separately from annotated demonstrations.
Timing in a performance demonstration is not silently sped up.
Sensitive information is redacted without falsifying the demonstrated outcome.
Media records identify the product revision and capture environment.
CLI products use authentic terminal or consumer evidence rather than fabricated application screens.
Library demonstrations exercise a real consuming program.
Asset rights and attribution requirements are recorded before publication.
Marketing media does not depict unimplemented functionality as shipping.
''')
add("D11","Polish review and craft acceptance","SEMANTIC","products with subjective presentation quality","Use anchored review cases and actual task evidence; record concrete defects, disagreement and the effect of proposed changes.", '''
A polish verdict names specific observable strengths or defects.
Reviewers distinguish personal preference from a violated accepted design constraint.
Comparisons use the same content and task state.
A rating has behaviorally described anchors.
Reviewer disagreement remains visible until adjudicated or accepted as uncertain.
The review includes loading, empty and error presentation.
Cosmetic improvement does not excuse a broken interaction.
A polished screenshot cannot compensate for an unusable actual journey.
A proposed visual change identifies the user problem it addresses.
The final presentation is checked at the actual delivery artifact.
''')

add("D12","Workload definition and measurement integrity","STRUCTURAL","subjects making performance or resource claims","Inspect workload, hardware, toolchain, clock and sampling definitions; replay the measurement from retained raw observations.", '''
The workload represents the claimed user or agent scenario.
Input size and distribution are specified.
Concurrency means active work rather than merely open sessions.
Warm-cache and cold-cache conditions are distinguished.
Hardware and relevant power or scheduling settings are recorded.
Measurement units and clock sources are explicit.
Percentiles are computed from a retained observation set.
Timed-out or failed operations remain in the reported workload outcome.
The benchmark identifies the exact artifact and configuration.
A result from one environment is not silently promoted to another environment's guarantee.
''')
add("D12","Latency and responsiveness","DYNAMIC","latency-sensitive products","Measure end-to-end and stage latency under the selected workload, including cold start and accepted contention conditions.", '''
End-to-end latency includes all user-visible required stages.
Tail latency is reported when it matters to the accepted task.
Cold-start latency is measured separately from steady state.
Queue waiting time is included or explicitly separated.
Cancellation latency meets the declared response budget.
Input-to-feedback latency is measured for real interactive paths.
A latency optimization preserves required correctness.
Timeout behavior respects the total request deadline.
Slow dependency behavior is included in the latency scenario.
The measured target uses the selected platform and display or transport path.
''')
add("D12","Throughput, capacity and backpressure","DYNAMIC","systems serving concurrent work","Sweep bounded load through the operating range; observe completed useful work, queue growth, fairness and saturation behavior.", '''
Throughput counts completed valid operations rather than attempted requests.
Capacity is measured at the accepted latency and error bounds.
Queue growth remains bounded under sustained overload.
Backpressure is observable to the submitting client.
Admission control prevents work beyond the configured capacity envelope.
Concurrent projects receive the declared fairness behavior.
Increasing concurrency does not silently drop required work.
Saturation produces a diagnosable degraded state.
Recovery from overload does not require losing accepted durable tasks.
Burst-load claims identify burst length and recovery conditions.
''')
add("D12","Memory, storage and resource efficiency","DYNAMIC","products with material resource use","Measure steady, peak and repeated-use resource behavior; inject allocation or storage pressure and observe bounded degradation.", '''
Peak memory is measured for the selected workload.
Repeated operations do not cause unbounded retained memory.
Temporary storage growth is bounded by the declared policy.
Disk-full behavior preserves required data integrity.
File descriptor or handle usage remains within the accepted operating envelope.
GPU memory use includes the relevant caches and concurrent workloads.
Network transfer volume is measured for the actual protocol path.
Cleanup returns owned resources after a completed trial.
Resource-saving modes preserve explicitly required behavior.
Published efficiency claims include the measurement scope and excluded overhead.
''')
add("D12","Mixed-load and multi-device performance","DYNAMIC","products intended for shared hosts, VMs or remote devices","Run representative competing CPU, GPU, storage, network and real-time workloads under authorized native or VM isolation.", '''
Foreground interactive work is included when shared-host operation is promised.
Audio-sensitive workloads are evaluated for relevant interruption or deadline failures.
GPU contention is measured under the selected graphics or inference coexistence scenario.
Storage-heavy background work is included in relevant responsiveness tests.
Remote network variation is distinguished from local processing latency.
Cross-device clock uncertainty is accounted for in timing claims.
VM or sandbox overhead is measured in the actual intended configuration.
Dynamic resource allocation does not violate the foreground reservation policy.
Quality degradation is measured alongside latency improvements.
The test records the actual concurrently active workloads rather than a nominal fleet size.
''')
add("D12","Performance regression and economic efficiency","DYNAMIC","products with performance baselines or cost targets","Compare matched baseline and candidate runs; include setup, verification, retries and useful outcomes in efficiency analysis.", '''
Performance comparisons use matched workload definitions.
A faster result is rejected when it fails the required correctness gate.
Resource-cost reports include failed attempts and retries.
Cache-related savings identify hit rate and cache population assumptions.
An optimization's effect exceeds or acknowledges measurement variability.
Regression thresholds have an accepted product rationale.
A baseline update preserves the old measurement and environment identity.
Cost per outcome uses accepted outcomes rather than rubric points.
Parallel execution reports both wall-clock savings and total resource use.
Performance claims are refreshed when a material environment or dependency changes.
''')

add("D13","Runtime observability","DYNAMIC","running products and services","Trigger known operations and failures; follow metrics, logs and traces to actual effects with bounded and redacted telemetry.", '''
Required operations emit an observable completion or failure signal.
Telemetry identifies the relevant subject artifact and environment.
A cross-component operation has usable correlation identifiers.
Metrics distinguish availability from merely running processes.
Structured logs preserve machine-readable error categories.
Sensitive payloads are excluded or redacted according to policy.
Telemetry failure does not corrupt the product's core operation.
High-cardinality data is controlled under the operating budget.
The operator can distinguish stale telemetry from healthy inactivity.
A known injected failure is visible through the selected observability path.
''')
add("D13","Health, readiness and graceful degradation","DYNAMIC","deployable or continuously operated products","Exercise startup, dependency loss, recovery and shutdown; compare reported health with actual ability to fulfill required work.", '''
Liveness checks identify a stuck process when that is their claimed role.
Readiness reflects actual ability to accept required work.
Optional disabled features are distinguishable from failed required features.
A degraded dependency is reported with the affected capability.
Startup ordering does not expose a falsely ready endpoint.
Readiness returns after recovery only when required behavior works.
Graceful shutdown stops accepting new work at the correct point.
In-flight work is completed or durably handed off during shutdown.
Health checks do not themselves create destructive side effects.
A green dashboard cannot override a failed core-journey probe.
''')
add("D13","Recovery, backups and restoration","DYNAMIC","stateful or operationally persistent products","Create representative data, produce a backup, inject an authorized failure and restore through the supported path; compare integrity and elapsed recovery.", '''
A backup contains the required recoverable data scope.
Backup completion is verified beyond command exit status.
A corrupt backup is detected before claiming successful recovery.
A clean environment can restore the retained backup.
Restored records preserve the required integrity predicates.
Recovery time is measured against the accepted scenario budget.
The declared recovery point matches the actually recoverable data age.
Backup credentials and encryption material have a viable authorized recovery path.
Restoration does not silently overwrite unrelated current data.
The recovery exercise identifies its actual source and target versions.
''')
add("D13","Incident response and operational learning","DYNAMIC","operated products with consequential failures","Run a bounded incident drill from detection through containment, recovery and follow-up; verify role routing and evidence retention.", '''
A relevant alert reaches an authorized responder path.
The alert identifies the affected user outcome or capability.
The responder can locate a tested mitigation procedure.
Containment actions remain inside actual operational authority.
The incident record preserves an ordered causal timeline.
Recovery is confirmed through product behavior rather than alert disappearance alone.
A recurring incident creates an owned prevention or research action.
Post-incident analysis distinguishes facts from causal hypotheses.
Temporary mitigations have expiry or review triggers.
An incident can proceed under delegated agent authority without unnecessary sponsor interruption.
''')
add("D13","Operations automation and change safety","DYNAMIC","products with automated operational actions","Exercise scheduled and triggered operations under valid, denied and partial-failure conditions; inspect idempotency, receipts and rollback.", '''
A scheduled operation records whether it actually ran.
Retries use an idempotency mechanism appropriate to their side effects.
Operational automation validates its target environment before mutation.
A dry-run is distinguishable from a completed live action.
Partial failure leaves a recoverable state and explicit receipt.
Automated actions respect the selected maintenance or resource constraints.
A failed permission check cannot be bypassed by fallback execution.
A reversible operational change has a tested reversal path.
Configuration drift is detected against the accepted baseline.
A disabled automation does not continue through orphaned workers.
''')
add("D13","Continuity and long-lived service burden","SEMANTIC","products expected to remain operated or supported","Review actual service dependencies, expiry events, operating work and continuity scenarios; validate the highest-risk assumption with an exercise.", '''
Critical external service dependencies have identifiable failure consequences.
Credential or certificate expiry has a renewal and detection path.
The service can be transferred to another authorized operator or agent session.
Recurring maintenance obligations have owners or automated execution.
A loss of the original developer workstation does not destroy required operating knowledge.
The support lifetime is consistent with available maintenance resources.
Unfunded recurring dependencies are visible in lifecycle decisions.
A provider exit or migration scenario has a bounded fallback plan.
Required operational artifacts have retention and recovery policies.
A continuity claim is limited to scenarios actually supported by evidence.
''')

add("D14","Threat model and trust boundaries","SEMANTIC","subjects with security-relevant capabilities","Map assets, actors, entrypoints and trust boundaries; derive plausible misuse cases and challenge assumptions with authorized tests.", '''
Sensitive assets are identified for the selected product slice.
External and internal trust boundaries are distinguishable.
Threat actors are matched to actual exposure and capabilities.
Abuse cases include misuse of legitimate authenticated access.
Agent-readable untrusted content is identified as a potential instruction-injection surface.
Security assumptions identify the controls on which they depend.
Threat mitigations map to testable obligations.
Residual risks have explicit owners or acceptance decisions.
New entrypoints trigger a threat-model review.
A threat-model document alone is not treated as proof of implemented protection.
''')
add("D14","Authentication and session security","DYNAMIC","subjects with identities or sessions","Use synthetic accounts to exercise valid, invalid, expired, revoked and replayed credentials against actual authentication boundaries.", '''
Invalid credentials cannot create an authenticated session.
Expired credentials are rejected according to the session policy.
Revoked credentials cease to authorize protected operations.
Session identifiers are not exposed through unnecessary public channels.
Logout invalidates the promised session scope.
Authentication failures do not reveal sensitive account details beyond policy.
Credential rotation preserves intended access without accepting obsolete secrets indefinitely.
Session fixation or replay is evaluated against the actual threat model.
Optional authentication absence cannot silently expose a protected production path.
Authentication test evidence uses the real selected identity boundary rather than mocks alone.
''')
add("D14","Authorization and tenant isolation","DYNAMIC","subjects controlling access to resources or actions","Exercise a permission matrix with synthetic principals across direct, indirect and cross-tenant resource paths.", '''
Protected operations verify the caller's permission at the actual enforcement boundary.
Resource ownership is checked for direct identifier access.
A lower-privilege user cannot invoke a higher-privilege action through an alternate route.
Cross-tenant reads are denied where tenant isolation is required.
Cross-tenant writes are denied where tenant isolation is required.
Permission revocation takes effect within the accepted window.
Background jobs preserve the initiating authorization scope.
Cached authorization does not outlive its declared validity.
A denied operation leaves protected state unchanged.
An agent-authored policy cannot grant host capabilities unavailable to its authority source.
''')
add("D14","Secrets and sensitive execution","DYNAMIC","subjects using credentials or sensitive configuration","Use synthetic secrets to inspect storage, logs, process arguments, artifacts and redaction paths under success and failure.", '''
Required secrets are not committed to ordinary source history.
Secret-like content in new changes is checked through the selected detection path.
Logs do not disclose the synthetic secret under expected failure conditions.
Child process arguments do not expose secrets when a safer supported channel exists.
Build artifacts exclude unintended credential material.
Credential scope is limited to the required operation.
Secret rotation has a verified consumer update path.
Redaction preserves diagnostic meaning without revealing protected values.
A missing secret remains an authority or environment blocker rather than a fake pass.
Sensitive captures remain within their authorized evidence store.
''')
add("D14","Input, protocol and dependency attack resistance","DYNAMIC","subjects processing untrusted inputs or dependencies","Run authorized malformed and adversarial fixtures against exposed boundaries; inspect containment and meaningful failure detection.", '''
Untrusted input cannot escape its intended command or query interpretation.
Filesystem paths are constrained to the authorized root where required.
Oversized inputs have bounded rejection behavior.
Malformed serialized data is rejected without corrupting accepted state.
Deserialization does not instantiate unintended executable behavior.
Untrusted URLs cannot access forbidden internal resources through the product.
Archive extraction cannot write outside the intended destination.
Dependency vulnerability findings identify the affected resolved version.
A mitigation is verified through the relevant reachable behavior.
Security tests do not use production victims or unapproved destructive payloads.
''')
add("D14","Supply chain, releases and security governance","STRUCTURAL","subjects distributing software or consuming executable artifacts","Trace release artifacts through source, build and publication records; verify selected signatures and security workflows against actual receipts.", '''
A distributed artifact maps to its actual source revision.
Build provenance identifies material inputs and the producing environment.
Artifact verification checks the expected identity rather than any valid signature.
Dependency and license inventory describes the distributed artifact scope.
Required release security checks executed on the actual release baseline.
A failed security gate cannot be silently marked successful by report editing.
Vulnerability disclosures have an authorized intake and response path.
Security exceptions identify scope, rationale and review date.
Publication credentials are separated from untrusted build execution where required.
A provenance receipt is not treated as proof that the product is correct or secure.
''')

add("D15","Data model and integrity","DYNAMIC","subjects storing or transforming durable data","Create representative valid and invalid records and execute supported transformations; compare against independently stated integrity predicates.", '''
Required fields cannot be silently omitted from accepted records.
Identifiers preserve their declared uniqueness scope.
Referential relationships remain valid across supported mutations.
Units and types remain consistent during data conversion.
Invalid state transitions are rejected.
Concurrent updates preserve the declared conflict semantics.
A failed transaction does not leave a forbidden partial state.
Round-trip serialization preserves required information.
Derived projections can be traced to authoritative records.
Integrity validation detects a deliberately corrupted fixture.
''')
add("D15","Migrations and compatibility","DYNAMIC","stateful products with schema or storage evolution","Run supported upgrade and rollback sequences on representative old datasets; inspect preserved information, locks and partial failures.", '''
A supported old dataset can be upgraded to the selected version.
Migration preserves required user information.
Migration records identify the source and target schema versions.
An interrupted migration has a supported continuation or rollback path.
Rollback limitations are explicit before the upgrade is accepted.
Concurrent access during migration follows the declared availability contract.
A migration cannot silently operate on the wrong environment.
Large-data migration behavior is evaluated under a representative volume.
Incompatible older consumers fail predictably after an unsupported transition.
A no-op migration is not reported as proof of data transformation correctness.
''')
add("D15","Privacy and data minimization","SEMANTIC","subjects handling personal, private or restricted data","Map actual data flows against purposes and authorized boundaries; validate the selected minimization and redaction behaviors with synthetic records.", '''
Collected sensitive fields have a stated product purpose.
Unnecessary sensitive data is not collected by default.
Data flows identify external processors or destinations.
Private research or source content is not published through a generated index accidentally.
Access to raw evidence follows the sensitivity of its contents.
Telemetry collection distinguishes required operations from optional analytics.
Derived embeddings or caches are included in the data-flow review when relevant.
A public demo uses authorized synthetic or appropriately redacted data.
Privacy claims identify their scope and supporting observations.
Unresolved legal or consent obligations remain explicit rather than inferred from a technical pass.
''')
add("D15","Retention, deletion and export","DYNAMIC","products retaining user or operational data","Exercise retention expiry, scoped deletion and authorized export using representative linked records and derived stores.", '''
Retention periods are defined for the relevant data classes.
Expired data is removed or retained under an explicit exception.
Deletion targets the authorized subject rather than unrelated records.
Required deletion propagates to relevant derived stores.
Backup retention limitations are disclosed in deletion claims.
Exports contain the promised data scope in a usable format.
Export authorization prevents access to another principal's data.
A deleted record is not recreated silently from a stale projection.
Permitted integrity metadata can survive without retaining prohibited raw payloads.
Deletion and export receipts identify their actual completed scope.
''')
add("D15","Lineage, synchronization and reconciliation","DYNAMIC","subjects with replicated, derived or synchronized data","Create controlled divergent updates and replay deliveries; verify identity, ordering, conflict handling and provenance.", '''
A derived record identifies the source version used.
Duplicate delivery does not duplicate the logical object.
Out-of-order events follow a declared reconciliation rule.
Conflicting updates preserve enough information for resolution.
A failed synchronization remains visibly pending or blocked.
Local completion is distinguishable from remote registration.
Projection rebuilding produces the expected state from accepted records.
A stale source cannot silently overwrite a newer accepted state.
Cross-device timestamps are not treated as total ordering without a justified clock model.
Reconciliation preserves supersession and correction history.
''')
add("D15","Dataset and model-data quality","DYNAMIC","subjects using datasets, retrieval corpora or model training/evaluation data","Inspect provenance and split definitions; run leakage, contamination, missingness and representative-query tests on permitted data.", '''
Dataset records identify source and permitted use.
Training and evaluation partitions follow the declared separation rule.
Duplicate or near-duplicate examples are considered in leakage analysis.
Labels have a documented interpretation and review process.
Missing or malformed records have an explicit disposition.
The dataset represents the workload population claimed by the result.
Evaluation holdouts are not exposed to the implementation path unintentionally.
Retrieval freshness and deletion behavior are tested.
Synthetic data is identified separately from observed data.
A dataset revision invalidates affected results when its material contents change.
''')

add("D16","Packaging and clean installation","DYNAMIC","distributable software","Install the actual built or released artifact into a clean consumer environment; inspect contents, startup and uninstall behavior.", '''
The package contains the files required for its promised capability.
A clean consumer can install the selected artifact.
Installation does not rely on the source repository being present.
The installed version is discoverable.
Required platform dependencies are detected with useful diagnostics.
Installation avoids overwriting unrelated user files.
The first installed smoke test exercises real product behavior.
Uninstall removes owned resources without deleting unrelated data.
Package metadata identifies the intended platform and runtime constraints.
A successful package build is not reported as a successful clean installation.
''')
add("D16","Release and artifact acceptance","DYNAMIC","products producing versioned releases","Rebuild or inspect the release candidate, verify required checks and exercise the artifact promoted to the release channel.", '''
The release version identifies a distinct intended baseline.
Required checks ran against the actual candidate artifact or its traceable source.
Release notes distinguish shipped changes from planned work.
The artifact digest matches the published or installed artifact.
A release tag cannot substitute for missing build evidence.
Promotion rules identify who or what may authorize publication.
A failed mandatory gate blocks the affected release.
Release rollback identifies a usable prior artifact.
A release receipt identifies the actual publication destination.
A source-level pass is not silently promoted to a release-level pass.
''')
add("D16","Deployment and runtime publication","DYNAMIC","products with hosted or service deployments","Deploy only within actual authority to a controlled target, verify routing and runtime behavior, and record honest blocked states for unavailable rights.", '''
The deployment target is distinguishable from a similarly named environment.
Required runtime configuration is present without leaking secrets.
The deployed artifact matches the intended release digest.
Routing reaches the actual intended product surface.
TLS or equivalent transport expectations are verified where applicable.
Health and core-journey checks pass after deployment.
A failed deployment leaves an observable status and recovery path.
DNS or domain naming declarations are not treated as proof of live availability.
Deployment logs identify the actual actor and target.
Missing deployment authority does not block unrelated local verification.
''')
add("D16","Updates, compatibility and deprecation","DYNAMIC","products expected to evolve for installed consumers","Exercise supported update and downgrade paths with representative user state; test version skew and deprecation messaging.", '''
A supported installed version can update through the documented path.
Updates preserve required user configuration and data.
An update failure has a supported recovery path.
Incompatible changes are communicated before the affected operation.
Supported client-server version combinations are exercised.
Deprecated interfaces expose their support and removal window.
The product does not require an undocumented forced migration.
A removed feature identifies affected consumers and alternatives.
Update verification uses the installed artifact rather than only source tests.
Rollback limitations are disclosed before a consequential update.
''')
add("D16","Documentation publication and discoverability","DYNAMIC","products publishing documentation or landing surfaces","Generate and access the actual published output using explicit content allowlists; follow routes and verify source-to-page identity.", '''
Published documentation identifies the product version it describes.
Generated pages trace back to owner-held source documents.
Private content is excluded by an explicit publication policy.
Required navigation links resolve in the deployed route layout.
Search results do not expose excluded private records.
The landing page distinguishes a product, library, tool and conceptual project accurately.
Documentation hosting does not become authoritative product state by accident.
A docs build pass is distinguishable from successful publication.
A changed source triggers a visible publication freshness state.
Canonical routes preserve justified aliases until a tested cutover.
''')
add("D16","Adoption, support and consumer evidence","OBSERVATIONAL","products intended for actual internal or external consumers","Observe an authorized real consumer using the delivered artifact; retain support friction, outcomes and evidence labels.", '''
An actual consumer can find the correct supported entrypoint.
Adoption evidence identifies the consumer and observation context appropriately.
Internal dogfooding is labeled separately from external adoption.
A support request has an identifiable intake and resolution path.
Known limitations are discoverable before consequential use.
Consumer-reported failures link to reproducible or explicitly unresolved findings.
A claimed case study uses observed outcomes rather than invented testimonial text.
Support burden is measured or explicitly estimated with uncertainty.
The consumer can identify the version involved in a problem.
Adoption claims do not count automated test invocations as independent customers.
''')

add("D17","Record identity and schema integrity","STRUCTURAL","all protocol records","Validate the actual record structure, identifiers and cross-references; perturb revisions, types and references to verify rejection.", '''
Records have stable unique identifiers within their declared namespace.
Each record declares its schema version.
Required fields cannot be omitted silently.
Unknown record types are not accepted as known facts.
References resolve to the intended record or remain explicit unresolved links.
Malformed timestamps cannot masquerade as valid observation times.
A record's content digest is computed over a documented representation.
Duplicate identifiers with different contents produce a conflict.
Extensions cannot silently change the meaning of required fields.
Template records are distinguishable from accepted operational records.
''')
add("D17","Subject, evidence and report provenance","STRUCTURAL","all assessments","Resolve subject, report, artifact, evaluator and evidence identities; recompute local digests and reject incorrect bindings.", '''
The result identifies the subject snapshot actually measured.
The report-storage revision is separate from the evaluated source revision.
Registry receipt identity is separate from local report completion.
Evidence bytes match their recorded digest when locally verifiable.
The evaluator and fixture revisions are identifiable.
Observation time is separate from report-production and registration time.
Dirty-worktree evidence records material uncommitted contents distinctly.
A previous report is not accepted as fresh product evidence by itself.
A superseding result preserves the earlier result identity.
A hash record alone is not represented as an independently trusted signature.
''')
add("D17","Scoring and maturity integrity","STRUCTURAL","all scorecards and maturity reports","Recompute totals from the frozen assignment and effective result set; inject unknowns, stale passes, exclusions and gate failures.", '''
Assessment coverage is reported separately from assessed pass rate.
Unknown results do not count as verified passes.
Stale evidence cannot satisfy a current gate without an accepted reuse justification.
Unresolved applicability remains visible outside the settled denominator.
A critical gate cannot be compensated by unrelated low-risk passes.
A waiver remains distinguishable from a pass.
Duplicate criteria cannot create extra score weight.
Empty denominators yield undefined values rather than perfect scores.
Maturity is scoped to a beneficiary slice and actual product baseline.
Scores across changed epochs distinguish product, evidence, scope, evaluator and policy deltas.
''')
add("D17","Assignment epochs and self-amendment","SEMANTIC","agent-defined assignments and evaluators","Compare frozen and proposed baselines, qualify changed obligations and inspect amendment authority; preserve urgent-stop semantics.", '''
An execution epoch freezes the material assignment and acceptance meaning.
The assignment has a valid and a meaningful invalid witness where feasible.
Requirement contradictions have a visible refutation or resolution record.
Changing a grader creates an attributable evaluator revision.
Removing an obligation identifies the rationale and affected consumers.
The builder cannot silently reduce an active acceptance threshold.
A corrected oracle does not retroactively rewrite the old product verdict.
An urgent safety or integrity defect can stop affected promotion before the next scheduled review.
Self-amendment remains inside actual delegated policy authority.
The bootstrap trust boundary is declared as an assumption rather than an absolute guarantee.
''')
add("D17","Ledger, outbox and concurrency integrity","DYNAMIC","records synchronized across workers or registries","Replay, duplicate, reorder and interrupt deliveries; verify idempotency, conflict detection and honest local-versus-remote state.", '''
Each delivery has an idempotency identity.
Duplicate delivery does not create duplicate accepted events.
Concurrent producers do not overwrite one shared mutable event record.
A failed delivery remains queued or blocked with its actual reason.
Receipt contents identify the payload actually accepted by the destination.
An outbox item is not reported as a completed registry write.
Correction events preserve the original history.
Conflicting accepted projections require explicit reconciliation.
A stale writer cannot overwrite a newer projection without detection.
Registry unavailability does not prevent independent authorized local work.
''')
add("D17","Assurance boundaries and evaluator security","DYNAMIC","evaluation pipelines and autonomous decision paths","Inject forged records, untrusted instructions, altered fixtures and unauthorized effects; inspect actual enforcement and independent observations.", '''
Repository instructions cannot redefine the evaluator's actual permissions.
A forged self-reported success cannot replace required raw evidence.
Protected holdouts are inaccessible to unauthorized implementation workers.
Verifier output is bound to the intended artifact.
A compromised optional report renderer cannot change accepted measurements.
Semantic reviewers have an explicit unknown or contested outcome.
Independent verification claims identify the real separation mechanism.
An unavailable required expert evaluation remains a visible limit on the claim.
An evaluator update is tested against both known-good and known-bad cases.
Qualification of one instrument is not generalized to untested adapters.
''')

add("D18","Stage and slice maturity","SEMANTIC","all product lifecycle assessments","Evaluate the selected stage's conjunctive gates against actual current evidence; keep value evidence and readiness axes independently visible.", '''
Concept maturity does not imply implemented behavior.
A feasibility prototype resolves a named technical uncertainty.
An integrated prototype demonstrates the selected end-to-end controlled journey.
A slice MVP delivers its minimum promised outcome to the defined beneficiary slice.
Supported-product status includes the relevant maintenance and recovery obligations.
Publication readiness is separate from product functionality.
Operational readiness is separate from successful deployment.
Value evidence is not inferred from engineering quality.
One mature slice does not promote an unsupported broader product scope.
Stage promotion identifies the exact evidence and assignment baseline supporting it.
''')
add("D18","Portfolio allocation and lifecycle choices","SEMANTIC","subjects receiving ongoing lab resources","Compare improve, experiment, narrow, merge, maintain, pause, pivot, retire and no-action alternatives under the actual mandate and resource envelope.", '''
Allocation decisions identify the outcome or uncertainty they fund.
A low engineering score is not treated as proof of absent demand.
A high engineering score is not treated as proof of beneficiary value.
The decision considers integration and maintenance burden.
A merge alternative examines unique capability and consumer dependencies.
A pause can preserve research value without implying deletion.
Pivot decisions identify the evidence that invalidated the previous thesis.
Resource changes remain within actual delegated limits.
Lifecycle choices have review and reversal conditions.
Repeated noisy observations do not force uncontrolled oscillation between dispositions.
''')
add("D18","Retirement, migration and custody","DYNAMIC","subjects being absorbed, archived or removed","Inventory live consumers and retained assets, exercise migration, verify custody and perform only authorized lifecycle effects.", '''
Retirement identifies actual dependent consumers.
Unique retained capabilities have a destination or explicit abandonment decision.
Data custody is established before removing the original store.
Migration preserves required identifiers and history.
Consumer compatibility is tested at the migration target.
The original remains recoverable until accepted cutover conditions are met.
Archival permission is distinguishable from deletion permission.
Public references point to the accepted successor or explain the retirement.
Retirement receipts identify the action actually performed.
An unused repository can be paused without falsely claiming full migration completion.
''')
add("D18","Economics and bounded resource use","OBSERVATIONAL","agent-operated work with resource costs","Collect actual worker, tool, runtime, setup, verification and rework observations; compare accepted outcomes under a declared budget.", '''
Resource accounting includes unsuccessful attempts.
Verification cost is included alongside generation cost.
Setup and environment-recovery effort are counted when material.
Elapsed latency is reported separately from aggregate worker time.
Cumulative task spending survives session replacement.
An exhausted budget produces an explicit stop or reallocation decision.
Economic claims distinguish observed costs from assumptions.
The denominator is an accepted outcome or defined learning result rather than a rubric point.
Parallelism benefits are compared with collision and integration overhead.
New infrastructure work names a concrete consumer and observed blocker.
''')
add("D18","Convergence, stalls and restart policy","OBSERVATIONAL","iterative agent execution","Compare attempts under a fixed success definition; retain failure fingerprints, reopened defects and censored work, then classify stalls before intervention.", '''
Progress comparisons identify a stable assignment epoch.
A repeated failure signature is retained across sessions.
A stalled run is checked for environment failure before blaming implementation.
A stalled run is checked for oracle defects using valid and invalid witnesses.
A contract contradiction can trigger a new assignment epoch.
Reopened defects are subtracted from naive closure counts.
Restart, replay, reseed, replan and contract revision are separately recorded.
Unsolved attempts remain in time-to-outcome analysis.
The process does not claim eventual success solely from repeated attempts.
A next action targets a discriminating observation rather than identical unbounded retries.
''')
add("D18","Lab autonomy and institution-level validation","DYNAMIC","the evaluation protocol and agent lab itself","Run a bounded no-platform vertical slice with agent-derived intent, qualified grading, an actual change or experiment, and a fresh-session handoff.", '''
The lab can begin authorized work without a human-authored local repository idea.
A missing central platform does not block the file-first execution path.
A fresh agent can reconstruct accepted state from retained records.
The loop produces a real measurement or discriminating experiment rather than only new plans.
A planted false pass is rejected through the actual verification path.
Agent-generated opportunities do not automatically become mandatory backlog.
Sponsor feedback is typed without turning every idea into an obligation.
An agent can recommend stopping or merging its own project when evidence warrants it.
The institution preserves learning when a worker is replaced.
Lab-level assurance claims remain limited to the workflows and boundaries actually tested.
''')

assert len(PILLARS)==108, len(PILLARS)
assert sum(len(p['predicates']) for p in PILLARS)==1080
