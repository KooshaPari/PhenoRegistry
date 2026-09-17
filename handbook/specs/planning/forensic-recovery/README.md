# Forensic SSOT recovery: helios-cli, heliosLab, forgecode, Agentora

Evidence capture generated: `2026-08-29T09:41:22+00:00`

## Result boundary

This bundle completes a **read-only, machine-derived acquisition and triage pass** over the four-repository scope. It does **not** claim that the recovered SSOT has been semantically adjudicated, that all private/deleted refs were visible, or that any recovery candidate should be merged. Those claims require the staged work in `ecosystem/recovery-work-plan.md`.

The two supplied protocols are copied byte-for-byte under `protocols/` and hashed in `protocols/protocol-index.json`.

## Acquisition summary

| Repository | Status | Default used | Reachable commits | Branches | Branch-only file candidates | TODO/debt markers |
|---|---|---|---:|---:|---:|---:|
| `helios-cli` | unavailable | `—` | — | — | — | — |
| `heliosLab` | unavailable | `—` | — | — | — | — |
| `forgecode` | unavailable | `—` | — | — | — | — |
| `Agentora` | unavailable | `—` | — | — | — | — |

Acquired repositories: **0/4**. Unavailable repositories: **4**. An unavailable repository is recorded as an evidence gap, never as an empty or nonexistent repository.

## High-value evidence tables

- `evidence/refs.csv` — advertised local branches/tags in each acquired mirror.
- `evidence/commits.csv` — reachable all-ref commit ledger with authorship and churn.
- `evidence/branch-divergence.csv` — default/non-default ahead/behind counts and merge bases.
- `evidence/restore-candidates.csv` — files absent from default but present on another branch.
- `evidence/historical-deletions.csv` — deletion events across reachable history.
- `evidence/documentation-inventory.csv` — current-tip prose and hashes.
- `evidence/manifests-and-ci.json` — build, dependency, task, and workflow signals.
- `evidence/cross-repo-mentions.csv` — textual references among the four names.

## What can be concluded now

1. The evidence perimeter and branch topology can be prioritized from the generated ledgers.
2. Candidate recovery material is enumerated without assuming that it is valid.
3. The current default tips can be compared against non-default history and against one another at the repository boundary.
4. No remote state was changed.

## What cannot honestly be concluded yet

1. Which branch or commit represents intended product truth.
2. Whether a missing path is a regression, rename, migration, duplication, or intentional deletion.
3. Whether README/roadmap claims match working behavior.
4. Whether all relevant private, deleted, forked, release, package, issue/PR, CI-artifact, or local-only evidence was visible.
5. Whether the four names represent the correct long-term repository boundaries.

## Next controlling documents

- `ecosystem/recovery-work-plan.md`
- `ecosystem/ssot-promotion-gates.md`
- `ecosystem/verification-matrix.md`
- `ecosystem/risk-register.md`
- `ecosystem/work-dag.json`
- each repository's `repositories/<name>/README.md`

## Integrity

Run `sha256sum -c SHA256SUMS` from the bundle root to verify all generated non-mirror artifacts. Git mirrors are excluded from the distributable archive; object IDs and acquisition logs remain in evidence.
