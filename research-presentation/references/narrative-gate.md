# Optional Narrative Gate

Default to preparing an evidence-grounded, reviewable deck from the user's
request and available project material. A draft narrative contract is enough
for ordinary work. Do not interview the user merely because the input is a
project directory, critique, or venue-specific presentation.

## When to ask

Use this gate when the user explicitly requests discussion/confirmation before
building, or when an unresolved choice about audience, main conclusion, or
research positioning would materially change the result and cannot be resolved
from the sources and current instructions. Ask about that choice only; continue
independent authorized work. An explicit instruction to wait before building
does prohibit building until the user releases it.

Read project facts and any existing `NARRATIVE-CONTRACT.md` first. Reuse current
decisions and valid authorization. Do not ask for facts available in the files.
For routine layout, wording, and implementation choices, use judgment and
proceed. Record material working assumptions as assumptions, not agreed facts.

## Interview-first mode

When the user chooses an interview, ask focused decision questions with a
recommended answer and reason. Use one question at a time when the user prefers
that interaction. Skip settled decisions; do not require all branches of a
fixed questionnaire. Relevant topics may include audience, primary claim,
evidence roles, nearest work, method identity, threat boundaries, and storyline.

## Record status honestly

- Create a new project contract as `status: draft`. Populate the useful template
  fields from evidence and mark unsupported novelty or effects as unestablished.
  Use a concrete `not applicable` explanation when a field does not apply.
- Leave `confirmed_by` and `confirmed_at` empty until the user actually confirms
  this narrative. A finished deck can have a draft narrative contract.
- If a current contract is frozen, reuse it. When new evidence materially
  changes its conclusion, boundary, or positioning, preserve the old record or
  version, mark the old framing stale, and prepare a revised draft. Ask only
  about affected consequential decisions; cosmetic edits do not reopen a gate.
- If the user requests freezing or an applicable contract requires it, present
  the concrete pitch, claim boundaries, and storyline for confirmation. Reuse a
  confirmation already given for that exact narrative; do not ask twice.

Validate ordinary drafts with:

```bash
python3 scripts/validate_narrative_contract.py path/to/NARRATIVE-CONTRACT.md
```

For an actually confirmed narrative, set `status: frozen`, record who confirmed
it and when, and validate with `--require-frozen`. Do not mark a narrative frozen
because a validator needs that state. A remaining narrative question blocks
only the affected content unless the user explicitly requested a full pause.
