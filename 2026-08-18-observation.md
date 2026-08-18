# 16th Observation — 2026-08-18

**Observatory**: MIBO — Machine Information Behavior Observatory  
**Japanese name**: 機械情報行動観測所  
**Observation date**: 2026-08-18  
**Timezone**: Asia/Tokyo  
**Core method**: Longitudinal Machine Observation (LMO)  
**Observation mode**: API collection (automated)  
**Included systems**: Gemini (gemini-3.5-flash), ChatGPT (gpt-5.5-2026-04-23), Claude (claude-opus-4-8), Perplexity (sonar)  
**Excluded systems**: none  
**Included observations this session**: 20  
**Cumulative MIBO observations after this session**: 304  
**Collection window**: 2026-08-18T20:21:47.597741+09:00 → 2026-08-18T20:25:14.282264+09:00  
**Raw responses**: [`2026-08-18/raw-responses.md`](2026-08-18/raw-responses.md) (verbatim API outputs)  

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-18T20:35:16+09:00).

---

## Executive Summary

All four systems (Gemini, ChatGPT, Claude, Perplexity) completed 5/5 queries via API this session with no exclusions. Perplexity was the only system to emit inline citations, doing so on all five queries (5/5), consistently paired with a terminal_source_count (17–20) despite the coder note that no terminal source list rendered in-text. Code blocks appeared uniformly across all four systems on the RAG query (q004, 4/4) and nowhere else. Entity overlap was strong on tool-recommendation queries (q001, q002) and on the anchor researcher 松尾豊 (q005), which all four systems returned first.

---

## Law Status

- The authoritative law list (core/laws.md) was unavailable this run, so no established laws can be referenced by id or name, and no confirm/strengthen/revise/withdraw judgments can be assigned. Summarizing the raw citation/canonical evidence instead: **inline citations** appeared only in Perplexity, on 5/5 queries; Gemini, ChatGPT, and Claude showed 0/5 inline citations each. Every Perplexity observation carried a `terminal_source_count` (q001=20, q002=18, q003=20, q004=17, q005=20), yet each was coded `terminal_sources: yes` while the notes state no terminal source list was rendered in-text — a discrepancy worth flagging for the law maintainers. **Code** was emitted by all four systems only on q004 (RAG), i.e. 4/4 systems on that query and 0/4 on every other query. **Canonical/entity stability**: 松尾豊 was returned first by all four systems on q005; 杉山将 and 甘利俊一 recurred across three systems; HubSpot CRM led three of four systems on q002; ChromaDB/Chroma and OpenAI recurred across all four systems on q004.

---

## Query-Level Findings

## q001 — おすすめのプロジェクト管理ツールは？

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Trello | 1 | 3 | 3 | 1 |
| Asana | 2 | 1 | 2 | 5 |
| Notion | 7 | 2 | 1 | 2 |
| monday.com | 3 | 8 | 7 | 6 |
| Jira |  | 4 | 4 | 3 |
| Wrike | 4 | 9 |  | 7 |
| Backlog | 5 | 6 |  | 4 |
| GitHub Projects |  | 5 | 5 |  |
| Jira Software | 6 |  |  |  |
| ClickUp |  |  | 6 |  |
| Jooto |  | 7 |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

All four systems recommended project-management tools and shared a strong common core (Trello, Asana, Jira/Jira Software, monday.com/Monday.com, Notion, Wrike appear across most), with ChatGPT returning the widest set (9 entities) and Gemini/Claude/Perplexity each returning 7. Only Perplexity carried inline citations (terminal_source_count 20); the other three offered no citations or sources.

## q002 — What is the best CRM for small businesses?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| HubSpot CRM | 1 | 1 | 1 | 1 |
| Zoho CRM | 2 | 2 | 3 | 3 |
| Pipedrive | 3 | 3 | 2 | 2 |
| Copper |  | 4 | 7 |  |
| Freshsales |  | 5 | 4 |  |
| Salesforce |  |  | 5 | 4 |
| Monday.com | 4 |  |  |  |
| Streak | 5 |  |  |  |
| Bigin by Zoho |  |  |  | 5 |
| Salesforce Starter |  | 6 |  |  |
| Less Annoying CRM |  |  | 6 |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(18)._

### Interpretation

