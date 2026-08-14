# Project Directory Input

Use project mode to turn a living research workspace into a progress talk, venue pitch, defense-style presentation, or claim-evidence briefing.

## Discovery Order

1. Read repository-level instructions such as `AGENTS.md`, `PROJECT-WORKSPACE.md`, `README`, task plans, and governance policies.
2. Inspect Git status without modifying or reverting unrelated work.
3. Locate existing narrative, paper, visualization, experiment, report, and literature directories with fast filename and text search.
4. Read experiment summaries and analysis reports before raw logs. Avoid checkpoints, datasets, large run artifacts, and private data unless explicitly necessary and permitted.
5. Inspect existing presentation manifests and terminology files before inventing names.
6. Record the current revision, dirty-worktree state, evidence cutoff, and relevant source paths.

## Evidence Inventory

Build an internal inventory with these fields:

| Field | Meaning |
|---|---|
| Claim candidate | The proposed sentence or comparison |
| Source | Exact file, experiment ID, table, or report |
| Evidence role | Primary, confirmatory, supporting, exploratory, negative, or pending |
| Scope | Dataset, model, threat, seed count, and protocol |
| Status | Completed, partial, failed, missing, or superseded |
| Risk | Leakage, unfair comparison, instability, or overclaim concern |

Use completed and frozen records for visible quantitative claims. If two records disagree, prefer neither silently: trace the discrepancy and record the resolution.

## Governance Boundary

- Keep presentation work inside the requested visualization/output directory.
- Do not edit experiment records, manuscript sources, HPC state, or paper repositories merely to make the presentation consistent.
- Cite those records from the presentation manifest instead.
- Preserve user changes in a dirty worktree.
- Respect local-to-HPC transfer restrictions and do not pull heavyweight or prohibited artifacts into the deck.

## Project-Mode Deliverables

Create:

- `NARRATIVE-CONTRACT.md`: frozen project packaging and claim boundary;
- `presentation-manifest.yml`: source, claim, slide, citation, and asset provenance;
- `LANGUAGE-AUDIT.md`: canonical terminology, ambiguity, and claim-strength review;
- `index.html` plus local `assets/`.

Run the Narrative Gate before creating the latter three unless a current frozen contract already exists.
