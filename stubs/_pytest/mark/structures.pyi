from typing import Any, Callable, TypeVar, Optional, List, Tuple, Union

_F = TypeVar("_F", bound=Callable[..., Any])

class MarkDecorator:
    def __call__(self, *args_: Any, **kwargs: Any) -> Any: ...

class MarkGenerator:
    def __getattr__(self, name: str) -> MarkDecorator: ...
    def parametrize(
        self,
        argnames: str,
        argvalues: Union[List[Any], Tuple[Any, ...]],
        indirect: Union[List[str], bool] = ...,
        ids: Union[None, List[Union[None, str]], Callable[[Any], Optional[str]]] = ...,
        scope: Optional[str] = ...,
    ) -> Callable[[_F], _F]: ...
    def skip(self, reason: Optional[str] = ...) -> Callable[[_F], _F]: ...


MARK_GEN: MarkGenerator
