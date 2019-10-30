from typing import Any, Optional, Union, overload, TypeVar, Iterable, Dict, \
    List

from typing_extensions import Literal, Protocol


class _Writable(Protocol):
    def write(self, s: bytes) -> Any: ...

_W = TypeVar("_W", bound=_Writable)

class VBase(object):
    @overload
    def serialize(self, buf: None = ..., lineLength: int = ..., validate: bool = ..., behavior: Optional[Any] = ...) -> str: ...
    @overload
    def serialize(self, buf: _W, lineLength: int = ..., validate: bool = ..., behavior: Optional[Any] = ...) -> _W: ...

class ContentLine(VBase):
    value: Any


class Component(VBase):
    contents: Dict[str, List[VBase]]
    @overload
    def add(self, objOrName: Literal["vevent"], group: Optional[str] = ...) -> Component: ...
    @overload
    def add(
        self, objOrName: Literal["uid", "summary", "description", "dtstart", "dtend"], group: Optional[str] = ...,
    ) -> ContentLine: ...
    @overload
    def add(self, objOrName: Union[str, VBase], group: Optional[str] = ...) -> Any: ...  # return VBase sub-class
    def components(self) -> Iterable[Component]: ...
