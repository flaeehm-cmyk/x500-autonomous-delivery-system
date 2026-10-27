"""Tests for trustworthy summary boundaries; synthetic rows are test fixtures only."""
import csv
import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("summarize_segments", ROOT / "analysis" / "summarize_segments.py")
module = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = module
SPEC.loader.exec_module(module)


class SummaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "fixture.csv"

    def row(self, **changes):
        result = dict(zip(module.FIELDS, [
            "0", "2026-10-01 10-00-00.bin", "1", "20", "10", "5",
            "2/6", "15.5", "12", "0",
        ]))
        result.update({key: str(value) for key, value in changes.items()})
        return result

    def write(self, rows):
        with self.path.open("w", newline="", encoding="utf-8") as stream:
            writer = csv.DictWriter(stream, fieldnames=module.FIELDS)
            writer.writeheader()
            writer.writerows(rows)
        return self.path

    def test_ground_auto_is_not_an_airborne_auto_interval(self):
        path = self.write([
            self.row(index=0, flight=1, airborne_s=0, modes="3", clip_0_delta=4),
            self.row(index=1, flight=2, airborne_s=8, modes="2/3/6"),
            self.row(index=2, flight=3, airborne_s=12, modes="13/6"),
        ])
        summary = module.aggregate(module.load_segments(path))
        self.assertEqual(summary["armed_intervals"], 3)
        self.assertEqual(summary["intervals_with_inferred_airborne_time"], 2)
        self.assertEqual(summary["airborne_intervals_with_auto_in_mode_set"], 1)
        self.assertEqual(summary["summed_inferred_airborne_s"], 20)
        self.assertEqual(summary["clipping_delta_in_other_intervals"], 4)
        self.assertEqual(summary["clipping_delta_in_intervals_with_airborne_time"], 0)

    def test_nonfinite_values_are_rejected(self):
        for value in ("nan", "inf", "-inf"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    module.load_segments(self.write([self.row(min_voltage=value)]))

    def test_impossible_duration_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "cannot exceed"):
            module.load_segments(self.write([self.row(airborne_s=21)]))

    def test_duplicate_interval_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            module.load_segments(self.write([self.row(), self.row(index=1)]))

    def test_missing_schema_is_rejected(self):
        self.path.write_text("flight,armed_s\n1,20\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "columns"):
            module.load_segments(self.path)

    def test_empty_dataset_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "no data"):
            module.load_segments(self.write([]))

    def test_invalid_modes_and_dates_are_rejected(self):
        for change in ({"modes": "3//6"}, {"file": "2026-02-30 10-00-00.bin"}):
            with self.subTest(change=change):
                with self.assertRaises(ValueError):
                    module.load_segments(self.write([self.row(**change)]))

    def test_negative_relative_ground_altitude_is_valid(self):
        rows = module.load_segments(self.write([self.row(airborne_s=0, max_alt_m=-0.5)]))
        self.assertEqual(rows[0].max_alt_m, -0.5)

    def test_included_dataset_regression(self):
        summary = module.aggregate(module.load_segments(module.DEFAULT_CSV))
        self.assertEqual(summary["armed_intervals"], 30)
        self.assertEqual(summary["source_logs"], 4)
        self.assertEqual(summary["intervals_with_inferred_airborne_time"], 16)
        self.assertEqual(summary["airborne_intervals_with_auto_in_mode_set"], 7)
        self.assertAlmostEqual(summary["summed_inferred_airborne_s"], 1239.6)
        self.assertEqual(summary["clipping_delta_in_other_intervals"], 11)

    def test_generated_reports_match_the_source(self):
        for name, content in module.make_outputs(module.DEFAULT_CSV).items():
            self.assertEqual((ROOT / "analysis" / name).read_text(encoding="utf-8"), content)


if __name__ == "__main__":
    unittest.main()
