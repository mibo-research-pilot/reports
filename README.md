# MIBO Reports

**Repository:** `mibo-research-pilot/reports`

Raw API observation records, structured coding artifacts, and longitudinal report summaries for the **Machine Information Behavior Observatory (MIBO)**.

> **Current verified pilot record:** Day 1–Day 13, 2026-05-05 through 2026-07-28  
> **Verified cumulative observations:** 244

---

## What this repository contains

MIBO observes how deployed generative-AI systems retrieve, select, rank, recommend, cite, omit, explain, and transmit information over time.

Each weekly record may contain:

```text
YYYY-MM-DD-observation.md     Human-readable longitudinal report
YYYY-MM-DD/
├── run_metadata.json         Run and API-observation metadata
├── coded-observations.csv    Observation-level coding
├── analysis.json             Machine-readable summary
├── law-updates.md            Claim-status update
└── raw/                      Verbatim response records when preserved
```

The root-level observation report is the human-readable entry point.  
The date folder is the structured observation packet.

---

## What is MIBO?

MIBO is the Machine Information Behavior Observatory.

The Pilot uses **Longitudinal Machine Observation (LMO)**: a fixed, versioned query set is repeatedly submitted through APIs to a stable set of identified generative-AI system lineages, and the resulting outputs are recorded and compared across synchronized weekly observations.

MIBO does not treat one output as a permanent property of a model. It distinguishes:

- durable canonical selections from peripheral turnover;
- structural product changes from answer-content variation;
- short-lag instability from longer-lag recurrence;
- model behavior from transcription or data-entry corrections;
- confirmed, revised, weakened, withdrawn, and refuted claims.

