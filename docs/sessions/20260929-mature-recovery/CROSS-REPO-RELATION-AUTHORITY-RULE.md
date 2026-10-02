# Cross-repository relation authority rule

A discovered cross-repository edge MUST be typed before it can affect product ontology.

Allowed relation classes include:
- dependency/import;
- runtime integration;
- telemetry/observability sink;
- data producer/consumer;
- shared schema/protocol;
- optional adapter;
- historical migration;
- ownership/source-of-truth;
- authorization/decision authority;
- product composition;
- supersession/absorption.

**Integration does not imply ownership.**
**Telemetry does not imply product authority.**
**A shared schema does not imply canonical state.**
**A consumer does not imply subordination.**

Ownership/source-of-truth/authorization/product-composition edges require direct user intent, accepted ADR/spec, or equivalent authoritative evidence. Implementation imports/adapters alone are insufficient.

If evidence conflicts, preserve both claims and mark the authority edge unresolved rather than promoting the stronger relationship.

This rule was added after the PhenoLab↔Tracera recovery error, where a real trace-store integration was incorrectly promoted into a canonical-product-state relationship.
