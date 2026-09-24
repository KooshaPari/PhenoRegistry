# Qualify a new product check

Bind the criterion to one subject slice, method, explicit expected behavior, environment, fixtures, units/anchors, resource cap, permitted side effects and invalidators. Find a valid witness and a meaningful broken witness. Establish why those witnesses are appropriate rather than copying the implementation expectation.

Run both under the same relevant conditions. The good witness must be accepted and the bad witness rejected. Include a no-op or zero-assertion control where that failure is plausible. For stateful behavior inspect actual resulting state, not just exit codes. For nondeterministic systems preserve trial count, seeds, distributions and uncertainty. Use consumer effects, references, properties or anchored semantic review as appropriate.

Record qualifications and raw evidence. Protect high-risk oracle inputs through actual filesystem/process permissions; prompt separation alone is insufficient. A material method, threshold, fixture or environment change invalidates qualification according to the binding. Correct an invalid grader through a new epoch. Never edit old failures into passes.

Activate only within the proven scope. A single synthetic witness does not establish full coverage of a production system or reliability across every input.
