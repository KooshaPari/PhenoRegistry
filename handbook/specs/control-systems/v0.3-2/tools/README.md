# Local package tools

Python 3.10+ is sufficient for the standard-library checks and reference functions:

```sh
python tools/validate_docset.py
python -m unittest discover -s tests -v
python tools/schedule_policy.py examples/schedule-two-commits.json
python tools/verify_manifest.py
```

The validator checks IDs/source links, FR/test bidirectionality, evidence requirements, status discipline, backlog coverage/DAG, the old excerpt hash/log extraction, and new intake/evidence metadata integrity. Unit tests include pure scheduling, synthetic intake, historical fixture and API structure cases. They do not exercise the user host, GitHub workflow compiler, provider API, approval issuer, private network or database recovery.

## Reproduce full-export intake

```sh
python tools/index_forge_export.py /path/to/original-export.md --output-directory /path/to/private-intake-output
```

Use the original full export supplied by the user, identified in `evidence/session/intake-manifest.json`. It is intentionally not bundled here. The indexer normalizes CRLF for line locations but hashes original bytes, rejects malformed/duplicate contexts, and decodes each stored JSON context once. It emits metadata/ranges, not full prompts or tool contents. New metadata still requires publication review. It cannot reconstruct pre-compaction history.

`analyze_logs.py` is separate: it handles the original escaped terminal excerpt, not the full nested export. Repeating the analysis on duplicate export representations would produce invalid event counts.

## Regenerate views

`python tools/render_views.py` regenerates structured findings, source/FR/test views and ADRs from JSON. `python tools/render_site.py` rebuilds REPORT.md and the offline HTML reader and requires the optional `markdown-it-py` package. JSON Schema validation uses the optional `jsonschema` package; data-shape validation is not operational proof. The exact release checks and their limits are in `evidence/validation.md`.

The proposed OpenAPI document is not a deployed service. Internal tests check references, identity/precondition fields and no client self-approval flag. A full OpenAPI meta-schema/linter and real server interoperability test were not run.

## Integrity

`python tools/build_manifest.py` rebuilds the payload manifest/checksum list after intentional edits. `verify_manifest.py` checks file bytes and rejects missing/unlisted payloads. Manifest and checksum files exclude themselves to avoid recursive hashing. Python bytecode cache directories are ignored and not distributed. Hashes are integrity comparisons, not signatures; anyone able to rewrite both bytes and manifest can forge such a comparison.

Synthetic examples contain no approved target identity. Running the schedule example only prints eligibility and always returns `authorizes_deployment: false` and `may_advance_watermark: false`.
