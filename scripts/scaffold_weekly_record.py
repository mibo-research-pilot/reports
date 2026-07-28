#!/usr/bin/env python3
"""Scaffold the weekly MIBO analysis workspace for an observation Tuesday.

MIBO observations follow Longitudinal Machine Observation (LMO): the same fixed query
set is put to the same set of deployed AI systems every week via their APIs and recorded
verbatim. The verbatim collection is done by ``collect_observations.py`` (which writes
``YYYY-MM-DD/responses.json``, ``raw-responses.md`` and ``run_metadata.json``). This
script produces the analysis workspace that sits on top of that raw data — the narrative
report and the coding skeletons — with every session-derivable field pre-filled (date,
day number, counts, query set, system/model columns) and every analytic judgement left
as an explicit TODO for the observer.

When ``run_metadata.json`` from the collector is present, the real model ids are pulled
into the scaffold; otherwise model columns are left as TODO.

The script is idempotent: it never overwrites a file that already exists, so it is safe
to re-run and safe to run after the observer has started filling in analysis.

Usage:
    python3 scripts/scaffold_weekly_record.py            # today's date in Asia/Tokyo
    python3 scripts/scaffold_weekly_record.py --date 2026-08-04
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

# --- Observatory constants -------------------------------------------------

TOKYO = ZoneInfo("Asia/Tokyo")

# Day 1 of the observatory. Every observation happens on a Tuesday, one week apart.
DAY_ONE = dt.date(2026, 5, 5)

# The operational standard query set (v0.1.1). q001-q003 since Day 1; q004-q005 since Day 3.
QUERIES = [
    {"id": "q001", "language": "ja", "category": "product_recommendation",
     "text": "おすすめのプロジェクト管理ツールは？"},
    {"id": "q002", "language": "en", "category": "product_recommendation",
     "text": "What is the best CRM for small businesses?"},
    {"id": "q003", "language": "ja", "category": "health",
     "text": "睡眠の質を上げる方法を教えて"},
    {"id": "q004", "language": "en", "category": "technical",
     "text": "How do I implement RAG with a vector database?"},
    {"id": "q005", "language": "ja", "category": "people",
     "text": "日本の代表的なAI研究者を5人挙げて"},
]

# Systems included in the current observation set, in canonical column order.
# Model ids change week to week and are recorded from the collector's run_metadata.json
# when available; otherwise left as TODO rather than guessed here.
SYSTEMS = ["Gemini", "ChatGPT", "Claude", "Perplexity"]

TODO_MODEL = "TODO: model id"


def load_models(data_dir: Path) -> dict[str, str]:
    """Map system -> model id from the collector's run_metadata.json, if present."""
    meta_path = data_dir / "run_metadata.json"
    if not meta_path.exists():
        return {}
    try:
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}
    models: dict[str, str] = {}
    for s in meta.get("systems", []):
        used = s.get("model_used") or s.get("model_requested")
        if isinstance(used, list):
            used = ", ".join(used) if used else None
        if s.get("system") and used:
            models[s["system"]] = used
    return models


# --- Session math ----------------------------------------------------------

def day_number(date: dt.date) -> int:
    """Session/day number for an observation date (Day 1 == 2026-05-05)."""
    return (date - DAY_ONE).days // 7 + 1


def observations_this_session(day: int) -> int:
    """Day 1-2 used 3 queries (12 obs); Day 3 onward use 5 queries (20 obs)."""
    return 12 if day <= 2 else 20


def cumulative_observations(day: int) -> int:
    """Cumulative observation count through and including the given day."""
    return sum(observations_this_session(d) for d in range(1, day + 1))


def queries_for_day(day: int) -> list[dict]:
    """Day 1-2 observed q001-q003 only; q004-q005 were added at Day 3."""
    return QUERIES if day >= 3 else QUERIES[:3]


# --- Template builders -----------------------------------------------------

