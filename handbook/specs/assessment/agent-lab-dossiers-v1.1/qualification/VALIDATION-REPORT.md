# Dossier-layer validation report — v1.1

Recorded: 2026-09-11T23:27:20.716325+00:00

## Executed checks

| Check | Observed outcome |
|---|---|
| New dossier-layer tests | **35 passed**, including stale/altered views, duplicate keys, wrong subject/assignment bytes, source-class relabeling, fake acceptance, unknown applicability, outbox payloads, HTML escaping, and same-subject evaluator deltas. |
| Retained core suite | **68 passed** on this runtime. |
| Independent JSON Schema cross-check | **288 new canonical typed records passed** using `jsonschema` Draft 2020-12 with an offline registry of the packaged schemas. |
| YAML round-trip | All eight generated YAML views decoded to their matching JSON models under the installed independent YAML parser. |
| Dossier consistency | All eight filled dossiers and the blank template passed canonical input, local byte-digest, reference, and generated-view checks. |
| Retained core bytes | Core manifest checked **183 files**; no core file modifications. |
| Executed fixture | Fresh bundled run rejected the no-op and accepted the checked implementation on exactly two predicates. |
| Browser layout | Gallery and broad dashboard loaded through Playwright `set_content` in Chromium **144.0.7559.96**. Eight gallery entries found; dossier expansion worked; no page errors; dashboard viewport at 390 px had no document-width overflow. |

## Runtime and method

Python: `3.13.5`. Platform: `Linux-6.18.35-x86_64-with-glibc2.41`. The tools have no third-party runtime dependency; `jsonschema`, PyYAML, and Playwright were used only for additional release validation in the available environment.

The environment's Chromium policy blocked direct `file://` navigation. The authored self-contained HTML was therefore rendered with `set_content`; filesystem targets are checked separately. The direct file-navigation route was not claimed tested. Screenshots were inspected. No full browser-matrix or WCAG conformance assessment is claimed.

## Evidence classes

Two dossiers contain actual executions of the bundled synthetic restoration fixture. Six contain authored fictional scenario premises. They have PROPOSED results and no claimed instrument qualifications, so their current evidence-based gates remain BLOCKED. Their hypothetical PASS/FAIL summaries are explicitly separate. No actual user repository, local workstation, deployment or external consumer was audited.

No signing identity, source Git commit, report Git commit or registry commit is invented. The rendered build receipts explicitly retain missing identities as null. An outbox item is PENDING with zero attempts and no receipt.

## Limits

These are consistency, rendering and reference-kernel tests, not independently authenticated product assurance. Record shape does not establish a truthful observation, genuine authority or adequate semantic judgment. A matching checksum is not a trusted signature. Test success does not demonstrate an autonomous lab run or complete recovery of historical rubrics.

Test logs: [dossier layer](dossier-tests.txt), [retained core](core-tests.txt). Browser examples: [gallery](gallery-desktop.png), [dashboard](dashboard-desktop.png).
