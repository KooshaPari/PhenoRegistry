from __future__ import annotations
import csv, hashlib, json, re, textwrap, zipfile
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
ROOT=Path(__file__).resolve().parent
NAMES=json.loads((ROOT/'records/list-observed-names.json').read_text())
IDS='''707502317 861430079 960016965 980996178 998124581 1009324469 1015249259 1017123874 1020556829 1048244869 1069864709 1077977094 1159182006 1162254344 1162255140 1164684442 1164684829 1164703420 1165315873 1165351720 1167587447 1169608854 1169864396 1177712269 1185005735 1191459198 1194326424 1199812615 1200273587 1201113097 1201987910 1214745478 1220333985 1220334053 1220437668 1220449881 1226104769 1226168548 1226171396 1226264690 1226547140 1241972761 1262466303 1269596554 1269695199 1271708536 1271786703 1272990345 1273002789 1273002818 1284536541 1308558334 1308570444 1315997929 1319179066 1322607630 1328507619 1330430083 1349458262 1363521465 1365855438 1369043600'''.split()
assert len(NAMES)==len(IDS)==62
PRIVATE=set('zz-pause-AgsLag zz-pause-ref-AtomsTech zz-pause-ref-AtomsBot zz-pause-ref-KaskMan zz-pause-ref-472P2FlameWar zz-pause-Parpoura zz-pause-QuadSGM Eidolon zz-pause-ref-NetWeave PhenoLab zz-tbd-PhenoSDKs'.split())
BRANCH={'zz-aa-dep-UnityDoorstop':'master','zz-aa-dep-Planify':'master','jcode':'master','zz-tbd-PhenoApps':'apps-extract'}
# The source records below are normalized observations of connector reads, not raw API exports.
README_SOURCES='''PhenoRegistry|228|cc1d3544c52e70ec6b7db0c16d5fac753ff3ee00
PhenoTooling|232|9d534492dfc364e93b1bd85e9158cff5fc8942b5
Civis|236|bb9bf1090ad5b3b92060223f8f8432ca9363b44f
AgilePlus|238|e3d317d302433868b36c7ab93643646e9976ec31
BytePort|241|1f2ab4c8cd60edf17a19c84b207a4256dc7757c7
PhenoInfra|242|f75ab5b42ee26100b79ac4f9f10e6d7937f70184
sharecli|243|cf711afaca3947bda0a3d1c1a52cfc5c0d6886b6
Tracera|244|0a8995c5fd7043361a001e96d407c65f3e0ec6b7
PhenoAI|245|c050ec66e51c53f62353c6dc83b386294c72c9b5
PhenoMLX|246|42e22485c6956600fcd637658608d29011e32110
PhenoFabric|247|581eeb8794d288d4c18c6c66588d1594e3db4e25
helios-cli|248|f71ee6abdc07d63ef90d03bd5b8d29707af1e380
HeliosLab|249|9ce35abe88beedfc1090dfa30957bc81b0972d1d
portage|250|5fe3756c542a812051a683be4f9362a1365864d9
PhenoDesign|251|32fb645b48a5401d24c43464ca7fc93d5b26c0e9
Dino|252|95f11713ae1e0ee68afa51fef973b617ede6ae70
Eidolon|253|
forgecode|254|cff704bcf3bf7350ac5228c2849196746b345a02
OmniRoute|255|9089b642b89c19fa9359b4cc57095fc25bae4833
Pine|256|8ff762cff0c6c79fe40b7b77e40315ec46a4e3a5
WorldSphereMod|257|e42f1e393b2bbc7b88577f275ddf67804aab5364
Melosviz|258|aeb7aff5d4214bfa7425cc4ea4fa6364c4a07a29
substrate|259|5a933e41583735bbf3ae4b82dcfb25fa68433a7a
PhenoLab|260|4810488a56099212d344dca49c10ec8025f2036f
PhenoGfx|261|98e8e03afa0c8adb2d35463134ecd345c5ecd18d
CivicSurvival-public|262|897f7b42eee4c64f23a9d86205ab0d060e3f9cc9
 ghostty|263|ff6cb75685900c4dd4e8f7840e2f202bfba76d8a
KooshaPari|264|2eff43f3235f631a6e91c1680113b0315656ab54
jcode|265|4ccdb48a064f46437526be3b610300b8d373f6e8
AirLock|268|0b6f292a6a731a3f70f2a9918b8ffe6a3f314774
zz-tbd-PhenoApps|269|4cb2afc674cb4ae0fa9121cd98c57eb7ca08ec9a
zz-tbd-PhenoSDKs|270|335b59d101f68fa4212e75fa73700be86f2ce107
zz-tbd-Pheno|271|c16c73a4066af3daf1c9fed5ef4e31c07f8a94de
zz-tbd-MobileCli|272|117d050ad4c2556a6cc41d56e86b2a5c2d6bba79
zz-pause-Thegent|273|15a2507928440547c3e631a94a7e6625675e6839
zz-pause-AgsLag|274|fc90395ebbe81dec1338a5552dac5023205f7bc9
zz-pause-Parpoura|275|3db9a1d20fd28312b1d64f3b8a8a4ef0b30051bb
zz-pause-Localbase|276|360b1693ddb2efffbcfbcb1c3f7225cda89c75b5
zz-pause-FocalPoint|277|00b4037b090ea595dc803507b3f281606dfb9912
zz-pause-QuadSGM|278|02335b01efd183c618781aa57d3f46f581f68e0a
zz-pause-SessionLedger|279|c016858d85c827ce4d50a884dd299c1965b4674e
zz-pause-ResearchLedger|280|d6be2ca9fc09fd3e539996295f16dc8456bd7f15
zz-pause-VibeKanban|281|2f962614372ea2c97a817e7f32ea75f1c6dfb2ea
zz-pause-GitHub|282|8edbd67ce9fae69adbe1a9bc6bca0d05dc50cdc8
zz-pause-RIPFitnessApp|283|0a025e1d59a317e8c40076a264efe07dcb4f041f
zz-aa-dep-AgentApiPlusPlus|284|3ef4be3eb98802f92d08c4d7183c8aee1dce277e
zz-aa-dep-CliproxyApiPlusPlus|285|17e615aadd9c529beecb8a81e46885dce3135dc2
zz-aa-dep-Planify|286|ccb960b41feda0e78b25c5ab919a948088eae38d
zz-aa-dep-Bifrost|287|3f808b8b2d9f25a82b8aa18fa29e2689ff3980ef
zz-aa-dep-PhenoMCPServers|288|f7746e9f7b263d5cce23a2831a5793f41876cc78
zz-aa-dep-UnityDoorstop|289|1ae257ba83b6f23042db4e7ad1f4c921e2e21178
zz-aa-dep-TurboQuant|290|a7b74859a5d5bdd1a8399fd36dadca9256566b51
zz-aa-dep-PhenoUnslothStudio|291|dcf1a5a70e89a7d0ec5298aec02c6f5f7168e793
zz-aa-dep-CompoundSpheres3D|292|c1ef3c3a033e37ca2d97240d7743db38b9ebb317
zz-pause-ref-ProjectSpyn|293|5100ecaefb9a491152650c5ba4747c3fe2ec5df0
zz-pause-ref-AtomsTech|294|0568c872fb91057931d8264913b4d7767bdbc3da
zz-pause-ref-AtomsBot|295|7b156830d001c844735d0eafa3b431d46d9bc068
zz-pause-ref-KaskMan|296|62d8bd6b4e7339c5699feff39f1e67455d4fdbec
zz-pause-ref-Synthia|297|a3a1b1ef0271cd2d9f38d3b75da47f01db3a652a
zz-pause-ref-472P2FlameWar|298|de9a011b45cdefbb77bb8dbe833d0657900c66f6
zz-pause-ref-NetWeave|299|2a5c95d21bcda772a3798bc6fc9ea5cb7658fb66'''
SOURCES={}; SRCBY={}
for row in README_SOURCES.strip().splitlines():
    name,turn,blob=[s.strip() for s in row.split('|')]
    sid=f'S{turn}'
    observed='zz-aa-dep-AirLock' if name=='AirLock' else name
    source={'id':sid,'kind':'connector_file_read','repository_cohort_name':name,'observed_repository':f'KooshaPari/{observed}',
            'path':'README.md','ref':BRANCH.get(name,'main'),'blob_sha':blob or None,
            'url':f'https://github.com/KooshaPari/{observed}/blob/{BRANCH.get(name,"main")}/README.md',
            'citation':f'fileciteturn{turn}file0L2-L2','coverage':'bounded README range; not whole-repository proof',
            'normalization':'source metadata and analyst observations, not full raw connector payload'}
    SOURCES[sid]=source; SRCBY[name]=sid

def extra(sid,repo,path,ref,blob,kind='connector_file_read',url=None,note=''):
    SOURCES[sid]={'id':sid,'kind':kind,'observed_repository':f'KooshaPari/{repo}','path':path,'ref':ref,'blob_sha':blob,
        'url':url or f'https://github.com/KooshaPari/{repo}/blob/{ref}/{path}',
        'citation':f'fileciteturn{sid[1:]}file0L2-L2','coverage':note or 'selected source read; native execution not performed'}
extra('S234','PhenoFabric','Cargo.toml','main','0ab5327ee2d97b2c5633aa890113c59405bccd2c')
extra('S235','PhenoFabric','crates/phenotype-nvms-adapter/Cargo.toml','main','9e3bcc2704c19a2a58a4745440147ccc94e9109e')
extra('S239','AgilePlus','.github/workflows/coverage.yml','main','ba2f6a40ab54753a18abea6a7aa735a39980e85b')
extra('S266','AirLock','contents','initial-name',None,'connector_redirect','https://api.github.com/repos/KooshaPari/AirLock/contents','301 body points to repository ID 1319179066')
extra('S300','Civis','commit diff','264359afc8dc08c31f55b0ee951842067d135751',None,'connector_commit_diff','https://github.com/KooshaPari/Civis/commit/264359afc8dc08c31f55b0ee951842067d135751','source diff and added tests inspected; tests not executed')
extra('S301','Civis','crates/engine/src/engine.rs','264359afc8dc08c31f55b0ee951842067d135751','19ceec43d96b92ba6ed3f9267ef6447f466bc9ef')
extra('S302','Civis','scripts/build-macos-app.sh','main','2ce5d99e017ce0679e508ef75cd1a2b2fe4bc219')
extra('S304','PhenoTooling','crates/docs-health/src/main.rs','dd0cf322ae72785a6511ede52db2d594360a3372','8c31243a22e15aaae8f054ad711a908c7213dd9b')
for sid,repo,tag in [('S305','Civis','v0.5.0'),('S306','sharecli','v0.3.0'),('S308','jcode','v0.85.0-k1.0.0'),('S309','AgilePlus','v2026.09.0'),('S310','Tracera','v0.49'),('S311','forgecode','v2.13.21-h.0.2.1')]:
    extra(sid,repo,'releases/latest',tag,None,'connector_release_metadata',f'https://api.github.com/repos/KooshaPari/{repo}/releases/latest','latest-release endpoint metadata; assets not downloaded, installed, or executed; other distribution channels not exhaustively searched')
