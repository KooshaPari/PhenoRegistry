# Internal dependency snapshot supplement — ShareCLI PhenoShared

Date: 2026-09-30.

ShareCLI frozen source `4f01d0199e82b62bcf20399afcc102f58a10ad07` declares unpinned-by-manifest Git dependencies on `KooshaPari/PhenoShared` for:
- `substrate`;
- `runtime-process`.

Its frozen `Cargo.lock` resolves those Git packages to exact source commit:

`KooshaPari/PhenoShared@68beca269720d582a408dc5bbb62982fe86964af`

That commit was verified through GitHub and is dated 2026-09-16T11:31:13Z.

## Evidence consequence

For this recovery program, the exact PhenoShared revision above is the dependency source snapshot materially used by ShareCLI's frozen build and native recovery oracles.

The source manifest's floating Git declaration and the lockfile's exact revision are separate facts:
- manifest expresses dependency selection policy;
- lockfile defines the exact source used by this candidate.

A future candidate that updates the lockfile has a different dependency identity and cannot reuse native evidence from the old revision without requalification.

## Scope

This freezes dependency identity only. It does not:
- start a PhenoShared product recovery;
- import PhenoShared requirements into ShareCLI;
- certify substrate/runtime-process correctness;
- establish that every declared dependency is semantically necessary.

Inspect dependency APIs/source only where a mapped ShareCLI capability actually calls them.
