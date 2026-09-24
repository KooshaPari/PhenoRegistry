# Portfolio pilot crosswalk (2026-09-07)

Scope is limited to KooshaPari-owned portfolio pilot artifacts under
`pheno-portfolio-demos/G1-agentapi`, `G2-Apisync`, and `G3`. Agentora was
previously recovered and is intentionally excluded here. This is a read-only
artifact inventory; filenames and media counts are not treated as proof of
completion.

| Pilot | Contract/source refs found | Evidence observed | Remaining gates / limits |
|---|---|---|---|
| G1-agentapi | `G1-agentapi/01-live-server-session.txt`; version `0.12.2`; captured OpenAPI-derived health/version/ready/status/messages surfaces | `/health` returned `ok`, `/version` returned `0.12.2`, `/ready` returned true, `/status` reported running/claude/pty, and `/messages` had one message. The live POST `/message` round-trip failed with HTTP 500 because the agent was not waiting for user input. A malformed body was rejected with HTTP 422. | A successful live message round-trip is not evidenced. The transcript does not establish repeatability, clean startup, controlled fixture provenance, source commit, artifact hashes, or a complete S4 acceptance record. The rendered video/HTML/PDF bundles are presentation artifacts and require independent claim-to-source/evidence QA before being treated as proof. |
| G2-Apisync | `G2-Apisync/01-build-test-evidence.txt`; `G2-Apisync/01-s4-real-pilot-transcript.txt`; crate `apisync v0.2.10`; public modules/exports listed in transcript | Build evidence says `cargo check` finished and reports `TOTAL PASSED: 164`. The S4 transcript records a release build, workspace test lines totaling 164 passes (139+11+10+4), generated docs, and the public export surface. | Evidence is captured text, not independently rerun here. The transcript also reports a crates.io reference of `apisync = "0.2.9"`, while the local pilot says `0.2.10`; version/provenance reconciliation is required. No explicit manifest with source commit, lockfile hash, environment, artifact hashes, or failure/negative-control results was found in this pilot directory. |
| G3 / argis | `G3/01-argis-s4-transcript.txt`; local HEAD `f16740206f7160d654afdf540e8873c65184e823`; claimed ancestry correction from Kogito/bifrost-extensions | Transcript records `bifrost version 1.0.0`, real plugin listing, config showing all three provider keys unset, dataset listing, migration CLI help, repo facts (3 branches, 524M, Go/Python counts), and lineage evidence that the claimed parent is a false fork. | No successful provider-backed execution is evidenced because API keys are unset. Dataset rows are inventory, not evaluation results. Migration output is help text, not applied/rollback verification. Lineage claims need source/remote evidence and provenance review. No explicit contract, run manifest, output hashes, or S4 acceptance matrix was found under `G3`/`G3/argis`. |

## Shared artifact and gate observations

- Each pilot has substantial video, still, audio, HTML, and PDF output trees. Their presence and repeated segment numbering do not prove that the underlying runs were successful or reproducible.
- `G2-Apisync` has the strongest retained execution transcript, but its version mismatch and lack of a machine-readable manifest leave provenance and repeatability open.
- `G1-agentapi` has a concrete negative result for the live message path; any headline claim must disclose that the captured session did not complete a live round trip.
- `G3` demonstrates CLI/plugin/configuration inspection and a lineage correction, not live model/provider behavior or migration correctness.
- Exact source references in the available artifacts are limited to transcript-described versions, exports, and the G3 HEAD; no per-run source/fixture/configuration hash manifest was found in these three pilot directories.

## Relationship to the Agentora portfolio pilot

These are separate portfolio pilot lanes, not evidence that closes the Agentora
Patch Review Workbench gates. Agentora's recovered scope remains its own frozen
fixture contract, adapter evidence, and isolated-capture requirements. This
crosswalk supplies comparative provenance and gap context only; it does not
upgrade any pilot to S4/S5 or certify the media bundles.
