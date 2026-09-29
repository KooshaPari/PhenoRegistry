# Pass 4 — native evidence promotion and ontology transition

Date: 2026-09-29.

## BytePort

BP-F03 is promoted from static/source finding to **native counterexample reproduced**.

Exact evidence:
- candidate/test commit `934b0456de5509b5e89294c3adaa046e632a2767`;
- workflow run `36615383712`;
- re-run job `109572633061`;
- Go test reached the real terminate handler;
- ProjectID `project-123`;
- persisted provider runtime ID `provider-sandbox-777`;
- actual upstream stop target `project-123`;
- expected `provider-sandbox-777`.

This confirms that Project and ProviderResource are distinct product identities. It does not close the replacement architecture.

BytePort now has ontology/source-artifact drafts establishing:
`Project → SourceSnapshot → ManifestRevision → BuildArtifact → DeploymentIntent → Operation → ProviderResource → Observation`.

The mounted source currently implements only fragments of that chain. Repository metadata is accepted/persisted, but immutable source resolution, manifest parsing, build-plan identity and selected application artifact are absent from the inspected deploy path. The provider request remains `alpine:latest`.

## ShareCLI

The original exact native attempt was infrastructure-blocked by unrelated tray compilation before the test ran. A targeted `sharecli-core` workflow removed that dependency, but its first isolated attempt exposed a second infrastructure prerequisite: `spawn-core-sys` requires Zig. The oracle still did not execute.

Classification remains:
`SC-F01 native = UNKNOWN / TEST NOT EXECUTED`.

The workflow has now been amended to provision the repository's pinned Zig 0.14.1 before running the unchanged adversarial test. This is an oracle-environment repair only.

ShareCLI's ontology/capability matrix now separates:
`observed, attributable, owned, supervised, mediated, filesystem-intercepted, optimization-eligible, result-shareable, recovery-managed`.

This prevents process detection from being treated as proof of command mediation or safe work sharing.

## Program consequence

The recovery program is now crossing from archaeology into semantic-contract construction, but only in evidence-backed slices. No mass requirement generation begins until the remaining source/authority denominator and high-risk architecture experiments are sufficiently resolved.

Native defect reproduction does not equal architecture closure. A remediation patch is not authorized merely because an exact failing test now exists.
