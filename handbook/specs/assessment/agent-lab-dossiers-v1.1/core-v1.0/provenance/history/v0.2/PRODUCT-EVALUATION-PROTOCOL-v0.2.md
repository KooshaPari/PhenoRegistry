# Product Evaluation Protocol — preliminary v0.2

Status: PROPOSED DESIGN, not an accepted authority migration, production evaluator, or recovered canonical catalog.
Prepared: 2026-09-10.
Scope: repository and whole-product inventory, assessment, gap discovery, maturity, and bounded autonomous lifecycle decisions.

## 0. v0.2 — autonomous-lab clarification

This revision incorporates the user's clarification on 2026-09-10. The target is a software lab operated by agents, including product discovery, repository creation and decomposition, intent derivation, requirements, implementation, evaluation, and lifecycle decisions. A human may supply high-authority feedback but is not a required author, operator, or approver for each repository. “By hand” means agents executing a portable procedure with text records and existing tools; it does not require a person to fill in a form.

The control problem is broader than grading a product against a supplied assignment: agents must construct, qualify, solve, and revise the assignment itself. Authority, factual support, and decision commitment are separate. Agent authorship is not a defect; an unsupported claim or an unauthorized action is.

The bootstrap MUST run without live AgilePlus, Tracera, RepoLedger, or any other unfinished portfolio service. Subject-held records and existing harnesses are sufficient. Live integrations are replaceable transports/projections and cannot veto unrelated, otherwise authorized local work. Registry unavailability remains visible; it does not make a local report falsely registered or stop every product task.

Changes relative to v0.1:

1. Agent-derived and agent-originated intent and repository genesis are explicit first-class records.
2. Assignment/evaluator qualification is separate from product verification and beneficiary validation.
3. Assignments are frozen for execution epochs; revisions require an explained contract change, not a silent moving target.
4. Restartable sessions consume durable evidence, rejected attempts, and exact current state instead of restarting institutional memory.
5. Convergence, economics, scope change, and evaluator improvement are measured separately; eventual success is not guaranteed.
6. Human feedback is a typed high-authority input. Routine autonomous work does not wait for a person to restate already delegated authority.
7. Bootstrap and strategic experimentation may proceed under an existing mandate; a separate platform implementation is never a prerequisite.

Sections 19–27 specify these additions. The retained v0.1 source inspections are historical, bounded findings; they have not been re-audited in this revision. This document and its companion files are design and operating instructions, not an implemented evaluation engine or an authorization grant.

## 1. Decision

Build one evidence-backed evaluation protocol with distinct objects and generated views. Do not merge inventory facts, verification results, maturity decisions, and investment decisions into a single spreadsheet score. The scorecard is an output, not the underlying state store.

The intended loop is:

`mandate + observations -> agent-derived mission and assignment -> assignment qualification -> locked execution epoch -> implementation and measurement -> findings and validated learning -> policy decision -> next epoch or lifecycle action`

“Tracera by hand” should mean using portable records and disciplined procedures before depending on the live Tracera product. It should not mean inventing a competing traceability service inside AgilePlus.

This proposal treats the spoken “Azure Plus” as AgilePlus, consistent with the recovered project context. It does not require Azure services.

### Verified source findings and limits

A bounded inspection found the following; none establishes complete local-device or Git-history coverage:

- Benchora has an 88-pillar checker at `scripts/scorecard_ci.py`, inspected at `8520ca49db1d4da3e42fea2a11c243aff9112eb4`. Many checks test names and file/directory existence, including coverage configuration, rollback-like names, and benchmark directories. These are structural inventory signals, not proof of functioning capabilities. Its broad library/CLI exclusions need capability-specific review rather than automatic inheritance. [I1]
- Tracera’s `audit/SCORECARD-FULL-2026-08-30.md`, inspected at `1f5122d6add50a16d55705378d2743223981c58d`, describes 11 clusters, 96 pillars, and 435/435 in its summary, while its displayed cluster table includes 12 clusters and 505/505. This is a report-consistency finding, not an independent verdict on the current software. [I2]
- The existing delivery contract explicitly distinguishes tools from registries; design, pipeline, product, publication, and operational readiness; measurement blockers from implementation blockers; and authentic product evidence from demonstrations. It also requires negative controls for the instruments themselves. [I3]
- The recalled historical sequence of 14, 30, 100+ pillars and 1,000+ atomic criteria has not been independently recovered and reconciled in this pass. Existing agents’ recovery outputs should be imported, not replaced with an invented count.

No repositories were built, tested, modified, merged, deployed, or archived for this proposal. No device-local audit was performed.

## 2. Ownership and interfaces

Preserve the existing authority boundaries. Verify exact destinations before applying writes.

| Surface | Proposed role in this protocol | Must not silently become |
|---|---|---|
| Subject repository/product owner | Product intent, requirements, local audit manifests, evidence references, exceptions, accepted decisions | A dumping ground for unrelated portfolio state |
| AgilePlus | Audit work packages, claims/leases, execution state, dependency routing, acceptance and remediation workflow | Portfolio registry or replacement Tracera |
| Benchora/evaluation owner | Check adapters, benchmark methodology, scoring reducers, evaluator qualification, regression evidence | Strategic product owner |
| Tracera | Eventual evidence graph, traceability, impact, audit/state projections | An immediate infrastructure prerequisite |
| RepoLedger/current registry instance | Repository identity, accepted lifecycle metadata, pointers to owner-held assessments | A second canonical copy of raw findings and evidence |
| ResearchLedger | External-source provenance, research and opportunity evidence | Product acceptance authority |
| SessionLedger | Actual agent-session/run evidence and replay pointers | Proof that an implementation works merely because a session says so |
| PhenoDocs | Rebuildable human-readable views | Registry or evidence authority |
| Accepted portfolio-policy owner | Resource mandate and strategic lifecycle decisions; integrate AGSLAG where its authority is actually accepted | An authority inferred from a rubric score |

Shared schemas belong in the verified shared-contract owner; do not create a new repository merely to hold this protocol. The immediate implementation is a portable agent procedure, subject-held files, existing machine checks, and small adapters only where needed. A CLI, database, graph service, or live AgilePlus/Tracera deployment is not required for v0. Every owner/approver role in this table may be an authorized agent function; the role does not imply a human bottleneck.

## 3. Canonical objects

Use distinct versioned records with stable identifiers.

**Subject snapshot.** Identifies the repository, component, package, product, release, deployment, or user journey being evaluated. Includes source revisions, tree/dirty-worktree digests when applicable, artifact digests, runtime/configuration fingerprints, platform, evaluation period, and relevant cross-repository dependencies.

