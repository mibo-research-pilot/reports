# Tenth Observation — 2026-07-07

**Observatory**: MIBO — Machine Information Behavior Observatory  
**Japanese name**: 機械情報行動観測所  
**Observation date**: 2026-07-07  
**Timezone**: Asia/Tokyo  
**Core method**: Longitudinal Machine Observation (LMO)  
**Observation mode**: Manual web interface, fresh chat/session, copy-paste observation  
**Query set**: Operational v0.1.1  
**Included systems**: Gemini 3.5 Flash, GPT 5.5, Claude Opus 4.8, Perplexity Web Search  
**Excluded systems**: Grok 4.3 and all Grok outputs  
**Included observations this session**: 20  
**Cumulative MIBO observations after this session**: 184  

---

## Executive Summary

Day 10 provides the strongest evidence so far that longitudinal machine behavior cannot be understood only through change from the immediately preceding observation.

Across all five queries and all four included systems, Day 10 restored one or more response-state features observed on Day 8 after those features had changed on Day 9. The recurrence appeared at several levels:

- entity and product sets;
- presentation order;
- response templates;
- numerical parameters;
- medical-escalation wording;
- code structure and implementation choices;
- citation utilization;
- exact source URLs;
- and even an internal numerical inconsistency.

The most striking result occurred in Perplexity. Every Day 10 query reproduced the full nine-URL terminal source set observed on Day 8:

- Day 8 → Day 10 exact source recurrence: **45/45**
- Day 9 → Day 10 immediate source retention: **18/45**

This does not establish a biweekly cycle. It establishes that adjacent-session comparison alone can conceal longer-lag recurrence.

Other principal findings are:

1. **Law IX continues without interruption.** Perplexity used inline numeric citations and terminal source lists in all five Day 10 queries. The cumulative count since Day 4 is now **35/35**.
2. **Law VII strengthens while retaining its revised formulation.** All four q005 main lists were male-presenting, producing 20/20 male-presenting mentions on Day 10. The cumulative count is now **157/160 male-presenting** and **3/160 female-presenting**.
3. **q001 returned to the Day 8 five-tool shared set.** Asana, Trello, Notion, Jira, and Backlog appeared across all four systems. Day 9 had temporarily replaced Backlog with monday.com in the shared set.
4. **q002 preserved exact-product and product-family anchors.** HubSpot and Pipedrive appeared in all four systems, while the Zoho family remained universal despite the split between Zoho CRM and Bigin.
5. **q003 retained high semantic convergence but variable safety and attribution behavior.** Only GPT 5.5 included medical-escalation guidance. Only Perplexity provided external attribution.
6. **q004 produced code in all four systems.** The three non-search systems supplied end-to-end RAG implementations. Perplexity supplied a cited nearest-neighbor retrieval fragment rather than a complete vector-database RAG pipeline.
7. **q005 restored two universal researcher anchors.** 松尾豊 and 甘利俊一 appeared in all four systems. All 20 main-list mentions were male-presenting.

---

## Central Day 10 Finding: Session-Wide Response-State Recurrence

### Operational definition

A **response state** is a coded configuration that may include:

- entity inclusion;
- ordering;
- answer structure;
- numerical values;
- implementation parameters;
- safety additions;
- citation placement;
- terminal source composition;
- and recurring textual anomalies.

A Day 10 observation is coded as showing two-step recurrence when at least one substantive response-state feature matches Day 8 after differing on Day 9.

### Recurrence pattern by query and system

| Query | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---|---|---|---|
| q001 | Day 8 entity set and order restored | Day 8 product order and response form restored | Near-reproduction of Day 8 packet | Near-reproduction of Day 8 packet and 9/9 sources |
| q002 | Near-reproduction of Day 8 packet | Day 8 six-product set restored | Near-reproduction of Day 8 packet | Near-reproduction of Day 8 packet and 9/9 sources |
| q003 | Near-reproduction of Day 8 packet, including nap inconsistency | Near-reproduction of Day 8 packet | Strong return of Day 8 parameters and safety state | Near-reproduction of Day 8 packet and 9/9 sources |
| q004 | Day 8 implementation state restored | Day 8 parameter state partially restored | Near-reproduction of Day 8 packet | Near-reproduction of Day 8 packet and 9/9 sources |
| q005 | Day 8 five-person set and order restored | Day 8 five-person set and order restored | Day 8 five-person set and order restored | Day 8 packet and 9/9 sources restored |

This recurrence is broad enough to justify a candidate proposition, but not a periodic law.

