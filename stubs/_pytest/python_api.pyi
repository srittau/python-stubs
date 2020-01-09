from types import TracebackType
from typing import overload, Any, Callable, Generic, Optional, Pattern, Tuple, Type, TypeVar, Union

from ._code import ExceptionInfo

_E = TypeVar("_E", bound=BaseException)

@overload
def raises(
    expected_exception: Union[Type[_E], Tuple[Type[_E], ...]], *, match: Optional[Union[str, Pattern[str]]] = ...,
) -> RaisesContext[_E]: ...
@overload
def raises(
    expected_exception: Union[Type[_E], Tuple[Type[_E], ...]],
    func: Callable[..., Any],
    *args: Any,
    match: Optional[str] = ...,
    **kwargs: Any
) -> Optional[ExceptionInfo[_E]]: ...

class RaisesContext(Generic[_E]):
    expected_exception: Union[Type[_E], Tuple[Type[_E], ...]]
    message: str
    match_expr: Optional[Union[str, Pattern[str]]]
    excinfo: Optional[ExceptionInfo[_E]]
    def __init__(
        self,
        expected_exception: Union[Type[_E], Tuple[Type[_E], ...]],
        message: str,
        match_expr: Optional[Union[str, Pattern[str]]] = ...,
    ) -> None: ...
    def __enter__(self) -> ExceptionInfo[_E]: ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType],
    ) -> bool: ...
