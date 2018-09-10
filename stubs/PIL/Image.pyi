from pathlib import Path
from typing import Protocol, Union, Any, Optional

from .ImageFile import ImageFile

class _Readable(Protocol):
    def read(self, length: int = ...) -> bytes: ...

class _Writeable(Protocol):
    def write(self, content: bytes) -> Any: ...
    def seek(self, offset: int, from_what: int) -> Any: ...

def open(fp: Union[str, bytes, Path, _Readable], mode: str = ...) -> ImageFile: ...

class Image(object):
    def save(self, fp: Union[str, bytes, Path, _Writeable], format: Optional[str] = ..., **params: Any) -> None: ...