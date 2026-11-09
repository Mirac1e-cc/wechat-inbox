# 资料包：《模型图鉴》第 1 篇 · DeepSeek

> **写作单**：`2026-11-10-写作单-001.md` 任务 C（先交资料包，**不写成稿**）  
> **选题索引**：`2026-11-10-选题清单.md` 第 7 条（V4.1-Flash-1017 + 自研 Search/Fetch）  
> **核对日期**：2026-11-10（Asia/Shanghai，UTC+8）  
> **口径**：全文「据官方资料整理」；无实测口吻；核不到不写；价格与型号以官方定价页为准。  
> **交付形态**：图鉴六节备料 + 现状（含选题 #7）+ 来源清单 + 自检。

---

## 题头速览

| 项 | 内容（据官方） |
|----|----------------|
| 品牌 | DeepSeek（深度求索） |
| 现状主线 | API / 网页 / App 当前主推 **DeepSeek-V4.1-Flash-1017**（调用名 `deepseek-flash`）；定价页仍列 **DeepSeek-V4-Pro-0813**（`deepseek-v4-pro`） |
| 新动态（选题 #7） | 2026-10-17：Flash-1017 更新；开放自研 **Search / Fetch** API |
| 产品入口 | 官网 https://www.deepseek.com/ ；对话 https://chat.deepseek.com/ ；API https://api.deepseek.com ；文档 https://api-docs.deepseek.com/ |
| 本包用途 | 成稿前备料，非推送正文 |

---

## 1. 一句话定位

据 DeepSeek 官方产品与 API 文档整理：DeepSeek 是深度求索的大模型品牌——**面向对话与 Agent 的高性价比旗舰**（现以 V4.1 Flash 为主力），开源权重与低价 API 并行，并自研搜索引擎向开发者开放 Search / Fetch。

（成稿时可再缩短为：给开发者与普通用户都能上手的国产开源向大模型全家桶，当前主推 V4.1 Flash。）

---

## 2. 版本演进小史（只取改变定位的节点）

> 原则：不写流水账；节点以官方 updates / news 为准。旧价与已下线路由仅作历史定位，不写进「当前价格」。

