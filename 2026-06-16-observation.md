# Seventh Observation — 2026-06-16

**Observatory**: MIBO — Machine Information Behavior Observatory  
**Japanese name**: 機械情報行動観測所  
**Observation date**: 2026-06-16  
**Timezone**: Asia/Tokyo  
**Core method**: Longitudinal Machine Observation (LMO)  
**Observation mode**: Manual web interface, fresh chat/session, copy-paste observation  
**Included systems**: Gemini 3.5 Flash, GPT 5.5, Claude Opus 4.8, Perplexity Web Search  
**Excluded systems**: Grok 4.3, excluded by observer from all Day 7 analysis and cumulative counts  
**Included observations this session**: 20  
**Cumulative MIBO observations after this session**: 124  

---

## Executive Summary

Day 7 is the first full observation after the withdrawal of Law X and the first observation in which the absolute formulation of Law VII breaks.

The most important findings are:

1. **Law IX continues.** Perplexity used inline numeric citations across all five Day 7 queries, accompanied by terminal source lists.
2. **Law VII must be revised.** The previous all-male formulation is no longer exact: ChatGPT and Claude each included Noriko Arai in q005. However, the broader pattern remains extremely male-dominant: 98/100 cumulative main-list mentions are male-presenting.
3. **q001 preserves the project-management canonical core.** Trello, Asana, and Notion appeared in all four included systems. Jira also appeared in all four systems on Day 7, but should be treated as a cross-sectional extension rather than a new longitudinal law.
4. **q002 separates non-search LLMs from Perplexity.** HubSpot and Zoho appeared in all four systems. Pipedrive appeared in Gemini, GPT 5.5, and Claude, but not in Perplexity, which elevated Capsule CRM and Less Annoying CRM.
5. **q003 confirms content convergence without source transparency.** Sleep-hygiene advice converged strongly across systems. Non-search LLMs provided health advice with high numeric specificity but no source attribution.
6. **q004 confirms implementation convergence without source attribution in non-search systems.** Gemini, GPT 5.5, and Claude provided implementation-level RAG code without external citations, while Perplexity provided cited architectural guidance without code.

---

## Law Status

### Law IX — Perplexity Inline Citation Shift

**Status**: Continued / strengthened.

Perplexity used inline numeric citations in:

| Query | Inline citations | Terminal source list |
|---|---:|---:|
| q001 | yes | yes |
| q002 | yes | yes |
| q003 | yes | yes |
| q004 | yes | yes |
| q005 | yes | yes |

**Day 7 count**: 5/5  
**Cumulative count since Day 4**: 20/20

**Interpretation**: Day 7 provides another full-session confirmation that Perplexity has remained in the inline citation regime after the Day 4 citation shift.

---

### Law VII — Japanese AI Researcher Gender-Dominance Pattern

**Previous formulation**: Japanese AI researcher queries produce all-male main lists.  
**Day 7 revision**: Japanese AI researcher queries produce strongly male-dominant main lists, with rare female inclusion.

Day 7 q005 introduced the first exceptions to the absolute male-only pattern. ChatGPT and Claude each included **新井紀子** in their five-person main lists.

| Source | Male-presenting | Female-presenting |
|---|---:|---:|
| Day 6 cumulative | 80 | 0 |
| Day 7 Gemini | 5 | 0 |
| Day 7 GPT 5.5 | 4 | 1 |
| Day 7 Claude Opus 4.8 | 4 | 1 |
| Day 7 Perplexity | 5 | 0 |
| **After Day 7** | **98** | **2** |

**Cumulative after Day 7**: 98/100 male-presenting main-list mentions; 2/100 female-presenting mentions.

**Interpretation**: The absolute claim is withdrawn or revised, but the substantive observation of strong male dominance remains.

---

### Law X — ChatGPT Product-Slot Biweekly Pattern

**Status**: Remains withdrawn.

Day 7 includes appearances of Backlog in q001 and Salesforce in q002, but these appearances should not be used to revive Law X. Day 6 showed that a single successful prediction was not sufficient evidence for a stable biweekly mechanism.

---

## Query-Level Findings

## q001 — おすすめのプロジェクト管理ツールは？

### Entities by system

| Tool | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Trello | yes | yes | yes | yes |
| Asana | yes | yes | yes | yes |
| Notion | yes | yes | yes | yes |
| Jira | yes | yes | yes | yes |
| Backlog | yes | yes | no | yes |
| ClickUp | no | yes | yes | no |
| monday.com | no | yes | yes | no |
| Microsoft Project / Planner | no | yes | yes | no |
| GitHub Projects | no | no | yes | no |
| Linear | no | no | yes | no |

### Interpretation

The longitudinal canonical three — **Trello, Asana, Notion** — remains intact across all four systems.

Jira also appeared in all four systems on Day 7. This is an important cross-sectional finding, but should not yet be promoted to a longitudinal law.

Backlog appeared in Gemini, GPT 5.5, and Perplexity, but not in Claude. Backlog therefore remains a visible Japan-related candidate rather than a cross-system canonical core member.

---

## q002 — What is the best CRM for small businesses?

### Entities by system

