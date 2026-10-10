import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PublicFrameworkDocsTests(unittest.TestCase):
    def test_public_guide_teaches_six_reasoning_pillars(self):
        docs = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        for pillar in ("Perception", "Imagination", "Empathy", "Introspection", "Emotion", "Reason"):
            with self.subTest(pillar=pillar):
                self.assertIn(pillar, docs)

    def test_public_guide_distinguishes_core_and_marketplace(self):
        docs = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        self.assertIn("No single pillar", docs)
        self.assertIn("Recognition remains continuous", docs)
        self.assertIn("siw-capcut-intent", docs)
        self.assertIn(".pmcro/tasks/capcut/", docs)

    def test_activation_and_handoff_reference_learning_docs(self):
        activation = (ROOT / "ACTIVATION.md").read_text(encoding="utf-8")
        handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8")
        self.assertIn("docs/index.html", activation)
        self.assertIn("Public documentation and learning", handoff)


if __name__ == "__main__":
    unittest.main()
