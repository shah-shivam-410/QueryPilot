from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

docs_path = ROOT_DIR / "docs" / "schema_outputs"

schema_context = ""

schema_file_list = [f for f in docs_path.glob("*.md") if f.is_file()]

for file in schema_file_list:
    with open(docs_path / file, "r", encoding="utf-8") as f:
        schema_context += f.read() + "\n\n========================================\n\n"

