from pathlib import Path
from datetime import datetime,timezone
import sys,json,shutil
ROOT=Path('/mnt/data/agent-lab-assessment-dossiers-v1.1')
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'tools'));import dossier
pep=dossier.pep
sys.path.insert(0,str(ROOT/'core-v1.0/tools'));import demo_loop
NOW=datetime.now(timezone.utc).isoformat()
CAT=pep.load_json(pep.ROOT/'catalog/catalog.json');CS={c['id']:c for c in CAT['criteria']}
def write(p,x):dossier.write(p,dossier.dumps(x))
def row(cid,state,note,action='Collect the actual product evidence before accepting this claim.',mandatory=False,gate=None,title=None,app='APPLICABLE',fresh='CURRENT'):
 return dict(cid=cid,state=state,note=note,action=action,mandatory=mandatory,gate=gate,title=title or CS[cid]['predicate'].rstrip('.'),app=app,fresh=fresh)
def axis(a,s,b):return {'axis':a,'status':s,'basis':b}
def inventory(item,declared,observed,gap):return {'item':item,'declared':declared,'observed_or_assumed':observed,'gap':gap}

def context(ident,title,subtitle,purpose,boundary,beneficiary,stage,next_action,stop,rows,inv,**kw):
 return {'kind':'dossier','schema_version':'1.1.0','id':ident,'record_status':'EXAMPLE','example_class':kw.get('example_class','ILLUSTRATIVE_SCENARIO'),
 'title':title,'subtitle':subtitle,'purpose':purpose,'boundary':boundary,'beneficiary':beneficiary,
 'authorship':kw.get('authorship','AGENT_ORIGINATED'),'intent_status':kw.get('intent_status','Accepted for a bounded experiment within the fictional scenario; not an actual portfolio commitment.'),
 'genesis_rationale':kw.get('genesis','This fictional repository was created by agents to isolate a consumer-facing capability. Its boundary is a hypothesis, not proof that a separate repository is necessary.'),
 'alternatives':kw.get('alternatives',['Implement the capability in an existing owner','Use a suitable existing dependency','Run a narrower experiment','Do not build']),
 'authority':kw.get('authority','Illustrative delegated mandate only. No actual device, repository, deployment, financial, or lifecycle authority is granted by this example.'),
 'non_goals':kw.get('non_goals',['Claim real-repository completion','Require a human-authored repository idea','Wait for a central registry to become operational']),
 'subject_identity':{'source_revision':None,'identity_method':'PEP value digest of subject.json (an authored scenario descriptor), not a Git commit or runtime artifact.','limitation':'No source checkout, real product execution, or real user observations were collected for this illustrative case.'},
 'inventory':[{'id':f'INV-{n:02d}',**x,'evidence_basis':'Authored scenario premise, not a collected product observation.'} for n,x in enumerate(inv,1)],
 'maturity':{'scenario_or_scoped_label':stage,'claim_limit':'Illustrative stage interpretation only. The current evidence-backed result is not a real-product maturity finding.','axes':kw.get('axes',[]),'value_evidence':kw.get('value','No actual consumer value evidence is included. The case distinguishes a plausible intent from a validated benefit.')},
 'finding_ids':[],'decision_ids':['DEC-NEXT'],
 'semantic_reviews':kw.get('reviews',[{'topic':'Does this assignment serve the parent outcome?','assessment':'Judge the named consumer outcome rather than the existence of infrastructure or the size of the repository.','support':'The fictional scenario names a bounded consumer and a failure that would prevent its outcome.','countercase':'The same outcome may be served more cheaply by an existing owner, a smaller feature, or no new product.','discriminator':'Execute the smallest real consumer journey under the same success and failure conditions.','confidence_basis':'Reasoned interpretation of the supplied fictional premises; no empirical product confidence is claimed.'}]),
 'next_action':next_action,'stop_condition':stop,
 'restart_packet':{'accepted_baseline':kw.get('baseline','Use this fixture as an example only; establish a real pinned subject and assignment before operational work.'),
 'failed_hypotheses':kw.get('failed',['A well-formed record is not proof the product behavior occurred.']),
 'next_reproduction':kw.get('reproduce','Translate the scenario into a bounded authorized real-product experiment, then replace fictional premises with collected observations.'),
 'budget_and_permissions':'No product mutation or external actions authorized by this package. Carry forward the actual cumulative budget and permissions from the operating mandate.'},
 'lineage':{'previous_dossier_id':kw.get('previous'),'change_class':kw.get('change','ILLUSTRATIVE_BASELINE'),'description':kw.get('delta','A constructed teaching case, not a measurement of changes in the user portfolio.')},
 'provenance_notice':kw.get('notice','Fictional worked example. Every purported product outcome below is an authored premise. Result records remain PROPOSED and instrument qualifications are absent, so the real evidence reducer grants no acceptance credit.'),
 'row_notes':[{'instance_id':f'I-{n:02d}','title':r['title'],'interpretation':r['note'],'next_action':r['action']} for n,r in enumerate(rows,1)]}

