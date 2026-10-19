"""Regression contracts for incomplete current-tree fallback coverage."""
import importlib.util
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