extra('S307','forgecode','pull/277','ad073e4d2f4c3eeebf3e0767bc48fdf5a04a1711',None,'connector_pr_metadata','https://github.com/KooshaPari/forgecode/pull/277','merged status and target branch verified; full check/review history not re-executed')
extra('S312','PhenoTooling','Cargo.toml','main','f016e8a1aef01b2b1282de863adb43884cc8d161')
extra('S313','PhenoTooling','crates/sharecli-core/src/lib.rs','main','cb35ab8d126c4571a2f329869efaec5102d94906')
extra('S314','sharecli','crates/sharecli-core/src/lib.rs','main','cb35ab8d126c4571a2f329869efaec5102d94906')
extra('S315','HeliosLab','Cargo.toml','main','599751c7058770b9de9440fdc1e17d1ecc2b29b9')
extra('S316','PhenoAI','Cargo.toml','main','7139cb61a95c7f303dec31ab8e0ea8403fbfd818')
SOURCES['W01']={'id':'W01','kind':'official_documentation','url':'https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api','coverage':'404 can conceal inaccessible private resources; not deletion proof'}
SOURCES['W02']={'id':'W02','kind':'official_documentation','url':'https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository','coverage':'Git redirects versus project-site and action-reference exceptions'}
SOURCES['W03']={'id':'W03','kind':'official_documentation','url':'https://doc.rust-lang.org/cargo/reference/resolver.html','coverage':'resolver 3 requires Rust 1.84+; Cargo.lock constrains resolution'}
SOURCES['W04']={'id':'W04','kind':'official_documentation','url':'https://doc.rust-lang.org/cargo/reference/specifying-dependencies.html','coverage':'Git dependencies, lockfiles, revisions and source resolution'}

A={}
def active(name,role,assessment,observed,next_action,acceptance,priority='P1',sources=(),baseline=''):
    A[name]={'role':role,'assessment':assessment,'observed':observed,'next_action':next_action,'acceptance':acceptance,'priority':priority,
        'source_ids':[SRCBY[name],*sources],'comparison_next':baseline,'cvp_acceptance':'NOT_INDEPENDENTLY_QUALIFIED_IN_THIS_PASS'}
active('BytePort','Git-to-deployment application','QUALIFY A BOUNDED DEPLOYMENT',
    'The README describes Go/API and desktop/web paths, but labels manifest delivery and isolated microVM execution planned. Development instructions still refer to NVMS. A UI/compose startup is not deployment completion.',
    'Select one already-supported target; reconcile the NVMS consumer boundary and run a clean repo-to-service deployment without an adjacent developer checkout.',
    'Authenticated connect, build, deploy, inspect logs, update and rollback; failed provisioning leaves known state; installed client or hosted route has exact artifact provenance.',baseline='Compare a matched application deployment with the simplest direct cloud/deployment workflow, including recovery and operator steps.')
active('Tracera','Persistent product/system graph and gap discovery','RECONCILE PRODUCT IDENTITY; THEN QUALIFY',
    'Its current README foregrounds observability, audit and session memory rather than the user-confirmed canonical product graph. The latest inspected GitHub release is v0.49 (September 3), a scorecard checkpoint with a Windows archive and manifest, not evidence of the full desired desktop product.',
    'Keep the graph identity and automatic dissatisfaction/gap detection explicit. Exercise one persistent product-model journey; preserve evidence links as a supporting view, not a replacement identity.',
    'Import a real product, traverse bounded component detail, expose a genuine missing/failed capability, link evidence, restart and retain state. Validate actual installed/hosted frontend against actual backend.',sources=('S310',),baseline='Compare product-model exploration and gap diagnosis against the current manual repository audit, not merely log search.')
active('Civis','Persistent systemic game','CLOSE THE PLAYER BUILD',
    'A source diff adds archive persistence for culture/ideology/aggression/unrest and real round-trip assertions. The Mac builder still selects only bevy,egui,client-bins and tolerates missing assets. Latest stable GitHub release v0.5.0 (September 5) exposes three CLI archives, not a current qualified game app.',
    'Pin a game-first candidate, required presentation profile and asset manifest. Close the world-create/play/intervene/save/reopen journey before widening mechanics. Reconcile old global-determinism and research-only claims with current intent.',
    'Install outside the checkout, launch through the OS, show real renderer/animation/audio, mutate a populated world, save/restore meaningful state, and prove bounded unattended continuation. Native visual review and performance under load are required.',sources=('S300','S301','S302','S305'),baseline='Use the already-defined living-settlement witness and bounded engine comparison; do not choose engines or declare fun from headless tests.')
active('helios-cli','Codex-derived CLI / harness workspace','RESOLVE WHAT THE SHIPPED BINARY IS',
    'The README says the root workspace is the harness system and excludes vendored codex-rs/codex-cli. Root workspace success therefore does not establish a functioning Codex-derived coding agent.',
    'Name the actual installable product and build root. Separate reusable harness packages from the agent executable while retaining their integration contract.',
    'A clean install uses the advertised binary to read a repository, edit an allowed file, run real tests, refuse prohibited scope, survive a tool error, and resume a session.',baseline='Matched coding task against direct upstream Codex and existing ForgeCode/Jcode; compare fork delta and maintenance burden.')
active('portage','Harbor-derived evaluation framework','RUN A REAL EVALUATION',
    'The README carefully distinguishes upstream PyPI from this fork and optional Rust bridge support, but still instructs cloning portage-TEMP. Static oracle badges and suite-info commands do not prove useful benchmark execution.',
    'Correct the consumer install target and run one real agent/environment benchmark with a deliberately failing candidate and missing-extra case.',
    'Clean fork install, task execution, trustworthy pass/fail reward, retained logs, cancellation and resource limits; optional bridge unavailability must be explicit.',baseline='Compare identical tasks through this fork and upstream Harbor; retain local changes only for evidenced workflow/quality/performance value.')
active('HeliosLab','Currently a config/flags/secrets phenoctl workspace','RECONCILE SCOPE AND DEPENDENCIES',
    'The README simultaneously says 65%, 80%, stable and a desktop/journeys lab, while the manifest confirms six config-oriented crates. It depends on old clap-ext and PhenoObservability locations; clap-ext returned 404 in this pass.',
    'Resolve whether this is the intended agent workbench or a config product without erasing useful code. Repoint only after verifying source/API equivalence and accepted ownership.',
    'Clean supported-toolchain build without retired private caches; config/flag/secrets workflows persist correctly and do not disclose secrets; then prove the actual chosen UI/CLI product.',sources=('S315',),priority='P0',baseline='Compare the accepted workflow, not two unrelated products sharing one repo name.')
active('AgilePlus','Reusable repository-scoped work/spec tooling','REPAIR FALSE ASSURANCE BEFORE ACCEPTANCE',
    'Coverage CI enforces 20% Rust lines, prints Go coverage without a threshold, and the aggregate 85% gate echoes success without evaluating artifacts. README includes static 100% claims and an incompatible shelf identity. Latest published release titled Installers + green tests has zero uploaded assets.',
    'Implement independent suite/metric denominators and failure propagation, remove unrelated portfolio content, and publish a real scoped CLI/MCP/desktop candidate through its actual local state contract.',
    'Unit/integration/E2E and other required families meet accepted floors; critical obligations all pass. Separate subjects remain isolated; live engine receipts back transitions; clean installation and real UI/MCP CRUD succeed.',sources=('S239','S309'),priority='P0',baseline='Compare governed repository work against current ad-hoc files/CLI, while proving the tool works for an unrelated external project.')
active('PhenoDesign','Shared design and asset foundation candidate','RESTORE AN UNAMBIGUOUS ROLE',
    'The active-named repository still consists of an archived/migrated notice dated July 29 with no concrete successor. This is not a usable design-system handoff.',
    'Inventory retained editable assets, tokens, licenses and actual consumers. Resolve ownership; do not regenerate the brand or create a new library solely to replace missing documentation.',
    'Two real consumers use versioned tokens/components or asset exports; editable sources and licensed inputs are traceable; visual baselines and no-color/accessibility rules exist.',baseline='Compare consistency and change propagation against the current per-product asset duplication.')
active('Dino','DINOForge game mod platform and companion','QUALIFY THE INSTALLED GAME PATH',
    'The README claims broad pack/asset/bridge/companion capability, 3,613+ tests and 95%+ coverage, but its status section is a development milestone summary. Those claims were not independently reproduced.',
    'Use the supported installed game and actual companion build to exercise one substantial pack; keep private/game dependencies explicit.',
    'Clean install, pack validation, runtime ECS/asset integration, UI interaction, save compatibility, hot reload or clear restart, and clean disable/uninstall. Required assets and failure logs are retained.',baseline='Compare the same mod-author/player task with the prior manual mod workflow; no invented standalone macOS game app.')
active('sharecli','OS-adjacent process/resource supervisor','RESOLVE DUPLICATE AUTHORITY; SHIP CURRENT CANDIDATE',
    'Its core source has the exact same blob in PhenoTooling and the standalone repo; PhenoTooling registers the copied crates. Latest inspected stable release is v0.3.0, published July 5, with Mac ARM/Linux archives uploaded July 14. Current source/UI claims must not be attributed to that release without a diff.',
    'Name one source/release owner or explicit synchronized distribution contract. Then prove the current supervisor under realistic concurrent agent/background/foreground workloads.',
    'No inappropriate command coalescing, secret/cache cross-talk or stuck children; cancel/retry/failure semantics survive; real native tray/CLI installs and resource limits protect foreground use.',sources=('S306','S312','S313','S314'),priority='P0',baseline='Compare identical workloads without the supervisor and against existing supervision; measure correctness first, tail latency/resource relief second.')
active('PhenoRegistry','Curated portfolio identity/projection tooling or data authority','REPAIR THE LIVE MAP',
    'The root advertises 111 repositories and retired authorities. Search surfaces copied platform work templates still referring to approximately 170 repositories. Neither is the current 62-ID roster.',
    'Generate a current ID/name/role projection and attach scoped accepted decisions; separate GitHub observations from intended roles and mutable work state.',
    'Renames retain identity, missing access is not deletion, paused/dependency/TBD classes are explicit, every advertised owner resolves, and stale facts are visibly dated.',priority='P0',baseline='Compare time to correctly answer where a capability lives and what is release-blocked against the current manual audit.')
active('PhenoAI','AI library/provider workspace with newly absorbed device code','RECONCILE EXPANDED BOUNDARY',
    'README says three AI crates, while Cargo.toml lists routing, embeddings, Eidolon device crates, PlayCua native code and more. Resolver 3 is selected alongside a declared Rust 1.75 floor; official Cargo docs require Rust 1.84+ for resolver 3.',
    'Establish which packages are reusable AI primitives, device adapters or product code, and who writes/releases each. Make toolchain claims executable rather than upgrading the label alone.',
    'Clean minimum-toolchain matrix, one authorized provider/MCP/embedding consumer path, negative credential and cancellation cases, and no competing independent Eidolon implementation without a declared contract.',sources=('S316','W03'),priority='P0',baseline='Compare the accepted thin integration layer with direct provider SDKs; do not make a generic AI umbrella the default destination for unrelated code.')
active('PhenoMLX','OMLX-derived inference and research application','QUALIFY A SELF-CONTAINED INFERENCE PROFILE',
    'The current README still depends on an installed /Applications/oMLX.app environment, local Python injections and adjacent research checkouts. It distinguishes some CPU-only/placeholder work, but broad performance claims are not qualification evidence.',
    'Select one supported model/backend and produce a reproducible extension or self-contained install with explicit upstream/fork identity and research boundaries.',
    'Clean install, model load/inference/cancel/unload/restart, memory-pressure/OOM handling, valid credential and data paths, and measured quality/performance using the actual shipped artifact.',baseline='Matched upstream OMLX/MLX or selected local server baseline, with model, quantization, inputs and hardware controlled.')
