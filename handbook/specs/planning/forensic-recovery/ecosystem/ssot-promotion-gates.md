# Proposed recovered-SSOT structure and promotion gates

This structure is a **proposal for adjudication**, not a recovered truth claim.

## Canonical layers

1. `docs/intent/` — verbatim user/operator intent, source date, source channel, and a separately marked synthesis.
2. `docs/product/` — user-visible capabilities, exclusions, journeys, acceptance criteria, and compatibility promises.
3. `docs/architecture/` — system context, repository boundaries, runtime topology, interfaces, data contracts, and threat model.
4. `docs/decisions/` — ADRs with evidence links, alternatives, reversibility, and supersession state.
5. `docs/specs/` — normative behavior with requirement identifiers and bidirectional implementation/test traceability.
6. `docs/work/` — WBS, dependency DAG, milestones, ownership, status, blockers, and evidence of completion.
7. `docs/verification/` — test catalog, build matrix, reproducible commands, fixtures, expected artifacts, and latest verified results.
8. `docs/forensics/` — immutable acquisition manifest, branch/commit ledgers, contradictions, restore candidates, and rejected hypotheses.

## Promotion rule

No statement becomes canonical merely by being placed under `docs/`. Promotion requires:

- provenance to an intent source or accepted engineering decision;
- consistency with current repository boundaries and public contracts;
- an implementation pointer or an explicit `planned` status;
- a verification method and result state;
- contradiction search across all reachable refs and scoped repositories;
- rejection or recording of plausible alternatives;
- reviewer identity and decision timestamp.

## Recovery-state labels

Use exactly one of: `observed`, `inferred`, `claimed`, `contradicted`, `candidate`, `accepted`, `rejected`, `superseded`, `unverified`, `verified`.

## Non-negotiable distinction

- **Historical truth:** what existed at a commit/ref.
- **Behavioral truth:** what reproducibly works.
- **Intent truth:** what was actually requested or accepted.
- **Canonical target:** the state selected after reconciling the first three.

Collapsing these into one category is the primary way an agent-managed repository manufactures a false SSOT.
