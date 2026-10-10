import unittest
from pathlib import Path

from src.signal_infowells.marketplace import load_marketplace, MarketplaceError


ROOT = Path(__file__).resolve().parents[1]


class MarketplaceLoaderTests(unittest.TestCase):
    def test_loads_all_catalogued_capabilities(self):
        marketplace = load_marketplace(ROOT)
        self.assertEqual(marketplace.framework, "signal-infowells")
        self.assertEqual(len(marketplace.capabilities), 14)
        self.assertIn("siw-autonomous-build", {item.name for item in marketplace.capabilities})
        self.assertIn("siw-capcut-intent", {item.name for item in marketplace.capabilities})

    def test_exposes_required_invariants(self):
        marketplace = load_marketplace(ROOT)
        self.assertIn("no_single_pillar_defines_reality", marketplace.invariants)
        self.assertIn("recognition_continuous_unresolved", marketplace.invariants)


if __name__ == "__main__":
    unittest.main()
