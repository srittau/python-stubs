from typing import Any


class _FunctionGenerator:
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __getattr__(self, item: str) -> _FunctionGenerator: ...

func: _FunctionGenerator
