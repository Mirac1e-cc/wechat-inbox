# 来源逐条核对：热修与官方数据

核对日期：2026 年 11 月 19 日（Asia/Shanghai）。所有展示发布时间均为北京时间；WebFetch 的「几小时前」不作精确发布日期。没有检索 NGA。

## 官方热修与国服范围

- **S1 暴雪新闻站**：[11 月 17 日活文章](https://news.blizzard.com/en-us/article/24315281/wow-forever-hotfixes-november-17-2026)。JSON 发布时间与修改时间均为北京时间 2026-11-18 11:23；2026-11-19 回源，最新仍为 November 17。正文资料保存 `_src/bnet.html` / `bnet.txt`（证据留本地，不进 zip）。
- **S2 Kaivax 原始蓝帖**：[第 12 楼](https://us.forums.blizzard.com/en/wow/t/2403040/12)。北京时间 2026-11-18 11:24 发布、未另修订，staff 标志为 true；已读完整楼层，与 S1 的 11-17 条目一致。未收与本题无关的后来话题。
- **S3 国服官方活页**：[在线修正](https://wow.blizzard.cn/news/24315281/index.html)。2026-11-19 现查，标题仍 11 月 6 日，署名日期和正文最新为 11 月 12 日。没有 11-17 本批，不能说整个正文停在 11-6，也不能据此认定国服游戏未部署。该页已有「辛德拉」译名。

## 11-17 条目定位与数据边界

1. **黑上恢复难度**：S1 / S2 Dungeons → Upper Blackrock Spire：「Corrected an issue causing enemy health and damage to be significantly lower than intended.」开发说明是恢复预定难度、需要 full complement of diligent players。没有百分比、首领数值或变更队伍上限。
2. **睡袋三条**：S1 / S2 Camping。不能骑乘睡、可像猎人陷阱选地点、显示 Resting aura。没有新经验 / 速度数字。
3. **增益与 Flurry**：S1 / S2 Classes。Might of Stormwind / Warchief's Blessing 死亡移除、不加非玩家；Flurry 不再被风怒图腾攻击错误消耗。
4. **Soulforge**：S1 / S2 Items → Paladin：「Soulforge Armor (upgraded Dungeon Set for tanks) now has Spell Power (was Strength).」开发说明「Paladin tanks favoring Spell Power as their primary stat for dealing damage」。**不是官方说治疗向**。没给逐件属性、手套智力或全套合计，未补异常数字。
5. **法杖**：S1 / S2 Items 原样列「25 Stamina, 25 Intellect, 74 Spell Power from Weapon damage」；Escape Plan 射程 / 伤害纠错无数值，Night Watchman's Torch 可被暗牧持有。
6. **专业**：S1 / S2 Professions 与 Blacksmithing、Herbalism：旧板条箱交付、The Old Ways 配方补领、Bronze Mace 绑定、Golden Scale Gauntlets 文书指向、Cultivation / Mageroyal、Her World 追踪条件。
7. **PvP / UI / 任务**：S1 / S2 对应段落，The Battle for Alterac Valley 要求 58 级；屏蔽名单持久性；辛德拉共享目标 / 全队掉落与刷新；Agamaggan's Blood 不再地下城任务、可在 Razorfen Downs 外精英区完成。未加任务掉率和刷新倍率。

## X 一手：已直接读取，不依赖二手新闻翻译

- **S4 @Warcraft 原帖**：[2122842235263680581](https://x.com/Warcraft/status/2122842235263680581)，北京时间 2026-11-18 08:00:04。通过已连接 X 的按 ID 读取能力取到正文、作者与三张 media URL，随后下载官方媒体原图，并逐张目视数字 / 标签。原帖正文只说持续破纪录，没有列统计窗口。
- 图 1：[官方媒体原图](https://pbs.twimg.com/media/HXXZwX6WcAANAJ4?format=jpg&name=orig)，1080×1440：15,160,147 **characters created**；1,480,343,357 **quests completed**；9,786,925,806 **enemies defeated**。
- 图 2：[官方媒体原图](https://pbs.twimg.com/media/HXXZwleW0AAYoaB?format=jpg&name=orig)，1080×1440：140,764 **guilds created**；28,696,386 **camping items used**；71,309,889 **parties formed**。
- 图 3：[官方媒体原图](https://pbs.twimg.com/media/HXXZw06WQAAvHaT?format=jpg&name=orig)，1080×1440：**Archmage Arugal / deadliest boss**；28,938,569 **PvP kills**；196,851,761 **player deaths**。
- **S5 Holly Longdale**：[原帖](https://x.com/TheWindstalker/status/2122843024791314913)，北京时间 2026-11-18 08:03:12。确切句子：「Another fun statistic for you! #WoWForever has more people playing weekly than we've seen in World of Warcraft in 15 years!」。**主语是 #WoWForever；历史比较对象是 World of Warcraft；没有绝对周活数字。**不改写为整个 WoW 目前的周活总数，也不凭该句认定同口径的全部版本合计。地区、去重和窗口仍缺。
- X 的 WebFetch 返回 403，但之后使用已连接的一手 X 读取成功；没有抓登录 cookie 或私有接口。三张媒体原图均取到，非二手截图。

## 站内回源（全部 2026-11-19 现查）

- [Soulforge 旧稿](https://4evrcore.cn/wp/soulforge-darkmoon-item-changes/)：「未列官方」「神圣骑治疗向」「手部智力待核」。与 S1 新说明冲突，仅列 SELF-CHECK，未改旧页。
- [副本专区](https://4evrcore.cn/wp/instances/)：黑上 10 人、58–60；黑下 54–60；黑石深渊 50–60，沿用站内。
- [门禁与钥匙](https://4evrcore.cn/wp/attunements-keys/)：达基萨斯将军中文、晋升印章风险项。
- [睡袋](https://4evrcore.cn/wp/cozy-sleeping-bag/)：舒适的睡袋中文。
- [商人青睐](https://4evrcore.cn/wp/merchants-favor-guide/)：遭劫的板条箱叫法来自 11-15 已回源包；本次专业修正由 S1 直接核对。
- [11 月 16 日热修](https://4evrcore.cn/wp/hotfixes-nov-16/)：已经发布的职业部分只作为范围边界，不重写。

## 新闻配图出处

- [S1 文章官方头图](https://bnetcmsus-a.akamaihd.net/cms/blog_header/2o/2OT6OCC1ADEM1789963421279.png)，2400×1350，包内存原图与 900×383 裁切封面。通用营地图，不冒充黑上实景。
- S4 三张统计原图完整入包，各附 900×1200 等比公众号版；不裁统计标签、不改数字。
