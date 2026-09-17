# Validation scope — v1.2

Run `python scripts/validate_package.py .`, `python scripts/validate_current_packets.py .`, and `python -m unittest discover -s tests -v` from this docs root in an isolated Python environment with the supplied dependencies.

The historical validator checks source/planning records, schemas, links, IDs, task graph, proposed pilot status and retained input integrity. The new validator checks the live non-zz set against one owner and one current folder each; source/name/default-branch identity; absent/fake session receipts; source SHA format; no invented native test/install/completion claim; next-action contracts; and projection consistency.

The Python tests include negative controls. They are NOT native product tests, a semantic proof of every statement, a live heartbeat collector, an authenticated reviewer, a secret scanner or an implementation of GitHub permissions. Passing schemas and checksums establish consistency/integrity, not truth of an author-provided result. No new product coverage percentages are claimed.

Actual results and archive/file digests are written after execution in validation/. The retained v1.1 VALIDATION_REPORT and reading PDF describe their historical scope; the current allocation is supplied by START-HERE and ONE-CHAT-PER-REPOSITORY.

## Final execution results

- 203 reference test methods passed in 29.463 seconds.
- Historical schema/trace/link/source-integrity validator: PASS.
- Current ID/name/branch/one-owner/folder/state-projection validator: PASS.
- All 24 non-zz subjects have eight packet files and a direct owner prompt.
- All 13 pages of the new reading edition rendered and visually inspected.
- No native product tests, installed application checks, real session polling, deployment changes or GitHub writes were performed.

Archive hashes, file counts and exact delta are computed at packaging. The full base archive remains unchanged.
