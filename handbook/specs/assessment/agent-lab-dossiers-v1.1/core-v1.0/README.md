# Agent Lab Evaluation System — v1.0 final handoff

**One portable operating kit for agent-originated intent, repository/product inventory, assignment construction, grader qualification, evidence-backed scorecards, gap discovery, improvement, and lifecycle decisions.**

Start with [START-HERE-AGENT.md](START-HERE-AGENT.md). Agents can perform every ordinary role under a real standing mandate. The kit does not grant permissions and does not require a human-written assignment, AgilePlus, Tracera, a central registry, or a new management platform.

## What is in this release

| Component | Delivered scope |
|---|---|
| Operating specification | Consolidated v1 protocol plus focused procedures, design decisions, threat model and completion matrix. |
| Candidate catalog | **1,080 original candidate criteria, 108 pillars, 18 domains**, in structured JSON and readable domain guides. |
| Product selection | **14 profiles** for agent, CLI, library, UI, service, infrastructure, games/mods, data/ML, polyrepo and other scopes. |
| Record contracts | **25 JSON Schemas**, templates, worked example records, and source/assessment/report/registry identity rules. |
| Agent handoff | Master prompt, **12 role prompts**, **8 operational runbooks**, report and restart templates. |
| Adoption | **36 bounded proposed work items**, owner boundaries, adapter contract, no-platform migration path. |
| Executable support | Offline Python reference kernel for structure, binding/digest consistency, scoring and non-compensating gates; metadata-only inspection and initializer. |
| Demonstration | Executed synthetic restoration example: successful-looking no-op rejected; corrected behavior passes qualified checks. |
| Release evidence | Test report, source register, provenance, retained v0.1/v0.2 originals and per-file SHA-256 manifest. |

**Candidate does not mean qualified.** The 1,080 entries are authored procedures, not the recovered historical catalog, a proof of semantic uniqueness, or 1,080 executable adapters. Product-specific measurement bindings, independent qualification and actual evidence are required. The reference kernel checks selected records; it cannot authenticate facts simply because they appear in JSON.

## Run the package checks

Use an installed Python 3.10+ interpreter; see the [validation report](qualification/VALIDATION-REPORT.md) for the version/platform actually tested. There are no third-party runtime dependencies. Execute from this extracted directory:

```sh
python tools/pep.py check-package
python tools/pep.py self-test
python tools/pep.py catalog
python tools/pep.py summarize examples/executed-toy-loop/before
python tools/pep.py summarize examples/executed-toy-loop/after
```

The first example has a FAIL gate and the second a PASS gate. The summary command can exit zero for either: zero means valid analysis, not product acceptance. The examples are explicitly synthetic, not grades of your repositories.

To rerun the trusted bundled toy in a **new** directory:

```sh
python tools/demo_loop.py --out .local-runs/toy-01
```

To create unaccepted starting records for a real authorized subject:

```sh
python tools/pep.py init-assessment --out .local-runs/project-01 --profile cli --subject-label YOUR_PROJECT
```

This initializer makes a deliberately small 12-entry skeleton. It does not decide the product's full applicability or pass any gates. Resolve the actual subject, mandate, intent, scope, measurements and evidence before operational acceptance. Use the catalog/profile as discovery aids; do not bulk activate all entries.

## Read by purpose

| Need | Entry point |
|---|---|
| Give this to Codex or Forgecode now | [Master session prompt](START-HERE-AGENT.md) |
| Understand the full model | [Integrated specification](docs/00-SPECIFICATION.md) |
| Construct agent-derived assignments and graders | [Assignment qualification](docs/05-ASSIGNMENT-QUALIFICATION.md) |
| Execute the assessment/improvement loop | [Execution SOP](docs/06-EXECUTION-SOP.md) |
| Handle semantic judgments and contrary hypotheses | [Semantic review](docs/07-SEMANTIC-REVIEW.md) |
| Explain maturity, uncertainty and scores | [Scoring and maturity](docs/08-SCORING-AND-MATURITY.md) |
| Resume and diagnose thrashing | [Restarts and economics](docs/09-RESTARTS-CONVERGENCE-AND-ECONOMICS.md) |
| Recover previous scorecards | [Census runbook](runbooks/02-RECOVER-HISTORY.md) |
| See schema/template usage | [Schema index](schemas/README.md), [templates](templates/README.md) |
| Browse the 1,080 predicates | [Catalog](catalog/README.md) |
| Integrate later without duplicate authority | [Integration contract](integration/README.md) |
| Know what was actually tested | [Qualification report](qualification/VALIDATION-REPORT.md) |
| See explicit non-claims | [Completion matrix](docs/22-LIMITATIONS-AND-COMPLETION-MATRIX.md) |

## Operating invariants

The lab has three loops: mission/portfolio, assignment/measurement, and execution. A solution passing an assignment does not prove the assignment represents a useful goal. Agents may revise the goal or evaluator, but must record a new baseline rather than rewrite the old result.

Keep authority, evidence, commitment and authorship separate. Keep applicability, execution, verdict, freshness and review separate. Keep inventory, requirements, hypotheses, findings and accepted work separate. Keep a successful pipeline distinct from a functioning product, delivered release and observed beneficiary value.

Use a fixed epoch for acceptance. Preserve counterexamples and failed hypotheses across replacement sessions. A missing registry blocks registration, not unrelated local work. A missing credential blocks the dependent action; do not invent authority or fake receipts.

Do not create a new repository just to adopt this kit. Map logical records to the accepted existing owner. PhenoDocs and AgilePlus remain tools, not dumping grounds for live portfolio truth.

## Release meaning and integrity

“Final” means the consolidated handoff for this request, not a claim that the user's portfolio has been audited or that this kit is a deployed autonomous lab. Local validation checks its reference kernel, schemas and synthetic demonstration. It does not establish regulatory certification, real-product quality, cross-platform assurance or external API integration.

`MANIFEST.json` covers every distributed file except itself. The ZIP's companion hash and manifest detect alteration relative to supplied bytes; neither is an authenticated signature. Do not rely on them against an adversary who can replace both. Prior versions are preserved under [provenance/history](provenance/README.md) for lineage, not as additional live authorities.
