# Research Presentation

把研究项目或论文 PDF 整理成可独立运行的 HTML 汇报，讲清论证，并让结论能够追溯到来源。

**[▶ 打开互动演示](https://delong-l.github.io/Research-Presentation-Skill/zh/)** · [安装技能](#get-started) · [使用指南](docs/guide.zh-CN.md) · [English](README.md)

<a href="#see-the-result"><img src="docs/previews/readme-cover-zh.png" alt="研究汇报：从材料出发，用证据讲清研究。概念分镜呈现问题、机制与证据之间的联系。" width="1942"></a>

[![MIT 许可证](https://img.shields.io/badge/license-MIT-333333)](LICENSE)

## 从你的研究材料开始

- **研究项目目录** → 依据已有材料，制作组会、研究进展或答辩型汇报。
- **单篇论文 PDF** → 解读研究问题、方法、证据与局限，并保留对应的论文出处。
- **已有演示与来源材料** → 修正结论、统一术语、改善版式，同时保留可用的交互。

每一页承担一个论证任务。图表、数字和比较都要有对应来源，不确定性与局限也应保留。

<a id="see-the-result"></a>
## 看看实际演示

[![中文互动示例：切换问题、机制与证据，了解每页承担的论证任务。](docs/previews/demo-zh.png)](https://delong-l.github.io/Research-Presentation-Skill/zh/)

这个三页示例以技能说明为来源。你可以切换论证任务、查看来源，并用按钮或键盘翻页。示例不包含实验研究结果。

**[▶ 打开中文互动演示](https://delong-l.github.io/Research-Presentation-Skill/zh/)**

<details>
<summary><strong>想离线体验？</strong></summary>

[下载仓库 ZIP](https://github.com/DELONG-L/Research-Presentation-Skill/archive/refs/heads/main.zip) 并解压，用浏览器打开 `examples/demo/zh/index.html`。与在线演示内容相同，无需构建步骤或外部运行资源。

</details>

<a id="get-started"></a>
## 安装并试一个任务

在 macOS 或 Linux 上**首次安装**：

```bash
git clone https://github.com/DELONG-L/Research-Presentation-Skill.git
cd Research-Presentation-Skill
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)/research-presentation" "${CODEX_HOME:-$HOME/.codex}/skills/research-presentation"
```

已有安装时，先保留本地修改。不支持符号链接时，可以复制 `research-presentation/` 目录。新建一个 Codex 任务，提供来源目录，再提出请求：

```text
用 $research-presentation
把这个研究项目整理成组会演示。
从已有证据制作可审阅草稿，
保留结论边界和来源记录。
```

<details>
<summary><strong>想解读 PDF，或修改已有演示？</strong></summary>

**解读论文**

```text
用 $research-presentation
把这篇 PDF 整理成 15 分钟的汇报。
让结论和图表对应论文出处，
并保留原文的局限。
```

**修改已有汇报**

```text
用 $research-presentation
依据来源记录修改这份演示。
修正缺少依据的结论，统一术语，
并保留可用的翻页方式。
```

</details>

## 交付内容

- **离线 HTML 演示**：`index.html` 与本地资源，支持键盘、触摸翻页和打印。
- **来源记录**：`presentation-manifest.yml` 对应结论、图表、数字、引用及其依据。
- **叙事与术语记录**：`LANGUAGE-AUDIT.md` 检查术语和结论强度；项目模式还提供 `NARRATIVE-CONTRACT.md`。

项目模式默认制作可审阅草稿。用户明确要求先讨论，或存在影响正确性的关键选择时，使用叙事确认流程；只有用户实际确认后才冻结叙事。

骨架与验证脚本使用 Python 3，不依赖第三方 Python 包。命令、输出结构和检查方法见[使用指南](docs/guide.zh-CN.md)。

[技能说明](research-presentation/SKILL.md) · [中文示例源码](examples/demo/zh/index.html) · [英文示例源码](examples/demo/index.html) · [视觉资源与来源](docs/visuals.md) · [MIT 许可证](LICENSE)
