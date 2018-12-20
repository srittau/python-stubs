from typing import Optional, Any, Type, Callable

from .base import TemplateError, Template

class TemplateNotFound(TemplateError): ...

class TemplateLoader:
    def __init__(
        self,
        search_path: Optional[Any] = ...,
        auto_reload: bool = ...,
        default_encoding: Optional[str] = ...,
        max_cache_size: int = ...,
        default_class: Optional[Type[Template]] = ...,
        variable_lookup: Any = ...,
        allow_exec: bool = ...,
        callback: Optional[Callable[[Template], Any]] = ...,
    ) -> None: ...
    def load(
        self,
        filename: str,
        relative_to: Optional[str] = None,
        cls: Optional[Type[Template]] = ...,
        encoding: Optional[str] = ...,
    ) -> Template: ...
