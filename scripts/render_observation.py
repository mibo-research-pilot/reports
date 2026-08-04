#!/usr/bin/env python3
"""Render the weekly MIBO observation report (``YYYY-MM-DD-observation.md``) automatically.

This is the final step of the weekly pipeline:

    collect_observations.py  ->  scaffold_weekly_record.py  ->  code_observations.py
        ->  render_observation.py   (this script)

By the time this runs, ``YYYY-MM-DD/analysis.json`` holds the per-(query, system) entity
coding and ``YYYY-MM-DD/run_metadata.json`` holds the collection facts. This script turns
that data into a finished ``observation.md``:

  - **Entity-by-system tables** are built deterministically from the coded entities — each
    cell shows the entity's rank in that system's answer (blank = not mentioned).
  - **Narrative sections** (executive summary, law status, per-query interpretation,
    methodological notes, one-sentence conclusion) are written by the ``reporter`` model
    from the same data.

The report is a machine-maintained artifact: it is regenerated (overwritten) on every run
so it always reflects the current data. To freeze a week's report against regeneration,
put the marker ``<!-- mibo:manual -->`` anywhere in the file and this script will skip it.

If the reporter API key is absent, the tables are still rendered and the narrative sections
are left as short TODO placeholders, so the step degrades gracefully.

Usage:
    python3 scripts/render_observation.py --date 2026-08-04
    python3 scripts/render_observation.py --date 2026-08-04 --force   # ignore the freeze marker
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

# Reuse the collector's retrying JSON POST helper (same directory on sys.path).
from collect_observations import _post_json

TOKYO = ZoneInfo("Asia/Tokyo")

FREEZE_MARKER = "<!-- mibo:manual -->"

# Single source of truth for the laws: the Established-laws section of core/laws.md,
# fetched fresh at render time so the reporter always grounds Law Status on the current
# authoritative definitions. Overridable via the "laws_source_url" config key.
DEFAULT_LAWS_URL = "https://raw.githubusercontent.com/mibo-research-pilot/core/main/laws.md"


def fetch_laws_text(url: str) -> str:
    """Fetch core/laws.md and return its '## Established laws' section (Markdown).

    Returns "" on any network/parse failure so render degrades to a data-only Law Status
    rather than failing the run. The reporter prompt handles an empty laws text explicitly.
    """
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "mibo-render"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            md = resp.read().decode("utf-8")
    except Exception as e:  # noqa: BLE001 - network/decoding; caller falls back gracefully
        print(f"warning: could not fetch laws from {url} ({e}); Law Status will be data-only.",
              file=sys.stderr)
        return ""
    lines = md.splitlines()
    out: list[str] = []
    capturing = False
    for ln in lines:
        if ln.startswith("## "):
            if ln.strip().lower().startswith("## established laws"):
                capturing = True
                continue
            if capturing:  # reached the next H2 (e.g. "## Withdrawn laws") — stop.
                break
        if capturing:
            out.append(ln)
    return "\n".join(out).strip()


# --- Small helpers ---------------------------------------------------------

def ordinal(n: int) -> str:
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def norm_entity(s: str) -> str:
    """Normalization key for grouping near-identical entity surface forms across systems."""
    return re.sub(r"\s+", " ", s.strip().lower()).strip(" .,;:·・")


def split_entities(raw: str) -> list[str]:
    """analysis.json stores entities as a '; '-joined string; split back to a list."""
    if not raw:
        return []
    return [e.strip() for e in raw.split(";") if e.strip()]


# --- Deterministic entity table -------------------------------------------

def entity_rows(systems: list[str], per_system: dict[str, list[str]]) -> list[tuple[str, list[str]]]:
    """Union entities across systems; each cell is the entity's 1-based rank in that system."""
    groups: dict[str, dict] = {}
    first_seen: list[str] = []
    for system in systems:
        for i, ent in enumerate(per_system.get(system, [])):
            key = norm_entity(ent)
            if not key:
                continue
            if key not in groups:
                groups[key] = {"display": ent, "ranks": {}}
                first_seen.append(key)
            groups[key]["ranks"].setdefault(system, i + 1)

    def sort_key(key: str):
        g = groups[key]
        return (-len(g["ranks"]), min(g["ranks"].values()), first_seen.index(key))

    rows: list[tuple[str, list[str]]] = []
    for key in sorted(first_seen, key=sort_key):
        g = groups[key]
        cells = [str(g["ranks"].get(s, "")) for s in systems]
        rows.append((g["display"], cells))
    return rows


