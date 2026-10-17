# Interactive examples on GitHub Pages / 互动示例托管

[English home](../README.md) · [中文首页](../README.zh-CN.md)

The [English demo](https://delong-l.github.io/Research-Presentation-Skill/) and [Chinese demo](https://delong-l.github.io/Research-Presentation-Skill/zh/) are served from the same self-contained HTML files available in `examples/demo/`. The language switch preserves the current slide.

[英文演示](https://delong-l.github.io/Research-Presentation-Skill/)与[中文演示](https://delong-l.github.io/Research-Presentation-Skill/zh/)直接使用 `examples/demo/` 中可独立运行的 HTML 文件。切换语言时保留当前页。

The [Pages workflow](../.github/workflows/pages.yml) validates both examples, packages them with [build_pages.py](../scripts/build_pages.py), and deploys the artifact. The artifact contains only `index.html`, `zh/index.html`, `LICENSE`, and `.nojekyll`. Repository documentation, source records, and skill instructions remain on GitHub and are linked from the demos.

[Pages 工作流](../.github/workflows/pages.yml)先验证两版示例，再通过 [build_pages.py](../scripts/build_pages.py) 打包并部署。发布包只包含 `index.html`、`zh/index.html`、`LICENSE` 和 `.nojekyll`。文档、来源记录与技能说明保留在 GitHub，通过演示中的链接访问。

To package the site locally, use an empty output directory:

本地打包时，指定一个空的输出目录：

```bash
python3 scripts/build_pages.py _site
python3 -m http.server 8139 --directory _site
```

Open `http://localhost:8139/` or `http://localhost:8139/zh/`. A build step is not needed to use the examples offline: open `examples/demo/index.html` or `examples/demo/zh/index.html` directly.

打开 `http://localhost:8139/` 或 `http://localhost:8139/zh/`。离线使用示例无需构建，直接打开 `examples/demo/index.html` 或 `examples/demo/zh/index.html` 即可。
