# incomplete

from typing import Any, Optional

from .base import Executable
from .elements import ColumnElement
from .selectable import FromClause

# incomplete
class FunctionElement(Executable, ColumnElement[Any], FromClause): ...

# incomplete
class _FunctionGenerator:
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getattr__(self, item: str) -> _FunctionGenerator: ...

func: _FunctionGenerator

# incomplete
class GenericFunction: ...

# incomplete
class count(GenericFunction):
    def __init__(self, expression: Optional[Any] = ..., **kwargs: Any) -> None: ...
