# Weekly record automation

This repository scaffolds the weekly MIBO record automatically so the observer only
has to fill in the observed responses.

## What runs, and when

- **Schedule**: every **Tuesday 20:00 Asia/Tokyo** (= 11:00 UTC).
- **Where**: GitHub Actions — [`.github/workflows/weekly-record.yml`](.github/workflows/weekly-record.yml).
- **What it does**: runs [`scripts/scaffold_weekly_record.py`](scripts/scaffold_weekly_record.py),
  which generates that week's record **scaffold** and commits it directly to the default branch.

Each run produces **both** parts of the record for the observation Tuesday:

1. **Observation report** — `YYYY-MM-DD-observation.md` (narrative template).
2. **Structured data** — `YYYY-MM-DD/` folder containing:
   - `run_metadata.json`
   - `analysis.json`
   - `coded-observations.csv` (20 pre-labelled rows: 5 queries × 4 systems)
   - `law-updates.md`

Every field that can be derived from the schedule is pre-filled — the date, the session/day
number, the observation count, the cumulative total, the query set, and the system columns.
Everything that must be *observed* is left as an explicit `TODO`.

## Why it scaffolds instead of collecting responses

MIBO's method is **Longitudinal Machine Observation**: "Manual web interface, fresh
chat/session, copy-paste observation." The actual responses from ChatGPT, Gemini,
Perplexity, and Claude are collected by a human through each provider's web interface.
An unattended job has no authenticated access to those interfaces, and generating
plausible-looking responses would be fabricating observation data. So the automation
handles the repetitive scaffolding and leaves the observation itself to the observer.

## The observer's weekly workflow

1. On Tuesday, `git pull` — the scaffold for the week is already committed.
2. Collect each system's response through its web interface (as usual).
3. Replace every `TODO` in `YYYY-MM-DD-observation.md` and the `YYYY-MM-DD/` files.
4. Update the observation log and law table in `README.md`.
5. Commit and push.

## Running it manually

- **From GitHub**: Actions tab → *Weekly MIBO record* → **Run workflow**. Optionally pass a
  specific `date` (YYYY-MM-DD); leave blank to use today's Asia/Tokyo date.
- **Locally**:

  ```bash
  python3 scripts/scaffold_weekly_record.py              # today's date (Asia/Tokyo)
  python3 scripts/scaffold_weekly_record.py --date 2026-08-04
  ```

The script is **idempotent**: it never overwrites an existing file, so re-running it — or
running it after you have started filling in data — only creates what is missing.

## One-time setup

For the scheduled job to commit back to the repository, GitHub Actions needs write
permission. The workflow already requests `permissions: contents: write`; in addition,
confirm in **Settings → Actions → General → Workflow permissions** that
*"Read and write permissions"* is enabled. The workflow file must also be present on the
repository's **default branch** for the schedule to take effect.
