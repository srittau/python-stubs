# incomplete

from abc import abstractmethod

# incomplete
class Dialect:
    @abstractmethod
    @property
    def name(self) -> str: ...
    @abstractmethod
    @property
    def paramstyle(self) -> str: ...

class Connectable: ...  # incomplete