def build_scenario(slug,d,rows,disposition='IMPROVE',subject_key=None):
 base=ROOT/'examples'/slug;base.mkdir(exist_ok=False)
 for p in ['results','evidence','qualifications','raw','measurement-bindings','findings','decisions']:(base/p).mkdir()
 subject={'example_class':'ILLUSTRATIVE_SCENARIO','subject_key':subject_key or d['id'],
          'material':'Authored case descriptor only; not source code, a deployment or a Git revision.'}
 write(base/'subject.json',subject);sd=pep.value_digest(subject)
 evaluator=pep.file_digest(Path(__file__))
 premise={'example_class':'ILLUSTRATIVE_SCENARIO','product_execution_performed':False,
          'notice':'All states are authored premises for explaining a filled audit. This is not a test transcript, consumer observation, or instrument qualification.',
          'rows':rows}
 write(base/'raw/scenario.json',premise)
 a={'kind':'assignment','schema_version':'1.0.0','id':'A-'+d['id'],'record_status':'EXAMPLE','epoch_id':'E-'+d['id'],
    'status':'LOCKED','subject_id':subject['subject_key'],'subject_digest':sd,'mandate_ref':'SCENARIO-MANDATE-NOT-ACTUAL-AUTHORITY',
    'intent_ref':'dossier.json','catalog_digest':pep.file_digest(pep.ROOT/'catalog/catalog.json'),'profile_id':'web' if 'dashboard' in slug else 'bootstrap',
    'coverage_statement':f'{len(rows)} deliberately selected criteria for this fictional bounded slice. Other catalog criteria remain unassessed; omitted is not not-applicable.',
    'created_at':NOW,'scope_review_status':'ACCEPTED','scope_review_ref':'SCENARIO-SCOPE-ASSUMPTION','instances':[],'gates':[]}
 gates={}
 for n,r in enumerate(rows,1):
  iid=f'I-{n:02d}'
  a['instances'].append({'id':iid,'criterion_id':r['cid'],'criterion_revision':'1.0.0','obligation_key':r['cid'],
   'scope':d['boundary'],'applicability':r['app'],'applicability_reason':'Capability is required by the stated fictional slice.' if r['app']=='APPLICABLE' else r['note'],
   'applicability_decision_ref':'SCENARIO-SCOPE-ASSUMPTION' if r['app']!='UNRESOLVED' else None,'weight':1,
   'mandatory':r['mandatory'],'measurement_binding_ref':f'measurement-bindings/MB-{iid}.json'})
  if r['gate']:
   assert r['mandatory']
   gates.setdefault(r['gate'],[]).append(iid)
 a['gates']=[{'id':g,'required_instance_ids':ids} for g,ids in gates.items()]
 write(base/'assignment.json',a);ad=pep.file_digest(base/'assignment.json')
 ev={'kind':'evidence','schema_version':'1.0.0','id':'EV-SCENARIO','subject_digest':sd,'path':'raw/scenario.json',
     'digest':pep.file_digest(base/'raw/scenario.json'),'observed_at':NOW,'sensitivity':'PUBLIC','role':'OBSERVATION','origin':'EXTERNAL_REFERENCE',
     'summary':'Reference to authored fictional premises only. No product observation or execution was performed.'}
 write(base/'evidence/EV-SCENARIO.json',ev)
 rids=[]
 for n,r in enumerate(rows,1):
  iid=f'I-{n:02d}';rid='R-'+iid
  binding={'kind':'measurement-binding','schema_version':'1.0.0','id':'MB-'+iid,'record_status':'EXAMPLE','created_at':NOW,
    'criterion_id':r['cid'],'instance_id':iid,'subject_scope':d['boundary'],'modality':CS[r['cid']]['modality'],
    'method':'PROPOSED PROCEDURE ONLY: '+CS[r['cid']]['measurement_procedure'] if 'measurement_procedure' in CS[r['cid']] else 'PROPOSED PROCEDURE ONLY: collect evidence directly relevant to '+r['title'],
    'expected_behavior':CS[r['cid']]['predicate'],'units_or_anchors':'Pass only the stated predicate at the accepted scope; otherwise fail, abstain, or record a measurement blocker.',
    'environment_ref':'No product environment was executed; resolve from the actual subject before use.',
    'fixtures':['raw/scenario.json (teaching premises only)'],
    'positive_control':'Before activation, demonstrate an independently justified valid witness accepted by the real instrument.',
    'negative_control':'Before activation, demonstrate a meaningful invalid/no-op witness rejected by the real instrument.',
    'qualification_refs':[],'resource_limit':'No product execution allowed by this fixture. Bind actual limits from the mandate.',
    'side_effects':[],'authority_ref':a['mandate_ref'],'freshness_rule':'Fictional premises never become current operational evidence; collect and pin a real run.',
    'evidence_requirements':['Actual raw observations at the pinned subject','Qualified positive and negative controls']}
  write(base/f'measurement-bindings/MB-{iid}.json',binding)
  if r['app']=='NOT_APPLICABLE':continue
  state=r['state']
  result={'kind':'result','schema_version':'1.0.0','id':rid,'instance_id':iid,'criterion_id':r['cid'],
   'assignment_id':a['id'],'epoch_id':a['epoch_id'],'subject_digest':sd,'assignment_digest':ad,
   'execution':'COMPLETED' if state in ['PASS','FAIL','CONTESTED'] else 'BLOCKED',
   'verdict':state if state in ['PASS','FAIL','CONTESTED'] else 'UNKNOWN','evidence_state':r['fresh'],
   'review_status':'PROPOSED','observed_at':NOW,'expires_at':None,'evidence_ids':['EV-SCENARIO'],'qualification_ids':[],
   'evaluator_id':'SCENARIO-AUTHOR-NOT-A-PRODUCT-EVALUATOR','evaluator_digest':evaluator,
   'observation':{'summary':'AUTHORED SCENARIO PREMISE, NOT EXECUTED: '+r['note'],'assertions_executed':None,'modality':CS[r['cid']]['modality']},'supersedes':[]}
  write(base/f'results/{rid}.json',result);rids.append(rid)
  if state in ['FAIL','UNKNOWN','CONTESTED'] or r['app']=='UNRESOLVED' or r['fresh']!='CURRENT':
   fid='F-'+iid
   cl='MEASUREMENT_DEFECT' if 'grader' in slug else 'IMPLEMENTATION_GAP' if state=='FAIL' else 'VERIFICATION_GAP'
   if r['cid'].startswith('PEP-18-'):cl='RESEARCH_GAP'
   f={'kind':'finding','schema_version':'1.0.0','id':fid,'record_status':'EXAMPLE','created_at':NOW,'subject_ref':a['subject_id'],
      'instance_refs':[iid],'class':cl,'severity':'HIGH' if r['mandatory'] else 'MEDIUM',
      'claim':'In the fictional scenario: '+r['note'],'evidence_refs':['EV-SCENARIO'],'counterevidence_refs':[],
      'owner_ref':'ROLE:measurement-owner' if cl=='MEASUREMENT_DEFECT' else 'ROLE:subject-owner','next_action_kind':'REVISE_ASSIGNMENT' if cl=='MEASUREMENT_DEFECT' else 'RESEARCH' if cl=='RESEARCH_GAP' else 'IMPLEMENT' if state=='FAIL' else 'TEST',
      'status':'PROPOSED','wakeup_condition':r['action']}
   write(base/f'findings/{fid}.json',f);d['finding_ids'].append(fid)
 m={'kind':'assessment','schema_version':'1.0.0','id':'ASSESS-'+d['id'],'record_status':'EXAMPLE','assignment_id':a['id'],
    'assignment_digest':ad,'epoch_id':a['epoch_id'],'subject_digest':sd,'catalog_digest':a['catalog_digest'],
    'as_of':NOW,'result_ids':rids,'evidence_ids':['EV-SCENARIO'],'qualification_ids':[],
    'coverage_limitations':['All product states are fictional premises. No product observations, benchmark runs, UI captures, or beneficiary evidence collected.',
      'Illustrative pass/fail states are PROPOSED; no qualification records exist. Operational acceptance remains blocked.',
      'The selected rows are a teaching slice, not comprehensive coverage of the candidate catalog.'],
    'registration_state':'PENDING' if 'service' in slug else 'NOT_REQUESTED'}
 write(base/'assessment.json',m)
 dec={'kind':'decision','schema_version':'1.0.0','id':'DEC-NEXT','record_status':'EXAMPLE','created_at':NOW,'subject_ref':a['subject_id'],
      'authority_ref':a['mandate_ref'],'disposition':disposition,'status':'PROPOSED','evidence_refs':['EV-SCENARIO'],
      'alternatives':d['alternatives'],'rationale':d['next_action'],'resource_envelope_ref':'SCENARIO-ONLY-NO-REAL-BUDGET',
      'reversal_condition':d['stop_condition'],'execution_receipt_refs':[]}
 write(base/'decisions/DEC-NEXT.json',dec);write(base/'dossier.json',d)
 return base

