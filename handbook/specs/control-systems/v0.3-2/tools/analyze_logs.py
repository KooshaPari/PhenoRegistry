#!/usr/bin/env python3
"""Narrow, reproducible pattern inventory; not a general JSONL parser or incident diagnosis."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
from typing import Any


def analyze(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    lines = raw.decode('utf-8').splitlines()
    traces = []
    warnings = []
    fallbacks = []
    sync_lines = []
    context_lines = []
    resolve_lines = []
    cpa_lines = []
    terminal_statuses: Counter[str] = Counter()
    terminal_nulls = 0
    unparsed_terminals = []
    for number, line in enumerate(lines, 1):
        if not line.startswith(('{"level":', '{"timestamp":')):
            continue
        time_match = re.search(r'"(?:time|timestamp)":"([^"]+)"', line)
        timestamp = time_match.group(1) if time_match else None
        if 'Combo context limit: 512000' in line:
            context_lines.append(number)
        if 'Attempting to resolve combo limits' in line:
            resolve_lines.append(number)
        if 'synced 0 model(s)' in line:
            sync_lines.append(number)
        if 'CLIProxyAPI →' in line:
            cpa_lines.append(number)
        m = re.search(r'combo trace (combo-[0-9a-f-]{36}).*decisions=(\d+)', line)
        if m:
            traces.append(dict(line=number, combo_id=m.group(1), decisions=int(m.group(2)), timestamp=timestamp))
            terminal = re.search(r'terminal=(.*?) decisions=', line)
            # Only decode this tiny known terminal-field shape. Never rewrite source bytes.
            normalized = terminal.group(1).replace('\\', '') if terminal else ''
            if re.fullmatch(r'\{"status":\d+,"errorClass":null\}', normalized):
                value = json.loads(normalized)
                terminal_statuses[str(value['status'])] += 1
                terminal_nulls += 1
            else:
                unparsed_terminals.append(number)
        if 'marking as invalid for combo failover' in line:
            kind = 'empty_completion' if 'with no content, reasoning, or' in line else 'upstream_error_before_content' if 'upstream error before content' in line else 'other'
            warnings.append(dict(line=number, kind=kind, timestamp=timestamp))
        m = re.search(r'succeeded \((\d+)ms, (\d+) fallbacks\)', line)
        if m:
            fallbacks.append(dict(line=number, reported_duration_ms=int(m.group(1)), reported_fallbacks=int(m.group(2)), timestamp=timestamp))
    hist = Counter(t['decisions'] for t in traces)
    return dict(
        schema_version='0.1.0', source_id='S001', source_sha256=hashlib.sha256(raw).hexdigest(),
        bytes=len(raw), lines=len(lines), method='Narrow string/regex extraction from structured-log-looking lines; source bytes unchanged.',
        counts=dict(context_limit_512000=len(context_lines), context_resolution=len(resolve_lines),
                    terminal_traces=len(traces), unique_combo_ids=len({t['combo_id'] for t in traces}),
                    decisions_histogram={str(k):v for k,v in sorted(hist.items())},
                    terminal_status_histogram=dict(terminal_statuses), terminal_error_class_null=terminal_nulls,
                    empty_completion_warnings=sum(w['kind']=='empty_completion' for w in warnings),
                    upstream_error_before_content_warnings=sum(w['kind']=='upstream_error_before_content' for w in warnings),
                    zero_model_sync_reports=len(sync_lines), cpa_route_lines=len(cpa_lines), explicit_fallback_events=len(fallbacks)),
        warning_events=warnings, explicit_fallback_events=fallbacks, unparsed_terminal_lines=unparsed_terminals,
        source_line_indexes=dict(context_limit=context_lines,context_resolution=resolve_lines,zero_model_sync=sync_lines,cpa_route=cpa_lines),
        trace_inventory=traces,
        coverage_limits=[
            'Partial, filtered and interleaved excerpt; selected sections are not globally time-ordered.',
            'No complete request/attempt denominator: no failure rate is computed.',
            'A decisions counter is not assumed to count upstream retries.',
            'Terminal HTTP status and reported duration are not application-success or end-to-end-latency proofs.',
            'No causal attribution to Cloudflare, model sync, providers, runtime or host follows from these counts.'
        ]
    )


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        result=analyze(args.input)
        text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(text,encoding='utf-8')
        else:
            print(text,end='')
    except (OSError,UnicodeError,ValueError) as exc:
        parser.exit(2,f'Cannot analyze input: {exc}\n')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
