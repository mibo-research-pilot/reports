# MIBO Paper B Pilot Evidence Release v1.0.0

**Status:** Release candidate; not published and not DOI-assigned.

## Purpose

This deterministic archival bundle preserves the historical MIBO Pilot evidence state accompanying *Operationalizing Longitudinal Machine Information Behavior: The Founding and Developmental Pilot of MIBO*.

## Evidence boundary

- Day 1–Day 13 only
- 2026-05-05 through 2026-07-28
- 244 included observations: `12 + 12 + (11 × 20) = 244`
- API-based continuously from Day 1
- later Pilot observations excluded from this release

## Pinned sources

- Core: `5f8dc0a21dcc73930f6ebc27cbd67dada3105a0e`
- Queries: `49144025fee43b6599892ad0a270c09c518ff815`
- Reports evidence source: `005b98c55158e95c71b1f4d963c04d4dcf2fd5f0`
- MIBO Pilot query set v0.1.1 ordered instrument SHA-256: `8463f51cf40bd0e2b7186569cdb84e26085ad16f6c62e7035c1a1c59311cdd35`

## Integrity

The existing reports evidence manifest is preserved and verified. The outer manifest covers release metadata, the complete pinned Core and Queries snapshots, and the selected reports evidence subset. The outer `SHA256SUMS.json` does not hash itself.

The deterministic ZIP SHA-256 is reported externally in the Draft PR and workflow result. It cannot be embedded inside the ZIP without changing the ZIP's own digest. The hash of the outer `SHA256SUMS.json` is likewise reported by the build.

## Provenance and corrections

Incomplete historical timestamps, provider identifiers, parameters, raw responses, structured responses, and citation evidence remain explicitly partial or absent. They are not reconstructed. Correction and withdrawal history is retained, including the Day 12 Claude q003 input/data-record correction, Grok exclusions, and API-from-Day-1 correction context. Later Pilot observations are excluded, not deleted or invalidated.

## Rights caveat

Source-specific licenses and limitations are documented in `RIGHTS_AND_LICENSES.md`. Embedded model-generated and third-party material requires human rights review before Zenodo publication. No DOI is available at release-candidate stage.
