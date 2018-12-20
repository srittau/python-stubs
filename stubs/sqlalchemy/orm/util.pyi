from typing import Any, Optional, overload, Type

from ..sql.selectable import FromClause, Alias

class AliasedClass:
    def __getattr__(self, key: str) -> Any: ...

@overload
def aliased(
    element: FromClause,
    alias: Optional[Any] = ...,
    name: Optional[str] = ...,
    flat: bool = ...,
    adapt_on_names: bool = ...,
) -> Alias: ...

@overload
def aliased(
    element: Type[Any],
    alias: Optional[Any] = ...,
    name: Optional[str] = ...,
    flat: bool = ...,
    adapt_on_names: bool = ...,
) -> AliasedClass: ...