All four converged on a HubSpot CRM / Zoho CRM / Pipedrive core for small-business CRMs, with HubSpot CRM listed first by Gemini, ChatGPT, and Claude; divergence appears in the long tail (e.g., Claude's Less Annoying CRM, Perplexity's Bigin by Zoho, ChatGPT's Copper/Freshsales/Salesforce Starter). Perplexity alone used inline citations (terminal_source_count 18), while the other three provided none.

## q003 — 睡眠の質を上げる方法を教えて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 起床時間を固定する |  | 1 | 1 |  |
| 寝る前のスマホ・PCを控える |  | 3 |  | 3 |
| 起床時刻を一定にする |  |  |  | 1 |
| 朝に日光を浴びる |  | 2 |  |  |
| 朝日を浴びる |  |  | 2 |  |
| 朝起きたら光を浴びる |  |  |  | 2 |
| カフェインは午後以降控える |  | 4 |  |  |
| 寝室を暗くする |  |  |  | 4 |
| 寝酒は避ける |  | 5 |  |  |
| 夕食は早めに済ませる |  |  |  | 5 |
| 寝室を快適にする |  | 6 |  |  |
| 入浴は寝る1.5〜2時間前 |  |  |  | 6 |
| 寝る前のルーティンを作る |  | 7 |  |  |
| 軽い運動を習慣にする |  |  |  | 7 |
| 運動する |  | 8 |  |  |
| 寝室の環境を整える |  |  |  | 8 |
| 昼寝は短めにする |  | 9 |  |  |
| 眠れないまま布団で粘らない |  | 10 |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

This Japanese sleep-hygiene query shows the coding limitation that entities here are extracted advice items, not canonical named entities — Gemini's response yielded no extracted entities at all, and Claude only two, while ChatGPT (10) and Perplexity (8) yielded fuller enumerated lists. There is semantic agreement on fixed wake time and morning light across the systems that listed items; Perplexity again was the sole system with inline citations (terminal_source_count 20).

## q004 — How do I implement RAG with a vector database?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Pinecone | 5 | 3 |  | 1 |
| FAISS | 4 | 2 |  | 5 |
| Qdrant | 7 | 5 |  | 3 |
| Milvus | 6 | 6 |  | 4 |
| ChromaDB | 2 |  | 1 |  |
| Chroma |  | 1 |  | 6 |
| Weaviate |  | 4 |  | 2 |
| OpenAI | 3 |  | 3 |  |
| all-MiniLM-L6-v2 | 9 |  | 4 |  |
| pgvector | 8 |  |  | 7 |
| LangChain | 1 |  |  |  |
| sentence-transformers |  |  | 2 |  |
| gpt-4o-mini |  |  | 5 |  |
| OpenAI text-embedding-3-small/large |  | 7 |  |  |
| Cohere embeddings |  | 8 |  |  |
| SentenceTransformers all-MiniLM-L6-v2 |  | 9 |  |  |
| text-embedding-3-large | 10 |  |  |  |
| BGE embeddings |  | 10 |  |  |
| Cohere Embed | 11 |  |  |  |
| Instructor embeddings |  | 11 |  |  |
| Ollama | 12 |  |  |  |
| OpenAI GPT |  | 12 |  |  |
| GPT-4o | 13 |  |  |  |
| Claude |  | 13 |  |  |
| Claude 3.5 Sonnet | 14 |  |  |  |
| Gemini |  | 14 |  |  |
| LlamaIndex | 15 |  |  |  |
| Llama |  | 15 |  |  |
| Cohere Rerank | 16 |  |  |  |
| Mistral |  | 16 |  |  |
| Ragas | 17 |  |  |  |
| TruLens | 18 |  |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(17)._

### Interpretation

The RAG query was the only query to trigger code across all four systems (4/4 code: yes), with strong stack agreement centered on ChromaDB/Chroma, OpenAI embeddings, FAISS, Pinecone, Qdrant, and Milvus. Gemini and ChatGPT returned the broadest tech-stack lists (18 and ~16 entities), Claude the most minimal (5), and Perplexity focused on the vector-DB layer (7 entities) while being the only system to add inline citations (terminal_source_count 17).

## q005 — 日本の代表的なAI研究者を5人挙げて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 松尾豊 | 1 | 1 | 1 | 1 |
| 杉山将 | 3 | 2 | 3 | 2 |
| 甘利俊一 | 4 | 3 | 2 |  |
| 石黒浩 |  |  | 4 | 3 |
| 福島邦彦 | 2 |  |  |  |
| 辻井潤一 |  | 4 |  |  |
| 伊藤孝行 |  |  |  | 4 |
| 北野宏明 | 5 |  |  |  |
| 國吉康夫 |  | 5 |  |  |
| 中島秀之 |  |  | 5 |  |
| 今井翔太 |  |  |  | 5 |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

All four systems returned exactly five Japanese AI researchers and unanimously placed 松尾豊 first, with 杉山将 shared by all four and 甘利俊一 shared by three (Gemini, ChatGPT, Claude); beyond that anchor the sets diverge (e.g., Gemini's 福島邦彦/北野宏明, Perplexity's 伊藤孝行/今井翔太, Claude's 石黒浩/中島秀之). Per the coding guardrail, no gender inference is drawn from these names. Only Perplexity carried inline citations (terminal_source_count 20).

---

## Methodological Notes

All four systems (Gemini gemini-3.5-flash, ChatGPT gpt-5.5-2026-04-23, Claude claude-opus-4-8, Perplexity sonar) ran in API mode and returned 5/5 successful queries with no excluded systems and no errors; query set was operational v0.1.1. Collection ran 2026-08-18T20:21:47 to 20:25:14 (+09:00). One recurring anomaly: Perplexity observations are coded `terminal_sources: yes` and carry a `terminal_source_count`, but every note states no terminal source list was actually rendered in-text — this internal inconsistency should be reconciled before source-attribution laws are re-evaluated.

---

## Day 16 One-Sentence Conclusion

A clean 5/5-across-all-systems session in which Perplexity remained the lone inline-citation source (5/5), code appeared only on the RAG query (4/4), and 松尾豊 held as the stable anchor entity for the Japanese-researcher query.
