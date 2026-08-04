# Second Observation — 2026-05-12

**Observatory**: MIBO (Machine Information Behaviour Observatory)
**Observer**: Kento Sasano
**Date**: 2026-05-12
**Method**: Manual web interface (copy-paste from chat UI)
**Query set**: v0.1 (queries q001–q003, partial)
**Models observed**:
- OpenAI ChatGPT (GPT-5.4)
- Anthropic Claude (claude-opus-4-7)
- Google Gemini (Gemini 3.0 Flash)
- Perplexity (Web search mode)

**Total observations this session**: 12 (4 models × 3 queries)

**Note**: q004 and q005 deferred to subsequent observation sessions.

---

## Methodology

This is the second observation of MIBO, conducted exactly one week after
Day 1 (2026-05-05). The observation methodology is identical to Day 1
to ensure longitudinal comparability:

- Same four AI systems
- Same standardised queries (q001-q003 from v0.1 query set)
- Manual web interface
- Verbatim response recording
- Same observer (Kento Sasano)

**Key longitudinal questions for Day 2**:
- Has the "canonical core" for project management / CRM held?
- Has Perplexity's citation source pattern remained stable?
- Have per-model response signatures persisted?
- Are there any visible model-version updates since 2026-05-05?

q004 and q005 will be observed in subsequent sessions (these were not
observed on Day 1; baseline establishment can occur later without
affecting the longitudinal value of q001-q003).

---

## q001 — おすすめのプロジェクト管理ツールは？

**Category**: product_recommendation | **Language**: ja
**First observed**: 2026-05-05 | **This observation**: 2026-05-12

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-12T__:__:__+09:00

```
### 目的別・おすすめのプロジェクト管理ツール

プロジェクトの規模や性質に応じて、最適なツールを選択する必要があります。

#### 1. 汎用性・ナレッジ共有重視

* **Notion**
    * **特徴**: ドキュメント作成、タスク管理、データベースを一つのワークスペースに集約できる。
    * **強み**: 自由度が極めて高く、独自の管理システムを構築可能。
    * **適した対象**: 個人開発者、スタートアップ、社内Wikiとタスク管理を統合したいチーム。
* **Asana**
    * **特徴**: リスト、ボード、タイムライン、カレンダーなど、用途に合わせて表示を切り替えられる。
    * **強み**: 誰が・いつまでに・何をやるかが明確になり、タスクの依存関係の把握に強い。
    * **適した対象**: 中〜大規模なチーム、複数のプロジェクトを並行して進める組織。

#### 2. 直感的な操作・小規模チーム向け

* **Trello**
    * **特徴**: 「カンバン方式」の代表格で、カードをドラッグ＆ドロップして進捗を管理する。
    * **強み**: 学習コストがほぼゼロで、視覚的に進捗を把握しやすい。
    * **適した対象**: シンプルなプロセスを好むチーム、個人のToDo管理。

#### 3. ソフトウェア開発・アジャイル向け

* **Jira Software**
    * **特徴**: スクラムやカンバンなど、アジャイル開発に特化した高度な機能を備える。
    * **強み**: バグトラッキング、バックログ管理、リリースサイクルの分析機能が強力。
    * **適した対象**: エンジニア中心の開発チーム、大規模なソフトウェアプロジェクト。

#### 4. 日本国内のチーム・非エンジニア混合

* **Backlog**
    * **特徴**: 日本発のツールで、ガントチャート、Wiki、Git連携が標準搭載されている。
    * **強み**: UIが親しみやすく、エンジニア以外の職種(営業や事務)でも使いこなしやすい。
    * **適した対象**: 国内のクライアントワーク、多職種が協力するプロジェクト。

#### 5. 自動化・多機能重視

* **monday.com**
    * **特徴**: 業務フローをノーコードで柔軟にカスタマイズできる。
    * **強み**: 「ステータスが変わったら通知を送る」といった自動化設定が非常に容易。
    * **適した対象**: 業務の定型化・効率化を最優先するチーム。
* **ClickUp**
    * **特徴**: 「一つのアプリですべての業務を代替する」ことを目指した超多機能ツール。
    * **強み**: 無料プランでも利用できる機能が非常に多く、ドキュメントから目標管理まで完結する。
    * **適した対象**: ツールを一つに集約してコストを抑えたいチーム。

---

### 選定のポイント

1. **管理手法**: カンバン(Trello/Notion)、ガントチャート(Backlog/Asana)、スクラム(Jira)のどれが必要か。
2. **チームのITリテラシー**: 導入後に全員が使いこなせる操作感か。
3. **連携性**: Slack、Google Drive、GitHub など、既存のツールと連携できるか。
```

**Mentioned products**: Notion, Asana, Trello, Jira Software, Backlog, monday.com, ClickUp (7 products)
**Explicit URL citations**: None
**Japan-origin tools**: 1 (Backlog)

**Notes vs Day 1**:
- Product count: 6 → 7 (+1)
- Canonical four (Notion/Trello/Asana/Monday) FULLY PRESERVED
- Wrike (in Day 1) → not present in Day 2
- Jira Software → newly added (was absent in Day 1)
- ClickUp → newly added (was absent in Day 1)
- Backlog → preserved with same Japan-domestic framing
- Structural change: Day 1 used product-by-product listing + comparison table.
  Day 2 reorganised into 5 purpose-based categories.
  No comparison table in Day 2.
- Pattern: canonical core fully stable; derivative layer is fluid.

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-12T__:__:__+09:00

```
目的別に選ぶのが一番です。定番はこのあたりです。

- **`Asana`**
  - バランス型
  - タスク管理、タイムライン、担当者管理が強い
  - 非エンジニア含むチームで使いやすい
- **`Trello`**
  - シンプル重視
  - カンバン方式で直感的
  - 小規模チームや個人利用向き
- **`Jira`**
  - 開発チーム向け
  - バグ管理、スプリント、アジャイル運用に強い
  - ソフトウェア開発ではかなり定番
- **`Notion`**
  - 柔軟性重視
  - ドキュメント、Wiki、タスク管理を一体化できる
  - ただし運用設計しないと散らかりやすい
- **`ClickUp`**
  - 多機能
  - タスク、ドキュメント、ダッシュボードなど全部入り寄り
  - 高機能だが最初は少し重いこともある
- **`Monday.com`**
  - 見た目がわかりやすい
  - 営業、マーケ、制作など幅広い部署で使いやすい
  - 可視化や自動化が豊富
- **`Backlog`**
  - 日本企業で使いやすい
  - タスク管理、Wiki、バグ管理がまとまっている
  - 日本語UIやサポート重視なら有力

選び方の目安：

- **個人や小規模チーム**: `Trello`, `Notion`
- **一般的な業務チーム**: `Asana`, `Monday.com`
- **開発チーム**: `Jira`, `Backlog`
- **何でも1つにまとめたい**: `ClickUp`, `Notion`

迷ったら、まずは以下で考えると失敗しにくいです。

1. 開発向けか、一般業務向けか
2. シンプルさ重視か、多機能重視か
3. タスク管理だけでいいか、Wikiや文書も必要か
4. 日本語サポートが重要か

無難なおすすめ3つだけ挙げるなら：

1. **`Asana`**: 万能で導入しやすい
2. **`Jira`**: 開発なら強い
3. **`Notion`**: 柔軟で情報集約しやすい

用途がわかればもっと絞れます。
例えば「個人用」「社内チーム用」「開発案件用」のどれかを教えてもらえれば、3つに厳選して比較できます。
```

