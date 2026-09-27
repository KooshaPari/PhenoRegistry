# E2E Tests workflow runs a script that does not exist

Status: open, needs an owner decision
Observed: 2026-09-27, PhenoRegistry `main` at `7fda71c`

## What CI reports

The `E2E Tests` workflow (`Playwright E2E` job) fails on every push:

```
Run E2E tests
bun run test:e2e
error: Script not found "test:e2e"
##[error]Process completed with exit code 1.
```

This is the same class of defect as the missing `check` script that broke the
Quality Gate. The difference is that `check` had an obvious correct
implementation, and this one does not.

## Why there is no obvious fix

`test:e2e` was never written, and nothing it would run exists either:

| Requirement | Status |
|---|---|
| `test:e2e` script in `package.json` | absent |
| `@playwright/test` in `devDependencies` | absent |
| `playwright.config.ts` at the repo root | absent |
| Any `*.spec.ts` | absent |
| `playwright-report/` produced by anything | absent |

The only Playwright files in the repository are archived copies of other
projects' test suites, e.g.
`docs/specs/pheno-specs/archive/agent-wave/docs/tests/e2e/docsite.spec.ts`.
They are documentation of another repo, not a suite for this site.

The workflow still runs `bunx playwright install --with-deps chromium` before
the failing step, so CI downloads a ~150 MB browser and then never uses it.

## Why this was not simply made to pass

Three options were considered.

1. **Add `"test:e2e": "echo ok"`.** Turns a red check green. The workflow then
   appears to run browser tests while running none, and the wasted browser
   download stays. This converts a visible gap into an invisible one.

2. **Add a real Playwright suite.** This is the actual fix, and it is worth
   doing. It was attempted: `@playwright/test` resolves and installs cleanly.
   The blocker is verification, not feasibility. Local port binding is
   restricted in the authoring sandbox, so `vitepress preview` never bound a
   port and no test could be executed. Shipping a suite that has never run
   once would mean pushing unverified code to fix a red check.

3. **Fail loudly with an explanation.** Ship `scripts/test-e2e-stub.sh`, which
   exits 1 and prints why. The check stays red, but the log now names the
   actual problem instead of a bare "Script not found".

Option 3 is what is committed. The failure is unchanged in colour and
strictly better in content.

## What the owner should decide

Either:

- **Implement it.** Add `@playwright/test`, commit `playwright.config.ts` and
  a smoke spec, then set `"test:e2e": "playwright test"`. A useful first
  target is asserting the built site serves `/` and that no page renders a
  literal `<REDACTED>` tag, which is the defect class that broke both
  VitePress builds (see `d0466c7`).
- **Disable it.** Delete `.github/workflows/e2e.yml` until there are specs, so
  the failure stops being noise on every push.

## To activate real coverage later

Replace `scripts/test-e2e-stub.sh` with a direct `playwright test` call and
delete the stub. The stub documents the three prerequisites inline so the
next person does not have to rediscover them.
