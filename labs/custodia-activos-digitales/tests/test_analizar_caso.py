from decimal import Decimal
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import unittest


LAB = Path(__file__).resolve().parents[1]
SPEC = spec_from_file_location("analizar_caso", LAB / "analizar_caso.py")
assert SPEC and SPEC.loader
MODULE = module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ReconciliationTest(unittest.TestCase):
    def setUp(self):
        self.result = MODULE.findings(LAB / "data")

    def test_btc_gap_is_reproducible(self):
        btc = next(item for item in self.result["reconciliation"] if item["asset"] == "BTC")
        self.assertEqual(btc["ledger"], Decimal("12.50000000"))
        self.assertEqual(btc["chain"], Decimal("11.80000000"))
        self.assertEqual(btc["difference"], Decimal("0.70000000"))

    def test_eth_reconciles(self):
        eth = next(item for item in self.result["reconciliation"] if item["asset"] == "ETH")
        self.assertEqual(eth["difference"], Decimal("0E-8"))

    def test_control_breaks_are_linked_to_req_002(self):
        self.assertEqual(self.result["executed_without_approval"], ["req-002"])
        self.assertEqual(self.result["executed_without_ledger"], ["req-002"])
        self.assertEqual(self.result["critical_open_alerts"], ["alert-001", "alert-002"])


if __name__ == "__main__":
    unittest.main()
