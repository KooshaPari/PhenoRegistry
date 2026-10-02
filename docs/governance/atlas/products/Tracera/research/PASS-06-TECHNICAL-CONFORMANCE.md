# Tracera: technical bootstrap and conformance, pass 06

**2026-09-29. Partial research; neither product nor specification is complete.**

This pass replaces broad candidate lists with inspected implementation seams, scoped evidence and an executable research example. It supplements, rather than overwrites, passes 1–5 and the later bootstrap/academic ledgers. Source keys resolve in [PASS-06-EVIDENCE.json](PASS-06-EVIDENCE.json). Statements marked proposed are architecture recommendations, not accepted product baselines.

## 1. Three lifetimes, not two disposable products

The latest user mandate and the archived June prompt [I6] require a persistent product state plus measurable worker feedback. A prior shorthand, “AgilePlus is ephemeral; Tracera is global,” is inadequate. The **attempt** is ephemeral; the development effort must survive it.

| Plane | Owns | Must survive |
|---|---|---|
| Worker attempt | Execution identity, model/tool configuration, sandbox/worktree, lease, messages, action/result provenance | Restart or replacement without losing durable progress |
| Development effort, AgilePlus | Change intent, specification revisions, work packages, prerequisites, review and grading history, execution receipts | Any individual agent, device checkout or chat |
| Product, Tracera | Accepted product meaning, configurations, releases, realized/observed state, trace relations, evidence interpretation | Any worker or development-management tool |

**Proposed rule:** require a stable development/change ID distinct from attempt ID and product-configuration ID. A human, agent, script or CI job can realize a change. None owns product identity by virtue of executing it. Failure, expiry or deletion of an attempt cannot erase accepted product state. External work completion supplies a fact, not an acceptance command.

A graph edit is a proposed product change. The resulting work request belongs to a durable development effort; the agent is replaceable. This preserves the original product-graph thesis without forcing Tracera to become an orchestration runtime.

## 2. Current code changes the bootstrap question

Inspection is pinned to Tracera `3c289c78a76b292826f019c233f2ce1f7200c197`. It is bounded, not a whole-repo audit.

### Existing renderer investment [I1]

The web manifest already declares React Flow, Sigma/Graphology, Cytoscape and ELK. Therefore “adopt React Flow” is not an implementation discovery. The unanswered questions are actual entry-point reachability, duplicated state, whether actions reach the canonical backend, accessibility, and retained component value.

**Proposed split:** React Flow is the first authoring candidate for bounded, richly interactive product slices; Sigma is the first broad network-exploration candidate; Graphology/ELK provide algorithms/layout as appropriate. Neither renderer's node array becomes accepted product truth. React Flow explicitly documents re-render and expansion costs; Sigma separates its WebGL rendering from Graphology's data/algorithm layer. [E7,E9,E10]

Do not add another renderer before replaying the same editing/navigation tasks through the installed options. Do not remove Cytoscape merely because another package appears preferable. Identify its actual consumers first. Core-library licensing and paid examples/support are separate review items; React Flow's core is MIT. [E8]

### Existing persistence boundary [I2]

`Store` already abstracts PostgreSQL and SQLite. `TraceLink` carries IDs, relationship, confidence, source and timestamps, but not explicit endpoint revisions, target configuration, accepted-versus-inferred authority or semantic-link validity. This is a **schema/contract problem first**, not proof that the storage engine is wrong.

**Proposed baseline:** retain the existing relational stores while specifying versioned relation assertions, snapshot/configuration identities and atomic acceptance operations. SQLite and PostgreSQL support recursive queries; that establishes feasibility, not performance superiority. [E11,E12]

Any later engine change must retain IDs and verify query, persistence, conflict, backup and migration behavior. Use one canonical write authority and rebuildable projections, not uncoordinated dual writes.

### Newly localized query risks [I3]

