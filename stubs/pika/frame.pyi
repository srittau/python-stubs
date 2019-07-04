from typing import Any, Optional, Text, Tuple

from .amqp_object import AMQPObject
from .spec import BasicProperties

class Frame(AMQPObject):
    def __init__(self, frame_type: int, channel_number: int) -> None: ...
    def marshal(self) -> str: ...

class Method(Frame):
    # FIXME: method: pika.Spec.Class.Method
    method: Any
    # FIXME: method: pika.Spec.Class.Method
    def __init__(self, channel_number: int, method: Any) -> None: ...

class Header(Frame):
    body_size: int
    properties: BasicProperties
    def __init__(self, channel_number: int, body_size: int, props: BasicProperties) -> None: ...

class Body(Frame):
    fragment: Text
    def __init__(self, channel_number: int, fragment: Text) -> None: ...

class Heartbeat(Frame):
    def __init__(self) -> None: ...

class ProtocolHeader(AMQPObject):
    frame_type: int
    major: int
    minor: int
    revision: int
    def __init__(self, major: Optional[int] = ..., minor: Optional[int] = ..., revision: Optional[int] = ...) -> None: ...

def decode_frame(data_in: bytes) -> Tuple[int, Optional[Frame]]: ...
