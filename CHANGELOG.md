# 更新日志 / Changelog

所有重要的项目变更都会记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased]

### 新增 / Added

- 🔀 **README2.md 内容融入 README.md**（2026-03-13）
  - 新增「🖼️ 效果预览」章节：答辩 PPT 和公众号封面效果截图
  - 新增「🗂️ 分类速查」章节：按场景归组的速查表（论文 / 开发流程 / 自媒体 / 周报 / 项目文档 / 工具扩展）
  - 扩充「安装方式」：新增 Cursor 个人级/项目级安装路径，补充 Claude Code、Codex、Cursor、Trae、GitHub Copilot、OpenClaw 官方文档链接
  - 新增「🌐 更多公开 Skills 资源」章节：合集网站（7 个）+ 源码仓库（7 个）推荐表格
  - README2.md 内容已完整迁移，原文件可归档删除

- 📖 **README 文档全量补全 + README2.md 融合**（2026-03-13）
  - 补全 13 个此前缺失的 Skills 中英双语说明（explain-code / paper-write / pptgen-drawio / drawio-diagram / codegen-diagram / codegen-doc / dev-workflow / md-report-summary / wechat-article-writer / translate-md-to-zh / flyfollow-training-analysis / skill-prompt-convert / skill-create）
  - 新增「🖼️ 效果预览」「🗂️ 分类速查」「🌐 更多公开 Skills 资源」三个章节
  - 扩充安装方式：Cursor 个人/项目级路径 + 7 个 Agent 工具官方文档链接
  - 同步更新快速开始命令列表与项目结构目录树（中英各增 13 条）

- 🔍 **代码解释助手** (explain-code)
  - 类比 + ASCII 图解释代码执行流程，适合讲解代码库、流程、复杂概念
  - 四步固定格式：类比开头 → ASCII 图解 → 逐步讲解 → 指出陷阱

- 📜 **学位论文撰写助手** (paper-write)
  - 本科 & 硕士论文全流程，理工（science-\*）/ 文科（liberal-\*）自动区分
  - 支持大纲审核、结构仿写（绪论/摘要/实验/文献综述/案例分析/对策建议）
  - 支持参考文献（GB/T 7714）、润色、缩写/扩写、防 AIGC、中英互译、结构化信息提取

- 🎞️ **PPT 生成助手** (pptgen-drawio)
  - 论文答辩 & 通用汇报双模式，输出 Draw.io 多页 XML，自动调用 drawio2pptx 导出 .pptx
  - 五种内置风格（经典学术/现代极简/暖色学术/科技明快/自定义模板）
  - 内置 10 条已知坑防护（id 唯一、坐标归零、文字溢出、浮层遮挡等）

- 🖼️ **Draw.io 图表生成** (drawio-diagram)
  - 从零生成深度学习模型架构图、算法流程图、感受野示意图等
  - 支持风格迁移：参考图 + 内容描述 → 按参考图排版/配色生成新图
  - 输出严格合规的 mxGraph XML，可直接在 Draw.io 打开编辑

- 🗂️ **代码生成项目图表** (codegen-diagram)
  - 基于当前代码仓库自动生成技术栈图、系统架构图、数据结构图、E-R 图
  - 统一配色方案（主色 #3366CC），输出可导入 Draw.io 的 .drawio 文件

- 📄 **代码生成项目文档** (codegen-doc)
  - 基于当前代码仓库生成论文系统章节、项目梳理文档、重点问题清单、简历项目描述
  - 不编造：所有内容有据可依，严格从代码/注释/README 中抽取

- ⚙️ **开发流程五步法** (dev-workflow)
  - 统一入口，自动匹配五步之一：需求理解 → 方案设计 → 代码实现 → 代码审查 → Bug 修复
  - 每步完成后提示进入下一阶段，支持跨步骤串联

- 📊 **周报汇报总结生成** (md-report-summary)
  - 无草稿：确认主题 → 联网搜索 → 按模板生成；有草稿：保留原数据/表格/图片，润色补充
  - 支持周报、工作汇报、总结/复盘、项目介绍/个人简介四种类型

- ✍️ **公众号创作助手** (wechat-article-writer)
  - 撰写文章、封面图、正文插图、风格提取四条执行路径
  - 内置 9 种写作风格：默认/高流量/清单体/资源盘点/个人实测/认知颠覆/身份共鸣/故事化/深度随笔
  - 风格提取输出风格画像 + 15-30 条可执行规则 + 复刻 Prompt

- 🌐 **Markdown 英译中** (translate-md-to-zh)
  - 将英文 .md 文件译为简体中文，输出同目录 -zh.md 文件
  - 保留代码块、内联代码、链接路径、图片路径、HTML 标签不变

- 🚁 **飞行跟随训练分析** (flyfollow-training-analysis)
  - 自动诊断 `logs/skrl/marl_flyfollow/` 下的 TensorBoard 训练日志
  - 分析奖励趋势、收敛状态、成功率、终止原因（飞太高/出界/超时）分布

- 🔄 **Skill 与 Prompt 互转** (skill-prompt-convert)
  - SKILL.md ↔ 聊天框 Prompt 双向转换，核心信息零丢失
  - 输出转换说明（映射关系）+ 转换结果（可直接粘贴使用）

- 🛠️ **Skill 创建助手** (skill-create)
  - 引导用户经历需求收集 → 设计 → 实现 → 验证全流程创建高质量 Skill
  - 覆盖 description 写法、文件结构、脚本使用等最佳实践，内置完整质量 Checklist

- 📚 **课程构建器** (lesson-builder)
  - 讨论驱动：先共创大纲，确认后再写课件，避免大量返工
  - 支持快速共创与严格确认两种模式，最少文档原则

