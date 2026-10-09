# Pass 13 — first reproduced behavioral failures

Date 2026-09-30. Exactly Dino + Civis. These are candidate-bound recovery-oracle results, not whole-product verdicts.

## Dino — two confirmed generation failures, one oracle refined

Candidate `8cfc998678d14bca3329083efa93f741aa5c7f5e`.
Workflow run `36628553200`; artifact `11061109680`; artifact digest `sha256:4ef143c274a9c9d9ca63b8c3dea9a3f044a773d9837169ace5efeea6a45b8404`.
Test execution reached assertions: 3 executed, 0 passed, 3 failed.

### Confirmed D-BEH-01: removed content remains effective after successful reload

Fixture: pack v1 contains recovery-x and recovery-y; v2 removes y; IPackReloadService.ReloadPack delegates to LoadPack and reports no hard error. After reload, Registry.Units.Get("recovery-y") still returns Y v1.

This reproduces stale-generation retention in the isolated SDK path.

### Confirmed D-BEH-02: repeated identical reload creates a conflict

Fixture loads one pack/one unit, records zero conflicts, reloads identical bytes three times. DetectConflicts returns 1 instead of remaining 0.

This reproduces generation accumulation/conflict manufacture under identical candidate bytes.

### Patch oracle: first failure was assertion classification, not stale-cache behavior

Initial patch fixture failed because ContentLoader intentionally routes patch-phase informational messages through ContentLoadResult.Errors prefixed `[patch]`; existing SmokeTests explicitly filter these as non-hard errors. The stale-cache assertion was not reached.

Oracle corrected at product commit `e8009135b0fcb7d45f772739cc511f6695498fe3` to filter only `[patch]` informational entries, matching repository precedent. Rerun required before classifying stale patched YAML.

This multiplexing is itself API debt: a field named Errors contains informational progress. It can produce false failures/agent confusion and should be separated/versioned, but is not treated as a patch-application failure.

## Civis — three confirmed semantic persistence failures

Candidate `eb74d0724163f9958e93c16c4deeb18344882246`.
Workflow run `36628556544`; artifact `11062202963`; artifact digest `sha256:9d76dede0df4b2da29a2fbb8f17220f8950157ee22b7490972235852af7738fb`.
Compile succeeded. Test execution: 3 executed, 0 passed, 3 failed, 866 filtered out.

### Confirmed C-BEH-01: runtime economy policy resets across save/load

Before save: base_consumption_joules=123456, scarcity_multiplier=2.75.
After load assertion observed base_consumption_joules=5,000,000,000 (DEFAULT_ECONOMY_POLICY) instead of123456.

This confirms the source-derived omission for direct world-save semantics. Architecture still must decide whether policy belongs to world state or external scenario/profile identity. Current direct load silently defaults it.

### Confirmed C-BEH-02: research cache state is lost

Before save: researched=["pottery","masonry"], queued contains "writing".
After load: researched=[] at the first assertion.

ResearchCache directly affects snapshots and Age of Enlightenment victory criteria, so this is user/outcome-affecting state loss under the isolated bundle path.

### Confirmed C-BEH-03: orphan mod guest memory survives without active mod identity

The fixture intentionally creates guest memory for recovery-orphan-mod while proving that mod is absent, saves/loads, proves the bytes survive, then requires a corresponding loaded mod. The final assertion fails.

This confirms that successful mod_state.json round-trip is not active-mod restoration.

## Scope of proof

These results prove the isolated SDK/bundle behaviors above on exact candidates. They do not prove licensed Dino in-game effects, Civis UI/server journey behavior, every pack/save format, or the final desired remediation. Architecture decisions and regression controls follow before production fixes.
