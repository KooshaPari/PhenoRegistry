"""Synthetic receipt fixtures. Never represents a native product execution."""
from copy import deepcopy
from pathlib import Path
import hashlib,json

def enc(x):return (json.dumps(x,indent=2,allow_nan=False)+'\n').encode()
def put(root,name,data):
 p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 return {'path':name,'sha256':hashlib.sha256(data).hexdigest()}
def make_case(root):
 h='a'*64
 cats=[{'id':'behavior','weight':70,'title':'Behavior'},{'id':'design','weight':30,'title':'Design'}]
 c0={'id':'CORE','category_id':'behavior','weight':1,'max_units':100,'passing_fraction':1,'mandatory':True,'critical':True,'oracle_sha256':h,'required_modalities':['test-report'],'required_actions':['user-input'],'max_age_hours':24,'allow_probabilistic':False,'rationale':'Synthetic declared mandatory behavior.'}
 c1={**c0,'id':'DESIGN','category_id':'design','mandatory':False,'critical':False,'required_actions':['read-only'],'rationale':'Synthetic design obligation.'}
 rb={'schema_version':'1.4','id':'SYN-RUBRIC','scope_id':'SYN-SCOPE','subject_id':'SYN-SUBJECT','revision':'1','profile_id':'SYN-PROFILE','source_revision':'SYN-SHA-1','artifact_sha256':'b'*64,'approval_reference':'SYN-NOT-AN-APPROVAL','synthetic':True,'categories':cats,'criteria':[c0,c1]}
 reports=[]
 for c in rb['criteria']:
  art=put(root,'artifacts/'+c['id']+'.json',enc({'synthetic':True,'note':'Test payload only; not a native application or bridge report.'}))
  r={'schema_version':'1.4','id':'SYN-RECEIPT-'+c['id'],'criterion_id':c['id'],'scope_id':rb['scope_id'],'subject_id':rb['subject_id'],'profile_id':rb['profile_id'],'source_revision':rb['source_revision'],'artifact_sha256':rb['artifact_sha256'],'oracle_sha256':h,'synthetic':True,'run_id':'SYN-RUN-'+c['id'],'observed_at':'2026-09-16T10:00:00Z','status':'assessed','earned_units':100,'total_units':100,'actions':c['required_actions'].copy(),'evaluator_kind':'deterministic','artifacts':[{**art,'modality':'test-report','media_type':'application/json'}]}
  reports.append(r)
 return rb,reports

def save_case(root,rb,reports):
 raw=enc(rb);put(root,'rubric.json',raw)
 idx={'schema_version':'1.4','rubric_sha256':hashlib.sha256(raw).hexdigest(),'as_of':'2026-09-16T12:00:00Z','receipts':[put(root,f'receipts/{i}.json',enc(r)) for i,r in enumerate(reports)]}
 put(root,'index.json',enc(idx));return raw,idx

