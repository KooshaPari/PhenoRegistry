> **Authored by Instinct (Koosha’s pilot assistant), not by the CLI agent fleet.**

# Repository and portfolio repair plan: WBS / PERT

**Planning baseline:** September 25, 2026. **Status:** proposal from a bounded read-only audit, not an execution receipt or approved release plan. **Owner:** Koosha Paridehpour. This document belongs in the PhenoRegistry governance atlas as a cross-repository planning record, not a product-specific `STATE.md` or a claim that the repositories have changed.

## Decision frame

- **26 work packages**, 102.8 expected engineering hours in total.
- **Modeled critical path:** 0.1 -> 3.1 -> 3.3 -> 3.4 -> 3.5 -> 3.6 -> 6.1, 33.2 expected hours, assuming parallel workstreams, immediate reviews and no new work.
- **Finish-to-start dependency:** each `After` value must complete before the package begins. Workstreams 1-5 can proceed in parallel after 0.1; 6.1 waits for 1.5, 2.4, 3.6 and 5.6. Hours are engineering effort, not elapsed calendar time or a promise.
- **PERT formula:** expected hours = (optimistic + 4 x most likely + pessimistic) / 6. The O/M/P figures are provisional estimates. Delays from owner decisions, reviews, releases and newly found failures are not modeled.

## Public information boundary

PhenoRegistry is public. The PhenoLab stream below names only high-level review outcomes, dependency IDs and planning estimates. Private issue/PR IDs, credential examples, test failures, security details, and internal source content belong in the private repository or a restricted review record, not here. The outline does not certify an issue as fixed, a vulnerability as present, or a gate as enforced. Confirm each claim against the relevant live source before editing another repository or sharing it publicly.

## Work packages

