from typing import Union, Iterable, Mapping, Any

from .extensions import Extension


class Markdown:
    def __init__(
        self,
        *,
        extensions: Iterable[Union[None, str, Extension]] = ...,
        extension_configs: Mapping[str, Mapping[Any, Any]] = ...,
        output_format: str = ...,
        tab_length: int = ...,
    ) -> None: ...
    def convert(self, source: str) -> str: ...

def markdown(
    text: str,
    *,
    extensions: Iterable[Union[None, str, Extension]] = ...,
    extension_configs: Mapping[str, Mapping[Any, Any]] = ...,
    output_format: str = ...,
    tab_length: int = ...,
) -> str: ...
