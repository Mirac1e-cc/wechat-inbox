# 成稿包：Kimi K3.1 Pro（写作单 #001-B）

> 核对日期：2026-11-10（Asia/Shanghai，UTC+8）  
> 口径：据官方资料整理；无实测口吻。  
> 交付形态：推送包（可直接发表正文 + 配图需求 + 来源清单）

---

## 1. 标题备选（3 个）

1. **【建议主标题】Kimi K3.1 Pro 来了：3D Make 普通人怎么玩，会员与 API 怎么选**
2. 一句话做 3D 网页、模型和打印件？Kimi K3.1 Pro 官方能力速览
3. K3.1 Pro 权重已上 Hugging Face：网页 / App / Work / Code / API 入口与额度

---

## 2. 作者

刀哥

---

## 3. 一句摘要

据月之暗面官方，Kimi K3.1 Pro 是 K3.1 系列首个旗舰（宣称约 3 万亿级参数、100 万上下文），网页与 App 上线 3D Make；完整权重已在 Hugging Face 开放——本文只整理怎么用、怎么订，不堆跑分。

---

## 4. 完整正文（可直接发表）

### 先说结论

据月之暗面 / Kimi 官方资料（产品官宣更新于 **2026-10-24**；开放权重仓库于核对日 **2026-11-10** 可访问）：

1. **模型定位**：Kimi K3.1 Pro 是 K3.1 系列第一个模型；官宣称「迄今能力最强的 **3 万亿级**参数模型」，支持 **100 万**上下文；同步有高速版 **Kimi K3.1 Pro Highspeed**（同等智能，输出约 **2～3 倍**速）。  
2. **普通人入口**：`kimi.com`、Kimi App、Kimi Work、Kimi Code、Kimi API；网页与 App 同步上线 **3D Make**（对话做 3D 网页 / 建模 / 打印准备文件）。  
3. **开放权重再核结论（本次必核）**：**已发布**。官方组织仓库：[`https://huggingface.co/moonshotai/Kimi-K3.1-Pro`](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)（核对日 2026-11-10 可打开；模型卡自称 open-weight，总参约 **2.8T**）。官宣原文曾写「完整模型权重将于 **11 月 4 日前**发布」——该句在新闻页与部分 API 文档仍未改掉，但 HF 仓库已上线；另有官方微博经媒体转载称「昨晚……已在 Hugging Face 开放下载」（转载标注约 2026-11-05）。**不以第三方测评站为准。**  
4. **怎么付钱**：会员走国内 Go～Ultra（帮助中心价目截图于 2026-10-19）；API 按量另计，**会员费不含 API**。

下文展开「3D Make 怎么玩」和「各端额度」，参数只保留定位所需的一两项。

---

### 一、它是什么（只留定位参数）

