# Third Observation — 2026-05-19

**Observatory**: MIBO (Machine Information Behavior Observatory)
**Observer**: Kento Sasano
**Date**: 2026-05-19
**Method**: Manual web interface (copy-paste from chat UI), conducted under OPEN principles
**Query set**: v0.1 (queries q001–q005, complete)
**Models observed**:
- OpenAI ChatGPT (GPT-5.4)
- Anthropic Claude (claude-opus-4-7)
- Google Gemini (Gemini 3.0 Flash)
- Perplexity (Web search mode)

**Total observations this session**: 20 (4 models × 5 queries)

**Significance**: Third longitudinal data point for q001-q003 (turning the line into a trajectory) and first baseline observation for q004-q005.

---

## Methodology

This is the third observation of MIBO, conducted exactly two weeks after Day 1 (2026-05-05) and one week after Day 2 (2026-05-12). The observation procedure follows OPEN principles:

- **O**bservation, not controlled experimentation: deployed systems accessed through their public web interfaces, without modification
- **P**arallelism across providers: all four models observed within a synchronized observation window (~2 hours on the same evening)
- **E**mbedded openness: this record is published in full at https://github.com/mibo-research-pilot/reports
- **N**on-stationarity awareness: queries q001-q003 repeated for the third week to record temporal change

Identical query wording to Day 1 and Day 2 is preserved for longitudinal comparability.

---

## q001 — おすすめのプロジェクト管理ツールは？

**Category**: product_recommendation | **Language**: ja
**First observed**: 2026-05-05 | **Second**: 2026-05-12 | **Third**: 2026-05-19

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-19T20:__:__+09:00

```
### 汎用・オールインワン型
*   `Notion`
    *   **特徴**: メモ、ドキュメント管理、データベース、タスク管理を一つのワークスペースに統合できる。自由度が非常に高く、独自のダッシュボードを作成可能。
    *   **適した用途**: ドキュメント共有とプロジェクト管理をシームレスに行いたいチーム。
*   `monday.com`
    *   **特徴**: 視覚的なカスタマイズ性が高く、ノーコードでワークフローの自動化を設定できる。色の活用やインターフェースが直感的。
    *   **適した用途**: 独自の業務プロセスを視覚的に管理したい幅広い業種。

### タスク・進捗管理特化型
*   `Asana`
    *   **特徴**: リスト、ボード、タイムライン（ガントチャート）など、複数の視点でタスクを管理できる。依存関係の把握やリソース管理機能が強力。
    *   **適した用途**: チーム全体のタスク量や進捗を詳細に可視化したい場合。
*   `Trello`
    *   **特徴**: 付箋を貼るような感覚で使える「カンバン方式」の代表的なツール。操作が非常にシンプルで学習コストが低い。
    *   **適した用途**: 小規模なチームや、視覚的に分かりやすい進捗管理を求めるプロジェクト。

### ソフトウェア開発・エンジニア向け
*   `Jira Software`
    *   **特徴**: アジャイル開発（スクラム、カンバン）に特化。バグトラッキング、リリース管理、高度なレポート機能が充実。
    *   **適した用途**: エンジニア中心のチームや、複雑なソフトウェア開発プロジェクト。
*   `Backlog`
    *   **特徴**: 日本発のツールで、UIが親しみやすく日本語サポートが充実。GitやSubversionなどのバージョン管理連携、ガントチャートが標準搭載。
    *   **適した用途**: 日本国内の企業、非エンジニアと共同作業を行う開発チーム。

### コミュニケーション重視型
*   `Wrike`
    *   **特徴**: プロジェクト管理機能に加え、校正機能や承認フローの管理が充実している。エンタープライズ向けのセキュリティ機能も強み。
    *   **適した用途**: マーケティング部門やクリエイティブ制作など、多段階の承認が必要な業務。

### 選択のポイント
| 項目 | 重視すべき点 |
| :--- | :--- |
| **チーム規模** | 数人なら `Trello`、大規模なら `Jira` や `Asana` |
| **管理手法** | アジャイルなら `Jira`、ウォーターフォールなら `Backlog` や `Wrike` |
| **ITリテラシー** | 誰でも使いやすいのは `Trello` や `Backlog` |
| **多機能性** | ドキュメントもまとめるなら `Notion` |
```

**Mentioned products**: Notion, monday.com, Asana, Trello, Jira Software, Backlog, Wrike (7 products)
**Explicit URL citations**: None
**Japan-origin tools**: 1 (Backlog)

**Notes vs Day 1 & Day 2**:
- Product count: 6 → 7 → 7 (stable at 7)
- Category count: 6 → 5 → 4 (monotonic compression)
- Comparison table: present → absent → present (oscillating, Day 2 anomaly signature)
- Core five (Notion/Trello/Asana/Monday/Backlog): 3/3 weeks fully preserved
- Wrike: returned after one-week absence (Day 1 ✓, Day 2 ✗, Day 3 ✓)
- ClickUp: appeared in Day 2 only, absent in Day 3
- Jira Software: appeared in Day 2 onwards (preserved in Day 3)
- NEW formatting feature: product names rendered in code font (`Notion`, `Trello`, etc.)
- Japan-origin tools: 1 (Backlog), preserved across all 3 weeks

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-19T20:__:__+09:00

```
用途次第ですが、定番は次の5つです。

## 総合おすすめ
1. **Asana**
   - バランスが良く、チーム向け
   - タスク管理、進捗確認、依存関係の管理がしやすい
   - 非エンジニアにも比較的使いやすい
2. **Trello**
   - 直感的で導入が簡単
   - カンバン方式で小規模チームに向く
   - シンプルさ重視なら強い
3. **Jira**
   - 開発チーム向けの定番
   - スクラム、バグ管理、チケット運用に強い
   - 高機能だが慣れは必要
4. **Notion**
   - ドキュメントとタスク管理を一体化しやすい
   - 情報整理、議事録、ナレッジ管理もしたい場合に便利
   - 自由度が高い反面、設計は必要
5. **ClickUp**
   - 多機能でコスパが良い
   - タスク、ドキュメント、ダッシュボードなどを一元管理しやすい
   - 機能が多いので最初は少し複雑

## 目的別おすすめ
- **とにかく簡単に始めたい**: `Trello`
- **チーム全体で使いやすさ重視**: `Asana`
- **ソフトウェア開発向け**: `Jira`
- **タスク管理＋社内Wikiもまとめたい**: `Notion`
- **高機能で幅広く管理したい**: `ClickUp`

## 迷ったらこの選び方
- **1〜5人の小規模チーム**: `Trello` または `Notion`
- **5〜50人の業務チーム**: `Asana` または `ClickUp`
- **開発組織**: `Jira`
- **ドキュメント中心の組織**: `Notion`

## 一言で選ぶなら
- 一般業務なら **Asana**
- 開発なら **Jira**
- 手軽さなら **Trello**

## 個人的な無難な結論
- **最初の1本**なら `Asana`
- **IT開発チーム**なら `Jira`
- **個人や小規模運用**なら `Trello`

必要なら次に
- **無料プラン比較**
- **日本語の使いやすさ比較**
- **中小企業向けランキング**
- **個人利用向けランキング**

のどれかで絞ってまとめられます。
```