**Mandate and intent node.** Records parent authority, origin, proposed beneficiary, expected outcome, assumptions, alternatives, resources, non-goals, factual support, review triggers, and the decision accepting or rejecting a derived intent. An agent-created repository may have no direct human request.

**Assignment capsule.** Locks a mission/intent revision, subject and beneficiary slice, requirements, criterion/evaluator/profile versions, evidence needs, environment, authority, resource envelope, non-goals, and stop rules for one execution epoch.

**Inventory item.** Records what exists, where it exists, what it declares, and how its presence was observed. A declaration, an inferred capability, an accepted requirement, and an observed behavior are different kinds of facts.

**Criterion definition.** Specifies the outcome to evaluate, applicability, measurement method, evidence requirements, anchors or thresholds, invalidators, negative controls, and provenance. A criterion is not an instance of a test on one platform.

**Evaluation result.** Records a criterion instance against a subject snapshot, its execution state, verdict, observation, evidence, freshness, and verifier identity. Results are append-only; correction produces a superseding record.

**Finding.** Captures an implementation failure, verification gap, contradictory claim, missing requirement, unexpected implemented behavior, research gap, opportunity, obsolete feature, or measurement defect. A finding is not automatically approved work.

**Decision.** Records accepted, rejected, deferred, or conditional dispositions, authority, rationale, alternatives, budget, stop conditions, and links to evidence and work packages.

**Assessment.** A manifest joining the exact subject set, catalog version, profile, results, findings, coverage statement, and derived reports. The scorecard, inventory, backlog, maturity view, and lifecycle recommendation are projections of this manifest.

Required relation types include `declares`, `requires`, `implements`, `exercises`, `verifies`, `contradicts`, `depends_on`, `supersedes`, `invalidates`, `motivates`, and `authorized_by`, `derived_from`, `qualifies`, `refutes`, `accepted_under`, and `observed_by`. Sharing a link or file path alone does not establish one of these semantic relationships.

## 4. Coverage architecture

Do not make pillar count the success criterion. Use a navigable hierarchy:

`domain -> pillar -> criterion -> scoped instance -> observation/evidence`

Keep the number of executive domains small enough to understand. Allow 100+ pillars and 1,000+ atomic criteria where distinct outcomes justify them. Do not multiply synonymous controls, platform instances, or paraphrases of third-party requirements and call that deeper coverage.

### Candidate domain map

These are proposed navigation groups, not recovered historical counts.

| Domain | What it must expose |
|---|---|
| Intent and value | Target beneficiaries, actual problem, outcomes, non-goals, alternatives, differentiation, reasons to stop |
| Research and decision quality | Source quality, freshness, competing explanations, untested assumptions, rejected options, experiments |
| Scope and capabilities | Accepted requirements, undeclared discoveries, end-to-end journeys, boundaries, slice completeness |
| Architecture and tradeoffs | Interfaces, dependency direction, failure domains, change scenarios, performance/security/modifiability tensions |
| Implementation and maintainability | Correctness, contracts, coupling, dependency health, unsupported paths, duplication, configuration design |
| Test and assurance quality | Behavioral coverage, assertions, integration/E2E tests, mutation/fuzz/property tests where applicable, oracle validity |
| Developer experience | Fresh checkout, setup, inner-loop latency, debug quality, docs, examples, contributor workflows |
| Agent experience (AX) | Headless operation, machine-readable outcomes, discovery, bounded permissions, reset/replay, leases, cancellation, parallelism |
| User experience | Task completion, recovery, navigation, onboarding, error/loading/empty states, content clarity |
| Accessibility and internationalization | Keyboard/assistive-technology journeys, visual access, language/locale behavior, inclusive evaluation coverage |
| Visual and interaction polish | Design consistency, hierarchy, spacing, motion, responsiveness, product-specific craft and coherence |
| Performance and resource use | Latency distributions, throughput, memory, CPU/GPU/storage/network, concurrency, mixed-load interference, cost per outcome |
| Reliability and operations | Failure behavior, observability, incident response, recovery, restore, upgrade and rollback |
| Security and trust | Threat model, authorization, secrets, abuse paths, dependency/build/source provenance, least privilege |
| Data stewardship | Integrity, migrations, retention, privacy, export/delete, lineage, backup and restoration obligations |
| Distribution and adoption | Packaging, clean install, updates, compatibility, deployment/publication evidence, support and adoption friction |
| Governance and evidence integrity | Ownership, authority, claims, reproducibility, freshness, exceptions, provenance and metric integrity |
| Viability and lifecycle | Real beneficiary outcomes, operating burden, resource envelope, sustained value, pivot/merge/retire triggers |

Accessibility remains separate from agent experience even when the shorthand AX is ambiguous. Backend, library, CLI, desktop, web, mobile, game/mod, infrastructure, data, and ML/agent products get relevant profile packs. Platform, user persona, release channel, risk, and lifecycle target are additional selectors.

Start with universal outcome requirements, then add product-form, capability/risk, and slice-specific obligations. File names and vendor products are adapters, not universal requirements. A native isolated environment can satisfy reproducible execution without a Dockerfile. A CLI may still require accessibility, privacy, performance, rollback, or authentication checks when its actual behavior makes them relevant.

Every run freezes its subject universe, selected profiles, accepted exclusions, and weights before grading. Unresolved applicability is visible and blocks any maturity decision depending on it.

## 5. Recover and normalize existing templates

Existing local agents should emit a template census before deleting, consolidating, or replacing sources.

For each artifact retain its stable source identifier, device/repository, exact path, commit/blob or content digest, observed branch/worktree, timestamps, declared schema/rubric version, owner, lineage, and collection coverage. Capture uncommitted local variants distinctly from Git revisions. Missing permissions, shallow history, unavailable devices, and index-only searches must remain explicit coverage limits.

Classify sources as templates, generators, executable checkers, result instances, generated reports, historical plans, or abandoned drafts. An audit report is not automatically the rubric that generated it.

Normalize by observable predicate and scope, not by label similarity. Preserve original IDs through crosswalks with relations such as `equivalent`, `narrower`, `broader`, `overlaps`, `conflicts`, and `superseded`. Never assume two matching labels mean identical evidence requirements.

For every legacy criterion choose `adopt`, `split`, `merge`, `adapt`, `reject`, or `historical_only`, with reasons and source anchors. Rejected criteria remain discoverable. Do not merge away a meaningful contradiction.

Report separate counts for source artifacts, historical versions, unique predicates, source mappings, active criterion definitions, executable adapters, and evaluated instances. Count growth is not proof of quality growth.

## 6. Third-party framework integration

Import their useful structure without flattening their different meanings.

