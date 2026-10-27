"""Regression checks for remote book state; browser checks use remote_host.py."""
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which('node')
SOURCE = (ROOT / 'ui/remote.js').read_text()


@unittest.skipUnless(NODE, 'Optional Node.js unavailable for UI state checks')
class RemoteUIContracts(unittest.TestCase):
    def run_js(self, code):
        result = subprocess.run([NODE, '-e', code], capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_results_follow_names_preserve_ids_and_retry_current_selection(self):
        render = SOURCE[SOURCE.index(' function showResults('):SOURCE.index(' async function loadWorkflow(')]
        listener = SOURCE[SOURCE.index(" document.addEventListener('cookbook:recipe'"):SOURCE.index(" $('language-options').addEventListener")]
        code = r'''
const assert=require('node:assert/strict');
let naming='kitchen',resultIds=[],selected=0,ready=true;
const recipes=[{id:'release',names:{kitchen:'Ready to Serve',plain:'Am I Ready to Share?'}}];
const recipeName=r=>r.names[naming],calls=[],chosen=[];
const loadWorkflow=id=>calls.push(id),chooseRecipe=index=>chosen.push(index);
const text=()=>({empty:'No matches'}),status={};
const results={children:[],replaceChildren(){this.children=[];},append(node){this.children.push(node);},querySelectorAll(){return this.children;}};
const listeners={};
const document={createElement(){return {dataset:{},addEventListener(type,callback){this[type]=callback;}};},addEventListener(type,callback){listeners[type]=callback;}};
RENDER
LISTENER
showResults([{id:'release'},{id:'unknown'}]);
assert.equal(results.children.length,1);
assert.equal(results.children[0].textContent,'Ready to Serve');
results.children[0].click();
assert.deepEqual(calls,['release']); // same selection must retry a failed load
naming='plain';listeners['cookbook:recipe']({detail:{id:'release'}});
assert.equal(results.children[0].textContent,'Am I Ready to Share?');
assert.equal(results.children[0].dataset.recipeId,'release');
assert.deepEqual(calls,['release','release']);
showResults([]);assert.equal(status.textContent,'No matches');
'''.replace('RENDER', render).replace('LISTENER', listener)
        self.run_js(code)

    def test_late_response_cannot_replace_new_selection_or_error(self):
        loader = SOURCE[SOURCE.index(' async function loadWorkflow('):SOURCE.index(' function applySelection(')]
        code = r'''
const assert=require('node:assert/strict');
let selectionRequest=0,currentWorkflow=null;
const copy={},instructions={},instructionStatus={},pending=[];
const text=()=>({loading:'Loading',error:'Error'}),apiLanguage=()=> 'en';
const tool=(name,args)=>new Promise((resolve,reject)=>pending.push({args,resolve,reject}));
LOADER
(async()=>{
 const old=loadWorkflow('old'),latest=loadWorkflow('latest');
 pending[1].resolve({workflow:{id:'latest',instructions:'New instructions'}});await latest;
 pending[0].resolve({workflow:{id:'old',instructions:'Stale instructions'}});await old;
 assert.equal(instructions.textContent,'New instructions');assert.equal(copy.disabled,false);
 const failure=loadWorkflow('broken');pending[2].reject(Error('Synthetic failure'));await failure;
 assert.equal(instructions.textContent,'');assert.equal(copy.disabled,true);assert.equal(instructionStatus.textContent,'Error');
 const retry=loadWorkflow('broken');pending[3].resolve({workflow:{id:'broken',instructions:'Recovered'}});await retry;
 assert.equal(instructions.textContent,'Recovered');assert.equal(copy.disabled,false);
})().catch(error=>{console.error(error);process.exitCode=1;});
'''.replace('LOADER', loader)
        self.run_js(code)
