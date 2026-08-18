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

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-18T20:26:09+09:00).

---

## Executive Summary

All four systems (Gemini, ChatGPT, Claude, Perplexity) returned successfully on all 5 queries with no exclusions. Perplexity was the sole system exhibiting inline-citation behavior, doing so on every one of its 5 responses, while carrying a terminal_source_count (17–20) despite the coded note that no terminal source list was rendered in-body. Code output clustered exclusively on the RAG query (q004), where all four systems produced code. Canonical/entity stability was strong on the domain-tool queries (q001, q002, q004) and on the single anchor entity 松尾豊 (q005), but the sleep-hygiene query (q003) showed high coding divergence.

---

## Law Status

- The authoritative law list (core/laws.md) was unavailable this run, so no established laws can be referenced by id or name, and no confirm/revise/withdraw judgments are assigned this session. Summarizing the citation/canonical evidence instead: Perplexity (sonar) was the only system showing inline-citation behavior, and it did so uniformly across all 5/5 queries; the other three systems (Gemini, ChatGPT, Claude) showed inline_citations=no and terminal_sources=no on all 5/5 responses. Perplexity's coded observations consistently flag `inline_citations: yes` and `terminal_sources: yes` but with a note that no terminal source list appeared in-body, alongside a terminal_source_count of 17–20 (q001=20, q002=18, q003=20, q004=17, q005=20) — a tension worth carrying forward. Code output appeared only on q004 (RAG), where all four systems emitted code. Canonical stability: 松尾豊 appeared in all four systems on q005; HubSpot CRM, Zoho CRM, and Pipedrive appeared in all four on q002; Trello/Notion/Asana/Jira and monday.com recurred across systems on q001.

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

All four systems recommended project-management tools with strong overlap — Trello, Notion, Asana, Jira, and monday.com recur across systems, with Backlog and Wrike shared by Gemini, ChatGPT, and Perplexity. Counts ranged from 7 (Gemini, Claude, Perplexity) to 9 (ChatGPT). Only Perplexity carried inline citations (terminal_source_count 20); none produced code.

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

High canonical agreement on small-business CRMs: HubSpot CRM, Zoho CRM, and Pipedrive appeared in all four systems, with Salesforce shared by Claude and Perplexity and Copper/Freshsales shared by ChatGPT and Claude. Entity counts spanned 5 (Gemini, Perplexity) to 7 (Claude). Only Perplexity showed inline citations (terminal_source_count 18).

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

This Japanese sleep-quality query showed the widest divergence in coded entities: Gemini returned no discrete entities (prose advice), Claude coded only 2 tips, ChatGPT coded 10, and Perplexity coded 8. Despite differing granularity, the shared advice cores (fixed wake time, morning light, limiting pre-sleep screens) recur; only Perplexity carried inline citations (terminal_source_count 20), and both ChatGPT and Perplexity closed with advice to consult a doctor.

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

The RAG query was the sole trigger for code across the board — all four systems produced code (code=yes). Vector databases showed strong overlap (Chroma/ChromaDB, FAISS, Pinecone, Qdrant, Milvus, pgvector recur), and embedding models like all-MiniLM-L6-v2 and OpenAI text-embedding-3 variants appeared in multiple systems; Gemini listed the most entities (18). Only Perplexity added inline citations (terminal_source_count 17).

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

All four systems named five Japanese AI researchers, with 松尾豊 the single universal anchor entity across all systems; 杉山将 appeared in all four and 甘利俊一 in Gemini, ChatGPT, and Claude, while the remaining names diverged (e.g., 石黒浩 in Claude and Perplexity, 福島邦彦/北野宏明 unique to Gemini). Only Perplexity carried inline citations (terminal_source_count 20).

---

## Methodological Notes

All four systems ran in API mode and returned ok on all 5/5 queries with zero excluded systems, using query set operational v0.1.1; collection ran 2026-08-18T20:21:47 to 20:25:14 (+09:00). One coding anomaly recurs across all Perplexity observations: terminal_sources is flagged `yes` with a terminal_source_count of 17–20, yet each note states no terminal source list was rendered in-body — this inline-vs-terminal flag tension should be reconciled in the codebook. No gender coding was performed on the q005 researcher names, per the prospective coding guardrail.

---

## Day 16 One-Sentence Conclusion

A clean full-panel session (4 systems, 5/5 each) reaffirming Perplexity as the lone inline-citing system, code output confined to the RAG query, and stable canonical entities anchored by 松尾豊 and the HubSpot/Zoho/Pipedrive CRM cluster.