| Source family | Import | Limitation |
|---|---|---|
| Factory Agent Readiness | Repository/application scoping, environment and feedback-loop signals, agent-readiness progression | Not product usefulness, full quality, or deterministic proof [E1-E3] |
| ISO/IEC 25010:2023 | Product-quality coverage reference and vocabulary | Not a ready-to-run repository grader; this pass reviewed the public overview, not licensed full text [E4] |
| SEI QAW and ATAM | Quality-attribute scenarios, business drivers, alternatives, sensitivity/tradeoff points, risk themes | A document’s existence is not an architecture evaluation; label an automated adaptation accurately [E5-E6] |
| OWASP ASVS and SAMM | Security verification requirements and security-development maturity | Different assurance scopes; preserve their native versions/IDs and do not imply certification [E7-E8] |
| OpenSSF Scorecard and OSPS Baseline | Automated security heuristics plus maturity-specific baseline controls | Heuristic score and verified control satisfaction remain distinct [E9-E10] |
| W3C WCAG, ACT, and evaluation guidance | Accessibility obligations, test-rule structure, evaluation coverage and result exchange | Automated results alone do not establish full accessibility [E11-E12] |
| DORA | Delivery-throughput and instability outcomes over time | Do not equate commit/deployment quantity with product value or compare unlike subjects [E13] |
| Google HEART | Goal-to-signal-to-metric mapping for user-centered outcomes | Instrumentation or simulated users do not establish real user benefit [E14] |
| SLSA/in-toto | Source/build/artifact provenance and attestation envelope conventions | Authentic provenance does not prove a quality verdict is true [E15] |

Each crosswalk must record source URI, source version/revision, retrieved date, native requirement ID, content digest where allowed, rights/license notes, local adaptation, applicability, and mapping strength. A standards update creates a candidate catalog migration; it must not silently change historical scores.

A useful source-drift example: Factory’s currently retrieved product page says eight technical pillars, while its current overview says nine. Preserve the source versions instead of treating the label “Factory readiness” as an immutable definition. [E1-E2]

## 7. Criterion contract

Every activated criterion must provide:

- Stable ID, immutable revision, title, intended outcome, source mappings, owner, and scope.
- Three-valued applicability: applicable, not applicable with accepted rationale, or unresolved.
- Measurement modality and a pinned adapter or anchored semantic-review procedure.
- Explicit observation shape, units, thresholds or behavioral anchors, and scope denominator.
- Evidence requirements, minimum assurance for each target gate, and the exact claim those artifacts support.
- Environment/permission requirements, timeout and resource budget, permitted side effects, and result/error semantics.
- Negative controls, known false-positive/false-negative risks, invalidators, and freshness policy.
- Severity, affected gate, remediation or research route, and dependencies.

Split conjunctive requirements unless their components form one intentionally indivisible outcome. For example, existence of rollback code, successful rollback execution, and preservation of user data are related but distinct claims. An end-to-end recovery gate can require all of them.

A criterion without a qualified measurement method remains a visible measurement-design task. It does not become a made-up semantic score to keep a spreadsheet complete.

## 8. Machine-first, without treating artifacts as outcomes

Use the cheapest adequate instrument, not the cheapest available proxy.

**Structural inspection:** Parse manifests, ASTs, schemas, configuration, repository metadata, and source-controlled contracts. Report declarations and presence as such.

**Executable verification:** Build, install, execute actual consumer journeys, test error paths, measure workloads, restore data, and verify emitted effects against explicit oracles. Record the real runner, arguments, fixtures, environment, artifact and dependency revisions, and raw output digests.

**Structured semantic review:** Evaluate coherence of intent and architecture, completeness of reasoning, UX/copy/polish, and research implications using behaviorally anchored questions. Require supporting and contradicting source anchors, alternatives, and an abstention path. Record model/provider/version when available, prompt/rubric digest, parameters, and result. Store concise review rationale, not private reasoning traces.

**Outcome observation:** Use authorized evidence from actual beneficiaries, consumers, or operations. Internal dogfooding can establish internal value, not automatically external market demand. Keep synthetic, simulated, researcher, sponsor, and independent-user evidence labeled separately.

A structured semantic reviewer can help evaluate many surfaces but is not a universal substitute for every required expert or real-user evaluation. When the method cannot support a claim, issue an evidence gap or a bounded experiment rather than fabricate certainty. W3C explicitly cautions that tools alone cannot determine full accessibility. [E11]

### Example: recovery capability

`rollback.sh exists` is inventory.

A stronger executable criterion is: within a named release/update scenario, inject a failed change into a disposable authorized environment, execute the documented recovery, and compare restored user data and externally observable behavior against the accepted pre-change oracle. The time budget and acceptable data-loss envelope come from the product contract, not a universal constant invented by the grader.

A README declaration, a mock-only test, or a successful compiler invocation cannot satisfy this behavioral criterion.

## 9. Truth states and scoring

Keep status dimensions separate:

- Applicability: `APPLICABLE`, `NOT_APPLICABLE`, `UNRESOLVED`.
- Execution: `NOT_STARTED`, `RUNNING`, `COMPLETED`, `ERROR`, `BLOCKED`.
- Verdict: `PASS`, `FAIL`, `UNKNOWN`, `CONTESTED`.
- Evidence state: `CURRENT`, `STALE`, `INVALID`, `MISSING`.
- Review/exception disposition: `ACCEPTED`, `PROPOSED`, `WAIVED`, `DEFERRED`, `REJECTED` where relevant.

A failed test is not the same as a runner error. A missing credential does not prove a product defect. A waiver is not a pass. Stale evidence remains historical evidence but cannot satisfy a current gate without an accepted reuse proof.

For binary criteria in a frozen applicable set A with positive weights, partition weights into P (current valid pass), F (current valid fail), and U (unresolved outcome, including missing, stale, disputed, or blocked evidence).

`assessed pass rate = P / (P + F)`

`assessment coverage = (P + F) / (P + F + U)`

`verified satisfaction = P / (P + F + U)`

`optimistic bound = (P + U) / (P + F + U)`

These are reporting quantities, not probabilities or calibrated confidence intervals. The range expresses unresolved outcomes within a declared scope. Report undefined denominators as null/not applicable, never 100%. Unresolved applicability is reported separately and prevents presenting a complete final aggregate for affected scopes.

Maintain group weights so splitting one predicate into cosmetic subcriteria does not create extra credit. Cross-framework mappings do not receive duplicate weight. Ordinal semantic ratings need explicit anchors and should not be casually treated as interval-scale measurements.

Critical gates are non-compensating: missing mandatory safety, authorization, data-integrity, core-journey, or release evidence blocks the relevant stage despite high scores elsewhere. The subject’s accepted policy decides which obligations are mandatory; neither the builder nor grader may relax them during remediation.

Existing delivery policies, including independently reported assurance floors and complete satisfaction of mandatory critical obligations, must remain inherited where accepted. This proposal does not reset them with a new average. [I3]

