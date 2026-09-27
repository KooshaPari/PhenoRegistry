#!/usr/bin/env bash
# Honest placeholder for the E2E gate.
#
# The E2E Tests workflow runs `bun run test:e2e`, but no `test:e2e` script,
# no Playwright dependency, and no Playwright spec files were ever committed
# to this repository. The step previously failed with:
#
#   error: Script not found "test:e2e"
#
# The obvious fix -- a no-op `echo` -- would turn a loud red check into a
# green check that asserts nothing, which is worse than the current state
# because the workflow would appear to be running browser tests it never
# runs. This stub fails instead, and says why, so the gap stays visible
# until real specs land.
#
# To activate real E2E coverage:
#   1. Add @playwright/test to devDependencies and commit a lockfile update.
#   2. Commit playwright.config.ts and at least one *.spec.ts.
#   3. Point test:e2e at `playwright test` and delete this file.
#
# See docs/ci-followups-e2e-test-script.md for the full analysis.
set -euo pipefail

cat >&2 <<'MSG'
test:e2e is not implemented.

This repository has no Playwright dependency, no playwright.config.ts, and
no *.spec.ts files, so there is nothing to run. This step fails on purpose:
an empty `test:e2e` script would report success without testing anything.

The E2E Tests workflow also runs `bunx playwright install --with-deps
chromium` before this, which downloads a browser that is then never used.

To fix: add @playwright/test, commit specs, then make test:e2e run
`playwright test`. Until then, disable the E2E workflow or accept the
failure as a known gap.
MSG

exit 1
