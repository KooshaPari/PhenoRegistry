# Formats, provenance, and integrity

## Canonical inputs and generated views

There is one authoritative input for each local fact/record. JSON is the exchange/default input in this implementation. `dossier.json` supplies contextual interpretation; `assignment.json` defines scoped obligations; `assessment.json` indexes exact result, evidence, and qualification records; those records contain their own state.

Human-readable MD/HTML and normalized JSON/YAML/JSONL are generated, not separately maintained. `views/build.json` records renderer/reducer/schema digests, a normalized input-list digest, every input file's byte digest, and every output's byte digest except its own. A receipt cannot contain its own finalized hash; the outer manifest covers it.

`verify` regenerates the expected views in memory and compares exact UTF-8 bytes. It therefore catches a stale report even if someone updates a separate file manifest to match the altered report. It cannot resist an adversary who can replace the trusted inputs, renderer, manifest and verification environment together.

## Four identities, no circular SHA problem

1. **S — Subject:** source commit or tree plus relevant uncommitted patch, build artifact, dependency/BOM and environment identities.
2. **A — Assignment:** exact locked assignment bytes and criterion/evaluator/profile versions.
3. **R — Report:** later commit or artifact containing the dossier produced from S under A.
4. **L — Ledger:** later independent registration receipt referencing S, A, R and bundle digest.

For these generated examples, no source/report/registry Git commits were created. They are null or explicitly absent. Actual fixture bytes and descriptors have real computed SHA-256 values. A hash of a fictional case descriptor is not misrepresented as a hash of nonexistent product source.

Time fields remain role-specific. `as_of` is the evidence cutoff. An illustrative authored premise's timestamp is a recording timestamp, not proof a product event happened. Device clocks are not a consensus protocol; use causal links and trusted receipts where chronology matters.

## Exact hash profiles in this package

- **File integrity:** SHA-256 over exact file bytes, with identifiers prefixed `sha256:`.
- **PEP value digest:** the inherited Python profile serializes JSON with sorted keys, compact separators, UTF-8, preserved strings, and rejection of non-finite numeric constants.
- **That profile is not RFC 8785/JCS.** Merely sorting JSON keys is not a general JCS implementation. JCS specifies particular number serialization and UTF-16 property ordering. A multi-language signing profile should use a conforming implementation, pin its version, and pass common canonicalization vectors before migration. [S1]
- **YAML:** never hashed as interchangeable with JSON. YAML exports have their own byte hashes. Changing YAML formatting may change bytes without changing its parsed meaning; explicit normalization is required before semantic content addressing.
- **Manifest:** covers all distributed files except itself; explicit ignored scratch/cache folders are not product evidence.
- **Outer ZIP checksum:** supplied separately. It detects corruption relative to the expected checksum but is not an authenticated signature.

Do not silently replace the PEP digest algorithm with JCS in an existing assignment. A migration must preserve old identities, declare the new digest profile and link the two by an explicit conversion record.

## Attestations and packaging

A signed attestation can bind named subjects and digest maps to typed assertions, as illustrated by the in-toto Statement model. This package does not issue an in-toto attestation or claim to possess a trusted signing identity. Future integration must use an actually authorized signer and verifier policy, not a synthetic key disguised as institutional authority. [S3]

Manifest-based file packaging has established precedents such as BagIt. This package adopts the useful idea of explicit payload integrity, but is not a BagIt bag and does not claim RFC 8493 conformance. Use a real adapter when interoperability with that format is needed. [S2]

## Concurrency, custody and retention

Use immutable per-assessment or per-producer records rather than many agents rewriting one shared file. A central index is a rebuildable projection. Shared acceptance needs actual compare-and-swap, locks or leases supplied by the host/registry; a YAML field does not enforce one.

Avoid silently following symlinks or escaping evidence paths. Run validators against a quiescent authorized snapshot: the included path checks are not an adversarial race-proof filesystem sandbox. Private raw evidence belongs in the authorized evidence store. A public dossier can reference a redacted derivative with provenance while reporting that the verifier lacks the original. It must not claim full offline reproducibility when required payloads are absent.

Keep drafts mutable; seal accepted snapshots. Corrections append superseding records and a new accepted baseline. Registry retries use stable idempotency keys and carry actual delivery state. A pending outbox entry is not a receipt.

## Implementation and limits

`tools/dossier.py` uses the retained core for record/bundle semantics. Its additional schema validates context shape; its code validates exact row coverage, finding/decision references, subject-descriptor hashes, example evidence classes, and render outputs. The core itself supports only its documented subset of JSON Schema. Release tests also cross-check records with an independent JSON Schema implementation where installed.

Authenticity, legal compliance, empirical product validity, causal completeness, model independence, network safety and multi-device consensus are not established by those tests.

Sources: [S1–S3](SOURCES.md).
