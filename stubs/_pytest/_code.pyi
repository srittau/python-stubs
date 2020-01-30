from typing import Generic, TypeVar

_E = TypeVar("_E", bound=BaseException)

class ExceptionInfo(Generic[_E]): ...
