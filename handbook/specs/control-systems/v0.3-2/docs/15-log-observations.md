# Reproducible excerpt observations

These are counts of matching lines in the supplied file, **not** full-session rates or causal diagnoses. See `tools/analyze_logs.py` for the exact method and `evidence/log-metrics.json` for original line indexes and the 316-item trace inventory.

| Observation | Count |
|---|---:|
| context_limit_512000 | 718 |
| context_resolution | 717 |
| terminal_traces | 316 |
| unique_combo_ids | 316 |
| terminal_error_class_null | 316 |
| empty_completion_warnings | 1 |
| upstream_error_before_content_warnings | 5 |
| zero_model_sync_reports | 18 |
| cpa_route_lines | 125 |
| explicit_fallback_events | 1 |

## Terminal decision-count distribution

| Recorded decisions field | Trace count |
|---:|---:|
| 61 | 1 |
| 62 | 1 |
| 63 | 6 |
| 64 | 30 |
| 70 | 1 |
| 71 | 3 |
| 72 | 19 |
| 94 | 1 |
| 95 | 53 |
| 97 | 2 |
| 98 | 7 |
| 99 | 192 |

## Explicit fallback observation

Original line 1777 reports `83173ms, 32 fallbacks` for one successful routing event. This is a source-recorded duration, not an independently measured user-end-to-end latency. The six warning lines are 501, 520, 593, 831, 1053 and 1191. The opening main log segment covers about 34.5 minutes, while the later selected active-log view includes earlier times. Do not merge them into a complete ordered request stream.

All parsed terminal-trace status records here are HTTP 200 with a null terminal error class. That does not prove useful output, absence of earlier failed attempts, or correct end-to-end behavior. The semantics of `decisions` remain unresolved. No inference of 99 retries, six failed user requests, or a request failure percentage is made.

Source: S001, whose exact SHA256 is preserved in `evidence/source-manifest.json`.
