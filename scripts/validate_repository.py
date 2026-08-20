#!/usr/bin/env python3
"""Validate the historical MIBO Pilot reports and Paper B evidence freeze."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "paper-b" / "evidence-manifest.json"
HASH_PATH = ROOT / "paper-b" / "SHA256SUMS.json"
EXPECTED_DATES = [
    "2026-05-05",
    "2026-05-12",
    "2026-05-19",
    "2026-05-26",
    "2026-06-02",
    "2026-06-09",
    "2026-06-16",
    "2026-06-23",
    "2026-06-30",
    "2026-07-07",
    "2026-07-14",
    "2026-07-21",
    "2026-07-28",
]
EXPECTED_QUERY_IDS = {
    1: ["q001", "q002", "q003"],
    2: ["q001", "q002", "q003"],
    **{day: ["q001", "q002", "q003", "q004", "q005"] for day in range(3, 14)},
}
ACTIVE_PROVENANCE_FILES = [
    "README.md",
    "INDEX.md",
    "AUTOMATION.md",
    "2026-08-04-observation.md",
    "scripts/observation_config.json",
    "scripts/render_observation.py",
]
PROVENANCE_FACT = (
    "MIBO Pilot collection has been API-based continuously since Day 1 (2026-05-05). "
    "Do not describe any later observation as the first API observation or as a transition "
    "from web/manual collection to API collection."
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def report_query_ids(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    ids = re.findall(r"^## q(00[1-5])\b", text, flags=re.MULTILINE)
    return [f"q{value}" for value in ids]


def release_files(manifest: dict[str, Any]) -> list[str]:
    paths = {
        "paper-b/README.md",
        "paper-b/evidence-manifest.json",
        "paper-b/provenance-matrix.csv",
    }
    for entry in manifest["included_days"]:
        paths.add(entry["report"])
        paths.update(entry.get("additional_source_files", []))
    return sorted(paths)


def sha256_file(path: Path) -> str:
    # All release files are text. Normalize Windows checkout line endings to the LF form
    # stored in Git so the manifest verifies identically on Windows and GitHub Actions.
    content = path.read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(content).hexdigest()


def write_hash_manifest(manifest: dict[str, Any]) -> None:
    files = release_files(manifest)
    payload = {
        "algorithm": "SHA-256",
        "hashing_rule": "SHA-256 of each identified text file after CRLF-to-LF normalization (the canonical Git text representation); paths are repository-relative POSIX paths; SHA256SUMS.json does not hash itself",
        "files": [
            {"path": rel, "sha256": sha256_file(ROOT / rel)}
            for rel in files
        ],
    }
    HASH_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"WROTE: {HASH_PATH.relative_to(ROOT).as_posix()} ({len(files)} files)")


def validate_hashes(manifest: dict[str, Any]) -> None:
    hashes = load_json(HASH_PATH)
    require(hashes.get("algorithm") == "SHA-256", "hash manifest algorithm must be SHA-256")
    entries = hashes.get("files")
    require(isinstance(entries, list), "hash manifest files must be a list")
    expected_paths = release_files(manifest)
    actual_paths = [entry.get("path") for entry in entries]
    require(actual_paths == expected_paths, "hash manifest file list is incomplete, extra, or unsorted")
    require(len(actual_paths) == len(set(actual_paths)), "hash manifest contains duplicate paths")
    for entry in entries:
        path = ROOT / entry["path"]
        require(path.is_file(), f"hashed file does not exist: {entry['path']}")
        require(sha256_file(path) == entry.get("sha256"), f"hash mismatch: {entry['path']}")


def validate_json_and_csv() -> None:
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" not in path.parts:
            load_json(path)
    for path in sorted(ROOT.rglob("*.csv")):
        if ".git" in path.parts:
            continue
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))
        require(bool(rows), f"CSV has no header: {path.relative_to(ROOT)}")
        width = len(rows[0])
        require(width > 0, f"CSV has an empty header: {path.relative_to(ROOT)}")
        require(
            all(len(row) == width for row in rows[1:]),
            f"CSV has inconsistent row widths: {path.relative_to(ROOT)}",
        )


def validate_manifest(manifest: dict[str, Any]) -> None:
    included = manifest.get("included_days")
    require(isinstance(included, list), "included_days must be a list")
    days = [entry.get("day") for entry in included]
    dates = [entry.get("date") for entry in included]
    counts = [entry.get("expected_included_observations") for entry in included]

    require(days == list(range(1, 14)), "Paper B included Day range must be exactly Day 1–Day 13")
    require(dates == EXPECTED_DATES, "Paper B dates must be chronological and match Day 1–Day 13")
    require(len(days) == len(set(days)), "duplicate official Observation Day ID")
    require(len(dates) == len(set(dates)), "duplicate official observation date")
    require(counts == [12, 12] + [20] * 11, "per-Day expected counts do not match the Pilot schedule")
    require(sum(counts) == 244, "Paper B expected count must sum to 244")
    require(manifest.get("total_included_observations") == 244, "manifest total must be 244")
    require(manifest.get("api_collection_since") == "2026-05-05", "API-since date must be 2026-05-05")
    require(manifest.get("collection_mode") == "api", "collection mode must be api")

    later = manifest.get("excluded_later_pilot_observations", [])
    require(all(entry.get("day", 0) > 13 for entry in later), "a later Day was included in the Paper B boundary")
    require({entry.get("day") for entry in later} == {14, 15}, "Days 14–15 must be explicitly excluded as later Pilot observations")

    schedule = manifest.get("query_schedule")
    require(isinstance(schedule, list) and len(schedule) == 2, "manifest query schedule must contain two periods")
    schedule_by_day: dict[int, list[str]] = {}
    for period in schedule:
        for day in period["days"]:
            schedule_by_day[day] = period["query_ids"]
    require(schedule_by_day == EXPECTED_QUERY_IDS, "manifest query IDs do not match the documented Day schedule")

    root_reports = sorted(path.name for path in ROOT.glob("????-??-??-observation.md"))
    require(len(root_reports) == len(set(root_reports)), "duplicate root observation filenames")
    # Paper B freezes Days 1-13; later Pilot observation days (14, 15, 16, ...) are added by the
    # weekly automation and grow over time, so require a floor rather than an exact count. The
    # frozen Day 1-13 reports are each verified individually in the manifest loop above, and the
    # release hash manifest guarantees their contents, so ongoing days cannot weaken Paper B.
    require(len(root_reports) >= 15, "expected at least the 15 known official root observation reports")

    for entry in included:
        report = ROOT / entry["report"]
        require(report.is_file(), f"manifest report does not exist: {entry['report']}")
        text = report.read_text(encoding="utf-8")
        require(entry["date"] in text, f"report does not state its observation date: {entry['report']}")
        require(
            report_query_ids(report) == EXPECTED_QUERY_IDS[entry["day"]],
            f"report query headings do not match Day schedule: {entry['report']}",
        )
        count_match = re.search(
            r"\*\*(?:Total observations(?: this session)?|Included observations this session)\*\*:\s*(\d+)",
            text,
        )
        require(count_match is not None, f"could not read included count from {entry['report']}")
        require(
            int(count_match.group(1)) == entry["expected_included_observations"],
            f"report count differs from manifest: {entry['report']}",
        )
        for rel in entry.get("additional_source_files", []):
            require((ROOT / rel).is_file(), f"manifest source file does not exist: {rel}")

    grok = manifest.get("excluded_systems", [])
    require(
        any(entry.get("system") == "Grok" and entry.get("days") == list(range(7, 14)) for entry in grok),
        "Grok exclusion for Day 7–Day 13 is missing",
    )


def validate_latest_pilot() -> None:
    responses = load_json(ROOT / "2026-08-11" / "responses.json")
    results = responses.get("results")
    require(responses.get("day") == 15, "latest structured packet must be Day 15")
    require(responses.get("date") == "2026-08-11", "latest structured packet date mismatch")
    require(isinstance(results, list) and len(results) == 20, "Day 15 must contain 20 response records")
    require(all(result.get("status") == "ok" for result in results), "Day 15 contains a non-success response")
    keys = [(result.get("query_id"), result.get("system")) for result in results]
    require(len(keys) == len(set(keys)), "Day 15 contains duplicate system–query observation IDs")


def validate_active_provenance() -> None:
    config = load_json(ROOT / "scripts" / "observation_config.json")
    require(config.get("immutable_historical_fact") == PROVENANCE_FACT, "generator provenance guardrail is missing or changed")
    guardrail = config.get("prospective_coding_guardrail", "").lower()
    require("do not infer or code gender from names or appearance" in guardrail, "prospective gender-inference guardrail is missing")

    banned = (
        "first api-collected session",
        "first api observation",
        "web-to-api transition",
        "web → api",
        "web->api",
        "interface-to-api transition",
        "manual phase followed by api phase",
    )
    contextual_markers = (
        "correction",
        "incorrect",
        "do not describe",
        "must not describe",
        "there was no",
        "no web-to-api",
    )
    for rel in ACTIVE_PROVENANCE_FILES:
        for number, line in enumerate((ROOT / rel).read_text(encoding="utf-8").splitlines(), 1):
            lower = line.lower()
            if any(term in lower for term in banned) and not any(marker in lower for marker in contextual_markers):
                raise ValueError(f"active false API-transition claim: {rel}:{number}")

    day14 = (ROOT / "2026-08-04-observation.md").read_text(encoding="utf-8")
    require("Correction — 14 August 2026" in day14, "Day 14 corrigendum is missing")
    require("<!-- mibo:manual -->" in day14, "Day 14 corrigendum is not protected from automated re-rendering")
    require("Day 14 continues the API-based MIBO Pilot sequence" in day14, "Day 14 active provenance prose is not corrected")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-hashes", action="store_true", help="regenerate paper-b/SHA256SUMS.json after intentional evidence-file changes")
    args = parser.parse_args()

    validate_json_and_csv()
    manifest = load_json(MANIFEST_PATH)
    validate_manifest(manifest)
    validate_latest_pilot()
    validate_active_provenance()
    if args.write_hashes:
        write_hash_manifest(manifest)
    else:
        validate_hashes(manifest)

    print("PASS: all JSON parses and all CSV files are structurally readable")
    print("PASS: official observation dates and Day IDs are unique and chronological")
    print("PASS: Paper B includes exactly Day 1–Day 13 and recomputes to 244")
    print("PASS: query schedules, source paths, Grok exclusion, and latest Day 15 packet")
    print("PASS: API-since-Day-1 and prospective gender-inference guardrails")
    print("PASS: Paper B SHA-256 manifest")


if __name__ == "__main__":
    main()
