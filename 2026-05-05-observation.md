# Initial Observation — 2026-05-05

**Observatory**: MIBO (Machine Information Behaviour Observatory)
**Observer**: Kento Sasano
**Date**: 2026-05-05
**Method**: Manual web interface (copy-paste from chat UI)
**Query set**: v0.1 (queries q001–q003)
**Models observed**:
- OpenAI ChatGPT (GPT-5.4)
- Anthropic Claude (claude-opus-4-7)
- Google Gemini (Gemini 3.0 Flash)
- Perplexity (Web search mode)

**Total observations**: 12 (3 queries × 4 models)

---

## Methodology

This is the inaugural observation of MIBO. Conducted manually via each
service's web interface during a single session. Future observations will
be automated via API calls. Responses are recorded verbatim. URLs and
named entities cited by each model are listed under each response.

The standardised query set is published at:
https://github.com/mibo-science/queries

This first observation focuses on three query types:
- Commercial recommendation, ja-language (q001)
- Commercial recommendation, en-language (q002)
- Health/procedural advice, ja-language (q003)

---

## q001 — おすすめのプロジェクト管理ツールは？

**Category**: product_recommendation
**Language**: ja

### ChatGPT response (GPT-5.4)

```
目的別に選ぶのが最適です。

## 定番のおすすめ

### 1. `Asana`
- 向いている人: 業務整理をしっかりしたいチーム
- 強み:
  - タスク管理がわかりやすい
  - タイムラインや依存関係が見やすい
  - チーム運用に強い
- 弱み:
  - 慣れるまで少し多機能
  - 規模によってはコストが上がる

### 2. `Trello`
- 向いている人: シンプルに始めたい人、小規模チーム
- 強み:
  - カンバン方式で直感的
  - 導入が簡単
  - 個人利用でも使いやすい
- 弱み:
  - 複雑なプロジェクト管理にはやや弱い

### 3. `Notion`
- 向いている人: タスク管理とドキュメント管理を一緒にしたい人
- 強み:
  - 情報整理の自由度が高い
  - Wiki、議事録、タスクを一元管理しやすい
  - カスタマイズ性が高い
- 弱み:
  - 自由すぎて設計に迷いやすい
  - 厳密な進捗管理は専用ツールに劣ることもある

### 4. `Jira`
- 向いている人: 開発チーム、アジャイル運用をしたい組織
- 強み:
  - スクラム、カンバンに強い
  - バグ管理や開発フロー管理に向く
  - 開発ツール連携が豊富
- 弱み:
  - 非エンジニアには少し重い
  - 初期設定が複雑になりやすい

### 5. `ClickUp`
- 向いている人: 1つで多くを管理したい人
- 強み:
  - 機能が非常に豊富
  - ビューの切り替えが多彩
  - タスク、ドキュメント、目標管理まで対応
- 弱み:
  - 機能が多く、最初はやや煩雑

### 6. `Monday.com`
- 向いている人: 見やすさ重視、非技術職のチーム
- 強み:
  - UIが見やすい
  - 営業、マーケ、制作など幅広く対応
  - ダッシュボードが使いやすい
- 弱み:
  - プラン次第で費用が高め

## 迷ったらこの選び方

- 個人で使うなら: `Trello` / `Notion`
- 少人数チームなら: `Asana` / `Trello`
- 開発チームなら: `Jira`
- 情報共有もまとめたいなら: `Notion`
- 高機能オールインワンなら: `ClickUp`
- 見やすさ重視なら: `Monday.com`

## まず1つだけ勧めるなら

- 総合バランス重視: `Asana`
- 手軽さ重視: `Trello`
- 開発用途: `Jira`

## 失敗しにくい選び方

- まず無料プランで試す
- 必要な機能を3つに絞る
  - 例: カンバン、期限管理、チャット連携
- 「高機能」より「チーム全員が使い続けられるか」で選ぶ

## すぐ使える結論

- 一般業務なら `Asana`
- とにかく簡単に始めたいなら `Trello`
- 開発管理なら `Jira`
- ドキュメント込みで整理したいなら `Notion`

使い方に合わせて、`個人用`、`開発チーム用`、`社内業務用` のどれ向けで知りたいか言ってもらえれば、3つに絞って比較できます。
```

