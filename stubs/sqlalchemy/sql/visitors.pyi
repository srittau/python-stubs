from typing import Tuple, Any

class TraversibleType(type):
    def __init__(cls, clsname: str, bases: Tuple[type, ...], clsdict: dict[str, Any]) -> None: ...

class Traversible(metaclass=TraversibleType): ...

class ExternalTraversal:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

VisitableType = TraversibleType
Visitable = Traversible
ClauseVisitor = ExternalTraversal

def __getattr__(__item: str) -> Any: ...  # incomplete
