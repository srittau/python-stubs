from typing import Any


class Row:
    def __getitem__(self, item: int) -> Any: ...
    @property
    def _mapping(self) -> RowMapping: ...

class RowMapping:
    def __getitem__(self, item: str) -> Any: ...
