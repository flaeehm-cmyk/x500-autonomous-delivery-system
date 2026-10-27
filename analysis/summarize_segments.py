#!/usr/bin/env python3
"""Summarize a derived flight-interval CSV; never connect to aircraft hardware."""
from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = ROOT / "data" / "flight_segment_summary_2026-10-10.csv"
FIELDS = (
    "index", "file", "flight", "armed_s", "airborne_s", "max_alt_m",
    "modes", "min_voltage", "max_vib_xyz", "clip_0_delta",
)


@dataclass(frozen=True)
class Segment:
    index: int
    source: str
    date: str
    interval: int
    armed_s: float
    airborne_s: float
    max_alt_m: float
    modes: tuple[int, ...]
    min_voltage: float
    max_vib_xyz: float
    clip_0_delta: int


def nonnegative_int(value: str, field: str) -> int:
    if not re.fullmatch(r"[0-9]+", value.strip()):
        raise ValueError(f"{field} must be a nonnegative integer")
    return int(value)


def finite_number(value: str, field: str, *, nonnegative: bool = True) -> float:
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{field} must be finite")
    if nonnegative and result < 0:
        raise ValueError(f"{field} must be nonnegative")
    return result


def load_segments(path: Path) -> list[Segment]:
    segments: list[Segment] = []
    seen_ids: set[tuple[str, int]] = set()
    seen_indexes: set[int] = set()
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != list(FIELDS):
            raise ValueError("CSV columns must match the documented schema: " + ",".join(FIELDS))
        for line, row in enumerate(reader, start=2):
            try:
                if None in row or any(value is None or not value.strip() for value in row.values()):
                    raise ValueError("row has missing or extra fields")
                source = row["file"].strip()
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2}\.bin", source):
                    raise ValueError("file must have format YYYY-MM-DD HH-MM-SS.bin")
                date = datetime.strptime(source, "%Y-%m-%d %H-%M-%S.bin").date().isoformat()
                index = nonnegative_int(row["index"], "index")
                interval = nonnegative_int(row["flight"], "flight")
                if interval < 1:
                    raise ValueError("flight interval ID must be at least 1")
                key = (source, interval)
                if key in seen_ids or index in seen_indexes:
                    raise ValueError("duplicate interval or row index")
                armed = finite_number(row["armed_s"], "armed_s")
                airborne = finite_number(row["airborne_s"], "airborne_s")
                if airborne > armed + 1e-6:
                    raise ValueError("airborne_s cannot exceed armed_s")
                mode_text = row["modes"].strip()
                if not re.fullmatch(r"[0-9]+(?:/[0-9]+)*", mode_text):
                    raise ValueError("modes must be slash-separated integer IDs")
                modes = tuple(int(value) for value in mode_text.split("/"))
                segment = Segment(
                    index=index, source=source, date=date, interval=interval,
                    armed_s=armed, airborne_s=airborne,
                    max_alt_m=finite_number(row["max_alt_m"], "max_alt_m", nonnegative=False),
                    modes=modes,
                    min_voltage=finite_number(row["min_voltage"], "min_voltage"),
                    max_vib_xyz=finite_number(row["max_vib_xyz"], "max_vib_xyz"),
                    clip_0_delta=nonnegative_int(row["clip_0_delta"], "clip_0_delta"),
                )
                seen_ids.add(key)
                seen_indexes.add(index)
                segments.append(segment)
            except (ValueError, TypeError) as exc:
                raise ValueError(f"{path.name}: line {line}: {exc}") from exc
    if not segments:
        raise ValueError("CSV contains no data rows")
    return segments


def aggregate(segments: list[Segment]) -> dict:
    if not segments:
        raise ValueError("cannot summarize an empty dataset")
    groups = []
    for date in sorted({item.date for item in segments}):
        rows = [item for item in segments if item.date == date]
        qualifying = [item for item in rows if item.airborne_s > 0]
        groups.append({
            "date": date,
            "source_logs": len({item.source for item in rows}),
            "armed_intervals": len(rows),
            "intervals_with_inferred_airborne_time": len(qualifying),
            "airborne_intervals_with_auto_in_mode_set": sum(3 in item.modes for item in qualifying),
            "summed_inferred_airborne_s": round(math.fsum(item.airborne_s for item in rows), 6),
            "max_vibration_across_armed_intervals_m_s2": max(item.max_vib_xyz for item in rows),
            "min_voltage_across_armed_intervals_v": min(item.min_voltage for item in rows),
            "clipping_delta_across_armed_intervals": sum(item.clip_0_delta for item in rows),
        })
    qualifying = [item for item in segments if item.airborne_s > 0]
    return {
        "armed_intervals": len(segments),
        "source_logs": len({item.source for item in segments}),
        "dates": len(groups),
        "intervals_with_inferred_airborne_time": len(qualifying),
        "airborne_intervals_with_auto_in_mode_set": sum(3 in item.modes for item in qualifying),
        "summed_inferred_airborne_s": round(math.fsum(item.airborne_s for item in segments), 6),
        "clipping_delta_in_intervals_with_airborne_time": sum(item.clip_0_delta for item in qualifying),
        "clipping_delta_in_other_intervals": sum(item.clip_0_delta for item in segments if item.airborne_s == 0),
        "by_date": groups,
    }


