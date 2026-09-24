#!/usr/bin/env python3
"""Execute the included synthetic restoration example; emit before/after bundles.

Uses only this package's toy code and a temporary directory. No user repositories,
network calls, credentials, deployments, or autonomous model sessions are involved.
"""
from __future__ import annotations
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path
import tempfile
import sys
sys.dont_write_bytecode=True
sys.path.insert(0,str(Path(__file__).resolve().parent))
import pep
from toy_product import restore_noop,restore_checked,records_digest

def now():return datetime.now(timezone.utc).isoformat()
def observe(fn):
    expected=[{'id':'alpha','value':7},{'id':'beta','value':'retained'}]
    with tempfile.TemporaryDirectory(prefix='pep-toy-') as td:
        root=Path(td);backup=root/'backup.json';target=root/'target.json'
        target.write_text(json.dumps({'records':[]}),encoding='utf-8')
        backup.write_text(json.dumps({'records':expected,'records_sha256':records_digest(expected)}),encoding='utf-8')
        narrative=fn(backup,target)
        actual=json.loads(target.read_text(encoding='utf-8'))
        integrity=actual=={'records':expected}
        # Corrupt content, preserving the original checksum. A real rejection must occur.
        backup.write_text(json.dumps({'records':[{'id':'alpha','value':'CORRUPTED'}],'records_sha256':records_digest(expected)}),encoding='utf-8')
        rejected=False
        try:fn(backup,target)
        except ValueError:rejected=True
        return {'fixture_kind':'SYNTHETIC_TOY_ONLY','narrative':narrative,
                'expected':{'records':expected},'observed':actual,
                'restored_integrity':integrity,'corrupt_backup_rejected':rejected,
                'assertions_executed':2}

