#!/usr/bin/env python3
"""Offline reference kernel for PEP 1.0.

Validates the shipped JSON Schema subset, record consistency and file digests;
reduces results under a frozen assignment. Does NOT authenticate observations,
execute product commands, enforce OS permissions, approve releases, or call APIs.
Python 3.10+; standard library only. See docs/12-REFERENCE-KERNEL.md.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import subprocess
import sys
from datetime import datetime, timezone
from typing import Any

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
VERSION = '1.0.0'
MAX_JSON_BYTES = 32 * 1024 * 1024

class ValidationError(ValueError):
    """An input is invalid, inconsistent, or unsafe to resolve."""

def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)

def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for k, v in pairs:
        need(k not in result, f'duplicate JSON key: {k}')
        result[k] = v
    return result

def _reject_constant(value: str) -> None:
    raise ValidationError(f'non-finite JSON constant: {value}')

def load_json(path: Path) -> Any:
    need(path.is_file(), f'missing file: {path}')
    need(path.stat().st_size <= MAX_JSON_BYTES, f'JSON exceeds {MAX_JSON_BYTES} bytes: {path}')
    try:
        return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_pairs,
                          parse_constant=_reject_constant)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ValidationError(f'invalid JSON {path}: {exc}') from exc

def canonical_bytes(value: Any) -> bytes:
    """PEP Python JSON digest profile, NOT RFC 8785/JCS or a signature."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
                      allow_nan=False).encode('utf-8')

def value_digest(value: Any) -> str:
    return 'sha256:' + hashlib.sha256(canonical_bytes(value)).hexdigest()

def file_digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return 'sha256:' + h.hexdigest()

def write_json_new(path: Path, value: Any) -> None:
    """Exclusive creation: no overwrite. Callers create parent directories deliberately."""
    with path.open('x', encoding='utf-8', newline='\n') as stream:
        json.dump(value, stream, ensure_ascii=False, indent=2, allow_nan=False)
        stream.write('\n')

def parse_time(value: str) -> datetime:
    need(isinstance(value, str), 'timestamp must be a string')
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValidationError(f'invalid timestamp: {value}') from exc
    need(parsed.tzinfo is not None and parsed.utcoffset() is not None,
         f'timestamp lacks timezone: {value}')
    return parsed

def safe_file(base: Path, relative: str) -> Path:
    """Resolve an existing, non-symlink, relative regular file under base.

    Intended for a quiescent trusted checkout. Not a race-proof filesystem sandbox.
    """
    need(isinstance(relative, str) and bool(relative), 'empty evidence path')
    need('\\' not in relative, f'nonportable path: {relative}')
    rel = Path(relative)
    need(not rel.is_absolute() and not re.match(r'^[A-Za-z]:', relative),
         f'absolute path forbidden: {relative}')
    need('..' not in rel.parts and '.' not in rel.parts, f'path traversal: {relative}')
    base = base.resolve()
    current = base
    for part in rel.parts:
        current = current / part
        need(not current.is_symlink(), f'symlink forbidden: {relative}')
    need(current.resolve().is_relative_to(base), f'path escapes bundle: {relative}')
    need(current.is_file(), f'missing regular file: {relative}')
    return current

ALLOWED_KEYWORDS = {
    '$schema', '$id', 'title', 'description', '$ref', 'type', 'const', 'enum',
    'required', 'properties', 'additionalProperties', 'items', 'minItems',
    'maxItems', 'minLength', 'pattern', 'minimum', 'exclusiveMinimum',
    'format', 'uniqueItems', 'maximum'
}

