# Paper B evidence freeze

This directory records a frozen evidence boundary within the live historical MIBO Pilot repository. It is not a copied or separate dataset.

- Included range: Day 1–Day 13
- First date: 2026-05-05
- Freeze date: 2026-07-28
- Included observations: 244
- Collection mode: API, continuously from Day 1
- Five-query operational portion: query-set `v0.1.1` from Day 3 onward

The count is `12 + 12 + (11 × 20) = 244`: Days 1–2 contain q001–q003 across four systems; Days 3–13 contain q001–q005 across four included systems. Grok is excluded from official Day 7–Day 13 analyses and counts.

Day 14 and later pre-2026-09-01 records remain MIBO Pilot observations but are intentionally outside Paper B. The source repository remains the live, correction-preserving historical Pilot repository.

**Model metadata correction — 11 October 2026:** the investigator has confirmed unchanged selection and designated the initial collector configuration as the correct model notation for Days 1–13. The corrected selected IDs are `gpt-5.5`, `claude-opus-4-8`, `gemini-3.5-flash`, and `sonar`. Earlier report-header labels are superseded metadata. This correction does not authenticate each historical request. See [MODEL_SELECTION_CORRECTION.md](./MODEL_SELECTION_CORRECTION.md).

Files in this directory:

- [`evidence-manifest.json`](./evidence-manifest.json) — machine-readable boundary, counts, inclusions, exclusions, corrections, and source paths;
- [`provenance-matrix.csv`](./provenance-matrix.csv) — per-Day artifact and metadata availability;
- [`SHA256SUMS.json`](./SHA256SUMS.json) — SHA-256 values for the intentionally identified Paper B evidence-release files.

Missing metadata is reported as absent or not assessable. It is not reconstructed or inferred.

- [model-selection.json](./model-selection.json) — investigator-confirmed selected-model metadata correction, separate from the preserved per-Day transaction records.
