#!/usr/bin/env python3
"""Draft the entity coding for a week's collected MIBO responses, using an LLM.

After collect_observations.py has recorded the verbatim responses and
scaffold_weekly_record.py has laid out the coding skeleton, this script reads each
verbatim response and asks a coding model to extract, for every (query, system):

  - entities            the main recommended products / named entities, in order
  - inline_citations    yes/no — inline citation markers ([1], [2] …) in the body
  - terminal_sources    yes/no — a source/reference list at the end
  - code                yes/no — the answer contains a code block
  - notes               one concise sentence

``terminal_sources`` is corrected deterministically afterwards: providers such as Perplexity
return the source list in a structured ``citations`` array rather than in the answer text, so
a text-only reading would miscode it as "no". When the collected response carries a non-empty
``citations`` array, terminal_sources is set to "yes" and the count recorded in analysis.json.

The result is written back into ``YYYY-MM-DD/coded-observations.csv`` and the
``observations`` array of ``YYYY-MM-DD/analysis.json`` as a **draft**. Coding is an
analytic judgement, so the output is explicitly marked ``coding_status: auto_draft`` for
the observer to review and correct before publishing.

Safety / idempotence:
  - Rows that already have entities filled are left untouched unless ``--force`` is given,
    so a re-run never clobbers the observer's manual corrections.
  - If the coder API key is absent, the script exits cleanly and leaves the skeleton as-is.

Usage:
    python3 scripts/code_observations.py --date 2026-08-04
    python3 scripts/code_observations.py --date 2026-08-04 --force
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
import re
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

# Reuse the collector's retrying JSON POST helper (same directory on sys.path).
from collect_observations import _post_json

TOKYO = ZoneInfo("Asia/Tokyo")

CODING_PROMPT = """You are coding a single AI system's response for a longitudinal \
observation study (MIBO). Read the user query and the system's response, then return ONLY \
a JSON object with these fields:

- "entities": array of strings — the main recommended products, tools, services, or named \
people that the response puts forward as its answer, in the order presented. Exclude generic \
category words and section headers. For a "name 5 people" style query, list the people.
- "inline_citations": "yes" or "no" — does the response body attach inline citation markers \
(e.g. [1], [2]) to individual claims?
- "terminal_sources": "yes" or "no" — is there a sources / references / citations list at the end?
- "code": "yes" or "no" — does the response contain a code block?
- "notes": one concise English sentence characterizing the response.

Return only the JSON object, no prose, no code fence.

QUERY ({language}, {category}):
{query}

RESPONSE:
{response}
"""


def call_coder(coder: dict, key: str, entry: dict) -> dict:
    """Ask the coding model to code one response. Returns the parsed coding dict."""
    prompt = CODING_PROMPT.format(
        language=entry.get("language", ""),
        category=entry.get("category", ""),
        query=entry["query"],
        response=entry["response"],
    )
    url = coder.get("endpoint", "https://api.anthropic.com/v1/messages")
    payload = {
        "model": coder["model"],
        "max_tokens": coder.get("max_tokens", 1024),
        "messages": [{"role": "user", "content": prompt}],
    }
    body = _post_json(url, payload, {"x-api-key": key, "anthropic-version": "2023-06-01"})
    text = "".join(b.get("text", "") for b in body.get("content", []) if b.get("type") == "text")
    return parse_coding(text)


def parse_coding(text: str) -> dict:
    """Tolerantly extract the JSON object from the coder's reply."""
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        raise ValueError(f"no JSON object in coder reply: {text[:200]!r}")
    obj = json.loads(m.group(0))
    ents = obj.get("entities", [])
    if isinstance(ents, str):
        ents = [e.strip() for e in re.split(r"[;\n]", ents) if e.strip()]

    def yn(v: object) -> str:
        return "yes" if str(v).strip().lower() in ("yes", "true", "1") else "no"

    return {
        "entities": "; ".join(str(e).strip() for e in ents if str(e).strip()),
        "inline_citations": yn(obj.get("inline_citations")),
        "terminal_sources": yn(obj.get("terminal_sources")),
        "code": yn(obj.get("code")),
        "notes": str(obj.get("notes", "")).strip().replace("\n", " "),
    }


