# 14th Observation — 2026-08-04

> **Correction — 14 August 2026:** An earlier version of this report incorrectly described Day 14 as the first API-collected session. MIBO Pilot collection has been API-based continuously since Day 1 (5 May 2026). This documentation correction does not change the Day 14 observation count, outputs, or coded data.

<!-- mibo:manual -->

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

> Automatically generated from this session's verbatim responses by `render_observation.py` — entity tables from the coded data; narrative by claude-opus-4-8 (2026-08-11T21:30:04+09:00).

---

## Executive Summary

Day 14 continues the API-based MIBO Pilot sequence, and all four systems (Gemini, ChatGPT, Claude, Perplexity) returned 5/5 responses with no exclusions. Perplexity carried inline numeric citations on all 5/5 responses with terminal sources delivered in the preserved packet through the API `citations` array (q001–q005: 20, 20, 19, 20, 20), while the other three systems again supplied zero citations across all 15 responses. The q005 person query produced a notable Law VII event: Arai Noriko (新井紀子) appeared inside Claude's five-person main list, the only female-presenting mention in an otherwise 19/20 male-presenting session. Canonical inclusion cores held for q001 (project-management tools) and q002 (CRMs) despite membership fluctuation, and Perplexity again returned zero scholarly citations, consistent with Law VIII.

---

## Law Status

- **Law I — Canonical Inclusion**: Confirm. q001 shows a durable nucleus — Asana, Trello, Backlog, Notion, and Jira appear across all four systems (with monday.com in three) — while list length varies from 6 (Gemini, Perplexity) to 9 (Claude), consistent with a stable core plus fluctuating periphery. q002 similarly shows HubSpot CRM and Pipedrive across all four and Zoho CRM in three of four.
- **Law II — Perplexity URL Stability**: Insufficient-evidence. This session's coded data reports terminal source counts (20, 20, 19, 20, 20) but no normalized-URL retention values against prior waves, so multi-lag URL survival cannot be judged here.
- **Law III — Day 2 Anomaly**: Insufficient-evidence. Nothing in Day 14's data bears on the localized 2026-05-12 anomaly.
- **Law VI — Per-Model Signature**: Confirm. Distinct signatures persist: Claude closes q001 and q002 with follow-up clarifying questions; ChatGPT uses comparison tables and a concluding favorite (HubSpot CRM/Zoho CRM on q002, highlighted top-three on q003); Gemini produces categorized guides with pricing and decision guides; Perplexity uniquely carries inline citations. All three of the code-flagged q004 responses (Gemini, ChatGPT, Claude) retain their characteristic implementation styles.
- **Law VII — Gender Dominance in Person Queries**: Strengthen. q005 produced 19/20 male-presenting and 1/20 female-presenting main-list mentions — Arai Noriko (新井紀子) inside Claude's five-person list — bringing the cumulative to 234/240 male-presenting versus 6/240 female-presenting, matching the stated Day 14 tally.
- **Law VIII — Absence of Stable Direct Academic Grounding**: Confirm. Perplexity supplied terminal sources on all 5 queries (via the API `citations` array) but the coded data records no peer-reviewed, arXiv, or first-party scholarly citations; source presence remains the norm without stable scholarly grounding.
- **Law IX — Perplexity Inline Citation Shift**: Confirm/strengthen. Perplexity showed inline numeric citations plus terminal sources on 5/5 responses, extending inline-plus-terminal continuity since Day 4. The twenty-source regime held on 4/5 queries (q003 returned 19), consistent with the reported 19/20.

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

Strong cross-system agreement on a project-management core: Asana, Trello, Backlog, Notion, and Jira appear in all four systems, with monday.com in three; list lengths diverge from Gemini's 6 to Claude's 9 (which adds Linear). Only Perplexity carried inline citations and a 20-source terminal list; the other three cited nothing.

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

HubSpot CRM and Pipedrive appear across all four systems and Zoho CRM in three, but divergence is wider than q001 — Claude returns 8 CRMs and Perplexity uniquely leads with Bigin by Zoho CRM and Salesforce. Perplexity alone cited sources (20 terminal), while Gemini, ChatGPT, and Claude gave uncited recommendations.

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

This Japanese sleep-hygiene query showed thematic convergence (morning sunlight, fixed wake time, limiting evening screens, bathing 1–2 hours before bed) but no shared canonical entity list, and Claude returned no coded entities. Only Perplexity attached inline citations, with 19 terminal sources (the sole query under the 20-source regime this session).

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

All four systems agreed on a vector-database core — Chroma, Pinecone, Weaviate, and Qdrant appear across all four, with FAISS and Milvus in most — and all four included code. Only Perplexity carried inline citations (20 terminal sources); Gemini, ChatGPT, and Claude gave uncited implementation tutorials.

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

松尾豊 (Matsuo) and 甘利俊一 (Amari) appear in all four systems and 石黒浩 (Ishiguro) in three, forming a stable researcher core, while peripheral picks diverge (Gemini's 福島邦彦, Perplexity's 栗原聡/松原仁). Claude's inclusion of 新井紀子 (Arai Noriko) is the session's only female-presenting main-list mention; only Perplexity cited sources (20 terminal).

---

## Methodological Notes

This session continues API-based collection under query set operational v0.1.1; all four systems (Gemini gemini-3.5-flash, ChatGPT gpt-5.5-2026-04-23, Claude claude-opus-4-8, Perplexity sonar) returned 5/5 with no excluded systems. In this preserved structured packet, terminal sources for Perplexity are read from the API `citations` array rather than rendered answer text, and each Perplexity note states 'no terminal source list' despite a reported terminal_source_count — a response-representation discrepancy worth flagging. Claude's q003 returned no coded entities.

---

## Day 14 One-Sentence Conclusion

This continuing API-based Pilot session preserved durable canonical cores and per-model signatures while Perplexity remained the sole citing system, and Claude's inclusion of Arai Noriko delivered the session's only female-presenting person mention.
