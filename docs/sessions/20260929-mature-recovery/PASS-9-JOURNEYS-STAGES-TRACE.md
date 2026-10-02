# Pass 9 — W8/W9 journeys, stages and trace graph

Date 2026-09-30.

All three product repos now have journey/stage v1 and authority-aware trace matrix v1. Existing earlier similarly named artifacts were preserved; v1 was added rather than silently overwritten.

## Stage doctrine

No stage is a requirement percentage. A stage qualifies only when its required actor-to-outcome journeys close with accepted evidence.

Portage CVP requires install/task/subject/run/failure/provenance journeys. PhenoMLX CVP deliberately includes cancel/unload/restart and qualification for one real RuntimeProfile. PhenoLab CVP deliberately includes independent assessment, durable decision history, worker replacement and negative-learning retention even with only one optimizer/task family.

No current product qualifies CVP.

## Trace state

Trace edges are explicitly typed as VERIFIED_SOURCE, VERIFIED_OBSERVATION, DETERMINISTIC_SOURCE, PROPOSED, MISSING or CONTRADICTORY. Confidence cannot upgrade them.

The matrices immediately expose why raw implementation/test counts are misleading:
- Portage has a real parser but missing/unmapped subject/evidence/attempt/export identities.
- PhenoMLX has launcher and historical performance evidence but lacks unified RuntimeProfile/lifecycle qualification.
- PhenoLab has a real tournament loop and serializable Trail but contradicts independent acceptance/hard-gate semantics and lacks candidate/durable-experiment/promotion identities.

## Product receipts

Portage journey head `f22b56156161ef67fcf08c2c74af571d9a8bb7b0`; trace head `7b16285de5712875f515616fa55a7fbdf3cda395`.

PhenoMLX journey head `2da65e35afcecd16dfdde9e634a6b8cdb0c8d62e`; trace head `212b5bd1cb15a4a07edbfcdac6cfdc97599253d3`.

PhenoLab journey head `d72ee38a4a4cd1f019fa0c977dbce419c61ee57d`; trace head `d2c264a0c8bd5ff453925160b95ec56cbc507770`.

## Next

Before accepting ontology/obligations, run a deliberate semantic falsification pass:
- missing lifecycle states;
- configuration/version transitions;
- authorization/security boundaries;
- multi-actor conflicts;
- offline/partial/degraded modes;
- import/export/interoperability;
- deletion/retention/deprecation;
- concurrent/duplicate/out-of-order events;
- alternative architecture interpretations.

Valid findings expand/correct ontology and obligations; invalid findings get evidence. Then continue obligation decomposition and implementation mapping. No percentage yet.
