# Portfolio end-to-end planning audit

**Observation date:** 2026-09-07 Pacific / 2026-09-08 UTC

Integration qualification: current explicit sponsor instructions take precedence over every package below. The separate `portfolio-slice-audit-2026-09-05` contains a 78-row observation slice (43 ZZ and 35 NON-ZZ). It must not be equated by count alone with the rationalization package's 63+15 scenario. Both require an identity crosswalk. CURRENT in the table means a retained planning reference, not a freshly revalidated hosted or accepted product state.

**Scope:** read-only crosswalk of `phenotype-portfolio-control`,
`kooshapari_portfolio_rationalization`, `portfolio-reconciliation`, and
`chat2-portfolio-audit-20260904`. This audit records planning authority and
traceability gaps. It does not authorize repository mutation, build execution,
remote changes, migration, archive, retirement, or release work.

## Current authority and historical sources

| Precedence | Source | Status | Authority in this audit |
|---:|---|---|---|
| 1 | `portfolio-reconciliation/prompts/MASTER-HANDOFF.md` and `prompts/EXECUTION-ADDENDUM.md` | CURRENT planning control | Treat imported packages as immutable historical proposals; preserve aliases; require live/receipt-based validation before relying on a proposal. Its addendum supersedes conflicting source-prompt instructions. |
| 2 | `chat2-portfolio-audit-20260904/doctrine.md`, `implementation-plan.md`, `plan.json`, and `repository-backlog.md` | CURRENT for the explicitly authorized 33-repository chat2 slice | Defines read-only sequencing, component work packages, authorization classes, and the rule that execution follows the decision/approval gates. It does not establish portfolio-wide authority. |
| 3 | `portfolio-reconciliation/data/reconciled-repositories.json`, `data/decisions.json`, `data/work-queue.json`, and `review/*` | CURRENT reconciled planning projection | Supplies validated import mapping and proposed decision/work records; it is not live host truth or accepted migration authority. |
| 4 | `phenotype-portfolio-control/10-ECOSYSTEM-SSOT-AUTHORITY.md`, `06-CLOSURE-FIRST-WBS.md`, and `12-INITIAL-WBS-PERT-DAG.md` | HISTORICAL policy and initial WBS | Useful control-spine and closure-first model. Its 146 snapshot and initial task statuses must be refreshed before operational use. |
| 5 | `kooshapari_portfolio_rationalization/kooshapari-portfolio-rationalization-master-plan.md` and disposition registers | HISTORICAL candidate-disposition package | Preserves 146 candidate dispositions, 108 E1/38 E0 labels, and a 63/15/13/55 scenario. It is not an accepted topology or current observation. |

Field-level rule: live repository facts require a current observation service;
curated roles require an accepted decision; product-local intent/specification
remains product-local with AgilePlus lifecycle linkage; cross-product contracts
need their separately adjudicated home. A projection is not a competing source
of truth.

## Count reconciliation: do not add unlike sets

| Count | Meaning | State | Join needed before any combined metric |
|---:|---|---|---|
| 146 | Imported repository snapshot, with preserved `REP-*` aliases | HISTORICAL import fact, not live count | Join by immutable host ID plus preserved `REP-*`; detect rename, transfer, access, and local-only divergence. |
| 33 | Exactly the named chat2 dossier/backlog scope | CURRENT scoped audit coverage, not a disposition denominator | Map each chat2 repository name to one `REP-*`, reconciliation row, rationalization disposition, and current host identity. |
| 78 | Candidate managed-plus-held eligibility view (`63` managed plus `15` held/incubating) | HISTORICAL scenario, not WIP, canonical-product, or validated-active count | Join all 146 imported rows to accepted lifecycle decisions; keep reference/historical/archived classes separate. |

`146 + 33 + 78` is invalid arithmetic: these are an imported universe, a
scoped evidence subset, and a proposed operating scenario. The only valid
comparison is after an identity join with observation dates and authority state.

## Existing WBS and decision namespaces

| Namespace | Existing IDs | Current use | Crosswalk status |
|---|---|---|---|
| Portfolio-control initial WBS | `T-000` through `T-720` | Historical control-spine, family-adjudication, consolidation, projection, and validation sequence | No demonstrated mapping to reconciliation work records or chat2 repository rows. |
| Chat2 audit WBS | `WP-01` through `WP-12` | Current read-only dossier-to-decision-to-approval sequence | Reused by dossier component tasks, but no machine join to `T-*` or `REC-DEC-*`. |
| Reconciliation decisions | `REC-DEC-001` through `REC-DEC-020` | Candidate authority, topology, boundary, fork, and lifecycle questions | Present in decisions/work queue; individual acceptance, owner, and source-receipt linkage are incomplete. |
| Repository/component tasks | e.g. `REG-01`, `PORTAGE-01`, `VCS-01`, `THEGENT-01` | Scoped evidence/characterization tasks in chat2 backlog | Names are local planning identifiers; no portfolio-level stable identity table links them to `REP-*`, decisions, or closure evidence. |

## Decisive planning decisions already represented

1. Preserve the imported 146-row universe and its aliases; do not force a live
   account to reproduce the historical count.
2. Treat the 63/15/13/55 and 78 figures as candidate lifecycle scenarios, not
   goals or concurrent assignments.
