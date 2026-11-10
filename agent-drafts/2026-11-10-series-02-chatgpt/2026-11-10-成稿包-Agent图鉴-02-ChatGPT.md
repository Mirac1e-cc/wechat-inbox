# 成稿包：《Agent 图鉴》第 2 篇 · ChatGPT（OpenAI）（写作单 #003）

> 核对日期：2026-11-10（Asia/Shanghai，UTC+8）  
> 口径：据官方资料整理；无实测口吻。按刀哥视角写介绍文，不装成用过。  
> 交付形态：推送包（可直接发表正文 + 配图需求 + 来源清单）  
> 结构依据：写作单 #003 的企划模板小节。未见 `agent-series-plan-20261110.md`，本文不虚构企划原文。

---

## 1. 标题备选（3 个）

1. **【建议主标题】先认识 ChatGPT：GPT-6 怎么选，Work、Codex 和 dots 怎么进，各档多少钱**
2. Agent 模式已经换成 Work：OpenAI 这条产品线该怎么订
3. Astra、Sol、Terra、Luna：ChatGPT 现在有哪些模型，Agent 从哪进

---

## 2. 作者

刀哥

---

## 3. 一句摘要

ChatGPT 用 OpenAI 自己的模型。付费 Chat 走 GPT-6 Sol，Pro 推理档是 Astra；交成品走 Work，写代码走 Codex。旧版 agent 已改走 Work。下文按 2026-11-10 官方页整理。

---

## 4. 完整正文（可直接发表）

<span style="color:#0F7A74;font-size:12px;display:block;text-align:left;">曾经的小狂 · Agent 图鉴 第 2 篇</span>

### 先说结论

《Agent 图鉴》一家一家讲：模型是谁家的、Agent 产品怎么用、钱怎么算。第一家是 Anthropic 的 Claude。这一篇是第二家，OpenAI，产品叫 ChatGPT。

我先把结论放在前面。这篇是介绍，不是评测——版本、价格、档位都对过 2026 年 11 月 10 日的官方页面；我没上手用过的，不会写成我的体验。官方页说法不一致的地方，我并陈，并标了待核。

- **模型是自家的。** ChatGPT 的聊天、交成品、写代码，用的都是 OpenAI 自己的 GPT 系模型，不是套别人的接口。
- **日常怎么选。** 在 Chat 里，官方帮助中心写：选 GPT-6 时，Instant 到 Extra High 由 **GPT-6 Sol** 驱动；Pro 推理档是 **GPT-6 Pro**，由 **GPT-6 Astra** 驱动。更长、要交文档或幻灯的任务，走 **ChatGPT Work**；写代码走 **Codex**。这两处还可以选 **GPT-6.1 Sol**、**GPT-6.1 Terra** 等，它们不在普通 Chat 对话里。Free / Go 在 Chat 里用哪一款，官方页写法不完全一样，下面单独说明。
- **你从哪进。** 普通聊天走 `chatgpt.com`，以及手机、桌面 App。要让它做完一件多步的事、交出文档或表格，走 **Work**。写代码走 **Codex**（桌面、终端、IDE、云端）。另外，Pro 等档还有常驻的 **dots**（官方称为 always-on agents）。帮助中心开篇写明：**ChatGPT agent 已不可用**，改用 Work；需要浏览网页的流程，另见云端浏览器说明。
- **钱怎么分。** 免费档可以聊天，Codex 也包含在各档里，但 **Codex Cloud** 不含 Free / Go。个人付费现在是 Go、Plus，以及按月计的 Pro 100 / Pro 200 / Pro 500。团队是 Business 与 Enterprise。API 另算。
- **榜上什么位置。** 只说一句，跟开场图用的是同一份数据：Arena（原来的 LMArena）Agent 榜在 **2026-11-08** 这份快照里，**GPT-6 Astra (Max)** 净改进 **14.24%**，排第 **5**；**GPT-6.1 Sol (Max)** 第 **6**（**12.53%**）；**GPT-6.1 Terra (Max)** 第 **7**（**12.10%**）。这个指标叫 Net Improvement（净改进），是按真实 Agent 会话里的综合表现排的，不是考试式跑分。

价格我按官方的 **美元标价** 写。税多少、你那边能不能订，以帮助中心的支持地区名单和结账页当场显示为准。官方支持名单里没有中国大陆，人民币税后价我也不猜。

---

### 〇、本期榜单数据

开场图是我按官方表做的，米白底、钢蓝条，本期主角（OpenAI 的三个型号）用深蓝条标出。