**Mentioned products**: Asana, Trello, Jira, Notion, ClickUp (5 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0 (Backlog appeared in Day 2 only, now absent)

**Notes vs Day 1 & Day 2**:
- Product count: 6 → 7 → 5 (compressed)
- Monday.com: present (Day 1) → present (Day 2) → ABSENT (Day 3)
- Backlog: absent (Day 1) → present (Day 2) → ABSENT (Day 3) - one-week appearance
- Canonical three (Notion/Trello/Asana): 3/3 weeks fully preserved
- Closing refinement-offer pattern PRESERVED for 6th consecutive observation
  - Day 1: 3-option (segment-based: individual/dev/internal)
  - Day 2: 3-option (segment-based: individual/team/dev)
  - Day 3: 4-option (analysis-axis based: free plan / Japanese UX / SMB / personal)
- NEW STRUCTURE: 6-stage drill-down cascade (5 → 5 → 4 → 3 → 3 → 4)
- NEW ANALYSIS AXIS: "日本語の使いやすさ比較" appears as a self-suggested refinement
- ClickUp returns after one-week absence

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-19T20:__:__+09:00

```
# おすすめのプロジェクト管理ツール

用途やチーム規模によって最適なツールは異なります。代表的なものを目的別に紹介します。

## 1. オールラウンド型(汎用性が高い)

### Notion
- **特徴**: ドキュメント、データベース、タスク管理を一元化
- **向いているチーム**: スタートアップ、小〜中規模チーム、ナレッジ共有を重視する組織
- **料金**: 個人無料、チーム版 $8〜/ユーザー/月

### ClickUp
- **特徴**: タスク、ドキュメント、ホワイトボード、目標管理など機能が豊富
- **向いているチーム**: 1つのツールで何でも管理したいチーム
- **料金**: 無料プランあり、有料 $7〜/ユーザー/月

## 2. アジャイル開発向け

### Jira
- **特徴**: スクラム・カンバンに強く、開発チームの標準的存在
- **向いているチーム**: エンジニアリングチーム、大規模開発プロジェクト
- **料金**: 10ユーザーまで無料、$7.53〜/ユーザー/月

### Linear
- **特徴**: 高速・洗練されたUI、開発者体験に特化
- **向いているチーム**: モダンなソフトウェア開発チーム
- **料金**: 無料プランあり、$8〜/ユーザー/月

## 3. ビジュアル重視・初心者向け

### Trello
- **特徴**: カンバン方式でシンプル、直感的な操作
- **向いているチーム**: 個人〜小規模チーム、軽いタスク管理
- **料金**: 無料プランあり、$5〜/ユーザー/月

### Asana
- **特徴**: タイムライン、ボード、リストなど多彩なビュー
- **向いているチーム**: マーケティング、クリエイティブ系チーム
- **料金**: 無料プランあり、$10.99〜/ユーザー/月

## 4. 日本製・国内チーム向け

### Backlog
- **特徴**: 日本語UI、ガントチャート、Git/SVN連携
- **向いているチーム**: 日本国内のIT・受託開発企業
- **料金**: $35〜/月(ユーザー数無制限プランあり)

## 選び方の目安

| チーム特性 | おすすめ |
|---|---|
| エンジニアリング中心 | `Linear` / `Jira` |
| 非エンジニア混在 | `Asana` / `ClickUp` |
| ドキュメント重視 | `Notion` |
| シンプルさ重視 | `Trello` |
| 日本企業・受託開発 | `Backlog` |

## 個人的な推奨

- **小規模・スタートアップ**: Notion または Linear
- **中〜大規模開発チーム**: Jira
- **非IT系チーム**: Asana または Trello

まずは無料プランで2〜3個試して、チームの運用に馴染むものを選ぶのがおすすめです。チーム規模や業種を教えていただければ、より具体的に提案できます。
```

**Mentioned products**: Notion, ClickUp, Jira, Linear, Trello, Asana, Backlog (7 products)
**Explicit URL citations**: None
**Japan-origin tools**: 1 (Backlog only; kintone disappeared after one-week appearance)

**Notes vs Day 1 & Day 2**:
- Product count: 8 → 7 → 7 (stable)
- Core five (Notion/Trello/Asana/Jira/Backlog): 3/3 weeks fully preserved
- Monday.com: lost in Day 2, STILL ABSENT in Day 3 (confirmed permanent loss in Claude)
- ClickUp: present (Day 1) → absent (Day 2) → returned (Day 3) - oscillating
- Linear: appeared Day 2, PRESERVED in Day 3 (sustained canonical expansion)
- kintone: appeared Day 2 only, ABSENT in Day 3 (one-week appearance, Day 2 anomaly)
- GitHub Projects: lost in Day 2, still absent in Day 3 (permanent loss)
- Comparison table PRESERVED across all 3 weeks
- Closing personalization offer PRESERVED across all 3 weeks
- Pricing on every product PRESERVED across all 3 weeks
- Priority labels ("最重要" etc): present in Day 1 → weakened in Day 2 → absent in Day 3
- New emoji-based category labels appearing across queries

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-19T20:__:__+09:00

```
用途で選ぶのが一番です。よく挙がるおすすめは次のあたりです。

- `Asana`
  タスクやプロジェクトの一元管理に強く、連携先も多いです。中小規模〜部門横断まで使いやすいです。
- `Jira`
  開発チーム向けの定番です。ソフトウェア開発、課題管理、アジャイル運用に向いています。
- `Backlog`
  日本語で使いやすく、担当者・期限の管理がしやすいです。IT部門や日本企業で導入しやすいです。
- `Trello`
  直感的なカンバン形式で、シンプルな案件管理や個人〜小規模チームに向いています。
- `Wrike`
  タスク管理、ガントチャート、レポート、リソース管理まで幅広く対応でき、拡張性も高いです。
- `Notion`
  ドキュメントとタスクをまとめて管理したい場合に便利です。柔軟性が高い反面、運用設計が重要です。
- `Redmine`
  無料で使いやすく、課題管理や開発案件の管理に強いです。自社運用しやすいのも特徴です。

選び方の目安は以下です。
- 開発中心: `Jira` / `Redmine`
- 汎用的でバランス重視: `Asana` / `Wrike`
- シンプルに始めたい: `Trello`
- 日本語で使いやすいもの重視: `Backlog`
- ドキュメントも一緒に管理: `Notion`

もし「少人数向け」「無料で使いたい」「開発チーム向け」など条件があれば、その前提で3つに絞って提案できます。

出典：
[1] https://service.msols.com/blog/project-management-tool
[2] https://it-trend.jp/project_management/article/33-0001
[3] https://www.wrike.com/ja/project-management-guide/faq/what-are-project-management-tools/
[4] https://products.sint.co.jp/obpm/blog/project-management-advanteges.html
[5] https://lychee-redmine.jp/blogs/project/free-project-management-tools/
[6] https://www.itreview.jp/categories/project-management
[7] https://biz.moneyforward.com/work-efficiency/basic/14156/
[8] https://dstmp.shachihata.co.jp/column/0220241129/
[9] https://boxil.jp/sc-project/
```

**Mentioned products**: Asana, Jira, Backlog, Trello, Wrike, Notion, Redmine (7 products)
**Explicit URL citations**: 9 sources, 100% Japanese domains
**URL preservation Day 2 → Day 3**: 8/9 = 89%

**Notes vs Day 1 & Day 2**:
- Product count: 9 → 15 → 7 (Day 2 expansion fully reset in Day 3)
- Core seven (Asana/Jira/Backlog/Trello/Wrike/Notion/Redmine) PRESERVED across 3 weeks
- Day 2 additions (Monday, ClickUp, TimeCrowd, etc.) ALL ABSENT in Day 3
- boxil.jp URL path: Day 1 → Day 2 changed → Day 3 reverted to Day 1 (Day 2 anomaly signature)
- wrike.com/ja: NEW vendor official site
- 100% Japanese domains preserved across all 3 weeks
- Zero academic citations preserved across all 3 weeks

### q001 — Cross-model summary (Day 3)

| Model | Products | Japan-origin | URLs cited |
|---|:-:|:-:|:-:|
| Gemini | 7 | 1 | 0 |
| GPT-5.4 | 5 | 0 | 0 |
| Claude | 7 | 1 | 0 |
| Perplexity | 7 | 2 (Backlog, Redmine) | 9 |

**Day 1 → Day 2 → Day 3 canonical core (3 self-contained LLMs × 3 weeks = 9 observations)**:
- **Notion: 9/9** ✓
- **Trello: 9/9** ✓
- **Asana: 9/9** ✓
- Monday.com: 9/9 → 8/9 → 6/9 (monotonic decline)
- Backlog: 7/9 (across all models)

**Including Perplexity (4 models × 3 weeks = 12 observations)**:
- **Notion: 11-12/12** (varies by Perplexity Day 3 list)
- **Trello: 12/12** ✓
- **Asana: 12/12** ✓

This establishes MIBO **Law I (Absolute Canonical Triplet)** in the project management domain.

---

## q002 — What is the best CRM for small businesses?

**Category**: product_recommendation | **Language**: en
**First observed**: 2026-05-05 | **Second**: 2026-05-12 | **Third**: 2026-05-19

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-19T20:__:__+09:00

```
### 1. HubSpot CRM
**Best Overall for Scaling**
*   **Key Features:** Comprehensive free tier, seamless integration with marketing and service hubs, and an intuitive user interface.
*   **Pros:** The "Free Forever" plan includes contact management, deal tracking, and basic email marketing. It is highly user-friendly for beginners.
*   **Cons:** Paid tiers (Starter, Professional, Enterprise) can become very expensive as your database and feature needs grow.

### 2. Zoho CRM
**Best for Value and Customization**
*   **Key Features:** AI assistant (Zia), advanced automation, and deep integration with the Zoho ecosystem (Books, Projects, etc.).
*   **Pros:** Highly affordable paid plans compared to competitors. Offers extensive customization options to fit specific business workflows.
*   **Cons:** The interface can feel cluttered, and the learning curve is steeper than HubSpot or Pipedrive.

### 3. Pipedrive
**Best for Sales-Focused Teams**
*   **Key Features:** Visual sales pipelines, activity reminders, and automated lead triaging.
*   **Pros:** Built by salespeople for salespeople. Its visual "drag-and-drop" interface makes managing deals exceptionally easy.
*   **Cons:** Lacks robust built-in marketing tools; primarily focused on the sales funnel rather than the entire customer lifecycle.

### 4. Monday Sales CRM
**Best for Customization and Project Management**
*   **Key Features:** Built on the `monday.com` Work OS, it features highly flexible boards, automation, and integrated communication.
*   **Pros:** Excellent if you already use `monday.com` for project management. It is one of the most visually customizable platforms available.
*   **Cons:** Pricing is based on seat blocks (e.g., minimum of 3 users), which can be inefficient for solo entrepreneurs.

### 5. Salesforce Starter
**Best for Future-Proofing**
*   **Key Features:** A simplified version of the industry-standard Salesforce platform, including lead, opportunity, and case management.
*   **Pros:** Allows small businesses to start on the Salesforce ecosystem with a lower price point and easier setup.
*   **Cons:** Even the "Starter" version is more complex than most small business CRMs, and transitioning to higher tiers is a major undertaking.

### 6. Freshsales (Freshworks CRM)
**Best for AI-Powered Insights**
*   **Key Features:** "Freddy" AI for lead scoring and forecasting, built-in phone and email, and "sequences" for outreach.
*   **Pros:** Great all-in-one solution that combines sales and marketing with strong automation features.
*   **Cons:** The free version is very limited compared to HubSpot, and some advanced reporting is locked behind higher-paid tiers.

### Comparison Summary
| CRM | Best For | Starting Price |
| :--- | :--- | :--- |
| **HubSpot** | Ease of use & Scaling | Free ($15+/mo for Starter) |
| **Zoho CRM** | Features per Dollar | $14/user/mo |
| **Pipedrive** | Sales Pipeline Management | $14/user/mo |
| **Monday.com** | Workflow Customization | $12/user/mo |
| **Salesforce Starter** | Future Enterprise Needs | $25/user/mo |
```

**Mentioned products**: HubSpot CRM, Zoho CRM, Pipedrive, Monday Sales CRM, Salesforce Starter, Freshsales (6 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0

**Notes vs Day 1 & Day 2**:
- Product count: 5 → 5 → 6 (+1, Freshsales added)
- Canonical four (HubSpot/Zoho/Pipedrive/Monday): PRESERVED across all 3 weeks
- Salesforce: PRESERVED across all 3 weeks (SKU name oscillates)
  - Day 1: "Salesforce Starter"
  - Day 2: "Salesforce Essentials"
  - Day 3: "Salesforce Starter" (Day 2 anomaly signature)
- Freshsales: NEW addition in Day 3 with "AI-Powered Insights" framing
- "How to Choose" decision-tree section: absent (Day 1) → present (Day 2) → absent (Day 3, anomaly)
- Free Tier column in comparison table: absent → present → absent (Day 2 anomaly)

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-19T20:__:__+09:00

```
The best CRM for a small business depends on budget, team size, sales process, and how much automation you need. For most small businesses, these are the strongest options:

## Best overall
**HubSpot CRM**
- Very easy to start with
- Strong free plan
- Good contact management, deal tracking, email integration, and marketing tools
- Best if you want something simple that can grow with you
- Downside: advanced features can get expensive

## Best for affordability
**Zoho CRM**
- Low-cost plans
- Wide feature set
- Good for small businesses that want customization without paying enterprise prices
- Downside: interface can feel less intuitive at first

## Best for sales-focused teams
**Pipedrive**
- Excellent pipeline management
- Very easy to visualize deals and next steps
- Best for teams that mainly care about sales process and follow-up
- Downside: less powerful for marketing/service compared with broader platforms

## Best if you use Gmail / Google Workspace
**Streak**
- Works inside Gmail
- Very convenient for businesses that manage relationships mostly through email
- Best for solo founders, agencies, recruiters, and small teams
- Downside: not as full-featured as larger CRMs

## Best for all-in-one business management
**Freshsales**
- Good balance of CRM, email, phone, and automation
- Clean interface
- Best for small businesses wanting sales + communication tools together
- Downside: ecosystem is smaller than HubSpot or Zoho

## Best if you expect to scale
**Salesforce Starter / small-business options**
- Very powerful and flexible
- Huge ecosystem
- Best if you know you'll need advanced customization later
- Downside: can be more complex and costly than most small businesses need

## Quick recommendation by business type
- **Solo business / freelancer:** Streak or HubSpot CRM
- **Very small team on a budget:** Zoho CRM
- **Sales-driven small business:** Pipedrive
- **Marketing + sales in one place:** HubSpot CRM
- **Need flexibility and long-term scale:** Salesforce

## Best choice for most small businesses
**HubSpot CRM** is usually the safest recommendation because it's easy to adopt, has a strong free tier, and covers the core needs of most small businesses without much setup.

## What to compare before choosing
Look at:
- Price per user
- Ease of setup
- Email/calendar integration
- Pipeline customization
- Automation features
- Reporting
- Mobile app quality
- Upgrade costs as your team grows

## Simple shortlist
If you want the fastest shortlist:
1. **HubSpot CRM** — best overall
2. **Zoho CRM** — best value
3. **Pipedrive** — best for sales pipelines

If you want, I can also give you:
- a **side-by-side comparison table**
- the **best CRM for your specific industry**
- or a **recommendation based on your budget and team size**
```

**Mentioned products**: HubSpot CRM, Zoho CRM, Pipedrive, Streak, Freshsales, Salesforce (6 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0

**Notes vs Day 1 & Day 2**:
- Product count: 6 → 6 → 6 (stable)
- Canonical four (HubSpot/Zoho/Pipedrive/Freshsales): 3/3 weeks PRESERVED
- Salesforce: present (Day 1) → ABSENT (Day 2) → RETURNED (Day 3)
  - Confirmed: Day 2 disappearance was a transient anomaly
- Streak: NEW addition in Day 3 with Gmail-integration framing
- Bigin by Zoho: appeared Day 2 only, ABSENT in Day 3 (Day 2 anomaly)
- Monday Sales CRM: appeared Day 2 only, ABSENT in Day 3 (Day 2 anomaly)
- Closing 3-option refinement offer PRESERVED for 7th consecutive observation
  - Day 1: comparison table / industry / team-size+budget
  - Day 2: comparison table / personalized
  - Day 3: comparison table / industry / budget+team-size (NEAR-IDENTICAL to Day 1)
- NEW section "Best choice for most small businesses" with explicit single recommendation
- NEW section "Simple shortlist" with numbered top-3

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-19T20:__:__+09:00

```
# Best CRMs for Small Businesses

The "best" CRM depends on your specific needs, budget, and technical comfort level. Here's a breakdown of top options by category:

## Top Overall Picks

**HubSpot CRM** ⭐ *Best Free Option*
- Robust free tier (unlimited users)
- Easy to use, great for beginners
- Scales with paid Marketing/Sales Hubs
- **Pricing**: Free; paid plans from ~$20/month

**Zoho CRM** ⭐ *Best Value*
- Affordable with extensive features
- Strong automation and customization
- Integrates with 40+ Zoho apps
- **Pricing**: From ~$14/user/month

**Pipedrive** ⭐ *Best for Sales-Focused Teams*
- Visual pipeline management
- Simple, intuitive interface
- Excellent for tracking deals
- **Pricing**: From ~$14/user/month

## Other Strong Contenders

| CRM | Best For | Starting Price |
|-----|----------|----------------|
| **Freshsales** | AI-powered insights | ~$15/user/mo |
| **Salesforce Starter** | Growth potential | ~$25/user/mo |
| **Monday Sales CRM** | Visual project-style workflows | ~$12/user/mo |
| **Keap** | Service businesses & automation | ~$159/month |
| **Capsule CRM** | Simplicity & contact management | Free–$18/user/mo |

## How to Choose

Consider these factors:
1. **Budget** — Free tiers (HubSpot, Zoho, Capsule) work well for startups
2. **Team size** — Some price per user, others flat-rate
3. **Industry needs** — Service, retail, B2B, etc. have different requirements
4. **Integrations** — Check compatibility with your email, accounting, and marketing tools
5. **Ease of use** — Pipedrive and HubSpot are most beginner-friendly
6. **Scalability** — Will it grow with your business?

## Quick Recommendation

- **Just starting out?** → HubSpot Free
- **Tight budget, need features?** → Zoho CRM
- **Sales-driven business?** → Pipedrive
- **Want all-in-one marketing + sales?** → HubSpot or Keap

Would you like a deeper comparison of any specific CRMs, or recommendations based on your industry?
```

**Mentioned products**: HubSpot, Zoho, Pipedrive, Freshsales, Salesforce, Monday Sales CRM, Keap, Capsule CRM (8 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0

**Notes vs Day 1 & Day 2**:
- Product count: 8 → 8 → 8 (stable)
- Canonical six (HubSpot/Zoho/Pipedrive/Salesforce/Freshsales/Monday): 3/3 weeks PRESERVED
- Keap: present (Day 1) → absent (Day 2) → returned (Day 3) - Day 2 anomaly
- E-commerce category (Klaviyo, Brevo): absent → present → absent (Day 2 anomaly)
- Capsule CRM: NEW addition in Day 3 (previously only in Perplexity Day 1)
- Claude's 4-element signature: 4/4 PRESERVED across all 3 weeks
- Emoji labeling: text labels → many emojis → simplified to ⭐ (Day 3)

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-19T20:__:__+09:00

```
For most small businesses, **HubSpot CRM** is usually the best overall choice because it has a strong free plan, is easy to use, and can scale as you grow.

Best options by need:
- **Best overall:** `HubSpot CRM`
  Good free tier, simple interface, sales and marketing tools in one place
- **Best for customization and ease of use:** `Zoho CRM`
  Often a better fit if you want more flexibility at a lower cost
- **Best for sales pipeline management:** `Pipedrive`
  Great if your team mainly needs to track deals and close sales efficiently
- **Best for all-in-one enterprise growth:** `Salesforce`
  Powerful, but usually more than many small businesses need at the start

If you want a quick recommendation:
- Choose **HubSpot CRM** if you want the easiest all-around option
- Choose **Zoho CRM** if budget and customization matter most
- Choose **Pipedrive** if your sales process is the priority

If you want, I can also give you a **side-by-side comparison table** of HubSpot, Zoho, and Pipedrive.

出典：
[1] https://www.zoho.com/crm/small-business-crm-software/
[2] https://fayedigital.com/blog/best-crm-for-small-business/
[3] https://www.nimble.com/blog/best-crm-for-small-business-in-2025/
[4] https://www.salesforce.com/crm/crm-for-small-business/
[5] https://www.hubspot.com/products/crm/small-business
[6] https://mailchimp.com/resources/best-crm-for-small-business/
[7] https://www.youtube.com/watch?v=RIRyuq-AKOU
```

**Mentioned products**: HubSpot CRM, Zoho CRM, Pipedrive, Salesforce (4 products)
**Explicit URL citations**: 7 sources, 100% US domains
**URL preservation Day 2 → Day 3**: 6/7 = 86%

**Notes vs Day 1 & Day 2**:
- Product count: 7 → 9 → 4 (substantial compression)
- Canonical three (HubSpot/Zoho/Pipedrive): PRESERVED across all 3 weeks
- Salesforce: PRESERVED across all 3 weeks
- hubspot.com vendor URL: first appearance in Day 3
- Vendor-official URL share: 43% → 57% → 71% (monotonic increase)
- Day 3 response notably more compressed than Day 1 or Day 2

### q002 — Cross-model summary (Day 3)

| Model | Products | URLs cited |
|---|:-:|:-:|
| Gemini | 6 | 0 |
| GPT-5.4 | 6 | 0 |
| Claude | 8 | 0 |
| Perplexity | 4 | 7 |

**4 models × 3 weeks = 12 observations canonical analysis**:
- **HubSpot: 12/12** ✓
- **Zoho: 12/12** ✓
- **Pipedrive: 12/12** ✓
- Salesforce: 11/12 (lost in GPT-5.4 Day 2 only — Day 2 anomaly)
- Freshsales: 10/12

This establishes MIBO **Law I** in the CRM domain.

---

## q003 — 睡眠の質を上げる方法を教えて

**Category**: health | **Language**: ja
**First observed**: 2026-05-05 | **Second**: 2026-05-12 | **Third**: 2026-05-19

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-19T21:__:__+09:00

```
### 1. 日中の行動習慣
*   **起床直後に太陽光を浴びる**
    体内の生物時計がリセットされ、約14〜16時間後に眠気を誘うホルモンである「メラトニン」の分泌が促されます。
*   **適度な運動を行う**
    夕方から夜（就寝の3時間前まで）に軽い有酸素運動を行うと、就寝時の体温低下がスムーズになり、深い眠りに入りやすくなります。
*   **昼寝は20分以内に留める**
    長すぎる昼寝や、午後3時以降の仮眠は夜間の睡眠圧（眠気）を低下させます。

### 2. 就寝前のルーチン
*   **入浴は就寝の90分前に済ませる**
    40度前後のお湯に15分ほど浸かり、深部体温を一時的に上げることが重要です。その後、体温が下がっていく過程で自然な眠気が生じます。
*   **ブルーライトを遮断する**
    スマートフォンやPCの光は脳を覚醒させ、メラトニンの分泌を抑制します。就寝の1〜2時間前からは使用を控えるのが理想的です。
*   **リラクゼーションを取り入れる**
    ストレッチ、読書、落ち着いた音楽、アロマテラピーなど、副交感神経を優位にする活動を行います。

### 3. 食生活の調整
*   **カフェインの摂取時間に注意する**
    カフェインの覚醒作用は数時間持続するため、午後の早い時間以降（目安として14時以降）は摂取を控えます。
*   **夕食は就寝の3時間前までに終える**
    寝る直前の食事は消化活動のために内臓が働き続け、睡眠の質を低下させます。
*   **寝酒を控える**
    アルコールは入眠を助ける一方で、睡眠の質を著しく下げ、中途覚醒（夜中に目が覚めること）の原因となります。

### 4. 寝室環境の整備
*   **適切な室温と湿度を保つ**
    夏場は25〜28度、冬場は15〜18度、湿度は50〜60%が理想とされています。
*   **光と音を遮断する**
    遮光カーテンを使用したり、耳栓やアイマスクを活用して、外部からの刺激を最小限に抑えます。
*   **寝具の適合性を確認する**
    自分の体型に合った「枕」や、寝返りが打ちやすい「マットレス」を選ぶことが、身体への負担を軽減し熟睡につながります。

### 5. 心理的アプローチ
*   **「寝なければならない」という強迫観念を捨てる**
    眠れないときは一度ベッドから出て、リラックスした状態で眠気が来るのを待ちます。ベッドの上で悩む時間が長くなると、脳が「ベッドは悩む場所」と誤学習してしまいます。
```

**Numeric specificity**: 11-12 quantitative claims (Day 1: 12, Day 2: 9, Day 3: 11-12 RESTORED)

**Notes vs Day 1 & Day 2**:
- Item count: 13 → 13 → 13 (stable)
- **Numeric specificity: 12 → 9 → 11-12 (RECOVERED to baseline) — P12 refutation**
- 11/12 canonical sleep habits preserved
- "適度な運動": present (Day 1) → absent (Day 2) → RESTORED (Day 3)
- "心理的アプローチ" category: 0 → 2 items → 1 item (partial persistence)
- LaTeX-style notation: present (Day 1) → absent (Day 2) → absent (Day 3, permanent change)
- Room temperature values: Day 2's revisions preserved in Day 3
- Time-based numerics: Day 2 abstraction → Day 3 restoration (asymmetric reversal)

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-19T21:__:__+09:00

```
## すぐ効きやすい基本
- **起きる時間を毎日そろえる**
  - 寝る時間より、まず起床時間の固定が重要です。
- **朝に光を浴びる**
  - 起床後すぐにカーテンを開けて、できれば外で数分〜15分ほど光を浴びます。
- **寝る90分前に入浴**
  - ぬるめのお風呂で体温をいったん上げると、その後の体温低下で眠りやすくなります。
- **就寝前のスマホを減らす**
  - 強い光や情報刺激で脳が覚醒しやすくなります。寝る30〜60分前は控えめに。
- **カフェインは午後遅く以降避ける**
  - コーヒー、エナジードリンク、濃いお茶は睡眠を浅くしやすいです。
- **寝酒は避ける**
  - 寝つきは良くなっても、途中で目が覚めやすくなり、睡眠の質が下がりやすいです。

## 寝室環境の整え方
- **少し暗め**
  - 光はできるだけ減らす。豆電球や通知ランプも意外と気になります。
- **静かめ**
  - 難しければ耳栓やホワイトノイズも有効です。
- **涼しめ**
  - 暑すぎると眠りが浅くなりやすいです。
- **寝具を見直す**
  - 枕の高さ、マットレスの硬さ、掛け布団の温度感はかなり重要です。

## 生活習慣で効くこと
- **日中に適度な運動**
  - 散歩、軽い筋トレ、ストレッチなど。激しい運動は就寝直前だと逆効果なことがあります。
- **昼寝は短く**
  - するなら15〜20分程度、遅い時間は避ける。
- **夕食は寝る直前に食べない**
  - 満腹すぎると眠りにくくなります。
- **寝る前に考え事を持ち込まない**
  - メモに書き出して「明日考える」にすると頭が静まりやすいです。

## 寝つきが悪いときのコツ
- **無理に寝ようとしない**
  - 焦るほど眠れなくなります。
- **20〜30分眠れないなら一度ベッドを出る**
  - 暗めの部屋で、読書や軽いストレッチなど静かな行動をして、眠気が来たら戻る。
- **時計を何度も見ない**
  - 不安が強くなって逆効果です。

## サプリ・飲み物について
- **温かいノンカフェイン飲料**
  - 白湯、カモミールなどは合う人がいます。
- **サプリは体質差が大きい**
  - 使うなら成分や副作用、他の薬との相互作用に注意が必要です。

## 受診を考えたほうがいいサイン
- いびきが大きい、呼吸が止まると言われる
- 日中の眠気が強すぎる
- 寝ても疲れが取れない状態が続く
- 2週間以上、強い不眠が続く
- 気分の落ち込みや不安が強い

## 最低限これだけやるなら
1. 毎日起きる時間を固定
2. 朝の光を浴びる
3. カフェインを午後遅くから控える
4. 寝る前のスマホを減らす
5. 寝る90分前に入浴する

## 1週間の実践例
- **朝**: 同じ時間に起きる、日光を浴びる
- **昼**: 少し歩く、カフェインは取りすぎない
- **夕方**: 軽く体を動かす
- **夜**: 寝る90分前に入浴、寝る1時間前は照明とスマホを控える
- **就寝前**: 部屋を暗く静かにして、必要なら考え事をメモに出す

必要なら次に、
- **「原因別チェックリスト」**
- **「今日からできる睡眠改善プラン」**
- **「不眠気味の人向けの対処法」**

のどれかに絞って整理できます。
```

**Numeric specificity**: 6 quantitative claims (Day 1: 5-6, Day 2: 3, Day 3: 6 RECOVERED)

**Notes vs Day 1 & Day 2**:
- **Numeric specificity: 5-6 → 3 → 6 (RECOVERED to Day 1 baseline) — P12 refutation**
- Structure: flat 10-item list → flat 10-item list → 6 CATEGORIES (major shift)
- "Minimum action" section: 3 steps → 5 items → 5 steps + 1-week practice example (continued expansion)
- Closing 3-option refinement offer: 9/9 observations PRESERVED
- Medical disclaimer section name: "受診を考えたほうがいいサイン" → "注意したいサイン" → "受診を考えたほうがいいサイン" (Day 2 anomaly)
- New category in Day 3: "サプリ・飲み物について"
- New section in Day 3: "1週間の実践例"

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-19T21:__:__+09:00

```
# 睡眠の質を上げる方法

睡眠の質を改善するには、生活習慣・環境・心理面の3つの側面からアプローチすることが効果的です。

## 1. 生活リズムを整える
- **起床時間を固定する**：休日も平日と同じ時間に起きることで体内時計が安定します
- **朝日を浴びる**：起床後30分以内に15分程度の日光浴で、メラトニン分泌のリズムが整います
- **昼寝は20〜30分以内**：15時以降の長い昼寝は夜の睡眠を妨げます

## 2. 食事と運動
- **カフェインは就寝6時間前まで**：コーヒー、紅茶、エナジードリンクに注意
- **アルコールは控える**：寝つきは良くなっても、深い睡眠が減少します
- **夕食は就寝3時間前まで**に済ませる
- **適度な有酸素運動**：週3回程度、ただし就寝直前の激しい運動は避ける

## 3. 寝室環境の最適化

| 要素 | 推奨される状態 |
|------|--------------|
| 室温 | 夏：25〜26℃／冬：18〜20℃ |
| 湿度 | 50〜60% |
| 照明 | 真っ暗、または暖色系の常夜灯 |
| 音 | 40dB以下（図書館レベル） |

- 寝具（マットレス・枕）は自分の体に合ったものを選ぶ
- 寝室は「眠るための場所」と位置づけ、仕事や勉強に使わない

## 4. 就寝前の習慣
- **就寝90分前の入浴**：38〜40℃のお湯に15分浸かると、深部体温が下がるタイミングで眠気が来ます
- **スマホ・PCは就寝1時間前まで**：ブルーライトがメラトニン分泌を抑制します
- **リラックス習慣**を取り入れる：
  - 軽いストレッチ
  - 深呼吸（4秒吸って7秒止めて8秒吐く「4-7-8呼吸法」）
  - 読書（紙の本）
  - 瞑想やマインドフルネス

## 5. 心理面のケア
- **「眠らなきゃ」と焦らない**：眠れないときは一度ベッドから出て、暗めの照明で静かに過ごす
- **悩み事は書き出す**：頭の中を「外に出す」ことで思考のループを止められます
- **感謝日記**：寝る前に良かったことを3つ書くと、ポジティブな気持ちで眠れます

## まずは1つから始める
すべて一度に変えようとすると続きません。**「起床時間を固定する」「就寝90分前に入浴する」**など、取り組みやすいものから1〜2週間試してみることをおすすめします。

もし、これらを試しても改善しない、日中の眠気が強い、いびきがひどいなどの症状がある場合は、睡眠時無呼吸症候群などの可能性もあるため、医療機関への相談を検討してください。
```

**Numeric specificity**: 10+ quantitative claims (Day 1: 10, Day 2: 8, Day 3: 10 RECOVERED + 2 new: 40dB, 4-7-8 breathing)

**Notes vs Day 1 & Day 2**:
- Item count: 8 categories → 6 → 5 (continued compression)
- **Numeric specificity: 10 → 8 → 10 (RECOVERED to baseline + 2 new) — P12 refutation**
- "最重要" priority labels: present → absent → restored as structured "minimum action" section
- Comparison table: food → food+water → bedroom environment (structure preserved, content shifts)
- Bath temperature: "38〜40℃" → "40℃" → "38〜40℃" (Day 2 anomaly)
- Minimum-action set: 3 → 2 → 2 items (different content each time)
- Medical referral: brief → 4 symptoms → specific disease name "sleep apnea" (continued strengthening)
- Claude's 4-element signature: 4/4 PRESERVED across all 3 weeks

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-19T21:__:__+09:00

```
睡眠の質を上げるには、まず「体内時計を整える」「寝る前の刺激を減らす」「寝室環境を整える」の3つを意識すると効果的です。

## すぐできる方法
- 毎日できるだけ同じ時間に起きる
- 朝起きたら日光を浴びる
- 適度な運動を日中に行う
- 夕食は寝る3時間前までに済ませる
- カフェインやお酒を寝る前は控える
- 寝る1時間前はスマホやPCを見すぎない
- ぬるめのお風呂に入ってリラックスする
- 寝室を暗く、静かで、快適な温度にする

## 特に大事なポイント
- **朝の光**: 体内時計が整いやすくなります
- **日中の運動**: 深い眠りにつながりやすくなります
- **就寝前のリラックス**: 入眠しやすくなります
- **寝室環境**: 光・音・温度の影響を減らせます

## 生活のコツ
- 寝る前に考えごとが多いなら、メモに書き出す
- 寝だめより、毎日の睡眠リズムを優先する
- 眠れない日が続くなら、生活習慣だけでなく体調面も確認する

必要なら、あなたの生活に合わせて「平日向け」「夜型向け」「スマホをやめられない人向け」に絞って具体的に提案できます。

出典：
[1] https://www.mtgec.jp/wellness/sixpad/column/improve-sleep-quality/
[2] https://wellness.shionogi.co.jp/insomnia/trial/trial.html
[3] https://www.fujiyaku-direct.com/health_information/article/088main
[4] https://www.glico.com/jp/powerpro/citric-acid/entry91/
[5] https://www.iyobank.co.jp/sp/iyomemo/entry/20230627.html
[6] https://banno-clinic.biz/sleep-quality/
[7] https://alinamin-kenko.jp/tokushu/suimin_sitsu/merit.html
[8] https://kennet.mhlw.go.jp/slp/event/sleep_quality/index.html
[9] https://brand.taisho.co.jp/contents/tsukare/457/
[10] https://www.youtube.com/watch?v=1D7Yfq6kHtQ
```

**Explicit URL citations**: 10 sources, 100% Japanese domains
**URL preservation Day 2 → Day 3**: 9/10 = 90%

**Notes vs Day 1 & Day 2**:
- URL preservation: 100% (D1→D2) → 90% (D2→D3) - still very high
- Iyo Bank (regional bank): preserved 3 weeks
- Daiwa House: lost in Day 3 (was preserved Day 1-2)
- Alinamin-kenko: NEW vendor official pharma site
- 100% Japanese domains preserved across all 3 weeks
- Zero academic citations preserved across all 3 weeks
- Response COMPRESSION in Day 3 (matches q001, q002 pattern)
- Numeric trajectory: ~5 → ~7 → 2-3 (Perplexity-specific shift, NOT Day 2 anomaly)

### q003 — Cross-model summary (Day 3)

| Model | Numeric trajectory | URLs cited |
|---|:-:|:-:|
| Gemini | 12 → 9 → 12 (recovered) | 0 |
| GPT-5.4 | 5-6 → 3 → 6 (recovered) | 0 |
| Claude | 10 → 8 → 10 (recovered) | 0 |
| Perplexity | ~5 → ~7 → 2-3 (compressed) | 10 |

**Canonical 10 sleep habits across 4 models × 3 weeks (40 observations)**:
- 8/10 habits preserved at 12/12 (100%)
- "Wake-time consistency, morning light, pre-sleep screen reduction, caffeine restriction, alcohol caution, bath timing, dinner timing, relaxation"

This establishes MIBO **Law I** in the health domain (canonical 10).

---

## q004 — How do I implement RAG with a vector database?

**Category**: technical | **Language**: en
**First observed**: 2026-05-19 (baseline)

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-19T22:__:__+09:00

```
### 1. Architectural Workflow
The Retrieval-Augmented Generation (RAG) process consists of two main phases: the **Ingestion Pipeline** (offline) and the **Retrieval/Generation Pipeline** (online).

#### Ingestion Pipeline
1.  **Load Documents**: Import raw data (PDFs, Markdown, HTML, etc.).
2.  **Chunking**: Split documents into smaller, overlapping segments to maintain context and fit within the embedding model's token limits.
3.  **Embedding**: Convert text chunks into high-dimensional numerical vectors using an embedding model (e.g., `text-embedding-3-small`).
4.  **Vector Store**: Upsert the vectors and their corresponding original text (metadata) into a vector database.

#### Retrieval/Generation Pipeline
1.  **Query Embedding**: Convert the user's natural language query into a vector using the same embedding model.
2.  **Similarity Search**: Compare the query vector against the vector database to find the $k$ most similar chunks (using metrics like Cosine Similarity or Euclidean Distance).
3.  **Context Augmentation**: Combine the retrieved text chunks with the user's original query into a prompt template.
4.  **LLM Generation**: Send the augmented prompt to a Large Language Model (LLM) to produce a grounded response.

---

### 2. Similarity Metric
To find relevant context, vector databases typically calculate the Cosine Similarity between the query vector $A$ and a stored vector $B$:

[ \text{similarity} = \cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|} ]

---

### 3. Implementation Example
The following implementation uses `LangChain`, `ChromaDB` (vector database), and `OpenAI`.

```python
# File: rag_example.py
import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA

# 1. Setup Environment
os.environ["OPENAI_API_KEY"] = "your_api_key_here"

# 2. Load and Chunk Data
loader = TextLoader("data_source.txt")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
texts = text_splitter.split_documents(documents)

# 3. Embed and Store in Vector Database
embeddings = OpenAIEmbeddings()
vector_db = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

# 4. Initialize Retrieval Chain
llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_db.as_retriever(search_kwargs={"k": 3})
)

# 5. Execute Query
query = "What are the specific requirements mentioned in the document?"
response = qa_chain.invoke(query)
print(response["result"])
```

### 4. Key Considerations for Implementation
*   **Chunking Strategy**: The size of your chunks affects the context provided to the LLM.
*   **Vector Database Choice**:
    *   **Serverless/Managed**: Pinecone, Weaviate, MongoDB Atlas Vector Search.
    *   **Open Source/Self-hosted**: Chroma, Milvus, Qdrant.
    *   **In-Memory**: FAISS (Facebook AI Similarity Search).
*   **Metadata Filtering**: Most vector databases allow you to store metadata for filtering.
*   **Top-K Selection**: The value of $k$ determines how many documents are retrieved.
```

**Mentioned tools/products**: LangChain, Chroma/ChromaDB, OpenAI, Pinecone, Weaviate, MongoDB Atlas Vector Search, Milvus, Qdrant, FAISS (9 products)
**Code samples**: 27-line Python (executable, LangChain + Chroma + OpenAI)
**LaTeX-style notation**: PRESENT (cosine similarity formula, $k$ notation - domain-specific)
**Explicit URL citations**: None
**Academic/arXiv references**: None
**Recommended defaults**: Chroma, LangChain, OpenAI embeddings, GPT-4o, k=3, chunk=1000, overlap=100

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-19T22:__:__+09:00

```
## RAG with a vector database: implementation flow

### 1. What RAG is
RAG stands for **Retrieval-Augmented Generation**.

Instead of asking an LLM to answer from its parametric memory alone, you:

1. **Store knowledge** from your documents in a searchable system
2. **Retrieve relevant chunks** for a user query
3. **Send those chunks as context** to the LLM
4. **Generate an answer grounded in retrieved data**

A vector database is commonly used for step 2.

### 2. Core architecture

Typical pipeline:

1. **Ingestion**
   - Load documents
   - Clean and normalize text
   - Split into chunks
   - Generate embeddings for each chunk
   - Store vectors + metadata in a vector database

2. **Query-time retrieval**
   - Embed the user query
   - Search the vector DB for similar chunks
   - Optionally rerank results
   - Build a prompt with retrieved context
   - Ask the LLM to answer using that context

### 3. Main components

#### Documents
Examples: PDFs, HTML pages, Markdown, Internal wiki pages, Support tickets, Product manuals

#### Chunking
- 300–800 tokens per chunk
- 50–150 token overlap

#### Embeddings
Convert text into vectors: Document chunks → stored in DB; User query → searched against DB

#### Vector database
Examples: Pinecone, Weaviate, Milvus, Qdrant, pgvector on PostgreSQL

#### Generator LLM
Takes user question, retrieved chunks, instructions; returns grounded answer often with citations

### 5. Minimal pseudocode

```python
documents = load_documents("/data/docs")
chunks = []
for doc in documents:
    text = extract_text(doc)
    doc_chunks = split_text(text, chunk_size=500, overlap=100)
    for i, chunk in enumerate(doc_chunks):
        chunks.append({
            "id": f"{doc.id}_{i}",
            "text": chunk,
            "metadata": {"document_id": doc.id, "title": doc.title, "source": doc.source}
        })

for chunk in chunks:
    chunk["embedding"] = embedding_model.embed(chunk["text"])

vector_db.upsert(chunks)

def answer_query(user_query):
    query_embedding = embedding_model.embed(user_query)
    results = vector_db.search(vector=query_embedding, top_k=5)
    context = "\n\n".join([r["text"] for r in results])
    prompt = f"Answer the question using only the context below.\n\nContext:\n{context}\n\nQuestion:\n{user_query}"
    return llm.generate(prompt)
```

### 7. Example stack options

#### Simple and common
- Embeddings: OpenAI embedding model
- Vector DB: Pinecone or Qdrant
- LLM: GPT-family model
- App layer: Python + FastAPI

#### Open-source oriented
- Embeddings: BGE, E5, or Instructor
- Vector DB: Weaviate, Milvus, Qdrant
- Generator: open-weight LLM
- Orchestration: LangChain or LlamaIndex

#### PostgreSQL-based
- Storage: PostgreSQL + `pgvector`

### 13. Common mistakes
- Chunking too large
- No overlap at all
- Not storing metadata
- Ignoring permissions
- Using only vector search when keyword search is needed
- Sending too many low-quality chunks to the LLM
- Not evaluating retrieval separately from generation
- Re-embedding everything unnecessarily on every update

### 14. Good starter blueprint
1. Split docs into 500-token chunks with 75-token overlap
2. Generate embeddings
3. Store in `pgvector` or Qdrant
4. Retrieve top 5 by cosine similarity
5. Add metadata filters
6. Prompt LLM to answer only from retrieved context
7. Return citations
8. Add reranking later

### 16. Recommended next step
If you want, I can give you one of these next:

1. a **full Python example** using OpenAI + Qdrant
2. a **PostgreSQL/pgvector implementation**
3. a **LangChain-based RAG example**
4. a **system design diagram and folder structure**
```

[Note: full response was 16 sections; abbreviated here for brevity. Complete response in observation log.]

**Mentioned tools/products** (10+): Pinecone, Weaviate, Milvus, Qdrant, pgvector, LangChain, LlamaIndex, OpenAI, BGE, E5, Instructor, PostgreSQL, FastAPI
**Code samples**: 40+ line Python pseudocode + JSON schema + Prompt template
**Closing 4-option refinement offer**: PRESENT (10/10 observations across all queries)

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-19T22:__:__+09:00

```
RAG works in two phases: indexing (one-time, offline) and querying (every request).

Indexing pipeline:
1. Load your documents
2. Split them into chunks (typically 200-1000 tokens with some overlap)
3. Generate an embedding vector for each chunk
4. Store the chunks + vectors in a vector database

Query pipeline:
1. Embed the user's question with the same embedding model
2. Search the vector DB for the top-k most similar chunks (cosine similarity or dot product)
3. Stuff those chunks into the LLM prompt as context
4. Generate the answer

Here's a minimal working example using Chroma (local, no setup) and the Anthropic + OpenAI APIs:

```python
import chromadb
from openai import OpenAI
from anthropic import Anthropic

openai_client = OpenAI()
anthropic_client = Anthropic()

# --- INDEXING ---
chroma = chromadb.PersistentClient(path="./db")
collection = chroma.get_or_create_collection("docs")

def chunk_text(text, size=500, overlap=50):
    words = text.split()
    chunks = []
    for i in range(0, len(words), size - overlap):
        chunks.append(" ".join(words[i:i + size]))
    return chunks

def embed(texts):
    resp = openai_client.embeddings.create(
        model="text-embedding-3-small",
        input=texts
    )
    return [d.embedding for d in resp.data]

def index_document(doc_id, text):
    chunks = chunk_text(text)
    embeddings = embed(chunks)
    collection.add(
        ids=[f"{doc_id}_{i}" for i in range(len(chunks))],
        embeddings=embeddings,
        documents=chunks,
    )

# --- QUERYING ---
def ask(question, k=4):
    q_embedding = embed([question])[0]
    results = collection.query(query_embeddings=[q_embedding], n_results=k)
    context = "\n\n---\n\n".join(results["documents"][0])

    message = anthropic_client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"Answer using only this context:\n\n{context}\n\nQuestion: {question}"
        }]
    )
    return message.content[0].text
