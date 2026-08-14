# Research Presentation Skill

[中文说明](README.zh-CN.md)

An open-source Codex skill for turning a research project or a single academic PDF into an evidence-grounded, standalone HTML presentation.

The skill treats presentation work as a research workflow rather than a slide-formatting task:

```text
Narrative Gate → Evidence Map → Storyboard → Presentation Build → Visual Audit
```

## What It Does

- Accepts either a research project directory or one academic PDF.
- Runs a mandatory, one-question-at-a-time **Narrative Gate** for project presentations.
- Freezes the agreed packaging, claims, terminology, and storyline in `NARRATIVE-CONTRACT.md` before building slides.
- Tracks visible claims, numbers, figures, citations, and assets in `presentation-manifest.yml`.
- Produces a self-contained interactive HTML deck with no required build step.
- Enforces single-line table headers/cells, meaningful shading, proposed-method emphasis, and abbreviation disclosure.
- Audits claim strength and terminology in `LANGUAGE-AUDIT.md`.
- Validates local assets, slide/manifest consistency, placeholders, accessibility basics, and offline runtime behavior.

The Narrative Gate is built into this repository. It does not require a separately installed “grilling” skill.

## Input Modes

### Project directory

Use this mode for a group meeting, research update, venue pitch, or defense-style talk. The skill first inspects project facts, then interviews the user about research decisions one at a time. It will not generate the formal presentation until the user confirms and freezes the narrative contract.

### Single PDF

Use this mode for a paper walkthrough, tutorial, critical reading, or related-work presentation. Claims and visuals are traced to PDF pages, sections, figures, and tables. Outside sources are introduced only when requested and must be recorded separately.

## Installation

Clone the repository and link the skill directory into Codex:

```bash
git clone https://github.com/DELONG-L/research-presentation-skill.git
cd research-presentation-skill
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
ln -s "$(pwd)/research-presentation" "${CODEX_HOME:-$HOME/.codex}/skills/research-presentation"
```

If symbolic links are unavailable, copy the `research-presentation/` directory into `${CODEX_HOME:-$HOME/.codex}/skills/`.

Restart or open a new Codex task if the skill does not appear immediately.

## Usage

Invoke it explicitly with `$research-presentation`, or use a matching natural-language request:

```text
Use $research-presentation to turn this research project into tomorrow's group-meeting HTML presentation.

Use $research-presentation to explain this paper PDF as a 15-minute research talk.

Audit this existing research deck against its experiment records and fix unsupported claims.
```

The default output is:

```text
presentation/
├── index.html
├── presentation-manifest.yml
├── LANGUAGE-AUDIT.md
├── NARRATIVE-CONTRACT.md    # project mode
└── assets/
```

## Optional Scaffold

The bundled scaffold creates an offline HTML starting point and provenance files:

```bash
python3 research-presentation/scripts/scaffold_presentation.py ./presentation \
  --title "My Research Talk" \
  --input-mode project \
  --source /path/to/project
```

For a PDF:

```bash
python3 research-presentation/scripts/scaffold_presentation.py ./presentation \
  --title "Paper Walkthrough" \
  --input-mode pdf \
  --source /path/to/paper.pdf
```

The scaffold deliberately contains visible placeholders. Replace them with source-grounded content before validation.

## Validation

```bash
python3 research-presentation/scripts/validate_narrative_contract.py \
  presentation/NARRATIVE-CONTRACT.md --require-frozen

python3 research-presentation/scripts/validate_presentation.py presentation
```

Static validation does not replace visual inspection. Open the deck and inspect every slide and dialog at desktop, compact laptop, and mobile portrait sizes.

## Repository Layout

```text
research-presentation/
├── SKILL.md
├── agents/openai.yaml
├── scripts/
├── references/
└── assets/
```

The skill has no required Python package dependencies. PDF extraction, browser screenshots, literature verification, and figure production use whichever specialized tools are available in the host Codex environment.

## Design Principles

- Facts are discovered from sources; research decisions belong to the user.
- Project packaging must be confirmed before presentation generation.
- Evidence roles and negative results remain visible.
- Adapted baselines are never attributed to the original authors.
- Presentation polish cannot override provenance or claim boundaries.
- Technical details may move to backup slides or dialogs, but they cannot disappear.

## Contributing

Open an issue with a concrete input type, expected presentation behavior, and a minimal reproducible example. Pull requests should keep `SKILL.md` concise, place detailed guidance under `references/`, and include tests for deterministic script changes.

## License

MIT License. See [LICENSE](LICENSE).
