from typing import Optional, Any, Type


class _Validator(object): ...

def validate(instance: object, schema: object, cls: Optional[Type[_Validator]] = None, *args: Any, **kwargs: Any) -> None: ...
