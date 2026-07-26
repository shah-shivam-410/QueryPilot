from __future__ import annotations

from pathlib import Path
from functools import lru_cache

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from src.agent_graph import app as agent_app
from src.config import config
from src.db_executor import execute_sql

import logging

from src.models import AskRequest, AskResponse
logging.basicConfig(
    level=logging.INFO, # Set the lowest severity level to capture
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),   # Save logs to a file
        logging.StreamHandler()          # Print logs to the console
    ]
)
logger = logging.getLogger(__name__)

webapp = FastAPI(
    title="AI Query Agent",
    description="Natural-language-to-SQL service with deterministic SELECT-only guardrails.",
    version="0.1.0",
)

STATIC_DIR = Path(__file__).resolve().parent / "static"
webapp.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@webapp.get("/health")
def health_check():
    return {"status": "healthy"}

@webapp.get("/ui")
def open_ask_ui():
    return FileResponse(STATIC_DIR / "ask_ui.html")

@webapp.post("/ask", response_model=AskResponse)
def ask(request: AskRequest) -> AskResponse:
    try:
        result = agent_app.invoke({"requirement": request["requirement"], "attempt": 0, "max_attempts": 3})
    except Exception as exc:
        logger.error(f"SQL creation failed: {exc}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"SQL builder failed: {exc}") from exc

    final_sql = result.get("revised_sql") or result.get("sql")

    # If validation failed, return a clear 400 with structured detail so UI can display it uniformly.
    if not result.get("is_valid", True):
        detail = {
            "message": "SQL validation failed",
            "errors": result.get("errors", []),
            "explanation": result.get("explanation", ""),
            "query": final_sql,
        }
        raise HTTPException(status_code=400, detail=detail)

    # Return generation-only response (execution moved to /execute endpoint)
    resp = AskResponse(
        requirement=request["requirement"],
        query=final_sql,
        explanation=result.get("explanation"),
        tables_used=result.get("tables_used", []),
        assumptions=result.get("assumptions", []),
        result=None,
    )

    logger.info(f"AskResponse: {resp}")
    return resp


@webapp.post("/execute")
def execute_query(payload: dict):
    """Execute a provided SQL query using the db_executor and return QueryResult-ish dict.
    The UI calls this with { query: "SELECT ..." } after generation.
    """
    sql = payload.get("query") if isinstance(payload, dict) else None
    if not sql:
        raise HTTPException(status_code=400, detail="No SQL query provided for execution")

    try:
        db_exec_result = execute_sql(sql)
    except Exception as exc:
        logger.error(f"SQL execution failed: {exc}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"SQL execution failed: {exc}") from exc

    # return as JSON-friendly dict
    return {
        "columns": db_exec_result["columns"],
        "rows": db_exec_result["rows"],
        "row_count": db_exec_result["row_count"],
    }
