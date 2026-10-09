# Current Owner Doctrine — 2026-09-30

Status: controlling synthesis, subject to later supersession with preserved lineage.

## Memory problem
The portfolio has exceeded reliable human/chat working memory. Repository/registry documentation must serve as durable external memory for both owner and agents. Human recoverability after months/years is a completion criterion.

## Documentation architecture
Major domains are documentation subsystems, not lone Markdown files:
- product dossier bulkhead;
- domain bulkhead (intent, Genesis, SOTA, architecture, verification, etc.);
- focused modules;
- evidence/raw sources.

Bulkheads must be concise relative to their subtree but substantive enough to stand alone. Shallow placeholder docs do not count.

## Genesis and raw intent
Genesis preserves conceptual lineage, motivating pain, historical names, pivots, rejected framings, surviving invariants and prerequisite reasoning.
Large owner-authored intent dumps are primary product artifacts. Index them, faithfully synthesize them, extract invariants/questions, and trace incorporation into canonical docs/decisions/specs.

## Portfolio constitution
Policy resolves through:
L0 portfolio constitution → L1 domain standards → L2 profiles → L3 repo constitution → L4 scoped overrides → L5 work snapshot.
Preserve policy lineage and supersession. Do not let an older document win because an agent found it first.

## Recurring policy seed
Repeated owner direction includes, pending exhaustive lineage audit:
- uv for Python project/workspace/package management where applicable;
- Bun as qualified JS/TS default;
- Oxc/Oxlint/Oxfmt direction where mature/compatible;
- mise as outer polyglot toolchain/version/env/task plane; native ecosystem managers retain dependency truth;
- Lefthook for cross-language hooks where applicable;
- FastMCP where appropriate;
- roughly 500 LOC/source-file as decomposition trigger/guardrail, not blind splitter;
- no silent paid GitHub Actions compute; use free public standard hosted where safe or self-hosted/already-paid compute; affected execution and cheap gates first;
- polyrepo physical ownership + synthetic-monorepo logical coordination;
- repository != build/release target; multi-app repos need affected target switches;
- modular monolith/vertical slices first, hexagonal seams at meaningful boundaries, services only when justified;
- shared libraries should expose narrow independently consumable capabilities, not god-libraries;
- agents are replaceable bounded workers; evidence outranks self-report;
- non-stable/post-stable release lifecycle can be automation-driven while stable/official promotion requires explicit authority/traceability;
- upstream is input, not authority; strategic hard forks are legitimate with lineage.

## Git ledger
Git is the append-oriented transactional ledger for repository state. Preserve meaningful transaction identities and ancestry.
Preferred: meaningful commits, fast-forward when possible, merge preserving commits when useful, revert/supersede rather than erase.
Disfavored: squash, rebase/rewrite of shared accepted history, force-push cleanup.
Historical ugly commits still have information value through their diffs/parents. Improve retrospective readability additively through dossiers, commit-range maps, decisions, annotations/notes where safe, and introduced/reverted/superseded relations. Do not rewrite old SHAs merely to beautify them.

## Product-recovery doctrine
Mature-first contract; stage projections (CVP/MVP/etc.) derive semantically from the mature product, not requirement quotas. Requirement counts are outputs. Progress distinguishes mature completeness, stage readiness, journey/feature closure, usable shape, evidence/trace state and transition debt.

SOTA/bootstrap research is a blocking design gate. For every major capability ask use/integrate/fork/adapt/compose/build and define the best realistic alternative stack.

MACE/ZyBooks-style grading is a shared control primitive: visible multidimensional distance-to-acceptance, localized feedback, exact evidence identity, anti-Goodhart controls, trajectory/regression/stagnation/thrash where meaningful.

Three lifetimes: ephemeral worker attempt; durable development effort (AgilePlus); persistent product truth (Tracera).

## Locked pair
Current pair is Tracera + AgilePlus. No third product in this program until both pass their strict design/specification gates.
