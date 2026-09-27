# Follow-up: doc-links test step is vacuous

Status: open, not fixed. Recorded 2026-09-27 during the t8 main-redness
clearance on PhenoRegistry.

## What

`.github/workflows/doc-links.yml` runs:

```yaml
- run: bun install --frozen-lockfile
- run: bun run test -- tests/requirements.test.ts
- run: bun run build
```

`tests/requirements.test.ts` is a Jest test (`describe` / `test` /
`expect`, uses `__dirname`). But:

- `package.json` defines no `test` script, so `bun run test` exits 0
  without running anything.
- `jest` is not in `devDependencies`, so it cannot run.
- There is no `jest.config.*` in the repo.

The step is therefore green while asserting nothing. The same applies to
`bun run check` before commit b54d63 added it.

## Why it was not fixed here

Adding a real `test` script turns the silent pass into a red build.
Evaluating all 37 assertions against the current tree, 20 fail:

- `SPEC.md` does not contain `### Security Anti-Patterns`,
  `### Performance Anti-Patterns`, `ANTI-PATTERN-SEC-001`,
  `METHODOLOGY-001: TDD`, `METHODOLOGY-002: BDD`,
  `CHECKLIST-001: Pre-Deployment`, `### Authentication Patterns`,
  `### Caching Patterns`, `### Observability Patterns`,
  `### Database Patterns`, any of the four ``` language fences,
  `## Code Quality`, `## Security`, `## Performance`, `## Deployment`,
  or `## Migration Guide`.
- `docs/.vitepress/config.mts` does not contain
  `{ text: "Patterns", link: "/patterns/" }`.

So the test encodes a specification the repo does not currently meet.
Closing the gap means either writing the missing SPEC.md content or
retiring the assertions. That is a product decision, not a CI fix.

## Options

1. Make the test real and bring SPEC.md up to what it asserts.
2. Narrow the assertions to what SPEC.md actually documents today, so
   the test guards real content instead of aspirational content.
3. Drop the `test` step from doc-links and keep only `bun run build`,
   which is what the workflow is actually named for.

Option 2 is the smallest honest change: the traceability test should
track the spec that exists, and separately record the gap.

## Note on the sibling workflow

`quality-gate.yml` had the same defect (`bun run check` with no
`check` script). That one is fixed in b54d63, pointed at
`scripts/conventions-lint.sh`.