## 10. Features, missing requirements, and open-world discovery

A repository-only closed checklist can measure declared obligations while missing a defective product thesis. Add a separate discovery process rather than turning every imagined feature into debt.

Represent four views:

1. Declared: promises, requirements, intended users, non-goals, and plans.
2. Implemented: observable capabilities, interfaces, dependency paths, and unsupported branches.
3. Exercised: behavior actually covered by execution, including failure and recovery.
4. Beneficial: evidence that the behavior achieves the intended user or operator outcome.

Compare them bidirectionally. Detect promised-but-absent capabilities, implemented-but-unclaimed behavior, tests without meaningful oracles, claims without evidence, undocumented dependencies, and obligations implied by accepted usage. An undeclared ability to write durable user data can trigger data-integrity/restore obligations even if the README says nothing about them.

Use explicit finding classes:

`IMPLEMENTATION_GAP`, `VERIFICATION_GAP`, `REQUIREMENT_GAP`, `RESEARCH_GAP`, `OPPORTUNITY`, `CONTRADICTORY_CLAIM`, `UNDECLARED_BEHAVIOR`, `OBSOLETE_CAPABILITY`, `MEASUREMENT_DEFECT`.

Each finding has a next-action kind: implement, instrument, test, clarify requirement, research, run experiment, remove, or explicitly do nothing. Opportunities require evidence and acceptance before they become release obligations. Competitor feature parity is not automatically the desired product.

A bounded discovery run examines beneficiary jobs, journey phases, failure/recovery cases, risk surfaces, interfaces, accepted architecture scenarios, and evidence-backed alternatives. Record research questions, source coverage, freshness, unvisited frontier, budget exhaustion, and why searching stopped. Never claim a finite checklist has exhausted all possible missing features.

## 11. Intent, planning, UX, and polish

Intent review asks whether the target problem is concrete, the beneficiary is real or explicitly hypothetical, the promised improvement is observable, alternatives are credible, constraints are coherent, and there is a condition under which not building is the right choice.

Planning review asks whether work resolves the largest uncertainty, creates an end-to-end increment, identifies dependencies and true blockers, has reproducible acceptance criteria, fits the resource envelope, and names a stop/rollback condition. Spec volume and ADR count are not benefits.

Translate “shittiness” into diagnosable patterns: unsupported promises, decorative infrastructure, duplicated authority, excessive setup, incoherent navigation, nonfunctional controls, unrecoverable failures, vague errors, fake verification, and architecture burden disproportionate to the accepted use case.

For UX/polish distinguish mechanical checks from judgments. Measure broken layouts, overflow, keyboard behavior, loading/error/empty states, contrast-rule results, screenshots at accepted viewports, and journey outcomes where appropriate. Use anchored review for hierarchy, clarity, coherence, and deliberate visual craft. A screenshot can show a rendering, not prove that its controls work or that users understand the task.

For AX explicitly test machine-readable failures, stable interfaces, discoverability, resumability, cancellation, idempotency, deterministic reset, auth boundaries, and concurrent worker isolation. For DX test an actual clean consumer/contributor path. For performance test the declared workload and competing-load conditions, not a conveniently empty machine alone.

## 12. Maturity is scoped and multidimensional

Store maturity per `(product, beneficiary slice, journey, release/deployment, environment, target profile)`.

Useful gate labels are:

| Label | Minimum interpretation |
|---|---|
| Concept | Intent and hypotheses exist; implementation is not implied |
| Feasibility prototype | A named technical uncertainty has been tested |
| Integrated prototype | The intended journey works in a controlled environment; real beneficiary use is not yet established |
| Slice MVP | One accepted beneficiary slice can obtain its promised minimum outcome through a complete journey, with mandatory safeguards and feedback collection |
| Supported product | Installation/delivery, recovery, maintenance and support expectations are demonstrably met for the declared users |
| Validated/expanding product | Outcome and operational evidence justify continued adoption or wider investment under the mandate |

These are proposed operational labels, not universal industry definitions. Maintain separate evidence of viability: untested, internal/dogfood, external pilot, repeated benefit, sustained use. An experiment may be a legitimate MVP attempt while its value hypothesis remains unproven.

Alongside the label report independent readiness axes: `DESIGN_READY`, `PIPELINE_VERIFIED`, `PRODUCT_VERIFIED`, `PUBLISHED_VERIFIED`, `OPERATED_VERIFIED`, plus explicit value evidence and agent-readiness assessments. Do not infer one from another. [I3]

A product can be an MVP for a local single-operator slice and merely a prototype for a hosted multi-tenant slice. Component maturity does not automatically establish integrated-product maturity; evaluate cross-repository journeys at a consistent bill of materials.

## 13. Autonomous control loop

The grader observes and recommends; a separately versioned policy authorizes effects. “Grade this repository” must not itself authorize merging, deployment, spending, contact with users, deletion, or archival.

Permit autonomy through a standing mandate rather than requiring repeated human signoff for every ordinary action. The mandate specifies goals, non-goals, source/data permissions, budget, reversible actions, required evidence, risk thresholds, allowed lifecycle transitions, and stop/rollback rules.

Suggested modes:

- `audit`: assess and emit records; no product mutation.
- `plan`: derive or revise intent, requirements, experiments, and portable work packages; synchronize to AgilePlus when a qualified adapter is available.
- `improve`: implement already-authorized bounded work in an isolated branch/worktree, then independently verify.
- `operate`: take pre-authorized operational actions within declared limits.
- `portfolio`: propose or execute lifecycle/resource transitions only when explicitly covered by the standing mandate.

The decision set includes continue, improve, research, experiment, narrow, pivot, merge, pause, maintain, and retire. “Do nothing” and “the measurement is wrong” are valid alternatives. A low quality grade may justify repair; it does not establish lack of demand. A high quality grade may coexist with a product nobody needs.

For each major decision record the leading hypothesis, credible alternatives, supporting and contradicting evidence, cheapest discriminating experiment, expected consequence, cost/risk envelope, and reversal/stop condition. Compare resource allocation on actual goal progress and validated learning, not rubric points gained.

Use stable decision windows and hysteresis to avoid oscillating between pivots after noisy assessments. Stop after repeated unproductive repair, evidence corruption, unresolved authority, exhausted budget, or violated safety limits. Stop can mean preserving a research backlog rather than destroying a project.

Before retirement verify consumer dependencies, migration obligations, data custody, retained artifacts, rollback/revival conditions, and the authority for archival/deletion. Agents may autonomously stop allocating effort under a mandate without thereby gaining deletion permission.

## 14. Evidence storage and ledger consistency

A suggested local shape, adapted to the subject’s existing audit directory:

```text
.audit/
  context.yaml
  catalog.lock.json
  assessments/<run-id>/
    manifest.json
    inventory.jsonl
    results.jsonl
    findings.jsonl
    decisions.jsonl
    evidence-index.json
    report.md
```

This is a suggested layout, not a requirement to duplicate existing authority files. Sensitive raw evidence lives in an authorized local/private store; Git contains permitted records and digested references. Preserve authentic evidence masters separately from redactions, demos, and marketing assets. [I3]

Record distinct revisions:

- S: subject commit/tree and any dirty-patch digest actually evaluated.
- R: commit storing the completed assessment records.
- L: registry/ledger commit or receipt registering the assessment.

An assessment of S stored later in R does not claim it tested R. Do not attempt to put a commit’s own future hash inside that same commit. The assessment manifest names S; the later registry receipt can name R and the assessment content digest; a subsequent receipt can name L when needed.

Also record component/artifact/configuration/dependency digests, rubric/profile/scorer versions, observation start/end times, production time, ledger-recording time, actor and signer identities, environment class, prior/superseded event IDs, and source coverage. Observation time is not necessarily trusted wall-clock time; causal links and server receipts matter when devices disagree.

Avoid concurrent agents rewriting one shared JSONL file. Use one immutable artifact per event/run or per-producer append logs with reconciliation. Use idempotency keys and compare-and-swap acceptance for shared projections. Registry ingestion is at-least-once safe with duplicate detection; failed registration remains a visible state and can be retried without regrading.

A hash chain is tamper-evident only relative to a trusted external anchor; timestamps and Git commits alone do not prevent a privileged writer from rewriting history. Define who signs, who verifies, what roots are trusted, and how independent receipts/checkpoints are stored. SLSA/in-toto provide useful provenance conventions; audit-specific assertions need their own accurate predicate semantics rather than being mislabeled build claims. [E15]

Corrections append a superseding record. Do not rewrite a bad old grade as though it never happened. Retention/deletion controls must preserve permitted integrity metadata without forcing sensitive raw payloads into public Git.

## 15. Evaluator qualification and attack resistance

Treat repository content, tool output, and research text as untrusted inputs, not instructions to the evaluator. Run executable audits under explicit permissions and resource limits, preferably native disposable sandboxes/VMs compatible with the fleet. Do not execute arbitrary discovered commands on a privileged workstation.

Pin evaluator, rubric, policy and test oracles separately from the code being improved. An agent repairing a product cannot quietly weaken its gate or relabel an exclusion in the same acceptance path. Evaluator updates require their own qualification and version.

Maintain known-good, known-bad, deceptive, and adversarial fixtures. Required negative controls include:

- A rich-looking repository with empty configs, zero effective tests, and nonexistent behavior.
- A small useful CLI without irrelevant cloud infrastructure.
- A removed test suite, skipped required jobs, forced successful exit code, and disconnected/mocked-only integration.
- Wrong subject SHA, stale benchmark, altered artifact, and inconsistent report totals.
- Unauthorized applicability waiver, duplicated criteria, or a split designed to inflate weight.
- Prompt injection in repository docs and forged/self-reported results.
- A product with excellent engineering but no beneficiary evidence.
- A critical authorization or data-integrity failure hidden beneath many passing low-risk checks.

Test deterministic reducers for identical frozen inputs, aggregation arithmetic, stable denominators, duplicate handling, supersession and freshness. Measure semantic-review disagreement against independently adjudicated cases; previous reports may help identify deltas but must not become circular evidence. Separate build, verification, and strategic-decision responsibilities with independently controlled evidence paths where the risk warrants it. Another agent in the same trust domain is not automatically independent assurance.

## 16. Execution economics and scheduling

Do not run every expensive check after every commit. Start with inventory and changed-scope impact analysis, then select affected checks while preserving periodic full and randomized audits for gaps in the dependency model.

Cache evidence by the relevant subject/dependency/environment/adapter/policy inputs. Invalidate on changes that affect the claim, not merely elapsed time; time-sensitive deployment and dependency-security claims also need freshness windows. Evidence reuse requires a recorded justification. A clean source tree does not imply unchanged deployment settings.

Order work by severity, user impact, uncertainty reduction, dependency unblocking, cost, and risk. A useful prioritization heuristic can include expected outcome benefit and value of information, but uncalibrated estimates must not be presented as precise economics. Preserve minimum coverage across risk classes so cheap checks do not monopolize the budget.

## 17. Implementation sequence and acceptance

**Recover in parallel.** Ingest current agents’ template census and source lineage while bounded local assessments proceed. Deliver an ambiguity/contradiction register, not a prematurely declared canonical rubric. A full historical census is not a prerequisite to a safe useful first assessment.

**Define the smallest records.** Start with the companion session prompt and bootstrap template using existing harnesses. Use subject identity, outcome states, evidence references, catalog/profile locks, and simple reducers as needed. Add executable validation incrementally; do not turn schema perfection into a new infrastructure dependency.

**Qualify a vertical slice.** Choose a deliberately diverse few subjects: a library/CLI, a UI product, and an integrated service or agent system. Prove derived assignment -> qualified checks -> semantic review where needed -> findings -> portable authorized work -> separate recheck -> local receipt and optional registry outbox. Exercise the no-platform path deliberately.

**Expand the catalog.** Import and deduplicate the 1,000+ candidate predicates if recovery and external mappings support them. Activate each with applicability, source provenance, an adequate instrument or explicit measurement gap, and negative controls. Do not pad the count.

**Enable bounded remediation.** Use standing authority, isolated work, evidence invalidation, and independently verified acceptance. Keep assessment delta separate from product delta and policy delta.

**Exercise strategic autonomy within evidence and authority.** Agents may propose goals, shape repositories, and perform reversible experiments immediately when covered by the existing mandate. Evidence requirements increase with consequence and irreversibility. Do not require human-written local intent or completion of a central platform. Before consequential resource, consumer, or retirement actions, verify the relevant outcome, authority, dependency/custody, and stop-rule evidence.

The v0 acceptance test is not “a large catalog exists.” It is: one real failing outcome is detected without a human interpreting undocumented context; it becomes a correctly owned, bounded action; a repair or experiment runs within authority; an independent verifier demonstrates the result; the subject records reconcile and registry delivery is either receipted or honestly queued/blocked; a planted false pass is rejected; and no unrelated maturity claim is promoted.

## 18. Generic agent contract