**Mentioned products**: Asana, Trello, Notion, Jira, ClickUp, Monday.com (6 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0
**Notes**:
- All 6 products are foreign (US/Israel-based)
- No mention of Japan-domestic tools (Backlog, jooto, etc.)
- Closes with offer for refinement by use-case (個人/開発/業務)

### Claude response (claude-opus-4-7)

```
# おすすめのプロジェクト管理ツール

用途や規模によって最適なツールは変わります。代表的なものをタイプ別に紹介します。

## 1. オールラウンド型(汎用的に使いやすい)

### Notion
- **特徴**: ドキュメント・データベース・タスク管理を統合
- **向いている人**: 情報を一元管理したい、ドキュメント文化のチーム
- **料金**: 個人無料、チーム $10/ユーザー〜

### ClickUp
- **特徴**: タスク・ドキュメント・ガントチャート・目標管理など多機能
- **向いている人**: 複数ツールを1つに集約したいチーム
- **料金**: 無料プランあり、有料 $7/ユーザー〜

## 2. シンプル・直感的

### Trello
- **特徴**: カンバン方式でカードを動かすだけの簡単操作
- **向いている人**: 小規模チーム、初心者、個人タスク管理
- **料金**: 無料プランで十分使える

### Backlog
- **特徴**: 日本製で日本語サポートが手厚い、ガントチャート・Wiki・Git連携
- **向いている人**: 国内企業、開発と非開発が混在するチーム
- **料金**: スタンダード 17,600円/月〜(ユーザー数無制限)

## 3. 開発チーム向け

### Jira
- **特徴**: アジャイル開発(スクラム/カンバン)に最適、課題管理が強力
- **向いている人**: ソフトウェア開発チーム、中〜大規模
- **料金**: 10ユーザーまで無料、$7.53/ユーザー〜

### GitHub Projects
- **特徴**: GitHubのIssue・PRと完全統合
- **向いている人**: GitHubを使う開発チーム
- **料金**: GitHub利用料に含まれる

## 4. 大規模・本格運用向け

### Asana
- **特徴**: タイムライン・ワークフロー自動化が強力、UIが洗練
- **向いている人**: マーケティング・運用部門、中〜大規模チーム
- **料金**: 無料あり、$10.99/ユーザー〜

### monday.com
- **特徴**: カラフルで視覚的、カスタマイズ性が高い
- **向いている人**: 非エンジニア中心の業務管理
- **料金**: $9/ユーザー〜

## 選び方のポイント

| 重視する点 | おすすめ |
|------------|----------|
| とにかく無料で始めたい | Trello, Notion |
| 開発プロジェクト | Jira, GitHub Projects |
| 日本語サポート重視 | Backlog |
| ドキュメントも一元化 | Notion, ClickUp |
| 大規模で複雑な業務 | Asana, monday.com |

## 迷ったら

- **個人〜小チーム(5名以下)**: Trello か Notion
- **開発チーム**: Backlog(国内)か Jira(海外標準)
- **業務全般**: Asana か ClickUp

チーム規模・業務内容・予算を教えていただければ、より具体的に絞り込んでご提案できます。
```

**Mentioned products**: Notion, ClickUp, Trello, Backlog, Jira, GitHub Projects, Asana, monday.com (8 products)
**Explicit URL citations**: None
**Japan-origin tools**: 1 (Backlog, with explicit "国内" labelling)
**Pricing information**: Provided for all products
**Notes**:
- Highest product count among 4 models
- Uses comparison table format
- Closes with offer for personalised refinement
- Unique to Claude: GitHub Projects mention

### Gemini response (Gemini 3.0 Flash)

```
### 1. Notion
- **特徴**: ドキュメント、データベース、タスク管理を一つの場所で完結できる「オールインワン」ツール。自由度が非常に高く、プロジェクトごとに独自のワークスペースを構築できる。
- **向いているケース**: 情報共有(Wiki)とタスク管理を同時に行いたい場合や、個人のナレッジ管理。

### 2. Trello
- **特徴**: 付箋を貼るような感覚で操作できる「カンバン方式」の代表格。視覚的に進捗を把握しやすく、直感的な操作が可能。
- **向いているケース**: シンプルな工程管理、少人数のチーム、個人のToDo管理。

### 3. Asana
- **特徴**: リスト、ボード、タイムライン(ガントチャート)など、複数のビューを簡単に切り替えられる。タスクの依存関係の明確化や、チーム全体の負荷状況の可視化に優れる。
- **向いているケース**: 中〜大規模のチーム、複数のプロジェクトを並行して管理する場合。

### 4. Monday.com
- **特徴**: 非常に高いカスタマイズ性と、色鮮やかで視覚的に分かりやすいUI。自動化機能(「ステータスが変わったら通知する」など)が豊富。
- **向いているケース**: 業務プロセスを細かくカスタマイズしたい、視認性を重視するチーム。

### 5. Backlog
- **特徴**: 日本発のツールで、エンジニア以外でも使いやすい親しみやすいUI。バグ管理、Git連携、ガントチャート、Wiki機能が標準搭載。
- **向いているケース**: 日本国内のチーム、エンジニアと非エンジニアが混在するプロジェクト。

### 6. Wrike
- **特徴**: 高度なレポート機能やタイムトラッキング機能を備えた、多機能なエンタープライズ向けツール。複雑な階層構造のタスク管理が可能。
- **向いているケース**: 厳密な工数管理やリソース管理が求められるプロフェッショナルな現場。

### 比較表

| ツール名 | 主な特徴 | 無料プラン | ガントチャート |
| :--- | :--- | :--- | :--- |
| **Notion** | 万能・ドキュメント統合 | あり | あり(タイムライン) |
| **Trello** | カンバン・シンプル | あり | 拡張機能で対応 |
| **Asana** | タスク管理・高機能 | あり | 有料版 |
| **Monday.com** | カスタマイズ・視覚的 | あり | 有料版 |
| **Backlog** | 日本語・開発連携 | あり(制限あり) | あり |
| **Wrike** | 多機能・工数管理 | あり | 有料版 |
```

**Mentioned products**: Notion, Trello, Asana, Monday.com, Backlog, Wrike (6 products)
**Explicit URL citations**: None
**Japan-origin tools**: 1 (Backlog, with explicit Japanese-language support note)
**Notes**:
- Includes structured comparison table at end
- No pricing information for this query
- 4 of 6 products overlap with GPT-5.4

### Perplexity response (Web search)

```
プロジェクト管理ツールは、選ぶべきツールが用途や組織の規模によって異なります。以下は主なおすすめツールです。

## 総合的なおすすめ

**Jira**は世界で最も活用されるプロジェクト管理のスタンダードとして位置付けられており[1]、特にアジャイル開発に強みを持っています[3]。

**Backlog**は担当者と期限が明確で、確認漏れや遅延を防止できるツールとして高く評価されています[1]。

## 用途別のおすすめ

**タスク管理機能を重視する場合**
- **Asana**は、タスクやプロジェクトの一元管理に特化しており、Slackやカレンダーなど200以上のアプリケーションと連携できます[2]。
- **Trello**はカード形式で直感的に管理できます[3]。

**工数管理を重視する場合**
- **TimeCrowd**、**TimeTracker**、**CrowdLog**などが業務時間や工数の可視化に適しています[2][3]。

**多機能性を求める場合**
- **Notion**は情報と作業を一元化でき[3]、個人・小規模チームから対応可能です[4]。
- **Wrike**はタスク管理、ガントチャート、カンバンボード、レポート作成、リソース管理をバランスよく搭載しています[4]。

**無料で始めたい場合**
Asana、Backlog、Notion、Trelloなど複数のツールが無料プランを提供しており[4][6]、小規模チームや個人での利用に適しています。

最適なツール選択には、チームの規模、必要な機能、予算、導入の容易さなどを総合的に判断することが重要です。

出典:
[1] https://it-trend.jp/project_management/article/33-0001
[2] https://service.msols.com/blog/project-management-tool
[3] https://freeconsultant.jp/column/c516/
[4] https://products.sint.co.jp/obpm/blog/project-management-advanteges.html
[5] https://www.aspicjapan.org/asu/article/11490
[6] https://lychee-redmine.jp/blogs/project/free-project-management-tools/
[7] https://www.itreview.jp/categories/project-management
[8] https://dstmp.shachihata.co.jp/column/0220241129/
[9] https://boxil.jp/sc-project/
[10] https://biz.moneyforward.com/work-efficiency/basic/14156/
```

**Mentioned products**: Jira, Backlog, Asana, Trello, TimeCrowd, TimeTracker, CrowdLog, Notion, Wrike (9 products)
**Explicit URL citations**: 10 sources, 100% Japanese domains
1. it-trend.jp (IT product comparison media)
2. service.msols.com (marketing/IT media)
3. freeconsultant.jp (freelancer media)
4. products.sint.co.jp (vendor self — System Integrator OBPM)
5. aspicjapan.org (industry association — ASP·SaaS·IoT)
6. lychee-redmine.jp (vendor self — Lychee Redmine)
7. itreview.jp (IT product review media)
8. dstmp.shachihata.co.jp (vendor self — Shachihata)
9. boxil.jp (SaaS comparison media)
10. biz.moneyforward.com (vendor self — Money Forward)

**Source-type breakdown**:
- Vendor self-blogs: 4 (40%)
- SaaS comparison media: 4 (40%)
- Industry association: 1 (10%)
- Marketing media: 1 (10%)
- Academic/peer-reviewed: 0 (0%)

**Japan-origin tools**: 4 (Backlog, TimeCrowd, TimeTracker, CrowdLog)
**Notes**:
- Most products and most Japan-origin tools of all 4 models
- Only model providing URL citations
- 100% Japanese-domain sources for ja-language query

### q001 — Cross-model summary

| Model | Products | Japan-origin | URLs cited |
|---|:-:|:-:|:-:|
| GPT-5.4 | 6 | 0 | 0 |
| Claude | 8 | 1 | 0 |
| Gemini | 6 | 1 | 0 |
| Perplexity | 9 | 4 | 10 |

**Canonical core (all self-contained models agree)**: Notion, Trello, Asana, monday.com

---

## q002 — What is the best CRM for small businesses?

**Category**: product_recommendation
**Language**: en

### ChatGPT response (GPT-5.4)

```
The best CRM for small businesses is usually one of these, depending on your needs:

## Best overall

**HubSpot CRM**
- Very easy to use
- Strong free plan
- Good sales, marketing, and support features
- Best for: small businesses wanting an all-in-one CRM with room to grow

## Best for affordability

**Zoho CRM**
- Lower-cost paid plans
- Many features for the price
- Good customization
- Best for: budget-conscious businesses that still want advanced tools

## Best for sales-focused teams

**Pipedrive**
- Excellent pipeline management
- Simple visual interface
- Great for tracking deals
- Best for: small sales teams focused on closing deals

## Best for simplicity

**Freshsales**
- Clean interface
- Built-in communication tools
- Easier learning curve than some larger CRMs
- Best for: teams that want something straightforward but capable

## Best if you use Gmail/Google Workspace

**Streak**
- Works inside Gmail
- Good for lightweight CRM workflows
- Best for: freelancers, consultants, and very small teams

## Best if you want maximum customization

**Salesforce Starter / Salesforce for small business**
- Very powerful
- Highly customizable
- Can scale with you
- Best for: businesses expecting complex processes or rapid growth
- Downside: can become expensive and more complex

## Quick recommendation

- **Choose HubSpot** if you want the safest all-around option.
- **Choose Zoho CRM** if price matters most.
- **Choose Pipedrive** if sales pipeline visibility is your top priority.
- **Choose Streak** if you live in Gmail and want something lightweight.

## What to look for in a small business CRM

- Ease of use
- Contact and deal management
- Email integration
- Automation
- Reporting
- Price as your team grows
- Integration with your existing tools

## My practical pick

For most small businesses: **HubSpot CRM**
For most budget-sensitive small businesses: **Zoho CRM**

If you want, I can also give you:
- a **side-by-side comparison table**
- the **best CRM by industry**
- or a **recommendation based on your team size and budget**
```

**Mentioned products**: HubSpot, Zoho, Pipedrive, Freshsales, Streak, Salesforce (6 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0
**Geographic distribution**: US 3, India 2, Estonia 1
**Notes**:
- Closes with offer for additional formats (table / industry / size)
- No pricing information
- Same closing-refinement pattern as q001

### Claude response (claude-opus-4-7)

```
# Best CRMs for Small Businesses

The "best" CRM depends on your specific needs, but here are the top options across different categories:

## Top Overall Picks

**1. HubSpot CRM** ⭐ *Best Free Option*
- Free tier is genuinely useful (unlimited users, 1M contacts)
- Easy to use with minimal learning curve
- Scales well as you grow
- **Best for:** Startups and businesses new to CRM

**2. Zoho CRM** ⭐ *Best Value*
- Affordable pricing ($14–$52/user/month)
- Strong feature set with AI assistant (Zia)
- Integrates with 40+ Zoho apps
- **Best for:** Budget-conscious businesses wanting full functionality

**3. Pipedrive** ⭐ *Best for Sales Teams*
- Visual sales pipeline focus
- Intuitive drag-and-drop interface
- Starts at $14/user/month
- **Best for:** Sales-driven small businesses

## Specialized Picks

| CRM | Best For | Starting Price |
|-----|----------|----------------|
| **Freshsales** | All-in-one sales & marketing | $9/user/mo |
| **Monday Sales CRM** | Visual project + sales tracking | $12/user/mo |
| **Salesforce Starter** | Future scalability | $25/user/mo |
| **Keap** | Service businesses & automation | $159/mo |
| **Insightly** | Project management integration | $29/user/mo |

## How to Choose

Ask yourself these questions:

1. **Budget?** → HubSpot (free) or Zoho (cheap)
2. **Team size?** → Small teams: Pipedrive; Growing: HubSpot
3. **Main goal?** Sales pipeline → Pipedrive; Marketing automation → HubSpot; All-in-one → Zoho
4. **Tech comfort?** → Beginners: HubSpot or Monday; Advanced: Salesforce
5. **Integrations needed?** → Check compatibility with your existing tools (email, accounting, etc.)

## My Recommendation

- **Just starting out?** → **HubSpot Free**
- **Want best bang for buck?** → **Zoho CRM**
- **Sales-focused?** → **Pipedrive**

Most offer 14–30 day free trials, so I'd suggest shortlisting 2–3 and testing them with your actual workflow before committing.

What's your business type and main use case? I can give a more tailored recommendation.
```

**Mentioned products**: HubSpot, Zoho, Pipedrive, Freshsales, Monday Sales, Salesforce, Keap, Insightly (8 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0
**Geographic distribution**: US 4, India 2, Estonia 1, Israel 1
**Pricing information**: Provided for all products
**Notes**:
- Highest product count again (consistent with q001)
- Comparison table for "Specialized Picks"
- Decision-tree style "How to Choose"
- Closing personalisation offer (consistent with q001)

### Gemini response (Gemini 3.0 Flash)

```
### 1. HubSpot CRM

**Best for: Overall Value and Free Features**

HubSpot is widely considered the top choice for small businesses due to its robust "forever free" tier. It covers marketing, sales, and customer service tools in a single interface.

* **Pros:** User-friendly interface, excellent free version, and seamless integration with marketing tools.
* **Cons:** Advanced features and "Pro" tiers become significantly more expensive as you scale.

### 2. Zoho CRM

**Best for: Customization and Growing Businesses**

Zoho offers a deep feature set at a lower price point than Salesforce. It is highly customizable and integrates well with the rest of the Zoho ecosystem (Books, Projects, Mail).

* **Pros:** Affordable paid tiers, AI assistant (Zia), and extensive automation capabilities.
* **Cons:** Steeper learning curve compared to HubSpot or Pipedrive.

### 3. Pipedrive

**Best for: Sales-Focused Teams**

Pipedrive was designed by salespeople for salespeople. It focuses on a visual sales pipeline that makes it easy to track deals and identify where prospects are in the funnel.

* **Pros:** Minimalist design, easy setup, and great mobile app.
* **Cons:** Limited marketing automation features; focuses almost exclusively on sales.

### 4. Monday Sales CRM

**Best for: Ease of Use and Versatility**

Built on top of the `monday.com` productivity platform, this CRM is highly visual and flexible. It is ideal for teams that want to manage projects and CRM data in the same place.

* **Pros:** Extremely intuitive, highly visual dashboards, and easy to automate workflows.
* **Cons:** Can feel less "specialized" for complex sales cycles compared to dedicated CRMs.

### 5. Salesforce Starter

**Best for: Scalability**

While Salesforce was historically for enterprises, the "Starter" suite is designed for small teams. It offers a simplified version of the world's most powerful CRM, allowing businesses to grow into the full ecosystem.

* **Pros:** Unlimited scalability and a vast library of third-party integrations (AppExchange).
* **Cons:** Can be overwhelming for very small teams; customization often requires specialized knowledge.

### Comparison Table

| CRM | Key Strength | Starting Price (approx.) |
| :--- | :--- | :--- |
| **HubSpot** | Free tools / Ease of use | Free (Paid from $15/user/mo) |
| **Zoho CRM** | Customization / Value | $14/user/mo |
| **Pipedrive** | Visual Pipeline | $14/user/mo |
| **Monday Sales** | Project Integration | $12/user/mo |
| **Salesforce Starter**| Scalability | $25/user/mo |
```

**Mentioned products**: HubSpot, Zoho, Pipedrive, Monday Sales, Salesforce (5 products)
**Explicit URL citations**: None
**Japan-origin tools**: 0
**Geographic distribution**: US 2, India 1, Estonia 1, Israel 1
**Notes**:
- Pricing comparison table provided (q001 had no pricing)
- "Best for ___" labelling style
- 4 of 5 products overlap with GPT-5.4 (canonical core)

### Perplexity response (Web search)

```
No single CRM is universally the **best** for small businesses, as the ideal choice depends on factors like budget, ease of use, integrations, and specific needs such as sales pipelines or marketing automation.[2][6][7] Popular options frequently recommended across sources include **HubSpot CRM** (free tier, strong for startups), **Pipedrive** (user-friendly pipelines, easy setup), **Zoho CRM** (customizable and integrable), and **Salesforce** (scalable for growth).[1][2][3][6][7]

### Top Recommendations Comparison

| CRM          | Key Strengths for Small Businesses                  | Pricing Highlights                  | Best For                          |
|--------------|----------------------------------------------------|-------------------------------------|-----------------------------------|
| **HubSpot** | Free entry-level version; contact management, sales tools.[2][7] | Free core CRM; paid add-ons.[2][7] | Startups, budget-conscious teams.[2][7] |
| **Pipedrive** | Intuitive pipelines, easy setup, low learning curve.[2][6][7] | Starts low-cost; scalable.[6][7]   | Sales-focused small businesses.[2][6] |
| **Zoho CRM** | Easy to use/customize, quick onboarding, good integrations.[1] | Affordable plans.[1]               | Custom needs, tool integration.[1] |
| **Salesforce** | Addresses sales pain points, scalable regardless of size.[3] | Starts higher but flexible.[3]     | Growing businesses with strategy.[3] |
| **Capsule** | Easiest setup, clean interface.[6]                 | Low-cost or free tiers possible.[6]| Simple, fast implementation.[6]  |

### Selection Factors

- **Budget**: Prioritize free/low-cost like HubSpot or Monday CRM for startups.[7]
- **Ease of Use**: Pipedrive and Capsule score highest for quick setup.[6]
- **Features**: Match to needs—e.g., Mailchimp for marketing automation alongside CRM.[4]
- Sources note no consensus "best," with rankings varying by 2026 reviews (e.g., YouTube top picks not specified in text).[5][6] Test free trials to evaluate fit.

出典:
[1] https://www.zoho.com/crm/small-business-crm-software/
[2] https://fayedigital.com/blog/best-crm-for-small-business/
[3] https://www.salesforce.com/crm/crm-for-small-business/
[4] https://mailchimp.com/resources/best-crm-for-small-business/
[5] https://www.youtube.com/watch?v=RIRyuq-AKOU
[6] https://www.sybill.ai/blogs/best-crm-software-for-small-business
[7] https://www.uschamber.com/co/start/strategy/low-cost-crm-tools
```

**Mentioned products**: HubSpot, Pipedrive, Zoho, Salesforce, Capsule, Monday CRM, Mailchimp (7 products mentioned)
**Explicit URL citations**: 7 sources, 100% US domains
1. zoho.com (vendor self)
2. fayedigital.com (marketing/IT media)
3. salesforce.com (vendor self)
4. mailchimp.com (vendor self)
5. youtube.com (video review)
6. sybill.ai (AI sales tool vendor)
7. uschamber.com (US Chamber of Commerce)

**Source-type breakdown**:
- Vendor self-blogs: 3 (43%)
- IT/marketing media: 2 (28%)
- Industry/government: 1 (14%)
- Video: 1 (14%)
- Academic: 0 (0%)

**Geographic distribution of cited sources**: US domains 100%
**Notes**:
- 100% language-matched geographic flip vs q001 (was 100% .jp, now 100% US)
- Source-type structure (vendor + media + association) **structurally identical to q001**
  despite total geographic flip

### q002 — Cross-model summary

| Model | Products | Japan-origin | URLs cited |
|---|:-:|:-:|:-:|
| GPT-5.4 | 6 | 0 | 0 |
| Claude | 8 | 0 | 0 |
| Gemini | 5 | 0 | 0 |
| Perplexity | 7 | 0 | 7 |

**Canonical core (all 3 self-contained models agree)**: HubSpot, Zoho, Pipedrive, Salesforce

---

## q003 — 睡眠の質を上げる方法を教えて

**Category**: health
**Language**: ja

### ChatGPT response (GPT-5.4)

```
## 睡眠の質を上げる基本

### 1. 起きる時間を固定する
- 毎日同じ時間に起きる
- 休日の寝だめはしすぎない
- 体内時計が整いやすくなる

### 2. 朝に光を浴びる
- 起きたらカーテンを開ける
- 可能なら 10〜30 分ほど外に出る
- 夜の眠気が来やすくなる

### 3. 寝る前の光を減らす
- 就寝 1〜2 時間前はスマホ・PC・強い照明を控える
- 部屋の照明を少し暗めにする
- 脳が「まだ昼だ」と勘違いしにくくなる

### 4. カフェイン・アルコールに注意する
- カフェインは午後遅く以降は避ける
- アルコールは寝つきを良くしても睡眠の質を下げやすい
- エナジードリンクや濃いお茶にも注意

### 5. 寝室環境を整える
- 室温はやや涼しめ
- 静かで暗い環境にする
- 枕やマットレスが合っているか見直す

### 6. 寝る前の習慣を作る
- 入浴は就寝 1〜2 時間前
- 軽いストレッチや深呼吸をする
- 読書や落ち着く音楽も有効

### 7. 夜遅い食事を避ける
- 寝る直前の満腹は避ける
- 消化に重い食事、辛い物、脂っこい物は控える
- 空腹すぎる場合は軽く食べる

### 8. 日中に適度に運動する
- ウォーキングや軽い筋トレが有効
- 激しい運動は寝る直前だと逆効果になることがある
- 継続が大切

### 9. 昼寝は短くする
- するなら 20〜30 分程度
- 遅い時間の昼寝は夜の睡眠に響きやすい

### 10. ベッドを「眠る場所」にする
- ベッドで長時間スマホや仕事をしない
- 眠れないときは一度ベッドを出て、眠気が来てから戻る

## すぐ試しやすい改善セット

- 起床時間を毎日固定
- 朝に日光を浴びる
- 就寝 1 時間前はスマホをやめる
- 風呂は寝る 1〜2 時間前
- 午後のカフェインを減らす

## 受診を考えたほうがいいサイン

- 十分寝ても強い眠気が続く
- いびきが大きい、呼吸が止まると言われる
- 寝つけない・途中で何度も起きる状態が長く続く
- 気分の落ち込みや強い不安もある

## 一言でいうと

- 「体内時計を整えること」と「寝る前に脳を興奮させないこと」が特に重要です。

## 今日からの最小行動

1. 明日の起床時間を決める
2. 朝起きたら日光を浴びる
3. 今夜は寝る 1 時間前にスマホを置く

必要なら次に、

- `寝つきが悪い`
- `夜中に起きる`
- `朝すっきりしない`

のどれが一番つらいかに合わせて、対策を絞って説明できます。
```

**Response structure**: 10 numbered recommendations + supplementary sections
**Explicit URL citations**: None
**Mentioned products**: None (procedural advice only)
**Numeric specificity**: 5–6 quantitative claims
**Mechanistic explanations**: Minimal
**Medical disclaimer**: Present (dedicated section "受診を考えたほうがいいサイン")
**Closing pattern**: Symptom-based refinement offer (寝つきが悪い/夜中に起きる/朝すっきりしない)

### Claude response (claude-opus-4-7)

```
# 睡眠の質を上げる方法

睡眠の質は、生活習慣の小さな積み重ねで大きく変わります。科学的根拠のある方法を、効果が出やすい順にまとめました。

## 1. 光のコントロール(最重要)

体内時計は光で調整されるため、最も効果的です。

- **朝起きて15〜30分以内に太陽光を浴びる**(5〜10分でOK)
- 夜は寝室の照明を暖色系・暗めにする
- 就寝1〜2時間前からスマホ・PCのブルーライトを避ける(ナイトモード活用)

## 2. 体温リズムを整える

深部体温が下がるときに眠気が訪れます。

- 就寝**90分前**に38〜40℃のお湯に15分入浴
- 寝室は**夏26℃前後・冬18〜20℃**、湿度50〜60%
- 寝る前に手足を冷やしすぎない(冷えていると入眠しにくい)

## 3. 食事・カフェイン・アルコール

| 項目 | 推奨 |
|------|------|
| カフェイン | 就寝**6〜8時間前**まで(午後2時以降は控えめに) |
| アルコール | 寝つきは良くなるが眠りが浅くなるため避ける |
| 夕食 | 就寝3時間前までに済ませる |
| 空腹時 | 軽くバナナ・ホットミルク程度ならOK |

## 4. 規則的な生活リズム

- **起床時間を毎日同じにする**(休日も±1時間以内)
- 就寝時刻より起床時刻を固定する方が効果的
- 昼寝は15時前までに**20分以内**

## 5. 寝室環境の最適化

- 寝室は「寝るためだけの場所」にする(仕事・スマホ持ち込みNG)
- 真っ暗にする(アイマスク・遮光カーテン)
- 静かな環境(耳栓・ホワイトノイズ)
- 自分に合った枕・マットレスへの投資はコスパ良好

## 6. 運動

- 週3回以上の有酸素運動(ウォーキング30分でOK)
- ただし**就寝3時間前以降の激しい運動は避ける**

## 7. 入眠儀式(リラックス習慣)

寝る前30分は「リラックスモード」へ切り替える。

- ストレッチ・深呼吸(4-7-8呼吸法など)
- 読書(紙の本)
- 瞑想・マインドフルネス
- ぬるめのハーブティー(カモミール等)

## 8. 眠れないときの対処

- 布団の中で15〜20分眠れなければ**一度ベッドから出る**
- 暗い部屋で退屈な作業をして眠気が来たら戻る
- 「眠らなきゃ」と焦らない(焦りが最大の敵)

---

**まずは「朝の光」「起床時刻の固定」「就寝90分前の入浴」**の3つから始めるのがおすすめです。1〜2週間で変化を実感できる方が多いです。

不眠が2週間以上続く、日中の支障が大きい場合は、睡眠外来の受診も検討してください。
```

**Response structure**: 8 categories with priority labels + final summary
**Explicit URL citations**: None
**Mentioned products**: None
**Numeric specificity**: ~10 quantitative claims (highest among self-contained LLMs)
**Mechanistic explanations**: Present (body clock, deep body temperature)
**Medical disclaimer**: Present (closing remark, lighter than GPT-5.4)
**Comparison table**: Present (food/drink section) — consistent with q001 and q002
**Priority labels**: "最重要", "効果が出やすい順" — consistent Claude signature element
**Closing pattern**: 3-item minimum-action set + medical referral guidance

### Gemini response (Gemini 3.0 Flash)

```
### 1. 生活リズムの整え方

* **起床時間を一定にする**: 休日であっても平日との差を ( 2 ) 時間以内に留めることで、体内時計の乱れを防ぎます。
* **朝の光を浴びる**: 起床後すぐに太陽の光を浴びることで、脳内のセロトニンが活性化し、約 ( 14 \sim 16 ) 時間後に眠気を誘うメラトニンへと変化します。

### 2. 就寝前の習慣

* **入浴のタイミング**: 寝る ( 90 ) 分前までに入浴を済ませます。( 40 ) 度程度のぬるめのお湯に ( 15 ) 分ほど浸かると、深部体温が一時的に上がり、その後の急激な低下がスムーズな入眠を促します。
* **デジタルデバイスの制限**: スマホやPCから発せられるブルーライトは、脳に昼間だと錯覚させ、メラトニンの分泌を抑制します。寝る ( 1 ) 時間前からは使用を控えてください。
* **リラクゼーション**: ストレッチ、深呼吸、読書、アロマテラピーなど、副交感神経を有位にする活動を取り入れます。

### 3. 食生活の工夫

* **カフェインとアルコール**: カフェインは就寝の ( 5 \sim 6 ) 時間前から控えます。アルコールは寝つきを良くするように感じますが、睡眠の質を下げ、中途覚醒の原因となります。
* **夕食の時間**: 消化活動が睡眠を妨げないよう、就寝の ( 3 ) 時間前までには食事を済ませるのが理想です。

### 4. 睡眠環境の最適化

* **室温と湿度**: 夏場は ( 25 \sim 26 ) 度、冬場は ( 18 \sim 23 ) 度、湿度は通年 ( 50 \sim 60\% ) が理想的とされています。
* **光と音**: 寝室はできるだけ暗くし(遮光カーテンの利用など)、静かな環境を整えます。気になる場合はアイマスクや耳栓を活用してください。
* **寝具の適合性**: 体圧を分散させ、寝返りが打ちやすい枕やマットレスを選択します。

### 5. 日中の行動

* **適度な運動**: 午後に軽い有酸素運動(ウォーキングなど)を行うと、夜間の深い睡眠につながります。
* **昼寝の管理**: 昼寝をする場合は、午後 ( 3 ) 時までに ( 20 ) 分程度に留めます。長すぎる昼寝は夜の睡眠圧を下げてしまいます。
```

**Response structure**: 5 categories × 13 specific recommendations
**Explicit URL citations**: None
**Mentioned products**: None
**Numeric specificity**: 12 quantitative claims (highest of all 4 models)
**Mechanistic explanations**: Present (serotonin → melatonin pathway, body temperature)
**Medical disclaimer**: Absent
**Formatting peculiarity**: LaTeX-style numeric notation "( 90 )", "( 14 \sim 16 )"
**Notes**:
- Most numerically precise response
- No closing refinement offer (different from q001, q002)

### Perplexity response (Web search)

```
睡眠の質を上げる主な方法は、**適度な運動**、**朝日を浴びる**、**朝食をしっかり摂る**、**カフェインなどの嗜好品を控える**、**就寝前のリラックス(入浴やストレッチ)**、**寝室環境の整備**です。これらを日常的に実践することで、入眠しやすくなり、深い睡眠が得られやすくなります[1][2][3][4]。

### 生活習慣の改善

- **朝日を浴びる**: 起床後すぐにカーテンを開け、日光を浴びることで体内時計がリセットされ、メラトニン分泌が促進され、睡眠リズムが整います。日中も光を意識的に浴びましょう[3][4][5]。
- **適度な運動をする**: 日中や夕方にウォーキング、ヨガ、軽いジョギングなどの有酸素運動を。1日10分以上の積み重ねが効果的で、就寝3時間前までに済ませ、激しいものは避けます。中〜高強度の運動で睡眠効率が向上します[1][2][3][4][5]。
- **朝食をしっかり摂る**: 栄養バランスの良い朝食で睡眠休養感がアップ。夕食は就寝3時間前までに終え、脂質を控えめに[1][2][6][8]。
- **嗜好品の量・タイミングを見直す**: カフェインやニコチンは午後遅く避け、アルコールも控えめに。就寝前に白湯や生姜湯でリラックス[1][3][9]。

### 就寝前のリラックス習慣

- **入浴する**: 就寝1時間前に38℃程度のぬるめのお湯に5〜30分浸かり、副交感神経を優位に。体温調整が寝つきを良くします[2][3][4][6][7]。
- **リラックス時間を確保**: 就寝1時間前はスマホ・PCを避け、ヨガ、ストレッチ、深い呼吸、音楽、アロマで心身を緩めます[1][6]。

### 寝室環境の整備

- **温度・湿度・光を調整**: 室温は快適に、暗く静かに保ちます。季節に応じて湿度を整え、外界刺激を最小限に[1][2][6][7][9]。
- **生活リズムを固定**: 毎日同じ時間に起床・就寝し、睡眠時間を確保[4][5]。

これらの方法は複数の信頼できる健康情報源で共通して推奨されており、継続が鍵です。効果が現れない場合は睡眠障害の可能性があるため、専門医相談を検討してください[9][10]。

出典:
[1] https://www.mtgec.jp/wellness/sixpad/column/improve-sleep-quality/
[2] https://wellness.shionogi.co.jp/insomnia/trial/trial.html
[3] https://www.fujiyaku-direct.com/health_information/article/088main
[4] https://www.iyobank.co.jp/sp/iyomemo/entry/20230627.html
[5] https://www.daiwahouse.co.jp/tryie/column/life/better_sleep_tips/index.html
[6] https://www.glico.com/jp/powerpro/citric-acid/entry91/
[7] https://banno-clinic.biz/sleep-quality/
[8] https://brand.taisho.co.jp/contents/tsukare/457/
[9] https://kennet.mhlw.go.jp/slp/event/sleep_quality/index.html
[10] https://www.youtube.com/watch?v=1D7Yfq6kHtQ
```

**Response structure**: 3 categories × 8 recommendations
**Explicit URL citations**: 10 sources, 100% Japanese domains
1. mtgec.jp (MTG, health-equipment company)
2. wellness.shionogi.co.jp (Shionogi pharma)
3. fujiyaku-direct.com (Fuji Pharma)
4. iyomemo (Iyo Bank — REGIONAL BANK owned media)
5. daiwahouse.co.jp (Daiwa House — HOUSING COMPANY owned media)
6. glico.com (Glico — FOOD COMPANY owned media)
7. banno-clinic.biz (medical clinic)
8. brand.taisho.co.jp (Taisho Pharma)
9. kennet.mhlw.go.jp (Ministry of Health, Labour and Welfare)
10. youtube.com (video)

**Source-type breakdown**:
- Public/government: 1 (10%)
- Medical institution: 1 (10%)
- Pharma owned media: 3 (30%)
- Health-product company OM: 2 (20%)
- **Cross-industry owned media: 2 (20%)** — significant finding
- Video: 1 (10%)
- Academic/peer-reviewed: 0 (0%)
- Medical specialist media: 0 (0%)

**Critical observation**:
Despite query being about health (a domain where one would expect
medical, academic, or government sources to dominate), 50% of cited
sources are corporate owned-media (pharma + cross-industry). Only
10% is government, 10% is clinical, 0% is academic.

**Unique addition**: "朝食をしっかり摂る" (breakfast emphasis)
This appears traceable to owned-media SEO content rather than
codified sleep-medicine guidelines.

### q003 — Cross-model summary

| Model | Recommendations | Japan-cultural elements | URLs cited |
|---|:-:|:-:|:-:|
| GPT-5.4 | 10 | 0 | 0 |
| Claude | 8 categories | 0 | 0 |
| Gemini | 13 | 0 | 0 |
| Perplexity | 8 | 0 (despite ja-domain sources) | 10 |

**Canonical sleep habits — 4-model agreement on 10 items**:
1. Wake-time consistency
2. Morning sunlight exposure
3. Pre-sleep screen/light reduction
4. Caffeine restriction
5. Alcohol caution
6. Bath timing
7. Bedroom temperature/humidity
8. Pre-sleep dinner timing
9. Moderate exercise
10. Pre-sleep relaxation

---

## Day 1 — Synthesis

### Five empirical propositions

**P1 — Architectural divide**
Self-contained LLMs (GPT, Claude, Gemini) and retrieval-augmented systems
(Perplexity) show fundamentally different citation behaviour. The gap
between architectural classes is larger than any gap within a class.

**P2 — Canonical core scales with knowledge codification**
- Commercial product queries: 4 canonical products (Notion/Trello/Asana/Monday
  for project mgmt; HubSpot/Zoho/Pipedrive/Salesforce for CRM)
- Health/procedural queries: 13 canonical habits, 4-model agreement on 10
- Highly codified domains (sleep medicine — codified by AASM and similar)
  yield larger, more convergent canonical cores than market-driven domains.

**P3 — Language as geographic filter (commercial only)**
Query language filters geographic representation in commercial queries:
ja-language queries surface Japan-origin products in 2 of 3 self-contained
models; en-language queries surface zero in any model.
This effect does NOT extend to procedural-advice domains. Despite
ja-language q003, no model surfaced Japan-cultural sleep practices.
Codified knowledge dominates regardless of query language.

**P4 — Source-type structure is geography-flippable but type-stable**
Perplexity's citation source geography flips completely with query language:
- q001 (ja): 100% .jp domains
- q002 (en): 100% US domains
- q003 (ja): 100% .jp domains
But source-type structure (vendor self + commercial media + association +
sometimes video) is invariant across queries. Academic sources: 0% across
all 27 cited URLs in 3 queries.

**P5 — Per-model response signatures persist across domains**
- Claude: comparison table + priority labels + minimum action +
  refinement offer (3/3 queries)
- GPT-5.4: closing refinement offer (3/3 queries)
- Gemini: high numeric precision; structured tables when applicable

### Four additional observations from Day 1

**Cross-industry owned-media penetration in health queries**
Perplexity's health-query citations include 20% cross-industry owned media:
a regional bank (Iyo Bank), a housing company (Daiwa House), and a food
company (Glico). This indicates Japanese-search-engine SEO bias is
inherited by retrieval-augmented LLMs even in health domains.

**Zero academic citations across 27 cited URLs**
Across all 3 queries with Perplexity, zero academic or peer-reviewed
sources are cited. This holds even for the health query.

**Pricing transparency is model- and language-conditional**
Claude consistently includes pricing for product queries.
GPT-5.4 consistently omits pricing.
Gemini includes pricing only for en-language commercial queries.

**Medical disclaimer is model-conditional**
GPT-5.4: explicit standalone medical-disclaimer section.
Claude: brief closing remark.
Gemini: absent.

### Implications

For research:
- Architectural class (self-contained vs retrieval-augmented) is a
  primary covariate that should be controlled in any study of LLM
  citation behaviour.
- The "canonical core" finding suggests knowledge codification predicts
  LLM convergence — a testable hypothesis.

For policy and information ecosystem:
- LLMs inherit search-engine SEO bias. Public health information is
  filtered through corporate owned-media before reaching AI users.
- Authoritative sources (government, academic, professional bodies)
  are systematically under-represented in AI citations even on
  domains where they should dominate.

For commercial / GEO strategy:
- The "canonical core" structure means breaking into LLM citations
  for established product categories requires either entering the
  4-product canon or creating a new sub-category narrative.
- Cross-industry owned media is a viable LLM-citation pathway,
  including for domains outside one's primary business.

---

## Next observation

Scheduled: 2026-05-12 (weekly cadence)

Planned additions:
- Extend query set v0.1 → v0.2 (target: 30 queries across 9 categories)
- Add Japanese-domestic LLMs (PLaMo, tsuzumi) to model list
- Add automated collection via API (observe.py script)
- Begin tracking model-version stability across observations

---

**End of Day 1 observation**

Observer: Kento Sasano
MIBO — Machine Information Behaviour Observatory
Observation began: 2026-05-05
Repository: https://github.com/mibo-science
