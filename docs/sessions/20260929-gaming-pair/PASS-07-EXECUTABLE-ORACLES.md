# Pass 7 — executable expected-failure oracles

Date 2026-09-29. Exactly Dino + Civis. These tests are committed on specification branches and are **non-grading until executed against their bound candidate**.

## Dino

Commit `b99f883c9c52de30dd447935d4200f51c3ffc3fb` adds `src/Tests/RecoveryGenerationOracleTests.cs`.

Tests:
- removed item after successful ReloadPack must no longer be effective (or reload must explicitly report unsupported/restart-required);
- repeated reload of identical bytes must converge without manufacturing additional conflicts.

They use the existing ContentLoader + RegistryManager + temp-pack pattern, not Unity/BepInEx. They are designed to isolate generation replacement before native game testing.

Not yet added: stale patch-cache fixture, because PatchSet fixture syntax/application semantics should be copied from an existing real patch test rather than guessed.

## Civis

Commits `23e3c2e57df5cc51625e5ce14e09d3e34b5ba548` and `3fa63afaebb8cda25d084ae7114191abd0951525` add and mount `crates/engine/src/recovery_oracle_tests.rs` under `#[cfg(test)]`.

Tests:
- economy_policy survives save/load or forces an explicit contract decision to rebind it externally;
- research cache researched + queued state survives save/load;
- orphan mod guest memory cannot count as restored active mod state.

The mod fixture first proves the bytes survive, then deliberately requires corresponding active mod identity. It is expected to fail under the current source model.

## Execution status

NOT RUN by this recovery worker. The available execution environment previously lacked dotnet/cargo. A committed test file is not evidence of a failing/passing product until:
- exact source/test revision;
- toolchain/environment;
- command;
- executed case count;
- raw output/artifact;
- verifier identity
are recorded.

No production code was modified to satisfy these tests.
