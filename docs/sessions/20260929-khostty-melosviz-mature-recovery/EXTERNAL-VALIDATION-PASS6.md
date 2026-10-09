# External validation baseline — pass 6

Observed 2026-09-29. This is a demand/evidence baseline, not a product-quality score.

## Khostty

- Repository created 2026-08-04; current raw GitHub metadata: 0 stars, 0 forks, 0 subscribers/watchers, 1 open-issue count (GitHub's field includes pull requests in some contexts).
- Search of all 7 pull requests returned in the repository shows all 7 authored by `KooshaPari`.
- Issue-only search returned no issues.
- Release `v0.1.0` published 2026-09-27. Asset download counts observed 2026-09-29: checksums 2; macOS zip 1; Windows installer 0; WASM tarball 1; VT-library Debian package 1; GTK app Debian package 1.

## Melosviz

- Repository created 2026-06-08; raw GitHub metadata: 0 stars, 0 forks, 0 subscribers/watchers, 13 open-issue/PR count.
- The first 100 PRs returned by chronological repository PR search are all authored by `KooshaPari`.
- Issue-only search returned one visible issue, `AgilePlus Pillar Scorecard`, i.e. process/tooling rather than user product feedback.
- Release `v0.1.1` published 2026-09-17. macOS arm64 tarball download count 2; DMG count 3.

## Interpretation

These observations **do not establish that either product is unwanted**. Both repositories and releases are young, GitHub download counters are not unique users, automated/internal downloads can occur, and private/off-platform use is invisible.

They do establish that the recovery program currently has **no defensible external-user validation evidence from public GitHub telemetry**. Therefore:

1. Existing code/release volume cannot substitute for the alternatives/existence gate.
2. `prod/users` validation remains a future empirical pilot dimension, separate from pre-build architecture/SOTA work.
3. No requirement should be justified with 'users depend on this' absent a specific external witness.
4. Once a credible CVP/vertical product exists, recruitment of a small real external user cohort and observed task outcomes is higher-value than further internal scorecard polishing.
5. The later pilot should distinguish unique external users, successful real tasks, repeat use/retention, human intervention, support burden and alternative-stack comparison; raw GitHub downloads/stars alone are weak measures.

## Source identity

GitHub repository/release metadata retrieved 2026-09-29 from the exact public repositories. Product source snapshots for the design program remain Khostty `a29aa9c6553d9f42aa68e2919116c0f6d53f329d` and Melosviz `1aec20a2ba41a01ed557d1c7f63f9a0089f842cf`; telemetry is intentionally current rather than frozen to those source commits.
