from typing import Union, Protocol, Any


class _StringReader(Protocol):
    def read(self, size: int) -> str: ...

class _BytesReader(Protocol):
    def read(self, size: int) -> bytes: ...

def parse(doc: Union[str, bytes, _StringReader, _BytesReader], treebuilder: str = ..., namespaceHTMLElements: bool = ...,
          **kwargs: Any) -> Any: ...
