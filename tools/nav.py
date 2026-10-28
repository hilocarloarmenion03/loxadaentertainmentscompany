#!/usr/bin/env python3
"""Offline ICM + deterministic Graphify. Python standard library; no credentials/network."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
STATES = {'READY','BLOCKED','CLAIMED','SUBMITTED','APPROVED','INTEGRATED','REJECTED'}
RESERVED = {'ACTIVE','SUBMITTED'}

def read(root, path):
    return json.loads((root / path).read_text())

def catalogs(root):
    return read(root,'knowledge/icm/routes.json')['routes'], read(root,'coordination/tasks.json')['tasks']

def graph_data(root):
    routes,tasks=catalogs(root)
    nodes=[{'id':r['id'],'kind':'context','title':r['title'],'files':r['files'],'status':r['status']} for r in routes]
    nodes += [{'id':t['id'],'kind':'task','title':t['title'],'status':t['state']} for t in tasks]
    edges=[{'from':r['id'],'to':n,'type':'related'} for r in routes for n in r.get('related',[])]
    edges += [{'from':t['id'],'to':d,'type':'requires'} for t in tasks for d in t['deps']]
    return {'schema_version':1,'nodes':sorted(nodes,key=lambda n:n['id']),'edges':sorted(edges,key=lambda e:(e['from'],e['to'],e['type']))}

def encoded(value):
    return json.dumps(value,indent=2,ensure_ascii=False)+'\n'

def safe_path(path):
    p=Path(path)
    return bool(path) and not p.is_absolute() and '..' not in p.parts and '\\' not in path

def overlaps(a,b):
    a,b=a.rstrip('/'),b.rstrip('/')
    return a==b or a.startswith(b+'/') or b.startswith(a+'/')

def ready(root):
    _,tasks=catalogs(root); by={t['id']:t for t in tasks}
    reserved={c['task'] for c in read(root,'coordination/claims.json')['claims'] if c['state'] in RESERVED}
    return [t for t in tasks if t['state']=='READY' and t['id'] not in reserved and all(by.get(d,{}).get('state')=='INTEGRATED' for d in t['deps'])]

def route(root,query,limit=5):
    words=set(re.findall(r'[\w.-]+',query.lower()))
    routes,_=catalogs(root); ranked=[]
    for r in routes:
        score=sum(3 if k in words else 1 if k in query.lower() else 0 for k in r['keywords'])
        if score:ranked.append((score,r))
    return [{'id':r['id'],'title':r['title'],'status':r['status'],'score':s,'files':r['files'],'related':r.get('related',[])} for s,r in sorted(ranked,key=lambda x:(-x[0],x[1]['id']))[:limit]]

def neighborhood(root,node,depth=1):
    g=graph_data(root); known={n['id'] for n in g['nodes']}
    if node not in known:raise ValueError('Unknown node: '+node)
    found={node};front={node}
    for _ in range(depth):
        new={e['to'] if e['from'] in front else e['from'] for e in g['edges'] if e['from'] in front or e['to'] in front}-found
        found|=new;front=new
    return {'nodes':[n for n in g['nodes'] if n['id'] in found],'edges':[e for e in g['edges'] if e['from'] in found and e['to'] in found]}

def doctor(root):
    errors=[]
    try:
        routes,tasks=catalogs(root); claims=read(root,'coordination/claims.json')['claims']
        ids=[r['id'] for r in routes]+[t['id'] for t in tasks]
        if len(ids)!=len(set(ids)):errors.append('Duplicate context/task ID')
        known=set(ids);by={t['id']:t for t in tasks}
        for r in routes:
            for f in r['files']:
                if not safe_path(f) or not (root/f).is_file():errors.append('Missing/unsafe routed file: '+f)
            for n in r.get('related',[]):
                if n not in known:errors.append('Dangling related node: '+n)
        for t in tasks:
            if t['state'] not in STATES:errors.append('Unknown task state: '+t['id'])
            for d in t['deps']:
                if d not in by:errors.append('Unknown prerequisite: '+d)
            for p in t['scope']:
                if not safe_path(p):errors.append('Unsafe task scope: '+p)
            if t['state'] in {'READY','INTEGRATED'} and any(by.get(d,{}).get('state')!='INTEGRATED' for d in t['deps']):errors.append('Unmet prerequisite: '+t['id'])
            if t['state']=='INTEGRATED' and not t.get('evidence'):errors.append('Missing integration evidence: '+t['id'])
            for p in t.get('evidence',[]):
                if not safe_path(p) or not (root/p).is_file():errors.append('Missing evidence file: '+p)
        visiting=set();seen=set()
        def visit(n):
            if n in visiting:raise ValueError('Task dependency cycle: '+n)
            if n in seen:return
            visiting.add(n)
            for d in by[n]['deps']:
                if d in by:visit(d)
            visiting.remove(n);seen.add(n)
        for n in by:visit(n)
        nonces=set();active=[]
        for c in claims:
            if c['nonce'] in nonces:errors.append('Duplicate claim nonce')
            nonces.add(c['nonce'])
            if c['task'] not in by:errors.append('Unknown claimed task')
            if c['state'] not in {'ACTIVE','SUBMITTED','RELEASED','REVOKED'}:errors.append('Unknown claim state')
            if c['state'] in RESERVED:
                if not c.get('owner') or not c.get('base_sha') or not c.get('scope'):errors.append('Incomplete reserved claim')
                if c['state']=='ACTIVE':
                    until=datetime.fromisoformat(c['expires_at'].replace('Z','+00:00'))
                    if until.tzinfo is None or until<=datetime.now(timezone.utc):errors.append('Expired/unreleased claim: '+c['task'])
                for p in c['scope']:
                    if not safe_path(p):errors.append('Unsafe claim scope')
                for other in active:
                    if c['task']==other['task'] or any(overlaps(a,b) for a in c['scope'] for b in other['scope']) or set(c.get('halo',[]))&set(other.get('halo',[])):errors.append('Reserved claim conflict')
                active.append(c)
        manifest=read(root,'knowledge/specification/manifest.json'); blob=(root/manifest['path']).read_bytes()
        if len(blob)!=manifest['bytes'] or hashlib.sha256(blob).hexdigest()!=manifest['sha256'] or hashlib.sha1(b'blob '+str(len(blob)).encode()+b'\0'+blob).hexdigest()!=manifest['git_blob_sha']:errors.append('Pinned baseline integrity mismatch')
        g=graph_data(root)
        if read(root,'knowledge/graphify/graph.json')!=g:errors.append('Stale generated graph; run graph-build')
        # Check navigable local Markdown links, excluding the immutable upstream baseline.
        for file in root.rglob('*.md'):
            if file==root/manifest['path']:continue
            for link in re.findall(r'\]\(([^)]+)\)',file.read_text()):
                if '://' in link or link.startswith(('#','mailto:')):continue
                target=link.split('#',1)[0]
                if target and not (file.parent/target).exists():errors.append('Broken Markdown link: '+str(file.relative_to(root))+' -> '+target)
    except (ValueError,KeyError,TypeError,OSError) as exc:errors.append(str(exc))
    return errors

def specification(root,process,contains='',context=32):
    manifest=read(root,'knowledge/specification/manifest.json');lines=(root/manifest['path']).read_text().splitlines();headings={};hits=[]
    for i,line in enumerate(lines):
        h=re.match(r'^(#{1,6})\s+(.+)',line)
        if h:
            level=len(h[1]);headings={k:v for k,v in headings.items() if k<level};headings[level]=h[2]
        if line.strip()=='Id: '+process:
            scope=' > '.join(headings.values())
            if contains.lower() in scope.lower():hits.append({'line':i+1,'heading':scope,'text':'\n'.join(lines[i:i+context])})
    return hits

def main():
    p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('doctor');sub.add_parser('graph-build');sub.add_parser('ready');sub.add_parser('status')
    r=sub.add_parser('route');r.add_argument('query');r.add_argument('--limit',type=int,default=5)
    g=sub.add_parser('graph');g.add_argument('node');g.add_argument('--depth',type=int,choices=range(1,5),default=1)
    s=sub.add_parser('spec');s.add_argument('process');s.add_argument('--contains',default='');s.add_argument('--context',type=int,choices=range(1,81),default=32)
    args=p.parse_args()
    try:
        if args.cmd=='doctor':
            e=doctor(ROOT);print(encoded({'ok':not e,'errors':e}));return bool(e)
        if args.cmd=='graph-build':
            (ROOT/'knowledge/graphify/graph.json').write_text(encoded(graph_data(ROOT)));print('Graph rebuilt from authoritative catalogs');return 0
        if args.cmd=='ready':result=ready(ROOT)
        elif args.cmd=='route':
            if not 1<=args.limit<=10:p.error('limit must be1..10')
            result=route(ROOT,args.query,args.limit)
        elif args.cmd=='graph':result=neighborhood(ROOT,args.node,args.depth)
        elif args.cmd=='spec':result=specification(ROOT,args.process,args.contains,args.context)
        else:result={'repository':'hilocarloarmenion03/loxadaentertainmentscompany','schedules':read(ROOT,'coordination/tasks.json')['schedules'],'application':'NOT_INSTALLED_BY_KNOWLEDGE_BOOTSTRAP','ready_manual_tasks':[t['id'] for t in ready(ROOT)],'read_next':'knowledge/vault/CURRENT_STATE.md'}
        print(encoded(result));return 0 if result else 2
    except (ValueError,KeyError,OSError) as exc:print(str(exc),file=sys.stderr);return 1

if __name__=='__main__':sys.exit(main())
