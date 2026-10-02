# Execution receipt — 2026-09-29

Program: HARNESS-MATURE-20260929. First recovery cycle executed; neither primary product passes the specification/design gate.

## Draft PRs

- [HeliosLite #320](https://github.com/KooshaPari/HeliosLite/pull/320)
- [KCode #12](https://github.com/KooshaPari/KCode/pull/12)
- [PhenoRegistry #594](https://github.com/KooshaPari/PhenoRegistry/pull/594)

Exactly two primary products. Registry is their research/index surface. Other Helios/Shared scope remains lineage/dependency custody.

## Immutable source versus specification revisions

| Repository | Source analyzed | Specification head inspected |
|---|---|---|
| HeliosLite | 536a25cac1dc21ac97bbc86c7e9af74bd5932780 | 59278b19ff10612d308e5e51e34bf6831d6e581e |
| KCode | 046ea2af5e01e84449f65d086510b51152360215 | 8c9131f7deabfcab9e0dd62bcaa09c491b134bfc |
| PhenoRegistry | 85d7cd00cf59c379c05b740e8130a85b0d5bd31b | 7c885dce9e55fe562bf50529e63a851bb7b5626b immediately before this receipt commit |

HeliosLite initial spec commit 6dd2cb423ac44eca6bfc6aebc4497852a8dd742a; KCode initial spec commit b058a2d00b9a10cb03a901e46dfe4aed213551a8; registry initial research commit 6268d522b6bf3e8dbfa1287593e20c0df454dd30. Later primary commits add diagnostics, not production fixes. No implementation candidate is accepted.

GitHub compare read-backs confirmed each primary branch is two commits ahead of its frozen source and changes only seven newly added files under its dated product-contract directory, with zero deletions. This verifies change boundaries, not product correctness. PRs were created as drafts and not merged by this cycle.

## Executed diagnostic identities

| Subject | Local execution | Script SHA-256 | Read-back Git blob |
|---|---|---|---|
| HeliosLite decision-flow probe | Node v22.16.0, Linux, 2026-09-29T18:36:23.058Z | 4d6b5dfe15f1fddb2a357d3df5dd9a11999a2749b112d64cb765dfb97d321abb | 0a61af99a2f039d4846e4f53100136c5a6f143ee |
| KCode synthetic identity probe | Python 3.13.5, 2026-09-29T18:37:05.969658+00:00 | a653f63a46154ff01c98ced6fe74a96a93ce97ccec4a48975678ec90162d5378 | e4b32df19ba1ceb62fec36e366c7555737d5cf2d |

The local scripts' computed Git blob IDs matched connector read-back blob IDs from the committed primary artifacts. Raw local outputs were persisted in `diagnostics/` here; their read-back Git blob IDs also matched local bytes: HeliosLite receipt `19334cdf60d42662624f2cee73f5a28a7fe940ca`; KCode receipt `a2ff31867cdb948f8b2adc19847d13a8a54f6692`.

HeliosLite reproduced five unacceptable decision-flow outcomes plus two controls. One signal event was an actual Node child-process termination; the product benchmark itself was not run. KCode's 15 controls used synthetic evidence only. Both scripts' assertion success is categorically excluded from native product acceptance. No trusted attestation, immutable store, full clock/freshness validation or independently authorized grader implementation is established.

## First-cycle outputs and limits

Frozen source/default/dependency distinctions; alias/conversation/history recovery begun; bounded Registry records inspected; separate open source-coverage ledgers established; leading runtime/architecture uncertainties recorded; current external protocol/SDK/provenance and academic screening started; dedicated branches and three linked draft PRs created; receipts retained.

Outstanding: complete useful source/history/alias denominator, raw intent reconciliation, full SOTA/license/health/cost audit, best-alternative experiments, authoritative mature contract, quality/stage/journey completeness, native verifier and recovery tests, dependency graph, macOS trust/Windows behavior, complete implementation and trace mapping, orphan/contradiction closure, automated enforcement and fresh independent review. Actual AgilePlus registration is still outstanding.

No percentage, final architecture, merger choice, product viability victory or 100% specification/design completion is claimed. Existing runtime/CI code is unchanged. The next acceptance work is source-bound native counterexamples and state/identity experiments, alongside continuing archaeology and research—not mass generation of requirements.
