# What the full session changes

## Bottom line

The earlier v0.1 design was directionally useful but lacked decisive implementation evidence and part of the product intent. The full stored session now supplies both. **The recovered pilot should be treated as a failed qualification fixture, not a deployment-ready implementation.** Repair it within the existing ecosystem rather than installing it and discovering these defects against a live service.

This is not a blanket judgment on every repository or all work performed in that Forge session. The strongest conclusions concern the exact caller, reusable nightly workflow, branch JSON and Blueprint that the session read back. Later source states and live deployments require separate receipts. [S032; S033]

## 1. The real scope is an API-driven local/managed lifecycle

E001 calls for the dev backend to join the desktop, for an eight-hour OR greater-than-one-new-commit cadence, and for production to require maximal CI strictness plus another trio-style run before final confirmation. E002 asks for managed-service-like ergonomics on the local node. E003 explicitly keeps the application/GUI layer in BytePort and asks for plans at the API/automation layer. E004 names the existing ecosystem and recalls PhenotypeActions as a possible home for GitOps work. E005 preserves the runtime and GitHub plan preference.

Consequences: a second GUI is outside scope; a second managed Render dev service is not the requested default; a generic local process launcher is insufficient; and “project agnostic” cannot mean every repository is a web service. CLI packages, libraries, desktop releases and documentation have different delivery outputs. The portable object is a typed application/environment contract with provider bindings—not a promise of identical implementations everywhere.

The domain/tailnet feedback in E006 further favors private access for internal services. Public reachability is an explicit exception. A polished API should handle lifecycle and evidence without requiring the human to paste tokens into ad hoc commands. These are design requirements, not claims that the current products already provide them.

## 2. The candidate trio is recoverable, but not yet trustworthy authority

The prior CI audit identifies `ci / lint`, `ci / test` and `CI`; a current connected read of Tracera’s CI file independently shows those job-name declarations. Our v0.1 claim that the members were unavailable is therefore superseded. However, the historical protection JSON records `ci/lint` and `ci/test` without spaces. Normalizing those names is not harmless if the enforcing system expects exact check contexts. [E008; E013; S034]

There is a second problem: names are not execution coverage. The fetched final `CI` aggregate lists dependencies including `detect-changes`, `dependency-review` and `trunk-check`, but its result-checking array omits those three. The displayed aggregates reject failure/cancellation but do not themselves require an explicit reason for a skipped dependency. Some skips may be valid path-based exclusions; production requires evidence that they were intentional and sufficient, not a universal skipped-equals-success rule.

Resolve actual check-run/context identifiers and trusted app/workflow provenance against the exact candidate. The list must come from the current policy and observed GitHub results, not merely job names or a JSON file. A stricter production rerun must exercise the candidate and required coverage; renaming a green aggregate is not a rerun.

## 3. GitHub cannot call the stored reusable-workflow path as written

The recovered caller references `.github/workflows/reusable/nightly-dev-deploy.yml@main`. GitHub documents reusable workflow files directly under `.github/workflows`; subdirectories are unsupported. A YAML parser can parse the file while the platform rejects the workflow reference. This is a semantic qualification failure. [E007; E009; S036]

The connected exact-path lookup also returned 404 during this audit. That is a separate observation: it does not prove the historical local file was never written or that no valid renamed replacement exists. Repair must first locate the canonical shared implementation, then version/pin a supported caller path and verify actual resolution.

## 4. The candidate being tested is not bound to the image being deployed

E010 defines `runtime: image` and an image tag ending in `:latest`. E009 checks out the caller’s source, runs configurable build/test commands, then triggers a Render deploy with `commitId`. It does not publish the image produced from that source or select its immutable digest. Render distinguishes Git-backed commit selection from deploying an existing image. [S037; S038]

Even a successful local build would therefore not establish that the runtime uses those tested bytes. The repair is not “add a commit label”: select a source mode, build once, publish an immutable artifact, record source/build provenance, and bind deployment and approval to its digest. Promote that same digest across eligible environments. For Git-backed managed builds, capture and verify the provider’s resulting artifact/revision instead of claiming prebuilt-image semantics.

The Blueprint also declares automatic deployment on the purported manual fallback and includes unsupported-by-this-evidence OIDC comments. Treat those as unverified configuration claims. The visible nightly uses a bearer API key; a comment does not establish an OIDC trust exchange or disable alternate deployment paths.

