---
name: research-presentation
description: Create, restructure, and validate evidence-grounded research presentations from either a research project directory or a single academic PDF. Use when Codex needs to make or revise a group-meeting talk, paper walkthrough, research update, defense-style deck, or standalone interactive HTML presentation; when a project presentation requires narrative grilling, claim-evidence alignment, terminology control, citations, and provenance; or when an existing research presentation needs visual and semantic auditing. Do not use for generic business slides or manuscript prose alone.
---

# Research Presentation

Turn research evidence into a defensible presentation. Treat narrative framing, evidence provenance, and visual validation as required parts of the build.

## Route The Input

Classify the input before editing anything:

- **Project directory:** Read `references/project-input.md`, then run the mandatory Narrative Gate in `references/narrative-gate.md`. Do not build the presentation until the user confirms a frozen `NARRATIVE-CONTRACT.md`.
- **Single PDF:** Read `references/pdf-input.md`. Default to a faithful paper walkthrough; use the Narrative Gate only when the user requests critique, reframing, or a venue-specific story.
- **Existing presentation plus sources:** Treat the source directory or PDF as primary and the presentation as a revision target. Preserve working interactions while rebuilding unsupported claims or inconsistent terminology.

If the path type is ambiguous, inspect it. Ask only when the source cannot be identified safely.

## Build Workflow

1. **Inspect facts.** Read governance files, source records, existing presentations, and relevant evidence. Do not ask the user for facts available in the input.
2. **Freeze decisions.** In project mode, conduct the Narrative Gate one question at a time. Record the confirmed result in `NARRATIVE-CONTRACT.md` using `assets/narrative-contract.template.md`.
3. **Map evidence.** Read `references/evidence-and-citations.md`. Assign every quantitative or comparative claim a source and evidence role before storyboarding.
4. **Storyboard.** Give each slide one argumentative job. Keep core story slides separate from method-detail and Q&A backup slides.
5. **Scaffold.** Run `scripts/scaffold_presentation.py` when starting a standalone HTML deck. Adapt the generated files to the project rather than exposing template filler.
6. **Design and implement.** Read `references/presentation-design.md`. Use real visual assets and source-grounded charts or tables. Preserve the project's design language when revising an existing deck.
7. **Audit language.** Keep method names, symbols, dataset names, claims, captions, and table abbreviations synchronized across the contract, manifest, deck, and `LANGUAGE-AUDIT.md`.
8. **Validate.** Run both applicable validators:

   ```bash
   python3 scripts/validate_narrative_contract.py path/to/NARRATIVE-CONTRACT.md --require-frozen
   python3 scripts/validate_presentation.py path/to/presentation
   ```

9. **Verify visually.** Open the deck and inspect screenshots at desktop and mobile viewports. Check every slide, dialog, table, citation, and navigation control. Fix overflow, overlap, blank media, unreadable text, and broken interactions before delivery.

## Hard Gates

- Never generate a project-mode deck before the user confirms shared understanding and freezes the narrative contract.
- Never invent experimental values, deployment evidence, citations, source data, or method details.
- Never promote exploratory, audit-only, single-seed, or negative evidence into a stronger claim category.
- Never imply that an adapted comparator was proposed by the cited paper. Explain the original purpose and the presentation's adaptation separately.
- Never silently use private or restricted data to justify a public-only decision rule.
- Never use a PDF figure as if its underlying numerical data were available. Attribute page and figure/table number.
- Never permit table headers or cells to wrap. Abbreviate and expand the term in the caption or a clickable detail dialog.

## Output Contract

Produce a self-contained directory unless the user requests another format:

```text
presentation/
├── index.html
├── presentation-manifest.yml
├── LANGUAGE-AUDIT.md
├── NARRATIVE-CONTRACT.md       # required for project mode
└── assets/
```

`index.html` must open without a build step. Keep runtime assets local; external citation links may open on click. Record every visible number, figure, table, external method, and generated asset in `presentation-manifest.yml`.

## Resource Map

- `references/narrative-gate.md`: mandatory project-story interview and freeze rules.
- `references/project-input.md`: project discovery, governance, and evidence inventory.
- `references/pdf-input.md`: PDF extraction, page-level provenance, and figure handling.
- `references/evidence-and-citations.md`: evidence roles, citations, comparator disclosure, and manifest rules.
- `references/presentation-design.md`: slide composition, table rules, interaction, and visual QA.
- `assets/html-deck/index.html`: offline HTML presentation scaffold.
- `assets/narrative-contract.template.md`: machine-checkable narrative contract.
- `assets/presentation-manifest.template.yml`: source and slide provenance template.
- `assets/language-audit.template.md`: terminology and claim-strength audit template.
- `scripts/scaffold_presentation.py`: initialize an output directory.
- `scripts/validate_narrative_contract.py`: enforce Narrative Gate completeness and freeze state.
- `scripts/validate_presentation.py`: static checks for output files, local assets, tables, accessibility, and presentation structure.
