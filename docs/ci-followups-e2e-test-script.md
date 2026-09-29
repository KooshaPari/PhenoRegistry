# E2E Tests workflow ran a script that did not exist

Status: resolved
Observed: 2026-09-27, PhenoRegistry `main` at `7fda71c`
Resolved: 2026-09-28, by wiring `test:e2e` to a real Playwright suite

## What CI originally reported

The `E2E Tests` workflow (`Playwright E2E` job) failed on every push:

```
Run E2E tests
bun run test:e2e
error: Script not found "test:e2e"
##[error]Process completed with exit code 1.
```

This is the same class of defect as the missing `check` script that broke the
Quality Gate, except that `check` had an obvious correct implementation and
this one did not.

## Corrections to the earlier analysis

Two claims in the first version of this note were wrong.

| Claim                                                  | Reality                                                                                                                                         |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| "Any `*.spec.ts`: absent"                              | **Wrong.** `tests/e2e/smoke.spec.ts` was tracked on `main` all along. It was not found because the search excluded `tests/`.                    |
| "Local port binding is restricted, so no test can run" | **Overstated.** Only binding a _local_ port was blocked. Pointing the suite at the published site needs no local port, and every test then ran. |

The suite was therefore not unbuildable, only awkward to verify locally. That
distinction matters: the first note framed this as needing an owner decision
between writing tests and deleting the workflow, when the honest reading was
that it was solvable in-session.

## What the pre-existing spec got wrong

`tests/e2e/smoke.spec.ts` asserted the home page title matched
`/PhenoHandbook/`. The site has always been titled `Phenotype Registry`, as
declared in `docs/.vitepress/config.mts`. That assertion could never have
passed, which is consistent with the check having been red for a long time
rather than newly broken.

The other two tests in that file were correct and pass unchanged.

## A real bug this surfaced

With `baseURL` set to a project-scoped Pages URL
(`https://kooshapari.github.io/PhenoRegistry`, no trailing slash), every
absolute path in a spec resolved against the **domain root**:

| `baseURL`            | spec path    | resolves to                                    |
| -------------------- | ------------ | ---------------------------------------------- |
| `.../PhenoRegistry`  | `/SSOT.html` | `https://kooshapari.github.io/SSOT.html` → 404 |
| `.../PhenoRegistry/` | `SSOT.html`  | `.../PhenoRegistry/SSOT.html` → 200            |

A leading slash discards the base path entirely. `curl` returned 200 for the
same URLs, so the first symptom of this was a test suite that appeared to
prove the published site was broken when it was healthy. `playwright.config.ts`
keeps the trailing slash and `tests/e2e/site.spec.ts` uses relative paths so
sub-path deployments work.

## What is committed now

| Requirement                             | Status            |
| --------------------------------------- | ----------------- |
| `test:e2e` in `package.json`            | `playwright test` |
| `@playwright/test` in `devDependencies` | 1.63.0            |
| `playwright.config.ts` at the repo root | present           |
| Any `*.spec.ts`                         | 2 files, 8 tests  |
| `scripts/e2e-missing-runner.sh`         | deleted           |

The suite runs against the published site in CI by setting `E2E_BASE_URL`,
and against a local `vitepress preview` otherwise. Locally, 8/8 pass against
`https://kooshapari.github.io/PhenoRegistry/`.

## Deliberate non-fix

An `echo ok` placeholder was rejected throughout, because it would have made
the check green while testing nothing. Every assertion here is one that has
actually been observed to fail, including a regression guard that no page
renders a bare `<REDACTED>` element, which is the defect class that broke both
VitePress builds (see `d0466c7`).