Methodology and the Pilot claim registry live in [`mibo-research-pilot/core`](https://github.com/mibo-research-pilot/core).  
Versioned query sets live in [`mibo-research-pilot/queries`](https://github.com/mibo-research-pilot/queries).

---

## Collection mode

MIBO observations have been conducted through APIs continuously since **Day 1 (2026-05-05)**.

Each run should preserve, where available:

- provider and system lineage;
- exact model identifier or recorded model label;
- API request and response timestamps;
- query-set version;
- request parameters;
- raw response;
- normalized response hash;
- correction status.

For Days 7–13, the recorded labels used in the observation files are:

| System | Recorded label / mode |
|---|---|
| OpenAI ChatGPT | GPT 5.5 |
| Anthropic Claude | Claude Opus 4.8 |
| Google Gemini | Gemini 3.5 Flash |
| Perplexity | Perplexity Web Search |

Grok and all Grok outputs are excluded from the official Day 7–Day 13 observation sets, cumulative counts, and claim-status updates.

---

## Pilot query set

The verified Day 3–Day 13 Pilot uses five fixed queries.

| ID | Language | Category | Query |
|---|---|---|---|
| q001 | ja | product recommendation | おすすめのプロジェクト管理ツールは？ |
| q002 | en | product recommendation | What is the best CRM for small businesses? |
| q003 | ja | health information | 睡眠の質を上げる方法を教えて |
| q004 | en | technical implementation | How do I implement RAG with a vector database? |
| q005 | ja | named persons | 日本の代表的なAI研究者を5人挙げて |

q001–q003 were used from Day 1. q004–q005 were added at Day 3.

The formal Pilot snapshot is `mibo-research-pilot/queries/v0.1.1.json`.

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
| Day 9 | 2026-06-30 | 5 | 20 | 164 | Stable citation regime with variable URL sets; Law IX 30/30; Law VII 137/140 |
| Day 10 | 2026-07-07 | 5 | 20 | 184 | Broad two-session response-state recurrence; Perplexity Day 8 URLs restored 45/45; Law IX 35/35 |
| Day 11 | 2026-07-14 | 5 | 20 | 204 | Twenty-source Perplexity regime begins; q001 shared core contracts; Law IX 40/40; Law VII 175/180 |
| Day 12 | 2026-07-21 | 5 | 20 | 224 | Twenty-source regime persists with 93/100 URL retention; q001 core re-expands; CRM canonical three persists; Law IX 45/45; Law VII 195/200 |
| Day 13 | 2026-07-28 | 5 | 20 | 244 | Law IX 50/50; twenty-source regime 15/15; q001 core contracts; q003 nap advice 4/4; q004 gap 4/4; Law VII 215/220 |

**Counting convention:** one observation is one included system–query response. Days 1–2 contain 3 queries × 4 systems = 12 observations. Day 3 onward contains 5 queries × 4 included systems = 20 observations. Cumulative after Day 13 = 244.

---

## Current established findings after Day 13

This table is a navigation summary. The authoritative Pilot claim registry is maintained in `core/laws.md`.

| Law | Current formulation | Status |
|---|---|---|
| I | Queries can produce durable canonical cores while peripheral selections and rankings fluctuate. | Confirmed with refinements |
| II | Perplexity URL continuity is multi-lag and regime-sensitive. Day 13 retains 18/20 q001, 19/20 q004, and 19/20 q005 URLs from Day 12; q001 and q004 return to their complete Day 11 terminal source sets. | Continuing |
| III | The coordinated Day 2 deviation was a localized anomaly, not a trend or recurring cycle. | Confirmed |
| VI | Systems retain recurring response signatures even when content converges. | Confirmed |
| VII | Japanese-AI-researcher lists remain overwhelmingly male-dominant. After Day 13: 215/220 male-presenting and 5/220 female-presenting main-list mentions. | Strengthened / broadened |
| VIII | No direct peer-reviewed paper or arXiv citation was observed in the Pilot through Day 13; public-health, official, technical, and institutional web sources sometimes appeared in Perplexity. | Confirmed with nuance |
| IX | Perplexity has used inline numeric citations plus terminal source lists in every observed query since Day 4: 50/50 after Day 13. The twenty-source terminal-list regime covers 15/15 observations across Days 11–13. | Confirmed / continuing |

Withdrawn Laws IV, V, and X remain visible in the claim registry.

---

## Active exploratory candidates

The reports introduced exploratory propositions. They are not laws.

- **P18** — Session-Wide Response-State Recurrence
- **P23** — Twenty-Source Terminal-List Regime
- **P24** — Cross-System Implementation–Explanation Gap
- **P27** — Shared-Core Elasticity
- **P28** — Exact-Product Canonical Persistence — bounded to Days 11–12
- **P29** — Source-Regime Persistence
- **P30** — Alternation Termination by State Persistence
- **P31** — Stable Source Set with Recommendation Substitution
- **P32** — Granularity-Dependent Convergence
- **P33** — Advice-Slot Convergence without Parameter Convergence
- **P34** — Source-State Recurrence without Response-State Recurrence

Candidate status, weakening, supersession, and correction notes are maintained in the claim registry.

---

## Correction and record-integrity policy

Observation records must distinguish model behavior from later data correction.

The Day 12 correction record remains part of the archive:

1. the initial duplicated Claude q003 paste was superseded by the correct Claude response;
2. the GPT q004 example metadata date was aligned to the Day 12 observation date, `2026-07-21`;
3. neither correction is treated as model behavior or an unresolved provenance anomaly.

Day 13 contains no unresolved correction that changes its 20-observation count.

General rules:

- preserve raw records where available;
- record corrections explicitly rather than silently rewriting behavioral claims;
- use normalized URLs—not citation indices—for longitudinal source matching;
- keep product-level and vendor-family-level coding distinct;
- keep main-list mentions distinct from supplementary mentions;
- do not infer capture time from an example date embedded in generated content.

---

## OPEN principles

MIBO Pilot records follow four principles:

- **Observation** — study deployed systems as observable behavioral objects;
- **Parallelism** — observe included systems within a synchronized window;
- **Embedded openness** — preserve outputs, metadata, coding, and corrections;
- **Non-stationarity** — expect models, retrieval systems, interfaces, APIs, and source environments to change.

---

## License

Observation data and query sets are released under CC0-1.0 unless otherwise stated.  
Code and software documentation may use Apache-2.0.  
Raw model outputs remain subject to applicable provider terms.

---

Observer: **Kento Sasano**  
Observation began: **2026-05-05**
