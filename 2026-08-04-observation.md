# 14th Observation — 2026-08-04

**Observatory**: MIBO — Machine Information Behavior Observatory  
**Japanese name**: 機械情報行動観測所  
**Observation date**: 2026-08-04  
**Timezone**: Asia/Tokyo  
**Core method**: Longitudinal Machine Observation (LMO)  
**Observation mode**: API collection (automated)  
**Included systems**: Gemini (gemini-3.5-flash), ChatGPT (gpt-5.5-2026-04-23), Claude (claude-opus-4-8), Perplexity (sonar)  
**Excluded systems**: none  
**Included observations this session**: 20  
**Cumulative MIBO observations after this session**: 264  
**Collection window**: 2026-08-04T20:33:02.089325+09:00 → 2026-08-04T20:36:59.845790+09:00  
**Raw responses**: [`2026-08-04/raw-responses.md`](2026-08-04/raw-responses.md) (verbatim API outputs)  

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-04T20:49:36+09:00).

---

## Executive Summary

All four systems (Gemini, ChatGPT, Claude, Perplexity) returned successful responses to all five queries with no exclusions this session. Canonical anchors held firmly: Asana appeared in every q001 response, HubSpot CRM in every q002 response, and Matsuo Yutaka (松尾豊) in all but Gemini's q005 list — while Amari Shun'ichi (甘利俊一) appeared in all four q005 responses. Perplexity attached inline [n] citation markers to every one of its five responses while producing zero terminal source lists, and no system emitted any academic or arXiv citation. Notably, Claude returned an empty coded-entity set for q003 (sleep-quality tips), the only such gap this session.

---

## Law Status

- **Law I (Absolute Canonical):** Confirm. Asana appeared in all 4/4 q001 responses; HubSpot CRM in all 4/4 q002 responses; Matsuo Yutaka (松尾豊) in 3/4 q005 responses (absent only from Gemini) with Amari Shun'ichi (甘利俊一) present in 4/4 q005 responses.
- **Law II (Perplexity URL Stability):** Insufficient-evidence. Perplexity produced no terminal source list on any of its 5 responses this session, so no cited URLs are available to assess week-to-week persistence.
- **Law III (Day 2 Anomaly):** Insufficient-evidence. This is a historical, non-recurring event from 2026-05-12; nothing in this Day 14 data bears on it.
- **Law VI (Per-Model Signature):** Confirm. Claude closed with follow-up/clarifying questions on q001 and q002; ChatGPT used comparison tables and concluding summaries (q001, q002) and appended a doctor-consultation caveat on q003; Perplexity uniquely carried inline citations across all 5 responses.
- **Law VII (Gender Bias in Person Queries):** Strengthen. Across the four q005 lists, the sole female mention is Arai Noriko (新井紀子) in Claude's list; Gemini, ChatGPT, and Perplexity returned all-male five-name lists, consistent with the female recurrence appearing in Claude's response.
- **Law VIII (Universal Absence of Academic Citations):** Confirm. Perplexity cited zero academic papers or arXiv entries across all 5 queries (and produced no terminal sources at all).
- **Law IX (Perplexity Inline Citation Shift):** Confirm. Perplexity attached inline [n] markers to all 5/5 of its responses while using no end-of-response bulk source list.

---

## Query-Level Findings

## q001 — おすすめのプロジェクト管理ツールは？

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Backlog | 1 | 6 | 9 | 2 |
| Trello | 2 | 2 | 1 | 4 |
| Asana | 3 | 1 | 2 | 1 |
| Notion | 6 | 3 | 3 | 6 |
| Monday.com | 4 | 8 | 5 | 5 |
| Jira |  | 4 | 6 | 3 |
| ClickUp |  | 7 | 4 |  |
| GitHub Projects |  | 5 | 7 |  |
| Jira Software | 5 |  |  |  |
| Linear |  |  | 8 |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=no._

### Interpretation

