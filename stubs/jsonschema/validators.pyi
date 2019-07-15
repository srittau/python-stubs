from typing import Optional, Any, Type, Mapping, Callable


class _Validator(object): ...

def validate(instance: object, schema: object, cls: Optional[Type[_Validator]] = None, *args: Any, **kwargs: Any) -> None: ...

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
