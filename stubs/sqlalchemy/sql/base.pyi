from collections.abc import Iterable, Sequence
from typing import Any, Generic, TypeVar

from ..util import HasMemoized, ImmutableProperties, ordered_column_set
from .elements import ColumnElement
from .roles import StatementRole
from .traversals import HasCacheKey, HasCopyInternals
from .visitors import ClauseVisitor

_V = TypeVar("_V")

class Immutable:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class SingletonConstant(Immutable):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class DialectKWArgs:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class CompileState:
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class Generative(HasMemoized): ...
class InPlaceGenerative(HasMemoized): ...
class HasCompileState(Generative): ...

class _MetaOptions(type):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class Options(metaclass=_MetaOptions):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class CacheableOptions(Options, HasCacheKey): ...
class ExecutableOption(HasCopyInternals, HasCacheKey): ...

class Executable(StatementRole, Generative):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class prefix_anon_map(dict[str, _V], Generic[_V]):
    def __missing__(self, key: str) -> str: ...

class SchemaEventTarget: ...

class SchemaVisitor(ClauseVisitor): ...

class ColumnCollection:
    def __init__(self, columns: Sequence[ColumnElement[Any]] | None = ...) -> None: ...
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class DedupeColumnCollection(ColumnCollection):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class ImmutableColumnCollection(ImmutableProperties[ColumnElement[Any]], ColumnCollection):
    def __getattr__(self, __item: str) -> Any: ...  # incomplete

class ColumnSet(ordered_column_set):
    def contains_column(self, col: ColumnElement[Any]) -> bool: ...
    def extend(self, cols: Iterable[ColumnElement[Any]]) -> None: ...
    def __add__(self, other: ColumnSet) -> list[ColumnElement[Any]]: ...
    def __eq__(self, other: ColumnSet) -> bool: ...  # type: ignore
    def __hash__(self) -> int: ...  # type: ignore