## 5. Failure handling is not rollback

The complete 205-line nightly implementation polls for live state and performs a health request. Its failure paths exit nonzero. There is no stored previous deploy ID, invocation of a rollback action/API, data compatibility decision, or post-recovery observation in that recovered file. [E009]

A nonzero job conclusion is useful but does not undo a deployment. The Render rollback API is a separate operation referring to a previous deployment, and invoking it does not inherently disable future automatic deploys. App-level recovery additionally depends on schema/data compatibility. [S039]

The design now separates failed promotion, recovery requested, recovery in progress, recovery observed and service still unknown. Restoring executable bytes is not sufficient when a migration has changed the database. A recovery receipt must describe both code/config and data state.

## 6. The trigger silently changes the requested policy

The user requested every eight hours OR **more than one new commit**. The caller has every-eight-hour cron plus every `main` push. The callee only compares the live commit to the checkout SHA. One new commit can therefore trigger deployment; no commit-count threshold is evaluated. The comment stating that every push naturally implements `>1` is false. [E001; E007; E009]

The comparison also presumes that the provider can supply the relevant live source identity. The listing reads only 20 deployments, assumes a response shape and treats no matching live commit as a reason to deploy. Missing/unknown provider state should not become approval. Pagination and recorded response fixtures are required; this audit does not claim a specific alternative JSON shape was proven. [S051]

A typed scheduler and reference truth table now preserve the literal threshold, use a last **observed healthy** candidate as the watermark, reject unknown/divergent ancestry, coalesce offline work and separate eligibility from authorization. Time-based eligibility is not a hard guarantee of execution while a desktop is unavailable.

## 7. Health, secrets and fallback storage need qualification

The caller uses `/health`; the Blueprint configures `/healthz`. Both could exist, but no contract or test proves that. Worse, the nightly exits successfully when it cannot resolve the service URL, skipping health validation. Unknown observation cannot produce a healthy promotion receipt. [E007; E009; E010]

The caller explicitly forwards only `RENDER_API_KEY`, while the callee needs a service ID through an input or secret. A configured environment secret could satisfy that dependency, but its presence was not established. Repository secrets are not automatically forwarded merely because a called workflow names them. Validate the actual secret-delivery contract without displaying values. [S036]

Build/test command strings run in the same job that exports provider credentials. That enlarges the trusted code surface. Separate untrusted or general build execution from the actuator’s credentials, then verify provenance at the boundary. The Blueprint’s static authentication values and in-memory SQLite settings are unsuitable defaults for a durable reusable fallback. Selected evidence redacts those values; their presence does not establish live compromise.

## 8. Stored output completeness needs its own audit

The initial workflow report repeatedly says 24 files while listing 25 rows. It also mixes runner labels and deployment environments in its prose. A later compaction frame calls the pilot production-ready while a readback shows modified/untracked manifests and the defects above. These are specific examples of summary drift—not grounds to assume every report is wrong. [S032; E011; E016]

The report-recovery map distinguishes exact write payloads, partial reads/patches and no direct body recovered. Both final Free/student and Podman/WSL/PaaS follow-up audit bodies remain unfinished or unrecovered in the retained contexts. A descendant’s VSOCK “stable” verdict relies on lack of negative evidence and should not be promoted to compatibility proof. Podman’s documented networking primitives do not establish that the proposed inter-service path uses VSOCK at all. [E014; E015; S041]

## 9. External corrections do not erase the user’s requirements

Render’s free-service budget is not literally a one-service rule; its documented shared hours and storage limits still matter. Correcting that misconception does not change the user’s selected local-dev placement. LocalStack’s March 2026 transition changed image/access distribution; the product did not disappear. A replaceable local API surface can use focused emulators for tests and actual durable services for stateful work, with separate claims and tests. [S040; S043–S047]

## Recommended order

Resolve authority and active revisions; repair the platform-invalid workflow call and exact check coverage; specify one local service profile; prove the event predicate and trusted build/apply boundary; then qualify one private route and real recovery. Add a managed binding only after its source mode, state, identity and recovery behavior are explicit. The goal is one demonstrated end-to-end path, not another completed-looking stack diagram.
