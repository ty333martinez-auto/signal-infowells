import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PILLARS = ("Perception", "Imagination", "Empathy", "Introspection", "Emotion", "Reason")


class PublicFrameworkDocsTests(unittest.TestCase):
    def test_canonical_guide_contains_six_reasoning_pillars(self):
        guide = (ROOT / "docs/reasoning-framework.md").read_text(encoding="utf-8")
        for pillar in PILLARS:
            with self.subTest(pillar=pillar):
                self.assertIn(f"**{pillar}**", guide)
        self.assertIn("Awareness", guide)
        self.assertIn("not a seventh pillar", guide)

    def test_public_page_teaches_six_pillars_and_recognition_uncertainty(self):
        docs = (ROOT / "docs/index.html").read_text(encoding="utf-8").lower()
        for phrase in ("perception", "imagination", "empathy", "introspection", "emotion", "reason",
                       "no single pillar", "what is actually here?", "what else is possible?",
                       "don't know yet", "recognition", "unresolved"):
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, docs)

    def test_public_page_distinguishes_marketplace_categories_from_pillars(self):
        docs = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        self.assertIn("Marketplace categories", docs)
        self.assertIn("not reasoning pillars", docs)
        self.assertIn("siw-autonomous-build", docs)
        self.assertIn("siw-capcut-intent", docs)
        self.assertIn(".pmcro/tasks/capcut/", docs)
        self.assertEqual(docs.count('class="plugin-card"'), 14)

    def test_canonical_framework_linked_from_readme_handoff_and_activation(self):
        for path in ("README.md", "HANDOFF.md", "ACTIVATION.md"):
            with self.subTest(path=path):
                content = (ROOT / path).read_text(encoding="utf-8")
                self.assertIn("docs/reasoning-framework.md", content)

    def test_promotion_boundary_is_preserved(self):
        activation = (ROOT / "ACTIVATION.md").read_text(encoding="utf-8").lower()
        handoff = (ROOT / "HANDOFF.md").read_text(encoding="utf-8").lower()
        docs = (ROOT / "docs/index.html").read_text(encoding="utf-8").lower()
        for text in (activation, handoff, docs):
            self.assertIn("independent validation", text)
            self.assertIn("not-yet-verified", text)
        self.assertIn("never auto-promote", activation)
        self.assertIn("never auto-promote", handoff)

    def test_canonical_guide_preserves_recognition_gap_and_baseline_harness(self):
        guide = (ROOT / "docs/reasoning-framework.md").read_text(encoding="utf-8")
        self.assertIn("Recognition Gap", guide)
        self.assertIn("HARNESS-TEST-007", guide)
        self.assertIn("Do not assume Run B is better", guide)


if __name__ == "__main__":
    unittest.main()
