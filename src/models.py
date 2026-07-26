from langchain_core.messages import AnyMessage
from typing_extensions import TypedDict, Annotated, Literal, Any, NotRequired
import operator

class AgentState(TypedDict):
    requirement: str
    sql_created: bool
    sql: str
    explanation: str
    tables_used: list[str]
    assumptions: list[str] | None
    is_valid: bool
    revised_sql_created: bool
    revised_sql: str | None = None
    errors: list[str] | None
    warnings: list[str] | None
    attempt: int = 0
    max_attempts: int = 3
    fatal_error: bool = False
    # messages: Annotated[list[AnyMessage], operator.add]
    
class SQLBuilderOutput(TypedDict):
    requirement: str
    sql_created: bool
    sql: str
    explanation: str
    tables_used: list[str]
    assumptions: list[str] | None

class SQLValidatorOutput(TypedDict):
    is_valid: bool
    errors: list[str] | None
    warnings: list[str] | None

class SQLRevisorOutput(TypedDict):
    revised_sql_created: bool
    revised_sql: str | None = None
    explanation: str
    tables_used: list[str]
    assumptions: list[str] | None

class QueryResult(TypedDict):
    columns: list[str]
    rows: list[dict[str, Any]] = []
    row_count: int

class AskRequest(TypedDict):
    requirement: str = Annotated[str, ...]

class AskResponse(TypedDict):
    requirement: str
    query: str | None = None
    explanation: str | None = None
    tables_used: list[str] = []
    assumptions: list[str] = []
    result: QueryResult | None = None
    # When backend has validation/runtime errors, populate these fields.
    message: NotRequired[str | None]
    errors: NotRequired[list[str] | None]
