# reports

Raw observation data and weekly reports for the **Machine Information Behavior Observatory (MIBO)**.

---

## What is MIBO?

MIBO is the Machine Information Behavior Observatory — a research institution that continuously observes how generative AI systems retrieve, select, communicate, and forget information. The first focus is **source-attribution and citation-like behavior**: when and how AI systems point to sources, and how that behavior changes over time.

MIBO conducts **Longitudinal Machine Observation (LMO)**: the same fixed set of queries is put to the same set of deployed AI systems every week, and the responses are recorded verbatim. Where a benchmark photographs a system once and scores it, an observatory watches the same system over time and can tell when it moves — distinguishing durable behavior from week-to-week noise, and timestamping product changes from the outside.

This repository holds the raw weekly reports. Methodology lives in [`mibo-science/core`](https://github.com/mibo-science/core); the standard query set lives in [`mibo-science/queries`](https://github.com/mibo-science/queries).

---

## The OPEN principles

MIBO observations follow four principles, abbreviated **OPEN**:

- **Observation** — study deployed systems in the field, as ordinary users encounter them, rather than lab-only probes.
- **Parallelism** — query all systems within a synchronized window, so cross-model differences are not confounded by time.
- **Embedded openness** — publish the full record (queries, raw responses, analysis) so anyone can re-examine it.
- **Non-stationarity** — treat AI behavior as a moving target, observed repeatedly over time rather than measured once.

Together these make findings **re-observable** — a complement to reproducibility suited to systems that change underneath you.

---

## Models observed

| System | Model (as of Day 5) |
|--------|---------------------|
| OpenAI ChatGPT | GPT-5.4 |
| Anthropic Claude | claude-opus-4-7 |
| Google Gemini | Gemini 3.0 Flash |
| Perplexity | Web search mode |

Three are self-contained (answer from internal knowledge); Perplexity is retrieval-augmented (answers from live web search with citations).

---

## Standard query set (v0.1)

| ID | Language | Category | Query |
|----|----------|----------|-------|
| q001 | ja | product_recommendation | おすすめのプロジェクト管理ツールは？ |
| q002 | en | product_recommendation | What is the best CRM for small businesses? |
| q003 | ja | health | 睡眠の質を上げる方法を教えて |
| q004 | en | technical | How do I implement RAG with a vector database? |
| q005 | ja | people / named entities | 日本の代表的なAI研究者を5人挙げて |

q001–q003 have been observed since Day 1; q004–q005 were added at Day 3.

---

## Observation log

| Session | Date | Queries | Observations | Cumulative | Key findings |
|---------|------|:-------:|:------------:|:----------:|--------------|
| Day 1 | 2026-05-05 | 3 | 12 | 12 | Baseline; self-contained vs retrieval-augmented divide |
| Day 2 | 2026-05-12 | 3 | 12 | 24 | Canonical-3; parallel abstraction shift (P12) hypothesized |
| Day 3 | 2026-05-19 | 5 | 20 | 44 | q004/q005 added; Day 2 Anomaly hypothesis; P12 refuted; Law VII baseline |
| Day 4 | 2026-05-26 | 5 | 20 | 64 | Day 2 Anomaly confirmed (H1); Law IX new; Law IV/V withdrawn |
| Day 5 | 2026-06-02 | 5 | 20 | 84 | Law X (biweekly) confirmed by prediction; Law IX longitudinal; Law VII 60 obs; P12 final refutation |

**Counting convention**: *session* = one weekly round; *observation* = one model-query response. Day 1–2 used 3 queries (12 observations each); Day 3 onward use 5 queries (20 observations each). Cumulative after Day 5 = 84.

---

## Established laws

A finding becomes a numbered "law" only after it survives at least four weekly observations and continued verification. Laws remain provisional and are revised or withdrawn when later data contradicts them. Gaps in the numbering (IV, V) mark withdrawn laws — kept visible on purpose, because retraction is part of the method.

| Law | Statement | Status |
|-----|-----------|--------|
| **I** | **Absolute Canonical.** A small set of products/names appears in essentially every response to a given query. q001 Asana 20/20; q002 HubSpot/Zoho/Pipedrive 20/20; q005 Matsuo Yutaka 12/12 mentions. *Refinement:* even "absolute" canonical can lapse in a single model (Trello 19/20, Pinecone 11/12, Matsuo #1 11/12 — each a single Day 5 lapse). | Confirmed (5 wk) |
| **II** | **Perplexity URL Stability.** Perplexity's cited URLs persist week to week at a high rate (band ~71–100%). Lost URLs often go dormant and resurface later. | Confirmed (5 wk) |
| **III** | **Day 2 Anomaly.** On 2026-05-12, several content features deviated together and reverted by Day 3 — a single localized common anomaly, not a recurring cycle. Evidence re-selected at Day 5 to elements stable across all 5 points (GPT-5.4 medical-section name; Perplexity boxil.jp path). | Confirmed (H1) |
| **VI** | **Per-Model Signature.** Each model carries stable stylistic fingerprints — e.g. GPT-5.4's closing refinement offer (18/18 across q001–q004; unstable only on q005), and per-model evaluation vocabularies (GPT-5.4 IR-classical Recall@k/MRR/nDCG vs Gemini RAG-specific RAGAS/TruLens). | Confirmed |
| **VII** | **Gender Bias in Person Queries.** Across 4 models × 3 weeks × 5 names, all 60 main-list mentions of "representative Japanese AI researchers" were male. The sole female mention anywhere is Arai Noriko, in Claude's supplementary section, present all 3 weeks. | Strengthened (60 obs) |
| **VIII** | **Universal Absence of Academic Citations.** Across all domains and 5 weeks, Perplexity cited zero academic papers / arXiv. *Nuance:* Claude referenced its own company's research (Anthropic "contextual retrieval") in body text, not as a URL. | Confirmed (5 wk) |
| **IX** | **Perplexity Inline Citation Shift.** From Day 4, Perplexity attaches inline [n] citation numbers to individual claims in the response body (Days 1–3 used end-of-response bulk citation only). Present in all 5 queries on Day 4 and Day 5 (10 observations), deepened into comparison-table cells. A permanent product change, with onset timestamped to between Day 3 and Day 4. | Confirmed (longitudinal) |
| **X** | **GPT-5.4 Product-Slot Biweekly Pattern.** Certain edge-of-list product mentions in GPT-5.4 alternate with the parity of the week, in anti-phase: Backlog (q001) ✗✓✗✓✗, Salesforce (q002) ✓✗✓✗✓. Established by predicting Day 5 (odd week) in advance and confirming both. Limited to product boundary slots (section count did not follow the pattern); GPT-5.4-specific. | Established by prediction |

### Withdrawn

| Law | Statement | Why withdrawn |
|-----|-----------|---------------|
| ~~IV~~ | Vendor-Official URL Ascendancy | The apparent monotonic rise (43→57→71%) was a 3-point artifact; returned to 43% at Days 4–5. |
| ~~V~~ | Perplexity Compression | No consistent trend across queries; product/numeric counts fluctuate without direction. |

### Refuted hypothesis

- **P12 (Parallel Abstraction Shift)** — definitively refuted at 5 points × 3 self-contained models (15 data points). Only Day 2 showed reduced numeric specificity; all other weeks held baseline. The most-tested refuted hypothesis in MIBO.

---

## License

Observation data is released under [CC0-1.0](LICENSE) (public domain dedication). The records are meant to be re-observed and reused freely.

---

*Observer: Kento Sasano — Machine Behavioral Scientist · GEO/LLMO Researcher · Founder of MIBO. Observation began 2026-05-05.*
