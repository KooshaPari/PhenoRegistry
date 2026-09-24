# Forensic history, branch, and regression audit policy

## Why this is required

The ecosystem has been heavily agent-managed, repeatedly reorganized, forked, extracted, archived, and regenerated. Current `main` is therefore only one evidence source. Contradictory READMEs, unusual default branches, duplicate product names, archived predecessors, and branch-specific extractions require history-aware analysis.

A forensic audit is not performed on all 146 repositories at maximum depth. It is triggered by risk and evidence.

## Audit depth tiers

### T0 — Census

For every repository:

- Identity, visibility, archive/fork state.
- Default branch and observed tip.
- Description, topics, size/languages.
- Last activity, releases, packages where available.
- Basic role hypothesis.
- Initial family and audit route.
- Known upstream or successor.
- Access/coverage limitations.

### T1 — Current canonical tree

- Repository instructions and exact current docs.
- Tree, manifests, packages, public interfaces, schemas, migrations.
- Tests, CI, release, packaging, deployment, examples.
- Current role/authority claims.
- Current build inclusion versus stubs/disconnected code.
- Current completeness vector.

### T2 — Reproducible current behavior

- Isolated build, lint, type, test, security, package and quickstart.
- Representative journeys.
- Quality-suite negative controls.
- Performance/resource smoke.
- Release artifact verification where available.
- Exact environment and logs.

### T3 — Targeted history and branches

- Releases/tags and major branch tips.
- Introduction/removal history of disputed capabilities.
- Rename/copy and extraction lineage.
- Merge-base and merge-result analysis.
- PR/issue/ADR history.
- Historical good/bad candidate reproduction.
- Consumer migration and compatibility.

### T4 — Full forensic recovery

- All accessible refs and commit graph.
- Unreachable/local evidence when safely available.
- Semantic clone and patch-equivalence analysis.
- Regression intervals and bisects where valid.
- Cross-repository extraction/fork history.
- Historical environment reconstruction.
- Capability-by-revision and branch-by-capability maps.
- Recovery frontier and staged integration candidates.

## T3/T4 triggers

Escalate when any apply:

- Two repositories claim the same product or authority.
- README, manifests, code, tests, registry, and branch status disagree.
- Default branch is an extraction/migration branch.
- Current implementation appears weaker than historical claims.
- A capability exists only on another branch or archived repo.
- Tests were removed, weakened, skipped, mocked, or disconnected.
- A repository is proposed for absorption, split, retirement, or deletion.
- A strategic fork’s base/divergence is unclear.
- Release/package history conflicts with source claims.
- A generic collection spans multiple likely bounded contexts.
- A large rewrite or agent wave may have lost prior behavior.
- Consumer paths reference nonexistent/renamed repositories.
- Licensing or provenance depends on exact lineage.
- The user explicitly identifies a high-priority recovery branch.

## Evidence preservation

Before mutation or broad fetch:

- Record local HEAD, refs, worktrees, dirty/staged/untracked state.
- Record remote URLs with credentials removed.
- Record shallow/partial clone, LFS, submodule, replace/graft, and alternates state.
- Preserve relevant local-only refs/reflogs without pruning.
- Create a coverage manifest.
- Work in an isolated clone/worktree.
- Disable unknown hooks and production credentials.
- Avoid automatic garbage collection.
- Hash retained raw evidence.

A fresh GitHub clone cannot prove the absence of local-only or expired history.

## Historical reasoning rules

- Commit messages are navigation, not truth.
- Timestamp order is not ancestry.
- `git log --follow` is not whole-repository lineage.
- Rename/copy detection is heuristic.
- Similar files do not prove common history.
- Similar history does not prove identical product purpose.
- Patch-equivalent commits may have different IDs after rebase/cherry-pick.
- Merge results must be compared against both parents and the merge base.
- Reverts and reintroductions create multiple good/bad intervals.
- An old snapshot failing to build in a modern environment is not proof it never worked.
- A current green build is not proof historical capability survived.
- A branch-only implementation is stranded capability until it was actually integrated/released.
- An unverified historical claim is not a demonstrated regression.
- An approved retirement is not a bug.

## Three baselines

Keep independent:

