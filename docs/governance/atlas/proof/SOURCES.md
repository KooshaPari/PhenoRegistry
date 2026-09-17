# Source and verification boundaries

This is a targeted source/reference review to refine contracts, not a new all-repository audit. No graphical app, native bridge, game, Steam identity or deployed service was run. The March-dated Dino matrix is historical even though the file was retrieved at a later source revision. An initialized system or enqueued command is weaker evidence than the visible behavior its story promises.

## SRC-V14-01 — Dino GameControlCli project

Source: https://github.com/KooshaPari/Dino/blob/17119051e782b32615413049c1c3cd207f0b540e/src/Tools/GameControlCli/GameControlCli.csproj

Connector search confirms existing named-pipe game-control CLI. Reuse/investigate; no execution here.

## SRC-V14-02 — Dino QA validation matrix

Source: https://github.com/KooshaPari/Dino/blob/17119051e782b32615413049c1c3cd207f0b540e/docs/QA_VALIDATION_MATRIX.md

Fetched source is explicitly last validated March 30, 2026. It distinguishes some visual/runtime failures, but also labels some visible-feature claims programmatic from initialization logs. Treat as historical evidence taxonomy needing refresh, not current bug/grade measurement.

## SRC-V14-03 — Civis capture guide and stub

Source: https://github.com/KooshaPari/Civis/blob/8650471500928f047370585d8fe5c43275b18aaf/scripts/capture/README.md

Search identifies this path as planned/stub capture helpers; does not imply no other working capture exists. Existing dispatch instructions separately require reading actual PNGs.

## SRC-V14-04 — Playwright visual comparisons

Source: https://playwright.dev/docs/test-snapshots

Official guidance on screenshot baselines and rendering environment variability; use pinned supported versions.

## SRC-V14-05 — Playwright screenshots

Source: https://playwright.dev/docs/screenshots

Official full-page, buffer and element capture primitives.

## SRC-V14-06 — Bevy externally driven renderer

Source: https://github.com/bevyengine/bevy/blob/main/examples/app/externally_driven_headless_renderer.rs

Official example of externally driven offscreen rendering; current main is a research source, not a pinned production dependency.

## SRC-V14-07 — Bevy headless renderer

Source: https://github.com/bevyengine/bevy/blob/main/examples/app/headless_renderer.rs

Official example includes GPU-image readback and render/main-world frame-latency concerns. No renderer execution here.

## SRC-V14-08 — Godot viewport capture

Source: https://docs.godotengine.org/en/stable/tutorials/rendering/viewports.html

Viewport texture capture and waiting for rendering are relevant primitives; verify actual shipped backend.

## SRC-V14-09 — Unreal Automation Test Framework

Source: https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine

Official framework distinguishes unit/feature/content/screenshot tests and input/functional testing facilities.

## SRC-V14-10 — Unreal screenshot comparison

Source: https://dev.epicgames.com/documentation/en-us/unreal-engine/screenshot-comparison-tool-in-unreal-engine

Official settings include tolerances, camera/resolution, noisy-feature handling and diagnostic buffers.

## SRC-V14-11 — Unreal automation execution

Source: https://dev.epicgames.com/documentation/unreal-engine/run-automation-tests-in-unreal-engine

Official client/editor execution and report export facilities; editor success is not automatically packaged-client proof.

## SRC-V14-12 — Unity Test Runner

Source: https://docs.unity3d.com/kr/2018.3/Manual/testing-editortestsrunner.html

Historical official documentation establishes Edit/Play/target-player distinction. It is not a current package-version recommendation. Inspect installed package docs before command selection.

## SRC-V14-13 — W3C accessibility evaluation tools

Source: https://www.w3.org/WAI/test-evaluate/tools/selecting/

Tools assist evaluation but cannot determine all accessibility aspects; qualified judgment remains needed for some criteria.

## SRC-V14-14 — Supplied v1.3 archive

Source: ../references/v1.3-input-identity.json

Previous package is preserved externally and identified by digest in this amendment; prior policies and 24 owner folders are retained, not a live refreshed census.

All numerical examples added in v1.4 are synthetic. Grading weights/letters are proposed policy, not empirical industry standards. Source platform features do not establish that any Phenotype adapter correctly uses them.
