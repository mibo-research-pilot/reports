# MIBO Reports

Raw observation records, structured coding artifacts, and longitudinal report summaries for the **Machine Information Behavior Observatory (MIBO)**.

> **Current verified pilot record:** Day 1–Day 12, 2026-05-05 through 2026-07-21  
> **Verified cumulative observations:** 224  
> **Day 13 (`2026-07-28`) status:** placeholder / pending review; excluded from verified counts

---

## What this repository contains

MIBO observes how deployed generative-AI services retrieve, select, rank, recommend, cite, omit, explain, and transmit information over time.

Each verified weekly record may contain:

```text
YYYY-MM-DD-observation.md     Human-readable longitudinal report
YYYY-MM-DD/
├── run_metadata.json         Run and provenance metadata
├── coded-observations.csv    Observation-level coding
├── analysis.json             Machine-readable summary
├── law-updates.md            Claim-status update
└── raw/                      Verbatim responses or transcripts
```

The root-level observation report is the human-readable entry point.  
The date folder is the structured observation packet when that packet has been committed.

See [`INDEX.md`](./INDEX.md) for the verified archive and [`PROVENANCE.md`](./PROVENANCE.md) for record-integrity rules.

---

## What is MIBO?

MIBO is the Machine Information Behavior Observatory.

The Pilot uses **Longitudinal Machine Observation (LMO)**: a fixed set of queries is repeatedly presented to a stable set of public generative-AI services, and the resulting outputs are recorded and compared across synchronized weekly observations.

MIBO does not treat one output as a permanent property of a model. It distinguishes:

- durable canonical selections from peripheral turnover;
- structural product changes from answer-content variation;
- short-lag instability from longer-lag recurrence;
- genuine behavioral evidence from provenance or transcription anomalies;
- confirmed, revised, weakened, withdrawn, and refuted claims.

