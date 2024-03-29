from collections.abc import Callable
from typing import Any, TypeVar, overload

from ..engine.interfaces import Connectable
from ..sql.schema import MetaData
from . import interfaces

_ClsT = TypeVar("_ClsT", bound=type[Any])
_DeclT = TypeVar("_DeclT", bound=type[_DeclarativeBase])

# Dynamic class as created by registry.generate_base() via DeclarativeMeta
# or another metaclass. This class does not exist at runtime.
class _DeclarativeBase(Any):  # type: ignore[misc]  # super classes are dynamic
    registry: registry
    metadata: MetaData
    __abstract__: bool
    # not always existing:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    __mapper_cls__: Any
    __class_getitem__: Any

# Meta class (or function) that creates a _DeclarativeBase class.
_DeclarativeBaseMeta = Callable[[str, tuple[type[Any], ...], dict[str, Any]], type[_DeclT]]

def has_inherited_table(cls: type[Any]) -> bool: ...

class DeclarativeMeta(type):
    def __init__(cls, classname: str, bases: tuple[type[Any], ...], dict_: dict[str, Any], **kw: object) -> None: ...
    def __setattr__(cls, key: str, value: Any) -> None: ...
    def __delattr__(cls, key: str) -> None: ...

def synonym_for(name: Any, map_column: bool = ...) -> Any: ...

def declarative_mixin(cls: _ClsT) -> _ClsT: ...
@overload
def declarative_base(
    bind: Connectable | None = ...,
    metadata: MetaData | None = ...,
    mapper: Any | None = ...,
    cls: type[Any] | tuple[type[Any], ...] = ...,
    name: str = ...,
    constructor: Callable[..., None] = ...,
    class_registry: dict[str, type[Any]] | None = ...,
) -> type[_DeclarativeBase]: ...
@overload
def declarative_base(
    bind: Connectable | None = ...,
    metadata: MetaData | None = ...,
    mapper: Any | None = ...,
    cls: type[Any] | tuple[type[Any], ...] = ...,
    name: str = ...,
    constructor: Callable[..., None] = ...,
    class_registry: dict[str, type[Any]] | None = ...,
    *,
    metaclass: _DeclarativeBaseMeta[_DeclT],
) -> _DeclT: ...
@overload
def declarative_base(
    bind: Connectable | None,
    metadata: MetaData | None,
    mapper: Any | None,
    cls: type[Any] | tuple[type[Any], ...],
    name: str,
    constructor: Callable[..., None],
    class_registry: dict[str, type[Any]] | None,
    metaclass: _DeclarativeBaseMeta[_DeclT],
) -> _DeclT: ...

class registry:
    metadata: MetaData
    constructor: Callable[..., None]
    def __init__(
        self,
        metadata: MetaData | None = ...,
        class_registry: dict[str, type[Any]] | None = ...,
        constructor: Callable[..., None] = ...,
        _bind: Connectable | None = ...,
    ) -> None: ...
    @property
    def mappers(self) -> frozenset[Any]: ...
    def configure(self, cascade: bool = ...) -> None: ...
    def dispose(self, cascade: bool = ...) -> None: ...
    @overload
    def generate_base(
        self, mapper: Any | None = ..., cls: type[Any] | tuple[type[Any], ...] = ..., name: str = ...
    ) -> type[_DeclarativeBase]: ...
    @overload
    def generate_base(
        self,
        mapper: Any | None = ...,
        cls: type[Any] | tuple[type[Any], ...] = ...,
        name: str = ...,
        *,
        metaclass: _DeclarativeBaseMeta[_DeclT],
    ) -> _DeclT: ...
    @overload
    def generate_base(
        self,
        mapper: Any | None,
        cls: type[Any] | tuple[type[Any], ...],
        name: str,
        metaclass: _DeclarativeBaseMeta[_DeclT],
    ) -> type[_DeclarativeBase]: ...
    def mapped(self, cls: _ClsT) -> _ClsT: ...
    def as_declarative_base(
        self, *, mapper: Any | None = ..., metaclass: _DeclT = ...
    ) -> Callable[[_ClsT], _ClsT | _DeclT | Any]: ...
    def map_declaratively(self, cls: Any) -> Any: ...
    def map_imperatively(self, class_: Any, local_table: Any | None = ..., **kw: Any) -> Any: ...

def as_declarative(
    *,
    bind: Connectable | None = ...,
    metadata: MetaData | None = ...,
    class_registry: dict[str, type[Any]] | None = ...,
    mapper: Any | None = ...,
    metaclass: _DeclarativeBaseMeta[_DeclT] = ...,
) -> Callable[[_ClsT], _ClsT | _DeclT | Any]: ...