# Executed pair: rerun the trusted included fixture, without touching user repositories.
tmp=ROOT/'.local-runs/fresh-toy';tmp.parent.mkdir(exist_ok=True)
summary=demo_loop.run(tmp)
for label,num in [('before','01'),('after','02')]:
 b=ROOT/'examples'/f'{num}-restoration-{label}';shutil.copytree(tmp/label,b)
 for n in ['findings','decisions']:(b/n).mkdir()
 a=pep.load_json(b/'assignment.json');rs=[pep.load_json(x) for x in sorted((b/'results').glob('*.json'))]
 write(b/'subject.json',{'source_digest':pep.file_digest(pep.ROOT/'tools/toy_product.py'),'variant':label})
 before=label=='before'
 d=context('RESTORE-'+label.upper(),'Restoration / '+('false success' if before else 'corrected behavior'),
   'Actual bundled fixture execution. Same two outcome checks; different implementation variants.',
   'Show that a successful-looking return message cannot substitute for restored data and corruption rejection.',
   'Two-record JSON restoration fixture in a temporary local directory; not a production backup system.',
   'The local fixture consumer reading the restored records, not an external user population.',
   'Not a product stage. Two-predicate fixture '+('fails' if before else 'passes')+'.',
   'Replace the no-op implementation and rerun the same qualified checks.' if before else 'Retain the verified fixture result; add independent failure modes before making any wider recovery claim.',
   'Stop any promotion that interprets these two toy passes as production backup safety.',[],
   [inventory('Restore operation','Claims restoration completed','Two required records '+('not restored' if before else 'restored with exact values'),'Data-integrity failure' if before else 'No gap in this two-record predicate'),
    inventory('Corruption handling','Backup digest should match records','Corrupt backup '+('accepted' if before else 'rejected with ValueError'),'Corruption silently tolerated' if before else 'Only this corruption fixture was exercised')],
   example_class='EXECUTED_FIXTURE',authorship='AGENT_DERIVED',intent_status='Accepted for local bundled demonstration only.',
   genesis='This fixture exists only to qualify the example grader. It is not a proposed new portfolio repository.',
   authority='Only bundled synthetic code and temporary local files were executed. No network, credentials or user repositories were used.',
   non_goals=['Validate a production storage system','Measure full product maturity','Claim an independent external auditor'],
   axes=[axis('PRODUCT_VERIFIED','FAIL' if before else 'PASS — scoped fixture only','Exact restore and corruption predicates executed.'),axis('PUBLISHED_VERIFIED','NOT_EVALUATED','No publication was performed.'),axis('VALUE_VALIDATED','NOT_EVALUATED','No beneficiary study was performed.')],
   value='Educational demonstration of outcome-based verification; no real-product or market value measurement.',
   notice='Executed synthetic fixture, not a real-repository audit. Raw observations were produced by the included Python demonstration during this response. The two-predicate grader accepted a valid witness and rejected a no-op.',
   previous='RESTORE-BEFORE' if not before else None,change='PRODUCT_VARIANT_CHANGE' if not before else 'EXECUTED_BASELINE',
   delta='The selected implementation variant changes; the two acceptance predicates stay the same. The report records real fixture outputs, not a simulated repair by an autonomous agent.',
   baseline='Retain both implementation-variant digests, raw outputs, and the E-TOY-1 predicate set.',
   failed=['Returning a success string establishes restoration.','A parseable but checksum-mismatched backup can be accepted.'],
   reproduce='Run python core-v1.0/tools/demo_loop.py --out .local-runs/new-toy and inspect raw/observations.json in both snapshots.')
 d['subject_identity']={'source_revision':None,'identity_method':'PEP value digest of the real bundled toy_product.py byte digest plus selected before/after variant in subject.json.',
   'limitation':'Actual Python fixture execution only; no Git commit exists for this materialized package and none was invented.'}
 d['maturity']['claim_limit']='This result supports only the two executed fixture predicates. It does not establish an MVP, a release, or production-safe restoration.'
 for x in d['inventory']:x['evidence_basis']='Actual raw/observations.json from this response.'
 d['row_notes']=[{'instance_id':r['instance_id'],'title':'Restore exact record contents' if r['instance_id']=='I-RESTORE' else 'Reject digest-mismatched backup',
                 'interpretation':r['observation']['summary'],
                 'next_action':'Retain the counterexample and repair the implementation.' if before else 'Reuse only within this unchanged fixture/implementation/evaluator scope.'} for r in rs]
 if before:
  for r in rs:
   f={'kind':'finding','schema_version':'1.0.0','id':'F-'+r['instance_id'],'record_status':'EXAMPLE','created_at':NOW,
      'subject_ref':a['subject_id'],'instance_refs':[r['instance_id']],'class':'IMPLEMENTATION_GAP','severity':'HIGH',
      'claim':r['observation']['summary'],'evidence_refs':['EV-OBS'],'counterevidence_refs':[],
      'owner_ref':'ROLE:toy-example-maintainer','next_action_kind':'IMPLEMENT','status':'ACCEPTED','wakeup_condition':None}
   write(b/f'findings/{f["id"]}.json',f);d['finding_ids'].append(f['id'])
 dec={'kind':'decision','schema_version':'1.0.0','id':'DEC-NEXT','record_status':'EXAMPLE','created_at':NOW,
      'subject_ref':a['subject_id'],'authority_ref':a['mandate_ref'],'disposition':'IMPROVE' if before else 'NO_ACTION','status':'PROPOSED',
      'evidence_refs':['EV-OBS','EV-QUAL'],'alternatives':d['alternatives'],'rationale':d['next_action'],
      'resource_envelope_ref':'LOCAL-BUNDLED-FIXTURE-ONLY','reversal_condition':d['stop_condition'],'execution_receipt_refs':[]}
 write(b/'decisions/DEC-NEXT.json',dec);write(b/'dossier.json',d)