# Expected state is admission/gate outcome, not product certification.
CASES={
 'good':'NO_RECORDED_MANDATORY_BLOCKER','critical-fail':'BLOCKED','missing':'UNASSESSED',
 'wrong-source':'UNASSESSED','wrong-artifact':'UNASSESSED','wrong-profile':'UNASSESSED',
 'wrong-scope':'UNASSESSED','wrong-subject':'UNASSESSED','wrong-oracle':'UNASSESSED',
 'future':'UNASSESSED','stale':'UNASSESSED','not-run':'UNASSESSED','error':'UNASSESSED',
 'blocked':'UNASSESSED','too-many-units':'UNASSESSED','wrong-denominator':'UNASSESSED',
 'no-user-action':'UNASSESSED','fixture-only':'UNASSESSED','missing-pixels':'UNASSESSED',
 'probabilistic-critical':'UNASSESSED','missing-payload':'UNASSESSED','tampered-payload':'UNASSESSED',
 'empty-payload':'UNASSESSED','escaped-payload':'UNASSESSED','duplicate-payload':'UNASSESSED',
 'synthetic-mismatch':'UNASSESSED','age-boundary':'NO_RECORDED_MANDATORY_BLOCKER',
 'all-unknown':'UNASSESSED','optional-unknown':'NO_RECORDED_MANDATORY_BLOCKER',
 'optional-probabilistic':'NO_RECORDED_MANDATORY_BLOCKER',
 'duplicate-criterion':'INPUT_ERROR','duplicate-receipt':'INPUT_ERROR','unknown-criterion':'INPUT_ERROR',
 'category-weight':'INPUT_ERROR','empty-category':'INPUT_ERROR','critical-not-mandatory':'INPUT_ERROR',
 'critical-probabilistic-policy':'INPUT_ERROR','critical-not-full':'INPUT_ERROR',
 'empty-rubric':'INPUT_ERROR','bad-field':'INPUT_ERROR','boolean-weight':'INPUT_ERROR',
 'bad-date':'INPUT_ERROR','bad-hash':'INPUT_ERROR','zero-denominator':'INPUT_ERROR'
}
def mutate(name,root,rb,rs):
 r=rs[0];c=rb['criteria'][0]
 if name=='good':pass
 elif name=='critical-fail':r['earned_units']=0
 elif name=='missing':rs.pop(0)
 elif name in ['wrong-source','wrong-artifact','wrong-profile','wrong-scope','wrong-subject','wrong-oracle']:
  key={'wrong-source':'source_revision','wrong-artifact':'artifact_sha256','wrong-profile':'profile_id','wrong-scope':'scope_id','wrong-subject':'subject_id','wrong-oracle':'oracle_sha256'}[name]
  r[key]='c'*64 if 'sha256' in key else 'SYN-WRONG'
 elif name=='future':r['observed_at']='2026-09-17T10:00:00Z'
 elif name=='stale':r['observed_at']='2026-09-14T10:00:00Z'
 elif name in ['not-run','error','blocked']:r['status']=name
 elif name=='too-many-units':r['earned_units']=101
 elif name=='wrong-denominator':r['total_units']=101
 elif name=='no-user-action':r['actions']=[]
 elif name=='fixture-only':r['actions']=['fixture-control']
 elif name=='missing-pixels':c['required_modalities']=['pixels']
 elif name=='probabilistic-critical':r['evaluator_kind']='model-assisted'
 elif name=='missing-payload':(root/r['artifacts'][0]['path']).unlink()
 elif name=='tampered-payload':(root/r['artifacts'][0]['path']).write_text('tampered')
 elif name=='empty-payload':(root/r['artifacts'][0]['path']).write_bytes(b'')
 elif name=='escaped-payload':r['artifacts'][0]['path']='../out.json'
 elif name=='duplicate-payload':r['artifacts'].append(deepcopy(r['artifacts'][0]))
 elif name=='synthetic-mismatch':r['synthetic']=False
 elif name=='age-boundary':r['observed_at']='2026-09-15T12:00:00Z'
 elif name=='all-unknown':rs.clear()
 elif name=='optional-unknown':rs.pop(1)
 elif name=='optional-probabilistic':rb['criteria'][1]['allow_probabilistic']=True;rs[1]['evaluator_kind']='model-assisted'
 elif name=='duplicate-criterion':rb['criteria'].append(deepcopy(c))
 elif name=='duplicate-receipt':rs.append(deepcopy(r))
 elif name=='unknown-criterion':r['criterion_id']='MISSING'
 elif name=='category-weight':rb['categories'][0]['weight']=69
 elif name=='empty-category':rb['categories'][0]['weight']=69;rb['categories'].append({'id':'unused','weight':1,'title':'Unused'})
 elif name=='critical-not-mandatory':c['mandatory']=False
 elif name=='critical-probabilistic-policy':c['allow_probabilistic']=True
 elif name=='critical-not-full':c['passing_fraction']=0.85
 elif name=='empty-rubric':rb['criteria']=[]
 elif name=='bad-field':r['approved']=True
 elif name=='boolean-weight':rb['categories'][0]['weight']=True
 elif name=='bad-date':r['observed_at']='2026-09-16T10:00:00'
 elif name=='bad-hash':r['artifact_sha256']='bad'
 elif name=='zero-denominator':r['total_units']=0
 else:raise KeyError(name)
