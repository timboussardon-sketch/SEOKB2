"""Checks that the cloud report uses separate site totals and page rows."""

import datetime as dt
import importlib.util
from pathlib import Path
import unittest


spec = importlib.util.spec_from_file_location(
    "gsc_audit", Path(__file__).with_name("gsc_audit.py")
)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)


class GscAuditTest(unittest.TestCase):
    def test_forbidden_property_has_actionable_error(self):
        class Response:
            status_code = 403

        class Session:
            def post(self, url, json, timeout):
                return Response()

        with self.assertRaisesRegex(PermissionError, "utilisateur restreint"):
            audit.fetch(Session(), "sc-domain:organikk.co", "2026-09-24", "2026-10-21")

    def test_fetch_uses_read_only_search_analytics_request(self):
        class Response:
            def raise_for_status(self):
                pass

            def json(self):
                return {"rows": [{"clicks": 7, "impressions": 80}]}

        class Session:
            def __init__(self):
                self.calls = []

            def post(self, url, json, timeout):
                self.calls.append((url, json, timeout))
                return Response()

        session = Session()
        rows = audit.fetch(session, "sc-domain:organikk.co", "2026-09-24", "2026-10-21")
        self.assertEqual(rows[0]["clicks"], 7)
        url, body, timeout = session.calls[0]
        self.assertIn("sc-domain%3Aorganikk.co/searchAnalytics/query", url)
        self.assertEqual(body, {
            "startDate": "2026-09-24", "endDate": "2026-10-21", "type": "web"
        })
        self.assertEqual(timeout, 90)

    def test_periods_are_equal_length_and_do_not_overlap(self):
        start, end = audit.period(dt.date(2026, 10, 21), 28)
        previous_start, previous_end = audit.period(
            dt.date.fromisoformat(start) - dt.timedelta(days=1), 28
        )
        self.assertEqual((start, end), ("2026-09-24", "2026-10-21"))
        self.assertEqual((previous_start, previous_end), ("2026-08-27", "2026-09-23"))

    def test_site_totals_are_not_sum_of_page_rows(self):
        content = audit.report(
            "sc-domain:organikk.co", "2026-09-24", "2026-10-21",
            "2026-08-27", "2026-09-23",
            {"clicks": 100, "impressions": 2000},
            {"clicks": 120, "impressions": 1800},
            [{"keys": ["https://organikk.co/a"], "clicks": 3,
              "impressions": 110, "position": 7.2}],
            [{"keys": ["https://organikk.co/a"], "clicks": 9,
              "impressions": 90, "position": 9.1}],
        )
        self.assertIn("| Clics | 100 | 120 | -20 |", content)
        self.assertIn("| Impressions | 2000 | 1800 | +200 |", content)
        self.assertIn("| https://organikk.co/a | 3 | 9 | -6 | 110 | 7.2 |", content)
        self.assertIn("Ce tableau ne démontre aucune cause", content)

    def test_missing_page_row_is_not_reported_as_zero(self):
        content = audit.report(
            "sc-domain:organikk.co", "2026-09-24", "2026-10-21",
            "2026-08-27", "2026-09-23",
            {"clicks": 12, "impressions": 200},
            {"clicks": 10, "impressions": 150},
            [{"keys": ["https://organikk.co/new"], "clicks": 2,
              "impressions": 120, "position": 8.0}],
            [],
        )
        self.assertIn("| https://organikk.co/new | 2 | — | — | 120 | 8.0 |", content)


if __name__ == "__main__":
    unittest.main()
