<div align="center">

<h1>Research Presentation</h1>
<p>把研究项目或论文整理成证据可追溯的 HTML 演示。</p>
<p><a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-333333" alt="MIT 许可证"></a></p>
<p><a href="#开始使用"><strong>开始使用</strong></a> · <a href="docs/guide.zh-CN.md">使用指南</a> · <a href="README.md">English</a></p>

</div>

## 看看效果

[![可独立运行的研究演示示例](docs/previews/demo.jpg)](examples/demo/index.html)

一个可以实际翻页的演示示例，说明布局、导航和来源记录，不包含虚构实验结果。下载仓库后，直接打开 `examples/demo/index.html` 即可试用。

## 选择输入

| 你的材料 | 演示用途 |
|---|---|
| 研究项目目录 | 组会、研究进展、答辩或结论与证据汇报 |
| 单篇学术 PDF | 忠实解读论文的问题、方法、证据与局限 |
| 已有演示与来源材料 | 检查结论、术语、引用和版式，再完成修订 |

项目模式默认先记录草稿叙事并制作可审阅演示。用户明确要求先讨论，或存在影响正确性的关键叙事选择时，使用叙事确认流程；只有实际确认后才冻结契约。

## 开始使用

首次安装：

```bash
git clone https://github.com/DELONG-L/Research-Presentation-Skill.git
cd Research-Presentation-Skill
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)/research-presentation" "${CODEX_HOME:-$HOME/.codex}/skills/research-presentation"
```

已有安装时先保留本地修改。不支持符号链接时可以复制技能目录。[使用指南](docs/guide.zh-CN.md)包含骨架脚本、验证命令和输出结构。

```text
用 $research-presentation 把这个研究项目整理成组会演示。
从已有证据制作可审阅草稿，保留结论边界和来源记录。
```

## 交付内容

独立 HTML 演示、本地资源、来源与结论清单、术语检查记录；项目模式额外提供叙事契约。页面不需要构建步骤，支持键盘、触摸翻页和打印。验证脚本使用 Python 3，不依赖第三方包。

[技能说明](research-presentation/SKILL.md) · [可运行示例](examples/demo/) · [详细指南](docs/guide.zh-CN.md) · [MIT 许可证](LICENSE)
