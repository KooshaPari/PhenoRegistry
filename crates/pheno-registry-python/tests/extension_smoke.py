"""Test the actual compiled extension: python extension_smoke.py PATH_TO_LIBRARY."""

import importlib.util
import sys
import unittest

spec = importlib.util.spec_from_file_location("pheno_registry_python", sys.argv.pop(1))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

SAMPLE = """| Role | Count | Repos |
|------|-------|-------|
| tooling | 1 | alpha |
| SDK | 1 | beta |

alpha -> beta
"""


class ExtensionTests(unittest.TestCase):
    def test_registration(self):
        self.assertEqual(module.__version__, "1.1.0")
        self.assertTrue(callable(module.parse_ecosystem_map_py))
        self.assertTrue(isinstance(module.RepoEntryPy, type))

    def test_dictionary_and_properties(self):
        entries = module.parse_ecosystem_map_py(SAMPLE)
        self.assertEqual(len(entries), 2)
        alpha = entries[0]
        self.assertIsInstance(alpha, module.RepoEntryPy)
        expected = dict(name="alpha", role="tooling", language=None,
                        status=None, notes=None, dependencies=["beta"])
        self.assertEqual(alpha.to_dict(), expected)
        for key, value in expected.items():
            self.assertEqual(getattr(alpha, key), value)
        self.assertIsInstance(alpha.to_dict()["dependencies"], list)
        self.assertTrue(all(isinstance(x, str) for x in alpha.dependencies))

    def test_optional_strings(self):
        source = """| Repo | Lang | Pushed | Proposed role | Notes |
|------|------|--------|---------------|-------|
| alpha | Rust | today | tooling | useful |

| Repo | Status | Verdict |
|------|--------|---------|
| alpha | Active | keep |
"""
        entry = module.parse_ecosystem_map_py(source)[0]
        result = entry.to_dict()
        self.assertEqual(result["language"], "Rust")
        self.assertEqual(result["status"], "Active")
        self.assertEqual(result["notes"], "useful")

    def test_errors(self):
        for source in ("", "   ", "| Role | Count | Repos |\n|---|---|---|\n| bad |\n"):
            with self.subTest(source=source), self.assertRaises(ValueError):
                module.parse_ecosystem_map_py(source)

    def test_representations(self):
        entry = module.parse_ecosystem_map_py(SAMPLE)[0]
        self.assertEqual(str(entry), "RepoEntry(alpha, role=tooling)")
        self.assertIn('RepoEntryPy(name="alpha", role="tooling"', repr(entry))


if __name__ == "__main__":
    unittest.main()
