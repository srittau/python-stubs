import sys
from typing import Union, Callable, Any, Optional, List, TypeVar, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

_F = TypeVar("_F", bound=Callable[[], Any])
_Scope = Literal["function", "class", "module", "package", "session"]
_FixtureF = Callable[[str, Any], _Scope]

class FixtureFunctionMarker:
    pass

@overload
def fixture(callable_or_scope: _F) -> _F: ...
@overload
def fixture(
    scope: Union[None, _Scope, _FixtureF] = ...,
    params: Optional[List[Any]] = ...,
    autouse: bool = ...,
    ids: Optional[List[str]] = ...,
    name: Optional[str] = ...,
) -> FixtureFunctionMarker: ...
