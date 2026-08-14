# MIBO Paper B Pilot Evidence Release v1.0.0

**Release status:** `release_candidate`

This is the deterministic archival evidence release candidate for:

**Operationalizing Longitudinal Machine Information Behavior: The Founding and Developmental Pilot of MIBO**

*An Open Resource and Methods Paper*

MIBO — Machine Information Behavioral Observatory — uses repeated, documented elicitation to observe longitudinal machine information behavior. This package preserves the exact historical evidence state used by Paper B; it is not a new analysis, a redesign of the Pilot, or a post-2026-09-01 MIBO Core protocol.

## Evidence boundary

- Day 1 through Day 13 only
- 2026-05-05 through 2026-07-28
- 244 included observations
- `12 + 12 + (11 × 20) = 244`
- API-based continuously from Day 1
- q001–q003 used from Day 1; q004–q005 added on Day 3
- five-query operational instrument: MIBO Pilot query set `v0.1.1`

Later pre-2026-09-01 Pilot observations, including Day 14 and Day 15, remain legitimate MIBO Pilot observations but are intentionally excluded from this Paper B evidence release.

## Repository roles and pinned commits

| Repository | Role | Pinned source commit |
|---|---|---|
| `mibo-research-pilot/core` | Historical conceptual, methodological, and claim-development context | `5f8dc0a21dcc73930f6ebc27cbd67dada3105a0e` |
| `mibo-research-pilot/queries` | Exact versioned Pilot query stimuli and integrity hashes | `49144025fee43b6599892ad0a270c09c518ff815` |
| `mibo-research-pilot/reports` | Paper B observation evidence, corrections, and provenance | evidence source `005b98c55158e95c71b1f4d963c04d4dcf2fd5f0` |

The final release-preparation commit is not self-embedded in package metadata. It will be recorded externally in tag and GitHub Release metadata after review and merge.

## Package layout

- `core-context/` — complete tracked snapshot of the pinned Core commit, excluding `.git`;
- `query-instrument/` — complete tracked snapshot of the pinned Queries commit, including historical version artifacts;
- `reports-evidence/` — only the Day 1–Day 13 evidence paths selected by the existing reports manifest, plus its integrity manifest;
- top-level release metadata — boundary, source locks, file manifest, outer hashes, rights notes, and citation/deposit drafts.

## Integrity verification

1. Parse `RELEASE_LOCK.json` and confirm the three pinned commits.
2. Verify `MANIFEST.json` entries against the corresponding bundle files.
3. Verify every entry in the outer `SHA256SUMS.json` against the exact file bytes. The outer manifest intentionally does not hash itself.
4. Within `reports-evidence/`, verify `paper-b/SHA256SUMS.json` using its documented CRLF-to-LF canonical-text rule.
5. Within `query-instrument/`, verify `HASHES.json` and the ordered instrument SHA-256 `8463f51cf40bd0e2b7186569cdb84e26085ad16f6c62e7035c1a1c59311cdd35`.
6. Re-run `scripts/build_paper_b_release.py` from the reports release repository with the same pinned Git objects; two builds must produce the same ZIP SHA-256.

`MANIFEST.json` enumerates payload files. It cannot include the exact byte hash of itself or the outer hash manifest without circularity. The outer `SHA256SUMS.json` hashes `MANIFEST.json` and every other bundle file except itself.

## Provenance limitations

The package preserves `reports-evidence/paper-b/provenance-matrix.csv`. Missing request or response timestamps, exact provider-returned model identifiers, request parameters, standalone raw responses, structured responses, or citation evidence are not reconstructed. Values such as `partial` and `absent` describe preservation status; they do not make the surviving observation invalid.

## Correction-history principle

Historical evidence is not silently sanitized. The release preserves corrections, withdrawals, weakening, revision, refutation, and anomalies. Pilot collection was API-based continuously from Day 1. The Day 12 duplicated Claude q003 record was an input/data-record problem, not model behavior. Day 14 is outside this release, and the former false description of Day 14 as the first API session is not propagated as current fact. Grok exclusions remain as recorded for Day 7–Day 13.

## Citation status

Author: Kento Sasano

ORCID: `0009-0009-3853-8029`

Affiliations:

1. Okayama University, Okayama, Japan
2. Keio Research Institute at SFC, Keio University, Fujisawa, Japan

After a DOI is assigned, cite the exact archived release and Paper B using the final release metadata. At release-candidate stage no DOI or arXiv identifier has been assigned, and no publication status is asserted.
