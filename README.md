# SQL Pilot Agent

A lightweight local web app that converts natural language requirements into SQL queries, optionally executes them against a configured PostgreSQL database, and returns query results with explanation and assumptions.

## Features

- Natural-language to SQL generation using an AI-backed query agent
- Optional SQL execution against a PostgreSQL database
- Built-in safety and guardrails for SELECT-only access
- Web UI for quick question submission and SQL copy support
- Result preview with row count and explanation context

## Requirements

- Python 3.13+
- PostgreSQL database access
- OpenAI or Gemini API key for the AI model
- `pip` to install dependencies

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-org>/SQL-Pilot-Agent.git
   cd SQL-Pilot-Agent
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not present, install directly from `pyproject.toml`:
   ```bash
   pip install -e .
   ```

## Configuration

Create a `.env` file in the project root with the following values:

```env
DATABASE_URL=postgresql+psycopg2://user:password@host:port/database
OPENAI_API_KEY=your-openai-api-key
# or GEMINI_API_KEY=your-gemini-api-key
# Optional overrides:
OPENAI_MODEL=gpt-4.1-mini
GEMINI_MODEL=gemini-2.5-flash
MAX_ROWS=100
STATEMENT_TIMEOUT_MS=5000
```

The application also loads these defaults from `pyproject.toml`:
- `schema_file`: `schema_Adventureworks_DB.sql`
- `allowed_schemas`: `production`, `sales`
- `blocked_tables`: `sales.creditcard`, `sales.personcreditcard`
- `blocked_columns`: `cardnumber`, `cardtype`, `expmonth`, `expyear`, `passwordhash`, `passwordsalt`

## Running the App

Start the FastAPI app with:

```bash
python main.py
```

Then open the UI at:

```
http://127.0.0.1:8000/ui
```

## Endpoints

- `GET /health` — health check
- `GET /ui` — serves the frontend UI page
- `POST /ask` — submit a requirement and receive SQL, explanation, assumptions, and optional query results

### `POST /ask` request body

```json
{
  "requirement": "Show the top 10 products by total sales in the sales schema",
  "execute": true
}
```

### Sample response

```json
{
  "requirement": "...",
  "query": "SELECT ...",
  "explanation": "...",
  "tables_used": ["sales.salesorderdetail", "production.product"],
  "assumptions": ["..."],
  "result": {
    "columns": ["name", "total_sales"],
    "rows": [
      {"name": "Bike", "total_sales": 12345}
    ],
    "row_count": 1
  }
}
```

## Project structure

- `main.py` — app entry point using `uvicorn`
- `src/api.py` — FastAPI server and endpoints
- `src/db_executor.py` — database execution logic
- `src/config.py` — configuration loading from environment and `.env`
- `src/models.py` — typed request and response models
- `src/agent_graph.py` — AI query agent logic
- `src/static/ask_ui.html` — frontend UI
- `docs/` — schema reference and supporting documentation

## Notes

- The system is designed for SELECT-only evaluation and SQL generation safety.
- Use the UI to copy generated SQL quickly or disable execution to inspect queries before running.
- Adjust `MAX_ROWS` and `STATEMENT_TIMEOUT_MS` as needed for your database workload.

## License

Add your project license here.
