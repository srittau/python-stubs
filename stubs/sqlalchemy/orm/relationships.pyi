from typing import overload, Generic, TypeVar, Any

from .decl_api import _DeclarativeBase
from .interfaces import StrategizedProperty

_T = TypeVar("_T")


class RelationshipProperty(StrategizedProperty, Generic[_T]):
    def __eq__(self, other: Any) -> Any: ...
    @overload
    def __get__(self, instance: _DeclarativeBase, owner: Any) -> _T: ...
    @overload
    def __get__(self, instance: Any, owner: Any) -> RelationshipProperty[_T]: ...
    def __set__(self, instance: _DeclarativeBase, value: Any) -> None: ...
