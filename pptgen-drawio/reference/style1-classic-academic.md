# 风格一：经典学术 / 商务严谨（来源：通用ppt模板1.pptx）

## 真实样式数据来源
- 源文件：`通用ppt模板1.pptx`（13 页）
- 画布：1920 × 1080（16:9）

## 配色系统（2026 顶级咨询风）

参考 McKinsey / 顶级学术答辩审美，遵循 **60-30-10 法则**：主色 60%（深海军蓝）+ 辅色 30%（浅石板灰/白）+ 强调色 10%（金铜色）。

| 角色 | 色值 | 说明 |
|------|------|------|
| 主色 / 顶栏 / 大色块 | `#1B2A4A` | 深海军蓝，权威、沉稳，替代原 `#2C5160` |
| 辅色 / 分隔线 / 次要装饰 | `#C9A84C` | 金铜色，高级感强调，替代原大红 `#FF0000` |
| 页面背景 | `#F7F8FA` | 冷白/极浅灰，比纯白更耐看 |
| 正文文字 | `#1A1A2E` | 近黑深蓝，比纯黑更柔和 |
| 次级信息（副标题/日期/人名） | `#4A5568` | 中性石板灰，层次分明 |
| 内容页底部装饰条 | `#E2E8F0` | 浅灰线，低调区隔 |

> **替换逻辑**：原配色 `#2C5160`（混浊蓝绿）→ `#1B2A4A`（纯正海军蓝）；`#FF0000`（刺眼红）→ `#C9A84C`（金铜）。视觉立即从「政府感」升级为「咨询/顶刊感」。

## 字体规范

| 用途 | 字体 | 字号 | 说明 |
|------|------|------|------|
| 封面主标题 | `微软雅黑` | 44 pt，加粗 | 中文场景更清晰 |
| 英文标题 / 副标题 | `Georgia` | 36–40 pt，部分加粗 | 衬线字体增加学术感 |
| 内容页标题 | `微软雅黑` | 36–40 pt，白色嵌顶栏 | 左对齐 |
| 正文内容 | `微软雅黑` | 18–22 pt | 中文正文，替代宋体 |
| 英文正文 / 数据 | `Calibri` | 18–24 pt | 英文段落 |
| 次级信息（人名/日期） | `Calibri` | 16–20 pt，`#4A5568` | 封面落款 |

## 版式规则（Draw.io 实现要点）

### 封面页
- 顶部 `#1B2A4A` 色块：全宽 × 120 px
- 顶部色块下方：`#C9A84C` 金色细线分隔条（高度 6 px）
- 左侧小方块装饰：`fillColor=#C9A84C`，用于修饰汇报人、单位信息行
- 主标题：`微软雅黑`，44 pt 加粗，`#1A1A2E`，竖向居中偏上
- 背景：`#F7F8FA`（冷白）

### 内容页
- 顶部同样使用 `#1B2A4A` 色块（高 120 px）+ `#C9A84C` 金线（高 6 px）
- 标题文字嵌入顶部色块内，左对齐，`微软雅黑`，40 pt，白色
- 正文区：`微软雅黑`，18–22 pt，`#1A1A2E`；关键词用 `#C9A84C` 金色强调
- 底部细线：`#E2E8F0`，全宽 × 4 px，区隔页码区

### 节标题（过渡）页
- 全宽 `#1B2A4A` 大色块铺满整页
- 白色大字节标题居中，可叠加半透明 `#C9A84C` 数字水印

### 通用装饰
- 小方块：`14 × 30 px`，`fillColor=#C9A84C`，无描边，段落标记
- 底部右侧：`Calibri`，日期信息，`#4A5568`

## 文字换行要点（重要）

Draw.io 文字默认**不换行**，必须同时满足以下三条才能正常折行：

1. **style 加 `whiteSpace=wrap`**：所有含文字的 cell 都必须加，缺一不可
2. **容器高度要足够**：正文行高约 1.4 倍字号，多行文字需预留 `行数 × 字号 × 1.5` 的高度
3. **不要用 `overflow=hidden`**：会裁掉溢出文字

> 高度参考：单行 ≈ 字号×2，两行 ≈ 字号×3.5，三行 ≈ 字号×5，宁可偏大不要偏小。

## Draw.io XML 关键样式片段

```xml
<!-- 页面背景（冷白） -->
<mxCell id="bg" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#F7F8FA;strokeColor=none;" vertex="1" parent="1">
  <mxGeometry x="0" y="0" width="1920" height="1080" as="geometry"/>
</mxCell>

<!-- 顶部深海军蓝色块 -->
<mxCell id="topbar" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#1B2A4A;strokeColor=none;" vertex="1" parent="1">
  <mxGeometry x="0" y="0" width="1920" height="120" as="geometry"/>
</mxCell>

<!-- 金色分隔线 -->
<mxCell id="line" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#C9A84C;strokeColor=none;" vertex="1" parent="1">
  <mxGeometry x="0" y="120" width="1920" height="6" as="geometry"/>
</mxCell>

<!-- 标题文字（嵌入顶色块内，单行高度=色块高度） -->
<mxCell id="title" value="  01. 标题内容" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;fontSize=40;fontStyle=1;fontColor=#FFFFFF;fontFamily=微软雅黑;" vertex="1" parent="1">
  <mxGeometry x="0" y="0" width="1920" height="120" as="geometry"/>
</mxCell>

<!-- 左侧小方块装饰（金铜色） -->
<mxCell id="badge" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#C9A84C;strokeColor=none;" vertex="1" parent="1">
  <mxGeometry x="120" y="210" width="8" height="36" as="geometry"/>
</mxCell>

<!-- 正文内容（多行需预留足够高度，verticalAlign=top） -->
<mxCell id="body" value="正文内容，支持换行显示。" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=left;verticalAlign=top;fontSize=20;fontColor=#1A1A2E;fontFamily=微软雅黑;" vertex="1" parent="1">
  <mxGeometry x="160" y="180" width="1680" height="720" as="geometry"/>
</mxCell>

<!-- 底部装饰细线 -->
<mxCell id="botline" value="" style="rounded=0;whiteSpace=wrap;html=1;fillColor=#E2E8F0;strokeColor=none;" vertex="1" parent="1">
  <mxGeometry x="0" y="1040" width="1920" height="4" as="geometry"/>
</mxCell>

<!-- 底部页码/日期（次级信息） -->
<mxCell id="footer" value="汇报人：xxx   |   2026.03" style="text;html=1;whiteSpace=wrap;strokeColor=none;fillColor=none;align=right;verticalAlign=middle;fontSize=18;fontColor=#4A5568;fontFamily=Calibri;" vertex="1" parent="1">
  <mxGeometry x="1400" y="1044" width="480" height="36" as="geometry"/>
</mxCell>

<!-- 关键词金色强调（正文内使用 HTML） -->
<!-- 在 value 字段中用 <font color="#C9A84C"><b>关键词</b></font> -->
```