def render_entity_table(systems: list[str], rows: list[tuple[str, list[str]]]) -> list[str]:
    out = ["| Entity | " + " | ".join(systems) + " |",
           "|---|" + "|".join(["---:"] * len(systems)) + "|"]
    if not rows:
        out.append("| _(no entities coded)_ | " + " | ".join([""] * len(systems)) + " |")
    for display, cells in rows:
        out.append(f"| {display} | " + " | ".join(cells) + " |")
    return out


# --- Reporter (LLM narrative) ---------------------------------------------

REPORTER_PROMPT = """You are writing the narrative sections of a weekly report for MIBO \
(Machine Information Behavior Observatory), a longitudinal study that puts the same fixed \
queries to the same deployed AI systems every week and records the responses verbatim. \
This is Day {day} ({date}). The observation focus is source-attribution and citation-like \
behavior, canonical/entity stability, and per-model style.

You are given this session's coded data (entities each system returned per query, plus \
inline-citation / terminal-source / code flags and a one-line note), the collection facts, \
and the observatory's established laws. Write grounded, specific prose — cite concrete \
counts and system names from the data. Do not invent sources, URLs, or facts not present \
in the data. When the data is insufficient to judge a law, say so rather than guessing.

Return ONLY a JSON object with these string fields (Markdown allowed inside each):
- "executive_summary": 2-5 sentences on this session's most important observations.
- "law_status": a Markdown bullet list. For each established law in the LAWS section below \
(reference it by its id and name, e.g. "Law IX — Perplexity Inline Citation Shift"), state \
confirm / strengthen / revise / withdraw / insufficient-evidence THIS session, with the \
supporting count from the data. Only discuss the laws in that section. If the LAWS section \
is empty, write a single bullet noting the authoritative law list was unavailable this run \
and summarize the citation/canonical evidence without assigning law numbers.
- "query_interpretations": an object mapping each query_id (e.g. "q001") to 1-3 sentences \
on cross-system agreement, divergence, and citation behavior for that query.
- "methodological_notes": 1-3 sentences on exclusions, any systems that errored or were \
skipped, the query-set version, and anomalies. Base this on the collection facts provided.
- "conclusion": a single sentence capturing the session.

COLLECTION FACTS (JSON):
{facts}

ESTABLISHED LAWS (Markdown, authoritative — from core/laws.md):
{laws}

THIS SESSION'S CODED DATA (JSON):
{data}
"""


def call_reporter(reporter: dict, key: str, facts: dict, laws_text: str, data: dict) -> dict:
    prompt = REPORTER_PROMPT.format(
        day=facts.get("day", "?"),
        date=facts.get("date", "?"),
        facts=json.dumps(facts, ensure_ascii=False),
        laws=laws_text if laws_text else "(unavailable this run)",
        data=json.dumps(data, ensure_ascii=False),
    )
    url = reporter.get("endpoint", "https://api.anthropic.com/v1/messages")
    payload = {
        "model": reporter["model"],
        "max_tokens": reporter.get("max_tokens", 4096),
        "messages": [{"role": "user", "content": prompt}],
    }
    body = _post_json(url, payload, {"x-api-key": key, "anthropic-version": "2023-06-01"})
    text = "".join(b.get("text", "") for b in body.get("content", []) if b.get("type") == "text")
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        raise ValueError(f"no JSON object in reporter reply: {text[:200]!r}")
    return json.loads(m.group(0))


# --- Report assembly -------------------------------------------------------

