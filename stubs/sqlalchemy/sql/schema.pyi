from typing import \
    Any, Optional, Generic, TypeVar, Type, Union, Callable, overload

from .elements import ColumnClause
from .type_api import TypeEngine

_T = TypeVar("_T")

class Column(ColumnClause, Generic[_T]):
    @overload
    def __init__(self, type_: Union[TypeEngine, Type[TypeEngine]],
                 *args: Any, primary_key: bool = ..., nullable: bool = ...,
                 unique: bool = ...,
                 default: Union[_T, Callable[[], _T]] = ...) -> None: ...
    @overload
    def __init__(self, column: str, type_: Union[TypeEngine, Type[TypeEngine]],
                 *args: Any, primary_key: bool = ..., nullable: bool = ...,
                 unique: bool = ...,
                 default: Union[_T, Callable[[], _T]] = ...) -> None: ...
    def __get__(self, instance: Optional[Any], owner: Any) -> _T: ...
    def __set__(self, instance: Any, value: _T) -> None: ...

class ForeignKey:
    def __init__(self, column: str) -> None: ...

class Table:
    def __new__(cls, *args: Any, **kwargs: Any) -> Table: ...