# Agent-born library: a legitimate MVP slice can still lack external value evidence.
rr=[
 row('PEP-01-04-01','PASS','Authorship is agent-originated; acceptance is a separate experiment decision.'),
 row('PEP-01-04-02','PASS','Parent capability is shared manifest parsing for two CLI consumers.'),
 row('PEP-01-04-04','PASS','The library owns parse/validate/normalize, not portfolio state.'),
 row('PEP-01-04-07','PASS','A module in the existing CLI and an upstream parser were compared before extraction.'),
 row('PEP-01-04-08','UNKNOWN','No absorption trigger was recorded.','Set a review condition for one remaining consumer or lockstep releases.'),
 row('PEP-05-01-01','PASS','Consumer A parses a valid manifest into the specified fields.',mandatory=True,gate='LOCAL-CONSUMER-SLICE'),
 row('PEP-05-01-04','PASS','Malformed required fields fail with structured diagnostics.',mandatory=True,gate='LOCAL-CONSUMER-SLICE'),
 row('PEP-16-01-02','PASS','A clean consumer installs the packaged artifact without the source checkout.',mandatory=True,gate='LOCAL-CONSUMER-SLICE'),
 row('PEP-07-01-02','PASS','Setup has no undeclared machine-specific paths.'),
 row('PEP-08-01-02','PASS','Machine-readable successful results match a documented schema.'),
 row('PEP-04-02-09','UNKNOWN','The second consumer still uses the preceding package version.','Run the actual older consumer against the proposed package.'),
 row('PEP-12-01-04','UNKNOWN','The only stated throughput number comes from a warm cache.','Collect a cold-cache run separately.',fresh='STALE'),
 row('PEP-10-01-01','UNKNOWN','No interactive controls are included in this pure library slice; consumer UI remains owned downstream.',app='NOT_APPLICABLE'),
 row('PEP-18-01-08','UNKNOWN','External value is unmeasured even though the local technical slice is assumed to work.','Measure a real consumer outcome before expanding scope.')]
