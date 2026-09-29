# Pass 4 — branch and predecessor lineage

Observed 2026-09-29. This pass records remote branch evidence that materially affects archaeology. Branch presence is evidence, not accepted product intent.

## HeliosLite

The frozen default source remains `536a25cac1dc21ac97bbc86c7e9af74bd5932780`. Branch search surfaced several non-default lines worth explicit review:

| Branch | Relation to frozen main | Material delta observed | Classification |
|---|---:|---|---|
| `preserve/helioslite-spec-20260807` | diverged; 15 ahead / 752 behind | release workflows, native update path, config reader, conversation hidden/migrations and other product surfaces | HISTORICAL/PRESERVATION; mine obligations, do not resurrect wholesale |
| `feat/journey-impl` | diverged; 1 ahead / 1186 behind | journey manifest README and journey traceability docs | HISTORICAL PROPOSAL/IMPLEMENTATION EVIDENCE; relevant to journey ontology |
| `fix/release-version-provenance-20260807` | diverged; 7 ahead / 696 behind | version/provenance and package/release changes | HISTORICAL IMPLEMENTATION; relevant to release identity |
| `feat/forge-dev-packaging-spec` | diverged; 1 ahead / 890 behind | 519-line packaging spec | HISTORICAL SPECIFICATION; authority must be reconciled before importing |

Main also has preservation/WIP/release branches. Search coverage is still not every branch; these were selected by alias and product-domain terms.

## KCode

Frozen default source remains `046ea2af5e01e84449f65d086510b51152360215` on `master`.

A branch named `fix/tui-focus-paste-panic-master` is **not a tiny patch relative to fork master**: GitHub compare reports it diverged, 2,111 commits ahead and 136 behind. Its manifest identifies upstream-style version `0.88.0`; its README retains upstream 1jehuang/jcode branding and its HANDOFF.md is absent. Current upstream source inspected separately is already version `0.89.2`. The branch therefore appears to be an upstream-sync/fix lineage, not sufficient evidence that it is the accepted KCode default or that 2,111 commits are owned fork intent.

Important consequence: do not replace the frozen master product model with this branch merely because it is numerically ahead. Instead:
1. identify fork-specific obligations/patches on master;
2. identify which are present, superseded or absent in later upstream;
3. construct an upstream-current + retained-patch alternative stack;
4. compare maintenance burden and behavior before deciding whether KCode should remain a deep fork.

The fork-prompt recovery artifacts on master point to commit `5670e8878`. Git comparison establishes the frozen master is 376 commits ahead of that commit with no divergence, so that specific runtime/visual acceptance work is part of master history rather than an orphan branch. The JSON records one direct user intent: make `/fork` visibly show the fork prompt; their self-reported final verification remains historical evidence, not current product acceptance.

## Falsification standard

A branch-name or ahead-count cannot establish authority. Before importing a branch obligation, require at least one of: direct user intent, accepted ADR/spec with provenance, a mounted current consumer contract, or a verified product behavior that would otherwise be unexplained. For abandoned branches, preserve unique obligations and evidence separately from obsolete implementation choices.

Still open: complete branch pagination/search vocabulary, tags/releases, PR linkage, merge-base chronology, deleted refs available only in airlock/local mirrors, and raw prior conversation passages.
