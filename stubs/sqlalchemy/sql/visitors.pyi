from typing import Tuple, Dict, Any


class VisitableType(type):
    def __init__(cls, clsname: str, bases: Tuple[type, ...], clsdict: Dict[str, Any]) -> None: ...

class Visitable(metaclass=VisitableType): ...
