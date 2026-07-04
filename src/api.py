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
        result = agent_app.invoke({"requirement": request["requirement"]})
    except Exception as exc:
        logger.error(f"SQL creation failed: {exc}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"SQL builder failed: {exc}") from exc

    if request["execute"] is False:
        return AskResponse(
            requirement=request["requirement"],
            query=result["sql"],
            explanation=result["explanation"],
            tables_used=result["tables_used"],
            assumptions=result["assumptions"],
            result=None,
        )
    else:
        try:
            final_sql = result["revised_sql"] if "revised_sql" in result and result["revised_sql"] else result["sql"]
            db_exec_result = execute_sql(final_sql)
        except Exception as exc:
            logger.error(f"SQL execution failed: {exc}", exc_info=True)
            raise HTTPException(status_code=500, detail=f"SQL execution failed: {exc}") from exc

    resp = AskResponse(
        requirement=request["requirement"],
        query=result["sql"],
        explanation=result["explanation"],
        tables_used=result["tables_used"],
        assumptions=result["assumptions"],
        result=db_exec_result,
    )
   
    logger.info(f"AskResponse: {resp}")
    return resp

