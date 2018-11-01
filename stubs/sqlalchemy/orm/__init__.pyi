from typing import Any, Optional, List

from ..sql.schema import Column
from .query import Query as Query


def relationship(argument: Any, *, secondary: Optional[Any] = ..., foreign_keys: List[Column] = ...,
                 backref: Optional[str] = ...) -> Any: ...
relation = relationship