| Baseline | Question |
|---|---|
| Intended | What did the human and accepted contracts require at the relevant time? |
| Historical demonstrated | What behavior is supported by executable or credible retained evidence at a revision? |
| Current observed | What works now under recorded conditions? |

Also record proposed future target. Never collapse the four into one “current truth.”

## Regression record

Every finding gets a stable `REG-*` ID:

```yaml
id: REG-FOCAL-001
capability: CAP-...
expected:
  source: INT/FR/ADR/release
  behavior: ...
current:
  repo: KooshaPari/...
  ref: <sha>
  behavior: ...
historical_candidate:
  repo: KooshaPari/...
  ref: <sha>
classification:
  status: REPRODUCED_REGRESSION
  confidence: HIGH
alternatives_considered:
  - intentional retirement
  - moved to sibling repository
  - environment mismatch
reproduction:
  environment: ...
  commands: [...]
  oracle: ...
  raw_evidence: ...
introduction_interval:
  good: <sha>
  bad: <sha>
recovery_candidates: [...]
impact: ...
```

Allowed statuses:

- `REPRODUCED_REGRESSION`
- `STATIC_REGRESSION_CANDIDATE`
- `ENVIRONMENT_BLOCKED`
- `INTENTIONAL_CHANGE`
- `STRANDED_CAPABILITY`
- `MOVED_OR_EXTRACTED`
- `NEVER_VERIFIED_CLAIM`
- `FALSE_POSITIVE`
- `UNRESOLVED_CONFLICT`

## Semantic clone analysis

For suspected clone/duplicate repos, compare:

- Common roots and merge bases.
- Patch IDs and commit-message/token similarity.
- Directory and symbol fingerprints.
- Public API/schema/CLI surface.
- Tests and fixtures.
- User jobs and requirements.
- Upstream base and divergence.
- Consumers and release artifacts.
- Branch-specific unique capabilities.

Produce a capability union/intersection:

```text
A-only capabilities
A∩B shared capabilities
B-only capabilities
conflicting implementations
different non-functional behavior
different consumers/lifecycles
```

Do not simply choose the larger or newer repo.

## Recovery frontier

The target is not “restore the old repo.” It is the best compatible combination of:

- Accepted current intent.
- Strongest evidenced historical capability.
- Current security and compatibility fixes.
- Current consumer contracts.
- Target architecture and repository boundary.
- Reproducible quality evidence.

For each candidate choose:

- Forward-port.
- Reimplement behind current contract.
- Preserve as reference.
- Replace with external alternative.
- Intentionally retire.
- Recover into a different target repo.
- Defer pending experiment.

Test combinations in disposable locations. A clean cherry-pick is not sufficient evidence.

## Forensic outputs

A T4 family produces:

```text
forensics/
├── observation-baseline.md
├── refs-and-coverage.json
├── branch-topology.md
├── commit-path-symbol-index.json
├── capability-by-revision.json
├── branch-capability-matrix.md
├── intent-lineage.md
├── semantic-clone-analysis.md
├── regression-register.json
├── stranded-capabilities.md
├── merge-loss-analysis.md
├── test-weakening-analysis.md
├── recovery-frontier.md
├── candidate-integration-dag.md
├── reproduction/
└── checkpoint.json
```

## Current priority forensic families

Based on present contradictions—not completed verdicts:

1. `FocalPoint` ↔ `phenotype-apps`.
2. `Planify` ↔ `Planify2`.
3. `vibeproxy`, `vibe-monitor`, `vibeproxy-monitoring`, `vibeproxy-monitoring-unified`, archived router monitoring.
4. `thegent`, `Agentora`, `substrate`, `Tasken`, `Sidekick`, `PhenoProc`, ShareCLI.
5. `HeliosLab`, `forgecode`, `helios-cli`, and related historical consolidation branches.
6. `PhenoSpecs`, `phenotype-registry`, `PhenoHandbook`, `phenodocs`, archived governance/audit repositories.
7. `zz-agslag`, `Parpoura`, current portfolio-strategy authority.
8. Generic foundation and kit families.
9. Upstream-derived routing and coding-agent forks.
10. Applied product predecessors and split/extraction repos.

## Completion honesty

Report exact refs indexed, commits indexed, branches inspected, snapshots run, and gaps. “All history checked” is not valid without a coverage ledger. A full graph index is not the same as deep semantic inspection of every commit.
