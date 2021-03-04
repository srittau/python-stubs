# incomplete

from typing import Any, Callable, Iterable, List, Mapping, Optional, Tuple, Type, TypeVar, Union, overload
from typing_extensions import Literal

from .query import Query
from ..engine import Connectable, Connection, Engine, ResultProxy
from ..sql.base import Executable
from ..sql.elements import ClauseElement, ColumnElement
from ..sql.schema import Table

_T = TypeVar("_T")

# incomplete
class Session:
    def rollback(self) -> None: ...
    def commit(self) -> None: ...
    def connection(
        self,
        mapper: Optional[Any] = ...,
        clause: Optional[ClauseElement] = ...,
        bind: Optional[Engine] = ...,
        close_with_result: bool = ...,
        execution_options: Optional[Mapping[str, Any]] = ...,
        **kw: Any
    ) -> Connection: ...
    def execute(
        self,
        clause: Executable,
        params: Union[None, Mapping[str, Any], Iterable[Mapping[str, Any]]] = ...,
        mapper: Optional[Any] = ...,
        bind: Optional[Engine] = ...,
        **kw: Any,
    ) -> ResultProxy: ...
    def scalar(
        self,
        clause: Executable,
        params: Union[None, Mapping[str, Any], Iterable[Mapping[str, Any]]] = ...,
        mapper: Optional[Any] = ...,
        bind: Optional[Engine] = ...,
        **kw: Any,
    ) -> Any: ...
    def close(self) -> None: ...
    @overload
    def query(self, entities: Table, **kwargs: Any) -> Query[Any]: ...
    @overload
    def query(self, entities: ColumnElement[_T], **kwargs: Any) -> Query[Tuple[_T]]: ...  # type: ignore
    @overload
    def query(self, *entities: ColumnElement[_T], **kwargs: Any) -> Query[Tuple[_T, ...]]: ...
    @overload
    def query(self, *entities: Type[_T], **kwargs: Any) -> Query[_T]: ...
    def refresh(
        self,
        instance: Any,
        attribute_names: Optional[Iterable[str]] = ...,
        with_for_update: Optional[Literal[True]] = ...,
        lockmode: Optional[Any] = ...,
    ) -> None: ...
    def expire_all(self) -> None: ...
    def expire(self, instance: Any, attribute_names: Optional[List[str]] = ...) -> None: ...
    def add(self, instance: Any) -> None: ...
    def add_all(self, instances: Iterable[Any]) -> None: ...
    def delete(self, instance: Any) -> None: ...
    def flush(self, objects: Optional[Any] = ...) -> None: ...

# incomplete
class _SessionClassMethods: ...

# incomplete
class sessionmaker(_SessionClassMethods):
    def __init__(
        self,
        bind: Optional[Connectable] = ...,
        class_: Callable[..., Session] = ...,
        autoflush: bool = ...,
        autocommit: bool = ...,
        expire_on_commit: bool = ...,
        info: Optional[Any] = ...,
        **kw: Any
    ) -> None: ...
    def __call__(self, **local_kw: Any) -> Any: ...
