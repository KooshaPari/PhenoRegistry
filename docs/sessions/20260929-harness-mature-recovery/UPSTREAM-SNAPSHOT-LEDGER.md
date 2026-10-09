# Upstream snapshot ledger

Freeze date: 2026-10-02

| Lineage | Repository | Exact snapshot | Snapshot time | Role |
|---|---|---|---|---|
| Codex | openai/codex | `44dd77b71e88c78295736bffd3dc3b684c13be6d` | 2026-10-02T20:19:28Z | Contemporary external/upstream baseline for HeliosCLI |
| jcode | 1jehuang/jcode | `2df1f77e920c01b4eb7830cc3c9f74d735e98087` | 2026-10-02T03:35:36Z | Contemporary upstream baseline for KCode |

## Rules

- Do not compare HeliosCLI primarily against its excluded vendored Codex tree when deciding present-day differentiation. Use the frozen current Codex snapshot.
- Do not compare KCode only against the earlier jcode snapshot used during the September pass. Re-run material semantic comparisons against the October 2 snapshot.
- Vendored/historical upstream snapshots remain useful for ancestry and regression archaeology.
- Any later upstream movement must receive a new dated row; never silently move this baseline.
- “Upstream has X” requires mounted/behavioral evidence at the exact snapshot, not filename/name similarity.
