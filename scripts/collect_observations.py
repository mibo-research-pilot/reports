#!/usr/bin/env python3
"""Collect MIBO observations via each provider's API and record them verbatim.

MIBO observes API-based answers: the same fixed query set is sent to the same set of
deployed AI systems every week and the responses are recorded verbatim. This script
performs that collection over the provider REST APIs, so the whole observation is
automatable and reproducible from the recorded metadata.

For each (query, system) it sends the query to the provider's API and records the
verbatim response, the exact model id used, token usage, latency, and any error. A
failure on one system is captured and does not stop collection of the others.

Outputs, all under the dated folder ``YYYY-MM-DD/``:
  - responses.json     structured verbatim results (one entry per query × system)
  - raw-responses.md   human-readable verbatim transcript
  - run_metadata.json  run-level metadata (models, timestamps, per-system status)

API keys are read from the environment variable named by each system's ``api_key_env``
in observation_config.json. A system whose key is absent is skipped and recorded as
such (status "skipped_no_api_key"), so the run still produces a partial record.

Usage:
    python3 scripts/collect_observations.py                 # today's Asia/Tokyo date
    python3 scripts/collect_observations.py --date 2026-08-04
    python3 scripts/collect_observations.py --force         # re-collect even if present
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from zoneinfo import ZoneInfo

TOKYO = ZoneInfo("Asia/Tokyo")
DAY_ONE = dt.date(2026, 5, 5)
HTTP_TIMEOUT = 120  # seconds
MAX_RETRIES = 3     # transient-error retries per request


def day_number(date: dt.date) -> int:
    return (date - DAY_ONE).days // 7 + 1


# --- HTTP helper -----------------------------------------------------------

def _post_json(url: str, payload: dict, headers: dict) -> dict:
    """POST JSON with retries on transient errors. Returns the parsed JSON body.

    Raises RuntimeError with a readable message on a non-retryable or exhausted error.
    """
    data = json.dumps(payload).encode("utf-8")
    last_err = None
    for attempt in range(1, MAX_RETRIES + 1):
        req = urllib.request.Request(url, data=data, method="POST")
        for k, v in {"Content-Type": "application/json", **headers}.items():
            req.add_header(k, v)
        try:
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            body = e.read().decode("utf-8", "replace")[:500]
            last_err = f"HTTP {e.code}: {body}"
            # 429 / 5xx are worth retrying; 4xx (bad request/auth) are not.
            if e.code != 429 and e.code < 500:
                break
        except (urllib.error.URLError, TimeoutError) as e:
            last_err = f"network error: {e}"
        if attempt < MAX_RETRIES:
            time.sleep(2 ** attempt)
    raise RuntimeError(last_err or "unknown request error")


# --- Provider adapters -----------------------------------------------------
# Each returns (text, model_used, usage_dict, extra_dict).

def call_openai(system: dict, key: str, query: str) -> tuple[str, str, dict, dict]:
    url = system.get("endpoint", "https://api.openai.com/v1/chat/completions")
    payload = {"model": system["model"], "messages": [{"role": "user", "content": query}],
               **system.get("params", {})}
    body = _post_json(url, payload, {"Authorization": f"Bearer {key}"})
    text = body["choices"][0]["message"]["content"]
    return text, body.get("model", system["model"]), body.get("usage", {}), {}


def call_anthropic(system: dict, key: str, query: str) -> tuple[str, str, dict, dict]:
    url = system.get("endpoint", "https://api.anthropic.com/v1/messages")
    params = dict(system.get("params", {}))
    params.setdefault("max_tokens", 4096)
    payload = {"model": system["model"], "messages": [{"role": "user", "content": query}],
               **params}
    body = _post_json(url, payload, {"x-api-key": key, "anthropic-version": "2023-06-01"})
    text = "".join(b.get("text", "") for b in body.get("content", []) if b.get("type") == "text")
    return text, body.get("model", system["model"]), body.get("usage", {}), {}


def call_google(system: dict, key: str, query: str) -> tuple[str, str, dict, dict]:
    base = system.get("endpoint", "https://generativelanguage.googleapis.com/v1beta/models")
    url = f"{base}/{system['model']}:generateContent?key={key}"
    payload = {"contents": [{"parts": [{"text": query}]}], **system.get("params", {})}
    body = _post_json(url, payload, {})
    parts = body["candidates"][0]["content"]["parts"]
    text = "".join(p.get("text", "") for p in parts)
    return text, system["model"], body.get("usageMetadata", {}), {}


def call_perplexity(system: dict, key: str, query: str) -> tuple[str, str, dict, dict]:
    url = system.get("endpoint", "https://api.perplexity.ai/chat/completions")
    payload = {"model": system["model"], "messages": [{"role": "user", "content": query}],
               **system.get("params", {})}
    body = _post_json(url, payload, {"Authorization": f"Bearer {key}"})
    text = body["choices"][0]["message"]["content"]
    extra = {}
    if "citations" in body:
        extra["citations"] = body["citations"]
    return text, body.get("model", system["model"]), body.get("usage", {}), extra


PROVIDERS = {
    "openai": call_openai,
    "anthropic": call_anthropic,
    "google": call_google,
    "perplexity": call_perplexity,
}


# --- Collection ------------------------------------------------------------

def collect(config: dict, date: dt.date) -> dict:
    day = day_number(date)
    started = dt.datetime.now(TOKYO)
    results = []

    for q in config["queries"]:
        for system in config["systems"]:
            provider = system["provider"]
            caller = PROVIDERS.get(provider)
            entry = {
                "query_id": q["id"],
                "language": q["language"],
                "category": q["category"],
                "query": q["text"],
                "system": system["system"],
                "provider": provider,
                "model_requested": system["model"],
            }
            key = os.environ.get(system.get("api_key_env", ""), "")
            if caller is None:
                entry.update(status="error", error=f"unknown provider '{provider}'")
                results.append(entry)
                continue
            if not key:
                entry.update(status="skipped_no_api_key",
                             error=f"env {system.get('api_key_env')} not set")
                results.append(entry)
                print(f"  skip  {q['id']} {system['system']}: no API key")
                continue
            t0 = time.monotonic()
            try:
                text, model_used, usage, extra = caller(system, key, q["text"])
                entry.update(status="ok", model_used=model_used, response=text,
                             usage=usage, latency_ms=round((time.monotonic() - t0) * 1000),
                             **extra)
                print(f"  ok    {q['id']} {system['system']} ({len(text)} chars)")
            except Exception as e:  # noqa: BLE001 - record any provider failure, keep going
                entry.update(status="error", error=str(e),
                             latency_ms=round((time.monotonic() - t0) * 1000))
                print(f"  FAIL  {q['id']} {system['system']}: {e}", file=sys.stderr)
            results.append(entry)

    ended = dt.datetime.now(TOKYO)
    return {
        "date": date.isoformat(),
        "day": day,
        "query_set": config.get("query_set"),
        "collected_at_start": started.isoformat(),
        "collected_at_end": ended.isoformat(),
        "timezone": "Asia/Tokyo",
        "results": results,
    }


# --- Rendering -------------------------------------------------------------

def render_raw_md(run: dict, config: dict) -> str:
    lines = [f"# MIBO raw API responses — {run['date']} (Day {run['day']})", ""]
    lines.append("Collected via provider APIs. Model outputs recorded verbatim.")
    lines.append("")
    lines.append(f"- Query set: {run['query_set']}")
    lines.append(f"- Collection window: {run['collected_at_start']} → {run['collected_at_end']} (Asia/Tokyo)")
    lines.append("")
    lines.append("---")
    lines.append("")
    by_q = {q["id"]: q for q in config["queries"]}
    for qid in [q["id"] for q in config["queries"]]:
        q = by_q[qid]
        lines.append(f"## {qid} — {q['text']}")
        lines.append("")
        for entry in run["results"]:
            if entry["query_id"] != qid:
                continue
            model = entry.get("model_used", entry.get("model_requested", ""))
            lines.append(f"### {entry['system']} ({model}) — {entry['status']}")
            lines.append("")
            if entry["status"] == "ok":
                lines.append(entry["response"].rstrip())
                if entry.get("citations"):
                    lines.append("")
                    lines.append("**Citations:**")
                    for i, c in enumerate(entry["citations"], 1):
                        lines.append(f"{i}. {c}")
            else:
                lines.append(f"> _No response recorded ({entry['status']}): "
                             f"{entry.get('error', '')}_")
            lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)


def render_run_metadata(run: dict, config: dict) -> dict:
    per_system = []
    for system in config["systems"]:
        entries = [r for r in run["results"] if r["system"] == system["system"]]
        ok = sum(1 for r in entries if r["status"] == "ok")
        models = sorted({r.get("model_used", r.get("model_requested"))
                         for r in entries if r.get("status") == "ok"})
        per_system.append({
            "system": system["system"],
            "provider": system["provider"],
            "model_requested": system["model"],
            "model_used": models[0] if len(models) == 1 else (models or None),
            "mode": "API",
            "ok_count": ok,
            "total_queries": len(entries),
        })
    ok_total = sum(1 for r in run["results"] if r["status"] == "ok")
    return {
        "observatory": "MIBO",
        "japanese_name": "機械情報行動観測所",
        "session": f"Day {run['day']}",
        "observation_date": run["date"],
        "timezone": "Asia/Tokyo",
        "method": "Longitudinal Machine Observation",
        "observation_mode": "API collection (automated)",
        "collection_method": {
            "type": "provider_api",
            "automation_used": True,
            "api_used": True,
            "collector": "scripts/collect_observations.py",
        },
        "collected_at_start": run["collected_at_start"],
        "collected_at_end": run["collected_at_end"],
        "query_set": run["query_set"],
        "query_count": len(config["queries"]),
        "systems": per_system,
        "included_observation_count": ok_total,
        "expected_observation_count": len(run["results"]),
    }


# --- Main ------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Collect MIBO observations via provider APIs.")
    parser.add_argument("--date", help="Observation date (YYYY-MM-DD). Default: today (Asia/Tokyo).")
    parser.add_argument("--root", default=".", help="Repository root (default: current directory).")
    parser.add_argument("--config", default="scripts/observation_config.json",
                        help="Path to the observation config JSON.")
    parser.add_argument("--force", action="store_true",
                        help="Re-collect even if responses.json already exists.")
    args = parser.parse_args()

    date = dt.date.fromisoformat(args.date) if args.date else dt.datetime.now(TOKYO).date()
    if date.weekday() != 1:
        print(f"warning: {date.isoformat()} is a {date.strftime('%A')}, not a Tuesday.",
              file=sys.stderr)

    config = json.loads(Path(args.config).read_text(encoding="utf-8"))
    root = Path(args.root)
    data_dir = root / date.isoformat()
    responses_path = data_dir / "responses.json"

    if responses_path.exists() and not args.force:
        print(f"responses.json already exists for {date.isoformat()}; use --force to re-collect.")
        return 0

    print(f"Collecting MIBO observations — {date.isoformat()} (Day {day_number(date)})")
    run = collect(config, date)

    data_dir.mkdir(parents=True, exist_ok=True)
    responses_path.write_text(json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (data_dir / "raw-responses.md").write_text(render_raw_md(run, config), encoding="utf-8")
    (data_dir / "run_metadata.json").write_text(
        json.dumps(render_run_metadata(run, config), ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8")

    ok = sum(1 for r in run["results"] if r["status"] == "ok")
    print(f"Recorded {ok}/{len(run['results'])} responses into {data_dir}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
