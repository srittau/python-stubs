from typing import Optional, Callable, Any

from .data import Arguments
from .frame import Method
from .spec import Basic, BasicProperties


class Channel(object):
    def basic_cancel(self, consumer_tag: str = ..., callback: Optional[Callable[[Method], Any]] = ...) -> None: ...

    def basic_consume(
        self,
        queue: str,
        on_message_callback: Callable[[Channel, Basic.Deliver, BasicProperties, bytes], Any],
        auto_ack: bool = ...,
        exclusive: bool = ...,
        consumer_tag: Optional[str] = ...,
        arguments: Optional[Arguments] = ...,
        callback: Optional[Callable[[Method], Any]] = ...,
    ) -> str: ...

    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...

    def exchange_declare(
        self,
        exchange: str,
        exchange_type: str = ...,
        passive: bool = ...,
        durable: bool = ...,
        auto_delete: bool = ...,
        internal: bool = ...,
        arguments: Optional[Arguments] = ...,
        callback: Optional[Callable[[Method], Any]] = ...,
    ) -> None: ...

    def queue_bind(
        self,
        queue: str,
        exchange: str,
        routing_key: Optional[str] = ...,
        arguments: Optional[Arguments] = ...,
        callback: Optional[Callable[[Method], Any]] = ...,
    ) -> None: ...

    def queue_declare(
        self,
        queue: str,
        passive: bool = ...,
        durable: bool = ...,
        exclusive: bool = ...,
        auto_delete: bool = ...,
        arguments: Optional[Arguments] = ...,
        callback: Optional[Callable[[Method], None]] = ...,
    ) -> None: ...

    def queue_delete(
        self, queue: str, if_unused: bool = ..., if_empty: bool = ..., callback: Optional[Callable[[Method], Any]] = ...,
    ) -> None: ...
