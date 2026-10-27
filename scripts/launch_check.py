#!/usr/bin/env python3
"""Local-only launch audit; no upload, login, Git mutation or publication."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def run(*args, cwd=ROOT):
    subprocess.run([sys.executable, *args], cwd=cwd, check=True)


def artifacts(root):
    paths = list((root / 'site/downloads').glob('*.zip'))
    paths += [root / 'dist/website.zip', *[root / 'dist' / v / 'sidebar/cookbook-sidebar.zip' for v in ('plain', 'kitchen')]]
    paths += list((root / 'dist/store').glob('*/*.zip'))
    paths += list((root / 'dist/remote').glob('*.zip'))
    return {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def main():
    run('scripts/cookbook.py', 'build')
    run('scripts/cookbook.py', 'check')
    run('scripts/cookbook.py', 'check-sources')
    run('-m', 'unittest', 'discover', '-s', 'tests')
    expected = artifacts(ROOT)
    with tempfile.TemporaryDirectory(prefix='cookbook-launch-') as temporary:
        portable = Path(temporary) / 'cookbook'
        shutil.copytree(ROOT, portable, ignore=shutil.ignore_patterns(
            '.git', '.scratch', 'site', 'dist', 'sources.local.json', '__pycache__', '*.pyc', '.DS_Store'))
        run('scripts/cookbook.py', 'build', cwd=portable)
        run('scripts/cookbook.py', 'check', cwd=portable)
        run('-m', 'unittest', 'discover', '-s', 'tests', cwd=portable)
        if artifacts(portable) != expected:
            raise ValueError('Portable artifact hashes differ')
    config = json.loads((ROOT / 'bundle.json').read_text())
    report = {'scope': 'local-only', 'version': config['version'],
              'selected_store_variant': config['store_variant'],
              'packaging': 'pass', 'portable_rebuild': 'pass', 'sha256': expected,
              'store_submission': 'not-assessed-by-local-checks',
              'remaining_gates': ['Clean desktop installation and main workflow acceptance of the exact upload package',
                  'Confirm submission access, verified publisher identity and portal category',
                  'Review the exact upload ZIP for unintended public content',
                  'Pass portal metadata and skill scans and store review',
                  'Explicit upload, submission and publication approval'],
              'separate_scopes': {
                  'website': ['Verify the GitHub Pages deployment and public legal/privacy destinations'],
                  'local_mcp_sidebar': ['Confirm partner eligibility and organization allowlisting before submission'],
                  'optional_verification': ['Additional TruffleHog coverage; absence alone is not a store blocker']}}
    (ROOT / 'dist/launch-report.json').write_text(json.dumps(report, indent=2) + '\n')
    print('PASS: local artifacts and portable rebuild. Public launch gates remain; see dist/launch-report.json')


if __name__ == '__main__':
    main()