数据来自 [Arena Agent 榜](https://arena.ai/leaderboard/agent)，页面标注快照日期 **Nov 8, 2026**（2026-11-08），同时写着 2,750,973 个会话、57 个模型。核对时间是 **2026-11-10 17:31–17:35**（Asia/Shanghai，UTC+8）。

**Net Improvement（净改进）** 是这个榜的综合排序指标。官方说明里写：按真实 Agent Arena 会话中的表现动态排名，信号包括任务成功、用户满意度、可引导性等。它不是把模型拉去考一张卷再排座次。图里的百分数是官方表的中心值，后面的 ± 是页面给出的区间。第 2 名 **Gemini 4 Carbon (High)** 带官方 **Preliminary** 标注，表示初步结果。

前 10 名和国产最高 1 名如下（与开场图、文末来源清单同一组数字）：

| 名次 | 模型 | 厂商 | 净改进 |
|------|------|------|--------|
| 1 | Claude Opus 5.5 (Max) | Anthropic | 19.96%±2.05% |
| 2 | Gemini 4 Carbon (High) | Google | 16.63%±0.71%（Preliminary） |
| 3 | Claude Sonnet 5.5 (Max) | Anthropic | 15.99%±2.84% |
| 4 | Claude Fable 5.1 (Max) | Anthropic | 14.34%±1.98% |
| 5 | GPT-6 Astra (Max) | OpenAI | 14.24%±2.03% |
| 6 | GPT-6.1 Sol (Max) | OpenAI | 12.53%±1.12% |
| 7 | GPT-6.1 Terra (Max) | OpenAI | 12.10%±1.36% |
| 8 | Gemini 4 Argon (High) | Google | 10.83%±0.87% |
| 9 | Muse Wonder Full (Max) | Meta | 9.09%±0.94% |
| 10 | Claude Fable 5 (High) | Anthropic | 7.70%±1.13% |
| 13 | Kimi K3.1 Pro (Max) | Moonshot | 5.24%±1.12%（国产最高） |

这份快照的日期是 11 月 8 日。Claude Fable 5.2 是第二天（11 月 9 日）才发布的，没有进这期名次，图里也不写。

配图：`images/01-arena-agent-top10-chatgpt.jpg`

---

### 一、一句话定位

ChatGPT 是 OpenAI 做的 AI 助手和 Agent 产品线。聊天在 Chat，把一件更长的事做完、交出文档或表格在 Work，写代码在 Codex；部分档位还有常驻的 dots。

**大脑来源：自家模型。** Chat、Work、Codex 和 dots，用的都是 OpenAI 自己的 GPT 系模型。

---

### 二、这家公司是怎么过来的

下面只写核对日打开的官方页里能对上的节点，没打开专页的创立年份、融资轮次不补。

官方 [About](https://openai.com/about/) 页写：OpenAI 是一家 AI 研究与部署公司，使命是确保通用人工智能（AGI）——官方把它解释为普遍比人更聪明的 AI 系统——造福全人类。同一页还写现行结构：非营利的 **OpenAI Foundation** 治理作为公共受益公司运营的 **OpenAI Group**，使命由这两个组织一起推进。

产品这条线上，和本期直接相关的节点是：2026 年 9 月 22 日发布 **GPT-6 Sol** 和 **GPT-6 Luna**；9 月 29 日发布 **GPT-6.1 Sol**，同一天介绍 **dots**；10 月 7 日把 GPT-6 与 **Intelligent UI** 推向 Chat。**GPT-6 Astra** 的发布页在核对日仍在线，页顶更新指向了 9 月 22 日和 9 月 29 日；最初发布日该页抓取文本里没有稳定读出，我标了待核，不把某一个日期写成已核事实。**GPT-6.1 Terra** 的发布页同样已打开，精确发布日也标待核；dots 介绍页在 2026 年 11 月 3 日的更新里写，已把 Terra 纳入 dots 所用的模型家族。

上述节点的出处，文末来源清单里都有。

---

### 2.5 现在有哪些模型（核对 2026-11-10）

先分清两个使用面。一个是 **Chat**（日常对话，可带 Intelligent UI）；另一个是 **Work / Codex**（交成品、写代码）。官方多次写明：型号在这两处并不完全一样。

怎么选，我按官方自己的说法整理，不是我用过之后的判断。

| 模型 | 官方怎么说 | 主要出现在哪 |
|------|------------|--------------|
| **GPT-6 Astra** | 官方模型指南把它写成最智能的一档，用于最吃推理、编码和专业工作的场合。API 调用名 `gpt-6-astra`。在 Chat 里，Pro 推理档由它驱动，产品名是 GPT-6 Pro。Plus 在 Chat 里不含这一档，但 Plus 在 Work 和 Codex 里含 Astra。 | Chat（符合条件的 Pro 等）；Work / Codex（Pro 全含；Plus 含，但是限量） |
| **GPT-6 Sol** | 2026-10-07 的 Chat 更新写：Plus / Pro / Business / Enterprise 的 Chat，由 GPT-6 Sol 驱动，针对日常对话调优。帮助中心写：选 GPT-6 时，Instant、Medium、High、Extra High 由它驱动。API 调用名 `gpt-6-sol`。 | Chat（付费档滚动推出）；Work / Codex 也列有 GPT-6 Sol |
| **GPT-6.1 Sol** | 官方定位：接近 Astra 的智能，标准输入 / 输出价是 Astra 的五分之一。发布页写：在 ChatGPT Work 和 Codex 向 Plus、Pro、Business、Enterprise、Edu 推出，**当时尚未进入 Chat**。默认上下文在 Work / Codex 里是 50 万 token。API 调用名 `gpt-6.1-sol`。 | Work / Codex；不在普通 Chat |
| **GPT-6.1 Terra** | 官方定位：更快、更省的一档，强调视觉推理、精确的电脑操作，以及更清楚、更自然的写作。发布页写：向 Plus、Pro、Enterprise、Edu 的 Work 和 Codex 推出，API 调用名 `gpt-6.1-terra`。该句没有点名 Business，和帮助中心「Work / Codex 的可选模型」如何对应，我标了待核。它也不在普通 Chat 里。 | Work / Codex；不在普通 Chat |
| **GPT-6 Luna** | 官方模型指南：最快、最省成本，适合目标明确、量大的日常任务。2026-10-07 的 Chat 更新写：Free / Go 的 GPT-6 由 Luna 驱动。API 调用名 `gpt-6-luna`。 | 见下方「Free / Go 用哪一款」 |
| **GPT-5.6 家族** | 帮助中心写：GPT-6 这次滚动推出，**并不退役**仍可选择的旧型号。GPT-5.6 Sol 面向复杂的编码、知识工作与研究等；GPT-5.6 Sol Pro 是这一家里最高能力的一档。Terra / Luna 在普通 Chat 里不可选，按计划出现在 Work、Codex 或 API。 | Chat 里仍可选 GPT-5.6 Sol；Work / Codex / API 另有 Terra、Luna |

**Free / Go 在 Chat 里用哪一款：两处官方说法不一致，并陈，待核。**

- 2026-10-07 的公告 [GPT-6 and Intelligent UI for everyone](https://openai.com/index/gpt-6-for-everyone/) 写：付费档由 **GPT-6 Sol** 驱动，Free 与 Go 由 **GPT-6 Luna** 驱动；当日先向 Plus / Pro / Business / Enterprise 的 Chat 滚动，次日扩到 Free / Go。同日的 October 系统卡也按 Chat 中的 GPT-6 Sol / Luna 来写。
- 帮助中心 [GPT-6 and other models in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt)（页头显示 Updated 10 days ago，核对于 2026-11-10）写：Free 与 Go **没有** GPT-5.6 Sol，默认是 **GPT-5.6 Luna**，Think 也由 GPT-5.6 Luna 驱动。Go 的专文（核对日显示 Updated 4 hours ago）同样写：Think 用 GPT-5.6 Luna，Go 不含 GPT-5.6 Sol。

我不在这两套说法里替你裁定哪一页已经过时。你在产品里看到的，以当时账号里的模型菜单为准。

**Intelligent UI。** 官方的说法是：GPT-6 在 Chat 里可以把文字、视觉和可交互组件组合在一起，不必写特殊提示；回答也可以边想边出现。帮助中心写：这些能力在 Web 和已更新的应用上，于 GPT-6 的 Instant 到 Extra High 滚动推出；**Pro 推理档（由 Astra 驱动）没有这项能力**。旧版 macOS / Windows 桌面应用也不支持，官方建议改用网页。它没有单独的用量配额，仍走各档已有的模型和工具额度。

#### API 价目（美元 / 百万 token）

来源是 2026-09-22 的 Sol / Luna 发布页、GPT-6.1 Sol 发布页、GPT-6.1 Terra 发布页，以及 2026-10-02 的 [GPT-6 家族模型指南](https://openai.com/index/practical-guide-building-gpt-6/)。核对日期 2026-11-10。下表是标准输入 / 输出，以及已写明的缓存命中价。

| 模型 | 输入 | 输出 | 缓存命中 |
|------|------|------|----------|
| GPT-6 Astra | $10 | $50 | $1.00 |
| GPT-6.1 Sol | $2 | $10 | $0.10 |
| GPT-6 Sol | $2 | $10 | 发布页未在同一张价表里给出缓存命中价；6.1 Sol 发布页写，它的缓存输入价比 GPT-6 Sol 的缓存价低 50% |
| GPT-6.1 Terra | $1 | $5 | $0.05 |
| GPT-6 Luna | $0.10 | $0.50 | $0.01 |

另外几笔也按官方页写：

- **Fast mode**（API）：Astra 的发布页写，最高大约是 Standard 的 2 倍速度，按标准价 **2 倍**计。
- **Ultrafast**：在 Codex / 部分 API 场景提供。个人档里，帮助中心写：在 Pro 各档中，只有 **Pro 500** 含 Ultrafast；计入套餐内用量时，按该模型 Standard 的 **8 倍**消耗，之后用积分则按 Standard 积分价的 **6 倍**。
- 列表价是否含税、能否随账户所在地变化，以 API 定价页和结账页为准。官方声明，价格可以调整。

---

### 三、能干什么

这里只讲 OpenAI 自己的产品。

**Chat（日常对话）。** 网页、iOS、Android、桌面都可以聊，免费档也包含。官方把 Chat 写成偏快的对话：提问、搜索、头脑风暴、日常问题。付费档在 GPT-6 滚动到位后，还可以用 Intelligent UI。Free 与 Go 的日常文字聊天，帮助中心写是不限条数的，但仍受防滥用限制；上传、作图、语音、数据分析等另有额度。

**ChatGPT Work。** 官方帮助中心把它写成一个 **Agent**：面向更长、多步的工作，以及做完的成品，例如研究一个题目、分析材料，或做出文档、表格、演示、报告、Site。可以在网页和手机上用（须是符合条件的付费档），桌面端在计划和空间允许时也可以用；桌面端经你允许后，还能用本地文件和桌面应用。云端的 Work 对话可以在网页、手机、桌面之间接着看。也可以设定时任务，或在符合条件时用事件触发（例如授权后的 Gmail、Slack、GitHub 动态）。帮助中心还写：Voice 可以在网页和手机的 Work 里用，桌面端的 Work 与 Codex 也可以用语音。

**原先的 ChatGPT agent。** 帮助中心专文开篇写：**ChatGPT agent is no longer available.** 官方要你改用 Work 做更长的多步任务和成品；需要浏览网页的，另看云端浏览器说明。同一篇后面还留着「如何开启 agent mode」和按月条数（Plus 40、Pro 400 等）的旧段落；Pro 介绍页也还出现 “agent mode” 字样。这是官方页面自身的不一致，我标了待核——介绍时以该文开篇的「已不可用、改走 Work」为准，不把旧条数当成当前规则来推荐。

**Codex。** 这是官方的编程 Agent：写代码、改代码、跑测试和命令、做代码评审，以及和仓库一起工作。产品页写：包含在 ChatGPT 套餐里；可以在 ChatGPT 里、编辑器和终端使用，账号打通。入口包括 ChatGPT 桌面应用的 Codex 模式、Codex CLI、IDE 扩展、网页，以及 **Codex Cloud**（在 OpenAI 托管的电脑上跑，电脑休眠也可以继续）。帮助中心写：Codex 包含在各档，**含 Free 与 Go**；Codex Cloud 只给符合条件的 Plus、各档 Pro、Business、Enterprise、Healthcare、Education，**不含 Free 与 Go**。Astra 要用 Codex CLI **0.153.0** 或更高，桌面应用也需要更新到最新版。

**dots。** 官方把它写成常驻（always-on）的 Agent：有自己的云端电脑和浏览器，能在对话之间继续推进项目，也可经你允许连接本机。2026-09-29 的介绍页写，由 GPT-6 Astra 驱动；2026-11-03 的更新写，已把 **GPT-6.1 Terra** 纳入，不同部分的工作可以调用不同模型。官方举例包括准备演示、根据反馈改应用、根据新证据更新分析等。入口在 ChatGPT 的桌面、网页和手机；也可以在 Slack、Teams 里对话，短信能力当时还在有限预览。帮助中心写：和 dot 的对话 **不计** 入 ChatGPT 的用量；但若它把任务交给 Work 或 Codex，那些任务仍按原规则计。第一枚 dot，介绍页写含在符合条件的 Pro 或 Business Premium 套餐里，不另收费。官方也提醒：dots 仍可能出错，重要结果需要你自己看过。

**云端浏览器、深度研究、定时任务、语音。** 浏览类工作，官方在 agent 专文里指向云端浏览器说明。Deep research、定时任务、自定义 GPT、Projects，出现在定价对照和各档说明里，具体哪一档有、额度多少，以定价页现网为准。Voice 在 Chat 与 Work / Codex 里的计量规则不同，帮助中心写：常规 Chat Voice 有单独额度，不会消耗 Codex 用量。

---

### 四、怎么用：从哪进、怎么上手、有什么门槛

#### 从哪进

| 入口 | 官方位置 | 谁能用（据官方） |
|------|----------|------------------|
| 网页 Chat / Work | https://chatgpt.com | 各档都可以聊天；Work 在符合条件的付费档 |
| 桌面 / 手机 | 官方 App（iOS、Android；桌面有 macOS、Windows） | 各档可以装 App；本地文件、本机应用须在桌面端授权 |
| Codex | 桌面应用的 Codex 模式、Codex CLI、IDE 扩展、网页；Cloud 另见帮助中心 | 各档含 Codex；Cloud 不含 Free / Go |
| dots | 在 ChatGPT 桌面应用、桌面网页或手机应用里创建；之后可在 Slack / Teams 对话 | 见下一节的地区和档位限制；不支持手机网页 |
| API / 控制台 | OpenAI API（Responses API 等）；也可经 Azure、Amazon Bedrock | 另开开发者账户和账单 |

#### 上手

官方步骤就这几步，我不加自己的路径。

1. 在官方支持地区打开 `chatgpt.com`，或下载官方 App，用官方登录方式注册。可以先用免费档，看能不能登录、能不能聊天。
2. 要用 GPT-6 的更高思考档位、Work、扩大后的 Codex，或 Pro 推理档（Astra），按定价对照升到对应的付费档。Plus 在 Settings 里走 Upgrade Plan → Get Plus。
3. **Work**：在网页或手机上选择 Work，说明要交的成果，补上需要的文件和限制。在桌面端，先选 ChatGPT，再用开关切到 Work；要用本地文件夹，须在桌面应用里授权。
4. **Codex**：用 ChatGPT 账号登录所选客户端。终端里，进入项目目录后运行 `codex`，按提示登录。Cloud 要先在桌面或网页创建并发布环境，再在手机上选用。CLI 要用 Astra，先确认版本不低于 0.153.0。
5. **dots**：在桌面应用、桌面网页或已更新的手机应用里按引导创建，给它起名，并连接你允许的应用。帮助中心写：创建可在这些客户端完成；不支持手机网页。可选是否允许它使用你的电脑（默认关闭，须在该电脑的桌面应用里打开）。
6. 用量在账户的 Settings → Usage（Codex 里是 Usage & Billing 或 `/status`）查看。触顶之后，可以等重置、换一档可用模型，或在符合条件时购买 credits。官方写明：客服不能帮你重置额度。

#### 地区、账号、语言

地区看帮助中心这篇：[ChatGPT Supported Countries](https://help.openai.com/en/articles/7947663-chatgpt-supported-countries)（页头显示 Updated 19 days ago，核对于 2026-11-10）。我打开时，名单里 **没有中国大陆，也没有见到香港、澳门**；**台湾在列**。官方写：在名单以外的地方访问或提供访问，账户可能被阻止或暂停。能不能订阅、按哪国结账，仍以该名单现网和结账页为准。

dots 还有额外限制。帮助中心写：个人 Pro 向 **18 岁及以上**、且市场 **不包括欧洲经济区、瑞士和英国** 的用户滚动推出；Business Premium 在 ChatGPT 支持地区，还要满足工作区条件；Enterprise / Edu / Healthcare 当时处于管理员预览（2026-11-04 至 11-18），之后默认打开、除非管理员退出。带阿联酋数据或推理驻留的工作区不可用。个人和 Business Premium 是逐步放开，可能要几天才看到。

账号上，个人套餐和 Business / Enterprise 工作区是分开的。Codex 也可以改用自己的 API 密钥，那时按 API 计价，不再走 ChatGPT 套餐用量。

模型能不能用中文对话，我打开的官方页没有写成一条单独的语言限制，我也不额外打包票。

---

### 五、多少钱（核对 2026-11-10）

个人档的美元数字，我以帮助中心和专项博文为准。`chatgpt.com/pricing` 在核对日可以打开功能对照，但是动态组件，部分价签在抓取时没有稳定读出；**推送前请再打开定价页看一眼当前展示价**。标价是否含税，以结账页为准；官方声明，价格可以调整。个人档（Go / Plus / Pro）帮助中心写：**不提供年付**，也不能提前一次付好几个月。

#### 个人档

| 档位 | 标价（USD） | 跟模型 / Agent 相关的要点（据官方） |
|------|-------------|--------------------------------------|
| **Free** | $0 | 可在网页 / 桌面 / 手机聊天。Codex 包含在各档里，但没有 Codex Cloud。没有 Work 的付费向能力（事件触发等帮助中心写明 Free / Go 没有）。日常文字聊天帮助中心写不限条数，仍受防滥用限制。 |
| **Go** | 2026-01-16 全球推出博文写：在美国是 **$8**/月，部分市场本地化计价。帮助中心（核对日刚更新）写：价格以定价页为准，美元结算，有限国家可用本地货币。我未能从定价页动态组件稳定读出当前展示数字，**待核**。 | 比 Free 更高的工具额度（作图、上传、数据分析等）。含 Think；Go 专文写 Think 用 GPT-5.6 Luna，不含 GPT-5.6 Sol。不含 Codex Cloud。有的地区正在测试广告。 |
| **Plus** | **$20**/月（按月） | 帮助中心：[What is ChatGPT Plus?](https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus/)。含 GPT-6 的 Medium / High，**不含 Extra High，也不含 Chat 里的 Pro 推理档**。Work、扩大后的 Codex、定时任务等在定价说明里列入 Plus。Plus **在 Work 和 Codex 含 Astra**（有限量，之后可用积分），Chat 里的 GPT-6 Pro / Astra 不在 Plus。 |
| **Pro 100** | **$100**/月 | 含 Chat、Work、Codex 中的 GPT-6 Pro（Astra）。在 Chat 里含 Extra High 与 Pro。Work / Codex 的套餐内用量，帮助中心写已比此前提高。不含 Ultrafast。只有月付。 |
| **Pro 200** | **$200**/月 | 用量高于 Pro 100。帮助中心写：新订阅重新开放，Work / Codex 额度已与较高档对齐。不含 Ultrafast。只有月付。 |
| **Pro 500** | **$500**/月 | 三档里套餐内用量最高，并含 **GPT-6 Astra / GPT-6.1 Sol 的 Ultrafast**。只有月付。 |

「不限量」要读官方限制。Pro 介绍页有 “Unlimited messages and uploads” 这类写法；同一套帮助中心又写：Pro 含的任何不限量访问都受防滥用限制；**GPT-6 Pro 本身有用量上限，订阅不等于可以无限用 Astra**。高峰期、模型、任务长度和速度档（Fast 按套餐内用量 2.5 倍计，Ultrafast 8 倍计）都会改变实际能做完的量。

Pricing 页还写 Pro 含每月 API credits，用于自建应用和 Agent；抓取时具体额度数字没有稳定读出，**待核**，以定价页现网为准。

#### Business 和 Enterprise

据 [ChatGPT Business overview](https://help.openai.com/en/articles/8792828-chatgpt-business-overview)（核对 2026-11-10）：

| 档位 | 标价（USD） | 要点（据官方） |
|------|-------------|---------------|
| **Business Standard** | 月付 **$25**/座/月；年付 **$20**/座/月 | 至少 2 座。含 ChatGPT、Work 和 Codex。可用灵活积分，在套餐额度之外续用。 |
| **Business Premium** | 月付 **$125**/座/月；年付 **$100**/座/月 | Work 与 Codex 用量更高；官方写没有 5 小时用量限制。可与 Standard 混配。dots 对 Business，官方写的是 Premium。 |
| **Enterprise** | 联系销售 | 管理员控制模型与功能。dots 须管理员开启（预览期规则见上）。 |

面向院校的 Edu、教师计划、非营利折扣，官方单列，这里不展开价目。

#### API 怎么算

具体单价见前面的价表。订阅费 **不含** 默认的全部 API 用量。Work / Codex 在用完套餐内额度后，符合条件的个人档可以买 credits，企业和教育另有 Rate Card。用自己的 API 密钥登录 Codex，按 API 价走，不走套餐池。

#### 国内能不能订

标价是美元。个人档支付方式，定价页 FAQ 写可用主流信用卡；Enterprise 可联系销售谈发票等。能不能用别的方式，以结账页为准，没有写明的渠道我不补。

官方支持地区名单（帮助中心，核对于 2026-11-10）**没有列入中国大陆，也没有见到香港、澳门**。

**中国大陆能不能订阅、人民币税后价是多少：以官方结账页和地区说明为准。** 我所用的官方页里，没有中国大陆的人民币税后价目表，这里不猜。

---

### 六、适合谁，不适合谁

这一节只根据官方自己的定位、帮助中心限制、定价和地区说明来对照，不是我用过之后给你分级。

**更对得上官方描述的，大概是这些人：**

- 在官方支持地区，用网页或 App 日常对话，并且接受付费使用 GPT-6 更高思考档位的个人（Plus 或以上）。
- 主要工作是编程、排错、和仓库一起改代码，愿意用 **Codex**（免费档可以入门；要 Cloud、更高用量，需 Plus 或以上）。
- 想先说一个目标，让它做出文档 / 表格 / 演示 / 报告，也愿意付费用 **Work**。
- 人在 dots 开放的市场、已满 18 岁、已经是 Pro（或 Business Premium / 已开启的 Enterprise），也接受它仍可能出错、重要步骤要你确认，可以看一看 **dots**。
- 要在自己产品里调用 GPT-6 家族，能接受按 token 计费的开发者（API）。

**按官方规则，往往对不上的是这些情况：**

- **所在地不在支持名单里。** 包括名单未列入的中国大陆等；不要假定一定能完成注册或扣款。
- **只想用免费档跑 Work，或用 Codex Cloud。** Work 的完整能力在付费档；Codex Cloud 不含 Free / Go。
- **在 Plus 里就要用 Chat 的 GPT-6 Pro / Astra，或 Extra High。** 官方对照表写这两项不在 Plus；Astra 在 Plus 里出现在 Work 和 Codex，而且是限量。
- **在 Pro 100 / Pro 200 里就要 Ultrafast。** 官方写，在 Pro 各档中只有 Pro 500 含。
- **在欧洲经济区、瑞士、英国的个人 Pro 用户，现在就想用 dots。** 帮助中心写明这些市场暂不在个人 Pro 的开放范围。
- **还想找到「Agent 模式」那个旧入口，并按旧的每月 40 / 400 条来规划。** 帮助中心开篇已写该产品不可用，改走 Work；旧段落是否仍残留在界面里，待核，不要按旧表下单。

---

### 七、同类对手一句话

同样是「有自家模型，并做成聊天或 Agent 产品」的，公开产品线可以对上的，包括 **Anthropic**（Claude 等，本连载第 1 篇）、**Google**（Gemini 等）、**xAI / SpaceXSI**（Grok 等，下一篇）、**月之暗面**（Kimi 等）。这里只点名，不展开评测。

---

### 信息时效与系列目录

关键价目、档位、模型名和入口，核对于 **2026-11-10（Asia/Shanghai，UTC+8）**。产品会改价、改规则、改默认模型——你下单或安装前，最好再打开 `chatgpt.com/pricing` 和对应帮助中心看一眼。

**系列目录**（《Agent 图鉴》第 2 篇）：

1. Claude（Anthropic）← 已刊  
2. ChatGPT（OpenAI）← 本篇  
3. Grok（SpaceXSI，原 xAI）  
其后已定顺序、尚未下单成稿：Cursor、Kimi。其余按点单，不预先写未公布的标题。

---

## 5. 封面与正文配图需求清单

合集封面已定版科技风 **1080×1440**；单篇封面沿用同一套科技风语言，不用魔兽站牌匾风。

**开场榜单图：已按写作单配色制作**（米白底、钢蓝条、本期主角深蓝条）。

| 编号 | 用途 | 尺寸建议 | 内容说明 | 来源 | 工作区路径 / 状态 |
|------|------|----------|----------|------|-------------------|
| 开场图 | 正文开头 | 1800×1438 | Arena Agent 榜前 10 + 国产最高；OpenAI 三条为深蓝 | 官方榜表，自制 | **已落盘** `images/01-arena-agent-top10-chatgpt.jpg`（旁有 png 与 SOURCES） |
| 封面候选 | 单篇封面 | 1600×900 等 | 科技风；可用官方 OG + 标题字「Agent 图鉴 · ChatGPT」 | ChatGPT / OpenAI 官方 OG | **已落盘** `og-gpt6-intelligent-ui.png`、`og-pricing.png`、`og-chatgpt-share.png` |
| 图1 | 正文·模型线 | 1600×900 | GPT-6 Astra 发布页 OG | 官方新闻 OG | **已落盘** `og-gpt6-astra.png` |
| 图2 | 正文·模型线 | 1600×900 | GPT-6 Sol / Luna 发布页 OG | 官方新闻 OG | **已落盘** `og-gpt6-sol-luna.png` |
| 图3 | 正文·模型线 | 1920×1080 | GPT-6.1 Sol 发布页 OG | 官方新闻 OG | **已落盘** `og-gpt6-1-sol.png` |
| 图4 | 正文·模型线 | 3840×2160 | GPT-6.1 Terra 发布页 OG | 官方新闻 OG | **已落盘** `og-gpt6-1-terra.png` |
| 图5 | 正文·Intelligent UI | 1600×900 | GPT-6 + Intelligent UI 公告 OG | 官方新闻 OG | **已落盘** `og-gpt6-intelligent-ui.png` |
| 图6 | 正文·Codex | 1600×900 | Codex 产品页 OG | openai.com/codex | **已落盘** `og-codex.png` |
| 图7 | 正文·dots | 1600×900 | dots 介绍页 / 产品页 OG | 官方产品 OG | **已落盘** `og-dots.png`、`og-dots-product.png` |
| 图8 | 正文·Go | 1600×900 | ChatGPT Go 公告 OG | 官方新闻 OG | **已落盘** `og-chatgpt-go.png` |
| 图9 | 可选·公司视觉 | 1600×900 | OpenAI About OG | openai.com/about | **已落盘** `og-openai-about.png` |
| 图10 | 正文·定价对照 | 现网截图 | 建议推送前在 `https://chatgpt.com/pricing` 截一张含各档价签的界面图，注明截图日期 | 官方现网 | **尚未截** |
| Arena 榜 OG | 可选 | 1200×630 | 官方 Agent 榜 og:image | indexable.arena.ai … v1.jpg | **缺**：核对日下载返回 HTTP 403，未落盘 |

**版权与使用**：已下载文件为官方站点公开 OG 图，用于本号文章配图并标注来源；推送前按公众号规范保留来源说明。不自制假的产品界面图。

---

## 6. 完整来源清单

| # | 关键事实 | 链接 | 信息日期 | 核对日期 |
|---|----------|------|----------|----------|
| 1 | GPT-6 + Intelligent UI 推向 Chat；付费档 Sol、Free/Go Luna 的公告口径 | https://openai.com/index/gpt-6-for-everyone/ | 2026-10-07 | 2026-11-10 |
| 2 | Chat 中的型号、思考档位、Intelligent UI 边界、Free/Go 写 GPT-5.6 Luna | https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt | 页头 Updated 10 days ago | 2026-11-10 |
| 3 | Work / Codex 定位、入口、Astra / 6.1 Sol / Terra、Voice、Ultrafast 规则 | https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex | 页头 Updated 4 days ago | 2026-11-10 |
| 4 | ChatGPT agent 已不可用，改走 Work；文内仍残留旧说明 | https://help.openai.com/en/articles/11752874-chatgpt-agent | 页头 Updated 14 days ago | 2026-11-10 |
| 5 | Codex 产品定位与套餐入口价签 | https://openai.com/codex/ | 核对日读取 | 2026-11-10 |
| 6 | Codex 各档可用性、Cloud 不含 Free/Go、CLI 登录 | https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan | 页头 Updated 5 days ago | 2026-11-10 |
| 7 | Pro 100 / 200 / 500 标价、月付、Ultrafast、用量口径 | https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers | 页头 Updated 7 days ago | 2026-11-10 |
| 8 | Plus $20/月、仅月付 | https://help.openai.com/en/articles/6950777-what-is-chatgpt-plus | 页头 Updated 21 days ago | 2026-11-10 |
| 9 | Go 的功能、以定价页为准、Think 用 GPT-5.6 Luna | https://help.openai.com/en/articles/11989085-what-is-chatgpt-go | 页头 Updated 4 hours ago | 2026-11-10 |
| 10 | Go 全球推出时美国 $8/月、部分市场本地化；当时 Plus $20、Pro $200 | https://openai.com/index/introducing-chatgpt-go/ | 2026-01-16 | 2026-11-10 |
| 11 | 定价页功能对照（动态价签未稳定读出） | https://chatgpt.com/pricing/ | 动态页；核对日读取 | 2026-11-10 |
| 12 | Business Standard / Premium 标价与座位规则 | https://help.openai.com/en/articles/8792828-chatgpt-business-overview | 核对日读取 | 2026-11-10 |
| 13 | GPT-6 Astra 定位、API 价、Fast mode、可用性 | https://openai.com/index/gpt-6-astra/ | 页顶更新 2026-09-22 / 09-29；最初发布日待核 | 2026-11-10 |
| 14 | GPT-6 Sol / Luna 发布、API 价、当时尚未进 Chat | https://openai.com/index/introducing-gpt-6-sol-and-luna/ | 2026-09-22 | 2026-11-10 |
| 15 | GPT-6.1 Sol 发布、价、Work/Codex 可用性、当时未进 Chat | https://openai.com/index/introducing-gpt-6-1-sol/ | 2026-09-29 | 2026-11-10 |
| 16 | GPT-6.1 Terra 定位、API 价、Work/Codex 可用性 | https://openai.com/index/introducing-gpt-6-1-terra/ | 精确发布日待核 | 2026-11-10 |
| 17 | GPT-6 家族选型与 Astra / 6.1 Sol / Luna 价签 | https://openai.com/index/practical-guide-building-gpt-6/ | 2026-10-02 | 2026-11-10 |
| 18 | dots 定位、档位、安全与 11-03 Terra 更新 | https://openai.com/index/introducing-dots/ | 2026-09-29；更新 2026-11-03 | 2026-11-10 |
| 19 | dots 产品页与档位 | https://chatgpt.com/features/dots/ | 核对日读取 | 2026-11-10 |
| 20 | dots 设置步骤、地区限制、计费预览窗口 | https://help.openai.com/en/articles/20001530-getting-started-with-your-dot | 页头 Updated 7 hours ago | 2026-11-10 |
| 21 | 支持地区名单 | https://help.openai.com/en/articles/7947663-chatgpt-supported-countries | 页头 Updated 19 days ago | 2026-11-10 |
| 22 | 公司定位与现行治理结构 | https://openai.com/about/ | 核对日读取 | 2026-11-10 |
| 23 | Arena Agent 榜快照（与 003 数据文件同一笔） | https://arena.ai/leaderboard/agent | 页面标注 Nov 8, 2026 | 2026-11-10 |

配图来源 URL 见第 5 节各行，下载日期 2026-11-10。

---

## 7. 待核项与自检

### 待核项

1. **Free / Go 在 Chat 中的驱动型号**：2026-10-07 公告与系统卡写 GPT-6 Luna；帮助中心（含核对日刚更新的 Go 专文）写 GPT-5.6 Luna。正文已并陈。  
2. **ChatGPT agent 专文开篇「已不可用」与文内旧步骤 / Pro 介绍页仍写 agent mode**：以开篇为准，界面是否仍残留旧入口，待核。  
3. **Go 当前展示价**：2026-01-16 博文写美国 $8/月；帮助中心要看定价页。定价页动态价签本次未稳定读出。  
4. **Pro 的每月 API credits 额度**：定价页有这项，具体数字抓取未稳定读出。  
5. **GPT-6 Astra、GPT-6.1 Terra 的精确发布日**：专页已打开，抓取文本未稳定读出日期。  
6. **GPT-6.1 Terra 是否包含 Business**：发布页该句只写 Plus / Pro / Enterprise / Edu；帮助中心把它列为 Work / Codex 可选模型。  
7. **中国大陆（及名单未列的香港、澳门）可用性与人民币税后价**：官方未给专表。  
8. **支持地区名单是否在「Updated 19 days ago」所覆盖范围之外还有未体现在该页的变更**。  
9. **各档绝对额度数字**（多少请求 / 多少 token）：公开页多为相对描述，精确值以账户 Usage 为准。  
10. **Arena Agent 榜若在发表前刷新**：须重抓，不能沿用 2026-11-08 快照。  
11. **定价页现网价签界面截图**：OG 已存，含完整档位价签的界面截图建议推送前补。

### 自检

- **来源是否齐**：是。模型名、API 价、订阅档位、Work / Codex / dots 限制、地区名单、Agent 榜名次，均回源至核对日已打开的官方页；无凭空步骤，无编造实测。官方不一致处已并陈并标待核。  
- **待核剩几条**：**11** 条（见上）。  
- **配图缺哪几张**：开场榜单图已制；已落盘多张官方 OG（Astra / Sol-Luna / 6.1 Sol / Terra、Intelligent UI、Codex、dots、Go、定价视觉、About）。仍缺：**Arena Agent 榜 OG**（下载 403）、**定价页现网价签界面截图**。按要求不自制假 UI。  
- **去味自检：已过（改动 8 处）**。按附则检查正文散文：删了重复预告和套话收尾，合并了同义限定；归因、待核、表格中的数字、URL、模型名与价格未改。
