# Runbook — workflow-action-guard (immutable Action references)

**Guard:** `scripts/workflow-action-guard.py`
**Checks:** `Immutable Action References`
(.github/workflows/workflow-action-guard.yml) and the inline
`Run workflow action guard` step in `.github/workflows/secret-guard.yml`
**Introduced:** PR #578 (`chore/workflow-action-guard-ci`, 2026-09-20);
filename/CR follow-up in PR #582.

## Why this exists

A workflow that pins an action to a mutable ref (`@v4`, `@main`) can be
silently re-run against different code the next time it runs: tags are
movable. Every `uses:` in this repo must therefore resolve to an immutable
identifier (a full 40-character commit SHA), so a CI run today executes the
same bits as a CI run next month.

## What the guard enforces

For every `*.yml` / `*.yaml` under the scanned workflow directory:

| `uses:` value                                   | Verdict |
| ----------------------------------------------- | ------- |
| `owner/action@<40-char SHA>` (+ `# vX` comment) | allowed |
| `./relative/path` (local composite action)      | allowed |
| `../other-repo/path`                            | allowed |
| `docker://image`                                | allowed |
| `owner/action@v4`, `@main`, bare `@latest`      | blocked |
| `owner/action` (no `@ref`)                      | blocked |

Parsing details (so failures are never a surprise):

- The parser is **line-oriented**: a `uses:` key at the start of a line
  (optionally as a compact list item `- uses:`) is checked; trailing
  ` # comment` is stripped before validation.
- The SHA must be **exactly 40 hex characters** — a short SHA is blocked.
- No network access: the guard does **not** verify that the SHA belongs to
  the named action. Ownership of the SHA is a review responsibility (see
  checklist below).

## When it runs

| Trigger                        | Workflow / step          | What is scanned               |
| ------------------------------ | ------------------------ | ----------------------------- |
| push to `main`                 | Workflow Action Guard    | trusted base tree workflows   |
| `pull_request_target` → `main` | Workflow Action Guard    | PR head workflows (read-only) |
| `workflow_dispatch`            | Workflow Action Guard    | trusted base tree workflows   |
| push / PR on **any branch**    | Secret Guard → last step | full `.github/workflows` dir  |

Trust model: on PRs the **script** always comes from the trusted base
checkout (`base/scripts/workflow-action-guard.py`); only the workflow files
being scanned come from the PR head, and they are parsed, never invoked.
The job has `contents: read` and a 5-minute timeout.

## Adding or changing a workflow — checklist

1. **Pin every `uses:`** to a full 40-char SHA, with the version in a
   trailing comment for humans:

   ```yaml
   - uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
   ```

2. **Resolve the SHA from the upstream repo** (do not invent it):

   ```bash
   gh api repos/OWNER/ACTION/git/ref/tags/vX.Y.Z   # → object.sha
   # annotated tags point at a tag object: resolve one level deeper
   gh api repos/OWNER/ACTION/git/tags/<tag-object-sha>
   ```

   Verify the commit is on the action's default branch before trusting it.

3. **Pre-flight locally** (fast, no CI round-trip):

   ```bash
   python scripts/workflow-action-guard.py .github/workflows
   # → workflow-action-guard: checked N workflow file(s)
   ```

   Or scan just the file you touched:
   `python scripts/workflow-action-guard.py .github/workflows/my-new.yml`.

4. Push / open the PR and confirm the `Immutable Action References` check
   is green. Secret Guard reruns the same script on every branch, so a
   failure surfaces there too.

5. **Bumping a pin**: repeat steps 1–4 in a normal PR; keep the
   `# vX.Y.Z` comment in sync with the new SHA so reviewers can eyeball
   the bump.

## Failure triage

| Symptom (check output)                     | Cause                            | Fix                                       |
| ------------------------------------------ | -------------------------------- | ----------------------------------------- |
| `unpinned action reference` at `file:line` | tag/branch ref or missing `@sha` | resolve full SHA (step 2), re-pin         |
| `unpinned` on a short SHA                  | < 40 hex chars                   | use the full commit SHA                   |
| `workflow path must be inside <repo>`      | scanned path escapes repo root   | pass paths relative to the repo root      |
| `missing workflow file`                    | wrong path argument              | check the filename (case-sensitive in CI) |
| Guard passes locally, fails in CI          | drift between base and head      | re-run step 3 on your exact branch        |

## Editing the guard itself

- PR scans run the **base** copy of `scripts/workflow-action-guard.py`;
  changes to the script only take effect for other PRs **after merge**.
- Keep the parser line-oriented and secret-free: failure output prints
  `file:line` only, never workflow contents (`No secrets are printed.` by
  design).
- If you extend the rules (e.g. allow a new scheme), update this runbook in
  the same PR.

## Related gates

- `secret-guard.yml` (all branches): runs `scripts/secret-guard.py` over the
  pushed/PR range **and** this workflow guard — it is the fast local-branch
  feedback path.
- `workflow-action-guard.yml` (main + PR target): the named
  `Immutable Action References` check with the trusted-base/untrusted-head
  split.
- Lefthook `pre-commit` (parallel) runs `scripts/workflow-action-guard.py`
  and `scripts/secret-guard.py --staged` locally (skipped on merge/rebase);
  `--no-verify` bypasses them, but CI will still catch an unpinned ref.
  The separate lefthook `grade` task is unrelated to this guard.
