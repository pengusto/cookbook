"""Maintain the declared Python 3.10 source-syntax floor on newer development hosts."""
import ast
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PythonCompatibility(unittest.TestCase):
    def test_runtime_and_build_sources_accept_python_310_grammar(self):
        for folder in ('scripts', 'skills'):
            for path in (ROOT / folder).rglob('*.py'):
                with self.subTest(path=str(path.relative_to(ROOT))):
                    ast.parse(path.read_text(), filename=str(path), feature_version=(3, 10))