def validate_shape(value: Any, schema: dict[str, Any], where: str = '$', depth: int = 0) -> None:
    """Validate only the subset used by this release; unknown keywords fail closed."""
    need(depth < 80, f'{where}: schema nesting limit')
    need(isinstance(schema, dict), f'{where}: schema must be object')
    need(not (set(schema) - ALLOWED_KEYWORDS),
         f'{where}: unsupported schema keywords {sorted(set(schema)-ALLOWED_KEYWORDS)}')
    if '$ref' in schema:
        ref = schema['$ref']
        need(isinstance(ref, str) and re.fullmatch(r'[a-z-]+\.schema\.json', ref) is not None,
             f'{where}: only packaged schema references are allowed')
        validate_shape(value, load_json(safe_file(ROOT/'schemas', ref)), where, depth+1)
        return
    if 'const' in schema:
        need(value == schema['const'] and type(value) is type(schema['const']), f'{where}: wrong constant')
    if 'enum' in schema:
        need(any(value == e and type(value) is type(e) for e in schema['enum']), f'{where}: invalid enum value {value!r}')
    if 'type' in schema:
        types = schema['type'] if isinstance(schema['type'], list) else [schema['type']]
        def matches(t: str) -> bool:
            return {'null': value is None, 'string': isinstance(value,str),
                    'object': isinstance(value,dict), 'array': isinstance(value,list),
                    'boolean': type(value) is bool, 'integer': type(value) is int,
                    'number': type(value) in (int,float) and math.isfinite(value)}.get(t, False)
        need(any(matches(t) for t in types), f'{where}: expected {types}, got {type(value).__name__}')
    if isinstance(value,str):
        need(len(value) >= schema.get('minLength',0), f'{where}: empty/short string')
        if 'pattern' in schema:
            need(re.search(schema['pattern'],value) is not None, f'{where}: invalid string pattern')
        if schema.get('format') == 'date-time':
            parse_time(value)
    if type(value) in (int,float):
        need(math.isfinite(value), f'{where}: non-finite number')
        if 'minimum'in schema: need(value >= schema['minimum'], f'{where}: below minimum')
        if 'maximum'in schema: need(value <= schema['maximum'], f'{where}: above maximum')
        if 'exclusiveMinimum'in schema: need(value > schema['exclusiveMinimum'], f'{where}: non-positive weight')
    if isinstance(value,list):
        need(len(value) >= schema.get('minItems',0), f'{where}: insufficient items')
        if 'maxItems'in schema: need(len(value) <= schema['maxItems'], f'{where}: too many items')
        if schema.get('uniqueItems'):
            need(len({canonical_bytes(v) for v in value})==len(value), f'{where}: duplicate array items')
        for i,v in enumerate(value):
            if 'items'in schema: validate_shape(v,schema['items'],f'{where}[{i}]',depth+1)
    if isinstance(value,dict):
        need(set(schema.get('required',[])) <= set(value), f'{where}: missing required fields {sorted(set(schema.get("required",[]))-set(value))}')
        props=schema.get('properties',{})
        if schema.get('additionalProperties') is False:
            need(set(value) <= set(props), f'{where}: unexpected fields {sorted(set(value)-set(props))}')
        for k,v in value.items():
            if k in props: validate_shape(v,props[k],f'{where}.{k}',depth+1)

def has_placeholder(value: Any) -> bool:
    if isinstance(value,str):
        return 'REPLACE_WITH_' in value or value=='sha256:'+'0'*64
    if isinstance(value,dict):return any(has_placeholder(v) for v in value.values())
    if isinstance(value,list):return any(has_placeholder(v) for v in value)
    return False

def validate_record(value: Any) -> None:
    need(isinstance(value,dict), 'record must be an object')
    kind=value.get('kind')
    need(isinstance(kind,str) and re.fullmatch(r'[a-z-]+',kind) is not None,'invalid record kind')
    schema=load_json(safe_file(ROOT/'schemas',kind+'.schema.json'))
    validate_shape(value,schema)
    if value.get('record_status')=='OPERATIONAL':
        need(not has_placeholder(value),'operational record contains template placeholders')
    if kind=='outbox':
        need((value['state']=='DELIVERED') == bool(value['receipt_ref']),
             'outbox receipt/state inconsistency')
    if kind=='result':
        need(not(value['execution']!='COMPLETED' and value['verdict'] in ('PASS','FAIL')),
             'unfinished/error execution cannot carry a PASS/FAIL product verdict')
        if value['expires_at'] is not None:
            need(parse_time(value['expires_at'])>=parse_time(value['observed_at']),
                 'result expiry precedes observation')
    if kind=='assignment':
        unique(value['instances'],'id');unique(value['instances'],'obligation_key')
        unique(value['gates'],'id')
        inst={x['id']:x for x in value['instances']}
        for i in inst.values():
            if i['applicability']=='NOT_APPLICABLE':
                need(bool(i['applicability_decision_ref']),'non-applicability requires decision reference')
        for g in value['gates']:
            need(len(set(g['required_instance_ids']))==len(g['required_instance_ids']), 'duplicate gate member')
            for ident in g['required_instance_ids']:
                need(ident in inst,f'unknown gate member {ident}')
                need(inst[ident]['mandatory'], f'gate member {ident} must be explicitly mandatory')
                need(inst[ident]['applicability']!='NOT_APPLICABLE', 'gate cannot require a non-applicable instance')
        if value['status']=='LOCKED':
            need(value['scope_review_status']=='ACCEPTED' and bool(value['scope_review_ref']),
                 'locked assignment lacks accepted scope review')

