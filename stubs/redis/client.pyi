from datetime import timedelta
from typing import Optional, Union, Mapping, Any

from .connection import ConnectionPool

class StrictRedis:
    def __init__(self, host: str = ..., port: int = ..., db: int = ..., password: Optional[str] = ...,
                 socket_timeout: Optional[float] = ..., socket_connect_timeout: Optional[float] = ...,
                 socket_keepalive: Optional[bool] = ..., socket_keepalive_options: Optional[Mapping[str, Union[int, str]]] = ...,
                 connection_pool: Optional[ConnectionPool] = ..., unix_socket_path: Optional[str] = ...,
                 encoding: str = ..., encoding_errors: str = ..., charset: Optional[str] = ..., errors: Optional[str] = ...,
                 decode_responses: bool = ..., retry_on_timeout: bool = ...,
                 ssl: bool = ..., ssl_keyfile: Optional[str] = ..., ssl_certfile: Optional[str] = ...,
                 ssl_cert_reqs: Optional[Union[str, int]] = ..., ssl_ca_certs: Optional[str] = ...,
                 max_connections: Optional[int] = ...) -> None: ...
    def get(self, name: str) -> Optional[bytes]: ...
    def set(self, name: str, value: Any, ex: Optional[int] = ..., px: Optional[int] = ..., nx: bool = ..., xx: bool = ...) -> Optional[bool]: ...
    def expire(self, name: str, time: Union[int, timedelta]) -> bool: ...

class Redis(StrictRedis): ...
