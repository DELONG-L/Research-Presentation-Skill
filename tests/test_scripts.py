from __future__ import annotations

import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "research-presentation"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


contract_validator = load_module(
    "contract_validator", SKILL / "scripts" / "validate_narrative_contract.py"
)
deck_validator = load_module(
    "deck_validator", SKILL / "scripts" / "validate_presentation.py"
)


VALID_CONTRACT = """---
schema_version: 1
status: frozen
input_mode: project
project_root: "/tmp/project"
source_revision: "abc123"
evidence_cutoff: "2026-08-14"
confirmed_by: "Research lead"
confirmed_at: "2026-08-14"
---

# Narrative Contract

## One-Sentence Pitch
We test a bounded research claim with traceable evidence.

## Audience And Purpose
A group meeting that must decide whether to continue the project.

## Problem And Deployment Scenario
A practitioner must make a decision under a documented constraint.

## Trust And Threat Boundary
The trusted and untrusted inputs and excluded adversaries are explicit.

## Research Gap
Nearest work does not address the stated decision under the same access constraint.

## Method Identity
The method maps declared inputs to one bounded action with a fallback.

## Novelty Thesis
Novelty lies in the constrained decision mechanism and its evidence, not component metrics.

## Primary Claim
Under the evaluated protocol, the method reduces the declared failure without broader guarantees.

## Contributions
- A problem formulation, method, and scoped empirical evaluation.

## Claim Boundaries
### Supported Claims
- The evaluated protocol supports the primary claim.
### Prohibited Claims
- Universal robustness is not established.

## Evidence Map
| Claim ID | Evidence Role | Source | Scope | Status |
|---|---|---|---|---|
| C1 | primary | reports/result.json | one protocol | complete |

## Terminology
| Concept | Canonical Term | Abbreviation | Avoid |
|---|---|---|---|
| Method | Bounded Gate | BG | generic selector |

## Storyline
1. Deployment pressure, gap, method, evidence, and boundary.

## Unresolved Risks
- Cross-domain evidence remains absent.
"""


VALID_HTML = """<!doctype html>
<html><head><meta name="viewport" content="width=device-width">
<style>th,td{white-space:nowrap} thead{background:#eee}@media print{.slide{display:block}}</style>
</head><body>
<section class="slide" id="s1"><h1>Title</h1></section>
<section class="slide" id="s2"><h2>Result</h2><table><thead><tr><th>A</th></tr></thead><tbody><tr data-emphasis="proposed"><td>1</td></tr></tbody></table></section>
<button aria-label="Next" title="Next">→</button>
</body></html>"""


VALID_MANIFEST = """schema_version: 1
presentation_id: "test"
input_mode: "pdf"
slides:
  - number: 1
    title: "Title"
  - number: 2
    title: "Result"
claim_ledger: []
citation_registry: {}
asset_registry: []
"""


VALID_AUDIT = """# Language And Claim Audit
## Canonical Terminology
Method names are stable.
## Claim Strength
Claims remain bounded.
## Prohibited Claims
Universal claims are prohibited.
## Final Consistency Check
All terms were checked.
"""


class ContractValidatorTests(unittest.TestCase):
    def test_accepts_frozen_complete_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "NARRATIVE-CONTRACT.md"
            path.write_text(VALID_CONTRACT, encoding="utf-8")
            errors, warnings, metadata = contract_validator.validate(path, True)
            self.assertEqual(errors, [])
            self.assertEqual(warnings, [])
            self.assertEqual(metadata["status"], "frozen")

    def test_rejects_draft_template(self):
        path = SKILL / "assets" / "narrative-contract.template.md"
        errors, _, metadata = contract_validator.validate(path, True)
        self.assertEqual(metadata["status"], "draft")
        self.assertTrue(errors)

    def test_accepts_complete_draft_without_confirmation(self):
        draft = VALID_CONTRACT.replace("status: frozen", "status: draft")
        draft = draft.replace('confirmed_by: "Research lead"\n', "")
        draft = draft.replace('confirmed_at: "2026-08-14"\n', "")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "NARRATIVE-CONTRACT.md"
            path.write_text(draft, encoding="utf-8")
            errors, warnings, metadata = contract_validator.validate(path, False)
            self.assertEqual(errors, [])
            self.assertEqual(warnings, [])
            self.assertEqual(metadata["status"], "draft")

    def test_requires_confirmation_when_freeze_is_requested(self):
        unconfirmed = VALID_CONTRACT.replace('confirmed_by: "Research lead"\n', "")
        unconfirmed = unconfirmed.replace('confirmed_at: "2026-08-14"\n', "")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "NARRATIVE-CONTRACT.md"
            path.write_text(unconfirmed, encoding="utf-8")
            errors, _, _ = contract_validator.validate(path, True)
            self.assertTrue(any("confirmed_by" in error for error in errors))
            self.assertTrue(any("confirmed_at" in error for error in errors))


class DeckValidatorTests(unittest.TestCase):
    def make_deck(self, root: Path, html: str = VALID_HTML) -> None:
        (root / "assets").mkdir()
        (root / "index.html").write_text(html, encoding="utf-8")
        (root / "presentation-manifest.yml").write_text(VALID_MANIFEST, encoding="utf-8")
        (root / "LANGUAGE-AUDIT.md").write_text(VALID_AUDIT, encoding="utf-8")

    def test_accepts_minimal_offline_deck(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_deck(root)
            errors, _, stats = deck_validator.validate(root)
            self.assertEqual(errors, [])
            self.assertEqual(stats["slides"], 2)

    def test_rejects_table_line_break(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_deck(root, VALID_HTML.replace("<td>1</td>", "<td>1<br>2</td>"))
            errors, _, _ = deck_validator.validate(root)
            self.assertTrue(any("inside table cells" in item for item in errors))


class ScaffoldTests(unittest.TestCase):
    def test_project_scaffold_contains_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "deck"
            subprocess.run(
                [
                    "python3",
                    str(SKILL / "scripts" / "scaffold_presentation.py"),
                    str(output),
                    "--title",
                    "Test Project",
                    "--input-mode",
                    "project",
                    "--source",
                    str(ROOT),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            self.assertTrue((output / "index.html").is_file())
            self.assertTrue((output / "NARRATIVE-CONTRACT.md").is_file())


if __name__ == "__main__":
    unittest.main()