d=context('PARCELKIT','ParcelKit / agent-created library','An agent-originated component can be legitimate without a human-authored idea.',
 'Reduce duplicated manifest parsing and inconsistent diagnostics across two real consumers in the scenario.',
 'One local packaged library and Consumer A; Consumer B compatibility remains an open check.',
 'Internal CLI maintainers and consuming agents.','Illustrative: local consumer slice MVP; broader compatibility and external value remain unproven.',
 'Run the second consumer against the package and define an absorption trigger before expanding the repository.',
 'Pause separate-repository investment if only one consumer remains and all releases must change in lockstep.',rr,
 [inventory('Library API','parse / validate / normalize','Representative consumer path assumed passing','Broader input corpus unmeasured'),
  inventory('Package distribution','Install without source checkout','Clean installation assumed passing','Second consumer compatibility missing'),
  inventory('Benchmark','Low-overhead parsing','Warm-cache number only','No current cold-cache evidence'),
  inventory('Repository role','Shared parsing owner','Agent-derived boundary recorded','Absorption condition missing')],
 axes=[axis('PRODUCT_VERIFIED','ILLUSTRATIVE PASS — Consumer A','Scenario assumes a genuine packaged consumer path.'),axis('COMPATIBILITY','ILLUSTRATIVE UNKNOWN','Consumer B not exercised.'),axis('VALUE_VALIDATED','UNKNOWN','No external outcome evidence.')],
 genesis='The scenario agents decomposed two CLI implementations to share parsing. The intent originates from a parent capability, not a human naming a new repo.',
 alternatives=['Keep parsing in the existing CLI module','Adopt a suitable upstream parser','Keep a separate package but not a separate repository','Do not generalize beyond one consumer'])
build_scenario('03-agent-born-library',d,rr,'EXPERIMENT')

# Broad 18-domain web dossier: 36 distinct scoped questions, not one colossal universal form.
web_facts={
 1:[('PASS','The scenario names a bounded evaluation mandate.'),('PASS','Observation and mutation permissions are separated.')],
 2:[('UNKNOWN','The user-demand claim has no underlying interview or usage record.'),('PASS','The scenario distinguishes reference documentation from agent interpretation.')],
 3:[('PASS','Routes, buttons, and request boundaries are inventoried.'),('PASS','Public exports and internal UI helpers are separated.')],
 4:[('PASS','The service is the intended authoritative owner of task data.'),('FAIL','The dashboard treats its local mock array as authoritative application state.')],
 5:[('FAIL','Creating a task produces a toast but no persisted task after restart.'),('PASS','An empty list renders a deliberate empty state rather than crashing.')],
 6:[('FAIL','The stated test inventory covers mock handlers, not the accepted persistence obligation.'),('PASS','The intended frontend package is selected by the scenario test command.')],
 7:[('PASS','The scenario setup guide names its runtime and package manager.'),('PASS','No undocumented absolute workstation path is required.')],
 8:[('PASS','The API surface is documented for agent discovery.'),('FAIL','The create response uses an unversioned ad-hoc success string.')],
 9:[('PASS','The screen presents a clear task-board purpose.'),('PASS','Create task is visually distinct from optional settings.')],
 10:[('FAIL','The primary modal cannot be dismissed or completed by keyboard alone.'),('PASS','Focusable buttons have a visible focus treatment.')],
 11:[('PASS','Repeated cards share coherent spacing and interaction treatment in the premise.'),('PASS','Color roles separate emphasis, state, and decoration.')],
 12:[('UNKNOWN','Latency claims use an idle machine and one request, not the declared concurrent workload.'),('PASS','The scenario records the data size used by its mock benchmark.')],
 13:[('FAIL','Success telemetry records the button handler, not durable task creation.'),('UNKNOWN','Logs are not tied to a deployed artifact and environment.')],
 14:[('PASS','Task content and user identifiers are named sensitive assets.'),('UNKNOWN','The service boundary is sketched, but tenant authorization behavior is unexamined.')],
 15:[('FAIL','Task creation can omit the accepted owner identifier without rejection.'),('PASS','The scenario declares task IDs unique within the project scope.')],
 16:[('FAIL','The distribution contains a frontend but omits the promised persistence service.'),('UNKNOWN','No clean end-user installation of the complete product was performed.')],
 17:[('PASS','The scenario separates immutable record IDs from display names.'),('PASS','Structured records declare their schema versions.')],
 18:[('PASS','The plan explicitly distinguishes a concept from shipping behavior.'),('UNKNOWN','No feasibility experiment tested the essential persistence dependency.')]
}
rr=[]
for dom,pairs in web_facts.items():
 for k,(st,note) in enumerate(pairs,1):
  mandatory=(dom,k) in [(4,2),(5,1),(6,1),(8,2),(10,1),(14,2),(15,1),(16,1)]
  gate='CORE-USER-JOURNEY' if dom in [4,5,6,8,15,16] and mandatory else 'ACCESSIBILITY-BASELINE' if dom==10 and mandatory else 'AUTHORIZATION' if mandatory else None
  rr.append(row(f'PEP-{dom:02d}-01-{k:02d}',st,note,
                'Capture and independently verify the real scoped behavior before accepting this row.',mandatory,gate))
