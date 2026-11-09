# 成稿包：The X Subscription（写作单 #001-A）

> 核对日期：2026-11-10（Asia/Shanghai，UTC+8）  
> 口径：据官方资料整理；无实测口吻。  
> 交付形态：推送包（可直接发表正文 + 配图需求 + 来源清单）

---

## 1. 标题备选（3 个）

1. **【建议主标题】一个订阅打通 Grok、干活 Bot 和写代码：X Subscription 怎么算账**
2. Premium 从「约 $90 三件套」收到 $30？五档价目与老用户退款路径
3. Grok + Cursor + X 合订了：共享用量池、按比例退款、你该不该切

---

## 2. 作者

刀哥

---

## 3. 一句摘要

据 xAI 官方，The X Subscription 把 Grok、Grok Bot、Cursor 与 X Premium 捆成一单；Premium 月费 $30，官方对标原先 SuperGrok + Cursor Pro + X Premium+ 合计约 $90/月——本文只做价目、用量池与切换退款的算账说明。

---

## 4. 完整正文（可直接发表）

### 先说结论

据 xAI 官方（信息日期约 2026-10-12，核对 2026-11-10）：

- **一件事**：原先可能要分别订的 Grok、Grok Bot、Cursor、X Premium，可以并进 **The X Subscription**。
- **一个价锚**：个人档 **Premium = $30/月**，官方写明包含原先 **SuperGrok + Cursor Pro + X Premium+** 的权益，并称此前合计约 **$90/月**。
- **一套用量**：付费档有一份 **按周刷新** 的 Grok 模型用量池，在 Grok 与 Cursor 之间共享；用超了可 top-up，第三方模型另计。
- **老用户**：可不切，旧价旧权益可继续；若切，走官方 Unify / 账单入口，**按比例退未用完周期**，新订阅立即生效。

本号的 Bot 团队就运行在这套工具上。

价格一律按官方 **美元标价**；税费、能否用某种支付方式、你所在地能不能订，都以结账页与账单页当场显示为准，本文不猜测人民币税后价或中国大陆可用性。

---

### 一、这单订阅里到底有什么

