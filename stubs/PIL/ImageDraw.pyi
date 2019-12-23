from typing import Optional, Tuple, Union, Any, Literal

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
    def rectangle(
        self,
        xy: Union[Tuple[float, float, float, float], Tuple[Tuple[float, float], Tuple[float, float]]],
        fill: Optional[_Ink] = ...,
        outline: Optional[_Ink] = ...,
        width: float = ...,
    ) -> None: ...
    def textsize(
        self,
        text: Union[str, bytes],
        font: Optional[_Font] = ...,
        spacing: float = ...,
        direction: Optional[Literal["rtl", "ltr", "ttb", "btt"]] = ...,
        features: Optional[Any] = ...,
        language: Optional[Any] = ...,
        stroke_width: float = ...,
    ) -> Tuple[int, int]: ...

def Draw(im: Image, mode: Optional[str] = ...) -> ImageDraw: ...