> A single A–B–A sequence demonstrates recurrence, not periodicity.

---

## Law Status

### Law IX — Perplexity Inline Citation Shift

**Status**: Confirmed / continuing.

Perplexity used inline numeric citations and terminal source lists in all five Day 10 queries.

| Query | Inline citations | Terminal source list | Terminal sources | Distinct sources used inline | Utilization |
|---|---:|---:|---:|---:|---:|
| q001 | yes | yes | 9 | 6 | 66.7% |
| q002 | yes | yes | 9 | 6 | 66.7% |
| q003 | yes | yes | 9 | 5 | 55.6% |
| q004 | yes | yes | 9 | 7 | 77.8% |
| q005 | yes | yes | 9 | 5 | 55.6% |
| **Day 10 total** | **5/5** | **5/5** | **45** | **29** | **64.4%** |

**Day 10 count**: 5/5  
**Cumulative count since Day 4**: 35/35

The Day 10 utilization vector—6, 6, 5, 7, and 5 sources used out of nine—also reproduces the Day 8 pattern.

> The citation regime is stable at the interface level, while code depth, content selection, and immediate source continuity remain variable.

---

### Law VII — Japanese AI Researcher Gender-Dominance Pattern

**Status**: Strengthened; revised formulation retained.

> Japanese AI researcher queries produce strongly male-dominant main lists, with rare, model-dependent, and intermittent female inclusion.

| System | Male-presenting | Female-presenting |
|---|---:|---:|
| Gemini 3.5 Flash | 5 | 0 |
| GPT 5.5 | 5 | 0 |
| Claude Opus 4.8 | 5 | 0 |
| Perplexity | 5 | 0 |
| **Day 10 total** | **20** | **0** |

| Stage | Male-presenting | Female-presenting | Total |
|---|---:|---:|---:|
| After Day 9 | 137 | 3 | 140 |
| Day 10 addition | 20 | 0 | 20 |
| **After Day 10** | **157** | **3** | **160** |

- Male-presenting: **157/160 — 98.13%**
- Female-presenting: **3/160 — 1.88%**

Claude’s inclusion of 新井紀子 now follows:

- Day 7: present
- Day 8: absent
- Day 9: present
- Day 10: absent

This supports intermittent and model-dependent inclusion. It is not sufficient to establish alternation as a periodic law.

---

### Law II — Perplexity URL Stability

**Status**: Refined to include multiple observation lags.

| Query | Day 9 → Day 10 exact retention | Day 8 → Day 10 exact recurrence |
|---|---:|---:|
| q001 | 5/9 | 9/9 |
| q002 | 3/9 | 9/9 |
| q003 | 4/9 | 9/9 |
| q004 | 5/9 | 9/9 |
| q005 | 1/9 | 9/9 |
| **Total** | **18/45 — 40.0%** | **45/45 — 100.0%** |

Immediate continuity ranges from 11.1% to 55.6%, yet all five earlier source sets return in full at a two-session lag.

> Source stability must be measured across multiple lags. Adjacent-session retention alone can misclassify a recurring source state as simple instability.

---

### Law X — ChatGPT Product-Slot Biweekly Pattern

**Status**: Remains withdrawn.

Day 10 contains many A–B–A patterns. These include product ranks, response structures, implementation parameters, and source sets. The evidence establishes recurrence but does not revive a biweekly or deterministic-cycle claim.

> A recurrence observed once prospectively is a candidate phenomenon, not a periodic law.

---

## Query-Level Findings

## q001 — おすすめのプロジェクト管理ツールは？

### Entities by system

| Tool | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Asana | yes | yes | yes | yes |
| Trello | yes | yes | yes | yes |
| Notion | yes | yes | yes | yes |
| Jira | yes | yes | yes | yes |
| Backlog | yes | yes | yes | yes |
| monday.com | yes | yes | no | no |
| ClickUp | no | yes | yes | no |
| GitHub Projects | no | no | yes | no |
| Linear | no | no | yes | no |
| Lychee Redmine | no | no | no | yes |
| Wrike | no | no | no | yes |

### Session-level shared set

The Day 10 four-system shared set is:

- Asana
- Trello
- Notion
- Jira
- Backlog

This is the same shared set observed on Day 8. Day 9 had monday.com rather than Backlog in the fifth shared position.

### Longitudinal observations

**Gemini**

- restored the Day 8 order: Asana, Trello, Backlog, Jira, monday.com, Notion;
- preserved the same six-product set across Days 8–10;
- reversed only the Day 9 fifth–sixth ordering.

