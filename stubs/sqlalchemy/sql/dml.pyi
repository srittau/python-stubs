from typing import Any, TypeVar

from .base import DialectKWArgs, Executable
from .elements import ClauseElement
from .selectable import HasCTE, HasPrefixes

_T = TypeVar("_T")

class UpdateBase(HasCTE, DialectKWArgs, HasPrefixes, Executable, ClauseElement): ...

class ValuesBase(UpdateBase):
    def values(self: _T, *args: Any, **kwargs: Any) -> _T: ...

class Insert(ValuesBase): ...

class Delete(UpdateBase):
    def where(self, whereclause: ClauseElement) -> Delete: ...
