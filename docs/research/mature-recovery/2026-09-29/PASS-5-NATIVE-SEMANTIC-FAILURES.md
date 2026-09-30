# Pass 5 — native semantic false-green and remediation-boundary update

Date: 2026-09-30.

## ShareCLI SC-F01 upgraded

Exact recovery workflow run `36627656798`, job `109609724650`, compiled and executed the real `sharecli-core::Hypervisor` adversarial test after provisioning the required Zig 0.14.1 build dependency.

The first invocation read `first edit\n`. The fixture changed the same already-modified file to `second edit\n` while preserving the Git-mode fingerprint dimensions. The second Hypervisor invocation returned `first edit\n`.

Classification: **SC-F01 NATIVE COUNTEREXAMPLE REPRODUCED**.

The same run attempted FUSE and degraded because `user_allow_other` was unavailable. This is independent mode evidence: the cache false hit reproduced without successful FUSE interception.

### Architecture consequence

Git HEAD + porcelain status is conclusively insufficient as a generic durable result-equivalence identity. This does not imply “hash the entire repo” is the correct fix. The product must first define bounded equivalence adapters and sharing lifetime.

A new native matrix now probes:
- Args mode across different workspaces;
- Git mode across different environment values;
- Time mode with changed external input.

The product implementation is unchanged.

## BytePort BP-F04 probe correction

The first crash-window probe failed before reaching the provider because it closed the database too early. It is classified **INVALID PROBE / NO PRODUCT CONCLUSION**.

The corrected probe keeps the DB live through request setup/provider deploy and injects failure specifically at GORM Project creation. It then requires:
- provider deploy was called exactly once;
- local response reports persistence failure;
- no compensating provider stop occurred;
- no local Project row exists.

A PASS means the current unsafe remote-side-effect window was reproduced. It is still an observational risk probe, not desired-behavior acceptance.

## BP-F03 remediation contract

Native wrong-provider-ID evidence is now converted into a lifecycle contract rather than a one-line patch. Project, RealizedDeployment and ProviderResource are distinct. Project-level terminate resolves the current deployment and exact provider resources; specific deployment/resource operations remain explicit.

Negative controls include multiple historical deployments, multiple resources, stale IDs, stop-success/local-write-failure, timeout-after-success, repeat terminate, generation replacement and missing mapping. Legacy placeholder rows must not be upgraded into verified deployment history.

## Gate delta

- SC-F01: NATIVE REPRODUCED.
- ShareCLI equivalence-domain expansion: native workflow pending.
- BP-F03: NATIVE REPRODUCED; remediation contract drafted, implementation still intentionally unfixed.
- BP-F04 first probe: INVALID; corrected exact probe pending.
- Architecture risks closed: still zero replacement architectures proven. Reproducing defects is not architecture closure.
