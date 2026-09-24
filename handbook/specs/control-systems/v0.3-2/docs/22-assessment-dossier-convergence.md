# Assessment dossier convergence

## Resolution of the "inventory versus scorecard" question

Use **one logical Assessment Dossier with two operational phases**, not two canonical systems. This matches the already-developed Master Assessment Kit contract. S053, S054.

### Phase A — inventory / applicability / evidence map

Populate subject identity, component BOM, beneficiary/scope, claims, observed artifacts, requirements, assumptions, missing obligations, evidence references and applicability. Measurement/verdict/score fields remain `unknown` or null.

The purpose is to answer **what exists, what is claimed, what applies and what can actually be measured?**

### Phase B — evaluation / score / decision

Bind selected criteria to qualified instruments, execute them, record raw observations, verdicts, freshness, reviewer state, findings and decisions. Only now calculate scoped metrics.

The purpose is to answer **what did the qualified evidence establish for this exact scope?**

## Why a single dossier is better

A separate inventory truth store plus scorecard truth store creates subject-identity drift, duplicated evidence, stale applicability and "100%" scores over different denominators. The dossier already separates these concepts internally, so the UI can present two stages without splitting authority.

## How to absorb existing scorecards

Do not throw away the 88-pillar/large rubric work. Convert it into:

- versioned **criterion catalogs**;
- **profiles** that select obligations for product/repository/slice types;
- **measurement bindings** defining the real instrument/fixture/threshold/freshness rule;
- generated human and machine views.

A linter pass, a document's existence, an exercised behavior and proven consumer value remain distinct predicates. Unselected is unassessed, not automatically N/A. A waiver does not become a pass. S053.

## Recommended canonical row lifecycle

```text
criterion instance
  -> applicability: applicable | not_applicable | unresolved
  -> evidence/instrument qualification
  -> execution: not_run | blocked | executed | stale
  -> verdict: pass | fail | unknown | contested | waived
  -> review disposition
  -> finding/decision linkage
  -> generated score/view
```

This directly supports the user's desired workflow: during inventory the score column is effectively empty; later evaluation fills it without copying the row into another authority.
