from typing import Any


class Row:
    @property
    def _mapping(self) -> RowMapping: ...

class RowMapping:
    def __getitem__(self, item: str | int) -> Any: ...
