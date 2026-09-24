# Quick Repository Closure / Absorption Agent Prompt

Use only for a repository whose provisional disposition is `archive_normalize`, `absorb_then_archive`, or `decompose_and_archive`.

## Inputs

```yaml
source_repository: "<path or owner/repo>"
target_repositories:
  - "<path or owner/repo>"
portfolio_register: "<path>"
repo_ledger: "<path>"
human_overrides: []
```

## Objective

Close the source repository completely and safely. “Quick” means the implementation scope is narrow, not that verification may be skipped.

A successful run ends with one of:

- source archived with verified successor and no live consumers;
- source absorbed into target(s), parity proven, consumers migrated, then archived;
- closure blocked by one precise contradiction and placed on forensic hold.

## Prohibitions

- no deletion;
- no forced Git operations;
- no archive before successor and consumer verification;
- no bulk folder copy without semantic/provenance mapping;
- no trusting README archive claims;
- no claiming parity from compilation alone;
- no silently omitting issues, releases, packages, tags, branches, docs, fixtures, or CI;
- no new repository;
- no unrelated cleanup.

## Procedure

### 1. Snapshot

Capture:

- HEAD and dirty state;
- all branches/tags/releases;
- package identities;
- source tree and entry points;
- issues/PRs containing unmerged unique work;
- consumers and downstream references;
- licenses/provenance;
- secrets/runtime-state risks;
- declared successor.

### 2. Verify the successor

The successor must:

- exist;
- accept the intended authority;
- contain or intentionally reject every unique source capability;
- have compatible license/provenance;
- have a build/test path;
- have a rollback path.

A README link is not proof.

### 3. Build the migration matrix

For every unique semantic unit:

| Source | Role | Target | Transform | Provenance | Consumer | Parity test | Status |
|---|---|---|---|---|---|---|---|

Include code, docs, tests, fixtures, package names, workflows, issues, releases, and operational procedures.

### 4. Search consumers

Search:

- all local repositories;
- package manifests and lockfiles;
- CI workflows;
- submodules/subtrees/vendor references;
- imports and API calls;
- docs and install scripts;
- deployment configuration;
- package registries;
- releases;
- local operational scripts when available.

Classify each reference as live, historical, generated, or false positive.

### 5. Migrate or preserve

- preserve unique history;
- migrate unique value in small commits;
- retain compatibility adapters where needed;
- update consumers;
- deprecate packages;
- update source and target docs;
- update RepoLedger relationships.

### 6. Prove parity

Use source and target on the same fixtures. Check:

- behavior;
- API/schema;
- error semantics;
- security invariants;
- performance where contractual;
- package/install paths;
- primary journey;
- rollback.

Record commands, environment, exit codes, and immutable evidence.

### 7. Tombstone

The source README must state:

- exact closure date and commit;
- successor(s);
- what moved where;
- what was intentionally not moved;
- consumer migration;
- package deprecation;
- recovery/rollback;
- provenance/license;
- prohibition on new work.

### 8. Reconcile lifecycle

- update RepoLedger;
- regenerate registry/docs/profile;
- archive GitHub repository;
- remove active work/agents;
- close or transfer issues;
- retain releases/history.

## Closure gate

All must pass:

```yaml
successor_exists: true
authority_accepted: true
unique_history_preserved: true
semantic_units_mapped: true
consumers_migrated: true
packages_deprecated_or_repointed: true
source_target_parity_passed: true
license_provenance_preserved: true
secrets_runtime_state_reviewed: true
rollback_documented_and_tested: true
repo_ledger_updated: true
generated_views_updated: true
github_archived: true
```

If any value is false, do not call the repository closed.

## Required final report

```markdown
# Closure report

## Source
- repository:
- audited SHA:
- disposition:

## Target(s)
- repository:
- authority accepted:

## Unique value
- migrated:
- preserved historically:
- rejected with reason:

## Consumers
- migrated:
- historical only:
- unresolved:

## Verification
| Command | Environment | Exit | Evidence |

## Package/release state

## Provenance/license

## Rollback/recovery

## RepoLedger/GitHub reconciliation

## Blockers
```