**Mentioned products**: Asana, Trello, Jira, Notion, ClickUp, Monday.com, Backlog (7 products)
**Explicit URL citations**: None
**Japan-origin tools**: 1 (Backlog) — NEW vs Day 1

**Notes vs Day 1**:
- Product count: 6 → 7 (+1)
- Canonical four (Notion/Trello/Asana/Monday) FULLY PRESERVED
- Day 1 unique 5/6 products (Jira, ClickUp) preserved
- Backlog NEWLY APPEARS — major change.
  Day 1 had ZERO Japan-origin tools; Day 2 surfaces Backlog
  with explicit "日本企業で使いやすい" / "日本語UIやサポート重視" framing.
- Closing refinement-offer pattern PRESERVED:
  - Day 1: 個人用 / 開発チーム用 / 社内業務用
  - Day 2: 個人用 / 社内チーム用 / 開発案件用
  Three-way categorisation, near-identical structure — strong evidence
  for P5 (model signature persistence).

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-12T__:__:__+09:00

```
# おすすめのプロジェクト管理ツール

用途や規模によって最適なツールが異なるため、目的別に紹介します。

## 総合的に人気の高いツール

### 1. Notion
- **特徴**: ドキュメント・データベース・タスク管理を一元化
- **向いている人**: 小〜中規模チーム、ドキュメント中心の業務
- **料金**: 無料プランあり、有料は$10/ユーザー〜

### 2. Asana
- **特徴**: タスクの依存関係、タイムライン表示が強力
- **向いている人**: 中〜大規模チーム、複数プロジェクトを並行管理
- **料金**: 無料プランあり(15人まで)、有料は$10.99/ユーザー〜

### 3. Trello
- **特徴**: カンバン方式でシンプル、直感的な操作
- **向いている人**: 小規模チーム、個人利用
- **料金**: 無料プランあり、有料は$5/ユーザー〜

## エンジニア・開発チーム向け

### 4. Jira
- **特徴**: アジャイル開発(スクラム・カンバン)に最適、課題管理に強い
- **向いている人**: ソフトウェア開発チーム
- **料金**: 無料プランあり(10人まで)

### 5. Linear
- **特徴**: 高速・モダンなUI、開発者体験を重視
- **向いている人**: スタートアップ、開発チーム
- **料金**: 無料プランあり、有料は$8/ユーザー〜

## 日本企業で人気

### 6. Backlog
- **特徴**: 日本語対応が完璧、ガントチャート・Wiki・Git機能を統合
- **向いている人**: 日本のチーム、受託開発
- **料金**: ¥2,970/月〜(人数無制限)

### 7. kintone
- **特徴**: 業務アプリを自作可能、ノーコードで柔軟
- **向いている人**: 業務プロセス全般を管理したい企業
- **料金**: ¥1,000/ユーザー〜

## 選び方のポイント

| 観点 | おすすめ |
|------|---------|
| 個人・小規模で手軽に | Trello, Notion |
| ドキュメント中心 | Notion |
| 開発チーム | Jira, Linear |
| 日本語サポート重視 | Backlog |
| 大規模・複雑な案件 | Asana, Jira |

## 補足アドバイス

導入前に以下を確認すると失敗しにくいです:

1. **チーム規模と予算**: 無料枠の人数制限を確認
2. **既存ツールとの連携**: Slack, GitHub, Google Workspace等
3. **無料トライアル**: 2週間ほど試用して操作感を確認
4. **学習コスト**: Jiraは高機能だが習得に時間がかかる

具体的な用途やチーム規模を教えていただければ、より絞り込んだ提案ができます。
```

**Mentioned products**: Notion, Asana, Trello, Jira, Linear, Backlog, kintone (7 products)
**Explicit URL citations**: None
**Japan-origin tools**: 2 (Backlog + kintone) — INCREASED from 1 in Day 1

**Notes vs Day 1**:
- Product count: 8 → 7 (-1)
- Core three (Notion/Trello/Asana) PRESERVED
- DROPPED from Day 1: Monday.com, ClickUp, GitHub Projects (3 products)
- NEWLY APPEARED: Linear, kintone (2 products)
- Backlog preserved
- Japan-origin tools: 1 → 2 (kintone newly added with dedicated
  "日本企業で人気" category)
- Claude signature elements ALL PRESERVED:
  * Comparison table ✓
  * Category-based organisation ✓
  * Pricing on every product ✓
  * Closing offer for personalisation ✓
