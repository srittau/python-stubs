from typing import Any, Callable, Dict, Optional, Text, Union

from .credentials import PlainCredentials, ExternalCredentials

class Parameters(object): ...

class ConnectionParameters(Parameters):
    def __init__(
            self,
            host: Text = ...,
            port: int = ...,
            virtual_host: Text = ...,
            credentials: Union[PlainCredentials, ExternalCredentials] = ...,
            channel_max: int = ...,
            frame_max: int = ...,
            heartbeat: Union[None, int, Callable[[Any, int], int]] = ...,  # Any = Connection
            ssl_options: SSLOptions = ...,
            connection_attempts: int = ...,
            retry_delay: float = ...,
            socket_timeout: float = ...,
            stack_timeout: float = ...,
            locale: Text = ...,
            blocked_connection_timeout: Optional[float] = ...,
            client_properties: Optional[Dict[Text, Any]] = ...,
            tcp_options: Optional[Dict[Any, Any]] = ...,
    ) -> None: ...

class SSLOptions(object): ...