active('PhenoTooling','Reusable developer/verification tooling collection','TRUST AND OWNERSHIP REPAIR',
    'The root remains a Genesis scaffold description, while the workspace contains many absorbed systems including Journeys, ShareCLI, eye tracking and orchestration. docs-health has three implementation TODOs, returns empty findings and an empty smoke test.',
    'Qualify the actual gate commands and identify per-package writer/release/consumer ownership. Preserve richer local intent systems; do not turn the collection into a universal product registry.',
    'Seeded broken input fails locally and in CI; nonzero errors propagate; missing backends are not green; an unrelated repo can use each published tool without copying the portfolio.',sources=('S304','S312','S313'),priority='P0',baseline='Compare each tool to the free/OSS native instrument it wraps; wrappers must add policy or usability without weakening evidence.')
active('PhenoInfra','Infrastructure/runtime composition home','PROVE CONSUMER CLOSURE',
    'The README still describes nanovms, PhenoCompose and BytePort consolidation. The old nanovms endpoint/ID is unavailable through this connection, while active consumers still reference it. The intended post-migration ownership is not demonstrated by this README.',
    'Map runtime/FFI/manifest packages to their accepted homes and all affected consumers; separate deploy configuration from product implementation.',
    'An authorized clean runtime provision/run/stop/cleanup path works; FFI ABI, source provenance, storage custody and rollback are verified. No schema or package is substituted merely because its name matches.',priority='P0',baseline='Compare exact deployment/isolation jobs with existing native/VM tooling; no new platform requirements solely to justify the repository.')
active('Eidolon','Cross-platform device automation and sandbox interfaces','QUALIFY EXPLICIT LIVE DRIVERS',
    'A detailed matrix distinguishes real, feature-gated and unsupported paths; REST daemon and crates publication are explicitly not shipped. Older 90%/alpha language coexists with that more useful matrix. PhenoAI now lists Eidolon crates too.',
    'Preserve the honest capability matrix and resolve the active source owner. Finish one consented desktop automation/recording path and one defined isolation path before more backends.',
    'Real screenshot/input/state checks under permissions; denial, lost display, absent runtime and unsupported platform fail explicitly. Do not confuse requested sandbox policy with introspected enforcement.',sources=('S316',),baseline='Compare a matched automation journey with the existing native/platform driver; validate security boundaries separately from throughput.')
active('forgecode','HeliosLite coding-agent CLI fork','INTEGRATED; RELEASE INSTALL PATH OPEN',
    'The previous h0.1.7 promotion PR #277 is now merged into main. The current README claims a separate heliosLite canonical repository/package. Latest GitHub release v2.13.21-h.0.2.1, September 15, has no uploaded assets; package registries were not audited.',
    'Select the actual install/update channel and immutable artifact. Reconcile binary/brand aliases and legacy session behavior without rewriting old conversation stores.',
    'Installed fork, not accidental upstream binary, passes task execution and SSE failure/reconnect; legacy/foreign sessions remain read-only; recall/forget honor scope; update/rollback preserves state.',sources=('S307','S311'),baseline='Compare the current fork against its upstream and Jcode on the same bounded task, including connection failures and concurrent children.')
active('OmniRoute','Maintained upstream-derived AI gateway/contribution fork','QUALIFY THE FORK DELTA',
    'The root is upstream-facing and advertises extensive provider/free-tier budgets and upstream releases. Those marketing numbers were not revalidated and do not establish your own fork deployment or accepted contribution state.',
    'Separate upstream contributions, local fork integration, deployed instance and user-installed version. Prove the local routing changes against selected real providers with protected credentials.',
    'Provider auth, streaming, fallback, quota accounting, cancellation and update/recovery behave correctly. External terms/quotas remain source-dated claims, not invented guaranteed free capacity.',baseline='Matched requests through upstream and fork; preserve task success and error semantics while measuring local improvements.')
active('Pine','Experimental application compatibility runtime','RESEARCH, NOT A GENERAL COMPATIBILITY CLAIM',
    'The README simultaneously says 70% and 25% pre-alpha. It declares a very broad Wine-equivalent goal but lists unresolved translation/isolation questions and five foundation crates.',
    'Keep the larger research intent, but select one explicit binary/API/platform compatibility experiment. Reuse established components where beneficial rather than promising arbitrary cross-OS execution.',
    'One real previously unsupported test program runs with correct observable behavior and bounded failures; reference semantics, supported imports and overhead are documented. No generic CVP label from compilation alone.',priority='P2',baseline='Compare the identical program with the relevant Wine/Proton/VM/native path, not generic guessed overhead percentages.')
active('WorldSphereMod','WorldBox 3D hard fork','CLOSE THE ACTUAL IN-GAME RENDER PROFILE',
    'The README usefully distinguishes CODE_LANDED from PROVEN, but names a local wip/208-height-fix branch as canonical while remote main is the inspected baseline. Many presentation features remain off or asset-bake deferred.',
    'Reconcile the actual game-tested branch and package. Verify Compound-Spheres provenance and consumer pin before enabling or pruning renderer variants.',
    'Installed mod displays the declared entities/terrain/water/lighting/UI on the supported game version; no asset fallbacks hide missing content; save/reload, disable and uninstall are tested.',baseline='Use the same save/camera/actions against upstream and the candidate; visuals need direct review and measured frame timing.')
active('Melosviz','Music visualization studio and native/web shells','QUALIFY REAL MEDIA, NOT DEMO OUTPUT',
    'The README offers a deterministic offline demo and an Electrobun app path, but its production stack mentions a C4D stub. Demonstrating a generated ZIP does not prove the real media/rendering path.',
    'Choose a real audio track and supported production renderer/backend; package a native app or correctly deployed web profile with explicit optional-service handling.',
    'Import, analyze, play/sync, edit preset, render/export, reopen and recover from a backend failure; validate audio/video output rather than file existence; capture an authentic polished app journey.',baseline='Compare time-to-usable visualization/export with the current manual or selected existing toolchain.')
active('substrate','AI dispatch gateway and TUI','BOUND ROUTING OWNERSHIP AND QUALIFY',
    'The README presents a concise runtime contract: SSE, retries, fallback, budgets, metrics and admin API. AgentApiPlusPlus separately claims both retained dependency status and absorption into substrate.',
    'Distinguish model-provider routing from control of agent processes. Declare the retained dependency/adapter contract and prove one safe gateway session end to end.',
    'Authentic streaming/cancel/failure cases, no duplicate charges or replayed unsafe requests, admin authorization, budget continuity and bounded logs. Do not certify production from /health alone.',sources=('S284',),baseline='Compare its intended minimal gateway/agent-control task with OmniRoute/Bifrost/CLIProxy and direct endpoints.')
active('PhenoLab','Reproducible evaluation/lab consumer','RUN AND AUDIT A REAL BENCHMARK',
    'The root still says pheno-harness and instructs a specs submodule/portage-TEMP installation. It distinguishes itself from the Harbor product but cites historical oracle/status claims rather than new execution evidence.',
    'Resolve install/submodule dependencies and run a seeded positive and known-negative evaluation in the supported environment; inspect current oracles rather than assuming prior fixes persisted.',
    'Source/config/model versions, inputs, results, failures, costs and artifacts are reproducible. Missing implementation/environment cannot silently skip required acceptance and produce success.',baseline='Compare a real agent task with the direct Harbor/Portage baseline; suite metadata introspection is not an evaluation workload.')
active('PhenoGfx','Shared graphics/data SDK','QUALIFY CONSUMER INTEROP',
    'The README has a focused four-module contract (Rust voxel; Unity terrain/water/postfx), but calls it scaffolding 2/10. It conditions supersession on consumer references, which is the correct kind of gate but not proof it passed.',
    'Verify one shared data-format/FFI path into actual game consumers and map donor provenance; preserve engine-specific capabilities that are not equivalent.',
    'Chunk/heightfield/mesh data and error behavior agree across the real consumers, including failed persistence and missing assets; native package/ABI tests and performance budgets pass.',baseline='Compare shared implementation and separate prior copies under the same game scene; require reduced change burden without lost rendering behavior.')
active('CivicSurvival-public','Public source/docs surface for a distributed CS2 mod','QUALIFY THE DISTRIBUTED MOD; RESPECT THE BOUNDARY',
    'The README explicitly says private generators and server sources are omitted and this public snapshot is not independently buildable. It advertises Paradox Mods distribution and warns beta saves are not version-stable.',
    'Trace the published player artifact to its qualified build and verify the actual mod journey. Do not invent the missing private components or count their absence as an accidental public build regression.',
    'Supported game install, onboarding, crisis mechanics, actual privacy defaults, declared save migration/limitations and uninstall behavior are demonstrated. Public-source transparency is not sufficient correctness evidence.',baseline='Compare the actual player experience and operator burden against vanilla plus the relevant prior mod workflow.')
active('AirLock','No-mistakes-derived Git publication gate','TRANSITIONED TO DEPENDENCY DURING AUDIT',
    'Initial inventory placed AirLock among the 30 unprefixed names. During this pass its stable ID resolved to zz-aa-dep-AirLock. The README remains the no-mistakes proxy/worktree pipeline with upstream installation.',
    'Record the ID-preserving role change and actual consumers. Retain the fork under dependency rules; verify the publication gate before relying on it for lifecycle safety.',
    'Known-invalid candidate is not forwarded; dirty user work remains intact; interrupted operations reconcile outcomes before retry; permissions and provider failures cannot be treated as passes.',sources=('S266',),baseline='Compare the local patch delta with upstream no-mistakes on positive/negative gated pushes using disposable remotes.')
active('ghostty','Terminal emulator fork / embeddable terminal dependency','QUALIFY OWNED DELTA AND CHANNEL',
    'The README prepends a fork note but retains upstream download links and maturity claims. Those establish the referenced upstream story, not a measured quality level for this fork.',
    'List intentional patches and decide whether this is an independently distributed terminal or an embeddable dependency. Trace terminal-fabric work to its current accepted home rather than assuming it vanished.',
    'Installed owned build passes terminal/input/render/clipboard/session cases for its supported platform; embedded use has a versioned contract; upstream and fork update channels cannot silently switch.',baseline='Run the same terminal conformance and real agent session in upstream and fork, including wide characters, paste and resize.')
active('KooshaPari','Profile / public portfolio consumer','PUBLISH ONLY CURRENT VERIFIED CLAIMS',
    'The profile links several renamed or absent products and advertises 101 merged OmniRoute PRs/rank #5. This pass did not reverify those statistics. Tracera is still positioned as audit infrastructure rather than the clarified product graph.',
    'Generate the public selection from approved product identity and bounded evidence; preserve historical achievements as dated claims rather than advertising deleted download routes as current.',
    'All public destinations resolve to the intended product or historical note; contribution metrics have exact query/window provenance; public build has no private data; landing/docs/app domains are tested.',baseline='Measure whether an unfamiliar visitor can install and understand a selected product without private explanation.')
active('PhenoFabric','Distributed compute/data/I-O graph runtime','REPAIR DEPENDENCY; PROVE A REAL ROUTE',
    'The root remains the original research/planning baseline while Cargo lists substantial implementation including GUI/TUI/capture/transport. Its NVMS adapter still fetches KooshaPari/nanovms, unavailable by old name and ID in this connection. Latest stable release endpoint returned 404.',
    'Verify the manifest/runtime successor by API and provenance, not matching crate name. Resolve dependencies, then demonstrate one real producer-consumer path and publish its actual profile.',
    'Clean reproducible build, authenticated two-node surface or task route, cancellation/reconnect, bounded contention and appropriate same-host fast path. GUI shell existence does not prove remoting or compute meshing.',sources=('S234','S235'),priority='P0',baseline='Compare the chosen route against its existing specialized transport; measure useful outcome and tail latency, not graph-editor appearance.')