def unique(items: list[dict[str,Any]], key: str) -> None:
    ids=[i[key] for i in items]
    need(len(ids)==len(set(ids)), f'duplicate {key}')

def validate_catalog(value: dict[str,Any]) -> dict[str,Any]:
    validate_record(value)
    for key in ['domains','pillars','criteria']: unique(value[key],'id')
    domain_ids={d['id'] for d in value['domains']}
    ps={p['id']:p for p in value['pillars']}
    for p in ps.values():need(p['domain_id'] in domain_ids,'unknown pillar domain')
    for c in value['criteria']:
        need(c['pillar_id'] in ps,'unknown criterion pillar')
        need(c['domain_id']==ps[c['pillar_id']]['domain_id'],'criterion domain mismatch')
        need(c['implementation_status']=='PROCEDURE_ONLY','catalog adapter claim exceeds this release')
        need(c['qualification_status']=='UNQUALIFIED','catalog must not fabricate qualification')
    return {'domains':len(domain_ids),'pillars':len(ps),'candidate_entries':len(value['criteria']),
            'exact_duplicate_predicates':len(value['criteria'])-len({c['predicate'].casefold() for c in value['criteria']}),
            'semantic_uniqueness':'requires adjudication at assignment binding'}

def index_records(base: Path, ids: list[str], folder: str, kind: str) -> dict[str,dict[str,Any]]:
    need(len(ids)==len(set(ids)),f'duplicate {kind} ID in manifest')
    result={}
    declared_files={i+'.json' for i in ids}
    actual_files={p.name for p in (base/folder).glob('*.json')}
    need(actual_files==declared_files,f'{kind} manifest/file set mismatch')
    for ident in ids:
        need(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]{0,180}',ident) is not None,'unsafe record ID')
        record=load_json(safe_file(base,f'{folder}/{ident}.json'))
        validate_record(record)
        need(record['id']==ident and record['kind']==kind,f'{kind} identity mismatch')
        result[ident]=record
    return result

