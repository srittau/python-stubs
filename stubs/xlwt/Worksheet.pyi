from datetime import date, time
from decimal import Decimal
from typing import Union

from .ExcelFormula import Formula
from .Style import XFStyle

_Data = Union[float, Decimal, str, bytes, date, time, bool, None, Formula]

class Worksheet:
    def write(self, r: int, c: int, label: _Data = ..., style: XFStyle = ...) -> None: ...
