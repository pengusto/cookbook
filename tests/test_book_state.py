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
