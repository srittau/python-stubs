from asyncio import AbstractEventLoop
from typing import Optional, Callable, Any

from pika.adapters import base_connection
from pika.connection import Parameters

class AsyncioConnection(base_connection.BaseConnection):
    def __init__(
        self,
        parameters: Optional[Parameters] = ...,
        on_open_callback: Optional[Callable[[AsyncioConnection], Any]] = ...,
        on_open_error_callback: Optional[Callable[[AsyncioConnection, BaseException], Any]] = ...,
        on_close_callback: Optional[Callable[[AsyncioConnection, BaseException], Any]] = ...,
        custom_ioloop: Optional[AbstractEventLoop] = ...,
        internal_connection_workflow: bool = ...,
    ) -> None: ...