- Major structural change: Monday.com (one of Day 1's "canonical four")
  no longer appears in Claude's Day 2 response.
- New category "日本企業で人気" did not exist in Day 1 response.

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-12T__:__:__+09:00

```
### おすすめのプロジェクト管理ツール

検索結果に基づき、2026年時点で頻出・高評価のプロジェクト管理ツールを用途別にまとめました。主な情報源はITトレンド、ITreview、MSOL、Lychee Redmineなどの比較記事です。Jira、Asana、Backlog、Trelloが複数ソースでトップランクされ、世界的に12万社以上が利用する定番ツールも目立ちます。

#### 総合おすすめトップ5(人気・多機能性で選定)

| ツール名 | 主な強み | 無料プラン | 連携機能 | 情報源 |
|----------|----------|------------|----------|--------|
| **Jira** | タスク/プロジェクト一元管理、世界標準。課題追跡に最適 | あり(10ユーザーまで) | 200以上(Slackなど) | [1][2][4] |
| **Asana** | タスク・プロジェクト特化、視覚的なボード管理 | あり(基本機能) | 200以上(Googleカレンダーなど) | [1][3][5][6] |
| **Backlog** | 担当者・期限明確化、Wiki共有。遅延防止に強い | あり(10ユーザーまで) | 豊富(ヌーラボ製) | [1][2][5][7] |
| **Trello** | シンプルKanbanボード、個人・小チーム向け | あり(無制限) | 多岐(Power-up) | [1][3][6] |
| **Redmine / Lychee Redmine** | カスタマイズ自由、オープンソース。無料重視 | 完全無料 | プラグイン豊富 | [1][3][5] |

#### 用途別おすすめ

- **タスク管理重視**: Asana、Jira、Trello(一元管理・視覚化が魅力)[1]
- **工数・スケジュール管理**: TimeCrowd、みんなでガント.com、Brabio!(ガントチャート・時間追跡)[1][8]
- **中小企業・無料志向**: Backlog、Freedcamp、Quip(Wiki・タスク共有)[5][6][7]
- **多機能・大規模**: Monday.com、ClickUp、Smartsheet(ガント・レポート一体型)[5]
- **個人/フリーランス**: Trello、Jooto、Wrike(軽量・直感操作)[6]

#### 選び方のポイント

- **チーム規模**: 小規模→Trello/Asana、中大規模→Jira/Backlog
- **機能**: ガントチャートが必要ならRedmine系、タスク依存関係ならJira
- **コスト**: 無料プランで試用推奨(Jira/Asana/Backlogは10ユーザー無料)
- **導入メリット**: 進捗可視化で遅延20-30%減、連携で業務効率化[2][9]

詳細は各公式サイトやデモで確認を。用途に合わせて無料トライアルから始めると良いでしょう。

出典：
[1] https://service.msols.com/blog/project-management-tool
[2] https://it-trend.jp/project_management/article/33-0001
[3] https://lychee-redmine.jp/blogs/project/free-project-management-tools/
[4] https://www.itreview.jp/categories/project-management
[5] https://dstmp.shachihata.co.jp/column/0220241129/
[6] https://boxil.jp/mag/a7325/
[7] https://biz.moneyforward.com/work-efficiency/basic/14156/
[8] https://products.sint.co.jp/obpm/blog/how-to-choose-the-right-project-management-tool
[9] https://www.aspicjapan.org/asu/article/11490
```

**Mentioned products** (~15): Jira, Asana, Backlog, Trello, Redmine/Lychee Redmine, TimeCrowd, みんなでガント.com, Brabio!, Freedcamp, Quip, Monday.com, ClickUp, Smartsheet, Jooto, Wrike

**Explicit URL citations**: 9 sources, 100% Japanese domains
1. service.msols.com
2. it-trend.jp
3. lychee-redmine.jp
4. itreview.jp
5. dstmp.shachihata.co.jp
6. boxil.jp (path changed: /sc-project/ → /mag/a7325/)
7. biz.moneyforward.com
8. products.sint.co.jp (path changed)
9. aspicjapan.org

**Japan-origin tools**: 5+ (Backlog, TimeCrowd, みんなでガント.com, Brabio!, Jooto)

**Notes vs Day 1**:
- Product count: 9 → 15 (substantial increase)
- Japan-origin tools: 4 → 5+ (Brabio!, みんなでガント.com newly added)
- URL count: 10 → 9 (slight decrease)
- URL stability: 8 of 10 domains preserved (80%)
  Only freeconsultant.jp dropped; no new domains added
- Geographic concentration: 100% .jp domains (preserved)
- Source-type composition (preserved):
  * SaaS comparison media (it-trend, itreview, boxil, msols)
  * Vendor self-blogs (Lychee Redmine, Sint OBPM, Shachihata, MoneyForward)
  * Industry association (ASPIC)
- Structural change: Day 1 was text-paragraph format.
  Day 2 includes explicit comparison table.
- Monday.com NEWLY APPEARS (was absent in Day 1)
- ClickUp NEWLY APPEARS (was absent in Day 1)
- Wrike preserved

### q001 — Cross-model summary (Day 2)

| Model | Products | Japan-origin | URLs cited |
|---|:-:|:-:|:-:|
| GPT-5.4 | 7 | 1 | 0 |
| Claude | 7 | 2 | 0 |
| Gemini | 7 | 1 | 0 |
| Perplexity | 15 | 5+ | 9 |

**Day 1 → Day 2 canonical core stability**: Notion, Trello, Asana appear in all 3 self-contained models on both days (6/6 observations). **Monday.com appears in 2/3 self-contained models in Day 2** (dropped from Claude) — first instance of canonical-four product being lost.

**Japan-origin tools (3 self-contained models)**:
- Day 1: 2 (Gemini ✓, Claude ✓, GPT ×)
- Day 2: 4 (Gemini ✓, Claude ✓✓ Backlog+kintone, GPT ✓ Backlog)
- **100% increase in one week**

---

## q002 — What is the best CRM for small businesses?

**Category**: product_recommendation | **Language**: en
**First observed**: 2026-05-05 | **This observation**: 2026-05-12

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-12T__:__:__+09:00

```
### 1. HubSpot CRM: Best Overall for Growth

HubSpot is widely considered the top choice for small businesses due to its robust "forever free" plan and its ability to scale as a company grows.

* **Key Features:** Contact management, email tracking, live chat, and meeting scheduling.
* **Pros:** User-friendly interface, excellent mobile app, and seamless integration with marketing and service tools.
* **Cons:** Advanced features in paid tiers (Starter, Professional, Enterprise) can become very expensive quickly.
* **Pricing:** Free plan available; paid plans start at approximately $15/month per user.

### 2. Zoho CRM: Best Value and Customization

Zoho CRM offers a deep feature set at a lower price point than many competitors, making it ideal for budget-conscious businesses that need automation.

* **Key Features:** AI assistant (Zia), workflow automation, social media integration, and extensive reporting.
* **Pros:** Highly customizable, integrates with the vast Zoho ecosystem (Books, Projects, etc.), and offers a strong free tier for up to 3 users.
* **Cons:** The interface can feel cluttered and has a steeper learning curve than HubSpot.
* **Pricing:** Standard plan starts at $14/month per user (billed annually).

### 3. Pipedrive: Best for Ease of Use

Designed by salespeople for salespeople, Pipedrive focuses on visual sales pipelines and activity-based selling.

* **Key Features:** Visual deal stages, automated reminders, lead segmentation, and revenue forecasting.
* **Pros:** Extremely intuitive "drag-and-drop" interface; requires minimal training to get started.
* **Cons:** No free plan; limited marketing tools compared to "all-in-one" platforms.
* **Pricing:** Starts at $14/month per user (billed annually).

### 4. Monday Sales CRM: Best for Visual Project Management

If your team already uses Monday.com for project management, their CRM module is a natural extension that excels in tracking complex workflows.

* **Key Features:** Fully customizable boards, automated lead scoring, and integrated email sync.
* **Pros:** Modern, colorful interface that is highly flexible; great for team collaboration.
* **Cons:** Requires a minimum of 3 users for paid plans; can feel like a spreadsheet on steroids rather than a dedicated CRM.
* **Pricing:** Basic CRM starts at $12/month per user (billed annually, 3-seat minimum).

### 5. Salesforce Essentials: Best for Scalability

Salesforce is the industry leader, and its "Essentials" plan provides a streamlined version of its enterprise-grade tool specifically for small teams.

* **Key Features:** Opportunity tracking, Einstein AI basics, and integration with the AppExchange.
* **Pros:** Access to the world's most powerful CRM ecosystem; easy to upgrade to higher tiers as your business becomes a large enterprise.
* **Cons:** Can be overwhelming for beginners; limited customization in the Essentials tier.
* **Pricing:** $25/month per user (billed annually).

### Summary Comparison Table

| CRM | Best For | Free Tier | Starting Price (Annual) |
| :--- | :--- | :--- | :--- |
| **HubSpot** | Scaling & Free Tools | Yes | $15/user/mo |
| **Zoho** | Customization & Value | Yes (3 users) | $14/user/mo |
| **Pipedrive** | Simple Sales Pipeline | No | $14/user/mo |
| **Monday.com** | Visual Workflows | No | $12/user/mo |
| **Salesforce** | Long-term Power | No | $25/user/mo |

### How to Choose

1. **Define your budget:** If you need $0 upfront, **HubSpot** or **Zoho** are the clear winners.
2. **Assess technical skill:** If you want something that works out of the box with zero training, choose **Pipedrive**.
3. **Consider your ecosystem:** If you use Google Workspace or Microsoft 365, look for a CRM with native "one-click" integrations to those platforms.
4. **Identify your bottleneck:** If you struggle with lead follow-up, prioritize **Zoho** for automation. If you struggle with deal visibility, prioritize **Pipedrive**.
```

**Mentioned products**: HubSpot CRM, Zoho CRM, Pipedrive, Monday Sales CRM, Salesforce Essentials (5 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0

**Notes vs Day 1**:
- Product count: 5 → 5 (no change)
- All 5 products PRESERVED between Day 1 and Day 2
- Notable name drift: "Salesforce Starter" (Day 1) → "Salesforce Essentials" (Day 2)
  Both are real Salesforce SKUs but referring to a different product tier.
  This may indicate Gemini's product knowledge updated mid-week.
- "Best for ___" labels modified slightly across products
- Comparison table PRESERVED
- Pricing information PRESERVED
- NEW SECTION added: "How to Choose" decision-tree
- 4-canonical-products (HubSpot/Zoho/Pipedrive/Salesforce) FULLY PRESERVED

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-12T__:__:__+09:00

```
The best CRM for a small business depends on your budget, sales process, and how much automation you need. For most small businesses, these are the strongest options:

## Best overall

**HubSpot CRM**
- Very easy to start with
- Strong free plan
- Good contact management, email tracking, pipeline visibility
- Scales well with marketing and service tools
- Can get expensive as you add advanced features

## Best for sales-focused small teams

**Pipedrive**
- Excellent pipeline management
- Simple, visual, and easy to adopt
- Good automation for follow-ups
- Better for sales teams than for full marketing/service needs

## Best budget option

**Zoho CRM**
- Affordable
- Broad feature set
- Good if you want lots of functionality at a lower price
- Interface and setup can feel more complex

## Best if you already use Google/Outlook and want simplicity

**Freshsales**
- Clean interface
- Built-in calling and email features
- Good balance of usability and features
- Less ecosystem depth than HubSpot

## Best for very small teams / freelancers

**Monday Sales CRM** or **Bigin by Zoho**
- Simple setup
- Good for basic lead and deal tracking
- Less overwhelming than enterprise-style CRMs

## Quick recommendation by scenario

- **Just getting started:** HubSpot CRM
- **Need a simple sales pipeline:** Pipedrive
- **Need low cost + lots of features:** Zoho CRM
- **Need easy all-around usability:** Freshsales
- **Very small team:** Bigin by Zoho

## What to look for

Choose a CRM based on:

- Ease of use
- Contact and lead management
- Pipeline customization
- Email/calendar integration
- Automation
- Reporting
- Pricing as your team grows

## My practical pick

If you want the safest choice for a typical small business: **HubSpot CRM**.
If you want the best pure sales CRM with less clutter: **Pipedrive**.

## Best next step

Shortlist 2–3 CRMs and test them with:

- 10 sample contacts
- 1 real sales pipeline
- 1 email integration
- 1 automation workflow

If you want, I can give you:

1. a **side-by-side comparison table**, or
2. a **personalized recommendation** based on your business type, team size, and budget.
```

**Mentioned products**: HubSpot CRM, Pipedrive, Zoho CRM, Freshsales, Monday Sales CRM, Bigin by Zoho (6 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0

**Notes vs Day 1**:
- Product count: 6 → 6 (same count)
- BUT product composition changed substantially:
  * MAJOR: Salesforce DISAPPEARED (one of Day 1's "canonical four")
  * Streak DISAPPEARED
  * Monday Sales CRM NEWLY ADDED
  * Bigin by Zoho NEWLY ADDED (product brand fragmentation:
    Zoho is now mentioned in two products — Zoho CRM and Bigin by Zoho)
- HubSpot, Zoho CRM, Pipedrive, Freshsales: ALL PRESERVED
- Response structure preserved across q002 Day 1 → Day 2
- "Best next step" section added (with 4-item test protocol)
- Closing refinement offer (table / personalized recommendation) PRESERVED:
  * Day 1: side-by-side comparison table / best CRM by industry / recommendation based on team size and budget
  * Day 2: side-by-side comparison table / personalized recommendation based on business type, team size, and budget
- Model signature confirmation: 4 of 4 observations now show identical
  closing-pattern, comparison-suggestion-3-options structure.

**Critical observation**: GPT-5.4 dropped Salesforce — a major product in the LLM CRM canonical core. First observed instance where a top-tier "canonical" product disappears from a single model's response between weeks.

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-12T__:__:__+09:00

```
# Best CRM for Small Businesses

There's no single "best" CRM — it depends on your budget, team size, and what you sell. Here's a breakdown of top options by use case:

## Top Picks by Category

### 🏆 Best Overall: **HubSpot CRM**
- **Free tier** with unlimited users
- Easy to learn, clean interface
- Scales with paid Marketing/Sales Hubs
- **Best for:** Businesses wanting room to grow
- **Downside:** Paid tiers get expensive fast

### 💰 Best Value: **Zoho CRM**
- Starts at ~$14/user/month
- Huge feature set (workflows, AI, analytics)
- Integrates with Zoho's full business suite
- **Best for:** Budget-conscious teams wanting depth

### 🎯 Best for Sales-Focused Teams: **Pipedrive**
- Starts at ~$14/user/month
- Visual pipeline-first design
- Simple, intuitive for sales reps
- **Best for:** Small sales teams closing deals

### 🛠️ Best for Customization: **Salesforce Starter**
- Starts at ~$25/user/month
- Industry-standard, massive ecosystem
- **Best for:** Businesses planning rapid growth
- **Downside:** Steeper learning curve

### 🛒 Best for E-commerce: **Klaviyo** or **Brevo**
- Strong email/SMS automation
- Built for online stores (Shopify, WooCommerce)
- **Best for:** D2C and online retailers

### 📞 Best Simple/All-in-One: **Freshsales** or **monday CRM**
- Clean UIs, built-in phone/email
- Affordable entry tiers
- **Best for:** Non-technical small teams

## Quick Decision Guide

| Your Situation | Recommended CRM |
|---|---|
| Just starting, tight budget | HubSpot Free |
| Want most features per dollar | Zoho CRM |
| Sales pipeline is the priority | Pipedrive |
| Plan to scale aggressively | Salesforce |
| Run an online store | Klaviyo / Brevo |
| Want simple & visual | monday CRM |

## Key Questions Before Choosing

1. **How many users?** Some charge per seat — costs add up fast.
2. **What integrations do you need?** (Gmail, QuickBooks, Shopify, etc.)
3. **Do you need marketing automation** built-in, or just contact management?
4. **What's your team's tech comfort level?**
5. **Will you need mobile access** for field sales?

**My general recommendation:** Start with **HubSpot's free tier** to learn what you actually need, then upgrade or switch to **Zoho** or **Pipedrive** once your requirements are clear.

Want me to dive deeper into any of these, or compare two specific ones side-by-side?
```

**Mentioned products**: HubSpot CRM, Zoho CRM, Pipedrive, Salesforce Starter, Klaviyo, Brevo, Freshsales, monday CRM (8 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0

**Notes vs Day 1**:
- Product count: 8 → 8 (same)
- 6 of 8 products PRESERVED: HubSpot, Zoho, Pipedrive, Salesforce,
  Freshsales, Monday Sales CRM
- DROPPED: Keap, Insightly
- NEWLY ADDED: Klaviyo, Brevo (both e-commerce-focused)
- NEW CATEGORY: "Best for E-commerce" — did not exist in Day 1
- All 4 Claude signature elements PRESERVED:
  * Comparison table (Quick Decision Guide) ✓
  * Category-based organisation with priority labels ✓
  * Pricing on every product ✓
  * Closing offer ("dive deeper or compare two specific ones") ✓
- New style elements: emoji labels (🏆💰🎯🛠️🛒📞)
- Claude q002 broadened scope to include email/SMS automation tools

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-12T__:__:__+09:00

```
### Top CRM Recommendations for Small Businesses

Based on recent search results from 2026 sources, there's no single "best" CRM—choices depend on needs like budget, ease of use, integrations, and features (e.g., free tiers, sales pipelines, marketing automation). HubSpot CRM emerges as the most frequently recommended option across multiple sites for its free core version, user-friendliness, and scalability. Here's a breakdown of the top contenders:

#### 1. **HubSpot CRM** (Most Recommended Overall)
   - **Why it's top-rated**: Free entry-level version with contact management, deal tracking, email integration, and reporting. Advanced features available in paid tiers. Praised for ease of use and no-cost start for startups/small teams.
   - **Sources**: Faye Digital, Nimble, US Chamber of Commerce.
   - **Best for**: Budget-conscious businesses wanting quick setup and growth potential.
   - **Limitations**: Advanced marketing/sales automation requires upgrades (starts ~$20/user/month).

#### 2. **Zoho CRM**
   - **Why it's strong**: Easy to use/customize, quick onboarding, strong integrations (e.g., Google Workspace), secure, and affordable for small teams.
   - **Source**: Zoho.
   - **Best for**: Businesses needing customization without complexity. Free for up to 3 users.
   - **Pricing**: Starts at $14/user/month (billed annually).

#### 3. **Pipedrive**
   - **Why it's popular**: Visual sales pipelines, simple interface, focused on deal management. Great for sales-driven small businesses.
   - **Sources**: Faye Digital, US Chamber.
   - **Best for**: Sales teams prioritizing pipeline tracking.
   - **Pricing**: Starts at $14/user/month; 14-day free trial.

#### 4. **Salesforce (Essentials/Starter Suite)**
   - **Why it fits**: Scalable for growth, addresses sales pain points, improves customer experience. Supports up to 10,000 contacts in growth plans.
   - **Source**: Salesforce.
   - **Best for**: Ambitious small businesses planning to scale.
   - **Pricing**: Starts at $25/user/month.

#### 5. **Other Notables**
   - **Mailchimp**: Strong for marketing-focused CRM with audience management and automation.
   - **Nimble**: Affordable for small teams wanting high value.
   - **Monday CRM / Less Annoying CRM**: User-friendly, low-cost/free options for pipelines/simple needs.
   - **HighLevel**: Mentioned in YouTube overviews for agencies/small ops, with AI features and trials.

| CRM          | Free Tier? | Key Strength              | Starting Paid Price (per user/mo) | Ideal User                  |
|--------------|------------|---------------------------|-----------------------------------|-----------------------------|
| **HubSpot** | Yes       | Free all-in-one starter  | $20                              | Startups/budget-focused    |
| **Zoho**    | Limited   | Customizable/integrations| $14                              | Custom needs               |
| **Pipedrive**| No       | Sales pipelines          | $14                              | Sales teams                |
| **Salesforce**| No      | Scalability              | $25                              | Growing businesses         |
| **Mailchimp**| Yes      | Marketing automation     | $13                              | Email/marketing heavy      |

#### How to Choose

- **Free priority?** Start with HubSpot or Monday CRM.
- **Sales focus?** Pipedrive or Nimble.
- **Test them**: Most offer free trials (e.g., 14-30 days). Evaluate based on your team size, integrations (e.g., email, Google), and mobile app needs.
- **Trends in 2026**: Emphasis on AI features, free tiers, and ease for non-tech users.

For personalized advice, share details like your industry, team size, or key features needed (e.g., invoicing, automation).

出典：
[1] https://www.zoho.com/crm/small-business-crm-software/
[2] https://fayedigital.com/blog/best-crm-for-small-business/
[3] https://www.nimble.com/blog/best-crm-for-small-business-in-2025/
[4] https://www.salesforce.com/crm/crm-for-small-business/
[5] https://mailchimp.com/resources/best-crm-for-small-business/
[6] https://www.youtube.com/watch?v=RIRyuq-AKOU
[7] https://www.uschamber.com/co/start/strategy/low-cost-crm-tools
```

**Mentioned products**: HubSpot, Zoho, Pipedrive, Salesforce, Mailchimp, Nimble, Monday CRM, Less Annoying CRM, HighLevel (9 products)
**Explicit URL citations**: 7 sources, 100% US domains
1. zoho.com (vendor self) — preserved from Day 1
2. fayedigital.com — preserved
3. nimble.com (vendor self) — NEW
4. salesforce.com (vendor self) — preserved
5. mailchimp.com (vendor self) — preserved
6. youtube.com — preserved
7. uschamber.com — preserved

**Geographic distribution**: 100% US domains (consistent with Day 1)

**Source-type breakdown**:
- Vendor self-blogs: 4 (Zoho, Salesforce, Mailchimp, Nimble)
- IT/marketing media: 1 (fayedigital)
- Industry/government: 1 (US Chamber)
- Video: 1 (YouTube)
- Academic: 0

**Notes vs Day 1**:
- Product count: 7 → 9 (+2)
- URL count: 7 → 7 (same)
- URL preservation: 6/7 = 86% (sybill.ai dropped, nimble.com added)
- Geographic concentration: 100% US (preserved)
- 6 of 7 products from Day 1 preserved
- Capsule (Day 1 unique British CRM) DROPPED
- NEW: Nimble, Less Annoying CRM, HighLevel
- Source structure (vendor + media + association) PRESERVED
- Comparison table format PRESERVED

### q002 — Cross-model summary (Day 2)

| Model | Products | Japan-origin | URLs cited |
|---|:-:|:-:|:-:|
| Gemini | 5 | 0 | 0 |
| GPT-5.4 | 6 | 0 | 0 |
| Claude | 8 | 0 | 0 |
| Perplexity | 9 | 0 | 7 |

**Day 1 → Day 2 canonical core stability**: HubSpot, Zoho, Pipedrive appear in ALL 4 models on BOTH days (8/8 observations).

**Salesforce trajectory**:
- Day 1: 4/4 models (canonical four)
- Day 2: 3/4 models (dropped from GPT-5.4 only)

**Monday CRM trajectory**:
- Day 1: 3/4 models
- Day 2: 4/4 models (newly added by GPT-5.4)

**Inverse symmetry**: Salesforce downgrade + Monday CRM upgrade in same week — suggests dynamic canonical reshuffling rather than random variation.

---

## q003 — 睡眠の質を上げる方法を教えて

**Category**: health | **Language**: ja
**First observed**: 2026-05-05 | **This observation**: 2026-05-12

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-12T__:__:__+09:00

```
### 1. 生活リズムの最適化

* **起床時間を一定にする**: 休日であっても平日と同じ時間に起きることで、体内時計(サーカディアンリズム)を安定させます。
* **朝日を浴びる**: 起床後すぐに太陽の光を浴びることで、セロトニンの分泌が促され、約14〜16時間後のメラトニン(睡眠ホルモン)の分泌準備が整います。
* **昼寝は短時間にする**: 昼寝をする場合は、午後3時までに20分程度にとどめます。長すぎる昼寝は夜間の睡眠圧を低下させます。

### 2. 就寝前の習慣(ルーティン)

* **ブルーライトの遮断**: 就寝の1〜2時間前からはスマートフォンやパソコンの使用を控えます。ブルーライトは脳を覚醒させ、メラトニンの生成を抑制します。
* **入浴のタイミング**: 就寝の約90分前に入浴を済ませます。40度程度のぬるま湯に浸かり、一度上げた深部体温が下がる過程で自然な眠気が誘発されます。
* **リラクゼーション**: 軽いストレッチ、読書、アロマ、瞑想など、副交感神経を有位にする活動を取り入れます。

### 3. 飲食のコントロール

* **カフェインの制限**: カフェインの覚醒効果は数時間持続するため、午後の早い時間以降は摂取を控えます。
* **アルコールを避ける**: アルコールは入眠を助けるように感じられますが、睡眠の質を著しく低下させ、中途覚醒の原因になります。
* **夕食の時間**: 消化活動が睡眠を妨げないよう、就寝の2〜3時間前までには食事を終えるのが理想です。

### 4. 寝室環境の整備

* **適切な温度・湿度**: 夏場は25〜28度、冬場は15〜18度、湿度は50〜60%が理想的とされています。
* **遮光と静音**: カーテンで外光を遮り、必要に応じて耳栓やアイマスクを使用して、外部からの刺激を最小限にします。
* **寝具の適合性**: 自分の体型に合った枕の高さや、寝返りが打ちやすいマットレスを選択します。

### 5. 心理的なアプローチ

* **悩みを書き出す**: 不安や翌日のタスクが気になって眠れない場合は、紙に書き出す(ジャーナリング)ことで脳の負担を減らします。
* **「眠らなければならない」と考えすぎない**: 眠れない時に無理にベッドに留まると、「ベッド＝眠れない場所」と脳が学習してしまいます。20分以上眠れない場合は一度ベッドを離れ、眠くなってから戻るようにします。
```

**Response structure**: 5 categories × 13 specific recommendations (Day 1 also had 13)
**Explicit URL citations**: None
**Mentioned products**: None

**Numeric specificity**: 9 quantitative claims (Day 1 was 12, -25%)

**Notes vs Day 1**:
- Item count: 13 → 13 (same total)
- 11 of 12 canonical sleep habits PRESERVED
- Lost: "適度な運動" (moderate exercise)
- Added: "心理的アプローチ" category (jornaling, get-out-of-bed if can't sleep)
- Numeric specificity DECREASED (12 → 9)
- Room temperature ranges SHIFTED:
  Summer: 25–26°C → 25–28°C (upper range widened)
  Winter: 18–23°C → 15–18°C (range shifted down)
- LaTeX-style notation FULLY REMOVED (Day 1 used "( 90 )", "( 14 \sim 16 )";
  Day 2 uses plain text)
- CBT-I elements newly added (sleep-bed association, journaling)

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-12T__:__:__+09:00

```
## 睡眠の質を上げる基本

- **毎日同じ時間に寝て、同じ時間に起きる**
  - 休日の寝だめもずれを大きくしやすいです。
- **朝に日光を浴びる**
  - 起床後1時間以内に外の光を浴びると、体内時計が整いやすくなります。
- **寝る前に強い光を避ける**
  - スマホ、PC、明るい照明は寝つきを悪くしやすいです。
  - 寝る1時間前から画面を見る時間を減らすのがおすすめです。
- **カフェインをとる時間に注意する**
  - コーヒー、エナジードリンク、濃いお茶は午後遅く以降を避けるとよいです。
- **夜の飲酒を控える**
  - 寝つきが良くなる感じがしても、眠りが浅くなりやすいです。
- **寝室環境を整える**
  - 静か、暗い、少し涼しめの環境が向いています。
  - 枕やマットレスが体に合っているかも大切です。
- **入浴を活用する**
  - 就寝の1〜2時間前にぬるめのお風呂に入ると、眠りやすくなることがあります。
- **軽い運動を習慣にする**
  - 日中のウォーキングやストレッチは効果的です。
  - ただし寝る直前の激しい運動は逆効果になりやすいです。
- **寝る前の食事を重くしない**
  - 就寝直前の満腹状態は睡眠の妨げになります。
  - 空腹すぎる場合は、消化の良い軽食を少量にします。
- **「眠れない」と焦らない**
  - 20〜30分ほど眠れないなら、いったん布団を出て、暗めの場所で静かに過ごしてから戻るほうがよいことがあります。

## すぐ試しやすい習慣

1. 起きたらカーテンを開ける
2. 朝に少し歩く
3. カフェインは昼すぎまで
4. 寝る1時間前はスマホを減らす
5. 毎日ほぼ同じ時刻に起きる

## 注意したいサイン

次のような場合は、生活習慣だけでなく医療相談も検討してください。

- いびきが大きい、呼吸が止まると言われる
- 日中の眠気が強い
- 寝ても疲れが取れない
- 2週間以上、寝つきや中途覚醒の悩みが続く
- 気分の落ち込みや不安が強い

必要なら、

- **今日からできる改善プラン**
- **寝る前1時間の理想ルーティン**
- **原因チェックリスト**

のどれかの形で整理できます。
```

**Response structure**:
- 10 numbered recommendations (flat list, no categorisation)
- "すぐ試しやすい習慣" (5-item quick-start)
- "注意したいサイン" (medical disclaimer — renamed from Day 1's "受診を考えたほうがいいサイン")
- Closing 3-way refinement offer (format-based)

**Explicit URL citations**: None
**Mentioned products**: None

**Numeric specificity**: ~3 quantitative claims (DECREASED from Day 1's 5-6, -50%)

**Notes vs Day 1**:
- Item count: 10 → 10 (same)
- Flat-list structure PRESERVED (vs Gemini's full categorisation)
- Numeric specificity DECREASED substantially
- Overall response is more abstract/concise than Day 1
- GPT-5.4 signature 3-option closing PRESERVED for 5th consecutive observation
  - Day 1 q003: 症状別 3択 (寝つき/夜中覚醒/朝すっきりしない)
  - Day 2 q003: 形式別 3択 (今日からのプラン/理想ルーティン/原因チェックリスト)
  - Structure (3-option closing) is invariant — content of options has changed
- Medical disclaimer renamed: "受診を考えたほうがいいサイン" → "注意したいサイン"
- 11 of 13 canonical sleep habits preserved (lost "昼寝の管理")
- Removed: "一言でいうと" section
- Removed: explicit "今日からの最小行動" 3-step section (merged into "すぐ試しやすい")

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-12T__:__:__+09:00

```
# 睡眠の質を上げる方法

## 1. 生活リズムを整える

- **起床時間を固定する**：休日も平日と同じ時刻に起きることで体内時計が安定する
- **朝日を浴びる**：起床後30分以内に15分程度の日光浴をするとメラトニン分泌のリズムが整う
- **昼寝は20分以内**：長時間の昼寝は夜の睡眠を妨げる

## 2. 食事と飲み物に気をつける

| 項目 | 推奨 |
|------|------|
| カフェイン | 就寝の **6〜8時間前まで** に控える |
| アルコール | 寝つきは良くなるが睡眠の質は低下するため避ける |
| 夕食 | 就寝の **3時間前まで** に済ませる |
| 水分 | 寝る直前の大量摂取は中途覚醒の原因になる |

## 3. 寝室環境を最適化する

- **室温**：夏は26℃前後、冬は18〜20℃が目安
- **湿度**：50〜60%を維持
- **光**：できるだけ暗く、遮光カーテンを活用
- **音**：静かな環境、または一定のホワイトノイズ
- **寝具**：体に合った枕とマットレスを選ぶ

## 4. 就寝前のルーティン

- 就寝の **90分前に入浴**(40℃のお湯に15分程度)すると、深部体温の低下とともに眠気が誘発される
- スマホ・PCのブルーライトは寝る **1時間前** にカット
- ストレッチや深呼吸でリラックスモードに切り替える
- 読書やヒーリング音楽など、心拍を落ち着かせる活動を選ぶ

## 5. 日中の習慣

- **適度な運動**：ウォーキングなど有酸素運動を週3〜5回、就寝3時間前までに
- **ストレスケア**：瞑想やマインドフルネスで自律神経を整える

## 6. 改善しない場合

2週間以上、以下の症状が続く場合は睡眠外来や心療内科への相談を検討してください。

- 寝つきに30分以上かかる
- 夜中に何度も目が覚める
- 早朝に目覚めて再入眠できない
- 日中に強い眠気がある

---

まずは「**起床時間の固定**」と「**朝日を浴びる**」の2つから始めると、1〜2週間で変化を実感しやすいです。どこから取り組みたいか教えていただければ、もう少し具体的にお伝えできます。
```

**Response structure**: 6 categories (Day 1 had 8)
**Explicit URL citations**: None
**Mentioned products**: None

**Numeric specificity**: ~8 quantitative claims (Day 1 was ~10, -20%)

**Medical disclaimer**: EXPANDED with 4 specific symptom criteria

**Claude signature elements** vs Day 1:
- Comparison table ✓ (food/drink section, now includes water — expanded)
- Category-based organisation ✓
- Numeric details ✓ (slightly reduced)
- Closing refinement offer ✓ ("どこから取り組みたいか教えていただければ" added)

**Notable changes**:
- LOST: "最重要" priority label (Day 1 highlighted light control)
- LOST: "効果が出やすい順にまとめました" framing
- CHANGED: Minimum-action set 3→2 (down from "morning light + wake time + bath 90min" to "wake time + morning light")
- ADDED: explicit symptom-based criteria for medical referral

**Notes vs Day 1**:
- Item count: 8 categories → 6 categories (consolidation)
- 11 of 13 canonical sleep habits preserved
- Numeric specificity decreased -20% (smallest decrease among 3 self-contained models)
- Priority labelling weakened — first instance where this signature element softens

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-12T__:__:__+09:00

```
### 睡眠の質を上げる主な方法

検索結果に基づき、信頼できる健康情報源(医療機関、製薬会社、専門サイト)から抽出された実践的な方法をまとめました。これらは生活習慣の見直しを中心に、即座に取り入れやすいものを優先。効果は個人差がありますが、継続が鍵です。主なポイントをカテゴリ別に分類します。

#### 1. **朝の習慣：体内時計をリセット**

   - **朝日・日光を浴びる**
     起床後すぐにカーテンを開け、日光を浴びる。セロトニンやメラトニンの分泌を促し、睡眠・覚醒リズムを整える([3][4][5])。
   - **しっかり朝食を摂る**
     栄養バランスの良い朝食で睡眠休養感を向上。空腹を避け、体内時計を活性化([1][2])。

#### 2. **運動習慣：適度な活動を**

   | 強度 | 例 | 効果・タイミング |
   |------|----|--------------------|
   | 低強度 | ストレッチ、ヨガ、家事、散歩 | リラックス効果。就寝3時間前までOK。 |
   | 中強度 | 速歩き、軽い筋トレ、水中歩行、ピラティス | 睡眠効率向上。夕方推奨。 |
   | 高強度 | ジョギング、水泳、登山 | 深い睡眠促進。ただし就寝2-3時間前までに。 |

   毎日10分以上の積み重ねを。激しい運動は逆効果になる場合あり([1][2][3][4][5])。

#### 3. **夕方〜就寝前のリラックス**

   - **就寝1時間前に入浴(ぬるめのお湯、38℃前後、5-30分)**
     体深部温度を上げ、副交感神経を優位に。寝つき改善([3][6][7])。
   - **リラックス時間を確保**
     ヨガ、深呼吸、音楽、アロマ。スマホ・仕事から離れる([1][6])。
   - **温かい飲み物**
     白湯や生姜湯で体を温め、眠気を誘う([6])。

#### 4. **食事・嗜好品の見直し**

   - **夕食は就寝3時間前までに**
     脂質控えめ、バランス良く。胃腸を休ませる([6][7][9])。
   - **カフェイン・アルコールの制限**
     午後以降避け、量・タイミングを調整([1][2])。

#### 5. **寝室環境の整備**

   - **温度・湿度調整**：快適(暑すぎず寒すぎず)。
   - **暗く静かに**：照明を落とし、遮光・防音を。
   - **清潔・快適に**：寝具を整え、ストレスフリー([1][2][6][7])。

#### 追加Tips

- **生活リズムの固定**：毎日同じ起床・就寝時間。
- **光のコントロール**：就寝前はブルーライト(スマホ・PC)を1時間前からオフ([4][7])。
- 効果が出ない場合：睡眠障害の可能性あり、専門医相談を([8])。

これらを1週間試すだけで変化を感じる人が多いです。参考元は主に日本国内の信頼サイトで、医師監修含む。継続と個別調整が重要。

出典：
[1] https://www.mtgec.jp/wellness/sixpad/column/improve-sleep-quality/
[2] https://wellness.shionogi.co.jp/insomnia/trial/trial.html
[3] https://www.fujiyaku-direct.com/health_information/article/088main
[4] https://www.iyobank.co.jp/sp/iyomemo/entry/20230627.html
[5] https://www.daiwahouse.co.jp/tryie/column/life/better_sleep_tips/index.html
[6] https://www.glico.com/jp/powerpro/citric-acid/entry91/
[7] https://banno-clinic.biz/sleep-quality/
[8] https://kennet.mhlw.go.jp/slp/event/sleep_quality/index.html
[9] https://brand.taisho.co.jp/contents/tsukare/457/
[10] https://www.youtube.com/watch?v=1D7Yfq6kHtQ
```

**Response structure**: 5 categories + Additional Tips + medical referral
**Explicit URL citations**: 10 sources, 100% Japanese domains

URL list (Day 2):
1. mtgec.jp (MTG / SIXPAD) — preserved from Day 1
2. wellness.shionogi.co.jp (Shionogi pharma) — preserved
3. fujiyaku-direct.com (Fuji Pharma) — preserved
4. iyobank.co.jp (Iyo Bank — regional bank OM) — preserved
5. daiwahouse.co.jp (Daiwa House — housing co. OM) — preserved
6. glico.com (Glico — food co. OM) — preserved
7. banno-clinic.biz (medical clinic) — preserved
8. kennet.mhlw.go.jp (Ministry of Health) — preserved
9. brand.taisho.co.jp (Taisho Pharma) — preserved
10. youtube.com — preserved

**URL preservation rate: 10/10 = 100%**

**Source-type breakdown** (identical to Day 1):
- Public/government: 1 (10%)
- Medical institution: 1 (10%)
- Pharma owned media: 3 (30%)
- Health-product company OM: 2 (20%)
- Cross-industry owned media: 2 (20%)
- Video: 1 (10%)
- Academic/peer-reviewed: 0 (0%)
- Medical specialist media: 0 (0%)

**Notes vs Day 1**:
- URL list: 100% preserved (10/10)
- Source-type composition: identical
- Geographic concentration: 100% .jp domains (preserved)
- Response structure: expanded from 3 categories to 5 + additional tips
- New comparison table: exercise intensity levels (low/medium/high)
- Content slightly more detailed than Day 1
- Mentions of cross-industry OM (Iyo Bank, Daiwa House) PRESERVED
  with same conceptual framing

**Critical observation**:
Perplexity does NOT show the parallel "abstraction shift" observed in
the 3 self-contained LLMs (Gemini, GPT-5.4, Claude). In fact, Perplexity
becomes MORE detailed in Day 2 (added intensity comparison table).
This bifurcates interpretation of the abstraction shift: it occurs
at the model-level (training data / safety policy / system prompt
updates), not at the retrieval-data level.

### q003 — Cross-model summary (Day 2)

| Model | Recommendations | Japan-cultural elements | URLs cited |
|---|:-:|:-:|:-:|
| Gemini | 13 | 0 | 0 |
| GPT-5.4 | 10 | 0 | 0 |
| Claude | 6 categories | 0 | 0 |
| Perplexity | 8 + tips | 0 | 10 |

**Canonical sleep habits — 4-model agreement Day 1 → Day 2**:
9 of 10 habits preserved across all models. The set:
1. Wake-time consistency ✓
2. Morning sunlight exposure ✓
3. Pre-sleep screen/light reduction ✓
4. Caffeine restriction ✓
5. Alcohol caution ✓
6. Bath timing ✓
7. Bedroom temperature/humidity ✓
8. Pre-sleep dinner timing ✓
9. Moderate exercise (some models lost this)
10. Pre-sleep relaxation ✓

---

## Day 2 — Synthesis

### Longitudinal findings (Day 1 → Day 2)

**Core canonical products PRESERVED across all 4 models × 2 weeks (8 observations each)**:
- Project management (q001): Notion, Trello, Asana
- CRM (q002): HubSpot, Zoho, Pipedrive

**This is MIBO's first established empirical law: the canonical-three pattern in product recommendation.**

**Canonical sleep habits PRESERVED**:
- 9 of 10 habits across all 4 models × 2 weeks (32 observations)

**Per-model response signatures PRESERVED across domains and weeks**:
- Claude (4-element pattern): 8/8 observations
- GPT-5.4 (closing 3-option refinement): 5/5 observations where applicable
- Gemini (comparison tables, numeric precision): persistent
- Perplexity (URL citations, geographic language-matching): 4/4 observations

**Perplexity citation source stability**:
- q001: 8/10 URLs preserved (80%)
- q002: 6/7 URLs preserved (86%)
- q003: 10/10 URLs preserved (100%)
- Average: 92% URL preservation across 1 week

### Drift findings

**Salesforce trajectory** (CRM canonical core element):
- Day 1: 4/4 models cited
- Day 2: 3/4 models cited (dropped from GPT-5.4 only)
- First observation of a canonical-core product disappearing from one model

**Monday CRM trajectory** (CRM):
- Day 1: 3/4 models cited
- Day 2: 4/4 models cited (added by GPT-5.4)
- First observation of a non-canonical product joining the canonical set

**Inverse symmetry**: Salesforce loss + Monday CRM gain suggests dynamic
canonical reshuffling rather than random fluctuation.

**Japan-origin tool representation** (q001, ja-language):
- Day 1: 2 total mentions across 3 self-contained models (Backlog only)
- Day 2: 4 total mentions (Backlog + kintone in Claude, Backlog newly in GPT)
- 100% increase in one week

**Numeric specificity in health domain (q003)**:
- Gemini: 12 → 9 (-25%)
- GPT-5.4: 5-6 → 3 (-50%)
- Claude: 10 → 8 (-20%)
- Perplexity: comparable to expanded (counter-trend)
- All 3 self-contained models show parallel abstraction shift; Perplexity does not

**Format changes**:
- Gemini's LaTeX-style numeric notation fully removed in Day 2
- Claude's priority labels ("最重要") removed in q003 specifically

### Updated propositions

**P1 — Architectural divide (CONFIRMED, strengthened)**
Self-contained LLMs and retrieval-augmented LLMs continue to show
fundamentally different citation behaviour. The abstraction shift observed
in self-contained models was NOT mirrored in Perplexity.

**P2 — Canonical core scales with knowledge codification (CONFIRMED & REFINED)**
- Commercial product queries: 3 canonical products (refined from "4" in Day 1)
- Health/procedural queries: 9-10 canonical habits
- The "fourth" canonical product is volatile (Salesforce/Monday CRM exchange,
  Monday.com lost from Claude q001)

**P3 — Language as geographic filter (CONFIRMED)**
English commercial queries continue to surface zero Japan-origin products.
Japan-origin tools in Japanese commercial queries doubled (2 → 4 mentions).

**P4 — Source-type structure stability (STRONGLY CONFIRMED)**
Perplexity URL preservation 80-100% across queries. Source-type composition
identical to Day 1 across all three queries.

**P5 — Per-model response signatures (CONFIRMED across all 8 observations)**
All four models exhibit stable response-style signatures spanning two weeks
and multiple domains.

**P9 — Cross-industry owned-media SEO penetration (STRONGLY CONFIRMED)**
Iyo Bank and Daiwa House still appear in Perplexity health query.
100% URL preservation for q003 means this is not a random artifact.

**P10 — Japan market representation increase (NEW)**
1-week increase from 2 to 4 Japan-origin tool mentions in q001 across
3 self-contained models. Independent same-direction changes across multiple
models suggest non-random shift.

**P11 — Perplexity citation source stability (NEW)**
92% URL preservation rate across 3 queries × 1 week. Citation behaviour
inherits search engine top-result stability.

**P12 — Parallel abstraction shift in self-contained LLMs (NEW)**
Three independent self-contained LLMs show simultaneous reduction in
numeric specificity in health-domain responses (-20% to -50%).
Perplexity does not show this shift. This suggests model-level rather
than retrieval-data-level changes (training data updates, safety policy
changes, system prompt modifications).

**P13 — Dynamic canonical reshuffling (NEW)**
The "canonical 4" structure shows weekly dynamics: products move in and
out symmetrically (Salesforce out, Monday CRM in for q002).
True invariance exists only at the "canonical 3" level.

### Implications

**For research**: MIBO has now demonstrated that longitudinal observation
reveals dynamics invisible to single-point observation. The "canonical 3
+ volatile 4th + fluid derivatives" structure is undetectable from one
day's data alone.

**For policy**: The parallel abstraction shift across independent
self-contained LLMs is potentially significant for AI governance
discussions. Behaviour that appears independent may be coordinated at
the industry level (shared safety policies, similar training-data
updates).

**For GEO/LLMO strategy**: Targeting the "canonical 3" is the highest-
stability play. Targeting the volatile 4th position offers higher upside
but lower predictability. Cross-industry owned-media remains a viable
LLM-citation pathway in Japan.

### What comes next

- q004 (RAG, en) and q005 (Japanese AI researchers, ja) to be observed
  in subsequent sessions
- Next scheduled observation: 2026-05-19 (third data point — turns the
  "line" into a "trajectory")
- Continue weekly cadence
- Consider adding Japanese-domestic LLMs (PLaMo, tsuzumi) to v0.3 set

---

**End of Day 2 observation**

Observer: Kento Sasano
MIBO — Machine Information Behaviour Observatory
Observation continues weekly. Next: 2026-05-19
Repository: https://github.com/mibo-research-pilot