def build_report(date_s: str, day: int, analysis: dict, meta: dict, queries: list[dict],
                 systems: list[str], narrative: dict, model_note: str) -> str:
    obs = analysis.get("observation", {})
    included = obs.get("included_systems", [])
    models = {s.get("system"): s.get("model", "?") for s in included}
    systems_line = ", ".join(f"{s} ({models.get(s, '?')})" for s in systems)

    excluded = obs.get("excluded_systems", [])
    excluded_line = ", ".join(
        f"{e.get('system', '?')} ({e.get('reason', 'no reason given')})" for e in excluded
    ) if excluded else "none"

    total = obs.get("total_included_observations", "?")
    cumulative = obs.get("cumulative_observations_after_session", "?")

    # Group coded observations by query -> system -> ordered entities.
    by_query: dict[str, dict[str, list[str]]] = {}
    flags_by_query: dict[str, dict[str, dict]] = {}
    for o in analysis.get("observations", []):
        q, s = o.get("query_id"), o.get("system")
        by_query.setdefault(q, {})[s] = split_entities(o.get("entities", ""))
        flags_by_query.setdefault(q, {})[s] = o

    qi = narrative.get("query_interpretations", {}) if narrative else {}

    L: list[str] = []
    L.append(f"# {ordinal(day)} Observation — {date_s}")
    L.append("")
    L.append("**Observatory**: MIBO — Machine Information Behavior Observatory  ")
    L.append("**Japanese name**: 機械情報行動観測所  ")
    L.append(f"**Observation date**: {date_s}  ")
    L.append("**Timezone**: Asia/Tokyo  ")
    L.append("**Core method**: Longitudinal Machine Observation (LMO)  ")
    L.append("**Observation mode**: API collection (automated)  ")
    L.append(f"**Included systems**: {systems_line}  ")
    L.append(f"**Excluded systems**: {excluded_line}  ")
    L.append(f"**Included observations this session**: {total}  ")
    L.append(f"**Cumulative MIBO observations after this session**: {cumulative}  ")
    win_start = meta.get("collected_at_start")
    win_end = meta.get("collected_at_end")
    if win_start and win_end:
        L.append(f"**Collection window**: {win_start} → {win_end}  ")
    L.append(f"**Raw responses**: [`{date_s}/raw-responses.md`]({date_s}/raw-responses.md) "
             f"(verbatim API outputs)  ")
    L.append("")
    L.append(f"> {model_note}")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Executive Summary")
    L.append("")
    L.append(narrative.get("executive_summary", "TODO").strip() if narrative else "TODO")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Law Status")
    L.append("")
    L.append(narrative.get("law_status", "TODO").strip() if narrative else "TODO")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## Query-Level Findings")
    L.append("")
    for q in queries:
        qid = q["id"]
        L.append(f"## {qid} — {q['text']}")
        L.append("")
        L.append("### Entities by system")
        L.append("")
        L.append("_Each cell is the entity's rank in that system's answer (blank = not mentioned)._")
        L.append("")
        rows = entity_rows(systems, by_query.get(qid, {}))
        L.extend(render_entity_table(systems, rows))
        L.append("")
        # Citation behaviour line, straight from the coded flags — deterministic.
        flags = flags_by_query.get(qid, {})
        if flags:
            def cite_cell(sysname: str) -> str:
                o = flags.get(sysname, {})
                inl = o.get("inline_citations") or "?"
                ts = o.get("terminal_sources") or "?"
                count = o.get("terminal_source_count")
                ts_disp = f"{ts}({count})" if count else ts
                return f"{sysname}: inline={inl}/terminal={ts_disp}"
            cites = ", ".join(cite_cell(s) for s in systems)
            L.append(f"_Citations — {cites}._")
            L.append("")
        L.append("### Interpretation")
        L.append("")
        L.append(qi.get(qid, "TODO").strip() if qi.get(qid) else "TODO")
        L.append("")
    L.append("---")
    L.append("")
    L.append("## Methodological Notes")
    L.append("")
    L.append(narrative.get("methodological_notes", "TODO").strip() if narrative else "TODO")
    L.append("")
    L.append("---")
    L.append("")
    L.append(f"## Day {day} One-Sentence Conclusion")
    L.append("")
    L.append(narrative.get("conclusion", "TODO").strip() if narrative else "TODO")
    L.append("")
    return "\n".join(L)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render the weekly MIBO observation report.")
    parser.add_argument("--date", help="Observation date (YYYY-MM-DD). Default: today (Asia/Tokyo).")
    parser.add_argument("--root", default=".", help="Repository root (default: current directory).")
    parser.add_argument("--config", default="scripts/observation_config.json",
                        help="Path to the observation config JSON.")
    parser.add_argument("--force", action="store_true",
                        help=f"Regenerate even if the file contains the {FREEZE_MARKER} freeze marker.")
    args = parser.parse_args()

    date = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(TOKYO).date()
    date_s = date.isoformat()
    root = Path(args.root)
    data_dir = root / date_s

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    queries = config.get("queries", [])
    systems = [s["system"] for s in config.get("systems", [])]
    # Laws are single-sourced from core/laws.md, fetched fresh at render time.
    laws_text = fetch_laws_text(config.get("laws_source_url", DEFAULT_LAWS_URL))

    analysis_path = data_dir / "analysis.json"
    if not analysis_path.exists():
        print(f"error: {analysis_path} not found; run scaffold/code first.", file=sys.stderr)
        return 1
    analysis = json.loads(analysis_path.read_text(encoding="utf-8"))

    meta_path = data_dir / "run_metadata.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.exists() else {}

    day = analysis.get("observation", {}).get("_day")
    # Day number is derivable from the cumulative helper only via scaffold; recompute simply.
    day_one = dt.date(2026, 5, 5)
    day = (date - day_one).days // 7 + 1

    out_path = root / f"{date_s}-observation.md"
    if out_path.exists() and FREEZE_MARKER in out_path.read_text(encoding="utf-8") and not args.force:
        print(f"{out_path} carries the freeze marker {FREEZE_MARKER}; skipping (use --force to override).")
        return 0

    # Restrict query set to what was actually observed this day (q004/q005 added at Day 3).
    coded_qids = {o.get("query_id") for o in analysis.get("observations", [])}
    if coded_qids:
        queries = [q for q in queries if q["id"] in coded_qids]

    # Narrative: use the reporter model when its key is available; otherwise leave TODOs.
    reporter = config.get("reporter") or config.get("coder")
    narrative: dict = {}
    stamp = dt.datetime.now(TOKYO).replace(microsecond=0).isoformat()
    key = os.environ.get(reporter.get("api_key_env", ""), "") if reporter else ""
    if reporter and key:
        facts = {
            "day": day, "date": date_s,
            "collected_at_start": meta.get("collected_at_start"),
            "collected_at_end": meta.get("collected_at_end"),
            "query_set_id": meta.get("query_set_id") or config.get("query_set"),
            "systems": meta.get("systems", []),
            "excluded_systems": analysis.get("observation", {}).get("excluded_systems", []),
        }
        data = {"observations": analysis.get("observations", [])}
        try:
            narrative = call_reporter(reporter, key, facts, laws_text, data)
            model_note = (f"Automatically generated from this session's verbatim responses by "
                          f"`render_observation.py` — entity tables from the coded data; narrative "
                          f"by {reporter['model']} ({stamp}).")
            print(f"reporter narrative drafted by {reporter['model']}.")
        except Exception as e:  # noqa: BLE001 - fall back to tables-only rather than fail the run
            print(f"warning: reporter failed ({e}); rendering tables with TODO narrative.",
                  file=sys.stderr)
            model_note = (f"Automatically generated by `render_observation.py` ({stamp}); entity "
                          f"tables from the coded data. Narrative generation failed this run — "
                          f"sections left as TODO.")
    else:
        model_note = (f"Automatically generated by `render_observation.py` ({stamp}); entity tables "
                      f"from the coded data. Reporter key absent — narrative sections left as TODO.")
        print("reporter key absent; rendering tables with TODO narrative.")

    report = build_report(date_s, day, analysis, meta, queries, systems, narrative, model_note)
    out_path.write_text(report, encoding="utf-8")
    print(f"wrote {out_path} (Day {day}, {len(queries)} queries, {len(systems)} systems).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
