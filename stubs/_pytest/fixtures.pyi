from typing import Union, Literal, Callable, Any, Optional, List, overload, \
    TypeVar

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