d=context('DRAFTBOARD','Draftboard / polished interface, broken outcome','A broad, 18-domain filled example: visual finish does not purchase a functioning core journey.',
 'Let a single project operator create and retrieve tasks reliably across a browser restart.',
 'Local browser interface, task API, and persistence boundary; one operator journey only.',
 'Single local project operator.','Illustrative: UI prototype, not an integrated product MVP.',
 'Wire and verify durable creation end to end before more visual refinement; repair the keyboard-blocking modal in parallel.',
 'Do not promote while task creation loses data or the required journey is inaccessible by keyboard.',rr,
 [inventory('Create-task control','Creates a durable task','Success toast changes a mock array','Core persistence missing'),
  inventory('Restart path','Tasks survive reload','Task disappears in scenario premise','Durability failure'),
  inventory('Visual design','Polished card layout','Consistent roles and hierarchy assumed','Does not prove behavior'),
  inventory('Keyboard path','Supported modal operation','Keyboard completion blocked','Accessibility gate fails'),
  inventory('Agent API','Stable JSON operations','Ad-hoc success response','Machine contract missing'),
  inventory('Deployment package','Complete local product','Frontend only','Missing runtime dependency'),
  inventory('Security boundary','Per-project ownership','Authorization untested','Unknown, not safe by default'),
  inventory('Value hypothesis','Less task-management friction','No beneficiary experiment','Research gap')],
 axes=[axis('DESIGN_READY','ILLUSTRATIVE PARTIAL','Visual design is assumed coherent; behavioral contract has gaps.'),axis('PIPELINE_VERIFIED','UNKNOWN','No actual CI evidence is provided.'),axis('PRODUCT_VERIFIED','ILLUSTRATIVE FAIL','Core persisted outcome is missing.'),axis('ACCESSIBILITY','ILLUSTRATIVE FAIL','Required keyboard journey blocked.'),axis('PUBLISHED_VERIFIED','NOT_EVALUATED','Package is incomplete even within scenario.'),axis('VALUE_VALIDATED','UNKNOWN','No actual user outcome evidence.')],
 reviews=[{'topic':'Visual polish versus product completeness','assessment':'The design may be coherent while the product is still a UI prototype.','support':'The premises describe consistent cards, semantic colors, and identifiable actions.','countercase':'Screenshots cannot show persistence, tenant authorization, error recovery, or keyboard completion.','discriminator':'Create a task through the real UI, kill/restart relevant processes, and retrieve it through an independent reader.','confidence_basis':'High confidence in the logical distinction; no confidence claim about any real application.'},
          {'topic':'Scope before expansion','assessment':'Do not add collaboration, analytics, or a second UI until the single-operator outcome is demonstrated.','support':'The central promise already requires data persistence and a working control path.','countercase':'A user might value an ephemeral board; that would require an explicit intent revision, not silently weakening persistence.','discriminator':'Compare persistent and intentionally ephemeral variants against the accepted beneficiary need.','confidence_basis':'Scenario-based recommendation; retain both hypotheses until evidence distinguishes them.'}])
build_scenario('04-polished-dashboard',d,rr)

# Service readiness vector, scoped credentials and applicability unknown.
rr=[row('PEP-05-01-01','PASS','Local request completes the documented operation.',mandatory=True,gate='LOCAL-SLICE'),
 row('PEP-05-01-04','PASS','Malformed records are rejected without storage corruption.',mandatory=True,gate='LOCAL-SLICE'),
 row('PEP-14-02-01','PASS','Local invalid tokens cannot create authenticated sessions.',mandatory=True,gate='LOCAL-SLICE'),
 row('PEP-03-03-06','PASS','Local records survive the supported restart boundary.',mandatory=True,gate='LOCAL-SLICE'),
 row('PEP-13-01-10','PASS','An injected local failure is visible in the declared diagnostic path.'),
 row('PEP-07-01-05','PASS','Missing deployment credentials produce a scoped diagnostic.'),
 row('PEP-16-03-03','UNKNOWN','No authority is available to inspect or change the hosted deployment.','Wait for explicitly scoped hosted verification access.',True,'HOSTED-RELEASE'),
 row('PEP-16-03-04','UNKNOWN','Routing to the actual hosted application is not verified.','Verify the requested host through the authorized route.',True,'HOSTED-RELEASE'),
 row('PEP-16-03-05','UNKNOWN','Required transport security is not measured on the hosted target.','Obtain authorized hosted transport evidence.',True,'HOSTED-RELEASE'),
 row('PEP-16-03-06','UNKNOWN','The hosted post-deployment journey has not run.','Run it only after the target and authority are resolved.',True,'HOSTED-RELEASE'),
 row('PEP-16-03-10','PASS','Independent local verification continues despite blocked deployment.'),
 row('PEP-08-02-10','PASS','The local native no-Docker path remains supported.'),
 row('PEP-12-01-10','PASS','Local performance is not promoted to a hosted guarantee.'),
 row('PEP-14-01-02','UNKNOWN','Multi-tenant exposure may apply, but the hosted slice and ownership boundary are unresolved.','Resolve hosted tenancy before releasing.',True,'HOSTED-RELEASE',app='UNRESOLVED')]