All four systems recommended project-management tools, with Asana (4/4), Trello (4/4), Notion (4/4), Backlog (4/4), Jira, and monday.com forming a broad shared core; list length varied from Perplexity's 5 to Claude's 9. Only Perplexity used inline citations; no system provided a terminal source list.

## q002 — What is the best CRM for small businesses?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| HubSpot CRM | 1 | 1 | 1 | 3 |
| Pipedrive | 2 | 3 | 2 | 4 |
| Zoho CRM | 3 | 2 | 3 |  |
| Freshsales |  | 4 | 4 |  |
| Less Annoying CRM | 5 |  | 8 |  |
| Bigin by Zoho CRM |  |  |  | 1 |
| Salesforce |  |  |  | 2 |
| Monday.com | 4 |  |  |  |
| Salesforce Starter |  | 5 |  |  |
| Copper |  |  | 5 |  |
| Insightly |  |  | 6 |  |
| Dynamics 365 |  |  | 7 |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=no._

### Interpretation

HubSpot CRM (4/4), Pipedrive (4/4), and Zoho CRM (in HubSpot/Zoho form, 4/4) anchored the CRM recommendations, though Perplexity uniquely surfaced Bigin by Zoho CRM and Salesforce rather than the plain listings. Divergence widened at the edges (Claude listed eight including Copper, Insightly, Dynamics 365); only Perplexity carried inline citations, with no terminal sources anywhere.

## q003 — 睡眠の質を上げる方法を教えて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 日中に適度な運動をする | 2 |  |  | 6 |
| 夕食は寝る3時間前までに済ませる | 7 |  |  | 7 |
| 朝起きたらすぐに日光を浴びる | 1 |  |  |  |
| 起きる時間を固定する |  | 1 |  |  |
| 毎日ほぼ同じ時間に起きる |  |  |  | 1 |
| 朝に日光を浴びる |  | 2 |  |  |
| 朝起きたら日光を浴びる |  |  |  | 2 |
| 昼寝は午後3時までに20分以内 | 3 |  |  |  |
| カフェインは午後以降控える |  | 3 |  |  |
| 夜はスマホ・PCを控える |  |  |  | 3 |
| お風呂は就寝の90分前に湯船に浸かる | 4 |  |  |  |
| 寝る前のスマホ・PCを減らす |  | 4 |  |  |
| 寝室を快適に保つ |  |  |  | 4 |
| 寝る1〜2時間前はスマホやPCを見ない | 5 |  |  |  |
| 寝室を快適にする |  | 5 |  |  |
| 就寝前に入浴して体を温める |  |  |  | 5 |
| カフェインとアルコールのコントロール | 6 |  |  |  |
| 寝る前のルーティンを作る |  | 6 |  |  |
| 入浴は寝る1〜2時間前 |  | 7 |  |  |
| トリプトファンを含む食材を摂る | 8 |  |  |  |
| 昼寝は短めにする |  | 8 |  |  |
| 昼寝は短くする |  |  |  | 8 |
| 室温と湿度を適切に保つ | 9 |  |  |  |
| お酒に頼らない |  | 9 |  |  |
| 寝室を暗く、静かにする | 10 |  |  |  |
| 眠れないときは一度ベッドを出る |  | 10 |  |  |
| 自分に合った寝具を選ぶ | 11 |  |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=no._

### Interpretation

The three systems with coded entities converged on stable sleep-hygiene themes — morning sunlight, fixed wake time, limiting pre-bed screens, comfortable bedroom, and bathing 1–2 hours before sleep. Claude returned an empty entity set here (a structured but unnamed-item guide), and only Perplexity attached inline citations while providing no terminal sources.

