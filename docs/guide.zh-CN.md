# 使用指南

[返回首页](../README.zh-CN.md) · [English](guide.md)

# Research Presentation Skill

[English](../README.md)

这是一个开源 Codex Skill，用于把**研究项目目录**或**单篇学术 PDF**转换成证据可追溯、可独立运行的 HTML 研究演示。

它把演示制作视为完整的科研流程，而不只是幻灯片排版：

```text
叙事门禁 → 证据映射 → 演示编排 → 页面构建 → 视觉验收
```

## 核心能力

- 支持研究项目目录和单篇 PDF 两种输入模式。
- 项目模式默认完成可审阅草稿；用户要求先讨论或存在关键叙事歧义时，使用 **Narrative Gate（叙事确认流程）**。
- 将拟定的结论、术语和故事线记录到草稿状态的 `NARRATIVE-CONTRACT.md`；只有用户实际确认后才标记为冻结。
- 在 `presentation-manifest.yml` 中记录可见结论、数字、图表、引用和资源来源。
- 输出不需要构建步骤、可直接打开的交互式 HTML 演示。
- 强制表头和单元格单行显示，并检查底纹、方法突出与缩写解释。
- 使用 `LANGUAGE-AUDIT.md` 统一术语并审计 claim 强度。
- 检查本地资源、页面与 manifest 一致性、遗留占位符、基础可访问性和离线运行条件。

Narrative Gate 已直接集成在仓库中，不依赖用户另外安装 `grilling` skill。

## 输入模式

### 项目目录

适用于组会、研究进度汇报、投稿定位汇报和答辩型演示。Skill 会先检查项目事实，记录拟定的叙事并制作可审阅草稿。只有用户明确要求先讨论，或存在影响正确性的关键选择时，才使用叙事确认流程；普通草稿不要求冻结契约。

### 单篇 PDF

适用于论文解读、教程、批判性阅读和相关工作汇报。所有结论和视觉材料都需要追溯到 PDF 页码、章节、图或表。只有用户要求时才引入外部来源，并与原 PDF 证据分开登记。

## 安装

克隆仓库，并把 Skill 目录链接到 Codex：

```bash
git clone https://github.com/DELONG-L/Research-Presentation-Skill.git
cd Research-Presentation-Skill
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)/research-presentation" "${CODEX_HOME:-$HOME/.codex}/skills/research-presentation"
```

如果系统不支持符号链接，可以直接把 `research-presentation/` 复制到 `${CODEX_HOME:-$HOME/.codex}/skills/`。

如果 Skill 没有立即出现，请重启 Codex 或打开一个新任务。

## 使用方法

可以显式调用 `$research-presentation`，也可以直接使用符合场景的自然语言：

```text
使用 $research-presentation 把这个研究项目制作成明天组会使用的 HTML 演示。

使用 $research-presentation 把这篇 PDF 整理成一场 15 分钟的论文汇报。

根据实验记录审计并修正这个现有研究演示中的过度 claim。
```

默认输出结构：

```text
presentation/
├── index.html
├── presentation-manifest.yml
├── LANGUAGE-AUDIT.md
├── NARRATIVE-CONTRACT.md    # 项目模式
└── assets/
```

## 可选演示骨架

仓库内置脚本可以生成离线 HTML 骨架和溯源文件：

```bash
python3 research-presentation/scripts/scaffold_presentation.py ./presentation \
  --title "My Research Talk" \
  --input-mode project \
  --source /path/to/project
```

PDF 模式：

```bash
python3 research-presentation/scripts/scaffold_presentation.py ./presentation \
  --title "Paper Walkthrough" \
  --input-mode pdf \
  --source /path/to/paper.pdf
```

骨架会故意保留可检测的占位内容。完成演示前，必须用可溯源的研究内容替换它们。

## 校验

```bash
python3 research-presentation/scripts/validate_narrative_contract.py \
  presentation/NARRATIVE-CONTRACT.md

python3 research-presentation/scripts/validate_presentation.py presentation
```

只有本次交付明确要求用户确认叙事时，才添加 `--require-frozen`。

静态校验不能替代视觉验收。需要在桌面、紧凑型笔记本和手机竖屏尺寸下逐页检查演示与详情弹窗。

## 仓库结构

```text
research-presentation/
├── SKILL.md
├── agents/openai.yaml
├── scripts/
├── references/
└── assets/
```

Skill 的脚本不依赖第三方 Python 包。PDF 提取、浏览器截图、文献核验和论文图表生成会使用宿主 Codex 环境中可用的专业工具。

## 设计原则

- 能从来源中查到的事实由 Skill 调查；研究决策由用户确认。
- 普通项目演示可以使用草稿叙事契约；用户明确要求先批准再制作时，遵守该要求。
- 证据等级和负面结果必须保持可见。
- 不把项目自行适配的 baseline 说成原论文提出的方法。
- 视觉包装不能覆盖证据来源或 claim 边界。
- 技术细节可以进入备查页或点击详情，但不能被省略。

## 参与贡献

提交 issue 时，请说明具体输入类型、预期演示行为，并提供最小可复现实例。Pull request 应保持 `SKILL.md` 简洁，将详细规范放在 `references/`，并为确定性脚本修改补充测试。

## 许可证

本项目使用 MIT License，详见 [LICENSE](../LICENSE)。
