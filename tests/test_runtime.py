import json
import tempfile
import unittest
from pathlib import Path

from lead_scriptor.cli import run


RAW_FILES = {
    "product.md": "# Product\n\n- B2B lead qualification assistant\n- For sales teams\n- Slow manual qualification\n- AI intake workflow\n- Faster qualification and reusable context\n",
    "company.md": "# Company\n\n- Lead Scriptor\n- AI intake workflow\n- B2B\n- Revenue operations\n- Better next-step quality\n",
    "audience.md": "# Audience\n\n- Sales teams in SMB B2B\n- Decision-makers in RevOps\n- Losing time on manual qualification\n- SDR managers\n",
    "tone.md": "# Tone\n\n- Formal and direct\n",
    "constraints.md": "# Constraints\n\n- Russian language\n- Export to Google Sheets as values only\n",
}


class RuntimeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for rel in [
            "inputs/raw",
            "inputs/normalized",
            "inputs/validation",
            "outputs/json",
            "runs",
        ]:
            (self.root / rel).mkdir(parents=True, exist_ok=True)
        for name, text in RAW_FILES.items():
            (self.root / "inputs" / "raw" / name).write_text(text, encoding="utf-8")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_runtime_writes_auto_discover_titles_default_false(self) -> None:
        code = run(self.root)
        self.assertEqual(code, 0)
        sales_yaml = (self.root / "inputs" / "normalized" / "sales.yaml").read_text(encoding="utf-8")
        self.assertIn('auto_discover_titles: false', sales_yaml)

    def test_lpr_is_blocked_when_titles_missing_and_auto_discover_false(self) -> None:
        run(self.root)
        completeness = json.loads((self.root / "inputs" / "validation" / "completeness.json").read_text(encoding="utf-8"))
        self.assertIn("lpr_chain", completeness["blocked_for"])
        self.assertIn("sales.target_titles_or_auto_discover_titles", completeness["missing_required"])


if __name__ == "__main__":
    unittest.main()
