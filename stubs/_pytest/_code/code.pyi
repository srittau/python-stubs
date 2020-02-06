# incomplete

import sys
from types import TracebackType
from typing import Any, Generic, Optional, Type, TypeVar, Tuple, Union, \
    Pattern, List

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

_E = TypeVar("_E", bound=BaseException)
_F = TypeVar("_F", bound=BaseException)

_TracebackStyle = Literal["long", "short", "line", "no", "native"]

# incomplete
class Traceback: ...

class ExceptionInfo(Generic[_E]):
    @classmethod
    def from_exc_info(cls, exc_info: Tuple[Type[_F], _F, TracebackType], exprinfo: Optional[str] = ...) -> ExceptionInfo[_F]: ...
    @classmethod
    def from_current(cls, exprinfo: Optional[str] = ...) -> ExceptionInfo[Any]: ...
    @classmethod
    def for_later(cls) -> ExceptionInfo[Any]: ...

    @property
    def type(self) -> Type[_E]: ...
    @property
    def value(self) -> _E: ...
    @property
    def tb(self) -> TracebackType: ...
    @property
    def typename(self) -> str: ...
    traceback: Traceback
    def exconly(self, tryshort: bool = ...) -> str: ...
    def errisinstance(self, exc: Union[Type[BaseException], Tuple[Type[BaseException], ...]]) -> bool: ...
    def getrepr(
        self,
        showlocals: bool = ...,
        style: _TracebackStyle = ...,
        abspath: bool = ...,
        tbfilter: bool = ...,
        funcargs: bool = ...,
        truncate_locals: bool = ...,
        chain: bool = ...,
    ) -> Union[ReprExceptionInfo, ExceptionChainRepr]: ...
    def match(self, regexp: Union[str, Pattern[str]]) -> bool: ...

class TerminalRepr:
    def toterminal(self, tw: Any) -> None: ...  # tw: py.io.TerminalWriter
class ExceptionRepr(TerminalRepr):
    sections: List[Tuple[str, str, str]]
    def addsection(self, name: str, content: str, sep: str = ...) -> None: ...
class ExceptionChainRepr(ExceptionRepr): ...
class ReprExceptionInfo(ExceptionRepr): ...
