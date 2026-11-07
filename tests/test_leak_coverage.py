"""Regression contracts for incomplete scanner fallback coverage."""
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SOURCE = Path(__file__).resolve().parents[1] / 'skills/did-i-leak/scripts/did_i_leak.py'
spec = importlib.util.spec_from_file_location('leak_coverage', SOURCE)
scanner = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = scanner
previous_bytecode = sys.dont_write_bytecode
sys.dont_write_bytecode = True
try:
    spec.loader.exec_module(scanner)
finally:
    sys.dont_write_bytecode = previous_bytecode


class CoverageTests(unittest.TestCase):
    def test_interrupted_history_scan_never_returns_a_verdict_or_updates_cache(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            (root / 'example.txt').write_text('ordinary public example\n')
            subprocess.run(['git', 'add', 'example.txt'], cwd=root, check=True)
            subprocess.run(
                ['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                 'commit', '-qm', 'fixture'], cwd=root, check=True,
            )
            class InterruptedCatFile:
                def __init__(self, output, status, broken_pipe=False):
                    class Input(io.BytesIO):
                        def write(self, data):
                            if broken_pipe:
                                raise BrokenPipeError('synthetic closed Git pipe')
                            return super().write(data)
                    self.stdin = Input()
                    self.stdout = io.BytesIO(output)
                    self.stderr = io.BytesIO()
                    self.status = status

                def wait(self, timeout=None):
                    return self.status

            original_popen = subprocess.Popen
            with patch.object(scanner, 'run_gitleaks', return_value=([], 'completed', None)), \
                 patch.object(scanner, 'run_trufflehog', return_value=([], 'completed', None)):
                self.assertEqual(scanner.scan_repo(root, full=True)['verdict'], 'GO')
                cache = root / '.git/did-i-leak/state.json'
                previous_cache = cache.read_bytes()
                (root / 'example.txt').write_text('changed public example\n')
                subprocess.run(['git', 'add', 'example.txt'], cwd=root, check=True)
                subprocess.run(
                    ['git', '-c', 'user.name=Test', '-c', 'user.email=test@example.invalid',
                     'commit', '-qm', 'new history'], cwd=root, check=True,
                )
                oid = subprocess.check_output(
                    ['git', 'rev-parse', 'HEAD:example.txt'], cwd=root, text=True,
                ).strip().encode()
                cached, cache_note = scanner.load_cache(root)
                plan = scanner.scan_plan(
                    root, scanner.repository_refs(root), cached, cache_note,
                    scanner.scanner_snapshot(True), full_requested=False,
                )
                self.assertFalse(plan['full'])
                self.assertTrue(plan['new_objects'])
                for label, output, status in (
                    ('missing header', b'', 0),
                    ('truncated blob', oid + b' blob 12\nshort', 0),
                    ('truncated large blob', oid + b' blob 4194305\n' + b'a' * 4194304, 0),
                    ('missing delimiter', oid + b' blob 4\nsafe', 0),
                    ('missing object', oid + b' missing\n', 0),
                    ('wrong object', b'b' * 40 + b' blob 4\nsafe\n', 0),
                    ('invalid type', oid + b' unknown 4\nsafe\n', 0),
                    ('invalid size', oid + b' blob invalid\n', 0),
                    ('failed process', oid + b' blob 4\nsafe\n', 128),
                    ('broken pipe', b'', 0),
                ):
                    for mode in ('full', 'incremental'):
                        def popen(args, *positional, **keywords):
                            if args[:3] == ['git', 'cat-file', '--batch']:
                                return InterruptedCatFile(output, status, label == 'broken pipe')
                            return original_popen(args, *positional, **keywords)
                        with self.subTest(failure=label, mode=mode):
                            stdout, stderr = io.StringIO(), io.StringIO()
                            args = ['--repo', str(root)] + (['--full'] if mode == 'full' else [])
                            with patch.object(subprocess, 'Popen', side_effect=popen), \
                                 redirect_stdout(stdout), redirect_stderr(stderr):
                                result = scanner.main(args)
                            self.assertEqual(result, 3)
                            self.assertNotIn('GO', stdout.getvalue())
                            self.assertIn('Git history scan incomplete', stderr.getvalue())
                            self.assertEqual(cache.read_bytes(), previous_cache)
                recovered = scanner.scan_repo(root)
                self.assertEqual(recovered['verdict'], 'GO')
                self.assertEqual(recovered['coverage']['scan_mode'], 'incremental')
                self.assertGreater(recovered['coverage']['historical_objects_scanned'], 0)
                with patch.object(scanner, 'detection_fingerprint', return_value='0' * 64):
                    scanner.scan_repo(root, full=True)
                refreshed = scanner.scan_repo(root)
                self.assertEqual(refreshed['coverage']['scan_mode'], 'full')
                self.assertIn('Detection logic changed', refreshed['coverage']['cache']['reason'])

    def test_unreadable_file_prevents_clean_verdict_even_with_completed_scanners(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            target = root / 'example.txt'
            target.write_text('ordinary public example\n')
            original = Path.read_bytes
            def read(path):
                if path == target:
                    raise PermissionError('synthetic read failure')
                return original(path)
            with patch.object(scanner, 'run_gitleaks', return_value=([], 'completed', None)), patch.object(scanner, 'run_trufflehog', return_value=([], 'completed', None)):
                clean = scanner.scan_repo(root, full=True)
                self.assertEqual(clean['verdict'], 'GO')
                with patch.object(Path, 'read_bytes', read):
                    result = scanner.scan_repo(root, full=True)
                self.assertEqual(result['verdict'], 'GO WITH REVIEW')
                self.assertEqual(result['coverage']['heuristic_unreadable_current_files'], 1)
                self.assertIn('1 current file(s) could not be read', scanner.render(result))
                recovered = scanner.scan_repo(root)
                self.assertEqual(recovered['verdict'], 'GO')
                self.assertEqual(recovered['coverage']['heuristic_unreadable_current_files'], 0)

    def test_large_text_and_binary_are_distinct_from_unreadable_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            (root / 'binary').write_bytes(b'\x00\x01')
            (root / 'large').write_bytes(b'a' * (scanner.MAX_TEXT_BYTES + 1))
            findings, capped, unreadable = scanner.scan_current_tree(root, {'binary', 'large'})
            self.assertEqual(findings, [])
            self.assertEqual((capped, unreadable), (1, 0))