active('jcode','Coding-agent harness fork','QUALIFY INSTALL AND DESTRUCTIVE-ACTION BOUNDARIES',
    'Latest GitHub fork release v0.85.0-k1.0.0 exists (September 15), but its observed attached asset list contains only a FreeBSD x86_64 archive. README install/update paths still predominantly point at upstream jcode.sh, while manual download points to this fork.',
    'Prove the exact fork installation/update path on the actual Mac and Windows hosts. Preserve successful connection/subagent work while making irreversible actions depend on explicit external authority.',
    'Installed digest/version matches tested fork; SSE loss and child restart do not duplicate actions; state survives update; scope/approval controls reject unauthorized deletion, force push and admin merge.',sources=('S308',),priority='P0',baseline='Compare the same task under failing provider connections against current ForgeCode/Codex behavior; do not use throughput as safety evidence.')
assert set(A)=={n for n in NAMES if not n.startswith('zz-')}

# End-of-pass identity changes. These are observations, not approved role changes.
CLOSING_RENAMES={
 'AirLock':'zz-aa-dep-AirLock',
 'zz-pause-AgsLag':'zz-inc-AgsLag',
 'zz-pause-RIPFitnessApp':'zz-inc-RIPFitnessApp',
 'zz-pause-VibeKanban':'zz-inc-VibeKanban',
 'zz-pause-Parpoura':'zz-inc-Parpoura',
 'zz-pause-QuadSGM':'zz-inc-QuadSGM',
 'zz-pause-SessionLedger':'zz-inc-SessionLedger',
 'zz-pause-ResearchLedger':'zz-inc-ResearchLedger',
}
MISSING_AT_CLOSE={'zz-aa-dep-MobileMcp'}
for sid,repo,blob in [
 ('S318','zz-inc-VibeKanban','2f962614372ea2c97a817e7f32ea75f1c6dfb2ea'),
 ('S319','zz-inc-AgsLag','fc90395ebbe81dec1338a5552dac5023205f7bc9'),
 ('S320','zz-inc-SessionLedger','c016858d85c827ce4d50a884dd299c1965b4674e')]:
 extra(sid,repo,'README.md','main',blob,note='closing-header recheck: new zz-inc name still carries the same paused/restricted README blob')
SOURCES['OBS-OPEN']={'id':'OBS-OPEN','kind':'connector_inventory_observation','url':'https://github.com/KooshaPari?tab=repositories','coverage':'Opening paged repository list/search, 62 stable IDs, 30 unprefixed names; normalized inventory, not raw API export or atomic snapshot.'}
SOURCES['OBS-CLOSE']={'id':'OBS-CLOSE','kind':'connector_inventory_observation','url':'https://github.com/KooshaPari?tab=repositories','coverage':'Closing list returned 61 stable IDs, 29 unprefixed; AirLock renamed and seven pause names became zz-inc. Missing MobileMcp remains unresolved. Sequential observation.'}
SOURCES['OBS-404']={'id':'OBS-404','kind':'connector_access_observation','url':'https://api.github.com/repos/KooshaPari/nanovms','coverage':'nanovms name and ID 1199379049 returned 404; clap-ext name returned 404; MobileMcp name and ID 1273002818 returned 404. No deletion conclusion.'}

H={}
def held(name,role,assessment,observed,next_action,acceptance,priority='P2',sources=()):
 H[name]={'role':role,'assessment':assessment,'observed':observed,'next_action':next_action,'acceptance':acceptance,'priority':priority,
          'source_ids':([SRCBY[name]] if name in SRCBY else [])+list(sources),
          'comparison_next':'No new full market pilot is required solely to preserve or support this repository. Compare retained contracts with the actual successor/upstream when disposition depends on equivalence.',
          'cvp_acceptance':'ROLE_SPECIFIC_CUSTODY_OR_CONSUMER_GATES; NOT_PRODUCT_CERTIFICATION'}
held('zz-tbd-Pheno','Unresolved organizational shelf','DO NOT USE AS AN UNADJUDICATED ABSORPTION TARGET',
 'The README calls it a shelf of about 30 independent repositories and adds a TBD merge-target header. That is a workspace organization model, not proof of one coherent product or canonical implementation.',
 'Inventory nested Git roots, separate dirty work and retained artifacts, and record a component-level destination map. Resolve the existing ban/exception history before any new imports.',
 'Every source capability and independent history is mapped; no recursive copy loses a nested repository; one approved owner per component; no deletion or broad merge authorization is implied.',priority='P0')
held('zz-tbd-PhenoApps','Unresolved collection containing the screen-time FocalPoint product','RECONCILE THE ACTUAL PRODUCT LINEAGE',
 'On apps-extract, one README simultaneously says compilation broken, builds green, and compilation still blocks production. It describes the actual screen-time/FocalPoint app, unlike the other FocalPoint repository. Adjacent PhenoObservability is required by the documented build.',
 'Compare actual branch/source/manifests with the separate FocalPoint ID and existing accepted product intent. Build in isolation with explicit dependencies before choosing a destination.',
 'Distinct capabilities, platform entitlements, private assets, data migrations and source history receive a disposition. Conflicting progress claims are replaced by one revision-specific observation.',priority='P0',sources=('S277',))
held('zz-tbd-PhenoSDKs','Unresolved shared SDK/observability collection','PRESERVE PACKAGES; DECIDE OWNERSHIP BY CONSUMERS',
 'The README says target undecided and lists Go SDK plus observability. Presence in a collection does not establish a compatible new package/versioning home.',
 'List module/import identities, real consumers, release obligations and provenance. Choose existing product or foundation owners by contract; avoid another generic utilities repository.',
 'Clean consumers resolve exact versions without old relative paths; package namespaces and licenses survive; old identifiers have deliberate compatibility treatment.')
held('zz-tbd-MobileCli','Mobile Next-derived device CLI under target review','KEEP FORK AND DEVICE CONTRACTS INTACT',
 'The source retains upstream mobilecli installation and device-control scope. The displayed license identifies FSL-1.1-Apache-2.0; this audit did not adjudicate its license terms or local patch delta.',
 'Identify required Eidolon/other consumers and compare actual mobile-device operations. Review the specific license and upstream relationship before porting or productizing.',
 'Selected physical/emulated-device paths work with consent and correct denial behavior; independent subprocess/API boundary, patches, distribution and license obligations are recorded.')
held('zz-pause-Thegent','Paused mixed bootstrap/labor/agent runtime','RETAIN PAUSE; DO NOT INHERIT ITS BROAD AUTHORITY',
 'The pause header coexists with 100% spec/test/trace, 60% active runtime and a broad dotfiles/bootstrap/multi-agent hub description.',
 'Preserve the latest restrictions and identify any existing consumers that need compatibility maintenance. Extract no new canonical authority from completion percentages.',
 'Current role and supported retained interfaces are explicit; historical labor/strategy intent remains traceable; no background worker resumes new product work from stale ACTIVE text.')
held('zz-pause-AgsLag','Strategy/executive lineage; newly renamed incubation candidate','INCUBATION NAME CONFLICTS WITH PAUSED CONTENT',
 'Closing list resolves this ID to zz-inc-AgsLag. Its refreshed README still says pause, pending merge into zz-agslag, and zz-agslag-dash retired. A new prefix did not resolve the actual strategy authority.',
 'Request/locate the exact accepted incubation decision and its bounded charter. Preserve the strategy/allocation responsibilities without silently assigning them to AgilePlus or a document ledger.',
 'One role, source lineage, owner, scope, graduation condition and allowed actions are explicit. No new work or deletion proceeds from the name alone.',priority='P0',sources=('S319','OBS-CLOSE'))
held('zz-pause-Parpoura','Founder/venture and governance lineage; incubation-name transition','VERIFY SEMANTIC SUCCESSOR BEFORE ANY RETIREMENT',
 'Earlier README says paused and migrated research documents to ResearchLedger, with venture Python superseded by AgilePlus and future deletion. Closing name is zz-inc-Parpoura; the new intended contract was not retrieved.',
 'Reconcile the scoped incubation/retirement decision. Separate copied research from executable venture behavior and verify any claimed successor with a matched consumer case.',
 'Every retained capability has explicit source/target responsibility and evidence; paused/retained obligations and new incubation are not conflated.',priority='P0',sources=('OBS-CLOSE',))
held('zz-pause-Localbase','Paused decentralized compute marketplace','KEEP RESEARCH/PRODUCT BOUNDARY DISTINCT',
 'The README describes Cosmos marketplace, provider/API and frontend subsystems under permanent pause.',
 'Preserve historical work and any authorized existing data. Do not silently import its marketplace/blockchain requirements into PhenoFabric or resume deployment.',
 'Custody, licenses, outstanding secrets/infrastructure and historical status are known. Future reuse requires a bounded accepted requirement, not name similarity.')
held('zz-pause-FocalPoint','Paused repository with ambiguous product lineage','DO NOT TREAT IT AS PROVEN SCREEN-TIME SUCCESSOR',
 'The header says paused and absorbed into PhenoTooling; the underlying description is dependency management. This differs from the FocalPoint product in PhenoApps.',
 'Resolve by repository IDs, historical paths and actual component/API behavior. Preserve distinct histories until the transfer map proves what each contains.',
 'No product feature or user data is declared redundant solely because the repository name matches. Any consumer migration passes a real test.',priority='P0',sources=('S269',))
held('zz-pause-QuadSGM','Governance template/history; incubation-name transition','CHARTER BEFORE RESTART',
 'Earlier header pauses a Python governance/template system with task, docs and QC tooling. Closing list now says zz-inc-QuadSGM; the corresponding decision was not established.',
 'Determine whether a bounded independent experiment is intended or the material remains reference for existing tools. Do not create a second portfolio policy authority.',
 'Document one authorized experiment, inputs/outputs and relationship to current tooling; preserve history and avoid conflicting enforcement.',sources=('OBS-CLOSE',))
held('zz-pause-SessionLedger','Session provenance/archive tool; incubation-name transition','PRESERVE DATA CONTRACT; RECONCILE ROLE',
 'The closing name is zz-inc-SessionLedger, but the refreshed header still says long pause. The retained tool advertises daemon, archive, replay and Dioxus viewer with some publication channels unfinished.',
 'Bind any revival to an explicit scoped decision. Consumers may use a qualified retained version without requiring a whole new product release; protect private captures and credential boundaries.',
 'Actual archive/restore and provenance verification retain session fidelity; live versus recorded state is distinct; paused obligations and new development permissions are explicit.',sources=('S320','OBS-CLOSE'))
held('zz-pause-ResearchLedger','Local-first research/vault app; incubation-name transition','PRESERVE VAULTS; VERIFY THE NEW CHARTER',
 'Earlier paused source describes a Tauri app with local Markdown/SQLite, browser captures and credential handling. Closing name is zz-inc-ResearchLedger; no live app or new charter was validated.',
 'Locate the accepted incarnation/owner decision; keep captures private and avoid mandatory dependencies from every product onto unfinished research integrations.',
 'Existing vault/import/export contracts remain readable and recoverable. New browser/native operations require consent, scoped fixtures and actual evidence.',sources=('OBS-CLOSE',))
