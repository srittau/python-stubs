# incomplete

from types import TracebackType
from typing import Any, Mapping, Optional, Type, Union

from ..log import Identified
from ..pool import Pool
from ..sql.compiler import Compiled
from ..sql.ddl import DDLElement
from ..sql.elements import ClauseElement
from ..sql.functions import FunctionElement
from ..sql.schema import DefaultGenerator
from .interfaces import Connectable, Dialect

# incomplete
class Connection(Connectable):
    engine: Engine
    def __enter__(self) -> Connection: ...
    def __exit__(self, type_: type[BaseException] | None, value: BaseException | None, traceback: TracebackType | None) -> None: ...
    @property
    def closed(self) -> bool: ...
    def begin(self) -> Transaction: ...
    def close(self) -> None: ...
    def execute(
        self,
        object_: Union[str, ClauseElement, FunctionElement, DDLElement, DefaultGenerator, Compiled],
        *multiparams: Any,
        **params: Any,
    ) -> Any: ...

# incomplete
class Engine(Connectable, Identified):
    pool: Pool
    url: str
    dialect: Dialect
    echo: Optional[bool]
    hide_parameters: bool

    def __init__(
        self,
        pool: Pool,
        dialect: Dialect,
        url: str,
        logging_name: Optional[str] = ...,
        echo: Optional[bool] = ...,
        proxy: Optional[Any] = ...,
        execution_options: Optional[Mapping[str, Any]] = ...,
        hide_parameters: bool = ...,
    ) -> None: ...
    @property
    def engine(self) -> Engine: ...
    def update_execution_options(self, **opt: Any) -> None: ...
    @property
    def name(self) -> str: ...
    def connect(self, **kwargs: Any) -> Connection: ...

class Transaction:
    connection: Connection
    def __init__(self, connection: Connection, parent: Transaction) -> None: ...
    def close(self) -> None: ...
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def __enter__(self) -> Transaction: ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType],
    ) -> None: ...
