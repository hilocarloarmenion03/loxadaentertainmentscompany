import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('nav',ROOT/'tools/nav.py');nav=importlib.util.module_from_spec(spec);spec.loader.exec_module(nav)

class Navigation(unittest.TestCase):
    def sandbox(self):
        t=tempfile.TemporaryDirectory();self.addCleanup(t.cleanup);out=Path(t.name)/'repo';shutil.copytree(ROOT,out,ignore=shutil.ignore_patterns('__pycache__'));return out
    def change(self,r,p,fn):
        f=r/p;value=json.loads(f.read_text());fn(value);f.write_text(json.dumps(value))
    def test_cold_start_offline_integrity_and_ready_manual_work(self):
        self.assertEqual(nav.doctor(ROOT),[])
        self.assertEqual([t['id'] for t in nav.ready(ROOT)],['SCHEMA-CONTRACTS'])
        self.assertEqual(nav.read(ROOT,'coordination/tasks.json')['schedules'],'PAUSED_BY_USER')
    def test_routing_is_bounded_relevant_and_unknown_is_visible(self):
        self.assertEqual(nav.route(ROOT,'merch invoice ownership')[0]['id'],'merch')
        self.assertEqual(nav.route(ROOT,'anime subscriber streaming')[0]['id'],'anime')
        self.assertEqual(nav.route(ROOT,'database dimensional etl')[0]['id'],'data')
        self.assertLessEqual(len(nav.route(ROOT,'owner account workflow task',2)),2)
        self.assertEqual(nav.route(ROOT,'zzzznotaconcept'),[])
    def test_exact_source_retrieval_keeps_department_context_and_lineage(self):
        hits=nav.specification(ROOT,'R-A-13',context=3)
        self.assertTrue(any('Merchandise' in h['heading'] and 'supplier invoice' in h['text'] for h in hits))
        self.assertTrue(all(len(h['text'].splitlines())<=3 for h in hits))
        self.assertEqual(nav.specification(ROOT,'NONEXISTENT'),[])
        self.assertEqual(nav.specification(ROOT,'R-A-13','not-the-heading'),[])
    def test_graph_deterministic_with_real_dependencies(self):
        self.assertEqual(nav.graph_data(ROOT),nav.read(ROOT,'knowledge/graphify/graph.json'))
        g=nav.neighborhood(ROOT,'SUPERADMIN-FIRST-FLOW')
        self.assertIn('STARTER-VERIFY',[n['id'] for n in g['nodes']])
        with self.assertRaises(ValueError):nav.neighborhood(ROOT,'unknown')
    def test_broken_navigation_and_stale_graph_fail_closed(self):
        r=self.sandbox();(r/'contracts/README.md').unlink()
        self.assertTrue(any('routed file' in e for e in nav.doctor(r)))
        r=self.sandbox();self.change(r,'knowledge/icm/routes.json',lambda d:d['routes'][0].update(title='Changed map'))
        self.assertTrue(any('Stale generated graph' in e for e in nav.doctor(r)))
        (r/'extra.md').write_text('[broken](missing.md)')
        self.assertTrue(any('Broken Markdown link' in e for e in nav.doctor(r)))
    def test_cycle_or_false_readiness_cannot_unlock_successors(self):
        r=self.sandbox();self.change(r,'coordination/tasks.json',lambda d:d['tasks'][0]['deps'].append('SUPERADMIN-FIRST-FLOW'))
        self.assertTrue(any('cycle' in e for e in nav.doctor(r)))
        r=self.sandbox();self.change(r,'coordination/tasks.json',lambda d:d['tasks'][0].update(state='BLOCKED'))
        self.assertEqual(nav.ready(r),[])
        self.assertTrue(any('Unmet prerequisite' in e for e in nav.doctor(r)))
    def test_expired_claim_stays_reserved_and_conflicting_paths_rejected(self):
        r=self.sandbox();claim={'nonce':'original','task':'SCHEMA-CONTRACTS','owner':'agent-a','base_sha':'a'*40,'state':'ACTIVE','expires_at':'2020-01-01T00:00:00Z','scope':['contracts/'],'halo':['schema']}
        self.change(r,'coordination/claims.json',lambda d:d['claims'].append(claim))
        self.assertEqual(nav.ready(r),[])
        self.assertTrue(any('Expired/unreleased' in e for e in nav.doctor(r)))
        other={**claim,'nonce':'other','task':'STARTER-VERIFY','owner':'agent-b','scope':['contracts/owner.json']}
        self.change(r,'coordination/claims.json',lambda d:d['claims'].append(other))
        self.assertTrue(any('claim conflict' in e for e in nav.doctor(r)))
        self.assertFalse(nav.overlaps('src/x','src/xyz'))
        self.assertTrue(nav.overlaps('src/x','src/x/y'))
    def test_tampered_baseline_or_path_escape_is_not_accepted(self):
        r=self.sandbox();f=r/'knowledge/specification/v1.0.md';f.write_bytes(f.read_bytes()+b'changed')
        self.assertTrue(any('integrity mismatch' in e for e in nav.doctor(r)))
        r=self.sandbox();self.change(r,'knowledge/icm/routes.json',lambda d:d['routes'][0]['files'].append('../outside.md'))
        self.assertTrue(any('unsafe routed file' in e for e in nav.doctor(r)))

if __name__=='__main__':unittest.main()