In the inspected `query_intents` helper, `ProductQuery.product_id` is not read. Unknown kind/status strings parse to `None`, removing that filter. The helper also uses a baseline lower bound rather than an exact baseline snapshot.

These are **static contract concerns**, not a demonstrated cross-tenant exploit. Callers may supply prefiltered input; that call-chain precondition has not been verified. The next implementation witness must use two products with overlapping local IDs, an exact baseline query, an invalid discriminator, and explicit expected rejection/isolation. A result-count limit is not proof that scan cost or traversal depth is bounded.

## 3. Reuse decisions and disqualifiers

| Concern | Proposed disposition | Why / what must falsify it |
|---|---|---|
| Canonical persistence | KEEP + qualify SQLite/PostgreSQL first | Existing boundary minimizes rewrite; compare against actual query and recovery workloads, not graph branding |
| Kuzu | Archived comparator, not maintained default | Upstream was archived October 10, 2025; extension distribution changed. [E1] |
| LadybugDB | Benchmark candidate, not adopted | Rust binding and embedded graph capabilities exist [E2]; a shared-file multiprocess deployment cannot ignore its one read-write Database object restriction. Multiple connections within that object are different. [E3] |
| RDF interchange | ADAPT Oxigraph toolkit if mappings justify it | RDF parsers/serializers are separable from the database; published development limits preclude unmeasured performance claims. [E13] |
| Code intelligence | INTEGRATE SCIP, syntax fallback via tree-sitter | SCIP has Rust and other language indexers/bindings; tree-sitter is syntax infrastructure, not a whole-program semantic authority. [E4,E6] |
| Build/test topology | ADAPT native build metadata, examine SPADE | The reviewed RIG extractor was automatic for CMake, not a ready-made automatic Cargo/npm solution. [P1] |
| Graph UI | QUALIFY existing authoring/exploration stack | Avoid duplicate rendering engines and preserve canonical IDs/selection across views [I1,E7,E9] |
| Provenance/shape checks | MAP PROV; consider SHACL at interchange boundary | Attribution/derivation and data-shape conformance are useful but neither proves real behavior. [E16,E17] |
| Grading protocol | BORROW feedback; strengthen evidence admission | Visible criterion-level feedback is useful. Imported display labels are not sufficient authority. [E14,E15] |

SCIP also changed organizational home: the old `sourcegraph/scip` repository resolves to `scip-code/scip`; the official announcement describes independent governance. Pin the actual repository identity/blob, not an assumed permanent URL. [E4,E5]

No BUY/ADOPT decision is finalized. Licensing, security policy, release cadence, transport behavior and supported-platform qualification remain required at the selected version. Stars and README performance adjectives are not acceptance evidence.

## 4. The oracle lesson worth importing — and the trap

Gradescope exposes criterion-level scores, feedback, visibility and metadata, and allows status presentation to differ from numerical points. [E14] This supports the user's visible-target feedback loop. It also shows why a generic imported “passed” display state cannot be the product verdict.

**Proposed Tracera/AgilePlus contract:** retain raw observed outcome, measurement value, rubric evaluation and display treatment separately. A grader can emit useful partial feedback while product acceptance remains blocked. “Best historical attempt” and “current candidate verified” must be different views.

The progress vector should be a function of a frozen measurement basis:

`basis = (product, configuration, contract revision, criterion revisions, candidate, evaluator, observation cut)`

Only compare like-for-like observations for engineering deltas. Contract, scope, evaluator or configuration changes open a new segment or require explicit recomputation. Never join incomparable grades into a smooth improving line.

A useful front end can show observed delta and uncertainty before there are enough points to estimate a slope. It must not invent asymptotic convergence from two samples. Regressions are negative movement, not deleted history. A scalar reward must not hide a failing safety-critical criterion behind unrelated polish.

Trust rules also require care. A hash identifies bytes, not who ran a check. An approved producer name in a payload is not authentication. Held-out checks supplement independent acceptance policy; they do not repair a grader the worker can overwrite.

