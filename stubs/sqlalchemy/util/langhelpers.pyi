from typing import Any

class HasMemoized:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

def __getattr__(__item: str) -> Any: ...  # incomplete
