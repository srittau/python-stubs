from typing import Any

def instrument_declarative(cls: Any, cls_registry: Any, metadata: Any) -> None: ...

class ConcreteBase:
    @classmethod
    def __declare_first__(cls) -> None: ...

class AbstractConcreteBase(ConcreteBase):
    __no_table__: bool
    @classmethod
    def __declare_first__(cls) -> None: ...

class DeferredReflection:
    @classmethod
    def prepare(cls, engine: Any) -> None: ...
