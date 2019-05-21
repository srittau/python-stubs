from typing import Any, Optional, Generic, TypeVar, Iterable

_T = TypeVar("_T")


class ColumnOperators(Generic[_T]):
    def __eq__(self, other: _T) -> Any: ...  # type: ignore
    def __ne__(self, other: _T) -> Any: ...  # type: ignore
    def __gt__(self, other: _T) -> Any: ...
    def __ge__(self, other: _T) -> Any: ...
    def __lt__(self, other: _T) -> Any: ...
    def __le__(self, other: _T) -> Any: ...
    def any_(self) -> Any: ...
    def all_(self) -> Any: ...
    def desc(self) -> Any: ...
    def asc(self) -> Any: ...
    def in_(self, other: Iterable[_T]) -> Any: ...
    def is_(self, other: _T) -> Any: ...
    def isnot(self, other: _T) -> Any: ...
    def like(self, other: _T, escape: Optional[str] = ...) -> Any: ...
    def match(self, other: str, **kwargs: Any) -> Any: ...