def read_bundle(base: Path) -> dict[str,Any]:
    base=base.resolve()
    a=load_json(safe_file(base,'assignment.json'));validate_record(a)
    m=load_json(safe_file(base,'assessment.json'));validate_record(m)
    need(a['kind']=='assignment' and m['kind']=='assessment','wrong bundle roots')
    need(m['assignment_id']==a['id'] and m['epoch_id']==a['epoch_id'],'assessment assignment mismatch')
    need(m['subject_digest']==a['subject_digest'],'assessment subject mismatch')
    need(m['assignment_digest']==file_digest(base/'assignment.json'),'assignment digest mismatch')
    need(m['catalog_digest']==a['catalog_digest']==file_digest(ROOT/'catalog/catalog.json'),'catalog digest mismatch')
    need(m['record_status']==a['record_status'],'record context mismatch')
    as_of=parse_time(m['as_of'])
    need(parse_time(a['created_at'])<=as_of,'assignment occurs after assessment')
    results=index_records(base,m['result_ids'],'results','result')
    evidence=index_records(base,m['evidence_ids'],'evidence','evidence')
    quals=index_records(base,m['qualification_ids'],'qualifications','qualification')
    catalog=load_json(ROOT/'catalog/catalog.json'); cats={c['id']:c for c in catalog['criteria']}
    inst={i['id']:i for i in a['instances']}
    bindings={}
    for i in inst.values():
        need(i['criterion_id'] in cats,'assignment criterion not in catalog')
        need(i['criterion_revision']==cats[i['criterion_id']]['revision'],'criterion revision mismatch')
        if i['measurement_binding_ref'] is not None:
            binding=load_json(safe_file(base,i['measurement_binding_ref']))
            validate_record(binding)
            need(binding['kind']=='measurement-binding','wrong measurement binding kind')
            need(binding['instance_id']==i['id'] and binding['criterion_id']==i['criterion_id'],'measurement binding mismatch')
            bindings[i['id']]=binding
    for ev in evidence.values():
        need(ev['subject_digest']==a['subject_digest'],'evidence subject mismatch')
        need(parse_time(ev['observed_at'])<=as_of,'evidence from future relative to assessment')
        path=safe_file(base,ev['path'])
        need(file_digest(path)==ev['digest'],f'evidence digest mismatch: {ev["id"]}')
    for q in quals.values():
        need(parse_time(q['observed_at'])<=as_of,'qualification from future')
        for iid in q['scope_instance_ids']:need(iid in inst,'qualification has unknown instance')
        for eid in q['evidence_ids']:
            need(eid in evidence,'qualification references missing evidence')
            need(evidence[eid]['role']=='QUALIFICATION','qualification needs qualification-role evidence')
    for r in results.values():
        need(r['instance_id'] in inst,'unknown result instance')
        need(r['criterion_id']==inst[r['instance_id']]['criterion_id'],'result criterion mismatch')
        need(r['assignment_id']==a['id'] and r['epoch_id']==a['epoch_id'],'result epoch mismatch')
        need(r['subject_digest']==a['subject_digest'],'result subject mismatch')
        need(r['assignment_digest']==m['assignment_digest'],'result assignment digest mismatch')
        need(parse_time(r['observed_at'])<=as_of,'result observed after assessment')
        for eid in r['evidence_ids']:
            need(eid in evidence,'missing evidence reference')
            need(evidence[eid]['role']=='OBSERVATION','result needs observation-role evidence')
        for qid in r['qualification_ids']:
            need(qid in quals,'missing qualification reference')
            q=quals[qid]
            need(q['evaluator_id']==r['evaluator_id'] and q['evaluator_digest']==r['evaluator_digest'],
                 'qualification evaluator mismatch')
            need(r['instance_id'] in q['scope_instance_ids'],'qualification scope mismatch')
        need(len(r['supersedes'])==len(set(r['supersedes'])),'duplicate supersession edge')
        for old in r['supersedes']:
            need(old in results and old!=r['id'],'invalid supersession reference')
            need(results[old]['instance_id']==r['instance_id'],'cross-instance supersession')
            need(parse_time(results[old]['observed_at'])<=parse_time(r['observed_at']), 'supersession reverses observation order')
    # Detect cycles even with equal timestamps; do not resolve forks by wall-clock luck.
    visiting:set[str]=set();done:set[str]=set()
    def visit(ident: str) -> None:
        need(ident not in visiting,'supersession cycle')
        if ident in done:return
        visiting.add(ident)
        for old in results[ident]['supersedes']:visit(old)
        visiting.remove(ident);done.add(ident)
    for ident in results:visit(ident)
    return {'base':base,'assignment':a,'assessment':m,'results':results,'evidence':evidence,'qualifications':quals,'bindings':bindings}

