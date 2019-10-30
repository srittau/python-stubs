import sys
from typing import Optional, Union

if sys.version_info >= (3,):
    from urllib.parse import ParseResult, SplitResult
else:
    from urlparse import ParseResult, SplitResult

class URL:
    def __init__(self, url: Union[str, ParseResult, SplitResult]) -> None: ...
    @classmethod
    def objectify(cls, url: Union[None, URL]) -> Optional[URL]: ...
