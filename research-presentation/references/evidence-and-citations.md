# Evidence And Citations

Ground each slide in traceable evidence and preserve the difference between observation, interpretation, and claim.

## Evidence Roles

Assign one role to each result:

- **Primary:** directly tests the main end-to-end claim under the intended protocol.
- **Confirmatory:** preregistered or frozen follow-up that challenges the primary conclusion.
- **Supporting:** mechanism, ablation, transfer, or diagnostic evidence that explains but does not close the main claim.
- **Exploratory:** hypothesis-generating scan, severity curve, or post hoc analysis.
- **Negative/boundary:** identifies where the method fails or where a broader interpretation is false.
- **Pending:** planned or running work; never display it as completed evidence.

Show the role in captions, notes, or detail dialogs when a viewer could otherwise overinterpret the result.

## Claim Ledger

Before implementation, maintain a ledger with:

| Claim ID | Claim | Evidence role | Source | Scope | Slide | Status |
|---|---|---|---|---|---|---|

Every visible number and comparative phrase such as “better,” “robust,” “generalizes,” or “preserves” must resolve to a ledger entry.

## Citation Rules

- Prefer primary papers, official documentation, and original datasets.
- Put a compact citation next to the supported claim and a complete entry in the citation registry or references slide.
- Keep citation numbering stable across slides, dialogs, and the manifest.
- Make URLs clickable only after verifying that they resolve to the claimed source.
- Do not cite a search result page.
- Keep direct quotation short and visually marked; default to paraphrase.

## External Method Comparisons

When a table or chart includes an external method, make its short name clickable. Its detail view must state:

1. full method name;
2. original task and access assumptions;
3. what was implemented or adapted in this evaluation;
4. whether the adaptation is author-provided or presentation/project-defined;
5. complete primary citation and link;
6. material fairness limitations.

Do not label an adapted variant as though the cited authors proposed it.

## Manifest Minimum

`presentation-manifest.yml` must include:

- presentation ID, title, input mode, creation/update date, and evidence cutoff;
- source revision or PDF digest;
- frozen story contract summary for project mode;
- slide number, title, argumentative role, and claim IDs;
- claim ledger with evidence roles and exact source locations;
- citation registry;
- asset registry with origin, transformation, and license/usage note;
- prohibited claims and known boundaries.

The manifest is the source of truth for provenance; the deck is the communication layer.