据官方介绍页 [Introducing The X Subscription](https://x.ai/news/x-subscription)（新闻列表标注 2026-10-12；核对 2026-11-10）：

| 组件 | 官方怎么说 |
|------|------------|
| **Grok** | 聊天、语音、图像与视频生成 |
| **Grok Bot** | AI 队友，帮你把活干完（**Premium 及以上才含**，见下文定价文档） |
| **Cursor** | 本地与云端 coding agents |
| **X** | 勾号、创作者工具、更少广告；更高档可接近去掉时间线广告 |

官方一句话定位：一条订阅覆盖「从想、做，到建、发」的路径（thinking and creating to building and sharing）。

新用户从即日起可订；老用户切换选项会滚动出现在账户账单设置里。

---

### 二、五档怎么算（个人）

综合官方公告价目表与定价文档（核对 2026-11-10）：

| 档位 | 月付（USD） | 年付（USD，官方表） | 含用量（相对 Plus） | 要点（据官方） |
|------|-------------|---------------------|---------------------|----------------|
| **Free** | $0 | $0 | Limited | 每日可用 Grok；Cursor coding agents 起步额度；标准 X |
| **Plus** | $8/月 | $80/年（约合 $7/月） | Base | 更多 Grok/Cursor 用量；X 勾号、创作者工具、更少广告；**不含 Grok Bot** |
| **Premium** | $30/月 | $300/年（约合 $25/月） | **4×** Plus | 官方写：SuperGrok + Cursor Pro + X Premium+ 权益，**此前合计约 $90/月**；含 Grok Bot |
| **Super** | $100/月 | $1000/年（约合 $84/月） | **15×** Plus | Premium 之上更大用量等 |
| **Ultra** | $200/月 | $2000/年（约合 $167/月） | **50×** Plus | 再上一级 |

来源：

- 月付五档与 Premium「previously $90/month combined」：[x.ai/news/x-subscription](https://x.ai/news/x-subscription)（2026-10-12）
- 年付与「Grok Bot 仅 Premium/Super/Ultra」：[docs.x.ai/x-subscription/pricing](https://docs.x.ai/x-subscription/pricing)（文档 Last updated 约 2026-10-11；核对 2026-11-10）
- 页面价目与「4x / 15x / 50x vs Plus」：[x.ai/pricing](https://x.ai/pricing)（核对 2026-11-10）

**算账提示（Premium）**

- 官方自己做的对标：**约 $90 → $30**，对应三件套权益合订。  
- 官方未在同一段拆出「SuperGrok 占多少 + Cursor Pro 占多少 + X Premium+ 占多少」的精确分项——正文只采用官方合计数，不自行拆账。  
- 列表价 **不含销售税**；需要时结账另加（定价文档原文）。  
- 定价页脚注：所示价格不含适用税费（如 VAT）；Cursor 里第三方模型不在月费内，须另购。

**团队档（顺带一眼）**：Team 的 Premium / Super / Ultra 与个人同档同价按座位计；相对旧 Cursor Teams，官方称单价更低、coding 用量约 **3×**，并含 SSO、管理、统一账单、用量分析、SOC 2 等（见新闻页 Teams 段）。普通人个人订可跳过；企业找销售。

---

### 三、共享用量池：钱花在哪、怎么耗

这是合订后最容易算错的一块。据官方 Usage / Pricing 文档与定价页 FAQ（核对 2026-11-10）：

1. **一周一池**  
   - 每个付费座位有一份 **weekly pool**，只覆盖合格的 **第一方** 用量（Grok 与 Cursor 相关表面）。  
   - **不是** Grok 一份、Cursor 一份各算各的；共享而非拆成两个产品配额。

2. **池子覆盖什么**  
   - Grok 侧：Chat、Imagine、Voice，以及（有权限时）**Bot**。  
   - Cursor 侧：使用 **Grok 模型** 的 coding 相关用量进同一池。  
   - 官方新闻页还写：各 X Subscription 档相对旧 Cursor 可比档，至少约 **2×** coding 用量（用自家模型时）。

3. **倍率怎么读**  
   - Plus = Base；Premium ≈ Plus 的 **4×**；Super **15×**；Ultra **50×**（官方对照表述）。  
   - 不同产品/任务从池里扣的速率不同——「刷一天语音」和「跑一晚 agent」耗量不一样；以账户内 live usage 为准。

4. **用超了怎么办**  
   - 可 **top-up** 预付额度，或等周刷新。  
   - 可开 Auto Top-up、设月度额外用量上限（见 [Managing The X Subscription](https://docs.x.ai/x-subscription/manage)）。

5. **第三方模型另账**  
   - Cursor 里 Claude、GPT 等：**不进** 周池含额；从第一次使用起按 **API 标价**，走 Additional Usage / 预付额度。  
   - 新闻页亦写：Premium 及以上仍可在 Cursor 用第三方模型，用量单独按 API list price top-up。

6. **Grok Bot 门槛**  
   - **Plus 不含 Bot**；Premium / Super / Ultra 才含。  
   - Bot 耗的也是同一座位的共享周池，不是额外白送一池。

定价页 FAQ 原意：额度按周刷新，所以「一天用猛了」不会直接吃光整月——但周池见底后，当周继续用就要靠 top-up 或等到重置。

---

### 四、官方建议你怎么选档

据 [x.ai/pricing](https://x.ai/pricing) FAQ「What is the right plan for me?」（核对 2026-11-10）：

- **Premium**：推荐给新接触 AI 的用户  
- **Super**：推荐给每天都在用 agent 的人  
- **Ultra**：重度用户  
- **Plus**：社交创作者、AI 用量有限  

这是官方推荐语，不是本站实测分级。

---

### 五、老用户：保留旧价，还是切换拿按比例退款

#### 1）可以不切

据 [Do I have to switch?](https://docs.x.ai/x-subscription/do-i-have-to-switch) 与新闻页：

- **切换是可选的**。  
- 不切：现有 SuperGrok / Cursor / X Premium 的计划、价格、功能继续，除非你自己改或取消。

#### 2）切了会发生什么（钱怎么走）

据 [Pricing · When you switch](https://docs.x.ai/x-subscription/pricing)、[Invoices & Refunds](https://docs.x.ai/x-subscription/invoices-and-refunds)、[What is The X Subscription?](https://docs.x.ai/x-subscription/overview)（核对 2026-11-10）：

- 纳入本次切换的、符合条件的直连计费旧订阅会在结账时 **取消**，由新的 X Subscription 取代。  
- **按比例退还** 账单周期内未使用时间；退款回到 **原支付方式**，**不会**先抵扣成新订阅的折扣——新计划按 **全价** 扣款。  
- 退款到账天数取决于银行/支付机构。  
- **新订阅立即生效**；新的计费周期从切换当天起算。  
- **合一（unify）一旦完成不可撤销**，客服也无法帮你撤销。

#### 3）从哪点进去（只写官方路径）

据 [How to unify accounts](https://docs.x.ai/x-subscription/unify-accounts) 与 X Premium 迁移文（核对 2026-11-10）：

| 你现在的情况 | 官方入口 |
|--------------|----------|
| 有付费 **Cursor** | 从 Cursor 开始：`https://cursor.com/unify` → Get started → 链接 Grok / X → 选档结账 |
| 从 **Grok** 起 | `grok.com` → Settings › Billing → Get started；或 `https://accounts.x.ai/unify` |
| 只有 **X**、没有付费 Cursor | 可在 `x.com` 订阅设置里升级；**此路径不含 Cursor**——若已有付费 Cursor，务必从 Cursor 起 |
| 新用户 | `https://x.ai/pricing` 直接选档 |

新闻页亦写：老用户会在 **account billing settings** 看到切换选项；也可见有限时优惠，以账单页展示为准。

切换后管理账单：`https://grok.com/dashboard/billing`（计划、发票、预付额度、Auto Top-up、支出上限等）。

#### 4）容易踩坑：App Store / Google Play

官方明确例外（须照办，避免双开账单）：

- **Cursor 经 Apple App Store 购买**：网页可以切到 X Subscription，但 **官方无法取消或退款** 该 Apple 订阅 → 须在 iPhone/iPad **设置 → 订阅** 里自己取消，并向 Apple 申请退款；否则可能被继续扣 Cursor 费。  
- **Grok / Grok Bot / X Premium 经 App Store**：切换时官方会取消并向 Apple 申请按比例退款，**是否退、退多少由 Apple 决定**。  
- **经 Google Play 买的 Grok / Bot / X Premium**：切换后请到 Google Play 核对是否仍自动续订，仍在续则自行取消。  
- **赠送的 X Premium 或 Apple Family Sharing**：不取消、不退款。

移动端：现有付费用户切换目前要走 **网页**；手机 App 会导向网页。

---

### 六、支付与「国内能不能用」——只写官方写明的

- 标价为 **美元**；列表价不含销售税，该加税时结账加（定价文档）。  
- 定价页脚注再次声明：不含 VAT 等税费；价格可能变更；取消须至少在续费前 24 小时。  
- 网页可接受的支付方式官方列出：**Cards、Apple Pay、Google Pay、Link、Alipay**；并写明 **部分支付方式仅在特定国家可用，以结账页显示为准**（[payment-methods](https://docs.x.ai/x-subscription/payment-methods)，核对 2026-11-10）。  
- **人民币支付、中国大陆可用性与税后价：以美元计价，支付与可用性以官方账单页 / 结账页为准**——官方未在本文所用页面给出「中国大陆人民币税后价目表」，本文不补猜。

订阅须经官方渠道；官方声明不授权经销商，第三方代购可能无效或被停用（定价页 FAQ）。

---

### 七、写给普通人的「要不要动」清单

1. **已经分别在付 SuperGrok + Cursor + X，且接近 Premium 能力**：对照官方「约 $90 → $30」算是否值得切；切前确认支付方式是否在结账可用列表。  
2. **只要轻度聊天 / 发帖**：看 Plus $8；需要 **Grok Bot** 至少 Premium。  
3. **Cursor 吃第三方模型很重**：合订省的是 Grok 池与 X 权益，**省不掉** Claude/GPT 的 API 另账。  
4. **App Store 买的 Cursor**：切之前先读清「双开账单」警告，安排好在苹果侧取消。  
5. **不想折腾**：官方允许不切，旧计划可继续。

---

### 八、信息时效

本文关键价目与切换规则核对于 **2026-11-10（Asia/Shanghai）**，主要依据 2026-10-11～10-12 前后的官方新闻与文档。订阅产品会改价改规则——下单前请再打开 `x.ai/pricing` 与你的账单页确认一眼。

---

## 5. 封面与正文配图需求清单

合集封面已定版科技风 **1080×1440**；单篇封面沿用科技风语言，不用魔兽站牌匾风。

| 编号 | 用途 | 尺寸建议 | 内容说明 | 来源 | 工作区路径 / 状态 |
|------|------|----------|----------|------|-------------------|
| 封面 | 单篇封面 | 按推送端裁切；素材底图 2400×1260 | 科技风；可用官方 OG 主视觉 + 标题字「X Subscription / 一单订」 | 官方新闻 OG | **已落盘** `assets/2026-11-10-X-Subscription/og-the-x-subscription.png`（2400×1260 PNG；来自 https://media.x.ai/v1/website/the-x-subscription-db7a1253.png ） |
| 图1 | 正文·五档价目 | 原图 2400×1260 或网页截图 | 定价页五档对照，便于读者对账 | 官方定价页 OG / 页面截图 | **已落盘** `assets/2026-11-10-X-Subscription/pricing-og.jpg`（2400×1260 JPEG；来自 x.ai/pricing OG）。**建议另补**：成稿推送前在 `https://x.ai/pricing` 截一张含 Free～Ultra 价签的界面图（官方页现网，标注截图日期 2026-11-10）——**尚未截**，见自检 |
| 图2 | 正文·共享池示意 | 16:9 或正文通栏 | 可用文字信息图（自制科技风）：「周池共享 Grok↔Cursor / 第三方另计 / 周刷新」；勿冒充官方 UI | 自制（非官方截图） | **未制作** |
| 图3 | 正文·切换路径 | 通栏 | 官方 Unify 入口示意：可截 `cursor.com/unify` 公开落地页（无登录态隐私信息） | 官方公开页截图 | **未截取** |
| 图4 | 正文·账单管理 | 可选 | `grok.com/dashboard/billing` 需登录，**不宜**用含个人账单的截图；可只用官方文档文字步骤，或官方帮助页公开示意图（若有） | — | **缺；建议正文以文字步骤代替，或推送前用官方无个人数据的示意图** |

**版权与使用**：上述两张已下载文件为官方站点公开 OG 图，用于本号文章配图引用并标注来源；推送前按公众号规范保留来源说明。

---

## 6. 完整来源清单

| # | 关键事实 | 链接 | 信息日期 | 核对日期 |
|---|----------|------|----------|----------|
| 1 | 产品发布、四组件、五档月价、Premium 原约 $90、2× coding、切换与按比例退款概述、Teams 3× | https://x.ai/news/x-subscription | 新闻列表 2026-10-12 | 2026-11-10 |
| 2 | 新闻列表日期交叉 | https://x.ai/news | 列表含 Oct 12, 2026 | 2026-11-10 |
| 3 | 现网页价目、4×/15×/50×、FAQ 选档与周池说明、税费脚注 | https://x.ai/pricing | 动态页；核对日读取 | 2026-11-10 |
| 4 | 月/年价表、Bot 档位、共享池与第三方、切换退款要点、税 | https://docs.x.ai/x-subscription/pricing | Last updated 约 2026-10-11 | 2026-11-10 |
| 5 | 周池机制、Additional Usage、Team 座位各有池 | https://docs.x.ai/x-subscription/usage-limits | 核对日读取 | 2026-11-10 |
| 6 | 切换可选、不切则旧计划继续 | https://docs.x.ai/x-subscription/do-i-have-to-switch | 核对日读取 | 2026-11-10 |
| 7 | Unify 入口与步骤、永久合一、App Store/Play 例外 | https://docs.x.ai/x-subscription/unify-accounts | 核对日读取 | 2026-11-10 |
| 8 | 退款去向、按剩余周期、旧订阅处理 | https://docs.x.ai/x-subscription/invoices-and-refunds | 文内 Last updated: October 12, 2026 | 2026-11-10 |
| 9 | 总览：周池、第三方、切换后果 | https://docs.x.ai/x-subscription/overview | 核对日读取 | 2026-11-10 |
| 10 | X 权益档位、从 X/Cursor 切换分支 | https://docs.x.ai/x-subscription/x-premium | 核对日读取 | 2026-11-10 |
| 11 | Grok Bot 仅 Premium+、进共享池 | https://docs.x.ai/x-subscription/grok-bot | 核对日读取 | 2026-11-10 |
| 12 | 账单后台路径、top-up、支出上限 | https://docs.x.ai/x-subscription/manage | 核对日读取 | 2026-11-10 |
| 13 | 支付方式含 Alipay；按国家显示 | https://docs.x.ai/x-subscription/payment-methods | 核对日读取 | 2026-11-10 |
| 14 | App Store Cursor 不能由官方退 | https://docs.x.ai/x-subscription/app-store | 核对日读取 | 2026-11-10 |
| 15 | 封面 OG 图 | https://media.x.ai/v1/website/the-x-subscription-db7a1253.png | 随新闻页 | 2026-11-10 下载 |

---

## 7. 待核项与自检

### 待核项

1. **中国大陆可用性与人民币税后价**：官方未给出专表；正文已写「以美元计价，支付与可用性以官方账单页为准」。Alipay 在支持列表中，但是否对你所在地开放 **仅以结账页为准**（待核个案）。  
2. **「约 $90」三件套的分项构成**：官方只给合计对标，未给分项价拆解 → 不成文猜测。  
3. **各档周池的绝对额度数字**（多少请求/多少美元计量）：公开页多用 Base/4×/15×/50×，精确绝对值以账户 Usage 与定价页现网为准 → 待核具体数字。  
4. **限时切换优惠内容**：新闻写 billing settings 可见；优惠条款因人而异 → 待核，正文未写死优惠金额。  
5. **定价页现网价签截图**：OG 已存；含完整五档价签的界面截图建议推送前补一张并注明截图时刻。

### 自检

- **来源是否齐**：是。关键价目、用量池、切换与退款路径均回源至 x.ai 新闻、定价页与 docs.x.ai；无凭空步骤。  
- **待核剩几条**：**5** 条（见上）。  
- **配图缺哪几张**：已落盘 **2** 张（封面 OG、定价 OG）。仍缺：**图1 现网价目界面截图**、**图2 共享池示意（自制）**、**图3 Unify 公开页截图**、**图4 账单示意（建议省略或仅用无个人数据图）**。
