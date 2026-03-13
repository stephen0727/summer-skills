# Summer 的 Skills / Summer's  Skills

[English](#english) | [中文](#中文)

---

## 中文

### 📖 简介

这是一个精心打造的 Claude Code Skills 集合，旨在提升软件开发和产品管理的效率。每个 Skill 都经过实战验证，帮助你在日常工作中更加高效。

可安装到 **Cursor、Claude Code、Codex、OpenClaw** 等 Agent 工具的 skills 目录使用。与普通 Prompt 的区别：Agent 会根据 `description` 中的关键词与触发场景**自动判断是否调用**，无需每次手动选择。

### 🖼️ 效果预览

**答辩 PPT（[pptgen-drawio](./pptgen-drawio)）**

<table><tr>
<td><img src="preview/paper-defense1.jpg" alt="答辩PPT预览1"/></td>
<td><img src="preview/paper-defense2.jpg" alt="答辩PPT预览2"/></td>
</tr></table>

**公众号封面（[wechat-article-writer](./wechat-article-writer)）**

![公众号封面预览](preview/wechat_cover.drawio.png)

### ✨ 包含的 Skills

#### 🎨 [配图助手](./image-assistant) (Image Assistant)
**描述**: 把文章/模块内容转成统一风格、少字高可读的 16:9 信息图提示词

**适用场景**:
- 文章需要配图但不知道怎么设计
- PPT、海报、社媒图需要统一风格
- 内容太多字，想要更趣味、更好读的视觉呈现
- 需要批量生成配图提示词

**核心功能**:
- 📋 需求澄清：挖掘内容、场景、受众和字数偏好
- 🗂️ 配图规划：拆分内容，定义图清单（几张图/每张讲什么）
- ✍️ 文案定稿：逐字定稿"图上写什么"（Copy Spec）
- 🎯 提示词封装：生成可复制的生图提示词，支持批量出图
- 🔄 迭代润色：根据反馈减字、换隐喻、提升可读性

**触发方式**:
```
这段内容做个图/配几张图
给我两张出图提示词
字太多不好看，帮我更趣味、更好读
/image /配图 /出图
```

---

#### 🧠 [思维挖掘助手](./thought-mining) (Thought Mining)
**描述**: 通过对话帮助你把脑子里的零散想法倒出来、记录下来、整理成文章

**适用场景**:
- 想写文章但思路不清晰
- 有很多零散想法需要整理
- 需要从混乱的思考中提炼核心观点

**核心功能**:
- 📝 思维挖掘：引导式对话，帮你说出并记录想法
- 🎯 选题确定：从洞察中找到核心观点
- ✅ 观点验证：联网搜索验证理解是否正确
- ✍️ 写作辅助：逻辑检查、文字润色、金句提炼
- 🔍 最终审核：发布前的全面检查

**触发方式**:
```
我想写一篇关于 XX 的文章
帮我整理一下我的想法
/thought-mining
```

---

#### 📋 [PRD 文档撰写助手](./prd-doc-writer) (PRD Doc Writer)
**描述**: 以故事驱动的方式，帮助你撰写和迭代完善 PRD/需求文档

**适用场景**:
- 需要撰写产品需求文档
- 想用用户故事的方式梳理需求
- 需要用图表减少需求歧义

**核心功能**:
- 🗺️ 用户旅程地图：构建宏观业务流程
- 📖 故事化需求：每个功能点都是一个完整的用户故事
- 🎨 ASCII 线框图：可视化页面布局
- 📊 Mermaid 图表：流程图/状态图/时序图
- ✅ 阶段性确认：确保每一步都与你达成共识

**触发方式**:
```
帮我写 PRD
梳理需求文档
/prd-doc-writer
```

---

#### 🎨 [新功能设计探索](./design-exploration) (Design Exploration)
**描述**: 新功能设计探索流程。从模糊想法产出可交付的设计参考文档，作为 PRD 阶段的输入

**适用场景**:
- 有模糊想法要做新功能/新模块
- 需要批量探索多种设计方案
- 需要完整覆盖页面状态（正常/异常/边界）
- 需要产出设计稿作为开发参考

**核心功能**:
- 📝 需求收敛：明确做什么、不做什么、边界在哪
- 🔍 技术调研：了解外部数据约束和技术可行性
- 🎨 ASCII 批量探索：一次出 5-8 个方案供选择
- 📐 HTML 设计稿：基于选定方案产出 mockup
- 📊 全状态覆盖：正常态/加载态/空态/错误态/边界情况
- 📋 交互规则表：前端开发直接对照实现

**触发方式**:
```
我想做个新功能
帮我设计一下这个模块
出个设计方案
/design-exploration
```

---

#### 🔄 [需求变更工作流](./req-change-workflow) (Requirement Change Workflow)
**描述**: 标准化需求变更流程，避免改需求时的混乱和代码崩溃

**适用场景**:
- 需要修改现有功能的需求
- 改需求时经常出现意外 bug
- 需要一个可靠的变更验证流程
- 特别适合 Chrome 扩展等复杂项目

**核心功能**:
- 📝 需求澄清：锁定变更范围和验收标准
- 🔍 现状基线：从代码中确认当前行为
- ⚠️ 影响评估：评估风险和变更范围
- 🎯 设计方案：提出新设计并获得批准
- 🛠️ 最小化实现：小范围、局部化的代码修改
- ✅ 回归测试：固定的验证清单
- 📚 文档维护：决策日志和文档更新

**触发方式**:
```
改需求/需求变更
调整交互/改功能
/req-change-workflow
```

---

#### 📚 [课程构建器](./lesson-builder) (Lesson Builder)
**描述**: 通过讨论驱动的方式，帮助你快速完成课程大纲和课件

**适用场景**:
- 需要快速备好一节课
- 已有清晰想法，需要整理成文档
- 需要迭代现有课程大纲
- 准备培训或教学内容

**核心功能**:
- 💭 共创大纲：通过讨论挖掘想法，形成清晰课程框架
- 📖 课件撰写：基于大纲写出完整课件内容
- 🎯 框架优先：先确认框架再写细节，避免返工
- ⚡ 快速迭代：支持快速共创和严格确认两种模式
- 📋 最少文档：只产出需要的内容（大纲/课件/补充材料）

**触发方式**:
```
备课
做课件/准备课程
/lesson-builder
```

---

#### 📦 [需求池管理](./backlog-manager) (Backlog Manager)
**描述**: 需求池管理。随时抛出想法/痛点，AI 负责追问、整理、合并、归档。准备开新版本时协助筛选。痛点驱动，不做提前排期

**适用场景**:
- 随时记录产品想法和功能需求
- 管理零散的需求，避免遗忘
- 准备新版本时挑选要做什么
- 整理和清理过时的需求

**核心功能**:
- 📝 收集：追问痛点、频率、绕过方式，确认理解
- 📂 归类：检查合并可能，判断状态（可以做了/需要想想/先放着）
- 🧹 整理：定期清理过时条目，升档想清楚的条目
- 🎯 筛选：基于频率/可绕过性/ROI 分析候选需求
- ✅ 归档：标记已完成，更新依赖关系

**触发方式**:
```
我想做个功能
记个需求
整理一下需求池
下一个版本做什么
/backlog-manager
```

---

#### 🗺️ [项目目录地图构建器](./project-map-builder) (Project Map Builder)
**描述**: 为指定目录范围生成或增量更新高信噪比的目录说明文档

**适用场景**:
- 需要生成项目目录概览
- 需要代码仓结构说明文档
- 想要更新已有的 PROJECT_MAP.md
- 需要理解项目文件夹结构

**核心功能**:
- 📋 智能范围确认：必须先询问要扫描的文件夹，不默认全仓扫描
- 🔍 关键文件识别：自动识别入口、配置、服务线程等关键文件
- 📝 增量更新：已有 PROJECT_MAP.md 时仅做增量更新，不全量重写
- 🎯 多目录支持：支持单目录或多目录（可合并或分别生成）
- ⚠️ 明确标注：不确定的地方显式标注"假设"或"未确认"

**触发方式**:
```
生成项目地图
更新 PROJECT_MAP
给我生成目录说明
/project-map-builder
```

---

#### 📅 [版本规划助手](./version-planner) (Version Planner)
**描述**: 将产品需求拆解成可执行的渐进式版本规划（V0.1 MVP → V1.0）

**适用场景**:
- 需要拆解产品版本
- 想要规划 MVP 最小可行产品
- 需要分阶段实现功能
- 不确定优先级和开发顺序

**核心功能**:
- 🎯 价值优先：优先解决用户最痛的点，而非技术最难的点
- 🚀 快速验证：MVP 设计为 2-3 天能跑通，避免过度设计
- 📋 明确边界：每个版本明确"做什么"和"不做什么"
- 🔄 渐进式交付：每个版本都能独立使用，不依赖后续版本
- ✅ 可测量：每个版本有清晰的验证点和完成标准

**触发方式**:
```
拆版本
版本规划
MVP怎么做
分阶段实现
/version-planner
```

---

#### ✍️ [写作助手](./writing-assistant) (Writing Assistant)
**描述**: 根据观点清晰度自动选择最优写作路线，覆盖从思维挖掘到成稿的完整流程

**适用场景**:
- 想写文章但思路不清晰
- 需要梳理选题和核心观点
- 需要组织文章框架和逻辑
- 从零散想法到完整文章

**核心功能**:
- 🔍 智能诊断：快速判断观点清晰度，选择最优路线
- 💭 思维挖掘：观点模糊时，通过引导式对话倒出零散想法
- 🎯 选题确定：从洞察中提炼核心选题和灵魂句
- 📐 框架打磨：组织文章逻辑结构，确保表达清晰
- ✍️ 内容产出：根据框架写成完整文章，保持用户风格

**触发方式**:
```
我想写XX
帮我梳理选题
怎么形成框架
给我组织思路
/writing-assistant
```

---

#### 📝 [周报写作助手](./weekly-report) (Weekly Report)
**描述**: 帮助用户梳理周报，按照完整逻辑展示工作价值和边界

**适用场景**:
- 需要整理一周的工作内容
- 想要清晰展示工作价值和成果
- 需要说明遇到的问题和挑战
- 梳理下周工作重点

**核心功能**:
- 📋 素材收集：引导式对话，收集本周工作内容
- 🗂️ 分类整理：根据角色灵活选择合适的模块分类
- 🔍 信息补充：追问背景、结果、价值、状态和下一步
- ✅ 讨论调整：确认表述习惯和逻辑完整性
- 📄 文档输出：生成结构清晰的周报文档

**触发方式**:
```
写周报
周报
梳理周报
整理工作
/weekly-report
```

---

#### 🎯 [优先级判断助手](./priority-judge) (Priority Judge)
**描述**: 从混沌的待办事项中判断优先级，确定现在该做什么

**适用场景**:
- 有很多事要做，不知道从哪开始
- 想快速理清楚今天/本周该做什么
- 需要基于客观标准判断优先级
- 避免在没想清楚的事情上浪费时间

**核心功能**:
- 📝 收集待办：记录所有要做的事情
- 🔍 状态询问：了解每件事的清晰度和deadline
- ⚖️ 优先级判断：基于清晰度和deadline做决策
- 🎯 聚焦行动：每次只聚焦1-2件最重要的事
- 📋 文档化：生成优先级清单文档

**触发方式**:
```
我有很多事要做
帮我理一下
排个优先级
今天该做什么
我要盘一下
/priority-judge
```

---

#### 🤝 [思考拍档](./thinking-partner) (Thinking Partner)
**描述**: 陪你从混沌中理清局面，锁定核心问题，拆解卡点，共创解法，落地行动

**适用场景**:
- 面对复杂问题不知道从哪入手
- 想法很多但理不清主次
- 需要有人陪你一起想清楚
- 避免陷入细节迷失方向

**核心功能**:
- 📝 信息获取：引导式提问，看清全局
- 🎯 锁定核心问题：从一堆问题中找到最关键的那个
- 🔍 拆解卡点：层层追问，找到真正的根因
- 💡 共创解法：基于你的想法补充和修正
- ✅ 落地计划：把讨论结论变成可执行的行动

**触发方式**:
```
我现在很乱，帮我理一下
这事我不知道怎么办
陪我想想这个问题
/thinking-partner
```

---

#### 🎨 [UI 样式修改助手](./ui-design) (UI Design)
**描述**: UI 样式修改协作流程。通过结构化流程减少沟通偏差，避免浪费 token

**适用场景**:
- 需要修改页面样式、布局
- 调整间距、颜色、组件搭配
- UI 细节优化和微调
- 避免猜测式改代码

**核心功能**:
- 📸 截图定位：用截图确认当前状态
- 📐 现状描述：ASCII 画出当前布局
- 🎯 方案选择：提供 2-3 个可视化方案
- 🛠️ 最小改动：只改选定方案涉及的部分
- 🔄 微调迭代：执行具体的小修改

**触发方式**:
```
改一下这个页面的布局
调整这里的样式
这个间距不太对
/ui-design
```

---

#### 🔮 [终局愿景探索](./vision-exploration) (Vision Exploration)
**描述**: 帮你把模糊想法推演到最远的未来形态，输出 4~6 种维度完全不同的终局 HTML 原型

**适用场景**:
- 有个想法，想看看它最终能长成什么样
- 需要发散思维，探索一个 idea 的多种可能性
- 想在 PRD 之前先看到终局愿景
- 需要投资人级别的视觉原型

**核心功能**:
- 🔍 价值挖掘：反复追问"为什么"，找到需求背后的核心诉求
- 🎯 动机发现：识别真实用户使用场景
- 🔄 演进推导：从最小可行版本推导自然演进路径
- 🎨 终局渲染：输出 4~6 个自包含 HTML 原型，每个代表不同维度的终局形态
- 📊 对比分析：生成演进路径图和终局对比表

**触发方式**:
```
探索一下这个想法的终局
帮我看看这个功能最终能长成什么
/vision-exploration
```

---

#### 🏷️ [产品命名助手](./product-naming) (Product Naming)
**描述**: 通过结构化协作流程，从产品本质出发推导名字，避免拍脑袋起名

**适用场景**:
- 需要给产品/项目/模块起名字
- 不想拍脑袋，想从品牌策略角度思考命名
- 需要竞品命名调研支撑决策
- 起了名字但不确定好不好

**核心功能**:
- 🔍 灵魂挖掘：理解产品本质、用户画像、品牌气质
- ⚡ 约束提取：提炼核心语素，识别诉求之间的张力
- 🛤️ 路线发散：推导 2~4 条不同的命名策略方向
- 🏷️ 竞品验证：搜索同赛道产品命名规律，用数据支撑建议
- 📌 最终确认：输出名称 + Slogan + 决策依据的完整结论

**触发方式**:
```
帮我起个名字
给项目取名
产品命名
/product-naming
```

---

#### 🔧 [Issue 协作处理](./issue-triage) (Issue Triage)
**描述**: GitHub Issue 分诊与回复工作流，系统化分析问题、定位根因、撰写专业回复

**适用场景**:
- 收到 GitHub Issue 需要分析和回复
- 不确定 Issue 是 bug、架构局限还是功能请求
- 需要量化修复成本来做决策
- 想写出专业、诚恳的用户回复

**核心功能**:
- 🔍 代码诊断：沿调用链完整追踪，找到真正根因
- 🏷️ 问题定性：区分 Bug / 架构局限 / 功能请求 / 使用疑问
- ⚖️ 做不做决策：从改动范围、影响面、测试条件、变通方案四维评估
- ✍️ 起草回复：三层结构——解释意图、说明影响、交代计划
- 📮 发布：发评论、打标签、记录需求

**触发方式**:
```
帮我处理这个 Issue
分析一下这个 bug 报告
/issue-triage
```

---

#### 🔍 [GitHub 开源项目搜索助手](./github-repo-search) (GitHub Repo Search)
**描述**: 帮助用户搜索和筛选 GitHub 开源项目，输出结构化推荐报告

**适用场景**:
- 想找某个方向的开源项目
- 需要对比多个同类项目
- 想了解技术栈选型方案
- 寻找可直接使用或二次开发的工具

**核心功能**:
- 📝 需求收敛：确认主题、数量、排序模式、目标形态
- 🔍 检索词拆解：5-10 组 query，覆盖同义词、场景词、技术词
- 🏷️ 仓库分类：框架层/应用层/记忆层/MCP层/目录清单层/垂直场景层/方法论层
- 📊 质量精炼：综合权重排序（相关性/场景适用性/活跃度/工程成熟度）
- 📋 结构化报告：可理解、可比较、可决策、可直接行动的候选仓库列表

**触发方式**:
```
帮我找开源项目
搜一下GitHub上有什么
找找XX方向的仓库
开源项目推荐
/github-search
```

---

#### 🔍 [代码解释助手](./explain-code) (Explain Code)
**描述**: 用"类比 + ASCII 图"解释代码，让复杂的执行流程一目了然

**适用场景**:
- 需要理解一段陌生代码的工作原理
- 想向他人讲解代码库或执行流程
- 遇到难以理解的复杂概念
- 需要找出常见陷阱和误解

**核心功能**:
- 🌀 类比开头：将代码比作日常生活中的事物，降低理解门槛
- 🖼️ ASCII 图解：用 ASCII 艺术展示流程、结构或关系
- 📋 逐步讲解：解释代码执行的每一步，逻辑清晰
- ⚠️ 指出陷阱：标注常见的错误写法或容易踩的坑

**触发方式**:
```
这段代码是怎么工作的？
帮我解释一下这个函数
讲解一下这个代码库的执行流程
/explain-code
```

---

#### 📜 [学位论文撰写助手](./paper-write) (Paper Write)
**描述**: 本科与硕士学位论文全流程撰写辅助，理工/文科自动区分，覆盖大纲审核、章节仿写、润色、参考文献等

**适用场景**:
- 需要审核或优化论文大纲（理工科/文科）
- 需要仿写绪论、摘要、实验章节等
- 需要文献综述、案例分析、对策建议（文科）
- 论文润色、防 AIGC、中英互译
- 参考文献格式整理（GB/T 7714）

**核心功能**:
- 📋 大纲审核：理工科/文科分别适配，结构逻辑检查
- ✍️ 结构仿写：绪论/摘要/实验章节/文献综述/案例分析/对策建议
- 📚 参考文献：GB/T 7714 格式获取与融合
- 🖊️ 润色降重：通用/实验章节/文科章节三种润色模式，防 AIGC
- 🌐 中英互译：学术风格互译，信息零丢失
- 📊 结构化提取：从论文提取答辩所需的结构化信息

**触发方式**:
```
帮我审核一下这个论文大纲
按这篇范文仿写我的实验章节
这段读起来像 AI 写的，帮我润色
帮我找 RLHF 代表作并给 BibTeX
/paper-write
```

---

#### 🎞️ [PPT 生成助手](./pptgen-drawio) (PPT Gen Drawio)
**描述**: 根据论文或汇报内容生成多页 Draw.io 格式 PPT，支持论文答辩与通用汇报两种模式，自动导出 .pptx

**适用场景**:
- 需要制作论文答辩/开题/预答辩 PPT
- 需要制作工作汇报、产品介绍、演讲 PPT
- 想快速生成多页幻灯片，跳过手动排版
- 有自己的 PPTX 模板，需要按模板风格生成

**核心功能**:
- 🎨 多风格支持：经典学术/现代极简/暖色学术/科技明快/自定义模板五种风格
- 📑 双模式：论文答辩（封面→目录→背景→方法→实验→结论）与通用汇报自动适配
- 📐 16:9 规范：严格 1920×1080 画布，坐标系正确，全局 id 唯一
- 🛠️ 自动导出：生成 .drawio 后自动调用 drawio2pptx 输出 .pptx
- ✅ 自验脚本：内置 XML 格式校验，防止常见坑（id 重复/坐标偏移/内容遮挡）

**触发方式**:
```
帮我做答辩 PPT，论文在 xxx
根据这个大纲生成汇报 PPT
/pptgen-drawio
```

---

#### 🖼️ [Draw.io 图表生成](./drawio-diagram) (Drawio Diagram)
**描述**: 生成标准 Draw.io (.drawio) 格式图表，支持从零生成（模型架构/流程图）与风格迁移（参考图风格复刻）

**适用场景**:
- 需要为深度学习模型生成架构图（Transformer、CNN 等）
- 需要绘制算法流程图、数据流图、系统架构图
- 有参考图，想按其风格生成新图
- 需要导出 PNG/SVG/PDF 供论文使用

**核心功能**:
- 🏗️ 从零生成：模型架构图、算法流程图、感受野示意图等
- 🎨 风格迁移：上传参考图 + 内容描述，按参考图排版/配色生成新图
- 📐 XML 规范：标签严格闭合、id 全局唯一、特殊字符转义，可直接在 Draw.io 打开
- 📤 导出就绪：生成图表说明和使用指南，附论文引用示例

**触发方式**:
```
画一个 Transformer 架构图
做一张算法流程图
按这张参考图的风格画
/drawio-diagram
```

---

#### 🗂️ [代码生成项目图表](./codegen-diagram) (Codegen Diagram)
**描述**: 基于当前项目/代码仓库生成 Draw.io 格式图表，支持技术栈图、系统架构图、数据结构图、E-R 图

**适用场景**:
- 需要可视化当前项目的技术选型
- 需要生成系统分层架构图
- 需要根据代码生成数据结构或实体关系图
- 毕设/项目汇报需要图表支撑

**核心功能**:
- 🔧 技术栈图：自动识别项目技术选型，生成组件关系图
- 🏛️ 系统架构图：分层结构、调用流程可视化
- 🗃️ 数据结构图：表结构、实体字段关系图
- 🔗 E-R 图：数据库实体关系图，支持主外键标注
- 🎨 统一风格：主色 #3366CC，连接线规范，字体 Helvetica

**触发方式**:
```
根据当前项目画技术栈结构图
画我们系统的四层架构图
根据代码生成数据结构图
根据数据库表结构画 E-R 图
/codegen-diagram
```

---

#### 📄 [代码生成项目文档](./codegen-doc) (Codegen Doc)
**描述**: 基于当前项目/代码生成论文章节、项目梳理、重点问题清单、简历项目描述

**适用场景**:
- 需要根据项目代码生成论文的系统设计章节
- 需要梳理项目结构和模块说明
- 需要整理项目技术难点和待解决问题
- 需要把当前项目写成简历项目经历

**核心功能**:
- 📋 论文章节：系统总体设计/详细设计章节，有据可依不编造
- 📁 项目梳理：按格式梳理项目概述、模块、技术栈
- ⚡ 重点问题：技术难点、待解决问题、项目风险清单
- 📝 简历项目描述：按简历格式输出项目经历，突出技术亮点

**触发方式**:
```
根据当前项目生成系统总体设计章节
按这个格式梳理我们项目
梳理这个项目的技术难点
按简历格式把当前项目写成项目经历
/codegen-doc
```

---

#### ⚙️ [开发流程五步法](./dev-workflow) (Dev Workflow)
**描述**: 统一开发流程，支持需求理解、方案设计、代码实现、代码审查、Bug 修复五步串联

**适用场景**:
- 有新功能想法，需要从需求分析开始
- 需要做技术方案设计和架构决策
- 开始编写代码实现具体功能
- 需要代码审查，确保质量
- 遇到报错/异常/测试失败需要修复

**核心功能**:
- 📝 需求理解：从描述中提炼功能需求、约束条件，产出需求文档
- 🏗️ 方案设计：技术方案、架构设计、模块拆分
- 💻 代码实现：按方案编写代码，分步交付
- 🔍 代码审查：多语言代码质量/安全/规范检查
- 🐛 Bug 修复：根因定位、复现分析、最小化修复
- 🔗 流程串联：每步完成后自动提示进入下一阶段

**触发方式**:
```
我想做一个 XXX，帮我整理需求
帮我做技术方案
按方案开始写代码
帮我审查这段代码
这里报错了：xxx
/dev-workflow
```

---

#### 📊 [周报汇报总结生成](./md-report-summary) (MD Report Summary)
**描述**: 生成高质量 Markdown 周报、工作汇报、总结、介绍等文档；无草稿时联网搜索，有草稿时整理润色

**适用场景**:
- 需要快速写本周周报
- 需要写工作汇报、季度总结、项目复盘
- 有草稿但需要整理润色
- 需要项目介绍或个人简介

**核心功能**:
- 🔍 无草稿模式：确认主题→联网搜索背景资料→按模板撰写，内容有据可查
- 📝 有草稿模式：保留所有原始数据/表格/图片，仅润色语句、补充遗漏
- 📊 数据具体：保留量化数据（时间/数量/百分比），不写"继续推进"类空话
- 🗂️ 结构清晰：小标题区分业务模块，重要结论引用块突出
- ✅ 输出就绪：Markdown 格式，可直接复制粘贴

**触发方式**:
```
帮我写本周周报
写一份 Q1 工作汇报
写项目总结
写一份项目介绍
/md-report-summary
```

---

#### ✍️ [公众号创作助手](./wechat-article-writer) (WeChat Article Writer)
**描述**: 公众号/自媒体全流程，支持撰写文章、封面图、正文插图、风格提取，内置 9 种写作风格

**适用场景**:
- 需要写公众号文章或技术博客
- 需要生成公众号封面、B 站封面、小红书配图
- 需要文章正文配图（步骤图/流程图/演示图）
- 想分析爆款文章的写作风格，提炼可复用规则

**核心功能**:
- 🖊️ 撰写文章：联网搜索最新资料，9 种风格自由选择，故事化开头
- 🖼️ 封面/插图：生成 Draw.io 格式封面图或正文步骤图，配色统一
- 🔍 风格提取：分析样本文章，输出风格画像、可执行规则（15-30条）、复刻 Prompt
- 📢 标题生成：5 个爆款风格备选标题，覆盖痛点/数字/情绪/悬念
- 🎨 9 种风格：默认/高流量/清单体/资源盘点/个人实测/认知颠覆/身份共鸣/故事化/深度随笔

**触发方式**:
```
写一篇关于 XX 的公众号文章
用高流量风格写 Vibe Coding
生成这篇文章的封面，16:9
分析这篇公众号文章的写作风格
/wechat-article-writer
```

---

#### 🌐 [Markdown 英译中](./translate-md-to-zh) (Translate MD to ZH)
**描述**: 将英文 Markdown 文件翻译为简体中文，保留 Markdown 格式、代码块、链接和文件路径，输出 -zh.md 文件

**适用场景**:
- priority-judge需要将英文 README 或文档本地化为中文
- 翻译技术文档，保持代码块和链接不变
- 批量处理 Markdown 格式的说明文件

**核心功能**:
- 🌐 结构保留：代码块、内联代码、链接路径、图片路径、HTML 标签均不翻译
- ✍️ 精准翻译：标题、正文、表格、列表、图片 alt 文本自然翻译
- 📁 安全输出：在同目录生成 `-zh.md` 文件，不覆盖源文件
- 🔒 质量保证：技术术语一致，内容完整，不添加译者注

**触发方式**:
```
把这个 README 翻译成中文
/translate-md-zh README.md
/translate-md-zh docs/getting-started.md
```

---

#### 🚁 [飞行跟随训练分析](./flyfollow-training-analysis) (Flyfollow Training Analysis)
**描述**: 自动诊断 SKRL flyfollow 任务训练日志，分析奖励趋势、收敛情况、成功率、终止原因等

**适用场景**:
- 想了解当前 flyfollow 训练是否在正常收敛
- 需要诊断奖励曲线异常（增长停滞/惩罚主导/震荡）
- 想分析终止原因分布（飞太高/飞出边界/超时）
- 对比多次训练运行的质量差异

**核心功能**:
- 📈 奖励趋势：分析 total reward 是否被惩罚项主导，tracking/velocity 奖励是否可达
- ✅ 收敛判断：判断训练是改善中/停滞/不稳定
- 📊 成功率分析：`sustained_success_rate` 是否真实上升
- 🏔️ 高度问题：height 是否始终偏高，未收敛至 desired_height
- 🔍 终止原因：fly_high/fly_low/out_of_bounds/timeout 各占比分析
- 🛠️ 脚本驱动：自动运行分析脚本，结合 params/env.yaml 配置综合解读

**触发方式**:
```
分析一下最近的训练结果
看看这次训练收敛了吗
诊断一下奖励曲线
/flyfollow-training-analysis
```

---

#### 🔄 [Skill 与 Prompt 互转](./skill-prompt-convert) (Skill Prompt Convert)
**描述**: 在 SKILL.md 与聊天框 Prompt 两种格式之间双向转换，核心信息零丢失

**适用场景**:
- 有一个 SKILL.md，需要转成可复制到聊天框的 Prompt
- 有一个好用的 Prompt，想固化为 Agent 可自动触发的 Skill
- 需要整理 Skill 或 Prompt 的格式规范

**核心功能**:
- 🔄 双向转换：Skill → Prompt 与 Prompt → Skill 均支持
- 📋 转换说明：输出映射关系说明，便于理解转换逻辑
- 🏷️ 命名规范：name 必须英文小写短横线，description 包含"何时用"和"干什么"
- ✅ 格式校验：确保 YAML 前置元数据格式正确（`---` 开头结尾）
- 🔒 信息完整：不删减核心逻辑、步骤、约束条件

**触发方式**:
```
把这个 Skill 转成聊天框可用的 Prompt
把这个 Prompt 转成 SKILL.md 格式
/skill-prompt-convert
```

---

#### 🛠️ [Skill 创建助手](./skill-create) (Skill Create)
**描述**: 引导用户创建高质量的 Agent Skill，涵盖需求收集、设计、实现、验证全流程，适用于 Claude Code、Cursor 等 Agent 工具

**适用场景**:
- 有重复性工作流，想固化为可自动触发的 Skill
- 不知道如何写 SKILL.md，需要指导
- 想了解 Skill 的最佳实践（description 写法、文件结构、脚本使用）
- 想把已有的工作流整理成标准 Skill

**核心功能**:
- 🔍 需求挖掘：引导明确 Skill 用途、触发场景、存储位置（个人/项目）
- 🎯 Description 优化：第三人称、包含 WHAT 和 WHEN、关键词驱动触发
- 🗂️ 文件结构：SKILL.md + reference + examples + scripts 的标准目录布局
- ✂️ 精简原则：500 行以内、渐进式披露、术语一致，避免过度解释
- ✅ 质量验证：完整的 Checklist，确保 Skill 可被发现、结构正确、示例具体

**触发方式**:
```
我经常要审查论文，帮我创建一个 Skill
帮我把这个工作流做成 Skill
/skill-create
```

---

### 🗂️ 分类速查

按场景快速找到对应 Skill 和示例 Prompt。

#### 📚 本科 & 硕士学位论文

| 用途 | Skill | 示例 Prompt |
| --- | --- | --- |
| 大纲审核（理工/文科） | paper-write | 「帮我审核一下这个论文大纲」（理工科 / 文科自动区分） |
| 结构仿写（理工） | paper-write | 「按这篇范文仿写我的实验章节」「帮我写绪论/摘要，参考 XX 论文」 |
| 结构仿写（文科） | paper-write | 「文科仿写文献综述/理论章节」「文科仿写案例分析/对策建议」「写文科摘要」 |
| 润色 / 去 AI 化 | paper-write | 「这段读起来像 AI 写的，帮我润色」「实验章节润色」「文科章节润色」 |
| 参考文献 | paper-write | 「帮我找 RLHF 代表作并给 BibTeX」「cite Vaswani 的 attention」 |
| 结构化信息提取 | paper-write | 「从这篇论文提取结构化信息，用于答辩 PPT」 |
| 系统章节生成 | codegen-doc | 「根据当前项目生成系统总体设计章节」 |
| 答辩 PPT / 通用汇报 PPT | pptgen-drawio | 「帮我做答辩 PPT，论文在 xxx」「根据这个大纲生成汇报 PPT」 |
| 模型架构图 / 流程图 | drawio-diagram | 「画一个 Transformer 架构图」「做一张算法流程图」 |
| 图片风格迁移 | drawio-diagram | 「按这张参考图的风格画」「参考图+描述：画一个三层系统，前端 Vue、后端 Spring、数据库 MySQL」 |
| 技术栈图 | codegen-diagram | 「根据当前项目画技术栈结构图」 |
| 系统架构图 | codegen-diagram | 「画我们系统的四层架构图」 |
| 数据结构图 | codegen-diagram | 「根据代码生成数据结构图」 |
| E-R 图 | codegen-diagram | 「根据数据库表结构画 E-R 图」 |

> **paper-write**：理工（science-\*）与文科（liberal-\*）自动区分，支持大纲审核、结构仿写、参考文献、润色、扩写/缩写、防 AIGC、中英互译、结构化信息提取。
> **pptgen-drawio**：支持论文答辩与通用汇报两种模式，输出 .drawio 后可用 drawio2pptx 导出 .pptx。

---

#### ⚙️ 开发流程五步法

| 步骤 | Skill | 示例 Prompt |
| --- | --- | --- |
| 需求理解 | dev-workflow | 「我想做一个 XXX，帮我整理需求」 |
| 方案设计 | dev-workflow | 「需求已整理好，帮我做技术方案」「架构设计：前后端分离」 |
| 代码实现 | dev-workflow | 「按方案开始写代码」「实现用户登录模块」 |
| 代码审查 | dev-workflow | 「帮我审查这段代码」「PR review，按团队规范检查」 |
| Bug 修复 | dev-workflow | 「这里报错了：xxx」「功能跑不通，帮我修」「测试挂了，看看怎么回事」 |

> **dev-workflow**：根据用户表述自动匹配 requirement / design / implementation / review / bug-fix 五步之一。

---

#### 📱 自媒体创作

| 用途 | Skill | 示例 Prompt |
| --- | --- | --- |
| 公众号/技术博客（含配图） | wechat-article-writer | 「写一篇关于 Cursor Skills 的公众号文章」「用高流量风格写 Vibe Coding」 |
| 公众号封面 / B站封面 / 小红书配图 | wechat-article-writer | 「生成这篇文章的封面，16:9」 |
| 正文插图 | wechat-article-writer | 「生成 Cursor 启用四步骤的步骤图」「画 Prompt/Rules/Skills 对比图」 |
| 风格提取 | wechat-article-writer | 「分析这篇公众号文章的写作风格」「提取可复用规则」「模仿这篇爆款文风」 |

> **wechat-article-writer**：支持 9 种写作风格：默认、高流量、清单体、资源盘点、个人实测、认知颠覆、身份共鸣、故事化、深度随笔。

---

#### 📊 周报 / 汇报 / 总结 / 介绍

| 用途 | Skill | 示例 Prompt |
| --- | --- | --- |
| 周报 | md-report-summary | 「帮我写本周周报，结合 websearch」 |
| 工作汇报 | md-report-summary | 「写一份 Q1 工作汇报」「整理汇报材料」 |
| 总结 / 复盘 | md-report-summary | 「写项目总结」「帮我复盘这次活动」 |
| 介绍 | md-report-summary | 「写一份项目介绍」「个人简介」 |

> **md-report-summary**：无草稿时从 Web 搜索并总结；有草稿时结合草稿整理、补充、润色。输出 Markdown。

---

#### 📄 项目文档与简历

| 用途 | Skill | 示例 Prompt |
| --- | --- | --- |
| 项目整体梳理 | codegen-doc | 「按这个格式梳理我们项目：概述、模块、技术栈」 |
| 项目重点问题 | codegen-doc | 「梳理这个项目的技术难点和待解决问题」 |
| 简历项目描述 | codegen-doc | 「按这个格式把当前项目写成简历项目经历」 |

---

#### 🔧 工具与扩展

| 用途 | Skill | 示例 Prompt |
| --- | --- | --- |
| Skill 创建 | skill-create | 「我经常要审查论文，帮我创建一个 Skill」 |
| Skill 与 Prompt 互转 | skill-prompt-convert | 「把这个 Skill 转成聊天框可用的 Prompt」 |
| Markdown 英译中 | translate-md-to-zh | 「把这个 README 翻译成中文」 |

---

### 🚀 快速开始

#### 安装方式

**使用 Codex 或 Claude Code CLI 安装**

如果你使用 Codex 或 Claude Code CLI，直接跟 AI 说：

```
安装这个 GitHub 库：https://github.com/yunshu0909/yunshu_skillshub
```

AI 会自动帮你完成安装！

**手动安装**

将本仓库克隆到对应 Agent 工具的 Skills 目录：

```bash
# Claude Code（默认目录）
cd ~/.claude/skills/
git clone https://github.com/yunshu0909/yunshu_skillshub.git

# Cursor（个人级）
cd ~/.cursor/skills/
git clone https://github.com/yunshu0909/yunshu_skillshub.git

# Cursor（项目级，放在项目根目录下）
cd .cursor/skills/
git clone https://github.com/yunshu0909/yunshu_skillshub.git
```

或者，你也可以单独复制需要的 Skill 到你的 Skills 目录。

**各平台官方文档参考**

> - Claude Code：[https://github.com/anthropics/skills](https://github.com/anthropics/skills)
> - Codex：[https://github.com/openai/skills](https://github.com/openai/skills)
> - Cursor：[https://cursor.com/cn/docs/context/skills](https://cursor.com/cn/docs/context/skills)
> - Trae：[https://docs.trae.cn/ide/skills](https://docs.trae.cn/ide/skills)
> - GitHub Copilot：[https://code.visualstudio.com/docs/copilot/customization/agent-skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
> - OpenClaw：[https://docs.openclaw.ai/zh-CN/tools/skills](https://docs.openclaw.ai/zh-CN/tools/skills)

#### 使用 Skills

在 Claude Code CLI 中，你可以通过以下方式使用：

```bash
# 使用配图助手
/image-assistant

# 使用思维挖掘助手
/thought-mining

# 使用 PRD 文档撰写助手
/prd-doc-writer

# 使用新功能设计探索
/design-exploration

# 使用需求变更工作流
/req-change-workflow

# 使用课程构建器
/lesson-builder

# 使用需求池管理
/backlog-manager

# 使用项目目录地图构建器
/project-map-builder

# 使用版本规划助手
/version-planner

# 使用写作助手
/writing-assistant

# 使用周报写作助手
/weekly-report

# 使用优先级判断助手
/priority-judge

# 使用思考拍档
/thinking-partner

# 使用 UI 样式修改助手
/ui-design

# 使用 GitHub 开源项目搜索助手
/github-search

# 使用终局愿景探索
/vision-exploration

# 使用产品命名助手
/product-naming

# 使用 Issue 协作处理
/issue-triage

# 使用代码解释助手
/explain-code

# 使用学位论文撰写助手
/paper-write

# 使用 PPT 生成助手
/pptgen-drawio

# 使用 Draw.io 图表生成
/drawio-diagram

# 使用代码生成项目图表
/codegen-diagram

# 使用代码生成项目文档
/codegen-doc

# 使用开发流程五步法
/dev-workflow

# 使用周报汇报总结生成
/md-report-summary

# 使用公众号创作助手
/wechat-article-writer

# 使用 Markdown 英译中
/translate-md-zh

# 使用飞行跟随训练分析
/flyfollow-training-analysis

# 使用 Skill 与 Prompt 互转
/skill-prompt-convert

# 使用 Skill 创建助手
/skill-create
```

或者直接在对话中描述你的需求，相关 Skill 会自动触发。

**📚 查看使用示例**

想了解每个 Skill 的具体使用方法？查看 [使用示例文档](./EXAMPLES.md)，里面包含了详细的使用场景和预期输出。

---

### 📂 项目结构

```
.
├── README.md                    # 项目说明文档
├── LICENSE                      # MIT 许可证
├── CHANGELOG.md                 # 更新日志
├── EXAMPLES.md                  # 使用示例
├── image-assistant/             # 配图助手
│   ├── SKILL.md                # Skill 定义文件
│   ├── stages/                 # 各阶段详细说明
│   ├── templates/              # 风格模板和配图模板
│   ├── examples/               # 使用示例
│   └── scripts/                # 批量生图脚本
├── thought-mining/              # 思维挖掘助手
│   ├── SKILL.md                # Skill 定义文件
│   ├── stages/                 # 各阶段详细说明
│   ├── templates/              # 模板文件
│   └── examples/               # 使用示例
├── prd-doc-writer/             # PRD 文档撰写助手
│   ├── SKILL.md               # Skill 定义文件
│   ├── assets/                # 模板资源
│   └── references/            # 参考文档和示例
├── design-exploration/         # 新功能设计探索
│   ├── SKILL.md               # Skill 定义文件
│   └── templates/             # 需求总结模板
├── req-change-workflow/        # 需求变更工作流
│   ├── SKILL.md               # Skill 定义文件
│   ├── references/            # 模板和清单
│   └── scripts/               # 辅助脚本
├── lesson-builder/             # 课程构建器
│   └── SKILL.md               # Skill 定义文件
├── backlog-manager/            # 需求池管理
│   └── SKILL.md               # Skill 定义文件
├── project-map-builder/        # 项目目录地图构建器
│   └── SKILL.md               # Skill 定义文件
├── version-planner/            # 版本规划助手
│   └── SKILL.md               # Skill 定义文件
├── writing-assistant/          # 写作助手
│   ├── SKILL.md               # Skill 定义文件
│   ├── stages/                # 各阶段详细说明
│   └── templates/             # 模板文件
├── weekly-report/             # 周报写作助手
│   └── SKILL.md              # Skill 定义文件
├── priority-judge/            # 优先级判断助手
│   └── SKILL.md              # Skill 定义文件
├── thinking-partner/          # 思考拍档
│   └── SKILL.md              # Skill 定义文件
├── ui-design/                 # UI 样式修改助手
│   └── SKILL.md              # Skill 定义文件
├── github-repo-search/        # GitHub 开源项目搜索助手
│   └── SKILL.md              # Skill 定义文件
├── vision-exploration/        # 终局愿景探索
│   └── SKILL.md              # Skill 定义文件
├── product-naming/            # 产品命名助手
│   └── SKILL.md              # Skill 定义文件
├── issue-triage/              # Issue 协作处理
│   └── SKILL.md              # Skill 定义文件
├── explain-code/              # 代码解释助手
│   └── SKILL.md              # Skill 定义文件
├── paper-write/               # 学位论文撰写助手
│   ├── SKILL.md              # Skill 定义文件
│   └── reference/            # 各场景详细指令
├── pptgen-drawio/             # PPT 生成助手
│   ├── SKILL.md              # Skill 定义文件
│   ├── ppt_template/         # PPT 模板目录
│   ├── scripts/              # 辅助脚本
│   └── reference/            # 风格参考文件
├── drawio-diagram/            # Draw.io 图表生成
│   ├── SKILL.md              # Skill 定义文件
│   └── reference/            # 生成与风格迁移指令
├── codegen-diagram/           # 代码生成项目图表
│   ├── SKILL.md              # Skill 定义文件
│   └── reference/            # 各图表类型指令
├── codegen-doc/               # 代码生成项目文档
│   ├── SKILL.md              # Skill 定义文件
│   └── reference/            # 各文档类型指令
├── dev-workflow/              # 开发流程五步法
│   ├── SKILL.md              # Skill 定义文件
│   └── reference/            # 各步骤详细指令
├── md-report-summary/         # 周报汇报总结生成
│   ├── SKILL.md              # Skill 定义文件
│   └── reference/            # 模板文件
├── wechat-article-writer/     # 公众号创作助手
│   ├── SKILL.md              # Skill 定义文件
│   └── reference/            # 各风格写作指令与封面/插图指南
├── translate-md-to-zh/        # Markdown 英译中
│   └── SKILL.md              # Skill 定义文件
├── flyfollow-training-analysis/ # 飞行跟随训练分析
│   ├── SKILL.md              # Skill 定义文件
│   └── scripts/              # 训练日志分析脚本
├── skill-prompt-convert/      # Skill 与 Prompt 互转
│   └── SKILL.md              # Skill 定义文件
└── skill-create/              # Skill 创建助手
    └── SKILL.md              # Skill 定义文件
```

---

### 🌐 更多公开 Skills 资源

**合集网站**：想快速找到现成技能，从这里入手

| 网站 | 特点 | 适合谁 |
| --- | --- | --- |
| [SkillsMP](https://skillsmp.com/) | 模板商店，已有 36 万+ | 想挑成品技能包的 |
| [agent-skills.md](https://agent-skills.md/) | 收录 6000+ 常用技能，强调直接可用 | 想快速上手，不想自己写的 |
| [Agent Skills Me](https://agentskills.me/) | 人工精选，"精而少" | 不想花时间筛选的 |
| [Skills Directory](https://www.skillsdirectory.com/) | Reddit 社区推荐，偏口碑榜单 | 想看真实评价再决定的 |
| [SkillStore](https://skillstore.io/zh-hans) | 中文友好，经过安全审查 | 团队使用或合规敏感场景 |
| [Skills.sh](https://skills.sh/) | 热门趋势技能，支持一键安装 | 想快速尝鲜新技能的 |
| [aitmpl.com/skills](https://www.aitmpl.com/skills) | Claude Code 模板集合 | Claude Code 用户 |

**源码仓库**：想学实现、深度定制，看这里

| 仓库 | 特点 |
| --- | --- |
| [Anthropic Skills](https://github.com/anthropics/skills) | 官方维护，最佳实践参考 |
| [Antfu Skills](https://github.com/antfu/skills) | 知名开发者实践，工程化质量高 |
| [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) | 偏 Web / 全栈场景 |
| [Awesome Agent Skills](https://github.com/JackyST0/awesome-agent-skills) | 社区精选索引，「awesome 系」风格 |
| [Ultimate Agent Skills Collection](https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection) | 多来源汇总，适合深挖扫货 |
| [Awesome OpenClaw Skills](https://github.com/VoltAgent/awesome-openclaw-skills) | OpenClaw 专属，5400+ 技能已分类 |
| [code-review-skill](https://github.com/awesome-skills/code-review-skill) | 代码审查专项，覆盖 React / Vue / Rust / TypeScript |

---

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！如果你有任何建议或发现了 bug，请随时告诉我。

---

### 📄 许可证

本项目采用 [MIT License](./LICENSE) 开源。

---

### 📧 联系方式

如有问题或建议，欢迎通过 GitHub Issues 联系。

---

## English

### 📖 Introduction

A carefully crafted collection of Claude Code Skills designed to boost efficiency in software development and product management. Each skill has been battle-tested to help you work more effectively in your daily tasks.

### ✨ Included Skills

#### 🎨 [Image Assistant](./image-assistant)
**Description**: Convert article/module content into unified-style, text-minimal, highly readable 16:9 infographic prompts

**Use Cases**:
- Need illustrations for articles but don't know how to design
- PPT, posters, or social media graphics need a unified style
- Too much text, want more engaging and readable visual presentation
- Need to batch generate illustration prompts

**Core Features**:
- 📋 Requirement Clarification: Extract content, scenario, audience, and text density preferences
- 🗂️ Illustration Planning: Split content, define image list (how many/what each explains)
- ✍️ Copy Finalization: Word-by-word finalization of "what text goes on the image" (Copy Spec)
- 🎯 Prompt Packaging: Generate copy-ready image generation prompts, support batch generation
- 🔄 Iterative Refinement: Reduce text, change metaphors, improve readability based on feedback

**Trigger**:
```
Make an image for this content / how many images?
Give me two image generation prompts
Too much text, make it more engaging and readable
/image
```

---

#### 🧠 [Thought Mining](./thought-mining)
**Description**: Helps you extract scattered thoughts from your mind, record them, and organize them into articles through conversational guidance

**Use Cases**:
- Want to write an article but thoughts are unclear
- Have many scattered ideas that need organizing
- Need to extract core insights from chaotic thinking

**Core Features**:
- 📝 Thought Mining: Guided conversation to help you articulate and record ideas
- 🎯 Topic Selection: Find core viewpoints from insights
- ✅ Validation: Verify understanding through web search
- ✍️ Writing Assistance: Logic checking, text polishing, extracting key phrases
- 🔍 Final Review: Comprehensive check before publishing

**Trigger**:
```
I want to write an article about XX
Help me organize my thoughts
/thought-mining
```

---

#### 📋 [PRD Doc Writer](./prd-doc-writer)
**Description**: A story-driven approach to writing and iteratively refining PRD/requirement documents

**Use Cases**:
- Need to write product requirement documents
- Want to organize requirements using user stories
- Need to reduce requirement ambiguity with diagrams

**Core Features**:
- 🗺️ User Journey Map: Build macro business processes
- 📖 Story-based Requirements: Each feature is a complete user story
- 🎨 ASCII Wireframes: Visualize page layouts
- 📊 Mermaid Diagrams: Flow charts/state diagrams/sequence diagrams
- ✅ Staged Confirmation: Ensure consensus at every step

**Trigger**:
```
Help me write a PRD
Organize requirement document
/prd-doc-writer
```

---

#### 🎨 [Design Exploration](./design-exploration)
**Description**: New feature design exploration workflow. From fuzzy ideas to deliverable design reference documents as input for the PRD phase

**Use Cases**:
- Have a fuzzy idea for a new feature/module
- Need to batch explore multiple design options
- Need complete coverage of page states (normal/exception/boundary)
- Need to produce design mockups as development reference

**Core Features**:
- 📝 Requirement Convergence: Define what to do, what not to do, and boundaries
- 🔍 Technical Research: Understand external data constraints and technical feasibility
- 🎨 ASCII Batch Exploration: Generate 5-8 options at once for selection
- 📐 HTML Mockups: Produce mockups based on selected option
- 📊 Full State Coverage: Normal/loading/empty/error/boundary states
- 📋 Interaction Rule Table: Frontend development reference

**Trigger**:
```
I want to build a new feature
Help me design this module
Create a design proposal
/design-exploration
```

---

#### 🔄 [Requirement Change Workflow](./req-change-workflow)
**Description**: Standardize the requirement change process to avoid chaos and code breakage when modifying requirements

**Use Cases**:
- Need to modify existing feature requirements
- Frequently encounter unexpected bugs when changing requirements
- Need a reliable change validation process
- Especially suitable for complex projects like Chrome extensions

**Core Features**:
- 📝 Requirement Clarification: Lock change scope and acceptance criteria
- 🔍 Current Baseline: Confirm current behavior from code
- ⚠️ Impact Assessment: Assess risks and change scope
- 🎯 Design Proposal: Propose new design and get approval
- 🛠️ Minimal Implementation: Small-scale, localized code changes
- ✅ Regression Testing: Fixed validation checklist
- 📚 Documentation Maintenance: Decision log and documentation updates

**Trigger**:
```
Change requirement/requirement modification
Adjust interaction/change feature
/req-change-workflow
```

---

#### 📚 [Lesson Builder](./lesson-builder)
**Description**: A discussion-driven approach to quickly complete course outlines and teaching materials

**Use Cases**:
- Need to quickly prepare a lesson
- Have clear ideas that need to be organized into documents
- Need to iterate on existing course outlines
- Preparing training or teaching content

**Core Features**:
- 💭 Co-create Outline: Extract ideas through discussion, form clear course framework
- 📖 Write Materials: Create complete teaching materials based on outline
- 🎯 Framework First: Confirm framework before details to avoid rework
- ⚡ Rapid Iteration: Supports both quick co-creation and strict confirmation modes
- 📋 Minimal Documentation: Only produce what you need (outline/materials/supplements)

**Trigger**:
```
Prepare lesson
Make teaching materials/prepare course
/lesson-builder
```

---

#### 📦 [Backlog Manager](./backlog-manager)
**Description**: Backlog management. Throw in ideas/pain points anytime, AI handles追问, organizing, merging, and archiving. Assists with selection when starting a new version. Pain-driven, no premature scheduling

**Use Cases**:
- Record product ideas and feature needs anytime
- Manage scattered requirements to avoid forgetting
- Select what to do when preparing a new version
- Organize and clean up outdated requirements

**Core Features**:
- 📝 Collection: Ask about pain points, frequency, workarounds to confirm understanding
- 📂 Categorization: Check merge possibilities, judge status (ready to do/needs thinking/on hold)
- 🧹 Organization: Regularly clean outdated items, upgrade well-thought-out items
- 🎯 Selection: Analyze candidates based on frequency/workaround feasibility/ROI
- ✅ Archiving: Mark completed, update dependencies

**Trigger**:
```
I want to build a feature
Record a requirement
Organize the backlog
What to do in next version
/backlog-manager
```

---

#### 🗺️ [Project Map Builder](./project-map-builder)
**Description**: Generate or incrementally update high signal-to-noise directory documentation for specified directories

**Use Cases**:
- Need to generate project directory overview
- Need codebase structure documentation
- Want to update existing PROJECT_MAP.md
- Need to understand project folder structure

**Core Features**:
- 📋 Smart Scope Confirmation: Must ask for folders to scan, never defaults to full repository
- 🔍 Key File Recognition: Automatically identifies entry points, configs, service threads, and other critical files
- 📝 Incremental Updates: Only does incremental updates when PROJECT_MAP.md exists, never full rewrites
- 🎯 Multi-directory Support: Supports single or multiple directories (merge or generate separately)
- ⚠️ Explicit Annotation: Clearly marks uncertain areas as "assumption" or "unconfirmed"

**Trigger**:
```
Generate project map
Update PROJECT_MAP
Generate directory documentation
/project-map-builder
```

---

#### 📅 [Version Planner](./version-planner)
**Description**: Decompose product requirements into executable progressive version roadmap (V0.1 MVP → V1.0)

**Use Cases**:
- Need to break down product versions
- Want to plan MVP (Minimum Viable Product)
- Need to implement features in stages
- Uncertain about priorities and development order

**Core Features**:
- 🎯 Value First: Prioritize solving users' biggest pain points, not the hardest technical challenges
- 🚀 Quick Validation: MVP designed to work in 2-3 days, avoiding over-engineering
- 📋 Clear Boundaries: Each version clearly defines "what to do" and "what not to do"
- 🔄 Progressive Delivery: Each version can be used independently, not dependent on future versions
- ✅ Measurable: Each version has clear validation points and completion criteria

**Trigger**:
```
Break down versions
Version planning
How to do MVP
Implement in stages
/version-planner
```

---

#### ✍️ [Writing Assistant](./writing-assistant)
**Description**: Automatically selects optimal writing route based on viewpoint clarity, covering complete flow from thought mining to final draft

**Use Cases**:
- Want to write an article but thoughts are unclear
- Need to organize topic and core viewpoint
- Need to organize article framework and logic
- From scattered ideas to complete article

**Core Features**:
- 🔍 Smart Diagnosis: Quickly assess viewpoint clarity and choose optimal route
- 💭 Thought Mining: When viewpoint is fuzzy, use guided dialogue to extract scattered ideas
- 🎯 Topic Selection: Extract core topic and key message from insights
- 📐 Framework Polishing: Organize article logic structure, ensure clear expression
- ✍️ Content Production: Write complete article based on framework, maintain user's style

**Trigger**:
```
I want to write XX
Help me organize my topic
How to form a framework
Help me organize my thoughts
/writing-assistant
```

---

#### 📝 [Weekly Report](./weekly-report)
**Description**: Helps users organize weekly reports with complete logic to showcase work value and boundaries

**Use Cases**:
- Need to organize a week's work content
- Want to clearly demonstrate work value and achievements
- Need to explain problems and challenges encountered
- Organize next week's priorities

**Core Features**:
- 📋 Material Collection: Guided dialogue to collect weekly work content
- 🗂️ Categorization: Flexibly choose appropriate module classification based on role
- 🔍 Information Supplement: Ask about background, results, value, status, and next steps
- ✅ Discussion & Adjustment: Confirm expression habits and logical completeness
- 📄 Document Output: Generate well-structured weekly report document

**Trigger**:
```
Write weekly report
Weekly report
Organize weekly report
Organize work
/weekly-report
```

---

#### 🎯 [Priority Judge](./priority-judge)
**Description**: Determine priorities from chaotic to-do items and decide what to do now

**Use Cases**:
- Have many things to do, don't know where to start
- Want to quickly figure out what to do today/this week
- Need to judge priorities based on objective criteria
- Avoid wasting time on things not thought through

**Core Features**:
- 📝 Collect To-dos: Record all things to do
- 🔍 Status Inquiry: Understand clarity and deadline of each item
- ⚖️ Priority Judgment: Make decisions based on clarity and deadline
- 🎯 Focus Action: Focus on only 1-2 most important things each time
- 📋 Documentation: Generate priority list document

**Trigger**:
```
I have many things to do
Help me sort it out
Prioritize
What should I do today
Let me review
/priority-judge
```

---

#### 🤝 [Thinking Partner](./thinking-partner)
**Description**: Accompany you to clarify the situation from chaos, lock core problems, break down bottlenecks, co-create solutions, and land actions

**Use Cases**:
- Facing complex problems and don't know where to start
- Have many ideas but can't sort out priorities
- Need someone to think through things with you
- Avoid getting lost in details and losing direction

**Core Features**:
- 📝 Information Gathering: Guided questioning to see the big picture
- 🎯 Lock Core Problem: Find the most critical one from a bunch of problems
- 🔍 Break Down Bottlenecks: Layer-by-layer questioning to find the real root cause
- 💡 Co-create Solutions: Supplement and refine based on your ideas
- ✅ Action Plan: Turn discussion conclusions into executable actions

**Trigger**:
```
I'm confused now, help me sort it out
I don't know what to do about this
Think through this problem with me
/thinking-partner
```

---

#### 🎨 [UI Design Assistant](./ui-design)
**Description**: UI style modification collaboration workflow. Reduce communication deviation and avoid wasting tokens through structured process

**Use Cases**:
- Need to modify page styles and layouts
- Adjust spacing, colors, component combinations
- UI detail optimization and fine-tuning
- Avoid guessing when changing code

**Core Features**:
- 📸 Screenshot Positioning: Confirm current state with screenshots
- 📐 Status Description: Draw current layout with ASCII
- 🎯 Solution Selection: Provide 2-3 visualized solutions
- 🛠️ Minimal Changes: Only change parts involved in selected solution
- 🔄 Iterative Refinement: Execute specific small modifications

**Trigger**:
```
Modify the layout of this page
Adjust the style here
The spacing is not quite right
/ui-design
```

---

#### 🔮 [Vision Exploration](./vision-exploration)
**Description**: Explore the ultimate potential of your ideas, outputting 4-6 dimensionally different end-state HTML prototypes

**Use Cases**:
- Have an idea and want to see what it could ultimately become
- Need divergent thinking to explore multiple possibilities
- Want to see end-state visions before writing a PRD
- Need investor-ready visual prototypes

**Core Features**:
- 🔍 Value Extraction: Repeatedly ask "why" to uncover the core need behind the requirement
- 🎯 Motivation Discovery: Identify real user scenarios
- 🔄 Evolution Derivation: Derive natural evolution path from minimum viable version
- 🎨 End-State Rendering: Output 4-6 self-contained HTML prototypes, each representing a different dimensional end-state
- 📊 Comparison Analysis: Generate evolution pathway diagram and end-state comparison table

**Trigger**:
```
Explore the end-state of this idea
What could this feature ultimately become
/vision-exploration
```

---

#### 🏷️ [Product Naming](./product-naming)
**Description**: Structured collaborative workflow to derive product names from brand essence, avoiding random name generation

**Use Cases**:
- Need to name a product/project/module
- Want to approach naming from a brand strategy perspective
- Need competitive naming research to support decisions
- Have a name but unsure if it's good

**Core Features**:
- 🔍 Soul Mining: Understand product essence, user persona, brand personality
- ⚡ Constraint Extraction: Extract core semantic elements, identify tension between requirements
- 🛤️ Route Divergence: Derive 2-4 different naming strategy directions
- 🏷️ Competitive Validation: Research naming patterns in the same space, back suggestions with data
- 📌 Final Confirmation: Output complete conclusion with name + slogan + decision rationale

**Trigger**:
```
Help me name this
Name this project
Product naming
/product-naming
```

---

#### 🔧 [Issue Triage](./issue-triage)
**Description**: GitHub Issue triage and response workflow for systematic analysis, root cause identification, and professional replies

**Use Cases**:
- Received a GitHub Issue that needs analysis and response
- Unsure if an Issue is a bug, architectural limitation, or feature request
- Need to quantify fix costs for decision-making
- Want to write professional, honest user responses

**Core Features**:
- 🔍 Code Diagnosis: Trace the full call chain to find the real root cause
- 🏷️ Issue Classification: Distinguish Bug / Architectural Limitation / Feature Request / Usage Question
- ⚖️ Do/Don't Decision: Evaluate across 4 dimensions — change scope, impact area, test conditions, workaround feasibility
- ✍️ Draft Reply: Three-layer structure — explain intent, describe impact, outline plans
- 📮 Publish: Post comment, apply labels, record requirements

**Trigger**:
```
Help me handle this Issue
Analyze this bug report
/issue-triage
```

---

#### 🔍 [GitHub Repo Search](./github-repo-search)
**Description**: Help users search and filter GitHub open source projects, output structured recommendation reports

**Use Cases**:
- Looking for open source projects in a specific direction
- Need to compare multiple similar projects
- Want to understand technology stack selection options
- Looking for tools ready to use or for secondary development

**Core Features**:
- 📝 Requirement Convergence: Confirm topic, quantity, sorting mode, target form
- 🔍 Query Breakdown: 5-10 query groups covering synonyms, scenario words, technical terms
- 🏷️ Repository Classification: Framework/Application/Memory/MCP/Catalog/Vertical/Methodology layers
- 📊 Quality Refinement: Comprehensive weighted ranking (relevance/applicability/activity/maturity)
- 📋 Structured Report: Understandable, comparable, decision-ready, actionable candidate repository list

**Trigger**:
```
Help me find open source projects
Search GitHub for XX
Looking for repositories in XX direction
Open source project recommendations
/github-search
```

---

#### 🔍 [Explain Code](./explain-code)
**Description**: Explain code using "analogy + ASCII diagram" to make complex execution flows crystal clear

**Use Cases**:
- Need to understand how an unfamiliar piece of code works
- Want to explain a codebase or execution flow to others
- Encounter complex concepts that are hard to grasp
- Need to identify common pitfalls and misconceptions

**Core Features**:
- 🌀 Analogy First: Compare code to everyday objects to lower the barrier to understanding
- 🖼️ ASCII Diagrams: Visualize flows, structures, and relationships with ASCII art
- 📋 Step-by-step: Explain each step of code execution with clear logic
- ⚠️ Flag Pitfalls: Highlight common mistakes and easy-to-miss traps

**Trigger**:
```
How does this code work?
Help me understand this function
Explain the execution flow of this codebase
/explain-code
```

---

#### 📜 [Paper Write](./paper-write)
**Description**: Full-process writing assistant for undergraduate and master's theses, auto-detecting STEM vs. liberal arts, covering outline review, chapter imitation, polishing, and references

**Use Cases**:
- Need to review or optimize thesis outline (STEM or liberal arts)
- Need to imitate introduction, abstract, experiment chapters, etc.
- Need literature review, case analysis, policy suggestions (liberal arts)
- Thesis polishing, anti-AIGC detection, Chinese-English translation
- Reference formatting in GB/T 7714 standard

**Core Features**:
- 📋 Outline Review: STEM/liberal arts separately adapted, structural logic check
- ✍️ Chapter Imitation: Introduction / abstract / experiment / literature review / case analysis / policy suggestions
- 📚 References: GB/T 7714 format acquisition and merging
- 🖊️ Polish & Reduce AI: General / experiment / liberal arts three modes, anti-AIGC
- 🌐 Translation: Academic-style bidirectional translation, zero information loss
- 📊 Structured Extraction: Extract structured info from thesis for defense PPT

**Trigger**:
```
Help me review this thesis outline
Imitate my experiment chapter based on this sample paper
This reads like AI, help me polish it
Find representative RLHF papers and give me BibTeX
/paper-write
```

---

#### 🎞️ [PPT Gen Drawio](./pptgen-drawio)
**Description**: Generate multi-page Draw.io PPT from thesis or presentation content, supporting thesis defense and general presentation modes, auto-export to .pptx

**Use Cases**:
- Need to create thesis defense / opening / pre-defense PPT
- Need to create work reports, product presentations, or speech slides
- Want to quickly generate multi-page slides, skipping manual layout
- Have a custom PPTX template and want to generate slides in that style

**Core Features**:
- 🎨 5 Styles: Classic Academic / Modern Minimal / Warm Academic / Tech Modern / Custom Template
- 📑 Dual Mode: Thesis defense (cover→TOC→background→method→experiment→conclusion) and general presentation
- 📐 16:9 Standard: Strict 1920×1080 canvas, correct coordinate system, globally unique IDs
- 🛠️ Auto Export: Automatically runs drawio2pptx to output .pptx after generating .drawio
- ✅ Self-validation Script: Built-in XML format check to prevent common pitfalls

**Trigger**:
```
Make a defense PPT, my thesis is at xxx
Generate a presentation PPT from this outline
/pptgen-drawio
```

---

#### 🖼️ [Drawio Diagram](./drawio-diagram)
**Description**: Generate standard Draw.io (.drawio) diagrams, supporting both from-scratch generation (model architectures / flowcharts) and style migration (replicating a reference image's style)

**Use Cases**:
- Need to generate architecture diagrams for deep learning models (Transformer, CNN, etc.)
- Need to draw algorithm flowcharts, data flow diagrams, system architecture diagrams
- Have a reference image and want to generate a new diagram in its style
- Need to export PNG/SVG/PDF for use in papers

**Core Features**:
- 🏗️ From Scratch: Model architecture diagrams, algorithm flowcharts, receptive field illustrations, etc.
- 🎨 Style Migration: Upload reference image + content description, generate new diagram matching the reference's layout/colors
- 📐 XML Compliance: Strict tag closure, globally unique IDs, special character escaping — opens directly in Draw.io
- 📤 Export Ready: Includes diagram description and usage guide with paper citation examples

**Trigger**:
```
Draw a Transformer architecture diagram
Create an algorithm flowchart
Generate a new diagram in the style of this reference image
/drawio-diagram
```

---

#### 🗂️ [Codegen Diagram](./codegen-diagram)
**Description**: Generate Draw.io diagrams from the current project/codebase, supporting tech stack diagrams, system architecture diagrams, data structure diagrams, and E-R diagrams

**Use Cases**:
- Need to visualize the current project's technology stack
- Need to generate a layered system architecture diagram
- Need to generate data structure or entity relationship diagrams from code
- Need diagram support for thesis defense or project presentation

**Core Features**:
- 🔧 Tech Stack Diagram: Auto-identify project technology choices, generate component relationship diagram
- 🏛️ System Architecture: Layered structure and call flow visualization
- 🗃️ Data Structure Diagram: Table structure and entity field relationship diagrams
- 🔗 E-R Diagram: Database entity relationship diagram with primary/foreign key annotations
- 🎨 Consistent Style: Primary color #3366CC, standard connector lines, Helvetica font

**Trigger**:
```
Draw a tech stack diagram for the current project
Draw our system's four-layer architecture
Generate a data structure diagram from the code
Draw an E-R diagram from the database table structure
/codegen-diagram
```

---

#### 📄 [Codegen Doc](./codegen-doc)
**Description**: Generate thesis chapters, project documentation, key issue lists, and resume project descriptions based on the current project/codebase

**Use Cases**:
- Need to generate a system design chapter for a thesis from project code
- Need to organize project structure and module documentation
- Need to compile technical difficulties and pending issues
- Need to write the current project as a resume project experience

**Core Features**:
- 📋 Thesis Chapter: System overall/detailed design chapters, evidence-based without fabrication
- 📁 Project Overview: Organize project overview, modules, and tech stack in a specified format
- ⚡ Key Issues: Technical difficulties, unresolved problems, and project risk lists
- 📝 Resume Description: Output project experience in resume format, highlighting technical highlights

**Trigger**:
```
Generate a system design chapter based on the current project
Organize our project in this format
List the technical difficulties in this project
Write the current project as a resume project experience
/codegen-doc
```

---

#### ⚙️ [Dev Workflow](./dev-workflow)
**Description**: Unified five-step development workflow covering requirement understanding, solution design, code implementation, code review, and bug fixing

**Use Cases**:
- Have a new feature idea and need to start from requirements analysis
- Need to do technical solution design and architecture decisions
- Ready to start coding a specific feature
- Need code review to ensure quality
- Encountering errors / exceptions / test failures that need fixing

**Core Features**:
- 📝 Requirements: Extract functional needs and constraints from descriptions, produce requirement docs
- 🏗️ Design: Technical solution, architecture design, module breakdown
- 💻 Implementation: Write code following the plan, deliver step by step
- 🔍 Code Review: Multi-language code quality / security / standards check
- 🐛 Bug Fixing: Root cause localization, reproduction analysis, minimal fix
- 🔗 Flow Chaining: Automatically prompt to proceed to the next stage after each step

**Trigger**:
```
I want to build a XXX, help me organize the requirements
Help me design a technical solution
Start writing code based on the plan
Help me review this code
There's an error here: xxx
/dev-workflow
```

---

#### 📊 [MD Report Summary](./md-report-summary)
**Description**: Generate high-quality Markdown weekly reports, work summaries, reviews, and introductions; web search when no draft exists, polish when draft is provided

**Use Cases**:
- Need to quickly write a weekly report
- Need to write work reports, quarterly summaries, or project retrospectives
- Have a draft that needs organizing and polishing
- Need a project introduction or personal bio

**Core Features**:
- 🔍 No-Draft Mode: Confirm topic → web search for background → write from template, content is well-sourced
- 📝 With-Draft Mode: Preserve all original data/tables/images, only polish sentences and fill gaps
- 📊 Specific Data: Keep quantified data (time/count/percentage), avoid filler phrases like "continue to advance"
- 🗂️ Clear Structure: Subheadings for different business modules, key conclusions highlighted in blockquotes
- ✅ Ready to Use: Markdown format, copy-paste ready

**Trigger**:
```
Help me write this week's report
Write a Q1 work summary
Write a project retrospective
Write a project introduction
/md-report-summary
```

---

#### ✍️ [WeChat Article Writer](./wechat-article-writer)
**Description**: Full-process WeChat/social media content creation supporting article writing, cover images, body illustrations, and style extraction with 9 built-in writing styles

**Use Cases**:
- Need to write a WeChat article or technical blog post
- Need to generate WeChat cover images, Bilibili covers, or Xiaohongshu graphics
- Need body illustrations for articles (step diagrams / flowcharts / demo images)
- Want to analyze a viral article's writing style and extract reusable rules

**Core Features**:
- 🖊️ Article Writing: Web search for latest info, 9 styles to choose from, story-driven openings
- 🖼️ Cover / Illustrations: Generate Draw.io format cover images or step diagrams, colors unified with article
- 🔍 Style Extraction: Analyze sample articles, output style portrait, 15-30 executable rules, replication Prompt
- 📢 Title Generation: 5 viral-style backup titles covering pain points / numbers / emotions / suspense
- 🎨 9 Styles: Default / Viral / Checklist / Resource Roundup / Personal Review / Contrarian / Identity Resonance / Storytelling / Deep Essay

**Trigger**:
```
Write a WeChat article about XX
Write about Vibe Coding in viral style
Generate a cover image for this article, 16:9
Analyze the writing style of this article
/wechat-article-writer
```

---

#### 🌐 [Translate MD to ZH](./translate-md-to-zh)
**Description**: Translate English Markdown files into Simplified Chinese while preserving Markdown structure, code blocks, links, and file paths, outputting a -zh.md sibling file

**Use Cases**:
- Need to localize an English README or documentation into Chinese
- Translate technical documents while keeping code blocks and links intact
- Batch process Markdown format documentation files

**Core Features**:
- 🌐 Structure Preserved: Code blocks, inline code, link paths, image paths, and HTML tags are never translated
- ✍️ Accurate Translation: Headings, body text, tables, lists, and image alt text translated naturally
- 📁 Safe Output: Generates a `-zh.md` file in the same directory, never overwrites the source
- 🔒 Quality Assured: Consistent technical terminology, complete content, no translator notes added

**Trigger**:
```
Translate this README into Chinese
/translate-md-zh README.md
/translate-md-zh docs/getting-started.md
```

---

#### 🚁 [Flyfollow Training Analysis](./flyfollow-training-analysis)
**Description**: Automatically diagnose SKRL flyfollow task training logs, analyzing reward trends, convergence, success rates, termination causes, and more

**Use Cases**:
- Want to know if the current flyfollow training is converging normally
- Need to diagnose abnormal reward curves (stalled growth / penalty-dominated / oscillating)
- Want to analyze termination cause distribution (flew too high / out of bounds / timeout)
- Compare training quality across multiple runs

**Core Features**:
- 📈 Reward Trends: Analyze if total reward is dominated by penalties, if tracking/velocity rewards are reachable
- ✅ Convergence Judgment: Determine if training is improving / stalled / unstable
- 📊 Success Rate Analysis: Whether `sustained_success_rate` is genuinely rising
- 🏔️ Height Issues: Whether height consistently stays too high, not converging to `desired_height`
- 🔍 Termination Causes: Distribution analysis of fly_high / fly_low / out_of_bounds / timeout
- 🛠️ Script-driven: Automatically runs analysis script and integrates with params/env.yaml config for comprehensive interpretation

**Trigger**:
```
Analyze the latest training results
Check if this training run converged
Diagnose the reward curves
/flyfollow-training-analysis
```

---

#### 🔄 [Skill Prompt Convert](./skill-prompt-convert)
**Description**: Bidirectional conversion between SKILL.md and chat-box Prompt formats with zero information loss

**Use Cases**:
- Have a SKILL.md and need to convert it to a Prompt that can be copied into a chat box
- Have a useful Prompt and want to turn it into a Skill that agents can auto-trigger
- Need to organize and standardize Skill or Prompt formats

**Core Features**:
- 🔄 Bidirectional: Skill → Prompt and Prompt → Skill both supported
- 📋 Conversion Notes: Outputs mapping relationship description for easy understanding
- 🏷️ Naming Standards: name must be English lowercase with hyphens; description must include "when to use" and "what it does"
- ✅ Format Validation: Ensures YAML frontmatter format is correct (opens and closes with `---`)
- 🔒 Complete Info: Core logic, steps, and constraints are never omitted

**Trigger**:
```
Convert this Skill into a chat-box Prompt
Convert this Prompt into SKILL.md format
/skill-prompt-convert
```

---

#### 🛠️ [Skill Create](./skill-create)
**Description**: Guide users through creating high-quality Agent Skills, covering the full workflow of requirements, design, implementation, and verification for Claude Code, Cursor, and similar tools

**Use Cases**:
- Have a repetitive workflow and want to solidify it into an auto-triggering Skill
- Don't know how to write SKILL.md and need guidance
- Want to learn Skill best practices (description writing, file structure, script usage)
- Want to organize an existing workflow into a standard Skill

**Core Features**:
- 🔍 Requirements Discovery: Guide clarification of Skill purpose, trigger scenarios, and storage location (personal vs. project)
- 🎯 Description Optimization: Third person, includes WHAT and WHEN, keyword-driven triggering
- 🗂️ File Structure: Standard directory layout of SKILL.md + reference + examples + scripts
- ✂️ Conciseness Principle: Under 500 lines, progressive disclosure, consistent terminology, avoid over-explanation
- ✅ Quality Checklist: Complete checklist ensuring the Skill is discoverable, correctly structured, and has concrete examples

**Trigger**:
```
I often review papers, help me create a Skill for it
Turn this workflow into a Skill
/skill-create
```

---

### 🚀 Quick Start

#### Installation

**Using Codex or Claude Code CLI**

If you're using Codex or Claude Code CLI, simply tell the AI:

```
Install this GitHub repository: https://github.com/yourusername/云舒的Skills搭子们
```

The AI will automatically install it for you!

**Manual Installation**

Clone this repository to your local Skills directory:

```bash
# Claude Code default Skills directory is usually ~/.claude/skills/
cd ~/.claude/skills/

# Clone this repository
git clone https://github.com/yourusername/云舒的Skills搭子们.git
```

Alternatively, you can copy individual Skills you need to your Skills directory.

#### Usage

In Claude Code CLI, you can use them by:

```bash
# Use Image Assistant
/image-assistant

# Use Thought Mining
/thought-mining

# Use PRD Doc Writer
/prd-doc-writer

# Use Design Exploration
/design-exploration

# Use Requirement Change Workflow
/req-change-workflow

# Use Lesson Builder
/lesson-builder

# Use Backlog Manager
/backlog-manager

# Use Project Map Builder
/project-map-builder

# Use Version Planner
/version-planner

# Use Writing Assistant
/writing-assistant

# Use Weekly Report
/weekly-report

# Use Priority Judge
/priority-judge

# Use Thinking Partner
/thinking-partner

# Use UI Design Assistant
/ui-design

# Use GitHub Repo Search
/github-search

# Use Vision Exploration
/vision-exploration

# Use Product Naming
/product-naming

# Use Issue Triage
/issue-triage

# Use Explain Code
/explain-code

# Use Paper Write
/paper-write

# Use PPT Gen Drawio
/pptgen-drawio

# Use Drawio Diagram
/drawio-diagram

# Use Codegen Diagram
/codegen-diagram

# Use Codegen Doc
/codegen-doc

# Use Dev Workflow
/dev-workflow

# Use MD Report Summary
/md-report-summary

# Use WeChat Article Writer
/wechat-article-writer

# Use Translate MD to ZH
/translate-md-zh

# Use Flyfollow Training Analysis
/flyfollow-training-analysis

# Use Skill Prompt Convert
/skill-prompt-convert

# Use Skill Create
/skill-create
```

Or simply describe your needs in conversation, and the relevant Skill will trigger automatically.

**📚 Check Usage Examples**

Want to learn how to use each Skill? Check out the [Usage Examples](./EXAMPLES.md) for detailed scenarios and expected outputs.

---

### 📂 Project Structure

```
.
├── README.md                    # Project documentation
├── LICENSE                      # MIT License
├── CHANGELOG.md                 # Changelog
├── EXAMPLES.md                  # Usage examples
├── image-assistant/             # Image Assistant
│   ├── SKILL.md                # Skill definition file
│   ├── stages/                 # Detailed stage descriptions
│   ├── templates/              # Style templates and layout templates
│   ├── examples/               # Usage examples
│   └── scripts/                # Batch image generation scripts
├── thought-mining/              # Thought Mining Assistant
│   ├── SKILL.md                # Skill definition file
│   ├── stages/                 # Detailed stage descriptions
│   ├── templates/              # Template files
│   └── examples/               # Usage examples
├── prd-doc-writer/             # PRD Doc Writer
│   ├── SKILL.md               # Skill definition file
│   ├── assets/                # Template resources
│   └── references/            # Reference docs and examples
├── design-exploration/         # Design Exploration
│   ├── SKILL.md               # Skill definition file
│   └── templates/             # Requirements summary template
├── req-change-workflow/        # Requirement Change Workflow
│   ├── SKILL.md               # Skill definition file
│   ├── references/            # Templates and checklists
│   └── scripts/               # Helper scripts
├── lesson-builder/             # Lesson Builder
│   └── SKILL.md               # Skill definition file
├── backlog-manager/            # Backlog Manager
│   └── SKILL.md               # Skill definition file
├── project-map-builder/        # Project Map Builder
│   └── SKILL.md               # Skill definition file
├── version-planner/            # Version Planner
│   └── SKILL.md               # Skill definition file
├── writing-assistant/          # Writing Assistant
│   ├── SKILL.md               # Skill definition file
│   ├── stages/                # Detailed stage descriptions
│   └── templates/             # Template files
├── weekly-report/             # Weekly Report
│   └── SKILL.md              # Skill definition file
├── priority-judge/            # Priority Judge
│   └── SKILL.md              # Skill definition file
├── thinking-partner/          # Thinking Partner
│   └── SKILL.md              # Skill definition file
├── ui-design/                 # UI Design Assistant
│   └── SKILL.md              # Skill definition file
├── github-repo-search/        # GitHub Repo Search
│   └── SKILL.md              # Skill definition file
├── vision-exploration/        # Vision Exploration
│   └── SKILL.md              # Skill definition file
├── product-naming/            # Product Naming
│   └── SKILL.md              # Skill definition file
├── issue-triage/              # Issue Triage
│   └── SKILL.md              # Skill definition file
├── explain-code/              # Explain Code
│   └── SKILL.md              # Skill definition file
├── paper-write/               # Paper Write
│   ├── SKILL.md              # Skill definition file
│   └── reference/            # Per-scenario detailed instructions
├── pptgen-drawio/             # PPT Gen Drawio
│   ├── SKILL.md              # Skill definition file
│   ├── ppt_template/         # PPT template directory
│   ├── scripts/              # Helper scripts
│   └── reference/            # Style reference files
├── drawio-diagram/            # Drawio Diagram
│   ├── SKILL.md              # Skill definition file
│   └── reference/            # Generation and style migration instructions
├── codegen-diagram/           # Codegen Diagram
│   ├── SKILL.md              # Skill definition file
│   └── reference/            # Per-diagram-type instructions
├── codegen-doc/               # Codegen Doc
│   ├── SKILL.md              # Skill definition file
│   └── reference/            # Per-document-type instructions
├── dev-workflow/              # Dev Workflow
│   ├── SKILL.md              # Skill definition file
│   └── reference/            # Per-step detailed instructions
├── md-report-summary/         # MD Report Summary
│   ├── SKILL.md              # Skill definition file
│   └── reference/            # Template files
├── wechat-article-writer/     # WeChat Article Writer
│   ├── SKILL.md              # Skill definition file
│   └── reference/            # Writing style files, cover/illustration guides
├── translate-md-to-zh/        # Translate MD to ZH
│   └── SKILL.md              # Skill definition file
├── flyfollow-training-analysis/ # Flyfollow Training Analysis
│   ├── SKILL.md              # Skill definition file
│   └── scripts/              # Training log analysis scripts
├── skill-prompt-convert/      # Skill Prompt Convert
│   └── SKILL.md              # Skill definition file
└── skill-create/              # Skill Create
    └── SKILL.md              # Skill definition file
```

---

### 🤝 Contributing

Issues and Pull Requests are welcome! If you have any suggestions or find bugs, please feel free to let me know.

---

### 📄 License

This project is open source under the [MIT License](./LICENSE).

---

### 📧 Contact

For questions or suggestions, please contact via GitHub Issues.

---

Made with ❤️ by Yunshu
