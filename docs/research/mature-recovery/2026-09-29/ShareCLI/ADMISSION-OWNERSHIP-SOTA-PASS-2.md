# ShareCLI admission/ownership SOTA — pass 2

Date: 2026-09-30. Product source remains `4f01d0199e82b62bcf20399afcc102f58a10ad07`.

## Native jobserver before generic queue duplication

GNU make's documented jobserver protocol exists specifically to cap total parallel jobs across recursive/multi-process tool execution.

Current GNU documentation states:
- children discover jobserver access through the last `--jobserver-auth=` entry in `MAKEFLAGS`;
- POSIX uses FIFO or pipe token transport;
- Windows uses a named semaphore;
- every launched command has one implicit slot;
- extra slots are acquired as tokens and the exact acquired token/count must be returned, including under errors/interrupts;
- tools should detect conflicts between their own parallelism limits and inherited jobserver controls.

Sources retrieved 2026-09-30:
- https://www.gnu.org/software/make/manual/html_node/Job-Slots.html
- https://www.gnu.org/software/make/manual/html_node/POSIX-Jobserver.html
- https://www.gnu.org/software/make/manual/html_node/Windows-Jobserver.html

The Rust `jobserver` ecosystem also exposes explicit child-command configuration so the inherited protocol is propagated rather than merely naming jobserver settings.

Source:
- https://docs.rs/jobserver/latest/jobserver/struct.Client.html

**ShareCLI consequence:** SC-AD-03 should treat native jobserver participation as the preferred admission provider for compatible build families. A second independent SlotQueue around the same nested build can create double-throttling or semantic disagreement. Custom admission remains justified for workload families with no suitable native provider or for cross-family policy above native providers.

## Process identity stronger than integer PID

Linux `pidfd_open` creates a file descriptor referring to a task and can be polled/waited for exit. Kernel/user-space documentation describes pidfd as the preferred way of obtaining a process file descriptor for an already-existing process.

Source:
- https://www.man7.org/linux/man-pages/man2/pidfd_open.2.html

**ShareCLI consequence:** on Linux, a generation-safe ownership implementation should compare pidfd/process-handle style primitives against inventing persistent PID-generation heuristics. A stale queue ticket containing only PID cannot become authoritative merely because that numeric PID currently exists.

This does not define the cross-platform abstraction by itself:
- Linux candidate: pidfd/task handle;
- Windows candidate: native process handle + creation identity;
- macOS requires its own stable-process-generation research;
- durable lease identity above process lifetime still needs a product-owned generation/lease token.

## Refined admission architecture

`AdmissionProvider` should support distinct provider types:

1. `NativeJobserver`
   - attach to existing protocol;
   - borrow/return tokens;
   - propagate to eligible children;
   - report provider identity/auth surface.

2. `ProductLeaseProvider`
   - ShareCLI-owned lanes for workloads lacking a native provider;
   - durable lease/generation identity;
   - dead-owner reclaim;
   - fairness policy;
   - restart behavior.

3. `OSResourceProvider`
   - policy/refusal/throttling using native resource controllers/signals;
   - separate from logical queue order.

4. `CompositeProvider`
   - explicit composition where one provider cannot represent all accepted policy;
   - must define which provider is authoritative for each constraint.

## Architecture attack

The current filesystem ticket queue combines:
- concurrency slots via OS flock;
- waiter priority;
- stale-owner inference;
- wall-clock aging;
- FIFO encoding.

That is more custom responsibility than the product thesis requires.

Potential simplification:
- keep OS lock/token primitives for local exclusion;
- represent ShareCLI-owned waiter/lease identity explicitly;
- use stable process handles where available for liveness;
- use native jobserver for eligible nested builds;
- isolate priority/fairness policy from filename ordering;
- avoid making wall-clock timestamps ownership authority.

## Required experiment

Compare one real nested build family under:
A. native jobserver only;
B. ShareCLI SlotQueue only;
C. explicit composition.

Measure:
- peak real concurrency;
- completion time;
- token/slot leakage after error/interrupt;
- nested-child behavior;
- double-throttling;
- recovery after caller replacement.

No implementation is selected by this pass.
