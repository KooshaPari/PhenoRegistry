# Integration contract and adoption

The [36 work items](adoption-work-items.json) are proposed templates, not accepted portfolio work or completed changes. Populate assignment, evidence, authority, budget and actual claim fields before importing. Local agents may own all roles.

## Logical interface, not invented API

A qualified adapter maps an owner-held record to the destination's actual supported contract. Resolve current endpoints, permissions, package versions, identifiers, response/error semantics and concurrency behavior through the live system or installed source. This kit intentionally supplies no guessed AgilePlus/Tracera endpoint or install command.

Input: record/schema revision, subject/epoch, owner, event ID, allowed payload, payload digest, idempotency key, actual authorization and expected destination version where needed. Output: real accepted/rejected/conflicted state, destination ID/version, returned receipt and audit-safe error. Record attempts; do not convert transport success into domain acceptance.

For at-least-once transport, replay preserves identity. Actual destination semantics must prevent repeated irreversible effects. No local JSON field alone supplies compare-and-swap, exactly-once effects or a fencing lock. When unavailable, serialize affected acceptance and keep queued delivery visible.

## Owner boundaries

Subject owners retain intent, requirements, results and findings. AgilePlus may govern execution work and claims. Benchora or the accepted evaluator owner holds qualified check implementations. Tracera may project evidence/trace relations. RepoLedger or the accepted registry instance owns identity/disposition references. ResearchLedger records sources; SessionLedger captures runs; PhenoDocs renders. Verify these boundaries against actual accepted policy before writes.

A tool repository hosts tool code, tests, documentation and labeled demonstrations—not arbitrary live consumer records. An index is a rebuildable projection, not a competing authority. The file-first fallback and live adapter must read the same logical records; never fork ownership to make both look canonical.

## Adapter qualification cases

Success; missing authority; malformed version; stale expected version; duplicate replay; conflicting payload for same key; crash after effect before receipt; offline queue; redacted private payload; wrong subject SHA; independent verification of acknowledgement. Each applicable case must produce an honest result and recoverable next action. A failed adapter blocks that integration, not the rest of the lab.