held('zz-pause-VibeKanban','Reference upstream-derived planning UI; incubation-name conflict','EXPLICIT NO-DEVELOPMENT NOTICE STILL PRESENT',
 'Despite the closing zz-inc-VibeKanban name, its refreshed README still explicitly says reference/inspiration only and tells agents to stop unarchiving/developing it.',
 'Do not treat the prefix as permission. Locate an explicit human supersession before new work. Preserve usable reference material and fork provenance.',
 'Until a scoped supersession is established, no automatic development, new integration authority or retirement action; any approved experiment must state why it is needed.',priority='P0',sources=('S318','OBS-CLOSE'))
held('zz-pause-GitHub','Historical special-name account defaults repository','PRESERVE; CHECK PUBLICATION RESPONSIBILITY ELSEWHERE',
 'The paused README refers to the old .github repository and says archived/retired, while platform metadata says unarchived.',
 'Separate authored account policy from any necessary specially named GitHub publication surface. Do not recreate, rename or enable workflows without the accepted owner decision.',
 'Required default community files and workflow references are intentionally provided or intentionally absent; historical code is preserved and no inferred redirect is used as proof.')
held('zz-pause-RIPFitnessApp','Retired fitness app; incubation-name transition','CONFIRM WHETHER A REVIVAL WAS ACTUALLY AUTHORIZED',
 'Earlier header says permanent pause/retirement. Closing name is zz-inc-RIPFitnessApp, without a retrieved new product charter.',
 'Preserve the old application and identify a bounded new user job only if a scoped decision exists; no obligation to manufacture a CVP from coursework/history.',
 'Explicit owner and decision separate archival custody from an actual incubation task. Existing secrets and user data are handled privately.',sources=('OBS-CLOSE',))
held('zz-aa-dep-AgentApiPlusPlus','Maintained agent-process API fork','CONFLICTING RETAIN/DELETE INSTRUCTIONS',
 'The README simultaneously says owned hard-fork dependency, do not pause/delete/archive/merge, and migrated to substrate with future deletion.',
 'Reconcile one current decision and actual substrate/process-control consumers. Preserve upstream and local history and prove any claimed replacement is semantically equivalent.',
 'Real agent lifecycle, stream and error contracts work on pinned versions; no destructive transition is derived from the obsolete paragraph.',priority='P0')
held('zz-aa-dep-CliproxyApiPlusPlus','Maintained provider proxy fork','KEEP AS A DEPENDENCY WITH AN EXPLICIT DELTA',
 'The retained header and fork attribution are relatively clear: provider routing/auth/quota/diagnostics extensions of router-for-me/CLIProxyAPI.',
 'Publish the intentional patch set, upstream base, real consumer pins and install/update policy. Avoid duplicating upstream claims as evidence for the fork.',
 'Authentic provider streaming/cancellation/auth/limit cases pass; documented integrations resolve; fork-network history is protected.')
held('zz-aa-dep-Planify','Plane-derived PM dependency/candidate','PRESERVE; RESOLVE OUTDATED PRODUCT COMPARISON',
 'The dependency header coexists with a June PM-frontend competition against AgilePlus and Tracera, with no newly established decision in this read.',
 'Keep source provenance and licensing; identify actual consumers and whether this is an adapter, maintained fork or an approved future UI experiment.',
 'Pinned build and required API/upgrade contracts work. Do not let the old competition statement redefine Tracera or AgilePlus today.')
held('zz-aa-dep-Bifrost','Maintained Go AI gateway fork','KEEP CONSUMER-LED MAINTENANCE',
 'The retained header preserves maximhq/Bifrost attribution; the remaining large product claims and package routes largely describe upstream.',
 'Establish fork delta and exact deployed/imported versions in the route family, especially duplicated routing responsibility with OmniRoute and substrate.',
 'Representative request, stream, fallback, quota, permission and failure behavior is tested on the owned revision; package identity remains explicit.')
held('zz-aa-dep-MobileMcp','Mobile MCP fork/dependency with unresolved access','DO NOT CLASSIFY AS DELETED OR MIGRATED',
 'Present in the opening cohort, its README read and stable repository-ID lookup returned 404; it is absent from the closing 61-ID list.',
 'Have the authorized owner resolve access/transfer/removal and report the actual successor, consumers and preserved source receipts. Do not synthesize a successful migration.',
 'Identity and custody are established by authorized evidence; every current consumer either resolves the retained dependency or is explicitly blocked.',priority='P0',sources=('OBS-OPEN','OBS-CLOSE','OBS-404','W01'))
held('zz-aa-dep-PhenoMCPServers','Deployable MCP servers/skills/plugins catalog','QUALIFY FRAMEWORK AND CONSUMER RESOLUTION',
 'The README defines an implementations registry and legitimate catalog schema, but depends on old PhenoFastMCP locations not present in the opening roster.',
 'Locate the actual framework package source and pins. Keep runnable server packages separate from generated catalog projections and portfolio ownership.',
 'One selected server installs and interoperates with a real client, including malformed requests, cancellation, permission denial and missing backend handling.')
held('zz-aa-dep-UnityDoorstop','Unity early managed-loader fork','RETAIN PREBOOT/LOAD ORDER CONTRACT',
 'The fork exposes Unity Doorstop as an early .NET assembly loader with upstream workflow/artifact references.',
 'Pin the actual build consumed by Dino or other mods and document loader/runtime compatibility and local patches.',
 'The supported game/runtime loads the correct managed entrypoint once, fails safely when missing/incompatible, and preserves upstream notices and provenance.')
held('zz-aa-dep-TurboQuant','KV-cache compression research/engine dependency','VERIFY LOCAL APPLICABILITY, NOT JUST UPSTREAM CLAIMS',
 'The README carries extensive upstream adoption and quality/performance claims. Those experiments and external PRs were not re-executed or independently verified in this pass.',
 'Identify the exact codec/backend/model profile used by your products and reproduce bounded quality plus memory/latency evidence before adopting a default.',
 'Matched baseline shows reported quality/performance tradeoffs on real hardware; failure/OOM behavior, format compatibility and attribution are explicit.')
held('zz-aa-dep-PhenoUnslothStudio','Local training/inference studio fork dependency','KEEP THE FORK/CONSUMER BOUNDARY CLEAR',
 'The dependency header retains the upstream Unsloth Studio description and assets; it is not evidence of a separately qualified Phenotype product.',
 'Record intentional changes and a clean install path for the real model workflow using this fork. Do not fabricate branding or original performance ownership.',
 'A safe bounded train/infer/export flow succeeds with required versions, resources, model/data permissions and clear failure behavior.')
held('zz-aa-dep-CompoundSpheres3D','WorldSphereMod rendering dependency','VERIFY THREE-SOURCE MERGE AT THE CONSUMER',
 'The README calls it canonical and describes a three-source merge with upstream and WSM3D renderer lineage. Those claims need more than source folder presence.',
 'Resolve submodule/assembly pins and check the intended terrain/height-field/culling behavior in the actual game build.',
 'Selected source capabilities, assets and ABI are retained; render correctness/performance and failure cases pass against the known working baseline.')
held('zz-pause-ref-ProjectSpyn','Historical coursework/reference','CUSTODY ONLY',
 'The header says paused ASU FSE100 project, while inherited text claims all work migrated without a specific successor.',
 'Preserve history and explicitly mark unverified historical migration language. Do not create new CVP work.',
 'Recoverable source, license and historical identity are recorded; no claim that undocumented absorption is proven.')
held('zz-pause-ref-AtomsTech','Historical website/product reference','CUSTODY ONLY',
 'Paused/reference header sits above a generic archived/migrated notice with no target.',
 'Keep the reference with dated role and provenance. Identify any still-owned domain/credential obligations separately.',
 'Historical source remains recoverable, obsolete live claims are flagged, and no new product work or deletion is inferred.')
held('zz-pause-ref-AtomsBot','Strictly paused bot/reference','HONOR THE EXPLICIT FREEZE',
 'The README explicitly prohibits new commits, PRs, issues, releases, dependents and agent work without owner sign-off.',
 'Maintain read-only observation and external custody records. Do not edit the repository merely to satisfy a generic portfolio checklist.',
 'No automated mutation occurs; any future resumption requires explicit scoped supersession and appropriate credential review.')
held('zz-pause-ref-KaskMan','Historical reference repository','CUSTODY ONLY',
 'The README says no longer maintained and absorbed or irrelevant, without identifying precise target parity.',
 'Preserve; flag migration status as unverified rather than converting the sentence into retirement authority.',
 'Stable ID, history, retained artifacts and access are known; no manufactured application or quality target is added.')
held('zz-pause-ref-Synthia','Retired PAL/Zen MCP-derived reference','RESPECT THE NO-WORK NOTICE',
 'The top-level instruction says no longer needed/stop working, followed by upstream PAL MCP material.',
 'Retain as reference and distinguish upstream documentation from owned maintained capability. Do not resume bot/provider development.',
 'Source/upstream lineage and retained rights are recorded; no operational dependency is added without a new decision.')
held('zz-pause-ref-472P2FlameWar','Historical coursework/reference','CUSTODY ONLY',
 'The document has pause/retired boilerplate rather than an active product contract.',
 'Keep protected reference material and provenance; resolve any uncertainty outside the repository before changes.',
 'Historical identity and recovery are documented; no regression or CVP claim is invented from an inactive course project.')
held('zz-pause-ref-NetWeave','Paused traffic/network simulation reference','PRESERVE A REUSABLE IDEA WITHOUT FORCED ABSORPTION',
 'The source describes a Go traffic/road-network simulator and Canvas UI, with education, planning and possible game use under a pause header.',
 'Retain as reference. A future Civis reuse proposal must identify the exact algorithm and contract, not import an entire traffic product by analogy.',
 'Source and provenance remain available; no new engine scope, deleted duplicate or release obligation is inferred from conceptual relevance.')
assert set(A)|set(H)==set(NAMES)
assert not(set(A)&set(H))

# Explicitly preserve the research depth and evidence limitations.
COVERAGE={
 'scope':'Opening cohort of all 62 GitHub repository IDs, including the 30 opening unprefixed names requested by the user.',
 'observed_date':'2026-09-15',
 'observation_atomic':False,
 'opening_inventory_count':62,'opening_active_named_count':30,
 'closing_inventory_count':61,'closing_active_named_count':29,
 'readme_identity_coverage':61,
 'readme_coverage_note':'61 original IDs have bounded root README reads; one of those (AirLock) was read under its new name. MobileMcp was inaccessible. Some content responses are truncated; no full-file/full-repo completeness is implied.',
 'deep_sampling':'Selected manifests, source functions, workflow configuration, PR metadata and six latest-release endpoints; NOT exhaustive code/history/CI evaluation for every repository.',
 'native_product_tests_run':False,'installed_products_inspected':False,
 'local_worktrees_or_sessions_observed':False,'all_branch_histories_traversed':False,
 'all_hosted_checks_reviewed':False,'all_releases_or_package_registries_reviewed':False,
 'sota_pilots_executed':False,'deployments_or_dns_validated':False,
 'forensic_preservation_certified':False,'cvps_certified':0,
 'writes_to_github':False,
 'risk':'Sequential live reads can span distinct revisions. Main-branch source observations are bound to returned blob hashes where available, not all to a common commit. Closing names do not confer approval.',
 'verdict_semantics':'Assessment flags express the next acceptance gap or observed defect, not a numeric completion score or a claim that a product has never worked.'
}

def category(name):
 if name.startswith('zz-aa-dep-'): return 'dependency'
 if name.startswith('zz-pause-ref-'): return 'paused-reference'
 if name.startswith('zz-pause-'): return 'paused'
 if name.startswith('zz-inc-'): return 'incubation-named'
 if name.startswith('zz-tbd-'): return 'target-undecided'
 return 'active-named'
