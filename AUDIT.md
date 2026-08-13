# MIBO Pilot reports audit for Paper B

- Audit date: 2026-08-14
- Scope: `mibo-research-pilot/reports` only
- Branch: `cleanup/pilot-reports-pre-paper-b`

## Outcome

The repository preserves official reports for Day 1 through Day 15. The latest valid Pilot observation found is Day 15, 2026-08-11: its structured packet contains 20 successful system–query responses, with 284 cumulative Pilot observations reported. Paper B remains frozen at Day 1–Day 13, 2026-05-05 through 2026-07-28, with 244 included observations.

The Paper B count was recomputed from the documented query schedule and included systems: `12 + 12 + (11 × 20) = 244`. Grok remains excluded from the official Day 7–Day 13 analyses and counts.

## Classified findings

| Classification | Finding | Disposition |
|---|---|---|
| Factual contradiction | Historical Day 1–Day 11 and Day 13 reports or metadata contain manual/web-interface provenance wording, despite the verified fact that Pilot collection was API-based continuously from Day 1. | Original historical text and metadata are preserved. README, INDEX, this audit, and the Paper B manifest explicitly supersede the incorrect provenance wording. |
| Correction needed | Day 14 called itself the first API-collected session and described an interface-to-API transition. | A visible 2026-08-14 corrigendum was added and active Day 14 prose now describes continuation of API-based collection. A renderer freeze marker protects the corrigendum. Counts, outputs, and coded data were not changed. |
| Stale current documentation | README called Day 13 the current verified Pilot record; INDEX called the completed Day 13 report a placeholder and omitted Days 14–15. | README and INDEX now separate the Pilot phase, Paper B freeze, and current Day 15 operational record. |
| Legitimate historical wording | Observation reports and law-update files use “law” terminology and preserve strong or later-withdrawn claims. | Preserved. Current repository-level documentation clarifies that these are provisional, corrigible Pilot claims, not universal laws. |
| Correction needed | Day 12 initially contained a duplicated Claude q003 paste. | Existing correction history is preserved and indexed. The duplication is identified as an input/data-record error, not model behavior. |
| Provenance limitation | Days 1–13 have uneven file preservation. Most lack separate response JSON, exact request/response timestamps, exact provider model identifiers, and request parameters. | Recorded transparently in `paper-b/provenance-matrix.csv`; missing fields are not invented. |
| Preserve unchanged | Raw outputs, anomalous results, withdrawn/refuted claims, correction language, Grok exclusion notes, and incomplete provenance. | Preserved without sanitizing the historical record. |
| Gender-coding risk | Historical reports contain Pilot-era male/female-presenting coding. The current coder extracts entities but does not have a gender field; the reporter could nevertheless reproduce or extend gender claims from names and law text. | Historical outputs remain. A prospective reporter guardrail now prohibits gender inference from names or appearance unless documented public professional identity and a defined protocol are explicitly supplied. No new gender coding was introduced. |
| Disposable technical artifact | No transient cache or generated temp file is tracked in the current tree. | No deletion proposed. |
| Test/placeholder history | Git history contains manually triggered/test Day 14 packets that were removed before the current official Day 14 packet was committed. | Historical commits remain untouched. No test packet exists in the current tree or enters the Paper B 244 count. |

## Repository-tree audit

| Area | Files reviewed | Result |
|---|---|---|
| Repository documentation | `README.md`, `INDEX.md`, `AUTOMATION.md`, `LICENSE` | Boundaries and active terminology corrected; license preserved. |
| Official reports | all 15 root `YYYY-MM-DD-observation.md` files | All discoverable; Day 14 corrected visibly; historical anomalies and claims preserved. |
| Paper B dated data | `2026-05-05/`, `2026-06-16/` | Available files parse/read; provenance limitations recorded. |
| Later Pilot packets | `2026-08-04/`, `2026-08-11/` | Each contains 20 successful responses plus metadata, raw transcript, coding, analysis, and law update; intentionally excluded from Paper B. |
| Automation | `.github/workflows/weekly-record.yml`, `AUTOMATION.md` | Current API workflow preserved; no historical-transition claim retained in active documentation. |
| Collection and reporting code | all files under `scripts/` | Query schedule/config reviewed; generator provenance and prospective gender guardrails added. |
| JSON and CSV | every tracked `.json` and `.csv` | JSON parses; CSV is structurally readable. Automated validation added. |

## Corrections and claim governance

- The Day 12 Claude q003 correction remains visible in the report and is not counted as behavioral duplication.
- Withdrawn Laws IV, V, and X, weakened/nonconfirmed claims, anomalies, and provenance flags remain intact.
- Existing Day 14–15 automated analysis remains explicitly marked as automated draft where the preserved files say so.
- Historical gender-related records remain Pilot-era coding and are not promoted as a central Paper B design-validation case.

## Files proposed for deletion

None.

## Unresolved issues

- Exact request and response timestamps, verified provider model identifiers, request parameters, and standalone raw/structured responses were not preserved consistently for Day 1–Day 13. The audit records these as provenance limitations rather than reconstructing them.
- Historical manual/web-interface provenance statements remain inside original observation artifacts and metadata to avoid silently rewriting the historical record. They must be read together with the repository-level provenance correction.
