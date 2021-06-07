from typing import Any

from .result import Result

class BaseCursorResult:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class CursorResult(BaseCursorResult, Result):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

def __getattr__(__item: str) -> Any: ...  # incomplete
