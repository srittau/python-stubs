from typing import Any, TypeVar, Generic

from ..sql.elements import ColumnElement

_T = TypeVar("_T")

class OrderedSet(set[_T], Generic[_T]):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class ImmutableContainer: ...

class Properties(Generic[_T]):
    def __getattr__(self, key: str) -> _T: ...

class OrderedProperties(Properties[_T], Generic[_T]): ...
class ImmutableProperties(ImmutableContainer, Properties[_T], Generic[_T]): ...

ordered_column_set = OrderedSet[ColumnElement[Any]]

def __getattr__(__name: str) -> Any: ...  # incomplete
