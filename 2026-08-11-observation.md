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

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-11T21:15:55+09:00).

---

## Executive Summary

Day 15 collected cleanly across all four systems (Gemini, ChatGPT, Claude, Perplexity) at 5/5 each via API on query-set v0.1.1. The citation split remained sharp: Perplexity carried inline numeric citations plus a structured terminal `citations` array on all 5/5 responses (q001–q005 terminal counts: 20, 20, 18, 20, 20), while Gemini, ChatGPT, and Claude supplied zero inline citations and zero terminal sources throughout. Law VII was again tested by q005, where Claude's five-person list included Arai Noriko (新井紀子), the sole female-presenting main-list mention this session (1/20). Per-model signatures held — Claude's clarifying questions, ChatGPT's top-pick framing, Gemini's decision guides, and Perplexity's inline-marker style.

---

## Law Status

- **Law I — Canonical Inclusion**: Confirm. q001's tool nucleus persisted across systems — Trello, Asana, and Notion appear in all four lists, and Jira in all four, while peripheral picks and ordering fluctuated (Gemini added Backlog/monday.com, Claude added Todoist/GitHub Projects, Perplexity added Wrike/Jooto/Redmine). q002 similarly shows a HubSpot CRM + Pipedrive + Zoho CRM core across all four systems with peripheral variation. This matches the durable-core / fluctuating-periphery formulation.
- **Law II — Perplexity URL Stability**: Insufficient-evidence this session. The coded data provides terminal_source_count per query (20/20/18/20/20) but no normalized-URL sets, so cross-wave URL survival, longer-lag recurrence, retained-share, and citation-index reassignment cannot be measured from this packet.
- **Law III — Day 2 Anomaly**: Insufficient-evidence this session. This is a confirmed historical single-day anomaly; nothing in Day 15 data bears on it.
- **Law VI — Per-Model Signature**: Confirm/strengthen. Signatures recur across all five queries: Claude closes with clarifying questions (q001, q002) and knowledge-limitation disclaimers (q005); ChatGPT leads with a named top pick and use-case summary (q002 HubSpot CRM) and adds one-example caveats (q005); Gemini produces categorized breakdowns with comparison tables and decision/selection guides (q001, q002); Perplexity uniformly carries inline citation markers and offers to narrow further (q005). 4/4 systems held recognizable style.
- **Law VII — Gender Dominance in Person Queries**: Strengthen. q005 produced four five-person lists (20 main-list mentions). Male-presenting: 19/20; female-presenting: 1/20 — Arai Noriko (新井紀子) inside Claude's main list, the same researcher that appeared on Day 14. This is consistent with the rare, intermittent, cross-system-but-unstable pattern.
- **Law VIII — Absence of Stable Direct Academic Grounding**: Insufficient-evidence for full audit, but consistent. Perplexity returned terminal sources on all five queries, but the packet gives only counts (20/20/18/20/20), not source classes or URLs, so no peer-reviewed / arXiv / first-party scholarly grounding can be confirmed or refuted at the item level; nothing contradicts the law.
- **Law IX — Perplexity Inline Citation Shift**: Confirm/continuing. Inline numeric citations present on 5/5 Perplexity responses, each with a terminal `citations` array (q001–q005: 20, 20, 18, 20, 20), extending inline-plus-terminal continuity. Twenty-source regime this session: 4/5 (q003 returned 18). The other three systems again showed no inline or terminal citations, preserving the interface-level citation dichotomy.

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

Strong cross-system agreement on a project-management core — Trello, Asana, Notion, and Jira appear in all four lists — with peripheral divergence (Gemini's Backlog/monday.com, Claude's Todoist/GitHub Projects, Perplexity's Wrike/Jooto/Redmine). Only Perplexity carried inline citations and a 20-source terminal array; the note's 'no terminal source list' phrasing conflicts with the terminal_sources=yes flag and count of 20, likely reflecting the API `citations` array not being rendered in answer text.

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

Broad agreement on a small-business CRM nucleus — HubSpot CRM, Pipedrive, and Zoho CRM appear across all four systems — but with distinct top picks: ChatGPT leads with HubSpot CRM while Perplexity tops its list with Salesforce. Perplexity alone supplied inline citations and 20 terminal sources; the other three gave comparison tables but no citations.

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

This sleep-quality query drew no named products from any system; Gemini and Claude returned prose hygiene advice with no coded entities, while ChatGPT (10 tips) and Perplexity (5 tips) enumerated Japanese-language behavioral items. Perplexity was the only system with inline citations and a terminal source array (18, the session's single sub-20 count).

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

All four systems converged on a RAG vector-database toolset — FAISS, Pinecone, and Qdrant appear in all four, with LangChain, Chroma/ChromaDB, and pgvector widely shared — but implementation style split on code: Gemini, ChatGPT, and Claude included working code blocks (code=yes), whereas Perplexity gave a conceptual walkthrough with inline citations and 20 terminal sources but no code, reprising its citation-over-code signature.

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

All four lists centered on 松尾豊 (present in every response), with 甘利俊一 shared by three and other picks diverging (ChatGPT's 辻井潤一/中島秀之, Claude's 石黒浩/中島秀之/新井紀子, Perplexity's 栗原聡/松原仁). Claude's inclusion of 新井紀子 is the session's lone female-presenting main-list mention (Law VII); only Perplexity attached inline citations and a 20-source terminal array.

---

## Methodological Notes

All four systems ran in API mode on query-set operational v0.1.1 with 5/5 ok each and no excluded or errored systems; collection ran 21:09:58–21:14:14 (+09:00) on 2026-08-11. One coding anomaly: Perplexity's q001 and q003 notes state there is 'no terminal source list' while the same records carry terminal_sources=yes with counts of 20 and 18, reflecting the post-Day-14 shift where terminal sources arrive via the API `citations` array rather than rendered answer text.

---

## Day 15 One-Sentence Conclusion

A clean four-system API session that reaffirmed the Perplexity-only citation regime, stable cross-system canonical cores on q001/q002/q004, persistent per-model signatures, and a single female-presenting researcher (Arai Noriko) in Claude's q005 list.
