from typing import Any

from ...orm.decl_api import DeclarativeMeta as DeclarativeMeta
from .extensions import (
    AbstractConcreteBase as AbstractConcreteBase,
    ConcreteBase as ConcreteBase,
    DeferredReflection as DeferredReflection,
    instrument_declarative as instrument_declarative,
)

__all__ = [
    "declarative_base",
    "synonym_for",
    "has_inherited_table",
    "instrument_declarative",
    "as_declarative",
    "ConcreteBase",
    "AbstractConcreteBase",
    "DeclarativeMeta",
    "DeferredReflection",
]

def declarative_base(*arg: Any, **kw: Any) -> Any: ...
def as_declarative(*arg: Any, **kw: Any) -> Any: ...
def has_inherited_table(*arg: Any, **kw: Any) -> Any: ...
def synonym_for(*arg: Any, **kw: Any) -> Any: ...
