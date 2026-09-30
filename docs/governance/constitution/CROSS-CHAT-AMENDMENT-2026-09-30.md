# Cross-Chat Amendment — Durable Memory, Portfolio Constitution, Git Ledger

**Date:** 2026-09-30  
**Purpose:** amend every active two-repository mature-first recovery program without restarting completed work.

## 1. Durable memory is now part of product quality

Repository + PhenoRegistry documentation is durable external memory for both the human owner and agents.

A repo is not specification/design complete if future recovery still depends on:
- replaying old chats;
- remembering hidden prerequisite reasoning;
- searching the whole repo blindly;
- asking the owner to restate prior decisions;
- rediscovering previously rejected approaches.

Human recoverability after months/years is a completion criterion.

## 2. Documentation uses progressive disclosure

Do not create one shallow `INTENT.md`, `SOTA.md`, `GENESIS.md`, etc. merely to satisfy a checklist.

Use:

```text
product dossier bulkhead
    ↓
domain bulkhead
    ↓
focused modules
    ↓
evidence / raw sources
```

A bulkhead is concise relative to its subtree but must still stand alone.

It should state:
- purpose;
- accepted conclusions;
- major uncertainty;
- key invariants;
- what changed;
- blockers;
- where deeper evidence lives.

Target:
- product bulkhead: 5–10 minute recovery;
- domain bulkhead: 5–15 minute domain recovery;
- deeper modules: research/implementation work.

## 3. Genesis is mandatory for long-lived products

Genesis should preserve:
- original pain/problem;
- earliest formulation;
- historical aliases;
- user-authored intent milestones;
- prerequisite reasoning;
- major conceptual pivots;
- surviving invariants;
- rejected framings;
- relationship to external influences;
- unresolved philosophical/product questions.

Do not rewrite origin history around competitors or frameworks discovered later.

## 4. Raw owner intent is primary product evidence

Important long-form owner messages/dumps are source artifacts.

For each high-value intent dump:
1. retain source/conversation provenance where possible;
2. make a faithful synthesis;
3. distinguish owner intent from assistant interpretation;
4. extract invariants;
5. extract unresolved questions;
6. identify affected architecture/specification/research;
7. record incorporation status.

The eventual system should answer:

> Which important things has the owner told us that are not yet incorporated into canonical product memory?

## 5. Documentation quality is graded

Suggested states:

```text
MISSING
STUB
PARTIAL
SUBSTANTIVE
RECOVERY_GRADE
VERIFIED_RECOVERY_GRADE
```

File existence is not completion.

A shallow placeholder can be worse than explicit absence because it produces false confidence.

Before 100%, run:
- fresh-agent recovery review;
- human-oriented fresh-context recovery review.

## 6. Portfolio policy uses inheritance

Do not copy generic portfolio policy into every repository.

Resolve:

```text
Portfolio Constitution
 + Domain Standards
 + Applicable Profiles
 + Repository Decisions
 + Scoped Exceptions
 = Resolved Policy Snapshot
```

When an old local rule conflicts with newer accepted portfolio policy:
- preserve the old source;
- explicitly adjudicate/supersede it;
- retain rationale.

Do not let whichever document an agent finds first become authority.

## 7. Recurring portfolio defaults are inherited, not retyped

Current qualified policy seed includes, subject to applicability/history audit:

- Python: `uv`;
- JS/TS: Bun;
- Oxc/Oxlint/Oxfmt direction where mature/compatible;
- `mise` as outer polyglot toolchain/version/env/task plane;
- native ecosystem managers retain dependency truth;
- Lefthook where appropriate;
- FastMCP where appropriate;
- ~500 LOC/source-file as a decomposition trigger, not blind splitter;
- no silent paid GitHub Actions compute;
- affected/component-aware CI;
- polyrepo physical ownership + synthetic-monorepo logical coordination;
- repository != build/release/test target;
- modular monolith/vertical-slice default;
- hexagonal seams at real trust/effect/volatility boundaries;
- microservices only with evidence;
- narrow independently consumable shared libraries;
- replaceable bounded workers;
- source/evidence over agent self-report;
- non-stable/post-stable release automation with stronger authority at stable promotion;
- upstream is input, not authority.

These are not universal commands. Applicability/profile resolution matters.

## 8. Git is the repository transaction ledger

Treat Git as append-oriented historical truth for repository content.

Preferred:
- coherent meaningful future commits;
- fast-forward when possible;
- merges that retain constituent commits where useful;
- revert/supersede instead of erase.

Disfavored:
- squash integration;
- rebase/rewrite of shared accepted history;
- force-push cleanup.

Historical ugly commits still have value through:
- diffs;
- parentage;
- ordering;
- authorship;
- later reverts/supersession.

Do **not** rewrite old SHAs merely to improve readability.

Improve retrospective readability additively:
- Genesis/history summaries;
- commit-range maps;
- ADR/decision links;
- PR/work references;
- regression dossiers;
- annotations/Git notes where safe;
- introduced-by / reverted-by / superseded-by relations.

Future commit readability should improve. Existing history should not be cosmetically rewritten.

## 9. Mature-first product recovery remains unchanged

This amendment does not replace:
- archaeology;
- SOTA;
- ontology;
- semantic requirements;
- quality overlays;
- journeys;
- stage projection;
- oracle design;
- implementation mapping;
- verticalization;
- falsification.

It adds durable-memory/recoverability as another hard completion dimension.

## 10. MACE/autograder remains first-class

Workers may see the rubric.

Protect correctness through:
- independent acceptance policy;
- exact candidate/configuration/verifier binding;
- negative/adversarial controls;
- immutable historical evidence;
- scope/grader changes separated from engineering progress;
- no empty/skipped greens;
- critical dimensions not averaged away;
- grader versioning;
- held-out checks where useful.

Track position/delta/slope/regression/stagnation/thrash/uncertainty only when the data supports those claims.

## 11. Preserve three lifetimes

```text
Worker Attempt
  ephemeral

Development Effort
  durable across workers

Product State
  durable across work systems
```

Do not conflate them.

## 12. GitHub execution

Add this doctrine into each pair's registry/repo documentation where it belongs.

Do not restart already-completed research solely to reorganize documents.

Reorganize/index existing good evidence rather than duplicate it.

Do not begin repository #3.

## 13. Completion amendment

100% is blocked if:
- major owner intent exists only in chat;
- Genesis is materially incomplete;
- important aliases/history are unrecovered;
- current decisions lack rationale/supersession;
- bulkheads are shallow placeholders;
- fresh human/agent recovery fails;
- repo policy cannot be resolved without manually asking the owner again.