d=context('HARBORAPI','HarborAPI / local slice ready, hosted slice blocked','Unknown deployment evidence is not the same as a failed product test.',
 'Provide reliable authenticated local API behavior and later a separately verified hosted release.',
 'Local single-operator service plus a distinct proposed hosted deployment; never combine their readiness.',
 'Local operator now; hosted clients only after the hosted acceptance gate.',
 'Illustrative: local slice MVP; hosted release BLOCKED, not failed by inference.',
 'Continue authorized local work and queue hosted verification. Resolve target tenancy before any release claim.',
 'Do not deploy, claim hosted readiness, or infer public authorization from local success.',rr,
 [inventory('Local API','Authenticated persistent behavior','Local path assumed passing','Only local fixture scope'),
  inventory('Hosted artifact','Same intended release','Not observable with available authority','Publication evidence blocked'),
  inventory('Hosted routing / TLS','Reachable protected endpoint','Not measured','Unknown'),
  inventory('Registry receipt','Assessment recorded centrally','No delivery receipt','Pending projection, not lab-wide blocker')],
 axes=[axis('PRODUCT_VERIFIED','ILLUSTRATIVE PASS — LOCAL ONLY','Local required behavior assumed passing.'),axis('PUBLISHED_VERIFIED','BLOCKED_AUTHORITY','Hosted target not verified.'),axis('OPERATED_VERIFIED','UNKNOWN','No hosted operating window.'),axis('TENANCY_SCOPE','UNRESOLVED','Deployment capability may add mandatory authorization obligations.')],
 value='The scenario provides local functional premises but no actual observed operational benefit or hosted adoption evidence.')
build_scenario('05-service-blocked-deployment',d,rr)

# Polyrepo: component success cannot substitute for an integrated outcome.
rr=[row('PEP-04-06-01','PASS','The scenario BOM identifies producer, queue, worker, and consumer versions.',mandatory=True,gate='INTEGRATED-JOURNEY'),
 row('PEP-04-06-02','PASS','Each artifact has a source mapping.'),
 row('PEP-04-02-01','FAIL','Producer uses deadline_ms while consumer interprets deadline as seconds.','Resolve units in the canonical contract.',True,'INTEGRATED-JOURNEY'),
 row('PEP-04-02-02','FAIL','The producer emits the new schema while the installed consumer expects the old one.','Exercise the actual two versions together.',True,'INTEGRATED-JOURNEY'),
 row('PEP-04-02-05','FAIL','The consumer treats a rejected job as successful empty output.','Preserve a structured failure across the interface.',True,'INTEGRATED-JOURNEY'),
 row('PEP-04-06-04','FAIL','Independent suites miss the incompatible shared contract.','Add a mismatched-version negative control.'),
 row('PEP-04-06-05','PASS','The report keeps component passes separate from product acceptance.'),
 row('PEP-04-06-06','UNKNOWN','An undocumented second consumer was discovered during review.','Find its contract version and owner before changing the schema.'),
 row('PEP-04-06-07','FAIL','The integration job mocks transport and bypasses the real serializer.','Use the selected queue and serialization boundary.',True,'INTEGRATED-JOURNEY'),
 row('PEP-04-06-09','UNKNOWN','Only all-at-once upgrades were considered.','Test permitted producer/consumer rollout orders.'),
 row('PEP-04-06-10','PASS','One integration owner is assigned to the pinned failing composition.'),
 row('PEP-01-04-06','UNKNOWN','Separate repositories have not demonstrated a benefit over a versioned package set.','Compare coupling and release cadence before further decomposition.')]
d=context('RELAYSUITE','RelaySuite / green components, broken product','Cross-repository acceptance requires a consistent composition and a real consumer journey.',
 'Deliver a job from producer to consumer with correct deadlines and explicit failures.',
 'Pinned producer → queue → worker → consumer composition; four fictional components.',
 'Agents submitting jobs and consuming the final result.','Illustrative: component prototypes; integrated product gate FAIL.',
 'Repair the contract boundary under one integration owner, then re-run actual serialization and supported version-skew paths.',
 'Pause new component splitting until a passing integrated baseline and a coherent boundary justification exist.',rr,
 [inventory('Producer suite','Local contract tests pass','New schema emitted','Old consumer incompatible'),
  inventory('Worker suite','Local behavior tests pass','Mock queue path only','Real transport unexercised'),
  inventory('Integrated job','Deadline respected, result delivered','Unit mismatch and success-looking rejection','Core journey fails'),
  inventory('Consumer inventory','All consumers known','Second consumer discovered','Scope gap must be resolved')],
 axes=[axis('COMPONENT_READINESS','ILLUSTRATIVE PASS — local suites','Local evidence cannot establish the composition.'),axis('PRODUCT_VERIFIED','ILLUSTRATIVE FAIL','Serializer and schema drift break the final effect.'),axis('REPOSITORY_BOUNDARIES','UNRESOLVED','Release separation has not demonstrated a benefit.')],
 alternatives=['Repair the shared versioned contract','Ship a coordinated package set','Merge tightly coupled components into one repository','Narrow the promised rollout compatibility'])