RECORDS=[]
for i,(name,rid) in enumerate(zip(NAMES,IDS),1):
 rec={'id':f'REP-{rid}','github_repository_id':int(rid),'cohort_index':i,'opening_name':name,
      'closing_name':None if name in MISSING_AT_CLOSE else CLOSING_RENAMES.get(name,name),
      'last_resolved_name':CLOSING_RENAMES.get(name,name),
      'opening_class':category(name),'opening_active_cohort':name in A,
      'closing_class':'access-unresolved' if name in MISSING_AT_CLOSE else category(CLOSING_RENAMES.get(name,name)),
      'opening_archived':False,'closing_archived':None if name in MISSING_AT_CLOSE else False,
      'visibility_observed':'private' if name in PRIVATE else 'public','default_branch_observed':BRANCH.get(name,'main'),
      'assessment_as_of':'2026-09-15','authority':'analyst recommendation, not an approved migration or lifecycle transition',
      'source_read_level':'bounded-root-plus-selected-source' if len((A.get(name) or H.get(name))['source_ids'])>1 else 'bounded-root',
      'coverage_missing':['local_state','full_history','native_execution','full_suite_coverage','current_deployed_artifact'],
      **(A.get(name) or H[name])}
 if name in MISSING_AT_CLOSE: rec['source_read_level']='inventory-and-access-failures'
 if name in CLOSING_RENAMES and name.startswith('zz-pause-'):
  rec['transition_caveat']='New incubation-like name is observed, not an accepted permission/role change. Previous root policy may remain in force; verify current scoped human decision.'
 RECORDS.append(rec)
assert len(RECORDS)==62 and len({r['github_repository_id'] for r in RECORDS})==62
CLOSING=[{'id':r['github_repository_id'],'name':r['closing_name'],'classification_by_name':r['closing_class'],'archived':r['closing_archived'],'visibility':r['visibility_observed'],'default_branch':r['default_branch_observed']} for r in RECORDS if r['closing_name']]
assert len(CLOSING)==61
assert Counter(x['classification_by_name'] for x in CLOSING)=={'active-named':29,'paused-reference':7,'paused':4,'incubation-named':7,'dependency':10,'target-undecided':4}
CHANGES=[]
for r in RECORDS:
 if r['opening_name']!=r['closing_name']:
  CHANGES.append({'repository_id':r['github_repository_id'],'opening_name':r['opening_name'],'closing_name':r['closing_name'],
     'classification':'unresolved-absence' if r['closing_name'] is None else 'identity-preserving-rename',
     'authorization_verified':False,'meaning':'Do not infer deletion, preservation parity, role approval or new work permission.'})

FINDINGS=[]
def finding(fid,title,status,severity,detail,impact,next_step,sids):
 FINDINGS.append({'id':fid,'title':title,'evidence_status':status,'severity':severity,'detail':detail,'impact':impact,'next_action':next_step,'source_ids':sids})
finding('F01','The live cohort changes while being evaluated','REMOTE_METADATA','P0',
 'Opening: 62 IDs/30 unprefixed names. Closing: 61 IDs/29 unprefixed, AirLock becomes a dependency and seven pause names become zz-inc. MobileMcp is not resolved. Refreshed VibeKanban, AgsLag and SessionLedger headers still say pause.',
 'Names and mutable counts cannot be a stable work queue or permission source.',
 'Preserve the 62-ID cohort; reconcile explicit decisions for the nine observation changes. Publish separate active, dependency, incubation, paused/reference and unresolved sets.', ['OBS-OPEN','OBS-CLOSE','S266','S318','S319','S320','W01'])
finding('F02','AgilePlus does not enforce its advertised all-language 85% coverage','SOURCE_CONFIRMED','P0',
 'The inspected workflow enforces Rust line coverage at 20%, enforces Python at 85%, prints Go coverage without a fail floor, and echoes the aggregate claim. These are configured controls, not measured coverage results.',
 'Successful workflow completion can overstate the accepted assurance contract. The inspected workflow also does not establish independent unit/integration/E2E metrics.',
 'Use approved denominator inventories, isolated suite measurements and real aggregate evaluation; seed below-threshold, missing and wrong-revision records and prove nonzero failure.', ['S239','S238'])
finding('F03','The documentation-health replacement is still a success-returning scaffold','SOURCE_CONFIRMED','P0',
 'docs-health counts Markdown files but leaves Vale, markdownlint and link detection TODO, emits empty findings and returns Ok. Its smoke test is empty.',
 'A consolidated tool can preserve or reintroduce the original false-green behavior; wrappers must not certify unexecuted checks.',
 'Implement or adapt real native checks; fail on missing required tools, traversal errors and broken fixtures; prove hosted failure propagation.', ['S304'])
finding('F04','Consolidation left active consumers pointing at inaccessible source locations','SOURCE_PLUS_ACCESS_LIMIT','P0',
 'PhenoFabric fetches a manifest crate from KooshaPari/nanovms; that name and ID 1199379049 are unavailable here. HeliosLab depends on clap-ext, whose old URL also returns 404, plus an old observability location.',
 'A cache-warm developer build may succeed while a clean checkout cannot resolve its dependencies. This audit has not executed a clean build or proved deletion.',
 'Verify source/API-equivalent successors and immutable dependency identity; perform cache-isolated fetch/build/consumer tests before retiring any old location.', ['S235','S315','OBS-404','W01','W04'])
finding('F05','Multiple repositories still expose overlapping source ownership','SOURCE_CONFIRMED_WITH_POLICY_OPEN','P0',
 'ShareCLI core lib.rs has identical Git blob cb35ab8d... in PhenoTooling and sharecli. PhenoTooling registers absorbed ShareCLI crates. PhenoAI registers Eidolon crates while Eidolon remains active.',
 'A deliberate mirror is possible, but a missing single-writer/release policy permits divergent fixes and reintroduces the duplication consolidation was intended to remove.',
 'Decide source owner, distribution/mirror contract, consumer pins and integration lead per capability; do not delete a copy solely because one file matches.', ['S312','S313','S314','S316','S253'])
finding('F06','Published release metadata is ahead of actual downloadable product evidence','REMOTE_RELEASE_METADATA','P0',
 'AgilePlus latest release Installers + green tests has no attached assets. Forgecode latest September 15 release has no assets. Jcode fork latest release returns only a FreeBSD x86_64 archive.',
 'Tags and release descriptions are not proof that the user can install the tested fork or desktop product on Mac/Windows. Other package channels were not exhaustively inspected.',
 'Resolve the actual distribution channel; bind source, build, signed artifact, install, update and run receipts. Qualify Mac/Windows channels actually used by the operator.', ['S309','S311','S308'])
finding('F07','Civis improved state persistence but the player build is still weakly specified','SOURCE_AND_RELEASE_METADATA','P1',
 'Commit 264359af adds populated archive round-trip cases and mirrors cultural/ideological/aggression/unrest state. The Mac script still builds a minimal Bevy feature set and permits absent assets. Latest stable is September 5 CLI archives.',
 'Substantive world correctness work is real; it does not establish game-first presentation, continuity or a qualified installed .app.',
 'Define required presentation/assets, build the real player artifact, and run create/play/intervene/save/quit/reopen plus bounded unattended continuation. Preserve subsystem determinism tests without globalizing them.', ['S300','S301','S302','S305'])
finding('F08','Forgecode integration did advance','REMOTE_PR_METADATA','P1',
 'Promotion PR #277, previously open in the September 11 audit, merged into main September 12 at 10:02:14 UTC. Current release has a newer tag but no attached binaries.',
 'This is verified integration progress, not evidence of a stalled worker. Installed artifact and current behavior remain separate questions.',
 'Test the actual current executable for session/search/readonly boundaries and streaming; publish and identify the same candidate, rather than reopening completed promotion work.', ['S307','S311','S254'])
finding('F09','Product identity still drifts away from the accepted intent','ROOT_CONTRACT_CONFLICT','P1',
 'Tracera is advertised as audit/observability rather than the canonical product graph. HeliosLab root/manifest describe mixed workbench/config identities. helios-cli excludes its vendored Codex implementation from the root workspace. Pine mixes 70% and 25%.',
 'Agents can pass a build for the wrong product surface or write more documentation for a changed goal without a decision.',
 'Name one current target and its public entrypoint; bind the exact acceptance journey and build profile. Preserve future intent without claiming it is shipped.', ['S244','S249','S315','S248','S256'])
finding('F10','PhenoAI minimum-toolchain claim conflicts with its resolver','SOURCE_PLUS_OFFICIAL_DOCS','P1',
 'The workspace selects resolver 3 while advertising rust-version 1.75. Official Cargo documentation requires Rust 1.84 or newer for resolver 3.',
 'The manifest cannot establish a coherent old-toolchain build promise. Native compatibility was not tested here.',
 'Choose and test the accepted minimum toolchain, member inheritance and lockfile behavior; fix the contract and implementation together.', ['S316','W03'])
finding('F11','Retained dependencies and paused repositories retain destructive or stale instructions','ROOT_CONTRACT_CONFLICT','P0',
 'AgentApiPlusPlus says both do not delete/merge and deprecated/will delete. Parpoura mixes pause, migration and deletion. Some current incubation-like names retain explicit no-work text.',
 'Workers can select whichever paragraph supports an action. A header or rename is not an authenticated decision record.',
 'Record latest scoped human decisions and supersession pointers in existing authority; constrain credentials separately; do not resume mass deletions or mass unpausing.', ['S284','S275','S318','S319','S320'])
finding('F12','A smaller count is not yet a proven simpler dependency graph','ANALYST_INFERENCE_FROM_SOURCE','P1',
 'The current 62-ID portfolio has fewer repository homes, but PhenoTooling now bundles broad subsystems, PhenoAI absorbs device code, and old dependency locations persist.',
 'Context width may have moved into wider workspaces and ambiguous package ownership instead of actually shrinking semantic change cost.',
 'Measure affected packages, duplicate implementations, dependency cycles, context/file footprint per change and clean consumer build time. Use package/applet boundaries before another repo-count target.', ['S312','S316','S235','S315'])
finding('F13','Some products have honest role-specific exceptions','ROOT_CONTRACT_EVIDENCE','P1',
 'CivicSurvival-public explicitly omits private generators/server and is not a third-party buildable snapshot. Eidolon distinguishes unsupported/default paths and an unshipped REST daemon. WorldSphereMod distinguishes CODE_LANDED and PROVEN.',
 'These boundaries should be retained, not erased to force a universal green score or artificial .app deliverable.',
 'Qualify the actual distributed mod, native driver or selected game profile, and explicitly model inaccessible producer evidence.', ['S262','S253','S257'])
finding('F14','Documentation/landing/observability migration needs a consumer proof, not another registry','SCOPE_GAP_AND_RECOMMENDATION','P1',
 'The current roster and source references do not by themselves demonstrate where the former PhenoDocs renderer, landing publication, journey verifier and retired framework dependencies are actually built and used.',
 'Renaming or copying a tooling package is not evidence of documentation deployment, private/public safety or preserved integration behavior.',
 'Identify existing canonical tool packages and content consumers, keep AgilePlus repo-scoped, and demonstrate one real docs/landing/app route with revision-linked product media. No new registry is required.', ['S232','S304','S264','S288'])

