import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("analizar_caso", ROOT / "analizar_caso.py")
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AnalyzeCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = json.loads((ROOT / "data" / "caso.json").read_text(encoding="utf-8"))
        cls.results = MODULE.analyze(cls.case)
        cls.by_classification = {item["classification"]: item for item in cls.results}

    def test_case_is_explicitly_fictional(self):
        self.assertTrue(self.case["all_entities_are_fictional"])

    def test_connection_and_authorization_are_distinguished(self):
        connection = next(e for e in self.case["timeline"] if e["type"] == "wallet_connection")
        self.assertFalse(connection["state_change"])
        self.assertIn("malicious-contract-authorization", self.by_classification)

    def test_drainer_requires_linked_approval_and_transfer(self):
        finding = self.by_classification["wallet-drainer"]
        self.assertEqual(finding["evidence"], ["evt-008", "evt-009"])

    def test_rug_pull_is_a_separate_case(self):
        self.assertFalse(self.case["liquidity_case"]["same_campaign_as_lv_001"])
        self.assertIn("rug-pull-scenario", self.by_classification)

    def test_requested_case_taxonomy_is_covered(self):
        expected = {
            "fake-token", "fake-website", "impersonation", "suspected-account-takeover",
            "fake-airdrop/fake-influencer/social-engineering/phishing", "seed-phrase-theft",
            "malicious-contract-authorization", "wallet-drainer", "clipboard-attack",
            "rug-pull-scenario",
        }
        self.assertEqual(expected, set(self.by_classification))


if __name__ == "__main__":
    unittest.main()
