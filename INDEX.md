# MIBO Pilot observation index

This index lists every preserved official observation report. Artifact completeness varies by Day and is reported without assuming that missing files once existed. See [`paper-b/provenance-matrix.csv`](./paper-b/provenance-matrix.csv).

## Paper B included observations

| Day | Date | Report | Included observations | Cumulative | Record note |
|---:|---:|---|---:|---:|---|
| 1 | 2026-05-05 | [`2026-05-05-observation.md`](./2026-05-05-observation.md) | 12 | 12 | Human-readable report plus run metadata; historical collection-mode wording is superseded by the repository provenance correction |
| 2 | 2026-05-12 | [`2026-05-12-observation.md`](./2026-05-12-observation.md) | 12 | 24 | Human-readable report; no separate structured packet preserved |
| 3 | 2026-05-19 | [`2026-05-19-observation.md`](./2026-05-19-observation.md) | 20 | 44 | Human-readable report; q004–q005 begin |
| 4 | 2026-05-26 | [`2026-05-26-observation.md`](./2026-05-26-observation.md) | 20 | 64 | Human-readable report |
| 5 | 2026-06-02 | [`2026-06-02-observation.md`](./2026-06-02-observation.md) | 20 | 84 | Human-readable analytical report; no separate raw packet preserved |
| 6 | 2026-06-09 | [`2026-06-09-observation.md`](./2026-06-09-observation.md) | 20 | 104 | Human-readable analytical report; Law X withdrawal preserved |
| 7 | 2026-06-16 | [`2026-06-16-observation.md`](./2026-06-16-observation.md) | 20 | 124 | Partial structured packet preserved; Grok excluded from official count |
| 8 | 2026-06-23 | [`2026-06-23-observation.md`](./2026-06-23-observation.md) | 20 | 144 | Human-readable analytical report; no separate structured packet preserved |
| 9 | 2026-06-30 | [`2026-06-30-observation.md`](./2026-06-30-observation.md) | 20 | 164 | Human-readable analytical report; no separate structured packet preserved |
| 10 | 2026-07-07 | [`2026-07-07-observation.md`](./2026-07-07-observation.md) | 20 | 184 | Human-readable analytical report; no separate structured packet preserved |
| 11 | 2026-07-14 | [`2026-07-14-observation.md`](./2026-07-14-observation.md) | 20 | 204 | Human-readable report with provenance flags |
| 12 | 2026-07-21 | [`2026-07-21-observation.md`](./2026-07-21-observation.md) | 20 | 224 | Corrected Claude q003 record preserved; duplicate was a data-record error, not model behavior |
| 13 | 2026-07-28 | [`2026-07-28-observation.md`](./2026-07-28-observation.md) | 20 | 244 | Complete human-readable Paper B boundary report; no separate structured packet preserved |

## Later MIBO Pilot observations outside Paper B

| Day | Date | Report | Structured packet | Included observations | Cumulative | Record note |
|---:|---:|---|---|---:|---:|---|
| 14 | 2026-08-04 | [`2026-08-04-observation.md`](./2026-08-04-observation.md) | [`2026-08-04/`](./2026-08-04/) | 20 | 264 | Complete packet; report carries the 2026-08-14 API-provenance corrigendum |
| 15 | 2026-08-11 | [`2026-08-11-observation.md`](./2026-08-11-observation.md) | [`2026-08-11/`](./2026-08-11/) | 20 | 284 | Latest preserved Pilot packet; automated coding remains explicitly marked as draft |

Day 13 / 244 is the Paper B evidence freeze, not the end of the Pilot. The term “law” in historical records is Pilot-era terminology for provisional and corrigible longitudinal claims.

No current-tree test, mock, or placeholder observation is indexed as official. Test records visible only in Git history remain outside official counts.
