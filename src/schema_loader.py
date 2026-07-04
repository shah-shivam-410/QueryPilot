from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

docs_path = ROOT_DIR / "docs" / "schema_outputs"

schema_context = ""

for file in ["production.md", "sales.md"]:
    with open(docs_path / file, "r", encoding="utf-8") as f:
        schema_context += f.read() + "\n\n"

