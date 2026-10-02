# Pass 3B — authority corrections from PR discussion archaeology

Date: 2026-09-29.

## ShareCLI PR #731 — do not promote bot summaries to user intent

Merged PR #731 was inspected with its full body/diff/comments.

The **User description** says the PR shards health/pool/status CSV export plus an agent-call admission kernel onto main, excludes a dirty recovery preservation state because those files were historical snapshot only, and updates FR/TRACEABILITY.

The separate **CodeAnt-AI Description** says specifications “remove superseded watch, FUSE, and harness requirements.” That sentence is bot-generated summary, not user text. It must not be cited as user intent to remove FUSE/harness from ShareCLI.

The actual diff shown in the PR removes a large set of FR-007 watch/export acceptance criteria and changes one-shot CSV behavior. Current main still contains FR-009 FUSE and harness recovery material. Therefore no accepted FUSE/harness scope deletion is inferred from PR #731.

This is a concrete example of the recovery program's authority rule: GitHub account ownership, merge status and textual proximity are insufficient. User-authored PR description, bot-generated description, review comments, implementation diff and current surviving contract are separate evidence types.

The same PR also demonstrates why passing tests are not enough: automated review identified contradictory CSV contracts and agent-call-policy correctness defects while a Quality Gate comment reported unit tests passed but FR annotations missing.

## BytePort source-wire contract

Current BytePort `deployment_contract_test.go` explicitly tests a SandboxConfig containing `alpine:latest` and verifies wire shape/auth/path. That is a valid protocol-level test but cannot be promoted into FR-DEPLOY-003/004 acceptance, which require selected Git repository/ref deployment. Protocol conformance and product-subject correctness are separate verifier dimensions.

This reinforces the planned source→artifact→provider identity chain and the rule that a test named “deployment contract” does not establish the mature deployment contract.