| ID | Stream | Package and acceptance criterion | After | O / M / P (h) | Expected (h) | Earliest start-finish (h) |
| --- | --- | --- | --- | ---: | ---: | ---: |
| 0.1 | Scope | Freeze claims and repair order. Confirm target audience, source of truth for each version, and which releases are actually intended. Baseline links and screenshot claims before editing. | start | 1 / 2 / 3 | 2.0 | 0.0-2.0 |
| 1.1 | Fork install | Map fork-specific installation paths. Identify fork-built binary, package, and container paths; distinguish upstream from fork across KCode, OmniRoute, HeliosLite. | 0.1 | 1 / 2 / 4 | 2.2 | 2.0-4.2 |
| 1.2 | Fork install | Correct KCode first command. Lead command installs the fork’s release, not upstream jcode.sh; document upstream separately and test clean environment. | 1.1 | 1 / 2 / 4 | 2.2 | 4.2-6.3 |
| 1.3 | Fork install | Correct OmniRoute quick start. Replace upstream Docker/npm lead with fork-specific build or release; mark upstream option explicitly. | 1.1 | 1 / 2 / 4 | 2.2 | 4.2-6.3 |
| 1.4 | Fork install | Correct HeliosLite legacy command. Retire forge-dev → old forgecode installer; verify current fork install and migration note. | 1.1 | 1 / 2 / 3 | 2.0 | 4.2-6.2 |
| 1.5 | Fork install | Smoke-test and publish fork instructions. Run all three first commands on clean targets; capture exact output, platform, and artifact provenance. | 1.2, 1.3, 1.4 | 2 / 4 / 8 | 4.3 | 6.3-10.7 |
| 2.1 | Releases | Reconcile release truth matrix. Record tag, binary/package version, installer artifact, and lead README claim for each project. Decide whether to publish missing artifacts or qualify claims. | 0.1 | 2 / 3 / 5 | 3.2 | 2.0-5.2 |
| 2.2 | Releases | Repair installer and version claims. ShareCLI v0.3.0 release vs tree 0.8.0 and Homebrew "when published"; BytePort v1.0.0 installers named 0.1.0; AgilePlus v1.1.0/21 releases vs v0.2.4; Melosviz v0.1.1 DMG named 0.1.0. | 2.1 | 2 / 4 / 7 | 4.2 | 5.2-9.3 |
| 2.3 | Releases | Qualify maturity and distribution. HeliosCLI v0.11.1 source-only; PhenoMLX tags without releases; WorldSphereMod beta runtime validation. Publish artifacts only if truly tested. | 2.1 | 3 / 6 / 10 | 6.2 | 5.2-11.3 |
| 2.4 | Releases | Verify public install and release paths. Test each supported install path; check release links and label unverified platforms rather than implying support. | 2.2, 2.3 | 2 / 4 / 7 | 4.2 | 11.3-15.5 |
| 3.1 | PhenoLab | Review private dashboard examples. Privately verify that published examples and credential handling are safe. Keep values and security findings out of public planning records. | 0.1 | 1 / 2 / 4 | 2.2 | 2.0-4.2 |
| 3.2 | PhenoLab | Review private onboarding and configuration changes. Check proposed onboarding and configuration changes against the private repository, then use its normal review and test gates. | 3.1 | 2 / 4 / 8 | 4.3 | 4.2-8.5 |
| 3.3 | PhenoLab | Review private security changes and tests. Review private security changes and add suitable tests before deciding whether to merge. Do not publish details of the review here. | 3.1 | 3 / 6 / 12 | 6.5 | 4.2-10.7 |
| 3.4 | PhenoLab | Reproduce private clean-install and test failures. Run the documented clean install and test suite in an approved environment; record reproducible evidence in the private repository. | 3.2, 3.3 | 2 / 5 / 10 | 5.3 | 10.7-16.0 |
| 3.5 | PhenoLab | Align private CI claims with actual checks. Review private CI rules, coverage and quality gates; correct either enforcement or claims before publication. | 3.4 | 4 / 8 / 16 | 8.7 | 16.0-24.7 |
| 3.6 | PhenoLab | Reconcile private metadata and public claims. Confirm package metadata and public-facing documentation match the current private source and verified results. | 3.5 | 2 / 4 / 7 | 4.2 | 24.7-28.8 |
| 4.1 | Substrate | Confirm absorbed component boundaries. Verify that the Substrate component paths and packaging are canonical in PhenoShared; resolve the product lineage before changing public status wording. | 0.1 | 1 / 2 / 3 | 2.0 | 2.0-4.0 |
| 4.2 | Substrate | Fix embedded dependency URL. Replace deleted KooshaPari/substrate URL in crates/substrate/README.md with canonical PhenoShared path and verify the example. | 4.1 | 1 / 2 / 4 | 2.2 | 4.0-6.2 |
| 4.3 | Substrate | Repoint public case study and profile. Update GitHub profile and site /work/substrate "CURRENT" plus links to PhenoShared, or mark case study archived/private if evidence is not public. | 4.2 | 2 / 4 / 7 | 4.2 | 6.2-10.3 |
| 5.1 | Portfolio | Choose one portfolio narrative. Choose systems engineering as the lead or product leadership; rank proof clusters to fit the role target without inflating scale. | 0.1 | 2 / 4 / 7 | 4.2 | 2.0-6.2 |
| 5.2 | Portfolio | Fix factual and historical labels. Mark the M.S. as "in progress" on the resume if still accurate; reconcile phenotype-omlx versus PhenoMLX naming against the actual product. Keep project status evidence tied to the right entity. | 5.1 | 2 / 4 / 7 | 4.2 | 6.2-10.3 |
| 5.3 | Portfolio | Reorder and tighten first viewport. Align GitHub and site ordering with chosen audience; test shorter systems headline and draft bio. Keep verified work, contribution, and maturity labels. | 5.1 | 2 / 4 / 8 | 4.3 | 6.2-10.5 |
| 5.4 | Portfolio | Move hardware case studies to main site. Treat Ram Designs as legacy: migrate dated hardware case studies to the main site, accurately label historical sales claims, and verify the LinkedIn destination. | 5.2, 5.3 | 3 / 5 / 9 | 5.3 | 10.5-15.8 |
| 5.5 | Portfolio | Redirect or sunset Ram Designs. Once migrated pages and links have been checked, redirect old routes to canonical case studies or provide an intentional sunset notice; preserve historical context. | 5.4 | 2 / 4 / 7 | 4.2 | 15.8-20.0 |
| 5.6 | Portfolio | Review mobile and links. Check landing at phone/desktop sizes, all project and social destinations, migrated hardware pages, redirects, and Substrate case study. | 5.5, 4.3 | 2 / 4 / 8 | 4.3 | 20.0-24.3 |
| 6.1 | Acceptance | Final evidence and release audit. Repeat clean-install, CI, package/release, public-link, and portfolio-claim checks. Keep private review receipts in the private repository. Log caveats and obtain owner review before publication. | 1.5, 2.4, 3.6, 5.6 | 2 / 4 / 8 | 4.3 | 28.8-33.2 |

## Acceptance and evidence limits

The owner should decide the target audience and release scope before implementation. A first-install command must install the intended fork, not an upstream project; version and distribution language must match tested artifacts; private test/security/CI wording must match enforced checks; Substrate links should point to its confirmed present home; the resume, naming and legacy hardware case studies should be accurate and dated. Public changes require owner review and the usual repository checks. Do not merge or publish an edit merely because its predecessor is complete.

These are leads from the September 25 read-only portfolio audit, not fresh tests run by this plan. Source project entry points: [KCode](https://github.com/KooshaPari/KCode), [OmniRoute](https://github.com/KooshaPari/OmniRoute), [HeliosLite](https://github.com/KooshaPari/HeliosLite), [PhenoShared](https://github.com/KooshaPari/PhenoShared), [main portfolio](https://kooshapari.com/), [resume](https://kooshapari.com/resume), and [legacy hardware site](https://ramdesigns.xyz/). Verify current state, licenses, and public claims at each owner source before acting. This plan does not change those sources.
