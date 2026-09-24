# GitHub capabilities and candidate-bound approval

**v0.2 evidence update:** the candidate job names are now recovered: `ci / lint`, `ci / test`, `CI`. The historical protection JSON drops spaces from the first two. The current fetched CI code confirms the declarations but does not establish the approved on-wire check contexts, trusted producers or full production coverage. Only those authority/run bindings—not the candidate names themselves—remain unresolved. Older references below to an unresolved trio mean this precise binding. [S033–S036]

## Correct plan matrix

This is a documentation-derived capability matrix, **not** a verified snapshot of the user’s account. Actual owner type, visibility and activated benefit must be recorded for every repository. [S008–S010]

| Repository / owner plan | Environments and environment secrets | Deployment-branch restrictions | Environment required reviewers / wait timers | Branch protection |
|---|---|---|---|---|
| Public / Free | Available | Available | Available | Available |
| Personal private / Free | Not available | Not available | Not available | Not available |
| Personal private / Pro, including activated eligible student benefit | Available | Available | Not available under Pro | Available |
| Organization private / Free | Not available | Not available | Not available | Not available |
| Organization private / Team | Available | Available | Not available under Team | Available |
| Private / applicable Enterprise offering | Verify exact offering/settings | Verify | Supported subject to configuration | Supported subject to configuration |

Repository secrets are a different feature from **environment secrets**. An unavailable environment feature does not imply every kind of secret or Actions feature is unavailable. Student eligibility is not proof the benefit is activated, and a personal Pro entitlement does not resolve an organization-owned repository’s plan. BytePort was returned as public by the connected repository search, so a blanket private-repository assumption is already inappropriate. [S009; S031]

The official Actions limits page gives Free/Pro hosted concurrency of 20/40 and included personal-plan minutes of 2,000/3,000 per month at review time. These are planning inputs, not the current remaining allowance or a promise of available runner capacity. Store limits separately from usage and refresh before relying on them. [S011]

## The two gates must not be collapsed

**Verification:** the actual required check set, including the unresolved “trio,” validates the exact candidate under trusted check identities and current policy.

**Authorization:** the appropriate human or independent policy authority authorizes promotion of that exact candidate to a specific environment. It is not enough that someone clicked Run workflow, that a bot said “approved,” or that HTTP returned 200. A configured list of permitted environment reviewers is not an all-member quorum. [S007; S008]

## Minimum candidate identity — proposed contract

| Field | Why it is required |
|---|---|
| Repository stable ID, canonical locator and source revision | Prevent source or repository substitution |
| Artifact digest(s), architecture and build/provenance reference | Prevent mutable-tag replacement or wrong-platform deployment |
| Manifest-byte digest and configuration/secret-reference version | Bind behavior, not just source code; never include raw secret values |
| Environment ID and target ID/generation | Prevent cross-environment reuse and apply against changed infrastructure |
| Policy version/digest and named required-check set | Prevent changing what “passed” means after approval |
| Check producer identities, run/attempt IDs and conclusions | Prevent spoofed names, rerun confusion and stale checks |
| Dependency and data-migration plan identity | Include material external changes and state compatibility |
| Approval actor, scope, issue/expiry time and unique authorization ID | Support authentic attribution, freshness and replay protection |

Hash the **exact persisted candidate bytes** and refer to those immutable bytes. Do not describe ordinary JSON pretty-printing as a universal canonical-JSON standard. Hash equality proves identity relative to the trusted reference; it does **not** prove authorship, approval or safety. Signatures or approval records need authenticated issuance, key/identity validation and a trust store outside candidate control.

## Fail-closed evaluation order

1. Establish trusted repository, target and policy identities. Refuse unknown gate definitions, including an unresolved trio.
2. Fetch evidence from trusted systems, not fields asserted by the candidate. Verify source revision, check producer, run attempt, accepted conclusion and policy freshness.
3. Verify artifact/configuration identity and required capability results. Refuse a required test that is skipped, missing, cancelled, stale or merely claimed by a README.
4. Authenticate the authorization, verify its scope/expiry, and compare its complete candidate binding.
5. Acquire an exclusive target lease and compare the observed generation against the approved precondition. Revalidate if the target changed while waiting.
6. Execute only the reviewed plan through the canonical actuator. Append receipts, observe health probation and transition to active only after the defined semantic health conditions hold.

This is a specification, not a cryptographic gate implementation bundled as production code.

## When native private-repository gates are unavailable

The low-component-count fallback is the **existing human-apply-only path** or an already-established trusted deployment integration, with its credentials separated from untrusted CI and the unprotected candidate repository. The operator verifies the pinned candidate/evidence and invokes the trusted actuator from an environment whose policy and credentials the candidate cannot modify. It is a real manual gate only to the extent that this trust separation actually holds. [S004; S007; design proposal]

A `workflow_dispatch` button may be a user interface for that flow, but it is not independently sufficient. Repository-write actors who can replace a workflow and obtain its deployment secrets may bypass the intended check. Do not compensate for a missing native feature by pretending branch protection exists, using an `echo success` job, or approving the same candidate under a self-authored policy.

## Reuse the review-control contract

Deduplicate and adjudicate findings, retain false-positive and accepted-risk rationales, cap optional review rounds, and invalidate stale applicable results when the candidate changes. Preserve independent GitHub App trigger behavior until explicitly reconfigured by its owner. A local review router cannot be assumed to disable an independently auto-triggering App. [S007]

Mandatory security checks and required reviews remain required. Optional semantic reviewer quota optimization is separate. This package neither changes required checks nor authorizes merge, deployment, review dismissal, branch-policy relaxation or secret movement.

## Unresolved production blockers

The trio’s exact members; accepted producer identities; authorization actor/quorum; activation and expiry of student benefits; repository-specific settings; current deployment credential custody; canonical actuator location; emergency override process. Until these are resolved, a generated release request may reach **planned**, but not **approved for production**.
