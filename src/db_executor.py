from sqlalchemy import Engine, create_engine, text
from sqlalchemy import exc as sa_exc

from src.config import config
from src.models import QueryResult

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

engine: Engine = create_engine(
    config.database_url,
    pool_pre_ping=True,
    pool_timeout=int(config.pool_timeout_sec),
    connect_args={"connect_timeout": int(config.connect_timeout_sec)},
)

def execute_sql(sql: str) -> QueryResult:
    """ Execute the SQL query and return the results. """
    logger.info("start execute_sql")
    logger.info("Executing SQL: %s", sql)
    try:
        with engine.connect() as connection:
            with connection.begin():
                connection.execute(text("SET TRANSACTION READ ONLY"))
                connection.execute(text(f"SET LOCAL statement_timeout = {int(config.statement_timeout_ms)}"))
                result = connection.execute(text(sql))
                rows = [dict(row._mapping) for row in result]
    except sa_exc.OperationalError as e:
        logger.error("Database operational error during execute_sql: %s", e)
        raise
    except Exception as e:
        logger.exception("Unexpected error during execute_sql")
        raise

    columns = list(rows[0].keys()) if rows else []
    logger.info("end execute_sql")
    return QueryResult(columns=columns, rows=rows, row_count=len(rows))