3. Separate live Git facts, curated registry identity, product-local
   specifications, cross-product contracts, lifecycle state, trace evidence,
   and strategy allocation by field authority.
4. Use closure slices and bounded family waves rather than cosmetic work across
   the imported universe.
5. Keep forks, references, historical repositories, and archive candidates as
   distinct classes; preservation, parity, consumer migration, and sponsor
   approval precede terminal actions.
6. In the chat2 slice, remain read-only through WP-01 to WP-07; WP-08 is an
   isolated pilot gate, WP-09 is approval review, and WP-10 to WP-12 are not
   authorized execution/terminal lifecycle work.

## Exact missing traceability

| Gap ID | Missing relationship | Why it blocks closure-oriented planning | Required evidence/record |
|---|---|---|---|
| TR-01 | `REP-*` alias -> immutable host ID -> current name -> rationalization row -> reconciliation row -> chat2 row | Cannot tell whether 33 is covered by, overlaps with, or contradicts 146/78 | Versioned identity crosswalk with source hashes, observation time, aliases, rename/transfer status, and unmatched rows. |
| TR-02 | `REC-DEC-*` -> affected `REP-*`/capabilities -> acceptance owner -> decision state | A decision register title is not an accepted authority boundary | Per-decision evidence receipts, explicit alternatives, chosen state, approver, and supersession link. |
| TR-03 | `T-*` -> `WP-*` -> repository/component task -> evidence gate | Existing WBS systems cannot safely be scheduled together | Machine dependency map with one canonical program-WBS ID and typed external-ID references. |
| TR-04 | Candidate lifecycle/disposition -> preservation/provenance -> consumer/package/URL migration -> terminal action | Retirement counts cannot become closure claims | Per-repository closure record with source/target parity, consumer migration, rollback, package/URL handling, and sponsor approval. |
| TR-05 | E0/E1/root-document assertion -> source revision/receipt -> reproducibility tier | Imported confidence is not current evidence | Claim ledger identifying source file/ref, inspection date, reviewer, falsifier, and evidence tier. |
| TR-06 | Chat2 component task -> exact checkout/files -> test/negative oracle -> approval class | The 33 dossiers are static and cannot authorize broad implementation | Scoped execution card naming exact files, characterization tests, preservation rule, and independent verification. |
| TR-07 | Live count -> inaccessible/local-only/org/collaborator scope -> snapshot variance | Any aggregate target can drift silently | Observer output with access scope, additions/removals, archived/fork metadata, and comparison to the 146 import. |

## Closure-oriented forward WBS

The forward WBS below is authoritative only as a planning proposal. Every row
is `NOT_STARTED`; it is ordered to close uncertainty before any migration or
retirement action.

| ID | Closure-oriented work | Depends on | Exit evidence | State |
|---|---|---|---|---|
| FWP-01 | Freeze imported source identities and hashes | — | Immutable source manifest for all four docsets and import archives | NOT_STARTED |
| FWP-02 | Build the 146-to-current identity and scope crosswalk | FWP-01 | `REP-*`/host/name/disposition/reconciliation/chat2 mapping, with unmatched set | NOT_STARTED |
| FWP-03 | Reconcile the 33 scoped dossiers to the identity crosswalk | FWP-02 | Each chat2 row maps to one identity or an explicit ambiguity record | NOT_STARTED |
| FWP-04 | Establish field-level authority decisions for registry, spec, and enforcement | FWP-02 | Accepted `REC-DEC-*` outcomes with writer/reader/projection rules | NOT_STARTED |
| FWP-05 | Convert candidate dispositions to evidence-backed closure cards | FWP-02, FWP-04 | Per-repository preservation, consumer, provenance, and terminal-gate card | NOT_STARTED |
| FWP-06 | Close one zero-code authority contradiction or preserved fork decision | FWP-05 | One independently reviewed decision with no destructive action | NOT_STARTED |
| FWP-07 | Run one approved isolated characterization/pilot slice | FWP-03, FWP-05, FWP-06 | Retained run, negative oracle, source/config hashes, and failure record | NOT_STARTED |
| FWP-08 | Prepare a bounded change or migration proposal | FWP-07 | Exact source/target, parity, rollback, consumer, and approval plan | NOT_STARTED |
| FWP-09 | Independently verify the proposed closure and authorize or reject it | FWP-08 | Independent verification and explicit sponsor decision | NOT_STARTED |
| FWP-10 | Publish regenerated portfolio projections after accepted decisions only | FWP-09 | Projection with source versions, freshness warning, and count reconciliation | NOT_STARTED |

## Hard gates and prohibited claims

- Do not call 146 a current portfolio count without a live observer run.
- Do not call 78 an active workload, a canonical-product count, or a completed
  rationalization outcome.
- Do not infer a lifecycle decision from a README, archive flag, name, or
  historical confidence field.
- Do not merge, archive, delete, force-push, rewrite refs, publish, or change
  a remote from this audit or any imported planning text.
- Do not treat a static dossier, queue row, or source import as runtime,
  consumer, license, migration, release, or product-completion evidence.

## Immediate next gate

Start FWP-01 and FWP-02 as read-only evidence work. No count-based portfolio
claim, authority reassignment, or closure action should proceed until the
identity crosswalk supplies the missing joins.
