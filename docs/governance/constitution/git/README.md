# Git as Transactional Ledger

**Status:** proposed portfolio invariant derived from repeated owner intent.  
**Date:** 2026-09-29.

## Principle

Git history is a durable append-oriented transactional ledger for portfolio work.

The current tree is only the latest materialized state.

History preserves:
- prior states;
- individual changes;
- ordering;
- authorship/producer identity;
- parentage;
- reversions;
- experiments;
- regressions;
- migrations;
- documentation evolution;
- evidence about how current state emerged.

This is foundational to durable human/agent memory.

## Consequence

Optimize Git workflows for **preserving meaningful transaction history**, not for making the commit graph cosmetically small.

### Preferred

- small/meaningful commits;
- explicit commit messages;
- fast-forward updates when appropriate;
- merge strategies that preserve constituent commits;
- revert commits rather than erasing bad changes;
- additive corrections/supersession;
- tags/releases/baselines as durable anchors;
- branch/worktree isolation for concurrent work;
- signed/attested commits/tags where risk justifies it;
- PR metadata linked to preserved commit identities.

### Avoid by default

- squash merges that collapse multiple meaningful transactions into one;
- rebasing/rewrite of already-shared historical work merely for aesthetics;
- force-push rewriting accepted/shared history;
- deleting history to hide failed experiments/regressions;
- giant commits combining unrelated work;
- commit-message-only claims with no source/evidence.

History rewriting may be necessary for credential/secret removal, legal/privacy obligations or other exceptional safety cases. Such exceptions must be explicit and preserve whatever non-sensitive provenance can safely remain.

## Fast-forward clarification

Fast-forwarding is compatible with the ledger principle because it moves a ref to an existing descendant commit without collapsing or rewriting those commits.

The important property is preserved transaction identity and ancestry, not whether a merge commit exists.

## Merge policy

The desired property is:

> All meaningful accepted transactions remain individually recoverable.

Therefore:
- a merge commit is acceptable when it preserves the branch commits and conveys integration meaning;
- a fast-forward merge is acceptable when topology permits;
- squash is disfavored because it destroys the accepted branch's individual transaction identities from the target history;
- rebase-and-merge is disfavored for shared/accepted work because it rewrites commit identities even if patch content survives.

Exact GitHub branch/merge settings should be audited and configured to match this doctrine.

## Reverts

A mistake is part of the historical record.

Prefer:

```text
A → B → C(bad) → D(revert C) → E(correct replacement)
```

over rewriting history to pretend C never happened.

This is especially important for agent work because failed attempts, regressions and reversals are useful training/recovery evidence.

## Documentation relationship

Curated documentation is a human/agent-readable projection over the ledger.

```text
Git transactions
   ↓
raw provenance / changes
   ↓
decision + intent + architecture docs
   ↓
current bulkheads
```

Do not expect a human to reconstruct product intent from `git log` alone.

Conversely, do not let curated docs erase the lower-level transactional history.

Both layers are required.

## Commit quality

For the ledger to be useful, commits should be semantically meaningful.

A strong commit identifies:
- coherent change;
- relevant product/work identity where available;
- reason or link to decision/work record;
- evidence/verification when appropriate.

Avoid meaningless streams such as repeated `fix`, `wip`, or giant generated commits as the only historical explanation.

Temporary work can still be checkpointed; promotion/integration should preserve enough context to explain it.

## Agent implications

Agents must not treat history cleanup as a default finishing step.

Before history-changing operations, ask:
- is this history already shared/accepted?
- would transaction identities be lost?
- are downstream references/evidence bound to these SHAs?
- is rewrite required for security/legal reasons?
- can a revert/superseding commit solve the problem instead?

Commit SHAs may participate in evidence/provenance, so rewriting them can invalidate more than Git aesthetics.

## Transaction semantics beyond Git

Git is authoritative for versioned repository content and its transaction history.

It is not automatically authoritative for:
- runtime state;
- deployments;
- external SaaS configuration;
- secrets;
- product observations;
- work-system state.

Tracera/AgilePlus should link those external transactions/evidence to Git identities rather than pretending Git contains the entire world.

## Recovery test

A future human/agent should be able to answer:
- when was this behavior introduced?
- what did it replace?
- was it later reverted?
- what decision/work item motivated it?
- what evidence was associated?
- which current documentation supersedes the old interpretation?

without discovering that integration collapsed the only useful transaction history.