build_scenario('06-polyrepo-integration',d,rr,'NARROW')

# Same fictional subject; assignment/evaluator change, not product improvement.
for after in [False,True]:
 label='after' if after else 'before'
 rr=[row('PEP-05-01-01','PASS','The scenario product produces the correct set of output records.',mandatory=True,gate='BEHAVIORAL-TARGET'),
  row('PEP-06-02-01','PASS' if after else 'FAIL',
      'A valid implementation using a different output filename is '+('accepted.' if after else 'rejected despite producing the right records.'),
      'Qualify filename-independent semantic equivalence against the accepted outcome.',True,'EVALUATOR-QUALIFICATION'),
  row('PEP-06-02-02','PASS','The grader still rejects empty/no-op output.',mandatory=True,gate='EVALUATOR-QUALIFICATION'),
  row('PEP-06-02-07','PASS','Expected records come from the accepted consumer contract rather than copying candidate output.'),
  row('PEP-06-02-09','PASS' if after else 'FAIL','The evaluator scope '+('excludes arbitrary filename requirements not in the consumer contract.' if after else 'silently adds a filename constraint absent from the consumer contract.')),
  row('PEP-06-02-10','PASS' if after else 'UNKNOWN','The corrected evaluator '+('has a new declared version with its own qualification procedure.' if after else 'has not yet been versioned and qualified.')),
  row('PEP-17-04-04','PASS' if after else 'UNKNOWN','Evaluator changes '+('are attributed to a new epoch.' if after else 'have not yet been applied.')),
  row('PEP-17-04-07','PASS','The previous report remains preserved; it is not rewritten as a product success.'),
  row('PEP-18-05-02','PASS','Repeated failure fingerprints identify the same incidental filename assertion.'),
  row('PEP-18-05-07','PASS','Restarting a context is distinguished from correcting the contract.'),
  row('PEP-18-05-10','PASS','A valid non-identical witness is the next discriminating experiment, not another identical patch.')]
 d=context('GRADER-'+label.upper(),'PathJudge / '+('corrected evaluator' if after else 'wrong rejection'),
   'The product is unchanged. A qualified assignment amendment can improve the judgment without improving the code.',
   'Distinguish behaviorally correct output from incidental filename choices that the consumer does not require.',
   'The same fictional output-producing component under two illustrative evaluator epochs.',
   'A consumer reading records via the public return path, not by a hard-coded grader filename.',
   'Illustrative: '+('behavioral gate passes; no product-change credit.' if after else 'product may be valid; evaluator qualification fails.'),
   'Preserve both epochs and classify the delta as evaluator correction, not implementation improvement.' if after else 'Use the valid alternate-filename witness to refute the incidental constraint before another implementation retry.',
   'Stop repeated implementation retries when a valid witness falsifies the grader assumption.',rr,
   [inventory('Product output','Returns required records','Correct contents assumed in both epochs','No product delta'),
    inventory('Filename rule','Not required by consumer','Grader '+('uses supported return path' if after else 'requires fixed name'),'Evaluator correction, not feature implementation'),
    inventory('Historical reports','Immutable old judgment','Old epoch retained','No retroactive replacement')],
   axes=[axis('PRODUCT_BEHAVIOR','ILLUSTRATIVE PASS — same premise','No product source changed.'),axis('ASSIGNMENT_QUALIFICATION','ILLUSTRATIVE PASS' if after else 'ILLUSTRATIVE FAIL','Valid non-identical witness distinguishes grader error.'),axis('ACTUAL_PRODUCT_EVIDENCE','NOT_EVALUATED','This is an authored scenario, not a live grader run.')],
   previous='GRADER-BEFORE' if after else None,change='EVALUATOR_CORRECTION' if after else 'ILLUSTRATIVE_BASELINE',
   delta='Subject descriptor digest is identical across the two dossiers. Assignment bytes, epoch, and proposed evaluator interpretation change; no actual product code was modified.',
   failed=['The only valid implementation must write output.json.','A fresh session alone repairs a logically wrong test.'],
   alternatives=['Keep the output filename requirement only if a real consumer depends on it','Correct the grader to validate the public behavior','Revise the public contract in a new epoch','Do not change the product'])
 build_scenario(('08' if after else '07')+'-grader-'+label,d,rr,'REVISE_EVALUATOR',subject_key='PATHJUDGE-SAME-SUBJECT')

# Retain generation source so every fictional premise is inspectable and reproducible.
shutil.copy2(Path(__file__),ROOT/'tools/example-authoring-source.py')
print('Dossiers:',len(dossier.case_dirs()))
for p in dossier.case_dirs():
 model=dossier.build_model(p)
 print(p.name,len(model['rows']),model['evidence_summary']['mandatory_gate_state'])
