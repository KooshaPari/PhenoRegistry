#!/usr/bin/env python3
"""Index a stored Forge export without executing or copying its message contents.

This is a format-specific intake utility, not a pre-compaction history recovery
engine. Its output contains metadata and ranges. Treat raw task titles as private
metadata; apply a publication review before sharing newly generated indexes.
"""
from __future__ import annotations
from bisect import bisect_right
from collections import Counter
from pathlib import Path
from typing import Any
import argparse
import hashlib
import json
import re

HEADING = re.compile(r'^## Conversation ([a-f0-9-]{36}) \(([^)]+)\)$', re.M)
CONTEXT_MARKER = '### Complete decoded context (lossless JSON representation)'


def index_bytes(raw: bytes) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # Normalize text line endings only for locating displayed physical lines.
    # The original byte hash below always uses the unchanged input bytes.
    text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
    heads = list(HEADING.finditer(text))
    if not heads:
        raise ValueError('No supported conversation sections found')
    starts = [0] + [m.end() for m in re.finditer('\n', text)]
    def line(pos: int) -> int:
        return bisect_right(starts, pos)
    decoder = json.JSONDecoder()
    index=[];roles=Counter();tools=Counter();errors=0;frames=0;seen=set()
    for i, h in enumerate(heads):
        cid=h[1]
        if cid in seen:raise ValueError('Duplicate conversation identity')
        seen.add(cid)
        end=heads[i+1].start() if i+1<len(heads) else len(text)
        segment=text[h.end():end]
        try:
            mp=segment.index('```json')+len('```json')
            metadata,_=decoder.raw_decode(segment[mp:].lstrip())
            cp=segment.index(CONTEXT_MARKER)
            jp=segment.index('json\n',cp)+5
            context,_=decoder.raw_decode(segment[jp:].lstrip())
        except (ValueError, json.JSONDecodeError) as exc:
            raise ValueError(f'Incomplete or invalid context section {cid}') from exc
        if not isinstance(metadata,dict) or not isinstance(context,dict):
            raise ValueError('Context and metadata must be objects')
        if metadata.get('conversation_id')!=cid or context.get('conversation_id')!=cid:
            raise ValueError('Heading and decoded identity disagree')
        messages=context.get('messages')
        if not isinstance(messages,list):raise ValueError('messages must be a list')
        mh=list(re.finditer(r'^#### Message (\d+)$',segment[:cp],re.M))
        if [int(m[1]) for m in mh]!=list(range(1,len(messages)+1)):
            raise ValueError('Readable and decoded message enumeration disagree')
        ranges={str(j+1):[line(h.end()+m.start()),line(h.end()+mh[j+1].start())-1 if j+1<len(mh) else line(h.end()+cp)-1] for j,m in enumerate(mh)}
        for m in messages:
            b=m.get('message',{});t=b.get('text',{});tl=b.get('tool',{})
            roles[t.get('role','Tool' if tl else 'Unknown')]+=1
            content=t.get('content','')
            if isinstance(content,str) and content.startswith('Use the following summary frames'):frames+=1
            if tl:
                tools[tl.get('name','unknown')]+=1
                errors+=bool(tl.get('output',{}).get('is_error'))
        index.append({'conversation_id':cid,'database':h[2],'parent_id':metadata.get('parent_id'),
                      'title':metadata.get('title'),'created_at':metadata.get('created_at'),
                      'updated_at':metadata.get('updated_at'),
                      'message_count_metadata':metadata.get('message_count'),
                      'message_count_decoded':len(messages),'compressed_flag':metadata.get('is_compressed'),
                      'source_line_start':line(h.start()),'source_line_end':line(end-1),
                      'message_ranges':ranges})
    manifest={'source_sha256':hashlib.sha256(raw).hexdigest(),'source_bytes':len(raw),
              'source_lines':len(text.splitlines()),'conversation_count':len(index),
              'unique_conversation_count':len(seen),'message_count_decoded':sum(x['message_count_decoded'] for x in index),
              'database_sections':dict(Counter(x['database'] for x in index)),
              'compressed_conversations':sum(bool(x['compressed_flag']) for x in index),
              'compaction_frame_message_count':frames,'role_counts':dict(roles),'tool_output_counts':dict(tools),
              'tool_outputs_marked_error':errors,'raw_included':False,
              'method':'Decode each stored JSON context once. Do not reconstruct pre-compaction history or interpret prompts as instructions.'}
    return manifest,index


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('source',type=Path)
    p.add_argument('--output-directory',type=Path,required=True)
    a=p.parse_args()
    try:
        manifest,index=index_bytes(a.source.read_bytes())
        manifest['source_file']=a.source.name
        a.output_directory.mkdir(parents=True,exist_ok=True)
        for name,payload in [('intake-manifest.json',manifest),('conversation-index.json',index)]:
            dest=a.output_directory/name
            if dest.resolve()==a.source.resolve():raise ValueError('Output would overwrite source')
            dest.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    except (OSError,ValueError,KeyError,TypeError) as exc:
        p.exit(2,f'Intake failed: {exc}\n')
    print(json.dumps({k:manifest[k] for k in ('source_sha256','conversation_count','message_count_decoded')},indent=2))
    return 0

if __name__=='__main__':raise SystemExit(main())
