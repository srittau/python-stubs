from typing import overload, Iterable, Union, Protocol, Any

class _BytesWritable(Protocol):
    def write(self, s: bytes) -> Any: ...
class _StrWritable(Protocol):
    def write(self, s: str) -> Any: ...

@overload
def encode(iterator: Iterable[str], method: Union[str, type] = ..., encoding: None = ..., out: None = ...) -> str: ...
@overload
def encode(iterator: Iterable[str], method: Union[str, type], encoding: str, out: None = ...) -> bytes: ...
@overload
def encode(iterator: Iterable[str], *, encoding: str, out: None = ...) -> bytes: ...
@overload
def encode(iterator: Iterable[str], method: Union[str, type], encoding: None, out: _StrWritable) -> None: ...
@overload
def encode(iterator: Iterable[str], *, encoding: None, out: _StrWritable) -> None: ...
@overload
def encode(iterator: Iterable[str], *, out: _StrWritable) -> None: ...
@overload
def encode(iterator: Iterable[str], method: Union[str, type], encoding: str, out: _BytesWritable) -> None: ...
@overload
def encode(iterator: Iterable[str], *, encoding: str, out: _BytesWritable) -> None: ...