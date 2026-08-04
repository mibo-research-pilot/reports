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

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-04T21:17:22+09:00).

---

## Executive Summary

Day 14 is the first API-collected session, and the instrument change is the headline: Perplexity's terminal sources now arrive via the API `citations` array rather than rendered answer text, yet inline numeric markers persist on all 5/5 responses, bringing inline-plus-terminal continuity to 55/55 since Day 4. Per-model signatures remain sharply legible — Gemini's categorized pricing guides, ChatGPT's comparison tables, Claude's follow-up clarifying questions, and Perplexity's inline-cited concise lists all recur. Law VII is strengthened: 19/20 Japanese-researcher mentions were male-presenting, with the sole female-presenting mention (Arai Noriko / 新井紀子) appearing inside Claude's five-person main list. Perplexity's terminal source classes again spanned comparison media, video, health/institutional, and aggregator sources with zero scholarly citations, consistent with Law VIII.

---

## Law Status

- **Law I — Canonical Inclusion**: Confirm. q001 shows a durable nucleus (Asana, Trello, Notion, Backlog, Jira/monday.com appear across all four systems) while peripheral entities and counts fluctuate — Gemini returned 6, ChatGPT 8, Claude 9, Perplexity 6 tools — supporting a stable core with variable periphery and order.
- **Law II — Perplexity URL Stability**: Insufficient-evidence this session. The coded data reports only terminal_source_count per query (q001–q005: 20, 20, 19, 20, 20) with no normalized-URL survival, retained-share, or citation-index reassignment data, so multi-lag continuity cannot be measured from this packet.
- **Law III — Day 2 Anomaly**: Insufficient-evidence. This is a Day 14 session with no re-observation of the 2026-05-12 anomaly window; nothing in the data bears on it.
- **Law VI — Per-Model Signature**: Confirm. Signatures persist across all five queries: Gemini gives categorized recommendations with pricing and decision guides (q001, q002), ChatGPT favors comparison tables and use-case framing (q001, q002, q004), Claude ends with follow-up clarifying questions (q001, q002), and Perplexity delivers concise inline-cited lists (all five). Code depth also differs on q004 while all four still supply RAG code.
- **Law VII — Gender Dominance in Person Queries**: Strengthen. q005 produced 19/20 male-presenting main-list mentions and 1/20 female-presenting — Arai Noriko (新井紀子) inside Claude's five-person list — bringing the cumulative to 234/240 male vs 6/240 female, consistent with the established formulation.
- **Law VIII — Absence of Stable Direct Academic Grounding**: Confirm. Perplexity supplied terminal sources on all applicable queries (counts 20/20/19/20/20) but the data records zero peer-reviewed, arXiv, or first-party scholarly citations; no stable direct academic grounding is present, consistent under continuing audit.
- **Law IX — Perplexity Inline Citation Shift**: Confirm/strengthen. Inline numeric citations appear on 5/5 Perplexity responses, and with terminal sources now read from the API `citations` array, inline-plus-terminal continuity reaches 55/55 since Day 4. The twenty-source regime held on 4/5 queries (q003 returned 19), for a 19/20 session tally.

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

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

Strong cross-system agreement on a project-management core — Asana, Trello, Notion, Backlog, and Jira recur across all four systems — while list length varies (Gemini 6, ChatGPT 8, Claude 9, Perplexity 6) and peripheral picks (ClickUp, Linear, GitHub Projects) diverge. Only Perplexity carried inline citations with 20 terminal sources; the other three cited nothing.

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

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

Systems converge on HubSpot CRM, Zoho CRM, and Pipedrive but diverge on periphery: ChatGPT adds Freshsales/Salesforce Starter, Claude expands to eight including Copper and Dynamics 365, and Perplexity leads with Bigin by Zoho and Salesforce. Perplexity alone cited (inline, 20 terminal sources); Gemini and Claude closed with decision guides and follow-up questions respectively.

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

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(19)._

### Interpretation

This sleep-hygiene query shows thematic agreement (morning sunlight, fixed wake time, limiting screens, warm bath before bed) but no shared canonical entities since the tips are phrased freely per system. Claude returned no coded entities (prose advice), Perplexity cited inline with 19 terminal sources — the session's only sub-20 count — while Gemini and ChatGPT cited nothing.

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

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

All four systems produced RAG implementation guides with code (code flag 'yes' across the board) and converged on vector databases (Chroma, Pinecone, Weaviate, Qdrant, FAISS recur), diverging on breadth — ChatGPT enumerated the most embedding/reranker options, Claude the fewest with RAGAS added. Only Perplexity cited (inline, 20 terminal sources); the others embedded code without any source list.

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

_Citations — Gemini: inline=no/terminal=no, ChatGPT: inline=no/terminal=no, Claude: inline=no/terminal=no, Perplexity: inline=yes/terminal=yes(20)._

### Interpretation

Japanese AI researcher lists agree tightly on 松尾豊 and 甘利俊一 (each in all or most lists) and 石黒浩, while diverging on the remaining slots (福島邦彦, 杉山将, 辻井潤一, 中島秀之, 栗原聡, 松原仁, 岡野原大輔). Claude's list uniquely included 新井紀子 (Arai Noriko), the sole female-presenting mention; only Perplexity attached inline citations with 20 terminal sources.

---

## Methodological Notes

This is the first API-collected session under query set operational v0.1.1; all four systems (Gemini gemini-3.5-flash, ChatGPT gpt-5.5-2026-04-23, Claude claude-opus-4-8, Perplexity sonar) returned 5/5 successful queries with no exclusions or errors. The instrument change matters: Perplexity's terminal sources are now read from the API `citations` array (counts 20/20/19/20/20) rather than the answer text, so several notes stating 'no terminal source list' reflect answer-body rendering rather than absence of sources. One anomaly: Claude returned no coded entities for q003, delivering prose sleep advice without discrete listed items.

---

## Day 14 One-Sentence Conclusion

Under the new API collection regime, per-model signatures and Perplexity's inline citation behavior held firm while male dominance in the Japanese-researcher query strengthened, softened only by Claude's inclusion of Arai Noriko.
