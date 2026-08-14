# Presentation Design And Validation

Build a research instrument for explanation and scrutiny, not a marketing landing page.

## Story And Density

- Give every slide one argumentative role and one dominant visual hierarchy.
- Keep titles literal and compact. Put nuance in supporting text, captions, or dialogs.
- Introduce the concrete deployment or failure before formalism when the audience is not already expert.
- Place exact algorithm details, threshold construction, assumptions, and extra ablations in backup slides or clickable dialogs rather than omitting them.
- Separate completed evidence, boundary evidence, and future work visibly.

## Visual System

- Use a restrained neutral base with at least two functional accent colors for distinct meanings, not a one-hue theme.
- Avoid gradients, decorative blobs, nested cards, excessive rounding, and atmospheric images unrelated to the research object.
- Use cards only for repeated items, dialogs, or genuinely framed tools; keep page sections unframed.
- Use border radii of 8px or less unless adapting an established design system.
- Use real or generated bitmap assets when a visual is needed. Record origin and transformation in the manifest.
- Reserve display-scale text for title slides. Use compact headings inside dense technical views.
- Define stable dimensions for diagrams, tables, controls, counters, and plots so interactions do not shift layout.
- Never scale font size continuously with viewport width.

## Tables

Treat these as hard requirements:

1. Apply meaningful header, group, or row shading that exposes structure.
2. Highlight the proposed method and decisive best result with restrained emphasis; do not rely on color alone.
3. Keep every header and body cell on one line. Do not insert `<br>` in cells.
4. Abbreviate text that would wrap, then expand it in the caption or a clickable detail dialog.
5. Keep method names short and clickable when external provenance or adaptation details matter.
6. Align numeric columns consistently and preserve units in headers or captions.
7. Explain arrows, boldface, shading, and abbreviations in the caption.

Use `white-space: nowrap` for table cells and test the longest entry at the smallest supported viewport. If the table remains too wide, use horizontal scrolling with a visible affordance, split the table, or move it to a wide slide; do not shrink it into illegibility.

## Interaction

- Support keyboard, pointer, and touch navigation.
- Use familiar arrow icons for previous/next controls with accessible names and tooltips.
- Provide slide number/progress without covering content.
- Make dialogs dismissible by button, Escape, and backdrop where supported.
- Preserve focus visibility and sensible reading order.
- Do not require hover to access essential evidence.

## Citations And Details

- Keep compact citation markers adjacent to claims.
- Use dialogs for full external-method details, long definitions, and source provenance.
- Ensure every dialog works at desktop and mobile sizes and can scroll independently.
- Include a references slide for primary sources even when details are clickable elsewhere.

## Responsive QA

Inspect at least:

- desktop landscape around 1440×900;
- compact laptop around 1280×720;
- mobile portrait around 390×844.

For every viewport verify:

- no overlap or clipped content;
- no blank images or charts;
- table labels remain single-line and readable;
- dialogs fit and scroll;
- controls do not occlude citations or captions;
- the title, method identity, and key result are immediately legible;
- navigation reaches every slide and returns correctly.

Also test print/PDF mode when the user intends to distribute a static copy.
