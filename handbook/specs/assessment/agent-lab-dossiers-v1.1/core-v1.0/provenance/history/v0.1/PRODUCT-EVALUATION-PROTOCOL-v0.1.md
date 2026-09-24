# Product Evaluation Protocol — preliminary v0.1

Status: PROPOSED DESIGN, not an accepted authority migration, production evaluator, or recovered canonical catalog.
Prepared: 2026-09-10.
Scope: repository and whole-product inventory, assessment, gap discovery, maturity, and bounded autonomous lifecycle decisions.

## 1. Decision

Build one evidence-backed evaluation protocol with distinct objects and generated views. Do not merge inventory facts, verification results, maturity decisions, and investment decisions into a single spreadsheet score. The scorecard is an output, not the underlying state store.

The intended loop is:

`inventory -> accepted context -> obligations and hypotheses -> evidence collection -> evaluation -> gaps and experiments -> policy decision -> governed work -> independent re-evaluation`

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

Shared schemas belong in the verified shared-contract owner; do not create a new repository merely to hold this protocol. The temporary implementation may be a CLI/skill and files with small adapters. A database or graph service is optional, not required for v0.

## 3. Canonical objects

Use distinct versioned records with stable identifiers.

**Subject snapshot.** Identifies the repository, component, package, product, release, deployment, or user journey being evaluated. Includes source revisions, tree/dirty-worktree digests when applicable, artifact digests, runtime/configuration fingerprints, platform, evaluation period, and relevant cross-repository dependencies.

**Inventory item.** Records what exists, where it exists, what it declares, and how its presence was observed. A declaration, an inferred capability, an accepted requirement, and an observed behavior are different kinds of facts.

**Criterion definition.** Specifies the outcome to evaluate, applicability, measurement method, evidence requirements, anchors or thresholds, invalidators, negative controls, and provenance. A criterion is not an instance of a test on one platform.

**Evaluation result.** Records a criterion instance against a subject snapshot, its execution state, verdict, observation, evidence, freshness, and verifier identity. Results are append-only; correction produces a superseding record.

**Finding.** Captures an implementation failure, verification gap, contradictory claim, missing requirement, unexpected implemented behavior, research gap, opportunity, obsolete feature, or measurement defect. A finding is not automatically approved work.

**Decision.** Records accepted, rejected, deferred, or conditional dispositions, authority, rationale, alternatives, budget, stop conditions, and links to evidence and work packages.

**Assessment.** A manifest joining the exact subject set, catalog version, profile, results, findings, coverage statement, and derived reports. The scorecard, inventory, backlog, maturity view, and lifecycle recommendation are projections of this manifest.

Required relation types include `declares`, `requires`, `implements`, `exercises`, `verifies`, `contradicts`, `depends_on`, `supersedes`, `invalidates`, `motivates`, and `authorized_by`. Sharing a link or file path alone does not establish one of these semantic relationships.

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
- `plan`: propose requirements, experiments and AgilePlus work packages.
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

**Recover.** Ingest current agents’ template census and source lineage. Deliver an ambiguity/contradiction register, not a prematurely declared canonical rubric.

**Define the kernel.** Implement schemas, subject identity, outcome states, evidence references, catalog/profile locks, scoring/gate reducers, and source crosswalks. The kernel must distinguish missing evidence from failure and reject internally inconsistent reports.

**Qualify a vertical slice.** Choose a deliberately diverse few subjects: a library/CLI, a UI product, and an integrated service or agent system. Prove inventory -> executable checks -> semantic review where needed -> findings -> AgilePlus work -> independent recheck -> registry reference.

**Expand the catalog.** Import and deduplicate the 1,000+ candidate predicates if recovery and external mappings support them. Activate each with applicability, source provenance, an adequate instrument or explicit measurement gap, and negative controls. Do not pad the count.

**Enable bounded remediation.** Use standing authority, isolated work, evidence invalidation, and independently verified acceptance. Keep assessment delta separate from product delta and policy delta.

**Enable strategic autonomy.** Only after real outcome measurement, mandate enforcement, consumer/custody analysis and stop rules are qualified should agents autonomously allocate, pivot, or retire under preauthorized rules.

The v0 acceptance test is not “a large catalog exists.” It is: one real failing outcome is detected without a human interpreting undocumented context; it becomes a correctly owned, bounded action; a repair or experiment runs within authority; an independent verifier demonstrates the result; the subject and registry records reconcile; a planted false pass is rejected; and no unrelated maturity claim is promoted.

## 18. Generic agent contract

> Evaluate the named subject at an exact snapshot using the locked applicable catalog and accepted product context. Inventory declarations separately from observations. Execute qualified deterministic checks first, then required behavioral checks, then anchored semantic review and outcome-evidence assessment. Do not interpret missing evidence as proof of failure or absence, and do not treat artifact presence as proof of behavior. Preserve unknown, blocked, disputed, stale, and out-of-scope states. Discover implied obligations and opportunities, but do not turn speculative features into accepted requirements. Produce traceable findings, slice-specific maturity, coverage and uncertainty, and bounded next actions with credible alternatives. Emit owner-held records and authorized registry references. Do not mutate the product or lifecycle unless the separate mandate permits that mode and action.

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
