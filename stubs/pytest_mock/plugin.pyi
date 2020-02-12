# incomplete

from typing import Any


class MockFixture:
    mock_module: Any  # unittest.mock module
    def __init__(self, config: Any) -> None: ...
    patch: _Patcher

    class _Patcher:
        mock_module: Any  # unittest.mock module
        def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
