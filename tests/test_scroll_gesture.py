"""Behavior checks for boundary gestures; uses an optional installed JS runtime."""
from pathlib import Path
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which('node')


class ScrollGestureContracts(unittest.TestCase):
    @unittest.skipUnless(NODE, 'Optional Node.js runtime unavailable for JS gesture checks')
    def test_reading_boundaries_momentum_direction_and_modifiers(self):
        source = (ROOT / 'ui/scroll-gesture.js').read_text()
        checks = r'''
const assert = require('node:assert/strict');
let gate = new BookScrollGesture();
const wheel = (delta,time,edge,extra={}) => gate.update({delta,time,edge,...extra});
// Reading content and scrolling controls must not accumulate a pending flip.
assert.equal(wheel(200,0,0),0);
assert.equal(wheel(200,10,1,{eligible:false}),0);
assert.equal(wheel(35,20,1),0);
assert.equal(wheel(35,30,1),0);
assert.equal(wheel(15,40,1),1);
// Animation and cooldown consume motion without queueing extra turns.
for(let time=50;time<650;time+=20)assert.equal(wheel(100,time,1),0);
// Sustained input turns again after cooldown and fresh accumulation.
assert.equal(wheel(90,700,1),0);
assert.equal(wheel(90,720,1),1);
// Decaying trackpad inertia does not trigger a third turn.
for(let time=740;time<1500;time+=20)assert.equal(wheel(8,time,1),0);
assert.equal(wheel(90,1740,1),1);
// A direction change starts a new accumulation rather than using old movement.
gate = new BookScrollGesture();
assert.equal(wheel(60,0,1),0);
assert.equal(wheel(-50,20,-1),0);
assert.equal(wheel(-40,40,-1),-1);
// A new spread with overflowing content remains scrollable until its next boundary.
gate = new BookScrollGesture();
assert.equal(wheel(100,0,1),1);
assert.equal(wheel(100,700,0),0);
assert.equal(gate.locked,false);
assert.equal(wheel(100,900,1),1);
// Busy animation input never accumulates a queued turn.
gate = new BookScrollGesture();
assert.equal(wheel(100,0,1),1);
for(let time=20;time<=700;time+=20)assert.equal(wheel(500,time,1,{busy:true}),0);
assert.equal(wheel(90,720,1),0);
assert.equal(wheel(90,740,1),1);
// Wrong-way motion at a boundary, an unfinished animation, and small noise do not turn.
gate = new BookScrollGesture();
assert.equal(wheel(-200,0,1),0);
assert.equal(wheel(200,20,1,{busy:true}),0);
assert.equal(wheel(1,220,1),0);
assert.equal(wheel(1,500,1),0);
'''
        result = subprocess.run([NODE, '-e', source + '\n' + checks],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)

    @unittest.skipUnless(NODE, 'Optional Node.js runtime unavailable for JS page checks')
    def test_fixed_frame_resets_internal_reading_positions(self):
        import re
        source = (ROOT / 'ui/book.js').read_text()
        reset = re.search(r'function resetPaperScroll\(direction=1\)\{.*?\n\}', source, re.S)[0]
        checks = r'''
const assert = require('node:assert/strict');
const pages = [{scrollTop:40,scrollHeight:1200,clientHeight:600},
               {scrollTop:80,scrollHeight:800,clientHeight:500},
               {scrollTop:0,scrollHeight:400,clientHeight:500}];
const document = {querySelectorAll: () => pages};
resetPaperScroll(1);
assert.deepEqual(pages.map(page=>page.scrollTop), [0,0,0]);
resetPaperScroll(-1);
assert.deepEqual(pages.map(page=>page.scrollTop), [600,300,0]);
resetPaperScroll();
assert.deepEqual(pages.map(page=>page.scrollTop), [0,0,0]);
'''
        result = subprocess.run([NODE, '-e', reset + '\n' + checks],
                                capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
