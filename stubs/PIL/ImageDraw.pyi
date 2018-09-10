from typing import Optional, Tuple, Union, Any

from .Image import Image
from .ImageFont import _Font

_Ink = Union[str, Tuple[int, int, int]]

class ImageDraw(object):
    def __init__(self, im: Image, mode: Optional[str] = ...) -> None: ...
    def text(self, xy: Tuple[float, float], text: Union[str, bytes], fill: Optional[_Ink] = ...,
             font: Optional[_Font] = ..., anchor: Any = ..., *args: Any, **kwargs: Any) -> None: ...
    def multiline_text(self, xy: Tuple[float, float], text: Union[str, bytes], fill: Optional[_Ink] = ...,
                       font: Optional[_Font] = ..., anchor: Any = ...,
                       spacing: int = ..., align: str = ..., direction: Any = ..., features: Any = ...) -> None: ...

def Draw(im: Image, mode: Optional[str] = ...) -> ImageDraw: ...