def effective_status(r: dict[str,Any] | None,b:dict[str,Any]) -> tuple[str,str]:
    if r is None:return 'UNKNOWN','no effective result'
    m=b['assessment'];qs=b['qualifications']
    binding=b['bindings'].get(r['instance_id'])
    if binding is None or binding['record_status']=='TEMPLATE':return 'UNKNOWN','missing activated measurement binding'
    if r['execution']!='COMPLETED':return 'UNKNOWN','execution not completed'
    if r['review_status']!='ACCEPTED':return 'UNKNOWN','review is not accepted (waivers are not passes)'
    if r['evidence_state']!='CURRENT':return 'UNKNOWN','evidence not current'
    if r['expires_at'] is not None and parse_time(r['expires_at'])<=parse_time(m['as_of']):
        return 'UNKNOWN','evidence expired'
    if r['verdict'] not in ('PASS','FAIL'):return 'UNKNOWN',r['verdict'].lower()
    if not r['evidence_ids']:return 'UNKNOWN','no raw observation evidence'
    if not r['qualification_ids']:return 'UNKNOWN','no instrument qualification'
    if not any(qs[q]['status']=='QUALIFIED' and qs[q]['positive_control_passed'] and
               qs[q]['negative_control_passed'] for q in r['qualification_ids']):
        return 'UNKNOWN','instrument controls not qualified'
    obs=r['observation']
    if obs['modality']=='DYNAMIC' and (obs['assertions_executed'] is None or obs['assertions_executed']<=0):
        return 'UNKNOWN','no dynamic assertions executed'
    return r['verdict'],'accepted input records with locally matching evidence digests'

def summarize_bundle(base: Path) -> dict[str,Any]:
    b=read_bundle(base);a=b['assignment'];m=b['assessment'];rs=b['results']
    superseded={old for r in rs.values() for old in r['supersedes']}
    totals={'pass_weight':0.0,'fail_weight':0.0,'unknown_weight':0.0,'unresolved_applicability_weight':0.0,'not_applicable_weight':0.0}
    states={};rows=[]
    for i in a['instances']:
        active=[r for rid,r in rs.items() if r['instance_id']==i['id'] and rid not in superseded]
        if i['applicability']=='NOT_APPLICABLE':
            state,reason='NOT_APPLICABLE',i['applicability_reason'];totals['not_applicable_weight']+=i['weight']
        elif i['applicability']=='UNRESOLVED':
            state,reason='UNRESOLVED','applicability not accepted';totals['unresolved_applicability_weight']+=i['weight']
        else:
            state,reason=('UNKNOWN','multiple competing effective results') if len(active)>1 else effective_status(active[0] if active else None,b)
            totals[{'PASS':'pass_weight','FAIL':'fail_weight','UNKNOWN':'unknown_weight'}[state]]+=i['weight']
        states[i['id']]=state
        rows.append({'instance_id':i['id'],'criterion_id':i['criterion_id'],'state':state,'reason':reason,'weight':i['weight'],'mandatory':i['mandatory']})
    need(all(math.isfinite(v) for v in totals.values()), 'weight accumulation overflow')
    p=totals['pass_weight'];f=totals['fail_weight'];u=totals['unknown_weight'];den=p+f+u
    ratio=lambda x,y: x/y if y else None
    gates=[]
    assignment_ready=a['status']=='LOCKED' and a['scope_review_status']=='ACCEPTED'
    for g in a['gates']:
        ss=[states[x] for x in g['required_instance_ids']]
        verdict=('BLOCKED' if not assignment_ready else 'FAIL' if 'FAIL'in ss else 'PASS' if all(s=='PASS' for s in ss) else 'BLOCKED')
        gates.append({'id':g['id'],'status':verdict,'required_instance_ids':g['required_instance_ids']})
    mandatory=[r for r in rows if r['mandatory'] and r['state']!='NOT_APPLICABLE']
    release=('NOT_EVALUATED' if not a['gates'] or not mandatory else 'BLOCKED' if not assignment_ready else
             'FAIL' if any(r['state']=='FAIL' for r in mandatory) else
             'PASS' if all(r['state']=='PASS' for r in mandatory) and all(g['status']=='PASS' for g in gates) and totals['unresolved_applicability_weight']==0 else 'BLOCKED')
    return {'kernel_version':VERSION,'assessment_id':m['id'],'epoch_id':a['epoch_id'],
            'subject_digest':a['subject_digest'],'as_of':m['as_of'],'record_status':m['record_status'],
            'interpretation':'Consistency-based reduction of accepted input records, NOT independent authentication, product verification, or publication authorization.',
            'coverage_statement':a['coverage_statement'],'coverage_limitations':m['coverage_limitations'],
            'weights':totals,'assessed_pass_rate':ratio(p,p+f),'assessment_coverage':ratio(p+f,den),
            'verified_satisfaction_within_settled_applicability':ratio(p,den),
            'optimistic_bound_within_settled_applicability':ratio(p+u,den),
            'applicability_complete':totals['unresolved_applicability_weight']==0,
            'scope_locked':assignment_ready,'mandatory_gate_state':release,
            'registration_state':m['registration_state'],'gates':gates,'instances':rows}

