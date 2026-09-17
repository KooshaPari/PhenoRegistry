# Initial forensic and recovery risk register

| Risk | Failure mode | Evidence needed | Mitigation |
|---|---|---|---|
| Incomplete ref visibility | valid work exists in private, deleted, local-only, or unadvertised refs | authenticated API, reflogs, forks, contributor clones, CI artifacts | label perimeter incomplete; never infer nonexistence |
| Default-branch bias | current tip is treated as canon despite regression | branch/merge-base/capability comparison | capability-level adjudication |
| Largest-document bias | generated plans overwhelm sparse but authentic intent | provenance and timestamps | separate verbatim intent from synthesis |
| Chronology bias | newest or oldest state is assumed best | test and contract evidence | score competing target states |
| Bulk-merge contamination | obsolete and valid changes are replayed together | dependency and capability slicing | isolated cherry-pick/port with characterization tests |
| Cross-repo version skew | locally valid repairs break ecosystem contracts | compatibility matrix | coordinate interface versions and migration |
| Build-success false confidence | build passes while required behavior is absent | requirement-linked negative tests | explicit observables and mutation testing where valuable |
| Secret/supply-chain exposure | historical blobs or regenerated dependencies introduce risk | secret scan, provenance/SBOM, lockfile audit | quarantine, rotate, pin, attest |
| Remote mutation before adjudication | evidence destroyed or false SSOT published | audit log | read-only until explicit authorization |
