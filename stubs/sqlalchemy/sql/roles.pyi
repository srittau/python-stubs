from typing import Any

class SQLRole:
    allows_lambda: bool
    uses_inspection: bool

class StatementRole(SQLRole): ...

def __getattr__(__item: str) -> Any: ...  # incomplete