def report_markdown(summary: dict, source_name: str, source_sha256: str) -> str:
    lines = [
        "# Historical flight-summary analysis", "",
        "Generated by the repository's offline analysis script from a derived CSV.",
        "Read the data dictionary and evidence register before interpreting these aggregates.", "",
        f"Source: {source_name}",
        f"SHA-256 of the included CSV: {source_sha256}", "",
        "## Dataset", "",
        "| Metric | Value |", "| --- | ---: |",
        f"| Armed intervals | {summary['armed_intervals']} |",
        f"| Source logs | {summary['source_logs']} |",
        f"| Dates represented | {summary['dates']} |",
        f"| Intervals with inferred airborne time | {summary['intervals_with_inferred_airborne_time']} |",
        f"| Such intervals with AUTO in their mode set | {summary['airborne_intervals_with_auto_in_mode_set']} |",
        f"| Summed inferred airborne time (s) | {summary['summed_inferred_airborne_s']:.1f} |",
        "",
        "Summed time spans multiple intervals and dates. It is not one-flight or one-charge endurance.",
        "AUTO in a mode set does not establish the duration in AUTO or mission completion.", "",
        "## By source date", "",
        "| Date | Logs | Armed intervals | With airborne time | With airborne time and AUTO in mode set | Summed airborne time (s) |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in summary["by_date"]:
        lines.append(
            f"| {item['date']} | {item['source_logs']} | {item['armed_intervals']} | "
            f"{item['intervals_with_inferred_airborne_time']} | "
            f"{item['airborne_intervals_with_auto_in_mode_set']} | "
            f"{item['summed_inferred_airborne_s']:.1f} |"
        )
    lines += [
        "", "## Armed-interval extrema", "",
        "These extrema are from whole armed intervals, not necessarily airborne portions.", "",
        "| Date | Minimum recorded pack voltage (V) | Maximum summarized vibration (m/s²) | Clipping-counter increase |",
        "| --- | ---: | ---: | ---: |",
    ]
    for item in summary["by_date"]:
        lines.append(
            f"| {item['date']} | {item['min_voltage_across_armed_intervals_v']:.2f} | "
            f"{item['max_vibration_across_armed_intervals_m_s2']:.1f} | "
            f"{item['clipping_delta_across_armed_intervals']} |"
        )
    lines += [
        "",
        f"Clipping-counter increase in intervals with inferred airborne time: {summary['clipping_delta_in_intervals_with_airborne_time']}.",
        f"Clipping-counter increase in the other intervals: {summary['clipping_delta_in_other_intervals']}.",
        "The summary cannot localize any event within an interval.", "",
        "## Limits", "",
        "- Airborne time follows the earlier extraction's relative-altitude-above-2-m heuristic.",
        "- Raw logs and their original extraction code are not included.",
        "- Current, energy, payload mass, battery state, weather, and path-error time series are absent.",
        "- Extrema and aggregates do not establish flight readiness or a safe operating envelope.",
        "- The 19 October flights are not part of this dataset.", "",
    ]
    return "\n".join(lines)


def make_outputs(path: Path) -> dict[str, str]:
    summary = aggregate(load_segments(path))
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    payload = {
        "schema_version": 1,
        "source_file": path.name,
        "source_sha256": digest,
        "method": "Aggregate the supplied derived armed-interval CSV; no raw-log reprocessing.",
        "summary": summary,
    }
    return {
        "results.md": report_markdown(summary, path.name, digest),
        "results.json": json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV, help="CSV using the documented schema")
    parser.add_argument("--output-dir", type=Path, default=ROOT / "analysis")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="write deterministic Markdown and JSON reports")
    mode.add_argument("--check", action="store_true", help="fail if saved reports do not match the input")
    args = parser.parse_args(argv)
    try:
        outputs = make_outputs(args.csv)
        if args.write:
            args.output_dir.mkdir(parents=True, exist_ok=True)
            for name, content in outputs.items():
                (args.output_dir / name).write_text(content, encoding="utf-8")
            print("Wrote results.md and results.json")
        elif args.check:
            stale = []
            for name, expected in outputs.items():
                path = args.output_dir / name
                if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                    stale.append(name)
            if stale:
                print("Missing or stale generated report(s): " + ", ".join(stale), file=sys.stderr)
                return 1
            print("Generated reports match the CSV.")
        else:
            print(outputs["results.md"], end="")
        return 0
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