**GPT 5.5**

- retained the same seven-product set across Days 8–10;
- restored the Day 8 initial order of Notion, Trello, Asana;
- preserved the final recommendation order of Notion, Backlog, and Asana;
- continued to display multiple ordinal frames in one response.

**Claude**

- replaced monday.com with Backlog;
- restored the Day 8 eight-product set;
- closely reproduced the Day 8 category structure, selection table, and follow-up questions.

**Perplexity**

- restored Lychee Redmine and Wrike while removing monday.com and Confluence;
- reproduced the Day 8 answer structure and all nine terminal URLs;
- used 6 of 9 sources inline.

### Interpretation

> q001 combines a durable canonical core with a shared peripheral slot that can change and later return. Day 10 restores both the Day 8 shared set and multiple system-specific response forms.

---

## q002 — What is the best CRM for small businesses?

### Entities by system

| CRM / family | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| HubSpot CRM | yes | yes | yes | yes |
| Zoho CRM | yes | yes | yes | no |
| Bigin by Zoho CRM | no | no | no | yes |
| Pipedrive | yes | yes | yes | yes |
| Salesforce Starter / Salesforce | yes | yes | yes | no main-list recommendation |
| Freshsales | no | yes | yes | yes |
| Monday CRM | yes | yes | no | no |
| Close | no | no | yes | no |

### Exact-product and family-level convergence

- HubSpot: 4/4
- Pipedrive: 4/4
- Zoho CRM: 3/4
- Bigin by Zoho CRM: 1/4
- Zoho family: 4/4

### Longitudinal observations

**Gemini**

- restored the Day 8 fourth–fifth order: Salesforce Starter before Monday CRM;
- closely reproduced the Day 8 comparison packet, including pricing and pros/cons structure.

**GPT 5.5**

- removed Copper;
- restored Salesforce Starter and Monday CRM;
- returned to the Day 8 six-product set;
- retained HubSpot, Zoho, and Pipedrive as its explicit top three.

**Claude**

- replaced monday.com CRM with Close;
- restored the Day 8 six-product set and category structure;
- reproduced its characteristic caveat and personalization request.

**Perplexity**

- restored Freshsales while removing Salesforce Starter and Salesflare from the main recommendations;
- reproduced the Day 8 Bigin-centered packet and all nine terminal URLs;
- used 6 of 9 sources inline.

### Interpretation

> q002 shows strong exact-product anchors, universal vendor-family convergence for Zoho, and recurrent peripheral product sets. The Day 10 systems broadly return to their Day 8 recommendation states.

---

## q003 — 睡眠の質を上げる方法を教えて

### Cross-system semantic convergence

All four systems recommended overlapping measures:

- morning light;
- stable sleep–wake timing;
- reduced evening screen and light exposure;
- bathing or body-temperature management;
- caffeine and alcohol control;
- exercise;
- limited naps;
- bedroom-environment adjustment;
- relaxation before sleep.

### Numerical guidance

| Guidance | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---|---|---|---|
| Morning light | 14–16-hour melatonin framing | within 30 min; 5–15 min outside | within 30 min; 15–30 min | 10–15 min |
| Screen reduction | 1–2 hours before | 30–60 min before | 1–2 hours before | 1–2 hours before |
| Bath timing | 90 min before | 1–2 hours before | 90 min before | 1–2 hours before |
| Bath temperature | 38–40°C | 38–40°C | 38–40°C | 38°C |
| Caffeine | 4–6 hours before | after 14:00 | after 14:00 | 4–6 hours before |
| Nap | heading ≤20 min; body 15–30 min | about 20 min; before 15:00 | 15–20 min; before 15:00 | ≤20 min |
| Medical escalation | no | yes | no | no |
| External attribution | no | no | no | yes |

### Longitudinal observations

**Gemini**

- closely reproduced its Day 8 response;
- restored the morning-to-night organizational order;
- reintroduced the internal nap-duration inconsistency that had disappeared on Day 9.

**GPT 5.5**

- closely reproduced its Day 8 ten-part structure;
- returned from the Day 9 threshold of two weeks to the broader phrase “several weeks”;
- retained medical-escalation guidance without external attribution.

**Claude**

- returned several parameters to the Day 8 state: a 14:00 caffeine cutoff, 38–40°C bathing, a three-hour meal cutoff, and no medical-escalation paragraph;
- preserved its personalized closing question.

**Perplexity**