- 🗺️ **项目目录地图构建器** (project-map-builder)
  - 生成或增量更新 PROJECT_MAP.md，必须先询问扫描范围，不默认全仓扫描
  - 自动识别入口/配置/服务线程等关键文件，不确定处显式标注"假设"或"未确认"

- 📅 **版本规划助手** (version-planner)
  - 将产品需求拆解为渐进式版本规划（V0.1 MVP → V1.0）
  - 价值优先原则：优先解决最痛痛点，MVP 设计 2-3 天可跑通，每版本均可独立使用

- ✍️ **写作助手** (writing-assistant)
  - 智能诊断观点清晰度：清晰走「框架→内容」，模糊走「挖掘→选题→框架→内容」
  - 覆盖从零散想法到完整文章的全链路

- 📝 **周报写作助手** (weekly-report)
  - 引导式对话收集本周工作素材，灵活分类，追问背景/结果/价值/状态/下一步
  - 生成结构清晰的周报文档

- 🎯 **优先级判断助手** (priority-judge)
  - 基于清晰度 × Deadline 双维度判断优先级，每次聚焦 1-2 件最重要的事
  - 生成可归档的优先级清单文档

- 🔮 **终局愿景探索** (vision-exploration)
  - 反复追问"为什么"找核心诉求，从最小可行版推导自然演进路径
  - 输出 4-6 个自包含 HTML 原型 + 演进路径图 + 终局对比表

- 🏷️ **产品命名助手** (product-naming)
  - 六步法：灵魂挖掘 → 约束提取 → 路线发散 → 方向选择 → 竞品验证 → 最终确认
  - 输出名称 + Slogan + 决策依据完整结论

- 🔧 **Issue 协作处理** (issue-triage)
  - 四步法：代码诊断 → 问题定性（Bug/架构局限/功能请求/使用疑问）→ 做不做决策 → 起草回复
  - 三层回复结构：解释意图 → 说明影响 → 交代计划

- 📦 **需求池管理** (Backlog Manager)
  - 6 步结构化流程：收集 → 归类 → 写入 → 整理 → 筛选 → 归档
  - 痛点驱动，不做假设性规划
  - AI 整理，用户决策
  - 支持需求合并和状态升档
  - 基于频率/可绕过性/ROI 的筛选分析

- 🎨 **新功能设计探索** (Design Exploration)
  - 7 步结构化流程：需求收敛 → 技术调研 → ASCII 批量探索 → HTML 设计稿 → 全状态覆盖 → 需求总结
  - 一次出 5-8 个 ASCII 方案供选择
  - 全状态覆盖（正常/加载/空态/错误/边界）
  - 交互行为规则表，前端开发直接对照实现
  - 产出 3 个文件：需求总结.md、设计稿.html、全状态设计参考.html

- 🤝 **思考拍档** (Thinking Partner)
  - 5 步结构化流程：信息获取 → 锁定核心问题 → 拆解卡点 → 共创解法 → 落地计划
  - 基于"主次矛盾"思维模型，帮用户找到核心问题
  - 严格的阶段里程碑确认机制
  - 共创式解法讨论，不是单向给答案
  - 落地计划包含"做什么"和"不做什么"

- 🎨 **UI 样式修改助手** (UI Design)
  - 结构化 UI 修改协作流程
  - ASCII 布局图辅助沟通
  - 方案选择机制（2-3 个可视化方案）
  - 最小改动原则，避免过度修改
  - 微调迭代流程

- 🎨 **配图助手** (Image Assistant)
  - 5 个完整的工作阶段：需求澄清、配图规划、文案定稿、提示词封装、迭代润色
  - 统一风格的 16:9 信息图提示词生成
  - 多种配图模板（封面、对比图、洞察卡片、漫画等）
  - 批量生图脚本支持
  - 完整的风格块和 API 配置模板

- 🔍 **GitHub 开源项目搜索助手** (GitHub Repo Search)
  - 四环节九步结构化流程：需求收敛 → 检索执行 → 质量精炼 → 交付迭代
  - 5-10 组检索词拆解，平衡召回率与相关性
  - 仓库归属类型分类（框架层/应用层/记忆层/MCP层/目录清单层等）
  - 综合权重排序（相关性/场景适用性/活跃度/工程成熟度）
  - 结构化推荐报告，可理解、可比较、可决策、可直接行动

### 计划中 / Planned
- 更多示例和最佳实践文档
- 视频教程
- 社区贡献的 Skills

---

## [1.0.0] - 2026-01-19

### 新增 / Added
- 🧠 **思维挖掘助手** (Thought Mining)
  - 5 个完整的工作阶段：思维挖掘、选题确定、观点验证、写作辅助、最终审核
  - 洞察记录模板和写作记录模板
  - 完整案例参考

- 📋 **PRD 文档撰写助手** (PRD Doc Writer)
  - 以用户故事为核心的需求文档撰写流程
  - ASCII 线框图支持
  - Mermaid 图表集成（流程图、状态图、时序图）
  - 阶段性确认机制
  - PRD 版本管理（总集/台账）

- 🔄 **需求变更工作流** (Requirement Change Workflow)
  - 7 步标准化变更流程
  - 需求澄清模板
  - 回归测试清单
  - 决策日志模板
  - 影响扫描脚本

### 文档 / Documentation
- 中英双语 README
- MIT 开源许可证
- 项目结构说明
- 快速开始指南
- 支持 Codex 和 Claude Code CLI 安装

---

## 版本说明 / Version Notes

### [Unreleased]
- 尚未发布的变更

### [1.0.0] - 2026-01-19
- 首次发布
- 包含 3 个核心 Skills

---

[Unreleased]: https://github.com/你的用户名/云舒的Skills搭子们/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/你的用户名/云舒的Skills搭子们/releases/tag/v1.0.0
