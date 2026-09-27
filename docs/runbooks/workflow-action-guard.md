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

One accepted exception is **not** immutable: `docker://image` references are
allowed as written (verdict table below), but Docker _tags_ are mutable and
can yield different bits on a later run. The 40-char-SHA guarantee does not
cover `docker://` refs — prefer digest-pinned `docker://image@sha256:...`
and treat tag-pinned docker refs as a review-resolved decision.

## What the guard enforces

For every `*.yml` / `*.yaml` under the scanned workflow directory:

| `uses:` value                                       | Verdict |
| --------------------------------------------------- | ------- |
| `owner/action@<40-char SHA>` (+ `# vX` comment)     | allowed |
| `./relative/path` (local composite action)          | allowed |
| `../other-repo/path`                                | allowed |
| `docker://image` (tag mutable — not digest-checked) | allowed |
| `owner/action@v4`, `@main`, bare `@latest`          | blocked |
| `owner/action` (no `@ref`)                          | blocked |

Parsing details (so failures are never a surprise):

- The parser is **line-oriented**: a `uses:` key at the start of a line
  (optionally as a compact list item `- uses:`) is checked; trailing
  ` # comment` is stripped before validation. **Known blind spot:**
  flow-style or inline mappings — e.g.
  `steps: [{ uses: actions/checkout@v4 }]`, or a `uses:` that follows
  another key on the same line — are **never scanned and report as
  compliant**. Both gates share this parser, so CI does not cover the blind
  spot either; keep workflows in standard block style.
- The SHA must be **exactly 40 hex characters** — a short SHA is blocked.
- No network access: the guard does **not** verify that the SHA belongs to
  the named action. Ownership of the SHA is a review responsibility (see
  checklist below).

## When it runs

| Trigger                        | Workflow / step          | What is scanned                             |
| ------------------------------ | ------------------------ | ------------------------------------------- |
| push to `main`                 | Workflow Action Guard    | trusted base tree workflows                 |
| `pull_request_target` → `main` | Workflow Action Guard    | PR head workflows (scanned, never executed) |
| `workflow_dispatch`            | Workflow Action Guard    | trusted base tree workflows                 |
| push / PR on **any branch**    | Secret Guard → last step | full `.github/workflows` dir                |

The `pull_request_target` row materializes the **PR head tree inside the
privileged job** — `ref: <head sha>` with
`allow-unsafe-pr-checkout: true` (required for fork PRs at the pinned
checkout version), sparse-checked out to `.github/workflows`. "Read-only"
is a _convention this workflow's steps enforce_, not a property of that
checkout: the guard parses `pr/`, and **nothing from `pr/` may ever be
`run:`** — a future `run:` step against `pr/` would execute untrusted PR
code with the base workflow's privileges.

Trust model — two gates, two script origins:

- **`Immutable Action References`** (`workflow-action-guard.yml`): the
  **script** always comes from the trusted base checkout
  (`base/scripts/workflow-action-guard.py`); only the scanned workflow
  files come from the PR head, and they are parsed, never invoked. The job
  has `contents: read` and a 5-minute timeout.
- **Secret Guard's inline step** (`secret-guard.yml`, every branch): a
  single checkout of the PR's tree, then
  `python scripts/workflow-action-guard.py` runs **that PR's own copy of
  the script** — a PR can weaken or delete it and the step still reports
  green. Base-script enforcement therefore exists **only** in the named
  `Immutable Action References` check.

## Adding or changing a workflow — checklist

1. **Pin every `uses:`** to a full 40-char SHA, with the version in a
   trailing comment for humans:

   ```yaml
   - uses: actions/checkout@<40-char-sha> # vX.Y.Z
   ```

   Use a placeholder until you have resolved the real values (step 2) —
   do not copy a label from elsewhere in this repo: the same
   `3d3c42e5aac5ba805825da76410c181273ba90b1` is commented `# v7` in
   `workflow-action-guard.yml` and `# v4` in `secret-guard.yml`, and the
   runbook's own instruction below is to keep the comment in sync with the
   SHA after verifying it upstream.

2. **Resolve the SHA from the upstream repo** (do not invent it):

   ```bash
   gh api repos/OWNER/ACTION/git/ref/tags/vX.Y.Z   # → object.sha
   # annotated tags point at a tag object: resolve one level deeper
   gh api repos/OWNER/ACTION/git/tags/<tag-object-sha>
   ```

   Verify the commit is on the action's default branch before trusting it.

3. **Pre-flight locally** (fast, no CI round-trip) — **run from the
   repository root**. Paths are anchored at the current working directory
   (`Path.cwd()`): invoked from a subdirectory, the default argument
   resolves to nothing and prints `checked 0 workflow file(s)` — a silent
   pass, not an error.

   ```bash
   python scripts/workflow-action-guard.py .github/workflows
   # → workflow-action-guard: checked N workflow file(s)
   ```

   Or scan just the file you touched (again, from the repo root):
   `python scripts/workflow-action-guard.py .github/workflows/my-new.yml`.

4. Push / open the PR and confirm the `Immutable Action References` check
   is green (that check runs only for PRs targeting **`main`**). Secret
   Guard reruns the guard on every branch **from your branch's own copy of
   the script** (see _Trust model_), so treat it as a fast smoke signal
   rather than an equivalent of the trusted-base check.

5. **Bumping a pin**: repeat steps 1–4 in a normal PR; keep the
   `# vX.Y.Z` comment in sync with the new SHA so reviewers can eyeball
   the bump.

## Failure triage

| Symptom (check output)                     | Cause                                                                                                                                                                                      | Fix                                                                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| `unpinned action reference` at `file:line` | tag/branch ref or missing `@sha`                                                                                                                                                           | resolve full SHA (step 2), re-pin                                                                                    |
| `unpinned` on a short SHA                  | < 40 hex chars                                                                                                                                                                             | use the full commit SHA                                                                                              |
| `workflow path must be inside <repo>`      | path resolved outside the current working directory — the dominant cause is running the script from a subdirectory (the anchor is `cwd`, not the repo root), not a genuinely escaping path | **run the guard from the repository root**; re-passing a relative path does not help when the anchor itself is wrong |
| `missing workflow file`                    | wrong path argument                                                                                                                                                                        | check the filename (case-sensitive in CI)                                                                            |
| Guard passes locally, fails in CI          | drift between base and head                                                                                                                                                                | re-run step 3 on your exact branch                                                                                   |

## Editing the guard itself

- In the `Immutable Action References` check, PR scans run the **base**
  copy of `scripts/workflow-action-guard.py`; changes to the script take
  effect there for other PRs only **after merge**. Secret Guard is the
  opposite: it runs whatever copy the PR itself carries, so a script change
  is live in that PR's Secret Guard run immediately (see _Trust model_).
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
  and `scripts/secret-guard.py --staged` locally (skipped on merge/rebase).
  `--no-verify` bypasses them; for PRs targeting **`main`** CI still catches
  an unpinned ref via the trusted-base `Immutable Action References` check —
  but a PR targeting any other branch runs only Secret Guard's inline step,
  which executes the PR's own copy of the script, so a `--no-verify` change
  that also edits the script has no remaining gate on that branch.
- Lefthook `pre-push` runs the separate `grade` task (`just grade` /
  `task grade`) — not part of `pre-commit`, unrelated to this guard, and
  equally skipped by `--no-verify`.