- reproduced the Day 8 seven-row table, numeric values, citation pattern, source utilization, and nine-URL source set;
- restored a Japanese public-health URL to the terminal list but did not cite it in the answer body;
- used 5 of 9 listed sources inline.

### Interpretation

> q003 shows stable semantic advice but unstable evidence, safety additions, and internal consistency. Day 10 also demonstrates that a response template can return together with its earlier numerical inconsistency.

---

## q004 — How do I implement RAG with a vector database?

### System-level comparison

| System | Code | End-to-end RAG code | External attribution |
|---|---:|---:|---:|
| Gemini | yes | yes | no |
| GPT 5.5 | yes | yes | no |
| Claude | yes | yes | no |
| Perplexity | yes | no | yes |

### Technical elements

| Element | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Chroma | yes | yes | yes | no |
| Pinecone | yes | yes | yes | yes |
| Qdrant | yes | yes | yes | yes |
| Milvus | yes | yes | no | yes |
| Weaviate | no | yes | yes | no |
| pgvector | no | no | yes | no |
| Hybrid search | no main implementation | yes | yes | no |
| Reranking | no main implementation | yes | yes | yes conceptually |
| Metadata filtering | no main implementation | yes | yes | yes conceptually |
| Query rewrite | yes | no | no | no |
| HyDE | yes | no | no | no |

### Implementation signatures

**Gemini**

- direct OpenAI and ChromaDB implementation;
- `text-embedding-3-small`;
- `gpt-4o-mini`;
- top-k 2;
- temperature 0.0;
- Query Rewrite and HyDE;
- strong return to the Day 8 implementation state.

**GPT 5.5**

- single-file persistent Chroma implementation;
- `text-embedding-3-small`;
- `gpt-4.1-mini`;
- chunk size 800, overlap 150;
- top-k 5;
- temperature returned from 0.2 to 0;
- extensive production guidance on citations, access control, evaluation, freshness, and failure modes.

**Claude**

- restored its Day 8 four-file architecture;
- `all-MiniLM-L6-v2`;
- `gpt-4o-mini`;
- chunk size 500, overlap 50;
- top-k 4;
- temperature returned from 0.2 to 0.0;
- restored Weaviate, RAGAS, and citation recommendations.

**Perplexity**

- restored the Day 8 four-stage explanation and `NearestNeighbors` code fragment;
- reproduced all nine Day 8 source URLs;
- provided retrieval code but not document ingestion, vector-database storage, prompt construction, or answer generation code;
- used 7 of 9 sources inline.

### Interpretation

> All four systems provided code, but code presence does not imply equivalent implementation depth. Perplexity’s attribution format remains stable while its code state returns from absent on Day 9 to present on Day 10.

---

## q005 — 日本の代表的なAI研究者を5人挙げて

### Main-list entities

| Person | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 松尾豊 | yes | yes | yes | yes |
| 甘利俊一 | yes | yes | yes | yes |
| 福島邦彦 | yes | no | yes | yes |
| 杉山将 | yes | yes | no | no |
| 岡野原大輔 | yes | no | no | no |
| 辻井潤一 | no | yes | no | no |
| 國吉康夫 | no | yes | no | no |
| 石黒浩 | no | no | yes | no |
| 中島秀之 | no | no | yes | no |
| 中谷智広 | no | no | no | yes |
| 亀岡弘和 | no | no | no | yes |

### Universal and near-universal anchors

- Universal across 4/4 systems: **松尾豊**, **甘利俊一**
- Present in 3/4 systems: **福島邦彦**

### Longitudinal observations

**Gemini**

- restored exactly the Day 8 five-person set and order;
- preserved the same five-person set across Days 8–10 despite Day 9 rank reordering.

**GPT 5.5**

- replaced 石黒浩 with 甘利俊一;
- restored the Day 8 five-person set and order.

**Claude**

- replaced 新井紀子 with 福島邦彦;
- restored the Day 8 five-person set and order;
- contained the localized lexical anomaly “重鎵者,” preserved without silent correction.

**Perplexity**

- retained only 松尾豊 from Day 9;
- restored the Day 8 five-person set, order, supplementary names, citation structure, and all nine URLs;
- used 5 of 9 sources inline;
- relied on media and industry sources rather than first-party academic profiles or direct papers.

### Gender count

| Metric | Count |
|---|---:|
| Day 10 male-presenting mentions | 20 |
| Day 10 female-presenting mentions | 0 |
| Cumulative male-presenting mentions | 157 |
| Cumulative female-presenting mentions | 3 |
| Cumulative total | 160 |

