"""Host invocation and content language are independent UI choices."""
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which('node')


class BookStateContracts(unittest.TestCase):
    @unittest.skipUnless(NODE, 'Optional Node.js unavailable for UI state checks')
    def test_copy_uses_current_invocation_and_preserves_manual_fallback(self):
        source = (ROOT / 'ui/book.js').read_text()
        handler = re.search(r"\$\('copy-command'\).addEventListener\('click',async\(\)=>\{.*?\n\}\);", source, re.S)[0]
        checks = r'''
const assert=require('node:assert/strict');
async function check(command,blocked){
 let language='de',copyTimer,callback,selectedNode;
 const locales={de:{copied:'Kopiert',copyManual:'Manuell kopieren',languageNote:'Hinweis',copyInvocation:'Aufruf kopieren'},en:{languageNote:'Note',copyInvocation:'Copy command'}};
 const controls={'copy-command':{dataset:{},addEventListener(name,handler){this.handler=handler;}},'copy-command-label':{textContent:locales.de.copyInvocation},'copy-status':{textContent:''},invocation:{textContent:command}};
 const $=id=>controls[id],writes=[];
 const navigator={clipboard:{async writeText(value){writes.push(value);if(blocked)throw Error('Denied');}}};
 const selection={removeAllRanges(){},addRange(range){selectedNode=range.node;}};
 const window={getSelection:()=>selection};
 const document={createRange:()=>({selectNodeContents(node){this.node=node;}})};
 const animate=()=>{},clearTimeout=()=>{},setTimeout=handler=>{callback=handler;return 1;};
 HANDLER
 await controls['copy-command'].handler();
 assert.deepEqual(writes,[command]);
 if(blocked){
  assert.equal(controls['copy-status'].textContent,locales.de.copyManual);
  assert.equal(selectedNode,controls.invocation);
  assert.equal(controls['copy-command'].dataset.copied,undefined);
 }else{
  assert.equal(controls['copy-command-label'].textContent,locales.de.copied);
  assert.equal(controls['copy-command'].dataset.copied,'true');
 }
 language='en';callback();
 assert.equal(controls['copy-command-label'].textContent,locales.en.copyInvocation);
 assert.equal(controls['copy-command'].dataset.copied,undefined);
 assert.equal(controls['copy-status'].textContent,locales.en.languageNote);
}
(async()=>{for(const command of ['$show-me-the-kitchen','/cookbook-by-pengusto:explain-the-cookbook'])for(const blocked of [false,true])await check(command,blocked);})().catch(error=>{console.error(error);process.exitCode=1;});
'''.replace('HANDLER', handler)
        result = subprocess.run([NODE, '-e', checks], capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(NODE, 'Optional Node.js unavailable for UI state checks')
    def test_keyboard_navigation_crosses_nested_chapter_boundaries(self):
        source = (ROOT / 'ui/book.js').read_text()
        registration = next(line for line in source.splitlines() if "button.addEventListener('keydown'" in line)
        checks = r'''
const assert = require('node:assert/strict');
const recipes=Array.from({length:18},(_,id)=>({id}));
const focused=[], chosen=[];
const buttons=recipes.map((_,index)=>({focus(){focused.push(index);}}));
const document={querySelectorAll:()=>buttons};
function chooseRecipe(index){chosen.push(index);}
for(const [index,key,expected] of [[3,'ArrowDown',4],[4,'ArrowUp',3],[17,'Home',0],[0,'End',17]]){
 const button={addEventListener(type,handler){this.handler=handler;}};
 REGISTRATION
 let prevented=false;
 button.handler({key,preventDefault(){prevented=true;}});
 assert.equal(chosen.at(-1),expected);
 assert.equal(focused.at(-1),expected);
 assert.equal(prevented,true);
}
'''.replace('REGISTRATION', registration)
        result = subprocess.run([NODE, '-e', checks], capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(NODE, 'Optional Node.js unavailable for UI state checks')
    def test_welcome_navigation_follows_source_identity_after_reordering(self):
        source = (ROOT / 'ui/book.js').read_text()
        registration = next(line for line in source.splitlines() if "querySelectorAll('[data-open-recipe]')" in line)
        checks = r'''
const assert = require('node:assert/strict');
for(const order of [['intro','start','return'], ['return','intro','start']]) {
 const recipes=order.map(sourceId=>({sourceId}));
 const buttons=['start','return'].map(id=>({dataset:{openRecipe:id},addEventListener(event,callback){this.action=callback;}}));
 const document={querySelectorAll:()=>buttons};
 const visited=[];
 function chooseRecipe(index,focus){visited.push([recipes[index].sourceId,focus]);}
 REGISTRATION
 buttons.forEach(button=>button.action());
 assert.deepEqual(visited,[['start',true],['return',true]]);
}
'''.replace('REGISTRATION', registration)
        result = subprocess.run([NODE, '-e', checks], capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(NODE, 'Optional Node.js unavailable for UI state checks')
    def test_static_pages_keep_their_language_and_invocations_follow_host(self):
        source = (ROOT / 'ui/book.js').read_text()
        functions = '\n'.join(re.search(r'function '+name+r'\([^)]*\)\{.*?\n\}', source, re.S)[0]
                              for name in ('currentBookLanguage', 'skillInvocation'))
        checks = r'''
const assert = require('node:assert/strict');
let publicBook=true, bookPage='welcome', language='ar', installHost='claude';
const document={body:{dataset:{publicLanguage:'de'}}};
for(const page of ['welcome','install','about']){
 bookPage=page;assert.equal(currentBookLanguage(),'de');
}
document.body.dataset.publicLanguage='en';
assert.equal(currentBookLanguage(),'en');
bookPage='recipe';assert.equal(currentBookLanguage(),'ar');
assert.equal(skillInvocation('youre-the-chef'),'/cookbook-by-pengusto:youre-the-chef');
assert.equal(skillInvocation('you-got-this'),'/cookbook-by-pengusto:you-got-this');
installHost='codex';assert.equal(skillInvocation('youre-the-chef'),'$youre-the-chef');
publicBook=false;bookPage='welcome';installHost='claude';
assert.equal(currentBookLanguage(),'ar');
assert.equal(skillInvocation('you-got-this'),'$you-got-this');
'''
        result = subprocess.run([NODE, '-e', functions + '\n' + checks],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
