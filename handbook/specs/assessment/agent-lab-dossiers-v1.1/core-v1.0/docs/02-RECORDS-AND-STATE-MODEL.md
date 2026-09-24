# Records and state model

## Authoritative objects

A **subject snapshot** identifies actual source, dirty state, dependencies, artifacts and environment. An **intent** states a supported or hypothetical beneficiary outcome. An **assignment** locks the selected scope, catalog, measurement bindings, gates and epoch. A **criterion** defines a reusable predicate; an **instance** applies it to a specific scope. A **measurement binding** makes the method concrete. A **qualification** describes evidence that the instrument accepts a valid witness and rejects a meaningful invalid witness. A **result** reports an observation, verdict, review and freshness at a subject identity.

A **finding** is not automatically authorized work. A **decision** accepts, rejects or defers a next step. A **work item** describes its bounded outcome and dependencies. An **attempt** preserves execution and learning. A **checkpoint** gives a fresh worker durable state and negative knowledge. An **outbox** is delivery intent; a **receipt** is actual destination acceptance. A **claim lease** describes temporary ownership but requires a real fencing authority to enforce it.

## Orthogonal result state

| Dimension | Values |
|---|---|
| Applicability | APPLICABLE, NOT_APPLICABLE, UNRESOLVED |
| Execution | NOT_STARTED, RUNNING, COMPLETED, ERROR, BLOCKED |
| Verdict | PASS, FAIL, UNKNOWN, CONTESTED |
| Evidence freshness | CURRENT, STALE, INVALID, MISSING |
| Review | PROPOSED, ACCEPTED, WAIVED, CONTESTED |

The absence of a result is UNKNOWN, not FAIL or PASS. A crashed runner is ERROR with UNKNOWN product verdict. A product assertion failure is COMPLETED with FAIL. A waiver is visible but cannot masquerade as a pass. Evidence expiry makes an old result historical. Non-applicability requires an accepted rationale tied to capabilities, not merely a product label.

## Record lifecycle

Templates are `TEMPLATE`; toy records are `EXAMPLE`; real observations are `OPERATIONAL`. These labels are not security controls, but prevent accidental category confusion. Operational records may not retain `REPLACE_WITH_*` or zero-digest placeholders. Version history is append/supersede. Do not rewrite a failed past run into a success.

An assignment moves PROPOSED → LOCKED → SUPERSEDED. Locking requires a scope review reference. A new epoch changes acceptance meaning explicitly. Within an assessment, effective results are leaves of the supersession relation for each instance. Multiple competing leaves remain unresolved; the newest wall-clock timestamp does not settle their disagreement. Cycles and cross-instance supersession are invalid.

## Digest representation

Files use SHA-256 of exact bytes. The Python value helper uses UTF-8 JSON with sorted keys, compact separators, no non-finite numbers and no ASCII escaping. This is a named PEP Python representation, not RFC 8785/JCS and not a signature. Prefer exact file-byte digests at inter-language boundaries until a canonicalization profile is accepted. A rewritten file with equal semantic content can have a different file digest, intentionally.

Assignment byte identity is recorded by assessments and results. The assignment does not embed its own digest. Artifact and subject digests must identify the actual evaluated state, not a release label. The reference metadata inspector deliberately does not claim to produce a complete content snapshot.

## Schemas versus truth

Schemas validate record shape. Cross-record checks validate selected bindings and arithmetic. Neither confirms that observations are honest, authorities exist, cryptographic signers are trusted, or every implied obligation was discovered. Those claims need actual permission/evidence paths and qualified instruments. External references may require connector-specific verification; do not satisfy them with invented local strings.

## Epoch versus candidate snapshots

An epoch freezes acceptance meaning, not the editable product forever. Each candidate assessment has a new immutable assignment snapshot binding its exact tested subject. Before/after snapshots may share the logical epoch only when the material intent, criterion meaning, gates, weights, exclusions and measurement policy remain unchanged. A new source binding is not by itself a new acceptance policy. Preserve the comparison/bridge explicitly. The reference kernel validates one bundle at a time; it does not enforce global epoch uniqueness or compare policy meaning across a fleet.