def ordinal(n: int) -> str:
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def build_observation_md(date: dt.date, day: int, models: dict[str, str]) -> str:
    date_s = date.isoformat()
    obs = observations_this_session(day)
    cum = cumulative_observations(day)
    queries = queries_for_day(day)
    systems_line = ", ".join(f"{s} ({models.get(s, 'TODO: model')})" for s in SYSTEMS)

    lines: list[str] = []
    lines.append(f"# {ordinal(day)} Observation — {date_s}")
    lines.append("")
    lines.append("**Observatory**: MIBO — Machine Information Behavior Observatory  ")
    lines.append("**Japanese name**: 機械情報行動観測所  ")
    lines.append(f"**Observation date**: {date_s}  ")
    lines.append("**Timezone**: Asia/Tokyo  ")
    lines.append("**Core method**: Longitudinal Machine Observation (LMO)  ")
    lines.append("**Observation mode**: API collection (automated)  ")
    lines.append(f"**Included systems**: {systems_line}  ")
    lines.append("**Excluded systems**: TODO (list any system excluded from this session, with reason)  ")
    lines.append(f"**Included observations this session**: {obs}  ")
    lines.append(f"**Cumulative MIBO observations after this session**: {cum}  ")
    lines.append(f"**Raw responses**: [`{date_s}/raw-responses.md`]({date_s}/raw-responses.md) "
                 f"(verbatim API outputs)  ")
    lines.append("")
    lines.append("> ⚠️ SCAFFOLD — analysis workspace. Verbatim responses are collected by "
                 "`collect_observations.py` into the dated folder; fill in the analysis TODOs below.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append("TODO: 2–6 sentence summary of this session's most important findings.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Law Status")
    lines.append("")
    lines.append("TODO: for each active law (see README), state whether this session "
                 "confirms, strengthens, revises, or withdraws it, with the supporting count.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Query-Level Findings")
    lines.append("")
    for q in queries:
        lines.append(f"## {q['id']} — {q['text']}")
        lines.append("")
        lines.append("### Entities by system")
        lines.append("")
        header = "| Entity | " + " | ".join(SYSTEMS) + " |"
        sep = "|---|" + "|".join(["---:"] * len(SYSTEMS)) + "|"
        lines.append(header)
        lines.append(sep)
        lines.append("| TODO | " + " | ".join([""] * len(SYSTEMS)) + " |")
        lines.append("")
        lines.append("### Interpretation")
        lines.append("")
        lines.append("TODO")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Methodological Notes")
    lines.append("")
    lines.append("TODO: exclusions, query-set version, anomalies, and any deviations this session.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"## Day {day} One-Sentence Conclusion")
    lines.append("")
    lines.append("TODO")
    lines.append("")
    return "\n".join(lines)


def build_analysis(date: dt.date, day: int, models: dict[str, str]) -> dict:
    queries = queries_for_day(day)
    return {
        "observation": {
            "title": f"MIBO {ordinal(day)} Observation",
            "date": date.isoformat(),
            "timezone": "Asia/Tokyo",
            "included_systems": [
                {"system": s, "model": models.get(s, TODO_MODEL), "mode": "API"}
                for s in SYSTEMS
            ],
            "excluded_systems": [],
            "total_included_observations": observations_this_session(day),
            "cumulative_observations_after_session": cumulative_observations(day),
        },
        "law_status": {"TODO": "per-law status for this session"},
        "observations": [
            {
                "query_id": q["id"],
                "system": s,
                "model": models.get(s, TODO_MODEL),
                "entities": "",
                "inline_citations": "",
                "terminal_sources": "",
                "code": "",
                "notes": "",
            }
            for q in queries
            for s in SYSTEMS
        ],
    }


def build_coded_csv(date: dt.date, day: int, models: dict[str, str]) -> str:
    header = "query_id,system,model,entities,inline_citations,terminal_sources,code,notes"
    rows = [header]
    for q in queries_for_day(day):
        for s in SYSTEMS:
            # model filled from run_metadata when available; coding fields blank.
            rows.append(f"{q['id']},{s},{models.get(s, '')},,,,,")
    return "\n".join(rows) + "\n"


def build_law_updates_md(date: dt.date, day: int) -> str:
    return "\n".join([
        f"# MIBO Day {day} — Law Updates",
        "",
        f"**Observation date**: {date.isoformat()}",
        "",
        "> SCAFFOLD — for each active law (see repository README), record its status this "
        "session (confirmed / strengthened / revised / withdrawn) with the supporting count, "
        "then remove this note.",
        "",
        "## Law status this session",
        "",
        "TODO",
        "",
        "## Candidate propositions",
        "",
        "TODO",
        "",
    ])


# --- Writing ---------------------------------------------------------------

def write_if_absent(path: Path, content: str, created: list[str], skipped: list[str]) -> None:
    if path.exists():
        skipped.append(str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created.append(str(path))


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold the weekly MIBO record.")
    parser.add_argument(
        "--date",
        help="Observation date (YYYY-MM-DD). Defaults to today's date in Asia/Tokyo.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to write into (default: current directory).",
    )
    args = parser.parse_args()

    if args.date:
        date = dt.date.fromisoformat(args.date)
    else:
        date = dt.datetime.now(TOKYO).date()

    if date.weekday() != 1:  # Monday == 0, Tuesday == 1
        print(
            f"warning: {date.isoformat()} is a {date.strftime('%A')}, not a Tuesday; "
            "MIBO observations run on Tuesdays.",
            file=sys.stderr,
        )

    day = day_number(date)
    if day < 1:
        print(f"error: {date.isoformat()} is before Day 1 ({DAY_ONE.isoformat()}).",
              file=sys.stderr)
        return 1

    root = Path(args.root)
    date_s = date.isoformat()
    data_dir = root / date_s
    # Pull real model ids from the collector's run_metadata.json when it has already run.
    models = load_models(data_dir)
    created: list[str] = []
    skipped: list[str] = []

    # 1) Observation report (narrative analysis markdown)
    write_if_absent(root / f"{date_s}-observation.md",
                    build_observation_md(date, day, models), created, skipped)

    # 2) Analysis workspace inside the dated folder. run_metadata.json / responses.json /
    #    raw-responses.md are owned by collect_observations.py, not written here.
    write_if_absent(data_dir / "analysis.json",
                    json.dumps(build_analysis(date, day, models), ensure_ascii=False, indent=2) + "\n",
                    created, skipped)
    write_if_absent(data_dir / "coded-observations.csv",
                    build_coded_csv(date, day, models), created, skipped)
    write_if_absent(data_dir / "law-updates.md",
                    build_law_updates_md(date, day), created, skipped)

    print(f"MIBO weekly scaffold — {date_s} (Day {day})")
    for p in created:
        print(f"  created: {p}")
    for p in skipped:
        print(f"  skipped (exists): {p}")
    if not created:
        print("  nothing to create; all files already present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
