import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_marketplace import validate_marketplace


INVARIANTS = [
    "no_single_pillar_defines_reality",
    "recognition_continuous_unresolved",
    "software_test_neq_real_world_efficacy",
    "promotion_requires_independent_validation",
    "evidence_must_be_sealed",
    "status_labels_remain_distinct",
]


class MarketplaceValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "plugins" / "demo").mkdir(parents=True)
        (self.root / ".infowells" / "registry").mkdir(parents=True)
        self.write_json("marketplace.json", {
            "framework": "signal-infowells", "invariants": INVARIANTS,
            "plugins": [{"name": "demo", "source": "./plugins/demo"}],
        })
        (self.root / "plugins/demo/SKILL.md").write_text(
            "---\nname: demo\nframework: signal-infowells\nstatus: NOT-RUN\n---\n",
            encoding="utf-8",
        )
        self.write_json(".infowells/registry/run_registry.schema.json", {
            "properties": {"status": {"enum": ["CONFIRMED", "NOT-YET-VERIFIED", "NOT-RUN"]}}
        })

    def tearDown(self):
        self.temp.cleanup()

    def write_json(self, path, data):
        (self.root / path).write_text(json.dumps(data), encoding="utf-8")

    def test_valid_catalog_passes(self):
        self.assertEqual(validate_marketplace(self.root), [])

    def test_missing_skill_is_reported(self):
        (self.root / "plugins/demo/SKILL.md").unlink()
        self.assertTrue(any("missing capability directory or SKILL.md" in e
                            for e in validate_marketplace(self.root)))

    def test_mismatched_frontmatter_name_is_reported(self):
        (self.root / "plugins/demo/SKILL.md").write_text(
            "---\nname: other\nframework: signal-infowells\nstatus: NOT-RUN\n---\n",
            encoding="utf-8",
        )
        self.assertTrue(any("frontmatter name" in e for e in validate_marketplace(self.root)))

    def test_duplicate_name_is_reported(self):
        data = json.loads((self.root / "marketplace.json").read_text(encoding="utf-8"))
        data["plugins"].append({"name": "demo", "source": "./plugins/demo"})
        self.write_json("marketplace.json", data)
        self.assertTrue(any("duplicate name" in e for e in validate_marketplace(self.root)))

    def test_status_vocabulary_is_preserved(self):
        self.write_json(".infowells/registry/run_registry.schema.json", {
            "properties": {"status": {"enum": ["CONFIRMED", "NOT-YET-VERIFIED"]}}
        })
        self.assertTrue(any("status vocabulary" in e for e in validate_marketplace(self.root)))


if __name__ == "__main__":
    unittest.main()
