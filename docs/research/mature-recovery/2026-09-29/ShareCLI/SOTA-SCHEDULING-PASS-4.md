# ShareCLI SOTA scheduling pass 4 — backfill, native admission, speculation

Date: 2026-09-30.

## Slurm backfill

Slurm distinguishes fast event scheduling from a more comprehensive backfill loop. Backfill may run lower-priority work only when it will not delay higher-priority expected starts. It depends materially on resource requests and reasonable runtime estimates.

Implications:
- ShareCLI SchedulingPolicy should distinguish strict priority/FIFO from backfill.
- Estimated duration is a first-class optional WorkItem attribute with provenance/confidence.
- Unknown duration must degrade backfill opportunity rather than invent an estimate.
- Reservation/time-horizon planning is distinct from immediate placement.
- scheduler computation itself has an overhead/responsiveness budget.

Decision: **ADAPT semantics/algorithms; do not embed Slurm.**

## GNU make jobserver

GNU jobserver coordinates parallelism across nested cooperating tools. POSIX uses FIFO/pipe token transport; Windows uses a named semaphore. Participants must return acquired slots even on error.

Implications:
- NativeJobserverProvider is strongly justified.
- ProductLeaseProvider should coexist for tools that cannot participate.
- Nested tools must not be double-throttled.
- lease/token accounting and error cleanup are hard correctness invariants.

Decision: **INTEGRATE when detected; do not replace with ShareCLI lease merely for uniformity.**

## Bazel dynamic execution

Bazel can race local and remote execution of the same action, accept the first successful result and cancel the loser; delays can avoid waste when remote cache hits are expected.

Implications:
- SpeculationGroup is production prior art, not speculative scope invention.
- ShareCLI needs explicit race eligibility, delay policy, cancellation semantics and wasted-work accounting.
- racing is valid only when action equivalence/result semantics are established.
- speculation quality must be measured against overhead/waste.

Decision: **ADAPT as one later strategy after deterministic scheduling spine.**

## Nomad

Nomad defaults to bin-packing and supports affinity/spread plus device requirements such as GPUs.

Implications:
- ResourceVector should support discrete devices/capabilities, not only scalar CPU/RAM.
- placement has feasibility filtering followed by scoring.
- packing and spreading are policy alternatives.

Decision: **LEARN FROM placement architecture.**

## Revised scheduler strategy set

Baseline:
- naive all-at-once;
- bounded FIFO.

Candidate deterministic:
- best-fit/binpack;
- priority;
- backfill when duration estimates qualify;
- fairness/DRF-inspired;
- device/capability-aware placement;
- pressure-aware admission/replan.

Later:
- speculation/dynamic execution;
- learned/predictive strategy only after deterministic baselines.

## New obligations implied

- WorkItem estimated duration + provenance/confidence.
- ResourceVector discrete capability/device requirements.
- SchedulePlan reservation/time-window representation where strategy uses it.
- Scheduler computation overhead receipt.
- native jobserver detection/composition.
- speculation delay/budget/waste/cancel receipt.
