# Pass 22 — authority reconciliation and native-evidence truth

Date 2026-09-30. Program remains exactly Dino + Civis.

## Dino — native evidence is not currently trustworthy by workflow name

Current/main source remains exactly `17119051e782b32615413049c1c3cd207f0b540e`.

The only inspected workflow with a genuinely real-game execution design is `.github/workflows/game-launch.yml`:
- self-hosted [windows, dino-installed];
- explicit DINO/BepInEx environment;
- installs Runtime plugin;
- executes dedicated GameLaunch tests;
- uploads TRX/BepInEx artifacts.

Recent weekly schedules found Sep28, Sep21, Sep14, Sep7, Aug31, Aug24 are all cancelled. Latest three jobs have no executed steps. No recent native qualification exists from them.

`.github/workflows/game-launch-validation.yml` is a false-green risk. Concrete run `34687636798` on current main concluded **success** while logs state the game was not found and all restore/build/deploy/game-test steps were skipped. Workflow-level success therefore does not mean native product success.

`.github/workflows/game-automation.yml` is explicitly mock-capable: when the game is absent, it creates an empty executable at the expected path. It is automation harness evidence, never native-game evidence absent a separate fail-closed real-executable predicate.

Product-local source: `PASS-22-REAL-GAME-EVIDENCE-AUDIT.md`.

## Civis — current code stable, catalogue authority still contested

Current main: `590fad0643eb85cae89edd9e64ed6b991461de6e`.
Effective current code snapshot: `54d5758970249c8d1f24688ea45920b530e77299`.
Difference: exactly one docs-only commit adding `docs/audits/spec-only-triage-2026-09-29.md`; no code changes.

The new audit is useful catalogue-quality evidence but its 205 verdicts are not mature-product requirements by default. It chooses a rule where a per-ID acceptance criterion in a design doc can become REAL-GAP. The recovery program instead requires accepted current intent and supersession handling.

`FUNCTIONAL_REQUIREMENTS.md` is Draft dated 2026-03-25 and still mandates global deterministic replay/multi-client behaviors explicitly corrected by the May29–31 governing charter. Those contradictory draft rows are historical/superseded, regardless of their SHALL wording.

Product-local source: `PASS-22-AUTHORITY-SUPERSESSION.md` plus source-ledger C-S27.

## Gate consequence

- Dino cannot close native vertical-slice/evidence gates from workflow names or historical green badges; real game availability + executed tests + candidate/session identity must be explicit predicates.
- Civis cannot import old/new catalog row counts as accepted obligation denominators until authority is resolved.
- In both products, evidence/catalogue machinery itself is now a first-class failure surface.

No third product, no merge, no completion percentage.
