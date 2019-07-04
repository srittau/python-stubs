from types import TracebackType
from typing import Any, Dict, Optional, Sequence, Text, Type, Union

from ..connection import Parameters
from ..frame import Method
from ..spec import BasicProperties

class BlockingConnection(object):
    def __init__(self, parameters: Optional[Union[Parameters, Sequence[Parameters]]] = ...) -> None: ...
    def __enter__(self) -> BlockingConnection: ...
    def __exit__(self, exc_type: Type[BaseException], exc_val: BaseException, exc_tb: TracebackType) -> bool: ...
    def channel(self, channel_number: Optional[int] = ...) -> BlockingChannel: ...

class BlockingChannel(object):
    def exchange_declare(
        self,
        exchange: Text,
        exchange_type: Text = ...,
        passive: bool = ...,
        durable: bool = ...,
        auto_delete: bool = ...,
        internal: bool = ...,
        arguments: Optional[Dict[Any, Any]] = ...,
    ) -> Method: ...
    def basic_publish(
        self,
        exchange: Text,
        routing_key: Text,
        body: Union[Text, bytes],
        properties: Optional[BasicProperties] = ...,
        mandatory: bool = ...,
    ) -> None: ...