def load_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description="Draft MIBO entity coding with an LLM.")
    parser.add_argument("--date", help="Observation date (YYYY-MM-DD). Default: today (Asia/Tokyo).")
    parser.add_argument("--root", default=".", help="Repository root (default: current directory).")
    parser.add_argument("--config", default="scripts/observation_config.json",
                        help="Path to the observation config JSON.")
    parser.add_argument("--force", action="store_true",
                        help="Re-code rows even if they already have entities.")
    args = parser.parse_args()

    date = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(TOKYO).date()
    date_s = date.isoformat()
    root = Path(args.root)
    data_dir = root / date_s

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    coder = config.get("coder")
    if not coder:
        print("no 'coder' section in config; nothing to do.")
        return 0
    key = os.environ.get(coder.get("api_key_env", ""), "")
    if not key:
        print(f"coder API key ({coder.get('api_key_env')}) not set; leaving coding skeleton as-is.")
        return 0

    responses_path = data_dir / "responses.json"
    csv_path = data_dir / "coded-observations.csv"
    analysis_path = data_dir / "analysis.json"
    if not responses_path.exists():
        print(f"error: {responses_path} not found; run collect_observations.py first.",
              file=sys.stderr)
        return 1
    if not csv_path.exists():
        print(f"error: {csv_path} not found; run scaffold_weekly_record.py first.",
              file=sys.stderr)
        return 1

    run = json.loads(responses_path.read_text(encoding="utf-8"))
    ok_by_key = {(r["query_id"], r["system"]): r
                 for r in run["results"] if r.get("status") == "ok"}

    fieldnames, rows = load_csv(csv_path)
    coding_by_key: dict[tuple, dict] = {}
    ts_by_key: dict[tuple, int] = {}  # (query_id, system) -> terminal source count
    coded = skipped = failed = 0

    for row in rows:
        rk = (row["query_id"], row["system"])
        entry = ok_by_key.get(rk)

        # Deterministic terminal-source correction from the provider's structured citations
        # array (e.g. Perplexity). This needs no API call, so it runs for every row — even
        # rows already LLM-coded or skipped below — and overrides the model's text-only guess.
        if entry is not None:
            n = len(entry.get("citations") or [])
            if n:
                row["terminal_sources"] = "yes"
                ts_by_key[rk] = n

        if row.get("entities", "").strip() and not args.force:
            skipped += 1
            continue
        if entry is None:
            continue  # no successful response to code for this cell
        try:
            coding = call_coder(coder, key, entry)
        except Exception as e:  # noqa: BLE001 - record failure, keep coding the rest
            print(f"  FAIL  {rk[0]} {rk[1]}: {e}", file=sys.stderr)
            failed += 1
            continue
        if rk in ts_by_key:  # keep the structured reading over the model's text-only guess
            coding["terminal_sources"] = "yes"
        row.update(coding)
        coding_by_key[rk] = coding
        coded += 1
        print(f"  coded {rk[0]} {rk[1]}: {coding['entities'][:60]}")

    write_csv(csv_path, fieldnames, rows)

    # Mirror the coding into analysis.json observations.
    if analysis_path.exists():
        analysis = json.loads(analysis_path.read_text(encoding="utf-8"))
        for obs in analysis.get("observations", []):
            rk = (obs.get("query_id"), obs.get("system"))
            coding = coding_by_key.get(rk)
            if coding:
                obs.update(coding)
            if rk in ts_by_key:  # deterministic terminal-source correction + count
                obs["terminal_sources"] = "yes"
                obs["terminal_source_count"] = ts_by_key[rk]
        analysis["coding_status"] = ("auto — entities drafted by LLM; terminal sources read "
                                     "from the provider citations array")
        analysis["coding_model"] = coder["model"]
        analysis_path.write_text(json.dumps(analysis, ensure_ascii=False, indent=2) + "\n",
                                 encoding="utf-8")

    print(f"Coding draft — {date_s}: coded {coded}, skipped {skipped} (already coded), "
          f"failed {failed}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