def inspect_metadata(root:Path,max_files:int=5000) -> dict[str,Any]:
    """Metadata-only, nonexecuting inventory; never a complete content snapshot."""
    need(root.is_dir(),'inspection root is not a directory')
    need(max_files>0,'max-files must be positive')
    root=root.resolve();rows=[];excluded=[];truncated=False
    skips={'.git','node_modules','.venv','venv','target','dist','build','__pycache__'}
    for cur,dirs,files in os.walk(root,followlinks=False):
        dirs.sort();files.sort();kept=[]
        for name in dirs:
            p=Path(cur)/name
            if name in skips or p.is_symlink():excluded.append(p.relative_to(root).as_posix()+'/')
            else:kept.append(name)
        dirs[:]=kept
        for name in files:
            if len(rows)>=max_files:truncated=True;break
            p=Path(cur)/name;rel=p.relative_to(root).as_posix()
            try:
                if p.is_symlink():excluded.append(rel);continue
                st=p.stat();rows.append({'path':rel,'bytes':st.st_size,'extension':p.suffix.lower()})
            except OSError as exc:excluded.append(rel+': '+type(exc).__name__)
        if truncated:break
    return {'kind':'metadata-inspection','kernel_version':VERSION,'root_label':root.name,
            'files':rows,'excluded_or_unreadable':excluded,'truncated':truncated,
            'coverage':'Names and sizes only; no file contents, Git history, ignored directories, symlinks or runtime behavior inspected. Not a subject digest or quality score.'}

def check_package() -> dict[str,Any]:
    manifest=load_json(ROOT/'MANIFEST.json');expected=manifest['files'];need(isinstance(expected,list),'bad manifest')
    paths=[r['path'] for r in expected];need(len(paths)==len(set(paths)),'duplicate manifest path')
    for item in expected:
        p=safe_file(ROOT,item['path'])
        need(p.stat().st_size==item['bytes'],'manifest size mismatch: '+item['path'])
        need(file_digest(p)==item['digest'],'manifest digest mismatch: '+item['path'])
    actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file()
            and '__pycache__' not in p.parts and '.local-runs' not in p.parts
            and p.name!='MANIFEST.json'}
    need(actual==set(paths),f'manifest file set differs: {sorted(actual^set(paths))}')
    return {'status':'PASS','files_verified':len(paths),'meaning':'Integrity relative to this unsigned manifest; no independent authenticity claim.'}

