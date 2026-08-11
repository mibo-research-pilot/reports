# 15th Observation — 2026-08-11

**Observatory**: MIBO — Machine Information Behavior Observatory  
**Japanese name**: 機械情報行動観測所  
**Observation date**: 2026-08-11  
**Timezone**: Asia/Tokyo  
**Core method**: Longitudinal Machine Observation (LMO)  
**Observation mode**: API collection (automated)  
**Included systems**: Gemini (gemini-3.5-flash), ChatGPT (gpt-5.5-2026-04-23), Claude (claude-opus-4-8), Perplexity (sonar)  
**Excluded systems**: none  
**Included observations this session**: 20  
**Cumulative MIBO observations after this session**: 284  
**Collection window**: 2026-08-11T21:09:58.089379+09:00 → 2026-08-11T21:14:14.173292+09:00  
**Raw responses**: [`2026-08-11/raw-responses.md`](2026-08-11/raw-responses.md) (verbatim API outputs)  

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-11T21:30:51+09:00).

---

## Executive Summary

All four systems (Gemini, ChatGPT, Claude, Perplexity) returned successful responses on 5/5 queries via API with no exclusions. Perplexity again carried inline numeric citations on all 5/5 responses with API `citations` arrays of 20, 20, 18, 20, and 20 sources (four of five in the twenty-source regime), while the other three systems supplied no citations or terminal sources on any query. Law VII held with a lopsided but non-zero gender ratio (19/20 male-presenting; 1/20 female-presenting via Arai Noriko in Claude's q005 main list), and canonical cores stayed durable in q001, q002, and q004 while person and ordinal selection continued to fluctuate.

---

## Law Status

- **Law I — Canonical Inclusion**: Confirm. Durable inclusion cores persisted across systems with peripheral fluctuation: q001 showed Trello, Asana, and Notion in all 4 systems and Jira in 4/4; q002 showed HubSpot CRM in all 4 and Pipedrive in all 4; q004 showed Pinecone in 4/4 and FAISS in 4/4, with list lengths varying from 5 to 13 entities. This matches the law's expectation of a stable nucleus alongside varying peripheral selections and ordinal positions.
- **Law II — Perplexity URL Stability**: Insufficient-evidence this session. The coded data provides terminal_source_count values (20/20/18/20/20) but no normalized-URL sets or prior-wave URL baselines, so normalized-URL survival, longer-lag recurrence, retained-share, and citation-index reassignment cannot be computed from this packet.
- **Law III — Day 2 Anomaly**: Insufficient-evidence this session. This is a fixed historical finding about 2026-05-12; nothing in the Day 15 data bears on it.
- **Law VI — Per-Model Signature**: Confirm. Signatures recurred: Claude closed with clarifying/narrowing questions or disclaimers (q001, q002, q005), ChatGPT led with a top pick and 'one example' caveats (q002, q005), Gemini produced categorized breakdowns with comparison tables and pricing (q001, q002), and Perplexity uniquely carried inline citations plus offers to narrow further (q004, q005). These held across changing entities and source sets.
- **Law VII — Gender Dominance in Person Queries**: Strengthen. q005 produced 4 five-person male-presenting lists totaling 19/20 male-presenting mentions, with the single female-presenting mention being Arai Noriko (新井紀子) inside Claude's main list — again the recurring name, again in a single system, consistent with rare, intermittent, cross-system-variable inclusion. 松尾豊 appeared in all 4 systems.
- **Law VIII — Absence of Stable Direct Academic Grounding**: Insufficient-evidence this session. Perplexity returned terminal source counts but the packet contains no source-class detail (no domains, titles, or URLs), so whether the terminal lists included peer-reviewed/arXiv/first-party scholarly sources cannot be judged this run; the counts alone are consistent with the law but do not test it.
- **Law IX — Perplexity Inline Citation Shift**: Confirm/strengthen. Perplexity carried inline numeric citations on 5/5 responses, each paired with an API `citations` terminal array (20, 20, 18, 20, 20), extending inline-plus-terminal continuity. Twenty-source regime this session was 4/5 (q003 returned 18); the other three systems produced no inline or terminal citations on any of their 15 responses, keeping the citation form a Perplexity-only signature.

---

## Query-Level Findings

## q001 — おすすめのプロジェクト管理ツールは？

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Trello | 1 | 2 | 1 | 5 |
| Asana | 2 | 3 | 3 | 1 |
| Notion | 4 | 1 | 4 | 4 |
| Backlog | 5 | 5 |  | 2 |
| Jira |  | 4 | 6 | 3 |
| monday.com | 3 |  |  | 9 |
| ClickUp |  | 6 | 5 |  |
| Todoist |  |  | 2 |  |
| Jira Software | 6 |  |  |  |
| Wrike |  |  |  | 6 |
| GitHub Projects |  |  | 7 |  |
| Jooto |  |  |  | 7 |
| Redmine |  |  |  | 8 |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

All four systems recommended project-management tools with strong overlap — Trello, Asana, and Notion appeared in all 4, and Jira in all 4 — while list length ranged from 6 (Gemini, ChatGPT) to 7 (Claude) to 9 (Perplexity, which added Wrike, Jooto, and Redmine). Only Perplexity carried inline citations and a 20-source terminal array; its note oddly claims 'no terminal source list' despite the terminal_sources flag and count of 20, a minor coding inconsistency.

## q002 — What is the best CRM for small businesses?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| HubSpot CRM | 1 | 1 | 1 | 2 |
| Pipedrive | 2 | 3 | 2 | 4 |
| Zoho CRM | 3 | 2 | 4 | 5 |
| Freshsales |  | 4 | 3 | 7 |
| Salesforce |  |  | 6 | 1 |
| Copper | 4 |  | 5 |  |
| Bigin by Zoho CRM |  |  |  | 3 |
| Less Annoying CRM | 5 |  |  |  |
| Salesforce Starter |  | 5 |  |  |
| Monday Sales CRM |  | 6 |  |  |
| NetHunt CRM |  |  |  | 6 |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

The four systems converged on HubSpot CRM (all 4) and Pipedrive (all 4), with Zoho CRM in all 4 as well; divergence appeared at the top pick, where ChatGPT led with HubSpot and Perplexity topped its list with Salesforce. Only Perplexity supplied inline citations and a 20-source terminal array.

## q003 — 睡眠の質を上げる方法を教えて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 毎日同じ時間に起きる |  | 1 |  |  |
| 毎日ほぼ同じ時刻に起きる |  |  |  | 1 |
| 朝に日光を浴びる |  | 2 |  |  |
| 朝起きたら光を浴びる |  |  |  | 2 |
| 寝る前のスマホ・PCを減らす |  | 3 |  |  |
| 寝る1時間前はスマホ・PCを減らす |  |  |  | 3 |
| カフェインは午後以降控える |  | 4 |  |  |
| 夕方〜就寝3時間前までに軽い運動をする |  |  |  | 4 |
| 寝る前のルーティンを作る |  | 5 |  |  |
| 寝室を暗く・静か・快適にする |  |  |  | 5 |
| 入浴は寝る1〜2時間前に |  | 6 |  |  |
| 寝室を快適にする |  | 7 |  |  |
| 寝る直前の食事・飲酒を避ける |  | 8 |  |  |
| 日中に軽く運動する |  | 9 |  |  |
| 眠れないときは一度ベッドを出る |  | 10 |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(18)._

### Interpretation

This Japanese sleep-quality query drew no product entities from Gemini or Claude (prose guidance only), while ChatGPT enumerated 10 tips and Perplexity 5; the two enumerated lists agree on the core habits (consistent wake time, morning light, reduced pre-sleep screens, comfortable bedroom). Perplexity alone carried inline citations with an 18-source terminal array — the only sub-20 count this session.

## q004 — How do I implement RAG with a vector database?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| FAISS | 4 | 2 | 6 | 3 |
| Pinecone | 6 | 3 | 2 | 4 |
| Qdrant | 7 | 4 | 4 | 2 |
| LangChain | 1 |  | 7 | 1 |
| Chroma | 2 | 1 |  |  |
| Weaviate |  | 5 | 3 |  |
| pgvector | 9 |  | 5 |  |
| Milvus | 8 | 6 |  |  |
| ChromaDB |  |  | 1 |  |
| OpenAI | 3 |  |  |  |
| SQLite (sqlite-vss) | 5 |  |  |  |
| BM25 |  |  |  | 5 |
| Postgres + pgvector |  | 7 |  |  |
| OpenAI API |  | 8 |  |  |
| LlamaIndex |  |  | 8 |  |
| MongoDB Atlas | 10 |  |  |  |
| Elasticsearch | 11 |  |  |  |
| Cohere Rerank | 12 |  |  |  |
| BGE-Reranker | 13 |  |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

All four gave RAG implementation guidance with shared vector-database nuclei — Pinecone and FAISS in all 4, Qdrant in 3/4 — but Gemini, ChatGPT, and Claude included runnable code while Perplexity did not, instead giving a conceptual walkthrough with inline citations and a 20-source terminal array. This is a clear split: code-bearing systems suppress citations, and the citation-bearing system suppresses code.

## q005 — 日本の代表的なAI研究者を5人挙げて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 松尾豊 | 1 | 1 | 1 | 1 |
| 甘利俊一 | 4 |  | 2 | 5 |
| 杉山将 | 2 | 2 |  |  |
| 石黒浩 |  |  | 3 | 2 |
| 北野宏明 | 5 | 4 |  |  |
| 中島秀之 |  | 5 | 4 |  |
| 福島邦彦 | 3 |  |  |  |
| 辻井潤一 |  | 3 |  |  |
| 栗原聡 |  |  |  | 3 |
| 松原仁 |  |  |  | 4 |
| 新井紀子 |  |  | 5 |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

松尾豊 was the sole unanimous name across all 4 systems, with 甘利俊一 in 3/4; otherwise the five-person lists diverged substantially (石黒浩, 中島秀之, 杉山将, and others distributed unevenly). Only Perplexity carried inline citations; Claude's list uniquely included the female-presenting Arai Noriko (新井紀子), the session's single female-presenting main-list mention.

---

## Methodological Notes

All four systems ran in API mode under query set 'operational v0.1.1' with 5/5 ok_count each and no excluded or errored systems; collection spanned roughly four minutes (21:09:58–21:14:14 JST). One anomaly of note is Perplexity's q001 coding, where the note states 'no terminal source list' while the terminal_sources flag is 'yes' with a count of 20; source-class detail and normalized URLs are absent from the packet, limiting Laws II and VIII.

---

## Day 15 One-Sentence Conclusion

A clean four-system API session in which durable canonical cores and per-model signatures held, Perplexity remained the sole citing system across all five queries, and Law VII's male dominance persisted with a single female-presenting exception in Claude's researcher list.
