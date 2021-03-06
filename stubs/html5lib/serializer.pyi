from typing import Any, overload


@overload
def serialize(input: Any, tree: str = ..., encoding: None = ..., **serializer_opts: Any) -> str: ...
@overload
def serialize(input: Any, tree: str, encoding: str, **serializer_opts: Any) -> bytes: ...
@overload
def serialize(input: Any, *, encoding: str, **serializer_opts: Any) -> bytes: ...
