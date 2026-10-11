# Single PDF Input

Use PDF mode for a faithful paper walkthrough, tutorial, critical reading, related-work presentation, or venue discussion based on one academic PDF.

## Extraction And Inspection

1. Record the absolute PDF path, filename, SHA-256 digest, page count, and extraction date.
2. Extract title, authors, abstract, section hierarchy, conclusions, limitations, references, and visible figure/table captions.
3. Render pages for visual inspection. Text extraction alone is insufficient for equations, multi-column reading order, charts, and figure annotations.
4. Use OCR when the PDF is scanned or the text layer is unusable. Mark OCR-derived passages as potentially noisy.
5. Separate statements made by the paper from the presentation author's interpretation or critique.

Use available PDF tooling rather than implementing ad hoc parsing in the deck generator.

## Default Story

Unless the user asks for another angle, organize the presentation as:

1. problem and motivation;
2. assumptions and system/threat model;
3. research gap and claimed contribution;
4. method overview followed by essential mechanism detail;
5. experimental protocol;
6. decisive results;
7. limitations, unsupported leaps, and open questions;
8. concise takeaway.

For new packaging, critique, or a venue-specific pitch, use the stated audience and evidence to prepare a reviewable draft. Use the optional Narrative Gate only if the user asks to discuss first or an unresolved choice would materially change the result.

## Page-Level Provenance

Every paper-derived claim must identify a page and, when applicable, a section, theorem, figure, or table. Record it in `presentation-manifest.yml`.

- Text claim: `PDF p. 4, Sec. 3.2`
- Figure: `PDF p. 6, Fig. 2`
- Table value: `PDF p. 8, Table 3, row ...`
- Appendix detail: `PDF p. 14, Appendix B`

Do not cite the PDF filename alone when a page-level location is available.

## Figures And Tables

- Reuse or crop a rendered figure only when legible, and visibly attribute its PDF page and original number.
- Preserve labels, legends, and uncertainty indicators.
- Do not reverse-engineer numerical source data from chart pixels and then present the reconstruction as exact.
- Recreate a chart only when the numerical values are faithfully extractable from a table or supplementary source; record the extraction source.
- If a table is too dense, select rows or columns transparently and say what was omitted.
- Never imply that the deck owns the paper's visual assets.

## External Sources

The PDF is the default evidence boundary. Use outside sources only when the user requests cross-validation, current context, or related work. Verify external citations against primary sources, distinguish them from the focal PDF, and record their URLs and access dates.

If an appendix, supplementary file, or source dataset is absent, state the limitation rather than filling the gap by inference.
