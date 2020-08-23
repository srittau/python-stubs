# TODO: incomplete

import datetime
import enum
import sys
from decimal import Decimal
from typing import (
    Any, Callable, Generic, Optional, Sequence, Type, TypeVar, Union, overload,
)

from ..dialects.postgresql import UUID
from ..engine import Engine
from ..ext.declarative.api import _DeclarativeBase
from .base import DialectKWArgs, SchemaEventTarget
from .elements import ColumnClause
from .selectable import TableClause
from .sqltypes import (
    Boolean,
    Date,
    DateTime,
    DECIMAL,
    Enum,
    Integer,
    JSON,
    Numeric,
    String,
    Time,
    TIMESTAMP,
    Unicode,
)
from .type_api import TypeEngine
from .visitors import Visitable

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

_T = TypeVar("_T")
_E = TypeVar("_E", bound=enum.Enum)

# TODO: incomplete
class SchemaItem(SchemaEventTarget, Visitable): ...

# TODO: incomplete
class Column(DialectKWArgs, SchemaItem, ColumnClause[_T], Generic[_T]):
    @overload
    def __init__(
        self: Column[bool],
        type_: Type[Boolean],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[bool],
        type_: Type[Boolean],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[bool]],
        type_: Type[Boolean],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[bool],
        column: str,
        type_: Type[Boolean],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[bool],
        column: str,
        type_: Type[Boolean],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[bool]],
        column: str,
        type_: Type[Boolean],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[int],
        type_: Type[Integer],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[int],
        type_: Type[Integer],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[int]],
        type_: Type[Integer],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[int],
        column: str,
        type_: Type[Integer],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[int],
        column: str,
        type_: Type[Integer],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[int]],
        column: str,
        type_: Type[Integer],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[Decimal],
        type_: Type[DECIMAL],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Decimal],
        type_: Type[DECIMAL],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[Decimal]],
        type_: Type[DECIMAL],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Decimal],
        column: str,
        type_: Type[DECIMAL],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Decimal],
        column: str,
        type_: Type[DECIMAL],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[Decimal]],
        column: str,
        type_: Type[DECIMAL],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[float],
        type_: Numeric,
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[float],
        type_: Numeric,
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[float]],
        type_: Numeric,
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[float],
        column: str,
        type_: Numeric,
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[float],
        column: str,
        type_: Numeric,
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[float]],
        column: str,
        type_: Numeric,
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...

    # needs to be before str, since this is a subtype
    @overload
    def __init__(
        self: Column[_E],
        type_: Enum[_E],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_E, Callable[[], _E]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[_E],
        type_: Enum[_E],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_E, Callable[[], _E]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[_E]],
        type_: Enum[_E],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[_E], Callable[[], Optional[_E]]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[_E],
        column: Enum[_E],
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_E, Callable[[], _E]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[_E],
        column: Enum[_E],
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_E, Callable[[], _E]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[_E]],
        column: Enum[_E],
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[_E], Callable[[], Optional[_E]]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[str],
        type_: Union[Type[String], String, Type[Unicode], Unicode],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[str],
        type_: Union[Type[String], String, Type[Unicode], Unicode],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[str]],
        type_: Union[Type[String], String, Type[Unicode], Unicode],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[str],
        column: str,
        type_: Union[Type[String], String, Type[Unicode], Unicode],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[str],
        column: str,
        type_: Union[Type[String], String, Type[Unicode], Unicode],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[str]],
        column: str,
        type_: Union[Type[String], String, Type[Unicode], Unicode],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[_T, Callable[[], _T]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[datetime.date],
        type_: Union[Date, Type[Date]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[datetime.date, Callable[[], datetime.date]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.date],
        type_: Union[Date, Type[Date]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[datetime.date, Callable[[], datetime.date]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[datetime.date]],
        type_: Union[Date, Type[Date]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[datetime.date], Callable[[], Optional[datetime.date]]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.date],
        column: str,
        type_: Union[Date, Type[Date]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[datetime.date, Callable[[], datetime.date]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.date],
        column: str,
        type_: Union[Date, Type[Date]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[datetime.date, Callable[[], datetime.date]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[datetime.date]],
        column: str,
        type_: Union[Date, Type[Date]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[datetime.date], Callable[[], Optional[datetime.date]]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[datetime.time],
        type_: Union[Time, Type[Time]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[datetime.time, Callable[[], datetime.time]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.time],
        type_: Union[Time, Type[Time]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[datetime.time, Callable[[], datetime.time]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[datetime.time]],
        type_: Union[Time, Type[Time]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[datetime.time], Callable[[], Optional[datetime.time]]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.time],
        column: str,
        type_: Union[Time, Type[Time]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[datetime.time, Callable[[], datetime.time]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.time],
        column: str,
        type_: Union[Time, Type[Time]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[datetime.time, Callable[[], datetime.time]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[datetime.time]],
        column: str,
        type_: Union[Time, Type[Time]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[datetime.time], Callable[[], Optional[datetime.time]]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[datetime.datetime],
        type_: Union[TIMESTAMP, Type[TIMESTAMP], DateTime, Type[DateTime]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[datetime.datetime, Callable[[], datetime.datetime]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.datetime],
        type_: Union[TIMESTAMP, Type[TIMESTAMP], DateTime, Type[DateTime]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[datetime.datetime, Callable[[], datetime.datetime]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[datetime.datetime]],
        type_: Union[TIMESTAMP, Type[TIMESTAMP], DateTime, Type[DateTime]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[datetime.datetime], Callable[[], Optional[datetime.datetime]]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.datetime],
        column: str,
        type_: Union[TIMESTAMP, Type[TIMESTAMP], DateTime, Type[DateTime]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[datetime.datetime, Callable[[], datetime.datetime]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[datetime.datetime],
        column: str,
        type_: Union[TIMESTAMP, Type[TIMESTAMP], DateTime, Type[DateTime]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[datetime.datetime, Callable[[], datetime.datetime]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[datetime.datetime]],
        column: str,
        type_: Union[TIMESTAMP, Type[TIMESTAMP], DateTime, Type[DateTime]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[datetime.datetime], Callable[[], Optional[datetime.datetime]]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[str],
        type_: Union[UUID, Type[UUID]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[str, Callable[[], str]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[str],
        type_: Union[UUID, Type[UUID]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[str, Callable[[], str]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[str]],
        type_: Union[UUID, Type[UUID]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[str], Callable[[], Optional[str]]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[str],
        column: str,
        type_: Union[UUID, Type[UUID]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[str, Callable[[], str]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[str],
        column: str,
        type_: Union[UUID, Type[UUID]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[str, Callable[[], str]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[str]],
        column: str,
        type_: Union[UUID, Type[UUID]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[str], Callable[[], Optional[str]]] = ...,
        server_default: str = ...,
    ) -> None: ...

    @overload
    def __init__(
        self: Column[Any],
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[Any, Callable[[], Any]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Any],
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[Any, Callable[[], Any]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[Any]],
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[Any], Callable[[], Optional[Any]]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Any],
        column: str,
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[False],
        unique: bool = ...,
        default: Union[Any, Callable[[], Any]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Any],
        column: str,
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: Literal[True],
        nullable: bool = ...,
        unique: bool = ...,
        default: Union[Any, Callable[[], Any]] = ...,
        server_default: str = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Column[Optional[Any]],
        column: str,
        type_: Union[JSON, Type[JSON]],
        *args: Any,
        primary_key: bool = ...,
        nullable: Literal[True] = ...,
        unique: bool = ...,
        default: Union[Optional[Any], Callable[[], Optional[Any]]] = ...,
        server_default: str = ...,
    ) -> None: ...

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
    def __init__(self, column: Union[str, Column[Any]], *, ondelete: Optional[str] = ...) -> None: ...

class _NotAColumnExpr: ...

# TODO: incomplete
class DefaultGenerator(_NotAColumnExpr, SchemaItem): ...

class Table(DialectKWArgs, TableClause):
    def __new__(cls, *args: Any, **kwargs: Any) -> Table: ...

class Constraint(DialectKWArgs, SchemaItem): ...
class ColumnCollectionMixin: ...
class ColumnCollectionConstraint(ColumnCollectionMixin, Constraint): ...

class ForeignKeyConstraint(ColumnCollectionConstraint):
    def __init__(self, columns: Sequence[Union[Column[Any], str]], refcolumns: Sequence[Union[Column[Any], str]]) -> None: ...

# incomplete
class MetaData(SchemaItem):
    def is_bound(self) -> bool: ...
    bind: Engine
