from typing import (
    Any, Generic, TypeVar, Type, Union, Callable, overload,
    Sequence,
)

from ..ext.declarative.api import _DeclarativeBase
from .base import DialectKWArgs, SchemaEventTarget
from .elements import ColumnClause
from .selectable import TableClause
from .type_api import TypeEngine

_T = TypeVar("_T")

class Column(ColumnClause, Generic[_T]):
    @overload
    def __init__(
        self,
        type_: Union[TypeEngine, Type[TypeEngine]],
        *args: Any,
        primary_key: bool = ...,
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self,
        column: str,
        type_: Union[TypeEngine, Type[TypeEngine]],
        *args: Any,
        primary_key: bool = ...,
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __get__(self, instance: _DeclarativeBase, owner: Any) -> _T: ...
    @overload
    def __get__(self, instance: Any, owner: Any) -> Column[_T]: ...
    def __set__(self, instance: Any, value: _T) -> None: ...

class ForeignKey:
    def __init__(self, column: Union[str, Column]) -> None: ...

class Table(DialectKWArgs, TableClause):
    def __new__(cls, *args: Any, **kwargs: Any) -> Table: ...

class SchemaItem(SchemaEventTarget): ...
class Constraint(DialectKWArgs, SchemaItem): ...
class ColumnCollectionMixin: ...
class ColumnCollectionConstraint(ColumnCollectionMixin, Constraint): ...

class ForeignKeyConstraint(ColumnCollectionConstraint):
    def __init__(self, columns: Sequence[Union[Column, str]], refcolumns: Sequence[Union[Column, str]]) -> None: ...

class MetaData(SchemaItem): ...
