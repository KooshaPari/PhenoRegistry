# Closest Viable Product (CVP)

A CVP is the minimum slice of a product that:

1. **Is naming something people can use** — not a roadmap slide, not a future
   promise, but a thing that exists and runs.
2. **Carries the product's identity** — if you swap it for a competitor, the
   user notices the loss.
3. **Survives end-to-end through one real user journey** — even if rough,
   incomplete, or behind feature flags.
4. **Is the smallest path to the next user-driven learning** — every other
   feature is justified by what the CVP teaches us.

A CVP is *not* an MVP. MVPs optimize for "ship something to validate demand".
CVPs optimize for "ship the smallest thing that still expresses the product".

## Why "Closest" and not "Minimum"?

The word "closest" matters. A CVP is **closest to the product's actual
identity**, not closest to a horizontal slice. A CVP is allowed to be ugly,
incomplete, behind feature flags, or single-user. It just has to be the
version that best expresses *what this product is at its core*.

Concretely: the difference between a CVP and an MVP for the same product might
be 1 feature. That 1 feature is the one that, if missing, would make the
product indistinguishable from a generic competitor.

## When to use CVP

- During build-out, when scope is up for negotiation.
- When evaluating whether a feature is worth shipping soon or deferring.
- When explaining to a new contributor what the project actually *is*.
- When pushing back on scope creep: "is this in the CVP, or is it post-CVP?"

## When **not** to use CVP

- Early idea validation (use MVP, spike, or design doc instead).
- Internal tools where "smallest thing that works" really is the only goal
  (CVP is overkill; just build it).
- Products that are intentionally thin wrappers (CVP = the wrapper).

## CVP doc structure

Each CVP doc lives at `docs/cvp/<repo-or-product>.md` and follows this
template:

```markdown
---
repo: "<repo-name>"
status: "<active|deferred|shipped>"
last_verified: "<YYYY-MM-DD>"
owner: "<primary maintainer / agent>"
---

# CVP — <repo-or-product>

## Identity
<One paragraph: what this product *is*, stated as a noun not a feature list.>

## Closest Viable Product
<One paragraph: what the smallest living slice is.>

## In CVP (must ship in this slice)
<Bulleted list of capabilities.>

## Post-CVP (defer until CVP is live)
<Bulleted list of what's explicitly out.>

## Anti-CVPs
<Things that look like they belong here but don't — and where they live instead.>

## Open Questions
<Unresolved CVP-shape questions.>

## Change Log
| Date | Change | Worklog |
| ---- | ------ | ------- |
```

## CVP status

| Repo | Status | CVP doc |
| ---- | ------ | ------- |
| Tracera | active (build-deploy pending) | [Tracera.md](./Tracera.md) |

## See also

- [`docs/intent/`](../intent/) — long-form product intent.
- [`docs/boundary/`](../boundary/) — what each repo owns vs delegates.
- [`docs/SPEC.md`](../SPEC.md) — Phenotype Registry system spec.
