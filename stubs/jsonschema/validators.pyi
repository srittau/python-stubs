# incomplete

from typing import Optional, Any, Type, Mapping, Callable

class _Validator: ...

def validate(instance: object, schema: object, cls: Optional[Type[_Validator]] = None, *args: Any, **kwargs: Any) -> None: ...

Draft3Validator: Type[_Validator]
Draft4Validator: Type[_Validator]
Draft6Validator: Type[_Validator]
Draft7Validator: Type[_Validator]

class RefResolver(object):
    def __init__(
        self,
        base_uri: str,
        referrer: str,
        store: Mapping[str, Any] = ...,
        cache_remote: bool = ...,
        handlers: Mapping[str, Callable[[str], Any]] = ...,
        urljoin_cache: Optional[Any] = ...,
        remote_cache: Optional[Any] = ...,
    ): ...
