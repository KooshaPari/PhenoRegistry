# Active upstream snapshots — 2026-10-01

These are evidence baselines, not permanent pins.

| Lineage | Repository | Branch | Snapshot | Commit time | Head subject |
|---|---|---|---|---|---|
| Codex | openai/codex | default/main lineage | `60947e234156ac12bdb7fba2477d3965f166bd34` | 2026-09-30T19:22:34Z | Add account security setup reminders to the TUI (#49715) |
| jcode | 1jehuang/jcode | master | `5f1c091cf7682cbce781d08444cc19ffb7ec01d8` | 2026-10-01T05:16:40Z | sdk: document provider-native web search and test its bridge events |

## Interpretation

Both strategic upstreams are actively moving. HeliosCLI frozen source `2adc983...` has an architecture document explicitly saying its Codex hard fork was severed on 2026-06-30 and its vendored Codex trees are excluded reference material. KCode frozen source `046ea2af...` is likewise materially behind current jcode.

Therefore the mature design must minimize permanent fork delta. Preferred mechanisms, subject to capability evidence, are upstream contribution, stable extension/plugin/provider/runtime interfaces, generated/automated rebases, thin overlays and shared external harness primitives. A deep fork is justified only for semantics that cannot responsibly live upstream or behind supported extension boundaries.

These snapshots must be refreshed before any final existence/convergence decision because upstream movement is itself part of the maintenance-cost model.
