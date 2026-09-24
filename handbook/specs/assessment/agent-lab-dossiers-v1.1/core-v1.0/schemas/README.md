# Record schemas

Draft 2020-12 JSON Schemas for the 25 record kinds. The offline reference kernel implements only the shipped keyword subset, not general JSON Schema. Full-library cross-check results are recorded in the qualification report. Local references resolve inside this directory, never through the network.

- [amendment](amendment.schema.json)
- [assessment](assessment.schema.json)
- [assignment](assignment.schema.json)
- [attempt](attempt.schema.json)
- [catalog](catalog.schema.json)
- [census-item](census-item.schema.json)
- [checkpoint](checkpoint.schema.json)
- [claim-lease](claim-lease.schema.json)
- [claim](claim.schema.json)
- [criterion](criterion.schema.json)
- [crosswalk](crosswalk.schema.json)
- [decision](decision.schema.json)
- [evidence](evidence.schema.json)
- [feedback](feedback.schema.json)
- [finding](finding.schema.json)
- [intent](intent.schema.json)
- [mandate](mandate.schema.json)
- [measurement-binding](measurement-binding.schema.json)
- [outbox](outbox.schema.json)
- [profile](profile.schema.json)
- [qualification](qualification.schema.json)
- [receipt](receipt.schema.json)
- [repo-genesis](repo-genesis.schema.json)
- [result](result.schema.json)
- [work-item](work-item.schema.json)

## Three levels

Shape validity means the fields match a schema. Bundle consistency additionally checks selected links, identities, timestamps, digests and evidence-state reductions. Neither authenticates external facts, authority or semantic correctness. Generic records such as intent and decisions do not receive universal cross-record graph validation in the reference kernel.

`TEMPLATE` records are starting forms. `EXAMPLE` records are labeled demonstrations. `OPERATIONAL` records require real context and reject the packaged placeholder convention. Record status is still caller-supplied data; it is not an authorization signature.

Assignment/assessment/result/evidence/qualification working examples are in [the toy bundle](../examples/README.md). Use the initializer for blank assessment records. The exact byte digest of assignment.json is required in assessment and results; reserialization changes that digest and requires a new consistent record set, never silent reuse.

## Offline identifiers

Schema IDs use the reserved namespace `https://schemas.phenotype.invalid/pep/1.0.0/`. This is an identifier, not a hosted service. A general validator must pre-register the bundled schemas by those IDs; all references resolve from local resources. The reference kernel loads allowed relative references directly from this directory and performs no network retrieval.