> Operate the named subject under the actual standing mandate. Do not assume a human-authored assignment exists. Recover or derive the subject's intent and repository role, preserving parent authority, hypotheses, alternatives, and provenance. Qualify the assignment and its grading instruments before treating passes as meaningful. Lock each bounded execution epoch. Evaluate the subject at an exact snapshot using the applicable catalog; distinguish declarations, observations, assumptions, and accepted obligations. Execute available machine checks and anchored semantic reviews. Preserve unknown, blocked, contested, stale, and out-of-scope states. Discover implied obligations without turning every speculative feature into debt. Perform authorized work, independently recheck, and record accepted outcomes or learning. When stuck, diagnose the contract, oracle, environment, strategy, and actual implementation before repeating. Checkpoint durable evidence and a precise fresh-session packet. Run locally without requiring unfinished portfolio tools; queue integrations rather than inventing receipts. Derive new goals and lifecycle proposals under the mandate, and escalate only the boundary that genuinely requires more authority, unavailable evidence, or a reserved human decision.

## 19. The lab operates three coupled loops

| Loop | Its question | Its principal outputs |
|---|---|---|
| Mission/portfolio | What outcome deserves effort, for whom, and why this product or boundary? | Intent hypotheses, experiments, resource/disposition decisions |
| Assignment and measurement | Do the requirements and graders represent that outcome, and can they distinguish success from failure? | Qualified assignment, oracle evidence, applicability and uncertainty |
| Execution | Can a worker realize the frozen assignment and preserve required existing behavior? | Candidate artifact, measurements, counterexamples, accepted result |

All three loops may be operated by agents. They are different responsibilities, not necessarily permanent agents or different products. A small bootstrap can run them sequentially in separate sessions with constrained inputs and permissions.

The execution loop is closed only relative to its locked assignment. The other loops keep the system open to new evidence: a consistently passing implementation may still pursue the wrong problem. Verification and validation serve different purposes; NASA distinguishes conformance to requirements from meeting mission/customer needs. [R1]

The desired economic hypothesis is that low-cost, replaceable workers can make more assurance affordable without overwhelming delivery with process overhead. This is a hypothesis to measure by actual resource use and accepted outcomes, not a universal claim that more agents or more documentation improve ROI.

## 20. Agent-derived intent, repo genesis, and high-authority feedback

An intent node MUST separate:

- Authorship: human-authored, agent-derived, agent-originated, inherited, or mixed.
- Authority: the parent mandate and allowed scope; proposed, delegated, or unauthorized where applicable.
- Epistemic status: hypothesis, supported, contradicted, or unknown, with source evidence.
- Commitment: proposed, accepted for experiment, accepted for implementation, deferred, rejected, or superseded.

An accepted experiment is not a proven market opportunity. A human instruction can authorize a preference or resource decision; it does not retroactively turn a failed test into a passed fact. An agent may legitimately invent a repo name, boundary, and goal within a portfolio-shaping mandate. Lack of a direct human quote for that local goal is not a failing criterion.

For repository genesis, record the beneficiary or consumer, parent capability, rationale for a separate boundary, alternatives (module, package, existing repo, upstream, no build), release/deployment/security/coupling consequences, smallest discriminating experiment, and reversal/absorption trigger. For pre-existing agent-born repos with missing lineage, record a provenance gap; do not forge an original mandate or assert the present explanation was historical intent. Authorized read-only investigation and current-state evaluation can continue.

Trace validity does not itself establish semantic validity. The edge from parent intent to child requirement needs a rationale and possible refutation, not merely an ID link. Also record external observations: real consumer programs, operational effects, authoritative interface behavior, or permitted beneficiary feedback. A chain consisting solely of agents repeating each other's claims is not independent outcome evidence.

Feedback from the sponsor is classified as binding instruction, preference, observation, question, brainstorm, or override. Preserve exact source and interpretation. A binding instruction changes the relevant mandate or acceptance baseline; a brainstorm need not become a mandatory feature. Ambiguous feedback can be treated as a provisional hypothesis for reversible exploration rather than stopping all work. Truly ambiguous permission for irreversible effects remains unresolved.

## 21. Assignment qualification: the agents build and test the maze

An assignment capsule contains:

`mandate/intent revisions + beneficiary/outcome + subject/BOM + requirements + accepted non-goals + criterion/profile/evaluator locks + fixtures/environment + evidence needs + permitted actions + resource envelope + stop/review conditions`

Before a capsule can support a maturity claim, qualify the material obligations against these questions:

1. **Relevance:** Does satisfaction support the parent outcome, rather than merely produce a convenient artifact?
2. **Consistency and feasibility:** Do requirements conflict? Are required resources and permissions available? Where feasible, use a small witness, reference solution, or prototype rather than a claim of solvability.
3. **Discrimination:** Does the grader reject known bad/no-op behavior and accept a valid non-identical solution? Are false-negative risks visible?
4. **Non-vacuity:** Did meaningful assertions execute against the real subject? Could an empty implementation, zero tests, or always-success return pass?
5. **Scope:** Are critical journey/failure cases represented? Is this a bounded and honest scope, not a completeness claim about all imaginable behavior?
6. **Resistance to circular evidence:** Are requirements derived from intent/observations instead of only copying current implementation behavior? Are high-risk judgments separated from the builder's mutable evidence path?
7. **Outcome anchoring:** Is there a way to test the intended benefit through actual consumer/environment effects, or an explicit unvalidated hypothesis?

Use known-good and known-bad fixtures, seeded faults, property/metamorphic tests, differential/reference behavior, real integration effects, and anchored semantic review as appropriate. Metamorphic and differential testing are established ways to address test-oracle limitations; each still depends on valid relations, references, and domain assumptions. [R4]

Positive controls matter as much as negative controls: a grader that rejects every solution is not qualified. Do not expose secret holdout contents through evaluator logs accessible to the implementation worker. A separate prompt alone does not create a security boundary; enforce read/write and execution separation where needed.

The rule is NOT “agents cannot modify the grader.” Agents may modify any derived artifact under their authority, including intent, evaluators, criteria, and policies. The rule is “a change is a new, qualified and attributable baseline, not retroactive proof of product improvement.” A correction to a broken test may be necessary; classify it as an evaluator correction, re-run affected evidence, and preserve the previous report.

## 22. Epochs, amendments, and the finite trust boundary

Within execution epoch E, freeze material intent, criterion meaning, severity/gates, exclusions, evaluator, and environment inputs. Workers may fix code and add exploratory tests but cannot silently redefine E's required pass conditions.

When new evidence challenges E, propose E+1. Record the change rationale, alternatives, affected claims, new/removed obligations, actual authority, qualification results, and migration impact. Re-score preserved subject snapshots under both baselines when feasible. Decompose movement into product improvement, new evidence, new scope, evaluator correction, and policy change. Historical scores remain historical.

This avoids both an immovable wrong rubric and moving goalposts. New urgent failures can stop the affected release immediately; versioning is not an excuse to ignore them. Not every change needs the same ceremony: proportionality follows impact and reversibility.

