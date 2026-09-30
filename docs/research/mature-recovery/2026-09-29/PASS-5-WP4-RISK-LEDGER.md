# WP-4 architecture-risk ledger — pass 5

Date: 2026-09-30. Scope remains exactly ShareCLI and BytePort.

## ShareCLI

### SC-RISK-01 — generic Git-mode durable result reuse
**Status: NATIVE COUNTEREXAMPLE REPRODUCED.**

Exact workflow `36627656798`, job `109609724650`, ran the real Hypervisor. The second invocation returned `first edit\n` after the relevant file contained `second edit\n`. This closes the question “can the current Git-mode key manufacture a semantic false green?” with **yes** for the tested configuration.

It does not close replacement architecture.

### SC-RISK-02 — omitted equivalence dimensions
**Status: NATIVE MATRIX PENDING.**

Independent tests now attack:
- Args mode across different workspaces;
- Git mode across environment changes;
- Time mode across changed external input.

The workflow is deliberately sequenced to continue after the already-known SC-F01 failure. Pending run: `36686200573`.

### SC-RISK-03 — FUSE mode truth
The successful native SC-F01 run also observed FUSE mount failure because the GitHub runner disallows `allow_other` absent `user_allow_other`; ShareCLI explicitly proceeded without FUSE. This is not a product defect by itself, but it is direct evidence that a Hypervisor result receipt must record interception mode. A cache/coalesce result cannot imply FUSE interception.

### Architecture decision pressure
The current generic `Args/Time/Git` modes should be treated as historical compatibility mechanisms, not accepted universal equivalence domains. The leading architecture is:
- tool-native cache delegation where available;
- explicit first-party adapters for bounded command families;
- potentially separate in-flight singleflight semantics;
- safe bypass for unknown equivalence;
- exact capability/evidence reporting.

## BytePort

### BP-RISK-03 — provider resource identity
**Status: NATIVE COUNTEREXAMPLE REPRODUCED.**

BP-F03 proves ProjectID and ProviderResourceID cannot share one identity field/meaning. A remediation contract now defines Project → RealizedDeployment → ProviderResource termination semantics before implementation repair.

### BP-RISK-04 — remote side effect before local persistence
**Status: FIRST PROBE INVALID; CORRECTED NATIVE PROBE PENDING.**

The first probe closed the database too early and therefore never reached NanoVMS. It is classified invalid, not negative evidence.

Corrected probe injects failure only at GORM Project create after provider success. Exact candidate `aae3fbaa1915cccb9498635c69e117d71a81763b`; CI run `36686241335` queued.

### BP-RISK-02 — selected application identity
**Status: SOURCE COUNTEREXAMPLE / NATIVE VERTICAL FIXTURE NOT YET BUILT.**

Mounted handler still submits `alpine:latest`; existing protocol tests validate that wire contract rather than selected-source correctness.

### Architecture decision pressure
Current evidence supports:
- BytePort owns Project/SourceSnapshot/ManifestRevision/DeploymentIntent/Operation/evidence semantics;
- NanoVMS is a runtime/sandbox adapter, not source-build owner;
- an established build engine should be prototyped before BytePort builds a custom build system;
- immutable artifact identity is mandatory at the deploy boundary;
- desired/observed state and provider side effects require explicit reconciliation semantics.

## Handoff state

Not ready for broad developer-agent implementation.

Ready now for **bounded architecture experiments**:
- ShareCLI equivalence adapters/singleflight experiments;
- BytePort delegated-build prototype and operation-journal/reconciliation prototype.

Production fixes to SC-F01/BP-F03 remain blocked until those bounded experiments select semantics that can grow into the mature contract.
