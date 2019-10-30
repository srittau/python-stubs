from typing import Optional, Union, Text, Any

from .objects import Principal

class DAVClient:
    def __init__(
        self,
        url: str,
        proxy: Optional[str] = ...,
        username: Optional[str] = ...,
        password: Optional[str] = ...,
        auth: Optional[Any] = ...,
        ssl_verify_cert: Union[bool, Text] = ...,
    ) -> None: ...
    def principal(self) -> Principal: ...