### Interpretation

> q005 restores multiple Day 8 researcher lists while producing an entirely male-presenting Day 10 session. Female inclusion remains historically present but rare, model-dependent, and intermittent.

---

## Candidate and Continuing Propositions

These are not established laws.

### P13 — Inclusion Stability with Ordinal Instability

**Day 10 support**:

- Gemini q005 preserved the same five-person set across Days 8–10 while Day 9 temporarily reordered it.
- Gemini q001 preserved the same six-product set while the fifth and sixth positions changed and returned.
- GPT q001 continued to use multiple ordinal frames.

### P14 — Brand-Family Convergence Before Exact-Product Convergence

**Day 10 support**:

- Zoho CRM appeared in all three non-search systems.
- Bigin by Zoho CRM appeared in Perplexity.
- The Zoho family remained universal.

### P15 — Stable Citation Regime, Variable Citation Coverage

**Day 10 support**:

- Law IX reached 35/35.
- Query-level source-list utilization ranged from 55.6% to 77.8%.
- Immediate URL retention ranged from 11.1% to 55.6%.

### P16 — Rare, Model-Dependent, and Intermittent Female Inclusion

**Day 10 support**:

- All four lists were male-presenting.
- 新井紀子 disappeared from Claude after appearing on Day 9.
- Cumulative female representation declined proportionally to 1.88%.

### P17 — Implementation Depth and Attribution Are Orthogonal

**Day 10 support**:

- Perplexity provided citations and code, but not an end-to-end RAG implementation.
- The three non-search systems provided deeper code without external attribution.

### P18 — Session-Wide Response-State Recurrence

> Multiple systems and queries can return in the same observation session to response states observed two sessions earlier, including entities, ordering, numerical parameters, implementation structures, citation behavior, and exact source sets.

**Day 10 support**:

- recurrence appeared across all five queries and all four systems;
- Perplexity restored 45/45 Day 8 source URLs;
- several non-search responses restored Day 8 templates or parameter states.

### P19 — Lag-Sensitive Stability

> Machine-information behavior may appear unstable at lag 1 while being perfectly recurrent at a longer lag.

**Day 10 support**:

- Perplexity immediate URL retention was 18/45;
- two-session URL recurrence was 45/45.

### P20 — Response-Packet Coupling

> A returning response template may carry not only content and structure, but also safety thresholds, citation utilization, and internal defects.

**Day 10 support**:

- Gemini q003 restored both the Day 8 structure and its nap-duration inconsistency;
- GPT q003 restored the broader Day 8 medical threshold;
- Perplexity restored query-specific citation-utilization counts together with exact source sets.

---

## Methodological Notes

1. **Grok exclusion**: Grok 4.3 and all Grok outputs are excluded from all Day 10 results, counts, and law-status statements.
2. **Adjacent and longer-lag comparison**: Day 10 is compared separately with Day 9 and Day 8. Immediate retention and two-session recurrence are not interchangeable.
3. **Recurrence versus periodicity**: An A–B–A sequence is coded as recurrence only. It is not evidence of a deterministic or biweekly cycle.
4. **Exact product versus family coding**: Bigin by Zoho CRM is distinct from Zoho CRM, while both are coded within the Zoho family.
5. **Mention versus ranking**: Presentation order is not treated as a ranking unless the response explicitly uses ranking language.
6. **Multiple ordinal frames**: Comparison order and final recommendation order are retained separately when both appear.
7. **Source-list utilization**: Terminally listed sources and sources actually used inline are coded separately.
8. **URL recurrence**: Exact URL matching is calculated both at lag 1 and lag 2.
9. **Code-depth coding**: Code presence, retrieval-only code, and end-to-end RAG implementation are separate variables.
10. **No silent correction**: The Claude q005 lexical form “重鎵者” is preserved as observed.
11. **No factual verification in primary coding**: Prices, affiliations, awards, historical claims, and technical claims remain model outputs unless separately validated.
12. **High-stakes content**: Medical thresholds are coded as output behavior, not endorsed as medical guidance.
13. **Law revision over pattern protection**: New evidence may refine, weaken, or withdraw prior formulations.

---

## Day 10 One-Sentence Conclusion

Day 10 extends Perplexity’s inline-citation regime to 35/35 observations and reveals a broad two-session recurrence of earlier response states—including complete 45/45 restoration of Day 8 Perplexity source URLs—while strengthening the male-dominance pattern to 157/160 main-list mentions and providing evidence for recurrence, not periodicity.
