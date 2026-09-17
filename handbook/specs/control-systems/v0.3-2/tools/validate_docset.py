#!/usr/bin/env python3
"""Dependency-free consistency checks for this design package, NOT a deployment/security gate."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

ROOT=Path(__file__).resolve().parents[1]

class ValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def validate_payload(data: dict[str, Any], sources: dict[str, Any]) -> dict[str, int]:
    require(data.get('schema_version')=='0.3.0','Unsupported docset schema version')
    require(data.get('status')=='design_baseline_not_deployment_approval','Package status cannot imply deployment approval')
    require(sources.get('schema_version')=='0.3.0','Unsupported sources schema version')
    groups={}
    for field in ['findings','requirements','acceptance_tests','decisions','work_items']:
        rows=data.get(field)
        require(isinstance(rows,list) and len(rows)>0,f'{field} must be a nonempty list')
        require(all(isinstance(x,dict) and isinstance(x.get('id'),str) and x['id'] for x in rows),f'Invalid IDs in {field}')
        ids=[x['id'] for x in rows]
        require(len(ids)==len(set(ids)),f'Duplicate IDs in {field}')
        groups[field]={x['id']:x for x in rows}
    all_ids=[i for g in groups.values() for i in g]
    require(len(all_ids)==len(set(all_ids)),'Cross-group duplicate IDs')
    src_rows=sources.get('sources',[])
    src_ids=[s['id'] for s in src_rows]
    require(len(src_ids)==len(set(src_ids)) and len(src_ids)>0,'Invalid source IDs')
    src_set=set(src_ids)
    for field in ['findings','requirements','decisions']:
        for row in data[field]:
            refs=row.get('source_ids',[])
            require(bool(refs),f'{row["id"]} lacks sources')
            require(set(refs)<=src_set,f'{row["id"]} has unknown source')
    reqs=groups['requirements']; tests=groups['acceptance_tests']; findings=groups['findings']
    for rid,row in reqs.items():
        require(row.get('status')=='proposed',f'{rid} must remain a proposed requirement in this baseline')
        require(isinstance(row.get('statement'),str) and bool(row['statement'].strip()),f'{rid} lacks a statement')
        require(bool(row.get('finding_ids')) and set(row['finding_ids'])<=set(findings),f'{rid} has invalid finding references')
        tids=row.get('acceptance_test_ids',[])
        require(bool(tids) and set(tids)<=set(tests),f'{rid} has missing/unknown acceptance tests')
        for tid in tids:
            require(rid in tests[tid].get('requirement_ids',[]),f'{rid}/{tid} is not bidirectional')
    for tid,row in tests.items():
        require(row.get('status')=='not_run',f'{tid} cannot claim execution in this reviewed-source baseline')
        require(row.get('execution_evidence')==[],f'{tid} has unexpected claimed execution evidence')
        require(bool(row.get('evidence_required')),f'{tid} lacks required evidence definition')
        rids=row.get('requirement_ids',[])
        require(bool(rids) and set(rids)<=set(reqs),f'{tid} has missing/unknown requirements')
        require(bool(row.get('procedure')) and bool(row.get('expected')),f'{tid} is not operationally specified')
        for rid in rids:
            require(tid in reqs[rid]['acceptance_test_ids'],f'{tid}/{rid} is not bidirectional')
    for row in data['decisions']:
        permitted='accepted_user_constraint' if row['id'] in {'ADR-DEP-001','ADR-DEP-014'} else 'proposed'
        require(row.get('status')==permitted,f'{row["id"]} has an unsupported approval state')
        require(bool(row.get('alternatives')) and bool(row.get('revisit')),f'{row["id"]} lacks alternatives/revisit')
    require(data.get('unresolved',{}).get('exact_ci_trio','missing') is None,'Do not turn observed candidate job names into an approved exact trio binding')
    jobs=groups['work_items'];covered=set()
    for jid,row in jobs.items():
        require(set(row.get('depends_on',[]))<=set(jobs),f'{jid} has unknown dependencies')
        require(bool(row.get('requirement_ids')) and set(row['requirement_ids'])<=set(reqs),f'{jid} has invalid requirements')
        require(row.get('status')=='not_started',f'{jid} cannot imply work performed by this package')
        covered.update(row['requirement_ids'])
    require(covered==set(reqs),'Work packages do not cover all requirements')
    done=set();visiting=set()
    def visit(jid: str) -> None:
        require(jid not in visiting,'Work package dependency cycle')
        if jid in done:return
        visiting.add(jid)
        for dep in jobs[jid]['depends_on']:visit(dep)
        visiting.remove(jid);done.add(jid)
    for jid in jobs:visit(jid)
    return {field:len(rows) for field,rows in groups.items()} | {'sources':len(src_set)}


def validate_tree(root: Path) -> dict[str, Any]:
    data=json.loads((root/'machine/docset.json').read_text(encoding='utf-8'))
    sources=json.loads((root/'machine/sources.json').read_text(encoding='utf-8'))
    counts=validate_payload(data,sources)
    manifest=json.loads((root/'evidence/source-manifest.json').read_text(encoding='utf-8'))
    raw=(root/manifest['bundled_path']).read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    require(digest==manifest['sha256'],'Original source hash mismatch')
    require(len(raw)==manifest['bytes'],'Original source byte count mismatch')
    require(len(raw.decode('utf-8').splitlines())==manifest['lines'],'Original source line count mismatch')
    # Import by sibling path when executed as a CLI or in the included unit tests.
    from analyze_logs import analyze
    expected=analyze(root/manifest['bundled_path'])
    actual=json.loads((root/'evidence/log-metrics.json').read_text(encoding='utf-8'))
    require(actual==expected,'Stored log metrics differ from reproducible extraction')
    intake=json.loads((root/'evidence/session/intake-manifest.json').read_text(encoding='utf-8'))
    conversations=json.loads((root/'evidence/session/conversation-index.json').read_text(encoding='utf-8'))
    evidence=json.loads((root/'evidence/session/evidence-index.json').read_text(encoding='utf-8'))
    ids=[c['conversation_id'] for c in conversations]
    require(len(ids)==len(set(ids))==intake['conversation_count'],'Intake conversation identity/count mismatch')
    require(sum(c['message_count_decoded'] for c in conversations)==intake['message_count_decoded'],'Intake message count mismatch')
    require(sum(bool(c['compressed_flag']) for c in conversations)==intake['compressed_conversations'],'Compression count mismatch')
    require(intake['raw_included'] is False,'Raw full export must not be redistributed')
    by_id={c['conversation_id']:c for c in conversations}
    for entry in evidence:
        path=(root/entry['bundled_path']).resolve()
        require(path.is_relative_to(root.resolve()),'Evidence path escapes package')
        require(hashlib.sha256(path.read_bytes()).hexdigest()==entry['sha256'],'Derivative evidence hash mismatch: '+entry['id'])
        require(entry['source_lines']==by_id[entry['conversation_id']]['message_ranges'][str(entry['message'])],'Evidence range mismatch')
    for decision in data['decisions']:
        require((root/'adrs'/f'{decision["id"]}.md').is_file(),f'Missing ADR document {decision["id"]}')
    return dict(status='passed',scope='Internal docset consistency and source integrity only; no operational acceptance tests executed.',counts=counts,source_sha256=digest)


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--report',type=Path)
    args=parser.parse_args()
    try:
        result=validate_tree(args.root)
        output=json.dumps(result,indent=2)+'\n'
        if args.report:
            args.report.parent.mkdir(parents=True,exist_ok=True)
            args.report.write_text(output,encoding='utf-8')
        print(output,end='')
    except (OSError,ValueError,KeyError,TypeError) as exc:
        parser.exit(2,f'Docset validation failed: {exc}\n')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