| 项 | 官方说法 | 来源 |
|----|----------|------|
| 系列位置 | K3.1 系列第一个模型 | [新闻页](https://www.kimi.com/news/kimi-k3-1-pro)（更新于 2026-10-24） |
| 规模 | 「3 万亿级」；HF 模型卡写总参 **2.8T**、激活约 **104B**（MoE） | 新闻页；[HF 模型卡](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) |
| 上下文 | **100 万** token（1,048,576） | 新闻页；API / Code 文档 |
| 高速版 | Highspeed，约 **2～3 倍**输出速度 | 新闻页 |
| 产品入口 | kimi.com、App、Work、Code、API | 新闻页 |
| 权重许可 | *Kimi K3.1 Pro License*（商用有门槛条款，详见仓库 LICENSE） | HF LICENSE |

跑分表官宣里很多，本号口径是「普通人用得上」——正文不展开排行榜。

---

### 二、开放权重再核（写作单要求）

| 核对项 | 结果 | 依据（核对 2026-11-10） |
|--------|------|-------------------------|
| 官宣计划 | 将于 **2026-11-04 前**发布完整权重 | [kimi.com/news/kimi-k3-1-pro](https://www.kimi.com/news/kimi-k3-1-pro)；[API 快速入门](https://platform.kimi.com/docs/guide/kimi-k3-1-pro-quickstart) 文内同句（文档或未刷新） |
| 是否已实际上线 | **是** | Hugging Face：`moonshotai/Kimi-K3.1-Pro` 可访问；含 README、config、多片 `safetensors`、LICENSE |
| 官方传播交叉 | 官方微博经新浪等转载：「昨晚，Kimi K3.1 Pro 模型权重已在 Hugging Face 开放下载」（转载页标注约 **2026-11-05**） | 转载页仅作交叉；主证据仍为 HF 官方组织仓库 |
| 自托管门槛 | 仓库体量约 **1.56 TB** 量级（HF 页面展示）；普通人优先用网页 / App / API，不必自己拉权重 | HF 仓库页 |

**给读者的实用结论**：想「玩玩模型」→ 打开 kimi.com / App；想「本地部署」→ 去 HF 看 LICENSE 与推理配方（vLLM / SGLang 等，见模型卡），并自行评估硬件与合规。

---

### 三、3D Make：普通人怎么玩

据 [3D Make 功能介绍](https://www.kimi.com/help/3d-make/3d-make-overview)（核对 2026-11-10）：**由 Kimi K3.1 Pro 驱动**；用自然语言或上传草图/参考图，在 Kimi 里完成预览、修改、导出——**不要求你会建模软件或写代码**。

#### 1）三种创作类型

| 类型 | 适合干什么 | 注意 |
|------|------------|------|
| **3D 网页** | 可交互 3D 页面、网页小游戏 | 网页里能看见模型 ≠ 另有一份独立模型文件 |
| **3D 建模** | 做三维对象，展示或继续加工 | 下载后用目标软件打开检查 |
| **3D 打印** | 生成供打印准备的模型文件 | **不会直接连打印机**；需自行切片、选材料与设备参数 |

#### 2）从哪进

1. 专属页：`https://www.kimi.com/make3d`（Chrome / Safari / Edge 等）  
2. 官网输入框功能栏或左侧边栏「3D Make」  
3. iOS / Android / 鸿蒙官方 App 内进入 3D Make  

#### 3）五步流程（官方步骤摘要）

1. **选类型**（3D 网页 / 建模 / 打印；不选时模型会猜，发送前建议确认）  
2. **描述想法**，或点「+」上传参考图；要特定格式请写清楚  
3. **生成后预览**：可旋转、缩放；网页作品建议点一点页面交互  
4. **多轮修改**：每轮改少量重点，并说明哪些部分保持不动  
5. **导出 / 分享**：模型文件、视频或实况照片、分享链接（访问范围以分享界面为准）  

官方还提供精选模板与「做同款」（复用官方 Prompt 再改）。打印路径 FAQ 写明：预览正常 ≠ 可直接上机；需在 Blender 等检查，再用 Cura / PrusaSlicer / Bambu Studio 等切片。

#### 4）额度

3D Make 走 **Kimi 统一额度**，生成与修改都会扣；查看路径：网页「设置 → 订阅」，App「我的 → 会员计划 → 订阅」。复杂作品可能要几分钟，官方提醒勿重复狂点同一任务。

更细的内部工作流与案例见学院文 [如何用 Kimi 做出更好的 3D 作品](https://www.kimi.com/academy/3d-tutorial)（更新于 2026-10-29）——文中区分：简单单件可用网页 3D Make；要驱动本机 Unity / Unreal 等可用 Work / Code。

---

### 四、日常还能拿它干什么（官方能力向，非实测）

据官宣与产品文档整理的**可用方向**（案例均为官方演示口径）：

- **写代码 / 搭小项目**：新闻页称可从小修到从零搭项目；游戏引擎（Unity、Unreal、Godot）与前端、Three.js 等在官方案例中出现。落地入口优先 **Kimi Code**（需对应会员档，见下节）。  
- **长文档与办公研究**：Office 文件处理、深度研究等在付费会员权益中列出（帮助中心）。  
- **金融类长流程**：官宣强调金融研究与建模工作流能力——适合「丢一叠材料让它整理推演」的场景；重要数字仍须人工回源核对（官方亦提示幻觉压力测试不等于日常错误率）。  
- **API 接入自己的应用**：模型 ID `kimi-k3.1-pro` / `kimi-k3.1-pro-highspeed`；始终开思考，可用 `reasoning_effort`：`low` / `high` / `max`。

---

### 五、各端怎么订、额度怎么算（核到多少写多少）

#### 1）网页 / App / Work（会员）

据帮助中心 [会员套餐价格](https://www.kimi.com/help/membership/membership-pricing)、[会员体系介绍](https://www.kimi.com/help/membership/membership-overview)（价目截图标注 **2026-10-19**；核对 2026-11-10），以及官方整理页 [Kimi K3.1 Pro 价格](https://www.kimi.com/resources/kimi-k3-1-pro-pricing)（更新于 **2026-10-26**）：

**价格（国内新套餐，人民币）**

| 套餐 | 连续包月 | 连续包年总价 | 年付折合每月 |
|------|----------|--------------|--------------|
| Go | ¥49/月 | ¥468/年 | ¥39/月 |
| Plus | ¥99/月 | ¥948/年 | ¥79/月 |
| Pro | ¥199/月 | ¥1,908/年 | ¥159/月 |
| Max | ¥699/月 | ¥6,708/年 | ¥559/月 |
| Ultra | ¥1,399/月 | ¥13,428/年 | ¥1,119/月 |

最新购买资格与完整权益以 **会员购买页现网**为准。

**与 K3.1 Pro 相关的门槛（据 resources 对照表）**

| 能力 | Free | Go | Plus | Pro / Max / Ultra |
|------|------|-----|------|-------------------|
| K3.1 Pro（网页与 Work） | **有限使用** | 包含 | 包含 | 包含 |
| K3.1 Pro Highspeed（网页、Work、Code） | — | — | — | **包含** |
| Kimi Code | — | — | 包含 | 包含 |
| Agent 额度倍率（相对表述） | 基础 | 更多 | 2× | 4× / 14× / 28× |

**共用规则（帮助中心）**

- 会员功能共享 **月度额度池**，按实际 token 用量扣；一项用光会影响其他项。  
- 按月刷新，**不结转**。  
- 新套餐 Plus 及以上：Kimi Code 有滚动 **5 小时**频率窗口，**无周限额**；旧套餐另有周限额。  
- 额度查看：Web「设置 → 订阅」；App「会员计划 → 订阅」。  
- 用尽后：等刷新、升级，或买**加油包**按量续用。

官方选档建议（帮助中心）：Go＝日常文档/PPT/深度研究/建站（无 Code）；Plus＝要 Code 与 Agent 集群；Pro＝要目标模式、Kimi Claw 与更多额度；Max / Ultra＝更重度。

#### 2）Kimi Code

据 [Kimi Code 模型配置](https://www.kimi.com/code/docs/kimi-code/models.html)（核对 2026-11-10）：

- 新套餐：**Plus 及以上**可用 `k3.1-pro`；**Pro 及以上**才可用 Highspeed，且 **1M 上下文**面向高档位（表内写 Pro 及以上支持 1M）。  
- 高速版消耗约为普速约 **2 倍**。  
- 仅支持思考模式，关思考会被拒。  
- 建议**新建会话**再切到 K3.1 Pro，勿在旧模型长会话里硬切。

#### 3）Kimi API（与会员分开）

据 [API 快速入门](https://platform.kimi.com/docs/guide/kimi-k3-1-pro-quickstart)、[账号与财务](https://platform.kimi.com/docs/guide/account-and-payments)、resources 价格页（核对 2026-11-10）：

- 按量计费；**最低充值 ¥10** 后可调；新用户认证赠送 **¥15** 代金券可用于标准版 K3.1 Pro，**不可**用于 Highspeed。  
- **会员费不含 API 用量**。  
- 国内页整理的单价（每 1M tokens，resources 核对标注 2026-10-24；以开放平台定价页为准）：  

| 模型 | 输入 | 输出 | 缓存命中 | 缓存写入 5min | 缓存写入 1h |
|------|------|------|----------|---------------|-------------|
| `kimi-k3.1-pro` | ¥13 | ¥68 | ¥1.30 | ¥13 | ¥26 |
| `kimi-k3.1-pro-highspeed` | ¥26 | ¥136 | ¥1.30 | ¥26 | ¥52 |

- Batch API：标准价约 **60%**（平台定价说明）。  
- 平台定价页表格多为动态组件，成稿推送前建议再打开 [`platform.kimi.com/docs/pricing/chat`](https://platform.kimi.com/docs/pricing/chat) 人眼核一次数字。

#### 4）阿里云百炼（交叉）

百炼帮助中心有 `kimi-k3.1-pro` 上架记录（约 2026-10-24 / 11-05）——**仅作渠道交叉**；产品事实与价格仍以月之暗面官方为准。

---

### 六、写给普通人的「怎么选」

1. **只想做个 3D 小网页 / 小摆件模型**：打开 `kimi.com/make3d`，Free「有限使用」可先试；常用再上 Go／Plus。  
2. **要写代码、用 Kimi Code**：至少 **Plus**；要 Highspeed 或满 1M 上下文，看官方表对准 **Pro+**。  
3. **接进自己的产品**：走 API 按量，别指望会员额度顶 API。  
4. **自己部署**：HF 已放权重，但体积与算力门槛高；先读 LICENSE。  
5. **重要结论（财务、结构安全、打印件）**：AI 输出仅供参考，打印前必须本地检查——这是官方反复强调的。

---

### 七、信息时效

产品官宣主文更新于 **2026-10-24**；会员价目帮助中心截图标注 **2026-10-19**；3D 学院文 **2026-10-29**；开放权重仓库于 **2026-11-10** 核对可访问。下单或部署前请再打开会员页、API 定价页与 HF 仓库确认一眼。

---

## 5. 封面与正文配图需求清单

合集封面已定版科技风 **1080×1440**；单篇封面沿用科技风，不用魔兽牌匾风。

| 编号 | 用途 | 尺寸 | 内容 | 来源 | 工作区 |
|------|------|------|------|------|--------|
| 封面 | 单篇封面底图 | 2133×1200（再裁 1080×1440） | K3.1 Pro 官方新闻封面视觉 | 新闻页 OG | **已落盘** `assets/2026-11-10-Kimi-K3.1-Pro/k3-1-pro-cover.webp` |
| 图1 | 正文·3D Make | 2000×1125 | 3D Make 功能介绍头图 | 帮助中心 | **已落盘** `…/3d-make-overview.png` |
| 图2 | 正文·会员价目 | 1564×570 | 连续包年价目示意 | 帮助中心（截图标注 2026-10-19） | **已落盘** `…/membership-plans-annual.jpg`；另存月付示意 `membership-plans-monthly.jpg` |
| 图3 | 正文·开放权重 | 1200×648 | HF 模型卡社交图 | Hugging Face | **已落盘** `…/hf-k3-1-pro-og.png` |
| 图4 | 正文·3D Make 界面 | 建议通栏 | `kimi.com/make3d` 公开界面（无个人隐私） | 官方产品页现网截图 | **未截**——推送前建议补一张并注明截图时刻 |
| 图5 | 可选·模板案例 | — | [3D Make 精选案例](https://www.kimi.com/showcases/3dmake) 卡片 | 官方 showcases | **未下载** |

---

## 6. 完整来源清单

| # | 事实用途 | 链接 | 信息日期 | 核对日期 |
|---|----------|------|----------|----------|
| 1 | 产品发布、参数定位、入口、权重计划句、3D Make 上线句 | https://www.kimi.com/news/kimi-k3-1-pro | 更新于 2026-10-24 | 2026-11-10 |
| 2 | 开放权重仓库与模型卡 | https://huggingface.co/moonshotai/Kimi-K3.1-Pro | 仓库已上线（HF 显示近期提交） | 2026-11-10 |
| 3 | 许可证 | https://huggingface.co/moonshotai/Kimi-K3.1-Pro/blob/main/LICENSE | 随仓库 | 2026-11-10 |
| 4 | API 能力、访问条件、思考模式 | https://platform.kimi.com/docs/guide/kimi-k3-1-pro-quickstart | 文内仍含「11 月 4 日前发布」旧句 | 2026-11-10 |
| 5 | API 计费概念 / Batch 60% | https://platform.kimi.com/docs/pricing/chat | 动态页 | 2026-11-10 |
| 6 | 新用户代金券等 | https://platform.kimi.com/docs/guide/account-and-payments | 核对日读取 | 2026-11-10 |
| 7 | 会员价格与额度规则 | https://www.kimi.com/help/membership/membership-pricing | 截图标注 2026-10-19 | 2026-11-10 |
| 8 | 会员权益总览 | https://www.kimi.com/help/membership/membership-overview | 同上 | 2026-11-10 |
| 9 | K3.1 Pro 与各档对照、API 单价整理 | https://www.kimi.com/resources/kimi-k3-1-pro-pricing | 更新于 2026-10-26 | 2026-11-10 |
| 10 | Kimi Code 模型门槛 | https://www.kimi.com/code/docs/kimi-code/models.html | 核对日读取 | 2026-11-10 |
| 11 | Code 会员与 5 小时窗口 | https://www.kimi.com/code/docs/kimi-code/membership.html | 核对日读取 | 2026-11-10 |
| 12 | 3D Make 功能与步骤 | https://www.kimi.com/help/3d-make/3d-make-overview | 核对日读取 | 2026-11-10 |
| 13 | 3D Make FAQ（不直连打印机等） | https://www.kimi.com/help/3d-make/3d-make-faq | 核对日读取 | 2026-11-10 |
| 14 | 3D 教程 / 入口选择 | https://www.kimi.com/academy/3d-tutorial | 更新于 2026-10-29 | 2026-11-10 |
| 15 | 百炼上架交叉 | https://help.aliyun.com/zh/model-studio/newly-released-models | 约 2026-10-24 / 11-05 条目 | 2026-11-10 |
| 16 | 官方微博权重声明转载（交叉） | https://www.sina.cn/news/detail/5361857965590958.html | 转载标注约 2026-11-05 | 2026-11-10；**主证据仍为 HF** |

---

## 7. 待核项与自检

### 待核项

1. **新闻页 / API 快速入门**仍写「权重将于 11 月 4 日前发布」——与 HF 已上线并存，属文案滞后；已在正文说明。  
2. **Free「有限使用」的具体次数/token 上限**：官方表仅写「有限使用」，无公开绝对数字 → 待核，以订阅页实时为准。  
3. **API 单价现网表**：resources 页有明确数字；`platform.kimi.com/docs/pricing/chat` WebFetch 未抽出表格单元格 → 推送前建议人眼再核定价页。  
4. **make3d 现网界面截图**：未截取。  
5. **HF 首次公开精确到分钟的官方一手帖**：X 搜索未命中；已用 HF + 微博转载交叉，若需更严可再补官方微信/微博原帖截图。

### 自检

- **来源是否齐**：是。产品、3D Make、会员、Code、API、权重均回源官方页或官方 HF 组织仓库。  
- **待核剩几条**：**5** 条。  
- **配图**：已落盘 **5** 个文件（封面 webp、3D 头图、会员年/月价目图、HF OG）；仍缺 **make3d 现网界面截图**、精选案例卡片图（可选）。

### 开放权重再核（汇报用一句话）

**已发布**：`https://huggingface.co/moonshotai/Kimi-K3.1-Pro`（2026-11-10 可访问）；兑现官宣「11 月 4 日前」计划；部分官网文案未改。