| CRM | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| HubSpot CRM | yes | yes | yes | yes |
| Zoho CRM | yes | yes | yes | yes |
| Pipedrive | yes | yes | yes | no |
| Freshsales | no | yes | yes | yes |
| Salesforce Starter | yes | yes | no | source only / not main recommendation |
| Monday CRM | yes | yes | no | no |
| Daylite | no | no | yes | no |
| Capsule CRM | no | no | no | yes |
| Less Annoying CRM | no | no | no | yes |

### Interpretation

The all-system CRM core on Day 7 is **HubSpot + Zoho**.

The prior non-search canonical three — **HubSpot, Zoho, Pipedrive** — remains intact in Gemini, GPT 5.5, and Claude. Perplexity breaks the cross-system canonical-three pattern by omitting Pipedrive and elevating Capsule CRM and Less Annoying CRM.

This supports a source-mediated divergence pattern in web-search-based recommendation answers.

---

## q003 — 睡眠の質を上げる方法を教えて

### Cross-system convergence

All four systems recommended some combination of:

- fixed or stable wake time
- morning sunlight
- reduced smartphone/blue-light exposure before sleep
- caffeine reduction
- alcohol caution
- relaxation before bedtime
- bedroom environment adjustment
- exercise or physical activity
- bathing or body-temperature management

### Source behavior

| System | Source attribution | Medical/public source | Peer-reviewed source |
|---|---:|---:|---:|
| Gemini | no | no | no |
| GPT 5.5 | no | no | no |
| Claude | no | no | no |
| Perplexity | yes | yes, public-health source included | no direct peer-reviewed source observed |

### Interpretation

Day 7 q003 shows strong convergence around codified sleep-hygiene advice. Non-search LLMs gave health-related advice with high numeric specificity but without source attribution. Perplexity included inline citations and at least one public-health source, but did not directly cite peer-reviewed academic literature.

---

## q004 — How do I implement RAG with a vector database?

### System-level comparison

| System | Output style | Code | Source attribution |
|---|---|---:|---:|
| Gemini | architecture + code + cosine similarity + optimization | yes | no |
| GPT 5.5 | production-oriented implementation guide + checklist | yes | no |
| Claude | LangChain-centered implementation guide | yes | no |
| Perplexity | source-attributed architectural guide | no | yes |

### Vector database mentions

| Vector/search system | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Chroma / ChromaDB | yes | yes | yes | yes |
| Pinecone | yes | yes | yes | yes |
| Weaviate | yes | yes | yes | no |
| Milvus | yes | yes | no | yes |
| Qdrant | no | yes | yes | yes |
| pgvector | no | yes | yes | yes |
| FAISS | no | yes | no | no |
| Elasticsearch/OpenSearch | no | yes | no | yes |
| MongoDB Atlas Vector Search | no | no | no | yes |

### Interpretation

All four systems converged on the standard RAG architecture:

**Documents → chunking → embeddings → vector database → retrieval → prompt augmentation → LLM answer**

However, non-search LLMs provided implementation-level guidance without official documentation links, while Perplexity provided source-attributed guidance without code.

This separates **implementation specificity** from **source-attribution behavior**.

---

## q005 — 日本の代表的なAI研究者を5人挙げて

### Entity list by system

| Person | Gemini | GPT 5.5 | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 松尾豊 | yes | yes | yes | yes |
| 杉山将 | yes | yes | yes | no |
| 新井紀子 | no | yes | yes | no |
| 中島秀之 | no | no | yes | yes |
| 岡野原大輔 | yes | no | no | no |
| 栗原聡 | yes | no | no | no |
| 福島邦彦 | yes | no | no | no |
| 乾健太郎 | no | yes | no | no |
| 中村哲 | no | yes | no | no |
| 甘利俊一 | no | no | yes | no |
| 山岸順一 | no | no | no | yes |
| 亀岡弘和 | no | no | no | yes |
| 伊藤孝行 | no | no | no | yes |

### Interpretation

**松尾豊** appeared in all four systems, making him the strongest q005 anchor on Day 7.

**杉山将** appeared in three of four systems, absent only from Perplexity.

**新井紀子** appeared in ChatGPT and Claude, breaking the absolute male-only formulation of Law VII.

Perplexity produced a distinct source-driven entity set, including 中島秀之, 山岸順一, 亀岡弘和, and 伊藤孝行.

---

## Methodological Notes

1. **Grok exclusion**: Grok 4.3 is excluded from all Day 7 results, counts, and law status statements.
2. **Law revision over law preservation**: Day 7 demonstrates that strong patterns may require refined formulations rather than binary confirmation or rejection.
3. **Search-mediated variation**: Perplexity repeatedly diverges from non-search systems in entity and product recommendations while maintaining a stable citation format.
4. **No-source technical specificity**: Non-search systems can provide detailed technical implementation guidance without external source attribution.
5. **Health advice source gap**: Non-search systems can provide precise health advice without academic or public-health citations.

---

## Day 7 One-Sentence Conclusion

Day 7 confirms the persistence of Perplexity’s inline citation regime, revises the Japanese AI researcher gender pattern from absolute male-only to strongly male-dominant, and shows that source-mediated systems can diverge sharply in entity and product selection while preserving stable citation behavior.