def write_bundle(base:Path,label:str,observation:dict,qualified:dict):
    base.mkdir(parents=True,exist_ok=False)
    for folder in ['results','evidence','qualifications','raw','measurement-bindings']:(base/folder).mkdir()
    stamp=now()
    subject=pep.value_digest({'source_digest':pep.file_digest(pep.ROOT/'tools/toy_product.py'),'variant':label})
    evaluator=pep.file_digest(Path(__file__))
    catalog_digest=pep.file_digest(pep.ROOT/'catalog/catalog.json')
    insts=[('I-RESTORE','PEP-13-03-05','restored_integrity'),('I-CORRUPT','PEP-13-03-03','corrupt_backup_rejected')]
    a={'kind':'assignment','schema_version':'1.0.0','id':'A-'+label,'record_status':'EXAMPLE',
       'epoch_id':'E-TOY-1','status':'LOCKED','subject_id':'synthetic-restoration-'+label,'subject_digest':subject,
       'mandate_ref':'EXAMPLE-LOCAL-TOY-ONLY','intent_ref':'EXAMPLE-RESTORE-TWO-RECORDS','catalog_digest':catalog_digest,
       'profile_id':'bootstrap','coverage_statement':'Two synthetic restoration obligations only. Not a product MVP or a real agent-run assessment.',
       'created_at':stamp,'scope_review_status':'ACCEPTED','scope_review_ref':'EXAMPLE-FROZEN-TWO-OBLIGATIONS',
       'instances':[{'id':iid,'criterion_id':cid,'criterion_revision':'1.0.0','obligation_key':key,
                     'scope':'The bundled synthetic two-record JSON restoration fixture','applicability':'APPLICABLE',
                     'applicability_reason':'This toy variant claims to restore integrity-checked records.',
                     'applicability_decision_ref':'EXAMPLE-SCOPE','weight':1,'mandatory':True,
                     'measurement_binding_ref':f'measurement-bindings/MB-{iid}.json'} for iid,cid,key in insts],
       'gates':[{'id':'TOY-RESTORATION','required_instance_ids':[x[0] for x in insts]}]}
    pep.write_json_new(base/'assignment.json',a)
    adigest=pep.file_digest(base/'assignment.json')
    pep.write_json_new(base/'raw/observations.json',observation)
    pep.write_json_new(base/'raw/qualification.json',qualified)
    evid=[]
    for eid,path,role in [('EV-OBS','raw/observations.json','OBSERVATION'),('EV-QUAL','raw/qualification.json','QUALIFICATION')]:
        ev={'kind':'evidence','schema_version':'1.0.0','id':eid,'subject_digest':subject,'path':path,
            'digest':pep.file_digest(base/path),'observed_at':stamp,'sensitivity':'PUBLIC','role':role,
            'origin':'EXAMPLE_EXECUTION','summary':'Actual execution of bundled synthetic example; no real product evaluation.'}
        pep.write_json_new(base/'evidence'/f'{eid}.json',ev);evid.append(eid)
    q={'kind':'qualification','schema_version':'1.0.0','id':'Q-TOY','evaluator_id':'toy-outcome-grader',
       'evaluator_digest':evaluator,'status':'QUALIFIED','scope_instance_ids':[x[0] for x in insts],
       'positive_control_passed':qualified['valid_accepted'],'negative_control_passed':qualified['noop_rejected'],
       'evidence_ids':['EV-QUAL'],'observed_at':stamp,
       'limitations':['This qualification covers two synthetic fixture predicates only.','The reference reducer checks record consistency; it is not an external authentication service.']}
    pep.write_json_new(base/'qualifications/Q-TOY.json',q)
    resultids=[]
    for iid,cid,key in insts:
        bid='MB-'+iid
        binding={'kind':'measurement-binding','schema_version':'1.0.0','id':bid,'record_status':'EXAMPLE','created_at':stamp,
                 'criterion_id':cid,'instance_id':iid,'subject_scope':'Bundled toy JSON restoration with a two-record fixture.',
                 'modality':'DYNAMIC','method':'tools/demo_loop.py observe() executes the selected toy variant and checks the retained raw outcome.',
                 'expected_behavior':key+' must be true','units_or_anchors':'Boolean predicate; exactly one asserted outcome for this instance.',
                 'environment_ref':'Local temporary directory under this Python process','fixtures':['synthetic-alpha-beta-records'],
                 'positive_control':'restore_checked accepts intact backup and rejects corrupted backup.',
                 'negative_control':'restore_noop emits success text but fails both required outcome predicates.',
                 'qualification_refs':['Q-TOY'],'resource_limit':'Two tiny fixture executions; no network.',
                 'side_effects':['Temporary toy files only'],'authority_ref':'EXAMPLE-LOCAL-TOY-ONLY',
                 'freshness_rule':'Any change to toy implementation variant, evaluator or fixture requires rerun.',
                 'evidence_requirements':['raw/observations.json','raw/qualification.json']}
        pep.validate_record(binding);pep.write_json_new(base/'measurement-bindings'/f'{bid}.json',binding)
        rid='R-'+iid
        r={'kind':'result','schema_version':'1.0.0','id':rid,'instance_id':iid,'criterion_id':cid,
           'assignment_id':a['id'],'assignment_digest':adigest,'epoch_id':a['epoch_id'],'subject_digest':subject,
           'execution':'COMPLETED','verdict':'PASS' if observation[key] else 'FAIL','evidence_state':'CURRENT','review_status':'ACCEPTED',
           'observed_at':stamp,'expires_at':None,'evidence_ids':['EV-OBS'],'qualification_ids':['Q-TOY'],
           'evaluator_id':'toy-outcome-grader','evaluator_digest':evaluator,
           'observation':{'summary':f'{key} observed as {observation[key]} on the actual bundled toy variant.',
                          'assertions_executed':1,'modality':'DYNAMIC'},'supersedes':[]}
        pep.write_json_new(base/'results'/f'{rid}.json',r);resultids.append(rid)
    m={'kind':'assessment','schema_version':'1.0.0','id':'ASSESS-'+label,'record_status':'EXAMPLE',
       'assignment_id':a['id'],'assignment_digest':adigest,'epoch_id':a['epoch_id'],'subject_digest':subject,'catalog_digest':catalog_digest,
       'as_of':now(),'result_ids':resultids,'evidence_ids':evid,'qualification_ids':['Q-TOY'],
       'coverage_limitations':['Only two toy restoration predicates evaluated.','No autonomous worker, hosted integration, actual user data, or portfolio repository evaluated.'],
       'registration_state':'NOT_REQUESTED'}
    pep.write_json_new(base/'assessment.json',m)
    return pep.summarize_bundle(base)

def run(out:Path):
    pep.need(not out.exists(),'output path already exists; refusing overwrite')
    good=observe(restore_checked);bad=observe(restore_noop)
    qualified={'valid_accepted':good['restored_integrity'] and good['corrupt_backup_rejected'],
               'noop_rejected':not bad['restored_integrity'] and not bad['corrupt_backup_rejected'],
               'good_observations':good,'bad_observations':bad,
               'meaning':'Actual controlled example execution; not qualification of arbitrary product adapters.'}
    pep.need(qualified['valid_accepted'] and qualified['noop_rejected'],'toy grader controls failed')
    out.mkdir(parents=True)
    before=write_bundle(out/'before','before',bad,qualified)
    after=write_bundle(out/'after','after',good,qualified)
    summary={'record_status':'EXAMPLE','before_gate':before['mandatory_gate_state'],
             'after_gate':after['mandatory_gate_state'],'false_success_rejected':qualified['noop_rejected'],
             'limitations':'This is a deterministic toy demonstration, not an autonomous lab or repository deployment.'}
    pep.write_json_new(out/'demo-summary.json',summary)
    return summary

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
    try:print(json.dumps(run(a.out),indent=2));return 0
    except (pep.ValidationError,OSError) as exc:print(str(exc),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
