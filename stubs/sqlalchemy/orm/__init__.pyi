from typing import Any, Optional

from .query import Query as Query


def relationship(argument: Any, *, secondary: Optional[Any] = ..., backref: Optional[str] = ...) -> Any: ...
relation = relationship
