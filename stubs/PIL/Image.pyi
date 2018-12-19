from pathlib import Path
from typing import Protocol, Union, Any, Optional, Tuple

from .ImageFile import ImageFile

class _Readable(Protocol):
    def read(self, length: int = ...) -> bytes: ...

class _Writeable(Protocol):
    def write(self, content: bytes) -> Any: ...
    def seek(self, offset: int, from_what: int) -> Any: ...

NONE: int
NEAREST: int
BOX: int
BILINEAR: int
LINEAR: int
HAMMING: int
BICUBIC: int
CUBIC: int
LANCZOS: int
ANTIALIAS: int

ORDERED: int
RASTERIZE: int
FLOYDSTEINBERG: int

WEB: int
ADAPTIVE: int

def open(fp: Union[str, bytes, Path, _Readable], mode: str = ...) -> ImageFile: ...

_ConversionMatrix = Union[
    Tuple[float, float, float, float],
    Tuple[float, float, float, float, float, float, float, float, float, float, float, float],
]

_Color = Union[float, Tuple[float, ...]]

class Image(object):
    mode: str
    def save(self, fp: Union[str, bytes, Path, _Writeable], format: Optional[str] = ..., **params: Any) -> None: ...
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def size(self) -> Tuple[int, int]: ...
    def convert(
        self,
        mode: Optional[str] = ...,
        matrix: Optional[_ConversionMatrix] = ...,
        dither: Optional[int] = ...,
        palette: int = ...,
        colors: int = ...,
    ) -> Image: ...
    def resize(
        self,
        size: Tuple[int, int],
        resample: int = ...,
        box: Optional[Tuple[float, float, float, float]] = ...,
    ) -> Image: ...
    def rotate(
        self,
        angle: float,
        resample: int = ...,
        expand: bool = ...,
        center: Optional[Tuple[float, float]] =  ...,
        translate: Optional[Tuple[float, float]] =  ...,
        fillcolor: Optional[_Color] = ...,
    ) -> Image: ...
