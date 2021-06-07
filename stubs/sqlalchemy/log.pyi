from typing import Any

class Identified:
    logging_name: str | None

def __getattr__(__name: str) -> Any: ...  # incomplete
