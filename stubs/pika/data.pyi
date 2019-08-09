from datetime import datetime
from decimal import Decimal
from typing import List, Union, Text, Mapping, Any, Dict

# stub only type aliases
TableKey = Union[Text, bytes]
# values of both list in dict are TableValues again
TableValue = Union[Text, bytes, bool, int, List[Any], Dict[TableKey, Any], None, Decimal, datetime]
Arguments = Mapping[TableKey, TableValue]

def encode_short_string(pieces: List[bytes], value: TableKey) -> int: ...
def encode_table(pieces: List[bytes], table: Mapping[TableKey, TableValue]) -> int: ...
def encode_value(pieces: List[bytes], value: TableValue) -> int: ...