RELEASES=[
 {'repo':'Civis','tag':'v0.5.0','published_utc':'2026-09-05T11:37:26Z','assets':'Linux AMD64, macOS ARM64 and Windows AMD64 CLI archives','source':'S305','gap':'No current game-app acceptance established by these CLI assets.'},
 {'repo':'sharecli','tag':'v0.3.0','published_utc':'2026-07-05T02:45:13Z','assets':'macOS ARM64 and Linux AMD64 archives plus checksums (uploaded July 14)','source':'S306','gap':'Map the current source/UI changes to an actual candidate; old release is not current-source proof.'},
 {'repo':'AgilePlus','tag':'v2026.09.0','published_utc':'2026-08-22T04:44:13Z','assets':'None attached in returned release','source':'S309','gap':'Title promises installers; resolve actual artifact channel and clean installation.'},
 {'repo':'forgecode','tag':'v2.13.21-h.0.2.1','published_utc':'2026-09-15T09:19:49Z','assets':'None attached in returned release','source':'S311','gap':'Integration and tag exist; verified installable fork channel not established.'},
 {'repo':'jcode','tag':'v0.85.0-k1.0.0','published_utc':'2026-09-15T04:59:14Z','assets':'One FreeBSD x86_64 archive','source':'S308','gap':'Mac/Windows fork distribution and installed identity need actual receipts.'},
 {'repo':'Tracera','tag':'v0.49','published_utc':'2026-09-03T08:24:33Z','assets':'Windows archive and release manifest','source':'S310','gap':'Scorecard checkpoint is not qualified proof of current product-graph frontend/backend.'},
]
WORK=[
 ('WP01','Reconcile current ID and decision projection','PhenoRegistry + portfolio coordinator',[],['F01','F11'],
  'Resolve the seven incubation transitions, AirLock role and MobileMcp access. Preserve original cohort. Do not create a new registry.',
  'One ID-keyed current map with explicit unknowns, decision provenance and allowed actions; latest no-work restrictions cannot be overridden by a prefix.'),
 ('WP02','Qualify the verification instruments','AgilePlus + PhenoTooling owners',[],['F02','F03'],
  'Repair real coverage aggregate and docs-health checks in isolated branches; reuse existing native instruments.',
  'Known missing/below-threshold/wrong-revision/empty-suite/broken-link fixtures fail locally and hosted. No blanket waivers or echo success.'),
 ('WP03','Close source/dependency migration gaps','PhenoFabric + HeliosLab + PhenoInfra/package owners',[],['F04','F10'],
  'Locate API-equivalent dependency sources, recorded pins and supported toolchains; verify clean resolution with no warm checkout.',
  'All selected manifest/FFI/consumer builds succeed from an isolated fetch and the correct supported toolchain, or have exact owned blockers.'),
 ('WP04','Resolve duplicate writer and release ownership','sharecli + Eidolon + PhenoTooling + PhenoAI leads',[],['F05','F12'],
  'Declare per-package single writer, mirror/distribution policy, consumers and source history. Freeze conflicting writers, not useful independent work.',
  'One known authority per live capability; integration strategy and parity tests before retiring copies.'),
 ('WP05','Qualify installed Civis game candidate','Civis product/integration owner',[],['F07'],
  'Use current accepted game-first horizon and required graphics/audio/assets. Preserve new persistence tests and run the player path outside the checkout.',
  'Install/launch, meaningful play/intervention, save/quit/reopen and bounded continuation all pass; exact build/profile and honest visual review attached.'),
 ('WP06','Qualify actual coding harness fork channels','forgecode + jcode + helios-cli owners',[],['F06','F08','F09'],
  'Choose actual executable/build root, package it and verify current installed identity; preserve completed Forgecode promotion.',
  'Clean supported-host install/update, session continuity, streaming recovery and negative scope tests pass on the distributed artifact.'),
 ('WP07','Qualify reusable AgilePlus/PhenoDocs delivery','AgilePlus + accepted docs/landing consumer owners',['WP02'],['F02','F06','F14'],
  'Prove repository-scoped work receipts and unrelated-project tooling use. Locate actual PhenoDocs renderer/publishing owner and qualify one site.',
  'No hardcoded portfolio state; docs build with links/private-data checks; one real CLI/MCP/desktop work journey and correct published artifact.'),
 ('WP08','Qualify Tracera as the intended product graph','Tracera owner',[],['F09'],
  'Resolve identity, then execute persistent product import/navigation/gap discovery on the actual frontend/backend profile.',
  'A real product model survives restart and exposes a genuine missing capability with evidence; supporting logs do not replace product identity.'),
 ('WP09','Run a real routing/inference/evaluation chain','OmniRoute + substrate + PhenoMLX + portage + PhenoLab owners',[],['F09','F12','F13'],
  'Use existing pinned providers/backends and selected workload; keep internal fork delivery distinct from upstream contribution.',
  'Successful and known-negative task results, auth/cancel/fallback/budget behavior and measured resource/quality outcomes are retained.'),
 ('WP10','Qualify native game/graphics/creative consumers','Dino + WorldSphereMod + PhenoGfx + Melosviz owners',[],['F13'],
  'Use supported installed game/media targets and actual assets; qualify shared dependency boundaries without relabeling mocks as live.',
  'Real consumer task, errors, persist/reopen and uninstall/export behavior are demonstrated. Copyright/licensing, hardware and source provenance explicit.'),
 ('WP11','Close privacy, publication and brand truth','KooshaPari + accepted landing/design owners',[],['F06','F14'],
  'Repair stale product/download identities from qualified records, preserve upstream attribution and inspect actual editable asset ownership.',
  'Public pages route to intended products, no private captures escape, metrics have query provenance, and current art/screenshots match actual products.'),
 ('WP12','Keep retained forks and paused/reference scope safe','Dependency maintainers + coordinator',[],['F01','F11'],
  'Apply role-specific maintenance/custody, verify active consumers and resolve explicit no-work supersessions without mass operations.',
  'No unapproved deletion/archive/branch rewrite; unknown custody remains unknown; meaningful retained interfaces work or are explicitly blocked.'),
]
WORK=[{'id':i,'title':t,'owner_role':o,'hard_dependencies':d,'finding_ids':f,'scope':s,'acceptance':a,'effort_estimate':None,'status':'PROPOSED_NOT_CLAIMED','write_authority':'requires existing scoped owner authorization; this audit grants none'} for i,t,o,d,f,s,a in WORK]

# Write machine-readable outputs, using normalized observations rather than pretending
# these data structures are raw GitHub API payloads.
def write(path,text):
 p=ROOT/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
