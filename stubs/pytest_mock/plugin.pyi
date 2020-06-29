# Incomplete, more complete version in typeshed HEAD.

import unittest.mock
from typing import Any, TypeVar, overload
from unittest.mock import MagicMock

_T = TypeVar("_T")

class MockFixture:
    mock_module: unittest.mock module
    Mock: unittest.mock.Mock
    MagicMock: unittest.mock.MagicMock
    NonCallableMock: unittest.mock.NonCallableMock
    PropertyMock: unittest.mock.PropertyMock
    call: unittest.mock.call
    ANY: unittest.mock.ANY
    DEFAULT: unittest.mock.DEFAULT
    create_autospec: unittest.mock.create_autospec
    sentinel: unittest.mock.sentinel
    mock_open: unittest.mock.mock_open
    def __init__(self, config: Any) -> None: ...
    patch: _Patcher

    class _Patcher:
        mock_module: Any  # unittest.mock module
        @overload
        def __call__(self, target: Any, new: _T, *args: Any, **kwargs: Any) -> _T: ...
        @overload
        def __call__(self, target: Any, *args: Any, **kwargs: Any) -> MagicMock: ...
