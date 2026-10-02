# Pass 11 — v1 obligation expansion and interaction attack

Date 2026-09-30.

Pass 10's valid counterexamples are now represented as distinct obligations, propagated into journeys/stage semantics and mapped into trace gaps. No mechanical dimension multiplication was used.

## Portage

New obligations P-OB-011..017 cover scoped authority, evidence lifecycle, idempotent/causal delivery, immutable dependency identity, criterion-level validity, cancellation/late-event terminal policy and imported observations.

Interaction rules now explicit:
- authorized late evidence cannot resurrect a cancelled attempt;
- authorized duplicate event is still duplicate;
- disposed evidence can make future regrade legitimately unavailable;
- imported result cannot be laundered into local verified observation.

Receipts: obligations `770bf6646fde6274835711b04237cef55e48ccb9`; journey delta `480740d6b275285916803240ad0223868107dbb1`; trace delta `5de02752d73bdf3009fd163637265d618493a355`.

## PhenoMLX

New M-OB-012..020 cover requested vs realized profile, distributed placement, remote cache/security domain, runtime generations, partial streams, support vs admission, dynamic operating state, support lifecycle and truthful observability.

Interaction rules:
- fallback invalidates incompatible cache/evidence identity;
- endpoint hot swap cannot relabel in-flight streams;
- support does not guarantee instantaneous admission;
- rollback cannot reconnect incompatible/unauthorized cache state;
- opaque remote internals constrain claim scope;
- deprecation preserves history but not current support.

Receipts: obligations `026e7d416373dd9aac5fa1d536eb54dc4cb70ffc`; journey `02ee3b83cfa7d02be14d1fd7ec398e4598cbd270`; trace `8b60186f2d81eba3e62a23a3cdfaeeadc39545e0`.

## PhenoLab

New L-OB-015..026 cover candidate lineage/rebase, assignment epochs, evaluator roles/query budgets, environment epochs, causal attribution, optimizer capabilities, observation windows/evidence age, rollback viability, human decisions, realized organization, imported experiments and replicate uncertainty.

Interaction rules:
- candidate crossing policy epoch must be explicitly historical or re-evaluated;
- human override cannot become a holdout leakage channel;
- acceptance machinery is outside optimizer capability or changing it creates new epoch;
- post-promotion regression attribution must consider environment drift;
- rollback targets are accepted subject revisions, not arbitrary Git SHAs;
- replicates bind realized organization;
- human action on imported evidence does not make it locally reproduced.

Receipts: obligations `0a706d7b7fb5b0c5e72e158a6bb71b825166e517`; journey `d75329923083f2dbd500827de9366212f9ad6727`; trace `98bdb29b7c77628ba1550ae77191b49cadd50d3f`.

## Program state

The interaction attack did not falsify the new identities themselves, but it added transition/authority rules necessary to prevent individually valid mechanisms composing into false greens.

Ontology remains DRAFT. The next useful step is not another generic semantic brainstorm: perform a **second implementation mapping pass** against actual storage/API/CLI/UI/runtime surfaces for these v1 identities, then decide which gaps are true product obligations versus delegated integration contracts. This will also expose whether any v1 concept is over-modeled.

No completion percentage or CVP qualification.