def jwrite(path,obj):write(path,json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
jwrite('records/repository-assessments.json',{'schema_version':'1.0','coverage':COVERAGE,'repositories':RECORDS})
jwrite('records/opening-inventory.json',[{'id':r['github_repository_id'],'name':r['opening_name'],'classification_by_name':r['opening_class'],'archived':False,'visibility':r['visibility_observed'],'default_branch':r['default_branch_observed']} for r in RECORDS])
jwrite('records/closing-inventory.json',CLOSING)
jwrite('records/identity-changes.json',CHANGES)
jwrite('records/findings.json',FINDINGS);jwrite('records/release-observations.json',RELEASES);jwrite('records/next-work.json',WORK)
jwrite('evidence/sources.json',list(SOURCES.values()));jwrite('records/coverage.json',COVERAGE)
with (ROOT/'records/repository-assessments.csv').open('w',newline='',encoding='utf-8') as f:
 fields=['github_repository_id','opening_name','closing_name','opening_class','closing_class','visibility_observed','role','assessment','priority','observed','next_action','acceptance','source_read_level','cvp_acceptance','source_ids']
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in RECORDS:w.writerow({k:(';'.join(r[k]) if isinstance(r.get(k),list) else r.get(k)) for k in fields})

METHOD = '''This is a bounded, read-only current-state evaluation, not certification of all code or a new migration order. The opening scope is all 62 repository IDs requested by the user. The 30 unprefixed names are an observed candidate cohort matching the user's stated active count; no current approved 30-item policy roster was independently established. A later list returned 61 IDs and 29 unprefixed names. The report retains the opening cohort and records later identity/access differences.

The audit read bounded root documentation for 61 of the original IDs, including AirLock under its renamed identity. MobileMcp could not be read and did not resolve by ID. Selected source, manifests, workflow configuration, six latest-release records and a prior promotion PR were examined more deeply. A source excerpt can prove a specific implementation or configuration defect. A README can prove that a claim or contradiction is present, not that the feature works or fails at runtime.

No native product suites, full branch histories, local worktrees, live agent sessions, deployment/DNS settings, all CI/check/review states, package registries, graphical apps or real benchmark/pilot programs were executed or exhaustively inspected. No approved product CVP is certified by this pass; that is an audit scope limit, not a finding that none of the products works.

The record is sequential. References to main name the branch read and record the returned file blob where available. They do not mean that all source came from the same immutable repository head. Latest-release data is endpoint metadata from the observation, not a universal inventory of all versions and distribution channels. All native-run and preservation conclusions that need more evidence remain open.

The 62-row assessment is complete as a triage and next-acceptance map. Code, test, deployment, UX, security and history completeness for every repository is not claimed. The next work is evidence completion and bounded CVP delivery, not a repeat of this full audit on unchanged repositories.'''

SUMMARY = '''The reduction in repository count is real as an observed organization change, but the audit does not establish that semantic complexity, maintenance burden or installation friction fell by the same amount. Several source owners remain duplicated, active consumers still point to unavailable old locations, and important checks still fail to enforce their advertised contracts.

The highest-leverage action is not another consolidation batch. Close three kinds of gap: (1) the current ID/role/decision map and dependency resolution; (2) trustworthy assurance instruments; (3) a small number of real installed product candidates. Keep the existing workers and useful work, but require a bounded parent outcome and an independent proof artifact.

Useful progress is visible. Forgecode's former promotion PR is now merged into main. Civis has new source-backed archive-persistence work with populated round-trip assertions. Several repositories honestly distinguish code landed, unsupported, or unshipped paths. These improvements should be preserved rather than swept into another reset.

The headline remains: fewer repositories is not yet the same as fewer competing authorities, fewer unsupported claims, or more current viable products. Give each active target its correct role-specific acceptance test. Give dependencies a pinned consumer contract. Give held and historical work safe custody, not a manufactured product release.'''

INTERPRETATION = '''Priority P0 means an observed trust, dependency, safety or ownership issue can undermine downstream acceptance. It is not an instruction to start every P0 task simultaneously. P1 is product qualification or an important contract correction; P2 is bounded research or retained/reference maintenance. Priorities and dispositions here are recommendations, not approved work assignments.

SOURCE_CONFIRMED means the inspected bytes or configuration support the precise finding. REMOTE_METADATA means the connector reported the property or state; it is not a runtime test. ROOT_CONTRACT_CONFLICT means instructions or claims disagree, not that the underlying application was proved broken. ACCESS_UNRESOLVED is not deletion. ANALYST_INFERENCE is a conclusion whose alternatives remain explicit.

There are no aggregate completion percentages. Eighty-five percent is a coverage floor in the accepted assurance policy, not a numerical score this audit assigns to a product. A task, PR, integrated revision, verified artifact, published release and adopted installation are distinct states.'''

ACCEPTANCE = '''Carry forward the already accepted assurance and delivery contracts. Do not weaken them to get a green badge, and do not restart their documentation generation. A product candidate must identify its current accepted horizon, public entrypoint, build profile, platforms, required assets, state ownership and real consumer journey.

Unit, integration, E2E and each other required assurance family need independent coverage and meaningful denominators at their accepted floors (at least 85% unless an existing contract is stronger). Critical obligations and selected mandatory checks must all pass. Union coverage, skipped suites, missing backends, empty tests, copied badges and self-declared percentages do not meet those conditions. Unsupported measurements become explicit instrument work or an authorized exception, never a fabricated result.

Documentation acceptance means complete applicable intent/spec/architecture/operations contracts, source-backed SOTA, executable examples, current version/source links and honest status. Preserve richer existing prompt scrapes and provenance systems. A renamed or copied docs checker must demonstrate that it actually detects bad input. PhenoDocs and AgilePlus remain reusable tools; the subject repository owns its own content/state under the accepted contract.

A pilot compares one bounded real job against rational alternatives, with controls and negative results. A case study proves an intended user can install, use, recover and understand the actual product. The candidate comparisons listed on the product cards are recommended next experiments, not completed competitor research.

For macOS desktop products, use the installed .app outside the checkout, not dev mode. Qualify the correct assets/features, resource use, UI states, accessibility, persistence and recovery. For CLI/tools, use real installations, clean stdout/machine formats and VHS plus native result assertions. For libraries, use real consumer packages. For mods, use the supported installed game and distribution path. For infra, prove provision/run/failure/cleanup/restore. For research systems, prove the specified experiment rather than inventing a desktop shell.

Keep real product recordings separate from authored branding/illustrations. Do not let synthetic screens, stub backends or promotional edits become product evidence. Keep private captures out of public site/search artifacts. Bind source revision, profile, artifact digest, verification run and published route. Protect foreground games and Ableton by global resource admission; coverage instrumentation and uninstrumented performance runs remain separate.

No irreversible lifecycle action is authorized by this report. Existing source retention and fork-network no-delete constraints stand. An incubation rename is not a human supersession. A held dependency can remain supported without new product development, and a reference repository need not be rebuilt merely to satisfy a generic template.'''

ORDER = '''Do not serialize every independent product behind rebuilding the entire governance ecosystem. Run a small assurance/dependency lane and a small CVP lane in parallel, bounded by real review, native-platform and hardware capacity. Reconcile duplicate writer ownership before overlapping source edits, not by halting unrelated work.

First resolve current IDs and permission-changing decisions, then assign the two trust repairs (AgilePlus coverage and PhenoTooling docs-health) to their current owners. In parallel, close source-resolution failures for the Fabric/Infra/HeliosLab consumers and settle the explicit ShareCLI/Eidolon source-writer boundary.

For visible user value, pick one GUI/game candidate and one operator tool candidate from current runnable evidence. Civis is a strong GUI/game candidate because useful world work exists and the packaging profile is concrete. Forgecode or ShareCLI is a strong operator-tool candidate. The final choice depends on the local installed state not visible in this audit; do not start all three merely because they are named here.

The next outcome should be a tested current artifact you can install and use, not an empty release or another hundred-page specification. A known integration that already landed (such as Forgecode #277) should not be redone. An inherited target-blocking defect should remain owned, even when a narrow PR did not introduce it.

For migration work, source workers prepare the component transfer and destination workers own integration. A family lead owns the joint outcome. Unique worktrees, locked shared-manifest edits, exact base revisions and receipt-aware retry are required. Do not let a lost harness connection cause blind resubmission of a mutation.

Report installed CVPs, independently verified capabilities, release-to-installed revision lag, unresolved source locations, stale role decisions, test-instrument defects, escaped installed defects, and active outcome WIP. Do not optimize commit counts, branch counts, document counts or raw repository counts as substitute outcomes.'''

HANDOFF = '''# Continue from this audit; do not restart it

You own the existing assigned repository/capability scope. This handoff grants no new authority to merge, publish, create/delete/archive/rename repositories, rewrite refs or change security policy. Preserve current work and scoped decisions. It supplements the existing CVP, assurance, delivery and migration contracts.

1. Resolve the assigned repository by stable GitHub ID and verify its current name, head, local worktree and active owner. The original audit cohort has 62 IDs; the closing remote list had 61. Do not silently replace missing IDs or decide that a 404 means deletion.
2. Read the corresponding row in records/repository-assessments.json. Recheck changed facts at the actual head. Reuse valid prior evidence; do not regenerate a large generic docset.
3. For zz-inc names, locate the exact accepted incubation decision. Names do not supersede pause/no-work instructions. For dependency/reference repos, use consumer/custody gates rather than inventing an independent product release.
4. Return a one-page outcome gap: accepted role, current viable horizon, source/build/verified/published/installed revisions, required proof, remaining dependencies, permission envelope, and next bounded work package.
5. Implement only ready, authorized work that advances that outcome. Keep PRs narrow, but inherited repository-local blockers remain owned. A repair PR is not the parent outcome.
6. Retain independent unit/integration/E2E and other required coverage floors. Prove required checks run, fail for meaningful negatives and propagate nonzero results. Do not mask failures, narrow denominators or replace unavailable tools with success.
7. Resolve real package/API equivalence before replacing old dependency URLs. A crate name or copied folder is not parity. One source/release owner per capability; explicit mirror policy if more than one distribution is intended.
8. For a current desktop/game candidate, install outside the checkout and execute the user journey with real graphics/audio/assets and persistence. For CLI/library/mod/infra/lab targets, use their actual consumer/distribution form. Record limitations instead of fabricating UI or fixtures as production proof.
9. Bind results to exact source revision, build profile, environment and artifact digest. Keep native test, hosted test, release and installed behavior separate. Pilot/case-study outcomes must use real evidence and report negative/inconclusive results honestly.
10. Record explicit blockers with owner, next action and wakeup condition. Continue other safe ready work or release the execution slot. Never turn a blocked target into a completed target.

Specific starting repairs: AgilePlus's actual coverage enforcement; PhenoTooling's unimplemented docs-health checker; Fabric/HeliosLab clean dependency resolution; ShareCLI and Eidolon writer/release ownership; current fork install channels; Civis's actual player profile. Recheck before fixing because the portfolio is actively changing.

Completion report: work-package state, PR state, integrated state, required evidence state, release/install state and parent-outcome state. This is not a request to create another dashboard or universal registry.
'''
write('report/AGENT-HANDOFF.md',HANDOFF)

# Build readable Markdown from the same assessment records.
md=['# Phenotype portfolio evaluation: the 62-ID / 30-active cohort','',
    '**Read-only observation date: September 15, 2026.** Original cohort preserved; closing observation 61 accessible IDs / 29 unprefixed names.','',
    '## Executive assessment',SUMMARY,'## Scope and evidence',METHOD,'## Reading the verdicts',INTERPRETATION,
    '## Inventory changed during the audit',
    '| Measure | Opening | Closing |','|---|---:|---:|',
    '| Accessible/listed repository IDs | 62 | 61 |',
    '| Unprefixed active-named candidates | 30 | 29 |',
    '| Dependency-named repositories | 10 | 10 |',
    '| Paused, including reference | 18 | 11 |',
    '| Incubation-named | 0 | 7 |',
    '| Target-undecided | 4 | 4 |',
    '| Platform archived=true | 0 | 0 |','',
    'These are name/metadata observations, not accepted role approvals or measured product readiness. Original MobileMcp is retained in the audit as access-unresolved.','',
    '| Repository ID | Opening identity | Closing identity |','|---|---|---|']
for c in CHANGES:md.append(f"| {c['repository_id']} | `{c['opening_name']}` | `{c['closing_name'] or 'NOT RESOLVED'}` |")
md+=['','## Findings']
for f in FINDINGS:
 md += [f"### {f['id']} — {f['title']}",f"**{f['severity']} · {f['evidence_status']}**",f['detail'],f"**Why it matters:** {f['impact']}",f"**Next:** {f['next_action']}",f"**Evidence:** {', '.join(f['source_ids'])}",'']
md+=['## Release observation boundaries','Only these six latest-release records were sampled. Automatic source archives are not native binaries. Empty assets do not prove that another package channel is empty. No asset was installed in this pass.','',
 '| Repository | Latest endpoint tag | Published UTC | Observed attached assets |','|---|---|---|---|']
for x in RELEASES:md.append(f"| {x['repo']} | {x['tag']} | {x['published_utc']} | {x['assets']} [{x['source']}] |")
md+=['','## The original 30 active-named projects']
for r in [r for r in RECORDS if r['opening_active_cohort']]:
 md += [f"### {r['cohort_index']:02d}. {r['opening_name']} — {r['assessment']}",f"**Stable ID:** {r['github_repository_id']} · **Role:** {r['role']} · **Priority:** {r['priority']}",
        f"**Observed:** {r['observed']}",f"**Next useful outcome:** {r['next_action']}",f"**Acceptance proof:** {r['acceptance']}",f"**Next comparative pilot:** {r['comparison_next']}",f"**Sources:** {', '.join(r['source_ids'])}",'']
md+=['## The other 32 original repositories: role-specific assessment']
for r in [r for r in RECORDS if not r['opening_active_cohort']]:
 md += [f"### {r['cohort_index']:02d}. {r['opening_name']}",f"**Stable ID:** {r['github_repository_id']} · **Closing name:** {r['closing_name'] or 'UNRESOLVED'} · **Assessment:** {r['assessment']}",
        f"**Observed:** {r['observed']}",f"**Next:** {r['next_action']}",f"**Acceptance:** {r['acceptance']}",f"**Sources:** {', '.join(r['source_ids'])}",'']
md+=['## Acceptance contract carried forward',ACCEPTANCE,'## Execution order and WIP',ORDER,'## Proposed next work']
for w in WORK:
 md += [f"### {w['id']} — {w['title']}",f"**Owner role:** {w['owner_role']}",f"**Hard prerequisite:** {', '.join(w['hard_dependencies']) or 'None specified; local preflight and authority still required'}",w['scope'],f"**Acceptance:** {w['acceptance']}",f"**Linked findings:** {', '.join(w['finding_ids'])}",'']
md+=['## Evidence/source register','Sources are normalized connector/web observations. A source URL can subsequently redirect or change; returned blob IDs and pinned commits are retained where available. Body excerpts and full raw API responses were not all exported. None of these records alone authenticates a human approval.','']
for sid,s in SOURCES.items():
 label=(s.get('observed_repository','')+' '+s.get('path','')).strip() or s['kind']
 md.append(f"- **{sid}** — [{label}]({s['url']}); ref `{s.get('ref','n/a')}`, blob `{s.get('blob_sha') or 'not captured / not applicable'}`. {s.get('coverage','')}")
write('report/PORTFOLIO-EVALUATION.md','\n\n'.join(md)+'\n')
write('README.md','''# Portfolio 62/30 evaluation — September 15, 2026

Start with `report/PORTFOLIO-EVALUATION.pdf` or the editable Markdown beside it.

The original 62-ID cohort and original 30 active-named candidates remain intact. A closing inventory returned 61 IDs / 29 unprefixed names, with identity and access changes recorded separately. Names are not approval authority. No repository or native application was modified or executed by this audit.

- `records/repository-assessments.json` and `.csv`: all 62 individual assessments.
- `records/opening-inventory.json`, `closing-inventory.json`, `identity-changes.json`: normalized observed metadata and transitions, not raw API exports.
- `records/findings.json`, `release-observations.json`, `next-work.json`: actionable evidence-backed triage.
- `records/coverage.json`: exact audit limitations.
- `report/AGENT-HANDOFF.md`: short continuation instructions without restarting the program.
- `evidence/sources.json`: source locations and returned identities.
- `checks/`: package-consistency and PDF-layout checks; these are not product tests or product coverage.

No HTML dashboard, new registry, repo-count quota, fabricated pilot result, native product certification or destructive authorization is included.
''')
