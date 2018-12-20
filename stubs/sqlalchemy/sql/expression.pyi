from typing import Any, Optional

from .elements import BooleanClauseList, ClauseElement

from .functions import (
    func as func,
)

def select(columns: Optional[Any] = ..., whereclause: Optional[ClauseElement] = ...) -> Any: ...

def desc(column: Any) -> Any: ...

def and_(*clauses: ClauseElement) -> BooleanClauseList: ...
def or_(*clauses: ClauseElement) -> BooleanClauseList: ...