def init_assessment(destination:Path,profile:str,subject_label:str) -> dict[str,Any]:
    need(not destination.exists(),'destination already exists; refusing overwrite')
    pp=load_json(safe_file(ROOT/'profiles',profile+'.json'));validate_record(pp)
    cat=load_json(ROOT/'catalog/catalog.json')
    # Small starting set. Full-domain review is a parallel procedure, not 1,080 compulsory tasks.
    ids=['PEP-01-01-01','PEP-01-02-01','PEP-01-03-01','PEP-01-04-02',
         'PEP-03-02-02','PEP-03-03-04','PEP-06-02-01','PEP-06-02-02',
         'PEP-17-02-01','PEP-17-03-01','PEP-17-04-01','PEP-18-01-04']
    now=datetime.now(timezone.utc).isoformat()
    a={'kind':'assignment','schema_version':VERSION,'id':'REPLACE_WITH_ASSIGNMENT_ID','record_status':'TEMPLATE',
       'epoch_id':'REPLACE_WITH_EPOCH','status':'PROPOSED','subject_id':subject_label,
       'subject_digest':'sha256:'+'0'*64,'mandate_ref':'REPLACE_WITH_ACTUAL_MANDATE','intent_ref':'REPLACE_WITH_INTENT',
       'catalog_digest':file_digest(ROOT/'catalog/catalog.json'),'profile_id':profile,
       'coverage_statement':'Initial 12-entry selection; review profile and capability risks before locking. Remaining catalog is unassessed.',
       'created_at':now,'scope_review_status':'PENDING','scope_review_ref':None,
       'instances':[{'id':'I-'+str(n+1),'criterion_id':cid,'criterion_revision':VERSION,'obligation_key':cid,'scope':'REPLACE_WITH_BOUNDED_SCOPE',
                     'applicability':'UNRESOLVED','applicability_reason':'Needs capability-based decision','applicability_decision_ref':None,
                     'weight':1,'mandatory':False,'measurement_binding_ref':None} for n,cid in enumerate(ids)],'gates':[]}
    m={'kind':'assessment','schema_version':VERSION,'id':'REPLACE_WITH_ASSESSMENT_ID','record_status':'TEMPLATE',
       'assignment_id':a['id'],'epoch_id':a['epoch_id'],'subject_digest':a['subject_digest'],'catalog_digest':a['catalog_digest'],
       'as_of':now,'result_ids':[],'evidence_ids':[],'qualification_ids':[],
       'coverage_limitations':['No product observations collected. Template placeholders are not operational state.'],
       'registration_state':'NOT_REQUESTED', 'assignment_digest':'sha256:'+'0'*64}
    validate_record(a);validate_record(m)
    destination.mkdir(parents=True)
    for folder in ['results','evidence','qualifications','raw']:(destination/folder).mkdir()
    write_json_new(destination/'assignment.json',a)
    m['assignment_digest']=file_digest(destination/'assignment.json')
    write_json_new(destination/'assessment.json',m)
    return {'status':'TEMPLATE_CREATED','destination':str(destination),'selected_entries':len(ids),
            'warning':'Not a locked assignment, grading run, authority grant, or product acceptance.'}

def main(argv:list[str]|None=None)->int:
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('catalog');p.add_argument('--domain')
    p=sub.add_parser('validate');p.add_argument('file',type=Path)
    p=sub.add_parser('summarize');p.add_argument('bundle',type=Path)
    p=sub.add_parser('inspect');p.add_argument('root',type=Path);p.add_argument('--max-files',type=int,default=5000)
    p=sub.add_parser('init-assessment');p.add_argument('--out',type=Path,required=True);p.add_argument('--profile',default='bootstrap');p.add_argument('--subject-label',required=True)
    sub.add_parser('check-package');sub.add_parser('self-test')
    args=parser.parse_args(argv)
    try:
        if args.command=='catalog':
            c=load_json(ROOT/'catalog/catalog.json');out=validate_catalog(c)
            if args.domain:
                need(any(d['id']==args.domain for d in c['domains']),'unknown domain')
                out['criteria']=[{'id':x['id'],'predicate':x['predicate'],'modality':x['modality']} for x in c['criteria'] if x['domain_id']==args.domain]
        elif args.command=='validate':
            x=load_json(args.file);validate_record(x);out={'status':'VALID_RECORD_SHAPE','kind':x['kind'],'warning':'Does not validate external authority, factual truth or all cross-record references.'}
        elif args.command=='summarize':out=summarize_bundle(args.bundle)
        elif args.command=='inspect':out=inspect_metadata(args.root,args.max_files)
        elif args.command=='init-assessment':out=init_assessment(args.out,args.profile,args.subject_label)
        elif args.command=='check-package':out=check_package()
        elif args.command=='self-test':
            env=dict(os.environ);env['PYTHONDONTWRITEBYTECODE']='1'
            return subprocess.run([sys.executable,'-m','unittest','discover','-s',str(ROOT/'tests'),'-v'],
                                  cwd=ROOT,env=env,check=False).returncode
        else:raise ValidationError('unsupported command')
        print(json.dumps(out,indent=2,ensure_ascii=False,allow_nan=False));return 0
    except (ValidationError,OSError,RecursionError) as exc:
        print(json.dumps({'status':'ERROR','message':str(exc)},ensure_ascii=False),file=sys.stderr);return 2

if __name__=='__main__':raise SystemExit(main())