## q004 — How do I implement RAG with a vector database?

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| Pinecone | 5 | 3 | 2 | 1 |
| Weaviate | 6 | 4 | 3 | 2 |
| Qdrant | 7 | 5 | 4 | 3 |
| Chroma |  | 1 | 1 | 6 |
| FAISS | 4 | 2 |  | 5 |
| LangChain | 1 |  | 8 |  |
| Milvus |  | 6 |  | 4 |
| pgvector | 8 |  | 5 |  |
| OpenAI | 9 |  | 7 |  |
| Cohere Rerank |  | 17 | 9 |  |
| LlamaIndex | 2 |  |  |  |
| ChromaDB | 3 |  |  |  |
| sentence-transformers |  |  | 6 |  |
| PostgreSQL + pgvector |  | 7 |  |  |
| OpenAI text-embedding-3-small/large |  | 8 |  |  |
| Cohere embeddings |  | 9 |  |  |
| Cohere | 10 |  |  |  |
| Voyage embeddings |  | 10 |  |  |
| RAGAS |  |  | 10 |  |
| HuggingFace | 11 |  |  |  |
| Hugging Face/Sentence Transformers |  | 11 |  |  |
| GPT-4o | 12 |  |  |  |
| BGE embeddings |  | 12 |  |  |
| Anthropic | 13 |  |  |  |
| GPT-4.1/GPT-4o |  | 13 |  |  |
| Llama 3 | 14 |  |  |  |
| Claude |  | 14 |  |  |
| Ollama | 15 |  |  |  |
| Gemini |  | 15 |  |  |
| BGE-Reranker | 16 |  |  |  |
| Llama/Mistral |  | 16 |  |  |
| BGE reranker |  | 18 |  |  |
| Jina reranker |  | 19 |  |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=no._

### Interpretation

All four gave RAG implementation guides and were flagged as containing code. Vector databases were the shared backbone — Weaviate and Qdrant appeared in all 4, with Chroma, FAISS, and Pinecone near-universal — while Gemini and ChatGPT went further into embedding models, rerankers, and frameworks (LangChain, LlamaIndex). Only Perplexity used inline citations; no system listed terminal sources.

## q005 — 日本の代表的なAI研究者を5人挙げて

### Entities by system

_Each cell is the entity's rank in that system's answer (blank = not mentioned)._

| Entity | Gemini | ChatGPT | Claude | Perplexity |
|---|---:|---:|---:|---:|
| 甘利俊一 | 2 | 1 | 2 | 5 |
| 松尾豊 | 3 | 2 | 1 | 1 |
| 石黒浩 |  | 5 | 4 | 2 |
| 杉山将 | 4 | 3 |  |  |
| 福島邦彦 | 1 |  |  |  |
| 中島秀之 |  |  | 3 |  |
| 栗原聡 |  |  |  | 3 |
| 辻井潤一 |  | 4 |  |  |
| 松原仁 |  |  |  | 4 |
| 岡野原大輔 | 5 |  |  |  |
| 新井紀子 |  |  | 5 |  |

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=no._

### Interpretation

Amari Shun'ichi (甘利俊一) appeared in all 4 lists and Matsuo Yutaka (松尾豊) in 3/4 (absent from Gemini), while Ishiguro Hiroshi (石黒浩) recurred in 3/4. The lists otherwise diverged on secondary names (e.g., Fukushima Kunihiko, Tsujii Jun'ichi, Nakajima Hideyuki, Kurihara Satoshi), and Arai Noriko (新井紀子) in Claude's list was the only female researcher named; Perplexity alone used inline citations.

---

## Methodological Notes

All four systems ran under query_set_id 'operational v0.1.1' via API with 5/5 successful responses each and no excluded systems. Model versions matched requests (Gemini gemini-3.5-flash, ChatGPT gpt-5.5-2026-04-23, Claude claude-opus-4-8, Perplexity sonar); the only notable anomaly was Claude's empty coded-entity set for q003, which reflects a guide without specific named items rather than a collection error.

---

## Day 14 One-Sentence Conclusion

A clean full-coverage session that reaffirmed the canonical anchors (Asana, HubSpot CRM, Amari/Matsuo), Perplexity's inline-citation-without-terminal-sources signature, and the male-dominated researcher lists with Arai Noriko as the sole female name in Claude's output.
