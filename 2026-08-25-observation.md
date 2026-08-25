# 17th Observation — 2026-08-25

**Observatory**: MIBO — Machine Information Behavior Observatory  
**Japanese name**: 機械情報行動観測所  
**Observation date**: 2026-08-25  
**Timezone**: Asia/Tokyo  
**Core method**: Longitudinal Machine Observation (LMO)  
**Observation mode**: API collection (automated)  
**Included systems**: Gemini (gemini-3.5-flash), ChatGPT (gpt-5.5-2026-04-23), Claude (claude-opus-4-8), Perplexity (sonar)  
**Excluded systems**: none  
**Included observations this session**: 20  
**Cumulative MIBO observations after this session**: 324  
**Collection window**: 2026-08-25T20:37:31.303590+09:00 → 2026-08-25T20:41:10.428194+09:00  
**Raw responses**: [`2026-08-25/raw-responses.md`](2026-08-25/raw-responses.md) (verbatim API outputs)  

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-25T20:42:03+09:00).

---

## Executive Summary

Across all five fixed queries, Perplexity (sonar) was the sole system to produce inline citations and terminal-source flags every time (5/5), while Gemini, ChatGPT, and Claude produced no citations or sources on any query (0/5 each). Code generation was uniform and query-driven: all four systems emitted code only for the RAG-implementation query q004 (4/4), and none elsewhere. Canonical entity overlap was strongest on the tooling queries (HubSpot CRM, Zoho CRM, and Pipedrive appeared in all four systems on q002), but the Japanese-AI-researcher query q005 showed sharp divergence, with 松尾豊 the only entity shared across all four systems. All four systems completed all 5 queries (20/20 observations, no exclusions).

---

## Law Status

- The authoritative law list was unavailable this run (core/laws.md returned '(unavailable this run)'), so no established laws can be referenced by id/name or assigned confirm/revise/withdraw status. Summarizing the session's citation/canonical evidence without law numbers: **Citation behavior** — Perplexity emitted inline citations and terminal-source flags on all 5/5 queries (terminal_source_count 20 on q001/q002/q003/q005 and 16 on q004), while Gemini, ChatGPT, and Claude emitted neither on any query (0/5 each). **Code behavior** — code appeared only on q004 (RAG implementation), where all four systems produced code (4/4), and on no other query (0/4 each). **Canonical/entity stability** — high cross-system agreement on tooling queries (HubSpot CRM, Zoho CRM, Pipedrive shared by all four on q002; Asana, Trello, Notion, Jira shared broadly on q001) but low stability on q005, where only 松尾豊 was common to all four systems.

---

## Query-Level Findings

## q001 — おすすめのプロジェクト管理ツールは？

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Trello | 1 | 2 | 1 | 2 |
| Asana | 2 | 1 | 2 | 1 |
| Notion | 3 | 3 | 3 | 5 |
| Backlog | 4 | 4 |  | 3 |
| Jira |  | 5 | 6 | 4 |
| monday.com | 6 | 6 | 5 |  |
| ClickUp | 7 |  | 4 |  |
| Jira Software | 5 |  |  |  |
| Bitrix24 |  |  |  | 6 |
| GitHub Projects |  |  | 7 |  |
| Microsoft Project |  |  | 8 |  |
| Wrike |  |  | 9 |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

All four systems recommended overlapping project-management tools — Asana, Trello, Notion, and Jira recurred across systems — with Claude widest (nine entities including GitHub Projects, Microsoft Project, Wrike) and Perplexity narrowest (four main picks plus Notion and Bitrix24). Only Perplexity carried inline citations and terminal sources (count 20); no system produced code.

## q002 — What is the best CRM for small businesses?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| HubSpot CRM | 1 | 1 | 1 | 2 |
| Zoho CRM | 2 | 2 | 2 | 1 |
| Pipedrive | 3 | 3 | 3 | 3 |
| Less Annoying CRM |  | 4 | 6 |  |
| Salesforce |  |  | 7 | 4 |
| Freshsales |  | 5 | 5 |  |
| Copper | 4 |  |  |  |
| Close |  |  | 4 |  |
| Monday.com CRM | 5 |  |  |  |
| Bigin by Zoho CRM |  |  |  | 5 |
| Salesforce Starter |  | 6 |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

Strong canonical convergence: HubSpot CRM, Zoho CRM, and Pipedrive appeared in all four systems, though defaults differed (ChatGPT/Gemini/Claude led with HubSpot, Perplexity defaulted to Zoho CRM). Perplexity alone attached inline citations and terminal sources (count 20); the other three had none.