End the recursive “who grades the grader?” question at a declared bootstrap trust boundary, not an invented guarantee. The boundary consists of actual host/organization permissions, sponsor-reserved constraints, a small set of versioned protocol invariants, trusted execution/recording mechanisms, and external observations. These elements remain fallible and periodically tested. The assurance claim is conditional on them.

Self-amendment has higher-risk permissions than ordinary repair. A policy-authoring agent cannot grant itself credentials or powers the platform has not supplied. Within legitimate delegation, agents can adjudicate routine changes without human review. Low confidence is not automatically a reason to ask a human: first obtain evidence or perform the smallest reversible experiment.

## 23. Restartable sessions and retained search progress

A fresh worker should reconstruct the current state from durable records, not from the former worker's memory or an optimistic narrative. A restart packet references:

- Mandate, intent, assignment epoch, allowed actions, remaining budget, and exact work claim.
- Current subject/BOM and report/evaluator revisions, evidence validity, dirty/unmerged branches, and lease state.
- Last accepted baseline plus useful candidate branches, including unexplained disagreements.
- Failure signatures, hypotheses already tried, exact reproductions, observed outcomes, and why a path was rejected.
- The next discriminating action, its acceptance/stop conditions, and unresolved dependencies.

Keep the packet compact; link to raw evidence and prior experiments rather than pasting an entire transcript. Summaries are navigation aids, not authoritative evidence. Revalidate environment-sensitive observations. A fresh context must not receive broader permissions or reset the cumulative resource cap.

A replay reproduces the same conditions for diagnosis. A restart changes session context. A reseed changes method, model, tool path, test corpus, or decomposition. A replan changes the proposed search strategy. A contract revision changes the target through the E+1 path. Record which occurred; they are not interchangeable retries.

Classify stalls before acting:

| Evidence pattern | Candidate diagnosis | Next useful action |
|---|---|---|
| Same failure and effectively same patch repeatedly | Strategy loop | Preserve failed hypothesis, change approach or reseed |
| Tests fail before reaching product behavior | Environment/runner fault | Repair or replace that instrument/environment |
| Good witness is rejected or no-op passes | Oracle defect | Qualify a corrected evaluator in a new baseline |
| Satisfying one requirement necessarily breaks another | Contract contradiction | Produce counterexample and revise assignment |
| Individual repos pass but integrated outcome fails | Boundary/integration defect | Grade a pinned cross-repo consumer journey |
| Stable engineering passes but no beneficiary evidence | Intent/value uncertainty | Consumer experiment or mission review |
| State or raw results do not match the report | Evidence integrity fault | Quarantine verdicts and reconstruct from verified sources |

Thresholds such as repeated-attempt counts, resource limits, or cooldowns are versioned local policy settings, not universal numbers. Preserve meaningful learning even when no repair succeeds. Do not reward random churn as exploration.

## 24. What convergence means—and what it does not

For a fixed success definition, let p_k be the probability of a genuinely acceptable result on attempt k conditional on all earlier attempts failing. Then:

`P(no success through n attempts) = product(k=1..n, 1 - p_k)`

If every conditional p_k is bounded below by an epsilon greater than zero, the failure probability is at most `(1-epsilon)^n`. This conditional form does not assume that trials are independent. It DOES assume that a meaningful success remains possible and that the stated lower bound holds. In practice neither a fresh prompt nor a larger worker count establishes such a bound.

This is not an eventual-success guarantee. Wrong objectives, correlated assumptions, inaccessible resources, a defective oracle, regressions, and changing assignments can invalidate the practical inference. Repeated passes also have different meaning for producing one reusable deterministic artifact than for deploying a stochastic agent that must succeed reliably on every request. Agent-evaluation practice distinguishes success within several attempts from repeatability across attempts. [R3]

The useful design target is retained verified progress and evidence-driven search. Preserve accepted results, counterexamples, rollback points, and cheap discriminating tests. Keep attempts bounded and re-open accepted claims when new evidence invalidates them. An append-only history is monotonic as history; our beliefs and product quality need not be.

Track three independent clocks:

- Construction: actual elapsed time to a qualified slice and through its dependency path.
- Assurance: delay until evidence is current and uncertainty about required behavior is resolved.
- Outcome learning: delay until the intended consumer benefit is supported or refuted.

Track net gate closure within a fixed epoch, reopen rate, repeated failure fingerprints, time since last accepted result or material learning, verification cost, evaluator disagreement, and blocked critical-path dependencies. Do not estimate “87% of the way to finished” from checklist length or compare unlike epochs without a bridge. A growing backlog may reflect useful discovery rather than regression.

To test the convergence hypothesis, compare equal-budget bounded tasks under a fixed qualified baseline using continued sessions, fresh-session restarts, and varied strategies. Preserve the exact harness/model/environment and track time-to-valid-outcome, total resource cost, reopen/false-pass rates, and censored unsolved tasks. Use real consumer or holdout evaluation where feasible. Do not select only successful runs.

## 25. File-first operation, canonical state, and eventual adapters

Canonical means the designated accepted record/projection with provenance and correction rules; it does not mean every recorded claim is true. The event history contains proposals, contradictory observations, and rejected attempts as well as accepted decisions. A backlog is a decision projection, not a collection of every idea agents ever generated.

The protocol may initially operate with existing audit folders, one assignment capsule, per-attempt records, and a current checkpoint. The files in this package are portable templates, not a required new folder hierarchy or service.

A suggested logical layout, to be mapped to existing owner-held paths:

```text
.audit/
  context-and-assignment.yaml
  catalog.lock.json
  attempts/<attempt-id>/{manifest,results,findings,decisions}.json
  evidence/<content-addressed or authorized references>
  checkpoint.md
  outbox/<registration-id>.json
```

Run existing shell commands, linters, compilers, test runners, browser/native tools, and semantic review sessions. Store source/command/outcome evidence and qualify any new adapter before relying on it. Do not prescribe a new orchestration framework, central service, Docker installation, or bespoke dashboard as a prerequisite.

The registry outbox records intended destination, payload digest, idempotency key, authorization, and delivery state. Local acceptance is not global registration. A missing registry adapter blocks that projection; a missing deployment right blocks that action. Neither automatically blocks unrelated authorized work.

Map logical work packages and events into AgilePlus/Tracera when their actual interfaces are available and qualified. They must be able to consume the same records without making the fallback a second source of truth. The tool implementation repositories do not become owners of unrelated live portfolio records.

New infrastructure work must name an observed blocker, the minimum capability required, its consumer, a bounded implementation budget, and how we continue without it. Documentation breadth and a new framework are not default prerequisites to the first useful loop.

## 26. Economics and risk-proportional assurance

Measure worker cost together with tool/runtime cost, environment setup, verification, integration, recovery, and rework. Measure accepted outcome value and validated learning separately; never divide by rubric points as though all points had equal value.

