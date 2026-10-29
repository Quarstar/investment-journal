"""Tests for the deterministic parts of the weekly agent. Run: python -m unittest discover agent/tests"""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "agent"))

import guard  # noqa: E402
import prices  # noqa: E402
from run_agent import review_date  # noqa: E402


class TestGuard(unittest.TestCase):
    def test_writes_only_in_drafts(self):
        self.assertIsNone(guard.check_write("weekly-reviews/drafts/2026-11-04.md"))
        self.assertIsNone(guard.check_write(str(ROOT / "weekly-reviews/drafts/2026-11-04.md")))
        self.assertIsNotNone(guard.check_write("weekly-reviews/2026-11-04.md"))
        self.assertIsNotNone(guard.check_write("plans/target-portfolio.md"))
        self.assertIsNotNone(guard.check_write("weekly-reviews/drafts/../../README.md"))
        self.assertIsNotNone(guard.check_write("weekly-reviews/drafts/x.py"))

    def test_private_is_off_limits(self):
        self.assertIsNotNone(guard.check_read("private/holdings_2026-10-28.csv"))
        self.assertIsNotNone(guard.check_tool("Grep", {"path": "private"}))
        self.assertIsNone(guard.check_read("weekly-reviews/_checklist.md"))

    def test_blocked_urls(self):
        self.assertIsNotNone(guard.check_url("https://api.stockanalysis.com/api/symbol/s/nvda"))
        self.assertIsNotNone(guard.check_url("https://stockanalysis.com/stocks/rtx/history/"))
        self.assertIsNone(guard.check_url("https://stockanalysis.com/stocks/nvda/"))

    def test_no_shell(self):
        self.assertIsNotNone(guard.check_tool("Bash", {"command": "ls"}))

    def test_validator(self):
        self.assertEqual(guard.validate_text("NVDA $217.94, weight 11.4%. VUKG £57.62."), [])
        self.assertTrue(guard.validate_text("Cash shield £1,686"))
        self.assertTrue(guard.validate_text("contact me at someone@example.com"))
        self.assertTrue(guard.validate_text("NI QQ123456C"))
        self.assertTrue(guard.validate_text("see private/holdings.csv"))
        self.assertEqual(guard.validate_text("dates like 2026-10-28 are fine"), [])


class TestPrices(unittest.TestCase):
    def test_parse_yahoo(self):
        payload = json.dumps({"chart": {"result": [{
            "meta": {"currency": "USD", "exchangeName": "NMS", "gmtoffset": -14400},
            "timestamp": [1793021400, 1793107800],  # 26 and 27 Oct 2026, 13:30 UTC opens
            "indicators": {"quote": [{"open": [213.11, 218.31], "high": [217.75, 218.5],
                                      "low": [212.61, 215.53], "close": [216.0, None],
                                      "volume": [90829293, None]}]}}]}}).encode()
        rows, meta = prices.parse_yahoo(payload)
        self.assertEqual(meta["currency"], "USD")
        self.assertEqual(len(rows), 1)  # the bar with no close is dropped
        self.assertEqual(rows[0]["date"], "2026-10-26")
        self.assertEqual(rows[0]["close"], "216.00")

    def test_parse_twelvedata(self):
        payload = json.dumps({"status": "ok", "values": [
            {"datetime": "2026-10-28", "open": "1", "high": "1", "low": "1", "close": "215.38", "volume": "1"},
            {"datetime": "2026-10-27", "open": "1", "high": "1", "low": "1", "close": "217.94", "volume": "1"}]}).encode()
        self.assertEqual(prices.parse_twelvedata(payload),
                         [{"date": "2026-10-27", "close": "217.94"}, {"date": "2026-10-28", "close": "215.38"}])
        self.assertEqual(prices.parse_twelvedata(b'{"status": "error", "code": 401}'), [])

    def test_merge_never_overwrites(self):
        existing = [{"date": "2026-10-26", "close": "216.00"}]
        new = [{"date": "2026-10-26", "close": "999.00"}, {"date": "2026-10-27", "close": "217.94"}]
        rows, added = prices.merge(existing, new)
        self.assertEqual(added, ["2026-10-27"])
        self.assertEqual(rows[0]["date"], "2026-10-27")
        self.assertEqual(rows[1]["close"], "216.00")

    def test_cross_check(self):
        self.assertEqual(prices.cross_check(100.0, 100.3, 0.5)[0], "verified")
        self.assertEqual(prices.cross_check(100.0, 101.0, 0.5)[0], "unverified")
        self.assertEqual(prices.cross_check(100.0, None, 0.5)[0], "single source")


class TestDates(unittest.TestCase):
    def test_review_is_the_wednesday_after(self):
        self.assertEqual(review_date("2026-10-27"), "2026-10-28")  # Tuesday close -> Wednesday
        self.assertEqual(review_date("2026-10-30"), "2026-11-04")  # a Friday close -> next Wednesday


if __name__ == "__main__":
    unittest.main()