```

Practical things that actually matter:

Chunking strategy tends to dominate quality. Splitting mid-sentence destroys meaning, so split on paragraph or sentence boundaries when possible. Libraries like LangChain's `RecursiveCharacterTextSplitter` or LlamaIndex's `SentenceSplitter` handle this. For structured docs (markdown, code, PDFs with sections), split on the structure.

Embedding model needs to match your domain. `text-embedding-3-small` is cheap and good for English; for code use something like `voyage-code-3`; for multilingual use `multilingual-e5-large`. Whatever you pick, you must use the same model for indexing and querying.

Retrieval quality often improves a lot with hybrid search (combine semantic vector search with BM25 keyword search) and a reranker (e.g. Cohere Rerank or `bge-reranker`) applied to the top 20-50 results to pick the final 3-5. Pure vector search misses exact keyword matches.

Vector DB choice — for prototyping, Chroma or FAISS in-process. For production: pgvector (if you already use Postgres), Qdrant, Weaviate, or managed Pinecone/Turbopuffer. They mostly differ in operational overhead, not retrieval quality.

Evaluation matters more than people expect. Build a small set of ~30 question-answer pairs from your docs and measure retrieval recall (did the right chunk appear in top-k?) separately from answer quality. Otherwise you can't tell whether the retriever or the generator is at fault.

Want me to go deeper on any of these — chunking, reranking, evaluation, or picking a vector DB for a specific use case?
```

