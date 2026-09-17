# Melosviz — next bounded outcomes

**Updated:** 2026-09-17 (post-v0.1.0). The existing owner continues valid work, not a new audit from zero. These are priority recommendations; actual permission, prerequisite and resource checks still apply.

## Backlog: carry-forward (still open)

1. **Type and label backend outcomes** (`CUR-1262466303-A1`) — Separate live render, placeholder, job-spec-only, unavailable and failed outputs; ensure release/product acceptance cannot silently consume fixture output as production. Acceptance: known absent backend, failed render and malformed/zero-duration media are rejected or explicitly blocked; rehearsal stays runnable.

2. **Run real creative output** (`CUR-1262466303-A2`) — Import an actual licensed audio track, use the intended available renderer, edit the scene/preset, export and inspect audio/video synchronization and content. Acceptance: real output reviewed, not only a ZIP/nonempty file; actual run parameters and derivatives are traceable.

3. **Qualify installation and comparison** (`CUR-1262466303-A3`) — On a clean machine outside the repository, install v0.1.0, create and reopen a project from real creative input, complete an export, and repeat the Melosviz workflow; compare it with a suitable established workflow. Acceptance: repeated Melosviz runs produce the same usable creative result; record installation/startup and time-to-useful-output, qualitative output differences, and CPU, memory, storage, and wall-time measurements. Fixture-only or source-tree success does not count.

## New post-release outcomes

4. **Clean-machine install smoke of v0.1.0** — Download the published `.dmg` and `.tar.gz` on a machine without the repo, launch the app, and confirm the packaged web frontend loads and a basic workflow runs. Acceptance: artifact is installable and runs outside the source tree; report any signing/gatekeeper or missing-resource errors. *(smallest gap between published artifact and verifiable installed product)*

5. **Wire the three skipped spec-first components** — Fullscreen toggle, playback transport, and scene jump panel exist as spec-first tests but are not yet wired into `App.tsx`. Acceptance: the 3 skipped web tests move to passing with no other regression.

6. **Document the v0.1.0 delivery contract** — Confirm shipped feature set matches release notes; amend `CHANGELOG.md` and `docs/` if the public claim exceeds what the artifact actually delivers.

## Do not lose the rest of the contract

Use the existing dossier and pilot as context, not proof. Maintain the explanatory atlas, complete intent/spec contracts, independent QA matrix, qualified failure oracles, actual release/install evidence, and consumer-aware reuse. Close source-target-consumer dependencies with their owners. The next small repair must remain linked to the parent outcome: The installed product produces and edits a real useful synchronized visualization, with honest backend modes.
