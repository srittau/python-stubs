import sys
from typing import Any, Callable, List, Optional, TypeVar, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

_F = TypeVar("_F", bound=Callable[..., Any])
_Scope = Literal["function", "class", "module", "package", "session"]
_FixtureF = Callable[[str, Any], _Scope]

class FixtureFunctionMarker:
    def __call__(self, function: _F) -> _F: ...

def fixture(
    callable_or_scope: Union[None, _Scope, Callable[..., Any]] = ...,
    *args: Any,
    scope: str = ...,
    params: Optional[List[Any]] = ...,
    autouse: bool = ...,
    ids: Optional[List[str]] = ...,
    name: Optional[str] = ...,
) -> FixtureFunctionMarker: ...
