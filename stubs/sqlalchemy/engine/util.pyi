from collections.abc import Callable
from types import TracebackType
from typing import Any, TypeVar

_T = TypeVar("_T")

def connection_memoize(key: str) -> Callable[..., Any]: ...

class TransactionalContext:
    def __enter__(self: _T) -> _T: ...
    def __exit__(
        self, exc_type: type[BaseException] | None,
        exc_val: BaseException | None, exc_tb: TracebackType | None,
    ) -> None: ...