Track elapsed time as well as agent/resource cost: parallelism can reduce latency while increasing total cost or collision risk. Use low-cost screening on broad scopes, then deeper verification on high-impact changes and uncertain claims. The availability of cheap workers justifies testing more assurance, not unlimited overhead.

Assurance effort should scale with consequence, reversibility, exposure, uncertainty, and the instrument's ability to detect a meaningful failure. Preserve existing non-negotiable floors where accepted. Do not manufacture a regulatory compliance or certification claim from adopting assurance techniques.

Objective-evidence and traceability practices from high-assurance engineering are useful models; NASA guidance explicitly connects requirements, observations, review artifacts, and traceability. [R2] Our proposed adaptation replaces role-specific manual handling with agent-compatible records and instrumentation where adequate. Its economic advantage remains to be measured in this lab.

## 27. Bootstrap acceptance and operational handoff

Start by reconstructing an assignment for one bounded outcome in an existing repo, including agent-derived intent if necessary. Use existing tools and preserved source evidence; do not wait for the historical catalog census or live central products.

The first vertical-slice acceptance requires:

1. The assignment was derived under real authority, with hypotheses and alternatives visible.
2. The grader accepts a valid witness and rejects a meaningful planted false pass, or explicitly limits claims where such a witness is not yet available.
3. The current product state is measured at a pinned snapshot and all missing evidence remains visible.
4. A bounded repair or useful discriminating experiment is performed when authorized.
5. A separate verification path judges the actual effect without mutable builder-controlled acceptance evidence.
6. A fresh session reconstructs the current state and continues without rediscovering the previous attempt's important failures.
7. Subject/report/registry identities are honest; absent integrations leave an outbox item rather than a fake receipt or a lab-wide block.
8. Product, assignment, evaluator, scope, and policy deltas remain distinct.

Subsequent expansion can cover the full catalog and stronger automation. Completion of these documents is not completion of the loop. The companion `START-HERE-AGENT.md` is the immediate session handoff; `bootstrap-assignment.template.yaml` is a data-entry template, not an accepted assignment or executable validator.

## Sources

Internal source snapshots:

- [I1] Benchora `scripts/scorecard_ci.py` at `8520ca49db1d4da3e42fea2a11c243aff9112eb4`; inspected via connected GitHub. Source URI: `https://github.com/KooshaPari/Benchora/blob/8520ca49db1d4da3e42fea2a11c243aff9112eb4/scripts/scorecard_ci.py`.
- [I2] Tracera `audit/SCORECARD-FULL-2026-08-30.md` at `1f5122d6add50a16d55705378d2743223981c58d`, first 200 source lines returned with tool truncation after the relevant opening sections; no whole-file completeness claim. Source URI: `https://github.com/KooshaPari/Tracera/blob/1f5122d6add50a16d55705378d2743223981c58d/audit/SCORECARD-FULL-2026-08-30.md`.
- [I3] Saved Library `DELIVERY-CONTRACT.md`, version 1, retrieved in full via Files on 2026-09-10; an existing saved contract, not independently established as every repository’s current accepted policy.
- [I4] Saved `AGSLAG_Venture_OS_Deck.pptx`, retrieved excerpts describing proposed domain authority; treated as architectural context, not proof of deployed capabilities or an enacted migration.

External primary sources, retrieved 2026-09-10. Referenced ideas are paraphrased; full standard catalogs have not been reproduced or imported in this proposal:

- [E1] Factory, Agent Readiness overview: `https://docs.factory.ai/agent-readiness/overview`.
- [E2] Factory, Agent Readiness product page: `https://factory.ai/product/agent-readiness`.
- [E3] Factory, Introducing Agent Readiness: `https://factory.ai/news/agent-readiness`.
- [E4] ISO, ISO/IEC 25010:2023 public overview: `https://www.iso.org/standard/78176.html`.
- [E5] CMU SEI, Architecture Tradeoff Analysis Method collection: `https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-collection/`.
- [E6] CMU SEI, SEI Architecture Analysis Techniques and When to Use Them: `https://sei.cmu.edu/library/sei-architecture-analysis-techniques-and-when-to-use-them/`.
- [E7] OWASP ASVS project: `https://owasp.org/www-project-application-security-verification-standard/`.
- [E8] OWASP SAMM model: `https://owaspsamm.org/model/`.
- [E9] OpenSSF Scorecard: `https://openssf.org/projects/scorecard/`.
- [E10] OpenSSF OSPS Baseline version index: `https://baseline.openssf.org/` (retrieved current version v2026.08.28).
- [E11] W3C WAI, Evaluating Web Accessibility Overview: `https://www.w3.org/WAI/test-evaluate/`.
- [E12] W3C WAI, Evaluation Standards Overview — ACT & EARL: `https://www.w3.org/WAI/standards-guidelines/evaluation/`.
- [E13] DORA, software delivery performance metrics: `https://dora.dev/guides/dora-metrics/`.
- [E14] Google Research, Measuring the User Experience on a Large Scale: `https://research.google/pubs/measuring-the-user-experience-on-a-large-scale-user-centered-metrics-for-web-applications/`.
- [E15] SLSA v1.2 provenance overview: `https://slsa.dev/spec/v1.2/provenance`.

New primary sources consulted for v0.2 on 2026-09-10:

- [R1] NASA, IV&V Overview, https://www.nasa.gov/ivv-overview/ . Used for the distinction between verification/validation and the dimensions of independence; this protocol does not claim NASA IV&V status.
- [R2] NASA, Identifying Objective Evidence Improves Requirement Implementation (2026-03-25), https://sma.nasa.gov/news/articles/newsitem/2026/03/25/identifying-objective-evidence-improves-requirement-implementation . Used for objective-evidence and traceability principles; not a claim that this lab meets NASA requirements.
- [R3] Anthropic, Demystifying evals for AI agents (2026-01-09), https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents . Used for outcome versus transcript, grader/environment limitations, and attempt success versus repeatability. No published model performance is used as a forecast for this lab.
- [R4] Manuel Rigger and Zhendong Su, Intramorphic Testing: A New Approach to the Test Oracle Problem (2022), https://arxiv.org/abs/2210.11228 . Used for test-oracle terminology and the existence of differential/metamorphic approaches; their validity remains assumption-dependent.
- [R5] Google DeepMind, Specification gaming: the flip side of AI ingenuity (2020-04-21), https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ . Relevant to separation of passing a proxy from satisfying an intended outcome. It is not evidence that any particular local agent has gamed a score.

The operating design, record fields, epochs, restart policy, and proposed experiment are recommendations in this revision, not externally validated results. The user's current description is the source for the intended autonomous-lab operating model and reported stalls; no live stall diagnosis was performed here.