| 信息日期 | 节点 | 定位变化（据官方） | 来源 |
|----------|------|--------------------|------|
| 2024-09-05 | DeepSeek **V2.5** | Chat 与 Coder 合并升级为统一 V2.5；`deepseek-chat` / `deepseek-coder` 均可访问 | [updates](https://api-docs.deepseek.com/zh-cn/updates) |
| 2024-12-26 | **DeepSeek-V3** | 通用旗舰升级为 V3；接口名仍 `deepseek-chat` | updates；官网研究索引见 deepseek.com |
| 2025-01-20 | **DeepSeek-R1** | 独立「推理模型」线：大规模 RL 后训练；API `deepseek-reasoner`；开放思维链；MIT 开源并允许蒸馏；网页/App「深度思考」 | [R1 新闻](https://api-docs.deepseek.com/zh-cn/news/news250120)；[官网 R1](https://www.deepseek.com/news/deepseek-r1/) |
| 2025-05-28 | **R1-0528** | reasoner 升级；官方称推理增强、幻觉抑制、补齐 JSON / Function Calling | updates |
| 2025-08-21 | **DeepSeek-V3.1** | **混合推理**：同一模型支持思考 / 非思考；强调思考效率与 Agent | updates |
| 2025-12-01 | **DeepSeek-V3.2** | chat / reasoner 均升至 V3.2；另有限时 Speciale（仅思考、无工具调用） | updates |
| 2026-04-24 | **DeepSeek-V4** 系列上架 | API 提供 `deepseek-v4-pro` / `deepseek-v4-flash`；旧名 `deepseek-chat` / `deepseek-reasoner` 计划于 2026-07-24 停用（当时分别指向 Flash 的非思考 / 思考） | updates |
| 2026-07-31 → 08-13 | V4-Flash / **V4-Pro 正式版** | Flash 正式公测；Pro 正式版同步 App / 网页 / API；引入 Responses API、思考强度 low/high/max；峰谷定价自 2026-08-17 生效 | updates；[V4-Pro 新闻](https://api-docs.deepseek.com/zh-cn/news/news260813) |
| 2026-08-21 | V4-Flash-Vision-Exp | 实验性视觉理解；后随 V4.1 下线并由路由承接 | updates |
| 2026-09-10 | **DeepSeek-V4.1-Flash** | **新模型结构系列中的最小尺寸**；原生多模态；API 名改为 `deepseek-flash`；官方称性能/费用/速度上全面超越 V4 Pro，并曾计划有序下线 Pro（同日 updates 又写明应需求继续提供 Pro） | [V4.1 Flash 新闻](https://api-docs.deepseek.com/zh-cn/news/news260910)；updates |
| **2026-10-17** | **V4.1-Flash-1017** + **Search/Fetch** | Flash 升级至 1017；网页/App 同步；API 名与价格不变；开放自研搜索与抓取 API | [updates 2026-10-17](https://api-docs.deepseek.com/zh-cn/updates)；官网首页横幅（核对 2026-11-10） |

**读史提示（成稿可用）**

1. **V 线**：通用对话 → 混合思考 → V4 Agent / 长上下文 → V4.1 新结构 Flash。  
2. **R 线**：以 R1 把「深度思考 / 推理模型」立住；之后能力逐步并入 V 系的思考模式，旧 `deepseek-reasoner` 名已退出当前定价表。  
3. **现状定价页只列两款模型名**：`deepseek-flash`、`deepseek-v4-pro`（见第 4 节）。

---

## 3. 擅长与不擅长

### 3.1 擅长（有官方依据）

| 方向 | 官方依据摘要 | 来源 |
|------|--------------|------|
| Agent / 代码与工具调用 | V4 Pro 正式版强调 Agent；V4.1 Flash / Flash-1017 更新日志突出 Agent、Harness / CodeBuddy 等框架适配；Flash 支持 Tool Calls、Responses API、Anthropic API | news260813；updates 2026-09-10 / 10-17；定价页功能表 |
| 原生多模态（Flash） | V4.1 Flash「具备原生多模态视觉理解」；定价页：`deepseek-flash` **图像理解 = 支持** | news260910；定价页 |
| 长上下文 | 定价页：Flash / Pro 上下文均为 **1M**；最大输出 **384K** | 定价页 |
| 思考强度可调 | 思考 / 非思考；思考档 low / high / max（自 V4 正式版起） | news260813；定价页 |
| 性价比与峰谷 | 官方反复强调成本与峰谷定价；V4.1 Flash 新闻称「更强、更快、更普惠」，并下调 Flash 价 | news260910；定价页 |
| 开源与蒸馏传统 | R1：MIT、可蒸馏；V4.1 Flash：HF 开源链接与技术报告 | news250120；news260910 |
| 自研搜索供给 Agent/RAG | Search 按 query 返回结构化结果；Fetch 返回 Markdown；服务 Agent 与 RAG | [网页搜索与抓取](https://api-docs.deepseek.com/zh-cn/guides/search) |

### 3.2 不擅长 / 官方边界（无实测时只写文档点明项）

| 边界 | 官方表述 | 来源 |
|------|----------|------|
| **Pro 无图像理解** | 定价页：`deepseek-v4-pro` 图像理解 = **不支持** | 定价页（核对 2026-11-10） |
| **FIM 仅非思考** | FIM 补全（Beta）仅非思考模式支持（Flash / Pro 同） | 定价页 |
| **Fetch 依赖目标站** | 「Fetch 的结果受目标站点的可用性和访问策略影响」；403 安全策略拒绝；404 抓不到可用正文等 | Search/Fetch 指南 |
| **Search/Fetch 限速** | 账号级：Search 100 QPS、Fetch 25 QPS；Fetch 另有按域名 QPS | 同上 |
| **峰谷价差** | 高峰价为闲时约 2 倍；工作日北京时间 9:00–12:00、14:00–18:00 为高峰（节假日例外） | 定价页脚注 |
| **V4.1 Flash 定位为「最小尺寸」** | 新结构系列「最小尺寸」；更大参数型号（如未来 V4.1 Pro）仍在路线上——勿把 Flash 写成「全家最大」 | news260910 |
| **无实测素材时禁止写** | 「比某某更好用 / 幻觉多少」等体验句；第三方评测站结论 | 写作纪律 |

**待核（成稿前）**：网页/App 免费额度、是否仍有「专家模式」独立切 Pro、个人会员产品——官网首页未给出与 API 同等清晰的价目表 → 标待核，勿猜。

---

## 4. 怎么用上它

### 4.1 官方入口

| 入口 | 地址 / 说明 | 来源 |
|------|-------------|------|
| 官网 | https://www.deepseek.com/ （对话、API、Harness、App 入口；首页横幅提 Flash-1017 与 Search/Fetch） | 官网，核对 2026-11-10 |
| 网页对话 | https://chat.deepseek.com/ （官网「和 DeepSeek 对话」） | 官网导航 |
| App | 官网「获取 APP」扫码；另有「DeepSeek 应用下载」 | 官网 |
| Harness 桌面端 | 官网「Harness 桌面端」；updates 建议升级至 DeepSeek Harness **0.2.1-rc.1+** 以适配新 Flash | 官网；updates 2026-10-17 |
| API | Base：`https://api.deepseek.com`；Anthropic 格式：`https://api.deepseek.com/anthropic` | 定价页 |
| 文档 | https://api-docs.deepseek.com/ （中文定价、updates、Search/Fetch） | — |
| 开放权重（Flash） | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash （新闻给出；大规模部署需联系官方） | news260910 |

### 4.2 当前在售型号与价格（官方定价页，核对 2026-11-10）

来源：https://api-docs.deepseek.com/zh-cn/quick_start/pricing （同页 `.md` 镜像一致）

#### 模型

| API 模型名 | 模型版本（定价页） | 上下文 | 最大输出 | 图像 | 并发限制（页内） |
|------------|--------------------|--------|----------|------|------------------|
| `deepseek-flash` | **DeepSeek-V4.1-Flash-1017** | 1M | 384K | 支持 | 2500 |
| `deepseek-v4-pro` | **DeepSeek-V4-Pro-0813** | 1M | 384K | **不支持** | 500 |

兼容说明（定价页脚注）：旧名 `deepseek-v4-flash`、`deepseek-v4-flash-vision-exp` 仍可调，但模型已下线，**由 Flash-1017 服务并按 Flash 价计费**。

#### 模型单价（人民币 / 百万 tokens）

| | Flash 闲时 | Flash 高峰 | Pro 闲时 | Pro 高峰 |
|--|------------|------------|----------|----------|
| 输入·缓存命中 | 0.02 元 | 0.04 元 | 0.15 元 | 0.30 元 |
| 输入·缓存未命中 | 1 元 | 2 元 | 4.5 元 | 9.0 元 |
| 输出 | 4 元 | 8 元 | 13.5 元 | 27.0 元 |

峰谷定义（定价页）：北京时间周一至周五（不含中国法定节假日）**9:00–12:00、14:00–18:00** 为高峰；其余含周末与法定节假日全天为闲时；闲时 = 高峰一半。

#### Search / Fetch 单价（选题 #7 必核，已从定价页 + 指南核对）

| API | 计费单位 | 价格 | 计费规则要点 |
|-----|----------|------|--------------|
| **Search** | 每 **1,000** 次**成功**请求 | **5 元** | 按请求次数，不按 token、不按返回条数；仅 HTTP 200 且 `results` **非空**计费 |
| **Fetch** | 每 **1,000** 次**成功**请求 | **5 元** | 仅 HTTP 200 且返回网页正文计费；失败 / 无结果 / 超时不计费 |

- Endpoint：`POST /v1/tools/search`、`POST /v1/tools/fetch`  
- 鉴权：与模型 API 相同 Bearer Key  
- **免费额度**：官方定价页与指南**未给出**单独免费配额 → **待核 / 视为无公开免费额，按成功请求计费**  
- 通过 Harness / Claude Code / Codex 触发的服务端 Search/Fetch **同样按成功次数计费**

#### 扣费

充值余额或赠送余额；两者并存时优先扣赠送。价格可能变动，官方保留调整权。

### 4.3 现状快照（并入选题 #7）

1. **Flash-1017（2026-10-17）**：网页 / App / API 同步；调用仍用 `deepseek-flash`；价格方式不变；官方称性能提升同时缩短任务时间与输出长度。  
2. **自研搜索 API**：网页端与 API 搜索均由自研引擎支撑；开放 Search + Fetch 给 Agent / RAG。  
3. **V4 Pro 仍在定价表**：与 2026-09-10 新闻「计划有序下线 / 路由到 Flash」并存——**以核对日定价页为准：Pro 仍在售、独立计价**；路由是否已撤销以现网行为为准（标待核：是否所有 `deepseek-v4-pro` 请求仍打 Pro-0813）。

---

## 5. 适合谁

| 画像 | 为何适合（据官方能力边界推导，非实测） | 建议入口 |
|------|----------------------------------------|----------|
| 个人学习者 / 普通问答用户 | 官网与 App 提供对话、深度思考、智能搜索入口 | chat.deepseek.com / App |
| 需要看图问答的用户 | Flash 原生图像理解；Pro 官方标明不支持图像 | `deepseek-flash` 或网页 Flash |
| 开发者接 Agent / 编程工具 | Tool Calls、Responses、Anthropic 兼容；官方提 Codex / Harness / 合作方 CodeBuddy 等 | API + Harness |
| RAG / 要实时网页的 Agent | 独立 Search / Fetch，结构化摘要 + Markdown 正文 | `/v1/tools/search`、`/fetch` |
| 成本敏感、可错峰 | 峰谷价差明确；Flash 单价显著低于同页 Pro | 闲时跑批 / Agent |
| 有卡有集群的自托管方 | V4.1 Flash 开源；大规模部署需具备资源并联系官方 | HF + 官方联系渠道 |

---

## 6. 同档对手（公平、可回源，不黑竞品、不编跑分）

> 对比只取**公开规格与价目维度**；基准分数各家自报口径不同，本资料包**不横比跑分**。对手选取与 DeepSeek 常见同场的「长上下文 / 可 API / 有开源或低价路线」产品，成稿时再按当期选题裁剪。

| 维度 | DeepSeek（本包） | Kimi（月之暗面，交叉） | 说明 |
|------|------------------|------------------------|------|
| 核对日主力 API 型号 | `deepseek-flash` = V4.1-Flash-1017；另售 `deepseek-v4-pro` | `kimi-k3.1-pro` / `kimi-k3.1-pro-highspeed` | DeepSeek：[定价](https://api-docs.deepseek.com/zh-cn/quick_start/pricing)；Kimi：[定价说明](https://platform.kimi.com/docs/pricing/chat) / 产品页（本号 Kimi 成稿包已核 2026-11-10） |
| 上下文 | 1M（定价页） | 1M（Kimi 官方） | 同量级 |
| 视觉 | Flash 支持；Pro 不支持 | K3.1 Pro 官方称原生视觉 | 选型号时注意 |
| API 计价形态 | 人民币峰谷 + 缓存命中；Flash 闲时未命中输入 **1 元/MTok**、输出 **4 元/MTok** | 人民币按量；K3.1 Pro 输入约 **13 元/MTok**、输出 **68 元/MTok**（resources/官方整理页，2026-10 核对） | **只比价目形态与数量级，不说谁「更强」** |
| 联网工具 API | 官方自研 Search + Fetch，按次 **5 元/千次成功** | Kimi 侧有插件/工具生态，**不可直接等同**；勿混写 | DeepSeek 指南可回源 |
| 开放权重 | V4.1 Flash 有 HF；R1 历史 MIT | K3.1 Pro 已在 HF（本号 B 成稿再核为已发） | 许可条款各异，部署前读 LICENSE |
| 网页 C 端 | chat.deepseek.com | kimi.com | 产品形态不同 |

**成稿禁令**：不得用第三方 Arena / 自媒体「完胜」句；不得把竞品帮助中心未写的弱点写进 DeepSeek「擅长」。

可选扩展对手（成稿时若需要再开官方页）：通义 / Qwen、智谱 GLM、OpenAI / Anthropic——同样只比公开上下文、价目、是否开放权重。

---

## 7. 配图需求与已落盘

| 编号 | 用途 | 规格 / 说明 | 状态 |
|------|------|-------------|------|
| 1 | 图鉴封面 / 题图 | 官方 API 文档社交图 | **已落盘** `assets/2026-11-10-DeepSeek-图鉴/deepseek-social-card.jpeg`（3836×2038 JPEG） |
| 2 | 官网首页横幅 | www.deepseek.com 现网截图（含 Flash-1017 文案） | **未截**；链接 https://www.deepseek.com/ |
| 3 | 定价页表格 | 定价页现网截图（两模型 + Search/Fetch） | **未截**；链接定价页 |
| 4 | Search/Fetch 示意 | 文档页结构图或自绘流程图（非实测界面） | **缺** |
| 5 | HF / 开源页 | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | **未下** |

官方图直链备份：`https://api-docs.deepseek.com/zh-cn/img/deepseek-social-card.jpeg`

---

## 8. 完整来源清单

| # | 用途 | 链接 | 信息日期 | 核对日期 |
|---|------|------|----------|----------|
| 1 | 更新日志（Flash-1017、Search、历史节点） | https://api-docs.deepseek.com/zh-cn/updates | 最新条目 2026-10-17 | 2026-11-10 |
| 2 | 模型与价格（在售型号、峰谷、Search/Fetch 价） | https://api-docs.deepseek.com/zh-cn/quick_start/pricing | 页内现网 | 2026-11-10 |
| 3 | 同上英文/Markdown 镜像 | https://api-docs.deepseek.com/zh-cn/quick_start/pricing.md | 同上 | 2026-11-10 |
| 4 | 网页搜索与抓取指南（计费规则、QPS、错误码） | https://api-docs.deepseek.com/zh-cn/guides/search | 核对日读取 | 2026-11-10 |
| 5 | Search API Reference | https://api-docs.deepseek.com/zh-cn/api/search | 核对日读取 | 2026-11-10 |
| 6 | Fetch API Reference | https://api-docs.deepseek.com/zh-cn/api/fetch | 核对日读取 | 2026-11-10 |
| 7 | V4.1 Flash 发布新闻 | https://api-docs.deepseek.com/zh-cn/news/news260910 | 2026-09-10 | 2026-11-10 |
| 8 | V4-Pro 正式版新闻 | https://api-docs.deepseek.com/zh-cn/news/news260813 | 2026-08-13 | 2026-11-10 |
| 9 | R1 发布新闻 | https://api-docs.deepseek.com/zh-cn/news/news250120 | 2025-01-20 | 2026-11-10 |
| 10 | 官网 R1 | https://www.deepseek.com/news/deepseek-r1/ | 2025-01-20 | 2026-11-10 |
| 11 | 官网首页（产品入口与横幅） | https://www.deepseek.com/ | 核对日现网 | 2026-11-10 |
| 12 | V4.1 Flash 开源（新闻给出） | https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash | 新闻 2026-09-10 | 2026-11-10（链接据新闻；未逐文件核仓） |
| 13 | 同档交叉·Kimi 价目（仅对手表） | https://www.kimi.com/resources/kimi-k3-1-pro-pricing 等 | 见本号 Kimi 成稿包 | 2026-11-10 |

公开 X：本回合检索未见可稳定引用的 DeepSeek 官方账号一手帖；**不以第三方用户体验帖入库**。

---

## 9. 待核项与自检

### 待核项

1. 网页 / App **免费额度、频率限制、是否收费会员**——官网未给 API 级价目表。  
2. 现网对话是否仍提供独立「专家模式 = Pro」——历史新闻有写，首页现网文案以 Flash-1017 为主 → 需成稿前打开 chat 页确认（不登录可核的公开说明优先）。  
3. `deepseek-v4-pro` 请求是否仍落到 **Pro-0813**（对照 2026-09-10「路由到 Flash」旧计划）。  
4. Search/Fetch **是否存在未公示的赠送额度**——定价页与指南均未写，暂按「无公开免费额」。  
5. HF 仓库文件完整性与 License 全文——新闻有链接，本包未做仓库深核。  
6. 英文定价页美元表与人民币表是否长期 1:1 换算——成稿若面向海外读者需再开英文 pricing。

### 自检

- **来源是否齐**：是。updates、定价、Search/Fetch、V4.1/V4-Pro/R1 新闻、官网入口均已回源。  
- **待核剩几条**：**6** 条。  
- **配图**：已落盘 **1** 张社交封面；缺官网横幅截图、定价页截图、Search/Fetch 示意、HF 页图（共约 **4** 张待补）。  
- **价格与 Search/Fetch**：**已从官方定价页核对**（人民币表 + 指南计费规则）；单价见 §4.2。  
- **未写成稿、未推 GitHub**。