Methodology and the pilot claim registry live in [`mibo-science/core`](https://github.com/mibo-science/core).  
Versioned query sets live in [`mibo-science/queries`](https://github.com/mibo-science/queries).

---

## Observation phases

### Pilot manual phase

Days 1–13 use or were planned to use manual web-interface collection.

The verified record currently ends at **Day 12**. A blank Day 13 report file exists but is not counted as a completed observation.

For Days 7–12, the recorded observer-facing labels were:

| System | Recorded label / mode |
|---|---|
| OpenAI ChatGPT | GPT 5.5 |
| Anthropic Claude | Claude Opus 4.8 |
| Google Gemini | Gemini 3.5 Flash |
| Perplexity | Perplexity Web Search |

Grok outputs were tested in some workflows but are excluded from the official Day 7–Day 12 observation sets, cumulative counts, and claim-status updates.

### Automated API phase

The repository contains a scheduled GitHub Actions workflow for future API collection. Exact API model IDs must be read from:

- `scripts/observation_config.json`; and
- the relevant `YYYY-MM-DD/run_metadata.json`.

Web-interface labels and API model IDs must not be treated as automatically equivalent.

See [`AUTOMATION.md`](./AUTOMATION.md).

---

## Pilot query set

The verified Day 3–Day 12 Pilot uses five fixed queries.

| ID | Language | Category | Query |
|---|---|---|---|
| q001 | ja | product recommendation | おすすめのプロジェクト管理ツールは？ |
| q002 | en | product recommendation | What is the best CRM for small businesses? |
| q003 | ja | health information | 睡眠の質を上げる方法を教えて |
| q004 | en | technical implementation | How do I implement RAG with a vector database? |
| q005 | ja | named persons | 日本の代表的なAI研究者を5人挙げて |

q001–q003 were used from Day 1. q004–q005 were added at Day 3.

The formal Pilot snapshot is `mibo-science/queries/v0.1.1.json`.

---

## Observation log

| Session | Date | Queries | Included observations | Cumulative | Key findings |
|---|---:|---:|---:|---:|---|
| Day 1 | 2026-05-05 | 3 | 12 | 12 | Baseline; self-contained versus retrieval-mediated divide |
| Day 2 | 2026-05-12 | 3 | 12 | 24 | Canonical selections; temporary abstraction-shift hypothesis |
| Day 3 | 2026-05-19 | 5 | 20 | 44 | q004/q005 added; Day 2 anomaly hypothesis; P12 tested |
| Day 4 | 2026-05-26 | 5 | 20 | 64 | Law IX onset; Day 2 anomaly confirmed; Laws IV/V withdrawn |
| Day 5 | 2026-06-02 | 5 | 20 | 84 | Law X proposed after one-step prediction; later withdrawn |
| Day 6 | 2026-06-09 | 5 | 20 | 104 | Law X reverse prediction failed and was withdrawn |
| Day 7 | 2026-06-16 | 5 | 20 | 124 | First female-presenting main-list inclusions; Law IX 20/20 |
| Day 8 | 2026-06-23 | 5 | 20 | 144 | Five-item q001 core; Zoho family convergence; Law IX 25/25 |
| Day 9 | 2026-06-30 | 5 | 20 | 164 | Stable citation regime with variable URL sets; Law IX 30/30; Law VII 137/140 male-presenting |
| Day 10 | 2026-07-07 | 5 | 20 | 184 | Broad two-session response-state recurrence; Perplexity Day 8 URLs restored 45/45; Law IX 35/35 |
| Day 11 | 2026-07-14 | 5 | 20 | 204 | Twenty-source Perplexity regime begins; q001 shared core contracts; Law IX 40/40; Law VII 175/180 |
| Day 12 | 2026-07-21 | 5 | 20 | 224 | Twenty-source regime persists with 93/100 URL retention; q001 core re-expands; exact CRM canonical three persists; Law IX 45/45; Law VII 195/200 |
| Day 13 | 2026-07-28 | — | — | — | Placeholder only; not verified and not included in cumulative counts |

**Counting convention:** one observation is one included system–query response. Days 1–2 contain 3 queries × 4 systems = 12 observations. Day 3 onward contains 5 queries × 4 included systems = 20 observations.

---

## Current established findings after Day 12

This table is a navigation summary. The authoritative Pilot claim registry is `core/laws.md`.

| Law | Current formulation | Status |
|---|---|---|
| I | Queries can produce durable canonical cores while peripheral selections and rankings fluctuate. | Confirmed with refinements |
| II | Perplexity URL continuity is multi-lag and regime-sensitive. The Day 11 twenty-source regime persisted on Day 12 with 93/100 normalized URLs retained. | Revised / strengthened |
| III | The coordinated Day 2 deviation was a localized anomaly, not a trend or recurring cycle. | Confirmed |
| VI | Systems retain recurring response signatures even when content converges. | Confirmed |
| VII | Japanese-AI-researcher lists remain overwhelmingly male-dominant; female inclusion is rare, intermittent, distributed across more than one model, and person-variable. After Day 12: 195/200 male-presenting. | Strengthened / broadened |
| VIII | No direct peer-reviewed paper or arXiv citation was observed in the verified Pilot through Day 12; public-health and official sources sometimes appeared in Perplexity. | Confirmed with nuance |
| IX | Perplexity has used inline numeric citations plus terminal source lists in every observed query since Day 4: 45/45 after Day 12. | Confirmed / continuing |

Withdrawn laws IV, V, and X remain visible in the claim registry.

---

## Active exploratory candidates

The reports introduced several exploratory propositions. They are not laws.

The most consequential active candidates after Day 12 are:

- **P18** — Session-Wide Response-State Recurrence
- **P23** — Twenty-Source Terminal-List Regime
- **P24** — Cross-System Implementation–Explanation Gap
- **P27** — Shared-Core Re-expansion
- **P28** — Exact-Product Canonical Persistence
- **P29** — Source-Regime Persistence
- **P30** — Cross-Model Exact Response Collision — provenance-sensitive anomaly
- **P31** — Alternation Termination by State Persistence
- **P32** — Stable Source Set with Recommendation Substitution

Candidate status, weakening, supersession, and provenance cautions are recorded in `core/laws.md`.

---

## Provenance and correction policy

A report date is not sufficient by itself to establish capture time.

Every structured observation should distinguish:

- declared observation date;
- actual collection timestamp;
- record-assembly timestamp;
- system and model identifier;
- web interface or API mode;
- observer or automated collector;
- raw-response hash;
- correction status;
- provenance flags.

Two Day 11–Day 12 examples show why this matters:

1. a GPT q004 response contains `2026-08-03`, which postdates the declared weekly observation dates;
2. the supplied Day 12 GPT and Claude q003 texts are identical, and copy-paste duplication cannot be excluded.

Neither item is silently corrected. See [`PROVENANCE.md`](./PROVENANCE.md).

---

## OPEN principles

MIBO Pilot records follow four principles:

- **Observation** — study deployed systems as observable behavioral objects;
- **Parallelism** — collect systems within a synchronized observation window;
- **Embedded openness** — preserve raw outputs, metadata, coding, and corrections;
- **Non-stationarity** — expect models, retrieval systems, interfaces, and source environments to change.

---

## License

Observation data and query sets are released under CC0-1.0 unless otherwise stated.  
Code and software documentation may use Apache-2.0.  
Raw model outputs remain subject to applicable provider terms.

---

Observer: **Kento Sasano**  
Observation began: **2026-05-05**
