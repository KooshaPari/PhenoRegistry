# Pass 21 — native vertical frontier

Date 2026-09-30.

## What could be advanced without external runtime access

Portage CI receipts are now definitive for the latest persistence head: Ubuntu and Windows reach checkout/toolchain/container setup then fail at dependency installation; every test step is skipped. This is a stable infrastructure blocker, not a product-oracle result.

PhenoLab CI/mutation again fails before recorded steps.

PhenoLab source inspection closes an important ambiguity: its current bench CLI is explicitly deprecated in favor of Harbor, and the repo already includes a `harbor_consumer_dry_run.py` boundary. Self-test/dry-run/stub paths are useful plumbing checks but are explicitly synthetic/inferred and cannot qualify the architecture gate.

The existing EvaluationReport evidence contract already encodes this distinction, so the program will not count a cheap stub smoke as the requested native vertical.

## New boundary artifacts

Portage TrialResult bridge and mapping are already in Pass 20.
PhenoMLX backend availability/version receipt is already in Pass 20.
PhenoLab native vertical boundary is now explicit at `23bb64ac4e23442611804d3c9b871f8a3934b67c`.

## External prerequisites now exact

### Portage
Need a runnable dependency environment for the frozen/spec branch, then one actual Harbor trial whose TrialConfig/TrialResult/ArtifactManifest can be transformed by the thin envelope. Current GitHub CI cannot reach tests due install failure.

### PhenoMLX
Need one environment with at least two compatible installed engines and one common pinned model/hardware population. GitHub connector cannot execute GPU/model workloads. Static adapter receipts cannot substitute.

### PhenoLab
Need a real runner/Harbor execution producing qualifying EvaluationReport evidence. Self-test, dry-run, mock/stub, inferred/reported/historical evidence is deliberately non-advancing. Then typed Candidate/Epoch → gates → Assessment → Decision → restart can be exercised.

## Program decision

Do not fake the native vertical with mocks merely to advance the gate.

The semantic/specification program can continue in parallel on:
- source-coverage closure;
- exact schemas and vertical-slice contracts;
- independent review packet;
- CI/setup diagnosis from workflow/config source.

But **architecture baseline promotion remains blocked on real execution evidence**.

This is the correct stopping boundary for native claims given current connected tools, not a request for user permission.
