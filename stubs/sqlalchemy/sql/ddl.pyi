# incomplete

from .base import Executable
from .elements import ClauseElement

class _DDLCompiles(ClauseElement): ...

# incomplete
class DDLElement(Executable, _DDLCompiles): ...
