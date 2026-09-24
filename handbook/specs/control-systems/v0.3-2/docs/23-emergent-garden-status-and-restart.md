# Emergent Garden corpus — actual status and restart packet

## Current status

This work **did not merely fail and disappear**. The exact ResearchLedger PR-81 head contains substantial Wave 5 research and executed package validation. PR 81 reports 70 offline tests rerun after extraction, 32 synthetic admission cases, 74 public uploads reconciled and explicit remaining gaps. S061, S062.

But the integration state is bad:

- ResearchLedger PR **#81 is closed, draft and not merged**. S061.
- The reviewed current `main` snapshot did not expose `docs/corpora/emergent-garden/research/README.md` at that path. S063.
- phenotype-registry PR **#550 did merge** a routing projection pointing at the pinned ResearchLedger evidence head. S064.

So the failure is primarily **source-authority integration**, not absence of research output.

## Do not restart from YouTube

The first action should preserve the exact PR-81 head and published artifact/hash records, compare its tree against current main, and decide whether to rebase/cherry-pick/reconstruct a minimal new PR. Do not redo the crawl just because the original PR is closed.

## Restart sequence

1. Pin `8822aa14baef2a964288076645edcc493c338688` and the publication artifact/hash from PR 81.
2. Diff its corpus paths and supporting scripts against current ResearchLedger main.
3. Classify conflicts as already-landed elsewhere, superseded, still-needed or stale.
4. Rebuild a clean source-authority integration branch from current main containing only still-valid records/tools.
5. Rerun the corpus bundle verifier, all 70 offline tests and synthetic admission cases; record any changed denominator rather than forcing the historical counts.
6. Land or explicitly supersede the source authority.
7. Update/qualify downstream projections such as phenotype-registry routing.
8. Only then continue independent remaining research lanes.

## Remaining lanes are independent

The branch itself says these remain open: full transcripts, exhaustive audience semantic review, broad recursive nested-source closure, complete historical behavior/lineage reconstruction, the persistent one-comment discrepancy and a live coordination/Benchora experiment. S061, S062.

Do not roll these into one giant "finish corpus" percentage. Each receives its own evidence denominator and stop condition.

## Authority

ResearchLedger remains the source/claim authority. Downstream project comments and registry links are bounded projections, not permission to alter product behavior automatically. The corpus can inspire hypotheses; it does not prove that more agents, a particular emergent architecture, or any transferred technique improves a target project until an experiment does so.