## 5. What the research evidence actually warrants

Four papers were checked beyond title/abstract; [PASS-06-PAPER-APPRAISAL.md](PASS-06-PAPER-APPRAISAL.md) records their limits. The older matrix remains a lead list for unreviewed entries [I5].

The architecture conclusions are narrower than “graphs make agents better”: use evidence-backed build structure, measure whether context actually reaches needed files, independently qualify semantic links, and compare graph-guided feedback with strong nongraph baselines.

A trace edge is evidence of a relationship claim; it is not automatically evidence that a requirement was satisfied. For example, a compiler can confirm a source reference to a requirement ID, while the source still implements the behavior incorrectly. Probabilistic relationship recovery and deterministic behavioral evaluation are distinct subsystems.

## 6. Executed architecture experiment

[pass06/reference_oracle.py](pass06/reference_oracle.py) is a standard-library-only, synthetic reference model. It is not imported into Tracera or AgilePlus and does not generate their product tests.

The run checked identity-bound evidence, explicit non-green states, independent worker identity, persistence across restart, idempotent replay, conflicting replay, append-only protection and rollback. **30 checks passed; seven deliberately removed binding guards were detected.** Raw expected/actual results and environment identities are in [pass06/reference-results.json](pass06/reference-results.json).

This establishes that those proposed rules can be expressed coherently in one small executable example. It does not establish runtime compliance, cryptographic admission, concurrent writers, scalable graph traversal, safe evidence subsumption, or production-quality precedence among mixed observations. Those limits are part of the receipt, not footnotes to a product pass.

## 7. Concrete next experiments, not another unbounded research list

### A. Existing-runtime identity and query witness

Run the real Rust helpers and mounted API against two products with overlapping local identifiers. Test product filter enforcement, exact versus lower-bound baseline selection, invalid filter rejection, and scoped counts. Preserve the raw result before changing code. This closes or refines the static concerns above, not the whole product.

### B. Configuration-aware evidence reuse

Specify a limited applicability language first. Compare exact matching, explicit dependency-equivalence certificates and constrained implication/subsumption. An omitted dimension is unknown, not a wildcard. Include changed feature flags, OS, schema, dependency, criterion and verifier versions. Measure unnecessary rechecks as well as unsafe reuse.

### C. Relational versus embedded graph witness

Use identical canonical IDs and recorded datasets for neighborhood expansion, reverse impact, as-of reads, invalidation, writes during reads, restart and backup/restore. Publish load shape, dataset size, p50/p95/p99, RSS and correctness separately. Include packaging/migration effort. Do not run a benchmark until all candidates implement equivalent semantics.

### D. Existing UI ownership witness

Use one shared product slice with editing, collapse/expand, undo, keyboard navigation, accessible details, pending delta and rejected mutation. Compare reachable React Flow/Sigma/Cytoscape paths before introducing new state. Benchmark authoring latency and comprehension tasks separately from whole-network drawing throughput.

### E. Worker-neutral restart and feedback witness

One durable change is attempted by worker A, resumed by worker B and inspected by a human. Current product evidence persists, stale leases do not authorize new writes, and work completion without fresh acceptance remains non-green. Export results using the common evidence contract without transplanting AgilePlus's execution state machine into Tracera.

## 8. Gate accounting

Closed within this pass: source-linked technical shortlist refinement; four bounded paper appraisals; synthetic oracle experiment and mutation controls; current-code mapping for three inspected files.

Still open: whole-source coverage; consumer/route reachability; final stages and atomic requirements; cross-engine and UI benchmarks; evidence subsumption; competitor hands-on comparisons; complete academic replication; trusted verifier integration; independent semantic review; AgilePlus methodology teardown.

**No mature completion percentage, superiority claim, accepted schema or 100% specification claim is awarded.** The two-repository lock remains active. A third repository is not authorized by this report.