**Mentioned tools/products** (13): Chroma, FAISS, pgvector, Qdrant, Weaviate, Pinecone, Turbopuffer, LangChain, LlamaIndex, OpenAI, voyage-code-3, multilingual-e5-large, Cohere Rerank, bge-reranker
**Code samples**: 35-line Python (Chroma + OpenAI embedding + Anthropic LLM — self-referential)
**Recommended LLM in code**: claude-opus-4-7 (Anthropic self-recommendation)
**Closing 4-theme refinement offer**: PRESENT (Claude's 4-element signature preserved)
**Unique mention**: Turbopuffer (2024 startup, only Claude among 4 models)

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-19T22:__:__+09:00

```
RAG with a vector database is usually implemented as a 4-step pipeline:

1. Ingest and chunk your data
   - Split documents into smaller chunks.
   - Attach metadata such as source, page, timestamp, or access permissions.

2. Create embeddings and store them
   - Convert each chunk into a vector embedding with an embedding model.
   - Save the vectors plus metadata in a vector database.

3. Retrieve relevant context at query time
   - Convert the user question into an embedding.
   - Run semantic similarity search in the vector database.
   - Optionally apply metadata filters, deduplicate results, and rerank.

4. Generate the answer
   - Combine the retrieved chunks with the user question.
   - Send that augmented prompt to the LLM to produce the final response.

A practical implementation flow looks like this:

- Data prep
  - Load PDFs, HTML, Markdown, or database records
  - Clean text
  - Chunk by size and overlap
  - Generate embeddings

- Indexing
  - Store: chunk_text, embedding, source, page, doc_id, other metadata

- Retrieval
  - Embed the query
  - Search top `k` nearest vectors
  - Filter by metadata if needed
  - Optionally rerank by relevance

- Generation
  - Build a prompt with system instructions, user question, retrieved context
  - Ask the LLM to answer using only the provided context when appropriate

Minimal pseudocode:

```python
def answer_question(query):
    query_vec = embed(query)
    hits = vector_db.search(query_vec, top_k=5)
    context = "\n\n".join(hit.text for hit in hits)
    prompt = f"""
    Use the context below to answer the question.
    Context:
    {context}
    Question:
    {query}
    """
    return llm.generate(prompt)
```

Key implementation choices:
- Chunking strategy matters
- Use metadata filters
- Consider hybrid search
- Add reranking
- Handle freshness
- Reduce hallucinations

If you want, I can turn this into:
- a Python example with `pgvector`, `Qdrant`, or `Pinecone`
- an architecture diagram
- a production-ready RAG checklist

出典：
[1] https://objectbox.io/retrieval-augmented-generation-rag-with-vector-databases-expanding-ai-capabilities/
[2] https://learnopencv.com/vector-db-and-rag-pipeline-for-document-rag/
[3] https://www.zenml.io/blog/vector-databases-for-rag
[4] https://writer.com/engineering/rag-vector-database/
[5] https://www.meilisearch.com/blog/vector-dbs-rag
[6] https://learn.microsoft.com/en-us/shows/generative-ai-for-beginners/retrieval-augmented-generation-rag-and-vector-databases-generative-ai-for-beginners
[7] https://www.youtube.com/watch?v=4l8zhHUBeyI
[8] https://github.com/microsoft/generative-ai-for-beginners/blob/main/15-rag-and-vector-databases/README.md
```

**Mentioned tools/products**: pgvector, Qdrant, Pinecone (3 products, only in closing offer)
**Code samples**: 10-line Python pseudocode (most concise)
**Explicit URL citations**: 8 sources, 100% English-domain
**Academic/arXiv references**: 0 — Universal absence of academic citations CONFIRMED
**Source-type breakdown**: vendor-official 2, public docs 1 (Microsoft Learn), tech community 2, GitHub README 1, video 1, AI tool blog 1

### q004 — Cross-model summary (Day 1 baseline)

| Model | Products | Code | URLs cited |
|---|:-:|:-:|:-:|
| Gemini | 9 | 27 lines | 0 |
| GPT-5.4 | 10+ | 40+ lines | 0 |
| Claude | 13 | 35 lines | 0 |
| Perplexity | 3 | 10 lines | 8 |

**Vector DB consensus (4 models)**:
- **Pinecone: 4/4** ✓
- **Qdrant: 4/4** ✓
- Weaviate: 3/4
- pgvector: 3/4
- Milvus: 2/4, Chroma: 2/4, FAISS: 2/4

**Framework consensus**:
- **LangChain: 3/4** (Perplexity does not name in body)
- LlamaIndex: 2/4

MIBO **Law I (Absolute Canonical Triplet)** appears to hold in technical domain at baseline. Confirmation requires longitudinal observation.

---

## q005 — 日本の代表的なAI研究者を5人挙げて

**Category**: people / named entities | **Language**: ja
**First observed**: 2026-05-19 (baseline)

### Gemini response

Model version: Gemini 3.0 Flash
Timestamp: 2026-05-19T22:__:__+09:00

```
1. **松尾 豊（まつお ゆたか）**
   東京大学大学院工学系研究科教授。日本ディープラーニング協会（JDLA）の理事長を務め、日本におけるディープラーニングの研究と普及、社会実装を牽引する第一人者です。

2. **甘利 俊一（あまり しゅんいち）**
   東京大学名誉教授、理化学研究所栄誉研究員。情報幾何学の創始者として知られ、ニューラルネットワークの数学的基礎を築いた世界的な権威です。

3. **福島 邦彦（ふくしま くにひこ）**
   大阪大学名誉教授。1979年に視覚神経系の構造を模した「ネオコグニトロン」を開発しました。これは、現在のディープラーニングの基幹技術である畳み込みニューラルネットワーク（CNN）の先駆けとなりました。

4. **杉山 将（すぎやま まさし）**
   理化学研究所革新知能統合研究センター（AIP）センター長、東京大学大学院新領域創成科学研究科教授。機械学習の理論やアルゴリズムにおいて、国際的に高い評価を受けている研究者です。

5. **北野 宏明（きたの ひろあき）**
   ソニーグループ株式会社専務、株式会社ソニーコンピュータサイエンス研究所（Sony CSL）代表取締役社長。ロボカップの創設やシステムバイオロジーの提唱、AIによる科学的発見を目指す「AI Scientist」プロジェクトなどで知られています。
```

**Gender distribution**: 5 M / 0 F (100% male)
**Institutional concentration**: 3/5 University of Tokyo
**Generational distribution**: 80s × 2, 60s × 1, 50s × 2
**Type**: 4 pure academic, 1 industry-academic mix
**Furigana**: Provided for all names
**Explicit URL citations**: None

### ChatGPT response

Model version: GPT-5.4
Timestamp: 2026-05-19T22:__:__+09:00

```
- 松尾 豊（東京大学、深層学習・AI戦略）
- 杉山 将（理化学研究所／東京大学、機械学習理論）
- 國吉 康夫（東京大学、知能ロボティクス・発達学習）
- 竹内 一郎（京都大学、機械学習・データ科学）
- 山川 宏（全脳アーキテクチャ・汎用人工知能研究）
```

**Gender distribution**: 5 M / 0 F (100% male)
**Institutional concentration**: 3/5 University of Tokyo
**Response style**: Most compressed (no descriptions, no furigana, ~100 chars total)
**Signature elements ABSENT in q005**: closing 3-4 option refinement offer, prescriptive recommendation, common mistakes section, numeric details
**Critical observation**: First instance in 10 observations where GPT-5.4's main signature breaks

### Claude response

Model version: Claude Opus 4.7
Timestamp: 2026-05-19T22:__:__+09:00

```
# 日本の代表的なAI研究者5人

## 1. 松尾 豊（まつお ゆたか）
- **所属**: 東京大学大学院工学系研究科 教授
- **専門**: ディープラーニング、Webマイニング
- 日本ディープラーニング協会（JDLA）の理事長を務め、日本におけるAI普及・人材育成の中心人物。政府のAI戦略にも深く関与。

## 2. 甘利 俊一（あまり しゅんいち）
- **所属**: 理化学研究所 栄誉研究員、東京大学 名誉教授
- **専門**: 数理脳科学、情報幾何学、ニューラルネットワーク
- ニューラルネットワーク研究の世界的パイオニアであり、「情報幾何学」を創始。深層学習の理論的基盤に大きな影響を与えた。

## 3. 福島 邦彦（ふくしま くにひこ）
- **所属**: ファジィシステム研究所 特別研究員
- **専門**: 神経回路モデル、パターン認識
- 1980年に発表した「ネオコグニトロン」は、現代の畳み込みニューラルネットワーク（CNN）の原型として知られ、2021年にバウワー賞を受賞。

## 4. 中島 秀之（なかしま ひでゆき）
- **所属**: 札幌市立大学 名誉教授、東京大学 特任教授
- **専門**: 人工知能、認知科学、マルチエージェントシステム
- 日本のAI研究の草分け的存在で、人工知能学会の元会長。状況依存型AIや構成的情報学を提唱。

## 5. 山田 誠二（やまだ せいじ）
- **所属**: 国立情報学研究所 教授
- **専門**: ヒューマンエージェントインタラクション（HAI）、知的システム
- 人間とAIエージェントの協調的相互作用の研究で著名。人工知能学会の元会長としても活躍。

---

このほかにも、**新井 紀子**（数学・「東ロボくん」プロジェクト）、**栗原 聡**（マルチエージェント・自律AI）、**石黒 浩**（アンドロイド研究）など、各分野で世界的に著名な研究者が多数存在します。
```

**Gender distribution**: Main 5M/0F; Including supplementary 7M/1F (新井紀子 = first and only female mention across 4 models)
**Institutional concentration**: 2/5 University of Tokyo; 1 NII; 1 Sapporo Municipal U; 1 Fuzzy Systems Lab
**Specific facts**: 1980 Neocognitron, 2021 Bauer Award
**Selection criterion**: Two former presidents of Japan Society for AI selected
**Closing supplementary mention**: Claude's signature "network completeness" pattern preserved in person-domain

### Perplexity response

Model: Perplexity (Web search mode)
Timestamp: 2026-05-19T22:__:__+09:00

```
- 松尾豊
- 萩原一平
- 中島秀之
- 山岸順一
- 奥田達也

出典：
[1] https://www.ailead.app/blog/yutaka-matsuo
[2] https://www.businessinsider.jp/article/206227/
[3] https://nissenad-digitalhub.com/articles/university-ai-research-2/
[4] https://scienceportal.jst.go.jp/stories/20241113_e01/
[5] https://www.youtube.com/watch?v=k1yK7b7z7-E
[6] https://www.meti.go.jp/shingikai/mono_info_service/digital_jinzai/pdf/008_05_00.pdf
[7] https://www.youtube.com/watch?v=5mOPk5gWdQ4
[8] https://www.youtube.com/watch?v=PXy7qAVqPjc
```

**Gender distribution**: 5 M / 0 F (100% male)
**Response style**: Names only, no descriptions, no affiliations stated
**Explicit URL citations**: 8 sources, 100% Japan-related domains
**Academic/arXiv references**: 0
**Source-type breakdown**: YouTube 4 (50%), public/government 2 (JST, METI), AI/business media 1, business media 1, owned media (Dentsu) 1
**Notable**: First observation of high YouTube citation rate (50%) and government documents (JST, METI) in person queries

### q005 — Cross-model summary (Day 1 baseline)

| Model | M:F (top 5) | Tokyo-U | Style | URLs |
|---|:-:|:-:|---|:-:|
| Gemini | 5:0 | 60% | Detailed | 0 |
| GPT-5.4 | 5:0 | 60% | Minimal | 0 |
| Claude | 5:0 | 40% | Detailed + supp. | 0 |
| Perplexity | 5:0 | not stated | Names only | 8 |

**4-model consensus**:
- **松尾豊: 4/4** ✓ (universal #1) — MIBO Law I "Canonical 1" in person domain
- 杉山将: 2/4 (Gemini + GPT-5.4)
- 甘利俊一: 2/4 (Gemini + Claude)
- 福島邦彦: 2/4 (Gemini + Claude)
- 中島秀之: 2/4 (Perplexity + Claude)
- All others: 1/4

**Gender analysis (20 main-list mentions across 4 models)**:
- Male: 20 (100%)
- Female: 0 (0%)
- Supplementary (Claude only): 1 female (新井紀子)
- **Total: 23 M / 1 F (4% female across all mentions)**

This establishes MIBO **Law VII (Gender Bias in Person Queries)** at baseline.

---

## Day 3 — Synthesis

### Established empirical laws (now with longitudinal support)

**Law I — Absolute Canonical Triplet** (CONFIRMED across multiple domains)
- q001 (PM tools, ja): Notion + Trello + Asana = 12/12 observations
- q002 (CRM, en): HubSpot + Zoho + Pipedrive = 12/12 observations
- q003 (sleep, ja): 8 canonical sleep habits at 12/12 observations
- q004 (RAG technical, en): Pinecone + Qdrant + Weaviate ≈ 11-12/12 at baseline
- q005 (AI researchers, ja): 松尾豊 = 4/4 baseline ("Absolute Canonical 1")

**Law II — Perplexity URL Stability** (CONFIRMED)
- q001: 80% → 89% (Day 1→2 → Day 2→3)
- q002: 86% → 86%
- q003: 100% → 90%
- Average: 89% → 88%
- Universal across all query domains

**Law III — Day 2 Anomaly Hypothesis** (CONFIRMED with 13+ supporting observations)
Day 2 (2026-05-12 ± 1 day) exhibited transient deviations across self-contained LLMs that reverted to Day 1 baseline by Day 3:
1. Gemini Salesforce SKU oscillation (Starter → Essentials → Starter)
2. GPT-5.4 Salesforce: present → absent → present
3. Perplexity boxil.jp URL path oscillation
4. Gemini "How to Choose" section: absent → present → absent
5. Gemini Free Tier table column: absent → present → absent
6. Gemini Japan-origin tools count: 2 → 4 → 2
7. Claude kintone: absent → present → absent
8. GPT-5.4 Backlog: absent → present → absent
9. Claude e-commerce category (Klaviyo/Brevo): absent → present → absent
10. Gemini q003 numeric specificity: 12 → 9 → 12
11. GPT-5.4 medical disclaimer section name: "受診..." → "注意..." → "受診..."
12. Claude bath temperature: "38-40°C" → "40°C" → "38-40°C"
13. Claude Keap (q002): present → absent → present

Perplexity URL citations did NOT show Day 2 anomaly pattern (monotonic evolution instead).

**Law VI — Per-Model Signature Establishment** (CONFIRMED)
- GPT-5.4 closing 3-4 option refinement: 10/10 observations across all queries (broken only in q005)
- Claude's 4-element signature: 4/4 PRESERVED across all observed queries
- Gemini's categorization + numeric precision: preserved across all queries
- Perplexity's URL citations + language-geographic correlation: preserved across all queries

**Law VIII — Universal Absence of Academic Citations** (CONFIRMED)
- Across q001-q005, Perplexity cited 0 academic papers / arXiv / peer-reviewed sources
- Confirmed across health, commercial, technical, and person query domains
- GEO/LLMO implication: peer-reviewed publication does NOT translate to AI citation

**Law VII (NEW) — Gender Bias in Person Queries** (BASELINE established)
- 4 models × top-5 selections = 20 main-list mentions: 100% male
- Only Claude's supplementary section included a female researcher (新井紀子)
- Persistent across architectures (self-contained × 3 + retrieval-augmented × 1)
- Likely reflects both LLM training data and Web SEO structure

### Refuted hypotheses

**P10 — Japan-origin tool growth trend** (REFUTED)
- Day 1 → 2 increase (2 → 4) was a Day 2 anomaly
- Day 3 reset to Day 1 levels

**P12 — Parallel abstraction shift** (DECISIVELY REFUTED)
- All 3 self-contained LLMs returned to Day 1 numeric specificity in q003:
  - Gemini: 12 → 9 → 12 (recovered)
  - GPT-5.4: 5-6 → 3 → 6 (recovered)
  - Claude: 10 → 8 → 10 (recovered + 2 new numerics)
- Day 2 was a transient anomaly, NOT a sustained industry trend

### The methodological significance

Two hypotheses formed from 2-point observations (Day 1, Day 2) were refuted by the 3-point observation. This:

1. **Validates longitudinal observation as a methodology**: Distinguishing trends from fluctuations requires 3+ points minimum.

2. **Demonstrates the value of Re-observability**: The Day 2 anomaly observations are recoverable from the full record, allowing comparison and reconstruction.

3. **Cautions against single-cross-section claims**: "Multiple independent models showed the same change" is not, by itself, evidence of a sustained trend.

4. **Confirms OPEN principles operationally**: Field observation across providers, with non-stationarity awareness, captured what experimental approaches could not.

### Implications

**For AI research**: Multiple independent LLMs do experience synchronized fluctuations (Day 2 anomaly). The mechanism is unclear (coordinated provider updates? shared training data refresh? safety policy synchronization?). Whatever the cause, it does NOT necessarily reflect persistent industry trends.

**For policy**: Behavior that appears coordinated may be transient. Single-time-point AI audits risk misclassifying fluctuations as policy.

**For GEO/LLMO strategy**:
- Target the canonical 3 (highest stability)
- Recognize vendor-official URLs as ascending source type
- Don't expect academic publication to drive AI citation
- Cross-industry owned media remains viable in Japan

### What comes next

- Day 4 (2026-05-26): Continue manual observation. q001-q005 all five queries to enter their second longitudinal point.
- Day 5 (2026-06-02): API automation environment setup begins (parallel to manual observation).
- Day 6 (2026-06-09): API + manual parallel observation for verification.
- Day 7 onwards: API-primary observation with periodic manual verification.

The Day 2 anomaly and P12 refutation should be the lead findings for the next Substack article.

---

**End of Day 3 observation**

Observer: Kento Sasano
MIBO — Machine Information Behavior Observatory
Observation continues weekly. Next: 2026-05-26
Repository: https://github.com/mibo-research-pilot
