from pathlib import Path
import sys

from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.models import AgentState
from src.nodes import sql_builder, sql_revisor,sql_validator

import logging
logging.basicConfig(
    level=logging.INFO, # Set the lowest severity level to capture
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),   # Save logs to a file
        logging.StreamHandler()          # Print logs to the console
    ]
)
logger = logging.getLogger(__name__)

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

graph = StateGraph(AgentState)

graph.add_node("sql_builder", sql_builder)
graph.add_node("sql_validator", sql_validator)
graph.add_node("sql_revisor", sql_revisor)

def should_revise_sql(state: AgentState) -> str:
    """ Determine if the SQL needs to be revised based on validation results. """
    res = not state["is_valid"] and len(state["errors"]) > 0 and state["attempt"] < state["max_attempts"]
    if res == True:
        logger.info("SQL needs revision. Attempt %d of %d.", state["attempt"] + 1, state["max_attempts"])
        return "revision_needed"
    else:
        logger.info("SQL is valid.")
        return "success"

graph.add_edge(START, "sql_builder")
graph.add_edge("sql_builder", "sql_validator")
graph.add_conditional_edges(
    "sql_validator",
    should_revise_sql,
    {
        "revision_needed": "sql_revisor",
        "success": END
    }
)
graph.add_edge("sql_revisor", "sql_validator")

app = graph.compile()

png_bytes = app.get_graph().draw_mermaid_png()
with open("graph_structure.png", "wb") as f:
    f.write(png_bytes)

# result = app.invoke({"requirement": "Get the total sales amount for each product category in the production schema."})

# logger.info("="*50)
# logger.info("Final Result: %s", result)
