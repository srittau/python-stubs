# incomplete

from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
    overload,
)

from ..sql.elements import BooleanClauseList
from ..sql.schema import Column, Table
from .attributes import Mapped as Mapped
from .decl_api import declarative_base as declarative_base
from .query import Query as Query
from .relationships import RelationshipProperty as RelationshipProperty
from .session import Session as Session, sessionmaker as sessionmaker
from .util import aliased as aliased

_T = TypeVar("_T")

_OrderType = Union[bool, str, Column[Any]]

load_only: Any

def compile_mappers() -> None: ...
def clear_mappers() -> None: ...
@overload
def relationship(
    argument: Type[_T],
    secondary: None = ...,
    primaryjoin: Optional[Union[str, BooleanClauseList]] = ...,
    secondaryjoin: Optional[Union[str, BooleanClauseList]] = ...,
    foreign_keys: List[Column[Any]] = ...,
    *,  # FIXME: more arguments
    cascade: bool | str = ...,
    order_by: Union[_OrderType, Callable[[], _OrderType]] = ...,
    backref: Union[None, str, Tuple[str, Dict[str, Any]]] = ...,
    lazy: Union[str, bool, None] = ...,
    remote_side: Optional[Column[Any]] = ...,
) -> RelationshipProperty[Optional[_T]]: ...
@overload
def relationship(
    argument: Type[_T],
    secondary: Table,
    primaryjoin: Optional[Union[str, BooleanClauseList]] = ...,
    secondaryjoin: Optional[Union[str, BooleanClauseList]] = ...,
    foreign_keys: List[Column[Any]] = ...,
    *,  # FIXME: more arguments
    cascade: bool | str = ...,
    order_by: Union[_OrderType, Callable[[], _OrderType]] = ...,
    backref: Union[None, str, Tuple[str, Dict[str, Any]]] = ...,
    lazy: Union[str, bool, None] = ...,
    remote_side: Optional[Column[Any]] = ...,
) -> RelationshipProperty[List[_T]]: ...
@overload
def relationship(
    argument: Any,
    secondary: Any = ...,
    primaryjoin: Optional[Union[str, BooleanClauseList]] = ...,
    secondaryjoin: Optional[Union[str, BooleanClauseList]] = ...,
    foreign_keys: List[Column[Any]] = ...,
    uselist: Optional[bool] = ...,
    order_by: Union[_OrderType, Callable[[], _OrderType]] = ...,
    backref: Union[None, str, Tuple[str, Dict[str, Any]]] = ...,
    *,  # FIXME: more arguments
    cascade: bool | str = ...,
    lazy: Union[str, bool, None] = ...,
    passive_deletes: bool = ...,
    passive_updates: bool = ...,
    remote_side: Optional[Column[Any]] = ...,
) -> RelationshipProperty[Any]: ...

relation = relationship

def backref(
    name: str,
    *,
    order_by: Union[_OrderType, Callable[[], _OrderType]] = ...,
    cascade: str = ...,
    viewonly: bool = ...,
    lazy: Union[str, bool, None] = ...,
    uselist: Optional[bool] = ...,
    passive_deletes: bool = ...,
    passive_updates: bool = ...,
) -> Tuple[str, Dict[str, Any]]: ...
