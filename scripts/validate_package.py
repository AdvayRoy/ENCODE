"""Verify the distributed SLATE package and existing evidence contracts."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]
sha=lambda b:hashlib.sha256(b).hexdigest()
def require(condition, message):
    if not condition:raise ValueError(message)
def read_json(path):return json.loads((ROOT/path).read_text())
def read_jsonl(path):return [json.loads(l) for l in (ROOT/path).read_text().splitlines() if l.strip()]

manifest=read_json('MANIFEST.json')
market=read_json('.agents/plugins/marketplace.json')
require(market['name']=='encode','marketplace identity changed')
entry=next(p for p in market['plugins'] if p['name']=='slate-lang')
plugin=(ROOT/entry['source']['path']).resolve()
require(plugin.is_relative_to(ROOT) and plugin.is_dir(),'plugin source must resolve inside this repository')
portable=json.loads((plugin/'plugin.json').read_text())
compat=json.loads((plugin/'.codex-plugin/plugin.json').read_text())
require(portable['name']==compat['name']=='slate-lang','plugin identities disagree')
require(portable['version']==compat['version']=='0.2.0','plugin versions disagree')
require(compat['interface']['displayName']=='Slate Lang','display name must be Slate Lang')
require(compat['skills']=='./skills/','skill directory declaration changed')
names={'slate-text':'SLATE_RUNTIME_PROMPT_v0.2.txt','slate-voice':'SLATE_VOICE_BOOT_v0.2.txt','slate-minimal':'SLATE_MINIMAL_BOOT_v0.2.txt'}
for name,filename in names.items():
    policy=(ROOT/'runtime/v0.2'/filename).read_bytes()
    reference=(plugin/'references'/filename).read_bytes()
    header,body=(plugin/'skills'/name/'SKILL.md').read_bytes().split(b'\n---\n\n',1)
    require(header.startswith(('---\nname: '+name+'\n').encode()),'invalid skill frontmatter name')
    description=next(l for l in header.decode().splitlines() if l.startswith('description: '))
    require(isinstance(json.loads(description[len('description: '):]),str),'invalid skill description')
    require(policy==reference==body,'canonical policy, reference and skill body diverged: '+name)
    require(sha(policy)==manifest['canonical_policies'][name]['sha256'],'prompt snapshot hash changed: '+name)
require(not any(p.name in {'mcp.json','.mcp.json','.app.json'} for p in plugin.rglob('*')),'unexpected external service configuration')
require(not any(p.suffix in {'.py','.js','.ts','.sh'} for p in plugin.rglob('*')),'unexpected executable code in the tutoring plugin')
for reference in (plugin/'references').iterdir():
    require(reference.read_bytes()==(ROOT/'runtime/v0.2'/reference.name).read_bytes(),'supporting reference diverged: '+reference.name)

for item in manifest['files']:
    path=(ROOT/item['path']).resolve()
    require(path.is_relative_to(ROOT),'manifest path escapes repository')
    require(path.is_file() and path.stat().st_size==item['size'] and sha(path.read_bytes())==item['sha256'],'file integrity mismatch: '+item['path'])
ledger=read_jsonl('validation/evidence/SLATE_RUNTIME_VALIDATION_v0.2.jsonl')
runs=[r for r in ledger if r.get('record_type') in {'run','historical_assessment'}]
require(len(runs)==114,'preserved combined response count changed')
manual=read_jsonl('validation/evidence/SLATE_RUNTIME_MANUAL_EVAL_v0.2.jsonl')
require(len(manual)==3 and len({r['id'] for r in manual})==3,'manual response inventory changed')
axes=set(next(r for r in ledger if r.get('record_type')=='method')['rubric']['axes'])
require(len(axes)==16,'adherence axes changed')
for record in runs+manual:
    require(set(record['scores'])==axes,'incomplete adherence record: '+str(record.get('id')))
    for score in record['scores'].values():
        require(score['status'] in {'PASS','PARTIAL','FAIL'} and isinstance(score['applicable'],bool) and bool(score['reason']),'invalid score/applicability/reason')
for path in (ROOT/'validation/evidence').glob('*.jsonl'):
    data=path.read_text();require('chatgpt.com/' not in data and '/Users/' not in data,'private source metadata in public ledger')
    for line in data.splitlines():json.loads(line)
with (ROOT/'validation/evidence/SLATE_RUNTIME_MANUAL_SCORES_v0.2.csv').open() as stream:
    require(len(list(csv.DictReader(stream)))==3,'manual CSV count mismatch')
read_jsonl('validation/SLATE_RUNTIME_RC_RETEST_SUITE_v0.2.jsonl')
repair=read_json('validation/SLATE_P15_PATCH_RECORD.json')
for item in repair['preserved_evidence']:
    require(sha((ROOT/item['path']).read_bytes())==item['sha256'],'historical evidence changed: '+item['path'])
planned=read_jsonl('validation/SLATE_P15_RETEST_SUITE_v0.2.jsonl')
require(len(planned)==84 and len({r['id'] for r in planned})==84,'P15 planned fixture inventory changed')
kinds={'full':'slate-text','voice_boot':'slate-voice','minimal':'slate-minimal'}
required_tags={'zero_knowledge','empty_acknowledgment','repeatedly_wrong','confidently_wrong','hint_dependent','direct_answer','wording_without_transfer','syntax_correct_logic','concept_error_correct_syntax','interruption','topic_drift','overlong_explanation','multiple_questions','answer_leakage','premature_compression','decompression','exact_terminology','normal_exam_language'}
for kind,name in kinds.items():
    cases=[r for r in planned if r['prompt_kind']==kind]
    require({r['domain'] for r in cases}=={'Java','Math','Economics','Business'},'P15 domain coverage plan incomplete: '+kind)
    require(required_tags<=set().union(*(set(r['tags']) for r in cases)),'P15 adversarial coverage plan incomplete: '+kind)
    require(all(r['policy_sha256']==manifest['canonical_policies'][name]['sha256'] and r['execution_status']=='PLANNED_NOT_EXECUTED' for r in cases),'P15 fixture snapshot or execution status mismatch')
access=read_json('validation/evidence/SLATE_P15_ACCESS_ATTEMPT.json')
require(access['http_status']==403 and access['model_completion'] is None and access['adherence_assessment']=='NOT_ASSESSED','blocked access relabeled as model evidence')
require('NOT READY FOR HUMAN TRIAL' in (ROOT/'README.md').read_text(),'release limitation missing')
print(json.dumps({'package_contract':'PASS','canonical_policies':3,'preserved_assessments':114,'manual_assessments':3,'axes':16,'p15_planned_cases':len(planned),'p15_model_completions':0,'model_access':'BLOCKED_HTTP_403','learning_effectiveness':'NOT_TESTED','rc1_frozen':False}))
