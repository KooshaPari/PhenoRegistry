# Review broker and historical finding reconciliation

## Goal

Extend the existing review/GitOps controller into a **quota-aware semantic-review broker**. Do not create a second review product. S052, S065.

The user's current provider set is already large enough: Kilo, CodeRabbit, CodeAnt, Macroscope while existing credit remains, Codex, plus deterministic and existing GitHub/security tooling. A sixth semantic reviewer is not a default requirement.

## Live provider facts that matter

| Provider | Useful current control | Budget/limit implication |
|---|---|---|
| CodeRabbit | auto-review can be disabled; labels/description/manual `@coderabbitai review`; pause/resume/full review | Free PR bucket documented at 3/hour; OSS may vary 1–8/hour; actual PR evidence hit a reset wait. S067-S069, S078 |
| CodeAnt | CLI can enumerate unresolved provider comments and resolve by thread/comment id | Useful for reconciliation; resolving is an action after adjudication, not the adjudicator. S070 |
| Kilo | GitHub reviewer, free models can be selected | Free models can be upstream-rate-limited/change over time; auto update reviews can waste capacity. S072-S073 |
| Macroscope | usage-priced review with spend caps; initial/free credit may exist | finite-credit specialist lane; `cash_spend_allowed=false`, auto-refill off. S071, S079 |
| Codex | GitHub review included within ChatGPT/Codex plan usage; `@codex review` supported | shared scarce subscription allowance; current remaining quota must be observed rather than treated as free. S074-S075 |

Deterministic tests/security remain outside this table: they are gates, not semantic-review quota competitors.

## Provider adapter state

```text
provider_id
health / auth / repository_eligibility
trigger_mode: automatic | label | comment | cli | unavailable
quota_remaining / reset_at / quota_confidence
credit_remaining / cash_spend_allowed / auto_refill
max_files / max_bytes / supported languages/specialties
supports_incremental / supports_full / supports_resolve
last_success / latency / reliability
unique_valid_yield / duplicate_rate / false_positive_rate
```

Do not encode CodeRabbit as "2/hour" or any other remembered constant. Refresh effective state because plan, OSS classification and fair-use windows differ.

## Risk-tier scheduler

A default policy can be:

- **R0**: deterministic gates only; docs/generated/trivial changes where semantic review is explicitly unnecessary.
- **R1**: one semantic reviewer selected for availability and fit.
- **R2**: primary reviewer plus one orthogonal specialist if risk warrants.
- **R3**: release/security/high-impact change; at least two independent semantic perspectives where capacity permits, plus all mandatory deterministic/security gates.
- **R4**: explicitly budgeted review summit for disputed or unusually high-risk work; never the default.

A provider being unavailable does not make a PR green. The broker either selects an allowed substitute or reports a blocked policy requirement.

## Quota discipline

- Disable/limit automatic per-push review where supported.
- Do not request review while the coding agent is producing rapid intermediate commits.
- Dispatch after a coherent candidate/repair batch.
- Reserve scarce reviews for exact-head final passes and escalations.
- Use bounded retries only for transient provider failures; quota exhaustion waits for reset/fallback instead of hammering the endpoint.
- Never enable paid overage or auto-refill under the current zero-new-spend authority.

## Common finding record

Normalize every provider finding into one record:

```text
finding_id / provider / review_run_id
repo / PR / base_sha / head_sha
path / diff anchor / semantic signature
severity / confidence / category
provider text reference (not copied authority)
status: valid_current | fixed_unresolved | stale_revalidate | duplicate |
        false_positive | accepted_risk | unclear
supersedes / duplicate_of
adjudication evidence
remediation PR/commit/test receipt
thread resolution receipt
```

## Historical reconciliation algorithm

1. Enumerate open PRs, recently merged PRs, then older backlog by risk and unresolved age.
2. Fetch review threads/comments from every installed provider plus human reviews.
3. Normalize and deduplicate findings.
4. Revalidate the code fact against the relevant current revision.
5. **Open PR:** repair valid findings on the current branch when still in scope.
6. **Merged/closed PR:** inspect current default branch. If the defect survives, open a new remediation PR; otherwise record `fixed_unresolved`, `stale`, `duplicate`, `false_positive` or `accepted_risk` with evidence.
7. Resolve old threads only after disposition is grounded.
8. Run exact-head deterministic gates and selected semantic final review.
9. Record review yield and remaining backlog.

ForgeCode PR 277 demonstrates why this matters: earlier audit evidence found unresolved material threads, and the PR is now merged. Current comments also show CodeAnt continuing while Copilot and CodeRabbit hit quota/limit states. S065-S068.

## Metrics

Track unique valid findings per review, duplicates, false positives, remediation rate, median latency, quota consumed per valid finding, cash/credit consumed, unresolved age and provider availability. Add another default reviewer only when these data show marginal value or useful independent availability.
