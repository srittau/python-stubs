from collections.abc import Collection, Mapping
from abc import abstractmethod
from typing import Any, Tuple, overload

from sqlalchemy.exc import StatementError

from .base import Connection, DBAPICursor, Engine
from .cursor import CursorResult
from ..sql.compiler import Compiled
from ..sql.ddl import DDLElement
from ..sql.elements import ClauseElement
from ..sql.functions import FunctionElement
from ..sql.schema import DefaultGenerator

class Dialect:
    @abstractmethod
    @property
    def name(self) -> str: ...
    @abstractmethod
    @property
    def paramstyle(self) -> str: ...
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class CreateEnginePlugin:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class ExecutionContext:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class Connectable:  # incomplete
    @overload
    def execute(
        self,
        object_: ClauseElement | FunctionElement | DDLElement | DefaultGenerator | Compiled,
        *multiparams: Mapping[str, Any],
        **params: Any,
    ) -> CursorResult: ...
    @overload
    def execute(
        self,
        object_: str,
        *multiparams: Any | Tuple[Any, ...] | Mapping[str, Any],
        **params: Any,
    ) -> CursorResult: ...
    @overload
    def scalar(
        self,
        object_: ClauseElement | FunctionElement | DDLElement | DefaultGenerator | Compiled,
        *multiparams: Mapping[str, Any],
        **params: Any,
    ) -> Any: ...
    @overload
    def scalar(
        self,
        object_: str,
        *multiparams: Any | Tuple[Any, ...] | Mapping[str, Any],
        **params: Any,
    ) -> Any: ...

class ExceptionContext:
    connection: Connection | None
    engine: Engine | None
    cursor: DBAPICursor | None
    statement: str | None
    parameters: Collection[Any] | None
    original_exception: BaseException | None
    sqlalchemy_exception: StatementError | None
    chained_exception: BaseException | None
    execution_context: ExecutionContext | None
    is_disconnect: bool | None
    invalidate_pool_on_disconnect: bool