## q003 — 睡眠の質を上げる方法を教えて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 朝に日光を浴びる |  | 2 |  | 2 |
| 寝る前のスマホ・PCを控える |  | 3 |  | 3 |
| 起きる時間を固定する |  | 1 |  |  |
| 起床時間を一定にする |  |  |  | 1 |
| カフェインは午後以降控える |  | 4 |  |  |
| 夕食は寝る2〜3時間前まで |  |  |  | 4 |
| 寝る前の飲酒を避ける |  | 5 |  |  |
| 就寝前のぬるめの入浴 |  |  |  | 5 |
| 寝室を快適にする |  | 6 |  |  |
| 日中の運動 |  |  |  | 6 |
| 寝る前のルーティンを作る |  | 7 |  |  |
| 寝室環境を整える |  |  |  | 7 |
| 入浴は寝る1〜2時間前に |  | 8 |  |  |
| カフェイン・アルコールの摂取時間に注意 |  |  |  | 8 |
| 昼寝は短めにする |  | 9 |  |  |
| 寝床で考え事をしない |  | 10 |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

This sleep-quality query returned no product/tool entities from Gemini or Claude (coded empty), while ChatGPT and Perplexity enumerated overlapping Japanese sleep-hygiene tips (both include 起床/起きる時間の固定, 朝の日光, 寝る前のスマホ・PC抑制). Only Perplexity used inline numeric citations (terminal_source_count 20); no code from any system.

## q004 — How do I implement RAG with a vector database?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Qdrant | 7 | 5 | 4 | 1 |
| Weaviate | 9 | 4 | 3 | 5 |
| Chroma |  | 1 | 1 | 3 |
| LangChain | 2 |  | 7 | 8 |
| Pinecone | 5 | 3 | 2 |  |
| Milvus | 6 | 6 |  | 4 |
| FAISS |  | 2 | 6 |  |
| pgvector | 8 |  | 5 |  |
| OpenAI embeddings |  | 7 |  | 6 |
| LlamaIndex |  |  | 8 | 9 |
| Python | 1 |  |  |  |
| pgvector/Postgres |  |  |  | 2 |
| ChromaDB | 3 |  |  |  |
| OpenAI | 4 |  |  |  |
| sentence-transformers |  |  |  | 7 |
| Cohere embeddings |  | 8 |  |  |
| Hugging Face sentence-transformers |  | 9 |  |  |
| Cohere | 10 |  |  |  |
| Voyage AI embeddings |  | 10 |  |  |
| HuggingFace | 11 |  |  |  |
| OpenAI GPT models |  | 11 |  |  |
| Anthropic Claude |  | 12 |  |  |
| Mistral |  | 13 |  |  |
| Llama-based local models |  | 14 |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(16)._

### Interpretation

The only query eliciting code from every system (4/4). Tool stacks overlapped heavily — Chroma/ChromaDB, Pinecone, Weaviate, Qdrant, Milvus, LangChain, and OpenAI embeddings recurred across systems, with LlamaIndex, pgvector, FAISS, and sentence-transformers variously added. Perplexity again uniquely provided inline citations and terminal sources (count 16, its lowest this session).

## q005 — 日本の代表的なAI研究者を5人挙げて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 松尾豊 | 2 | 2 | 1 | 1 |
| 辻井潤一 | 5 | 4 | 4 |  |
| 甘利俊一 |  | 1 | 2 |  |
| 石黒浩 |  |  | 5 | 2 |
| 杉山将 | 3 | 3 |  |  |
| 福島邦彦 | 1 |  |  |  |
| 中島秀之 |  |  | 3 |  |
| 原田達也 |  |  |  | 3 |
| 北野宏明 | 4 |  |  |  |
| 山岸順一 |  |  |  | 4 |
| 長尾真 |  | 5 |  |  |
| 小野順貴 |  |  |  | 5 |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

Sharpest divergence of the session: 松尾豊 was the only researcher named by all four systems, with each list otherwise distinct (e.g., Gemini's 福島邦彦/北野宏明, ChatGPT's 甘利俊一/長尾真, Claude's 中島秀之/石黒浩, Perplexity's 原田達也/山岸順一/小野順貴). Per the coding guardrail, no gender inference is drawn from these names. Only Perplexity supplied inline citations and terminal sources (count 20).

---

## Methodological Notes

Query set operational v0.1.1 was run against four systems (Gemini gemini-3.5-flash, ChatGPT gpt-5.5-2026-04-23, Claude claude-opus-4-8, Perplexity sonar), all in API mode with 5/5 queries OK each (20/20 observations); no systems were excluded, skipped, or errored. Consistent with the immutable historical fact, this was a continued API-based collection, not a first or transitional API observation. One minor consistency note: Perplexity's terminal_sources flag is 'yes' across all five queries, but the note text for q002, q003, q004, and q005 states 'no terminal source list' despite terminal_source_count values (16–20) being recorded.

---

## Day 17 One-Sentence Conclusion

A clean 20/20 API session in which Perplexity remained the only citing system (5/5), code appeared exclusively on the RAG query (4/4), and canonical stability was high for tooling queries but collapsed for the Japanese-AI-researcher query where only 松尾豊 was universal.
