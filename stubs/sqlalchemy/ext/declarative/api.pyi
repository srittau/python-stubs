from typing import Type

from ...sql.schema import Table, MetaData

class DeclarativeMeta(type): ...
class _DeclarativeBase(metaclass=DeclarativeMeta):
    __table__: Table
    metadata: MetaData

def declarative_base() -> Type[_DeclarativeBase]: ...
