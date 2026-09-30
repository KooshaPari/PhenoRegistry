# Pass 20 — runtime consumer semantics and expanded save rerun

Date 2026-09-30. Exactly Dino + Civis.

Dino source tracing classifies real runtime consumers: PackUnitSpawner/WaveInjector are lookup-on-demand over retained RegistryManager references; BuildMenuInjector materializes cached/live UI state behind a one-shot flag; AerialSpawnSystem has a one-shot building sweep. Therefore pointer rebinding cannot be one universal ACK. Product doc3cfde963619598644af841fff2691d657460b290 and test-only consumer-semantics prototype0124edd7aff871ca63d8f92fc4cd959bd3cbb5f4 add lookup/materialized/restart-required distinctions.

Civis latest completed run36703825128 remains9 production reds +1 prototype-fixture red. Expanded semantic prototype now covers tutorial progress, religious profiles and active caravans; atomicity fault targets required semantic-state.json. Prior rerun36705591591 was cancelled before any job and is inadmissible. Fresh run36705722211 was also cancelled by supersession; no credit. A new head/run is required after latest spec-branch commits settle.

No completion percentages or third product.
