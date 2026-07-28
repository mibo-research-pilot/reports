# Weekly record automation

Every Tuesday this repository runs the MIBO observation automatically over the provider
APIs and commits the result, so the weekly record is collected without manual copy-paste.

## What runs, and when

- **Schedule**: every **Tuesday 20:00 Asia/Tokyo** (= 11:00 UTC).
- **Where**: GitHub Actions — [`.github/workflows/weekly-record.yml`](.github/workflows/weekly-record.yml).
- **Steps**:
  1. [`scripts/collect_observations.py`](scripts/collect_observations.py) sends the standard
     query set (q001–q005) to each system's API and records the **verbatim** responses.
  2. [`scripts/scaffold_weekly_record.py`](scripts/scaffold_weekly_record.py) builds the
     analysis workspace on top of the collected data.
  3. [`scripts/code_observations.py`](scripts/code_observations.py) LLM-drafts the entity
     coding for each response (entities, citation/source/code flags, a note).
  4. The workflow commits and pushes the week's record to the default branch.

## What each run produces

Both parts of the record for the observation Tuesday:

**1. Collected observation (automatic, verbatim)** — in `YYYY-MM-DD/`:
- `responses.json` — structured verbatim results (one entry per query × system: response
  text, model id used, token usage, latency, and any error).
- `raw-responses.md` — human-readable verbatim transcript.
- `run_metadata.json` — run metadata: models, collection window, per-system status.

**2. Analysis workspace (scaffold + drafted coding, reviewed by the observer)**:
- `YYYY-MM-DD-observation.md` — the narrative report (front matter and model ids pre-filled;
  analysis sections left as `TODO`).
- `YYYY-MM-DD/coded-observations.csv`, `analysis.json` — coding of each response:
  entities plus `inline_citations` / `terminal_sources` / `code` flags and a note. These
  are **LLM-drafted** (`analysis.json` carries `coding_status: auto_draft`) and must be
  reviewed and corrected by the observer before publishing.
- `YYYY-MM-DD/law-updates.md` — law-status template.

Collection and a first-pass entity coding are automatic. Interpretation — law status,
executive summary, and verifying/correcting the drafted coding — remains the observer's
analytic work. The coder only fills rows that are empty, so it never overwrites your
manual corrections on a re-run (use `--force` to re-draft).

## Configuration

The observed systems and models live in
[`scripts/observation_config.json`](scripts/observation_config.json). Edit that file to
change model ids, add/remove systems, or set per-request params. Each system names the
environment variable that holds its API key (`api_key_env`).

Default systems: Gemini (`google`), ChatGPT (`openai`), Claude (`anthropic`),
Perplexity (`perplexity`). **Update the `model` ids to the exact API model strings you
intend to observe** — the defaults mirror the latest report and may need adjusting.

## One-time setup

1. **Add API keys as repository secrets** (Settings → Secrets and variables → Actions):
   `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `PERPLEXITY_API_KEY`.
   A system whose key is missing is skipped and recorded as `skipped_no_api_key`, so the
   run still produces a partial record rather than failing.
2. **Enable write access for Actions**: Settings → Actions → General → Workflow permissions
   → *Read and write permissions*. (The workflow already declares `permissions: contents: write`.)
3. Ensure the workflow file is on the repository's **default branch** so the schedule takes effect.

## Running it manually

- **From GitHub**: Actions tab → *Weekly MIBO record* → **Run workflow**. Optionally pass a
  specific `date` (YYYY-MM-DD); blank uses today's Asia/Tokyo date.
- **Locally** (keys in your environment):

  ```bash
  export OPENAI_API_KEY=... ANTHROPIC_API_KEY=... GEMINI_API_KEY=... PERPLEXITY_API_KEY=...
  python3 scripts/collect_observations.py --date 2026-08-04   # collect verbatim responses
  python3 scripts/scaffold_weekly_record.py --date 2026-08-04 # analysis workspace
  python3 scripts/code_observations.py --date 2026-08-04      # LLM-draft entity coding
  ```

  The coder (`code_observations.py`) uses the `coder` model in
  `observation_config.json` and its `api_key_env` (Anthropic by default).

`collect_observations.py` skips a date that already has `responses.json` (use `--force` to
re-collect). `scaffold_weekly_record.py` never overwrites an existing file. Both are
therefore safe to re-run.

## The observer's weekly workflow

1. The scheduled run collects responses, drafts the coding, and commits on Tuesday.
2. `git pull`, read `YYYY-MM-DD/raw-responses.md`.
3. Review and correct the drafted coding in `coded-observations.csv` / `analysis.json`
   (remove the `auto_draft` marker once verified), and write the report
   (`YYYY-MM-DD-observation.md`, `law-updates.md`).
4. Update the observation log and law table in `README.md`.
5. Commit and push.
