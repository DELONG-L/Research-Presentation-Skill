# Narrative Gate

Use this protocol before creating or materially restructuring a project-mode presentation. The gate resolves research decisions; it is not a questionnaire about facts already present in the workspace.

## Entry Conditions

1. Inspect the project first using `project-input.md`.
2. Summarize the evidence state internally: completed, exploratory, negative, pending, and unknown.
3. Load any existing `NARRATIVE-CONTRACT.md`.
4. If the contract is frozen and the evidence has not materially changed, reuse it. If the method, main claim, venue, deployment story, or decisive evidence changed, mark it `stale` and reopen only affected decisions.

## Interview Rules

- Ask exactly one decision question per turn and wait for the answer.
- Include a recommended answer and a concrete reason with every question.
- Challenge unsupported ambition, vague novelty, hidden trust assumptions, and claims stronger than the evidence.
- Resolve upstream decisions before downstream wording. Do not ask for slide count or color before the research story is stable.
- Look up project facts instead of asking the user to recall them.
- Do not create, rewrite, or restyle the presentation until the user explicitly confirms shared understanding.

## Decision Order

Walk this dependency order. Skip only decisions already explicit and current.

1. **Purpose and audience:** venue, meeting type, audience expertise, and desired decision after the talk.
2. **Core problem:** the concrete failure or unmet need, not a method-shaped problem statement.
3. **Deployment scenario:** actors, data flows, timing, and what help the method provides.
4. **Trust and threat boundary:** trusted and untrusted inputs, private access, adversary capability, and exclusions.
5. **Research gap:** nearest work, what it already solves, and the exact remaining gap.
6. **Method identity:** input, output, decision granularity, algorithmic components, fallback, and name.
7. **Novelty thesis:** the smallest defensible reason the method is more than an assembly of known components.
8. **Primary claim:** one sentence containing setting, intervention, measured effect, and boundary.
9. **Contribution list:** problem/formalization, method, evidence, and boundary contributions without duplication.
10. **Evidence roles:** which experiments are primary, confirmatory, supporting, exploratory, negative, or pending.
11. **Failure interpretation:** what negative results mean and which broader claims they prohibit.
12. **Comparison framing:** external methods, adaptations, fairness conditions, and strongest reviewer objection.
13. **Terminology:** canonical method name, abbreviations, symbols, datasets, metrics, and prohibited synonyms.
14. **Storyline:** the causal sequence from deployment pressure to problem, method, evidence, boundaries, and next step.

## Question Pattern

Use this compact structure:

```text
Decision: <one decision only>

Question: <specific question>

Recommended answer: <one concrete option>
Reason: <why it best matches the evidence and audience>
Consequence: <what this choice enables or rules out>
```

Do not present several unrelated questions as a menu. Alternatives may be mentioned only when they clarify the current decision.

## Freeze Protocol

After all dependencies are resolved:

1. Draft `NARRATIVE-CONTRACT.md` from `assets/narrative-contract.template.md`.
2. Show the user the one-sentence pitch, method identity, primary claim, contribution list, prohibited claims, evidence roles, and proposed storyline.
3. Ask one final question: whether this records the shared understanding and may be frozen.
4. Only after explicit confirmation, set `status: frozen`, fill `confirmed_by` and `confirmed_at`, and run:

   ```bash
   python3 scripts/validate_narrative_contract.py NARRATIVE-CONTRACT.md --require-frozen
   ```

5. If validation fails, repair the contract before storyboarding.

## Reopening The Gate

Mark the contract `stale` when new evidence materially changes any of these:

- the main conclusion or its confidence;
- the deployment or threat model;
- the method's actual decision rule;
- the novelty position against nearest work;
- a primary comparison or failure boundary;
- the target venue or audience.

Cosmetic edits, additional citations that do not change positioning, and exact reruns consistent with the frozen conclusion do not require a full restart.
