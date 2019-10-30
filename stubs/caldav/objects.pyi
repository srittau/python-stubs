import datetime
import sys
from typing import List, Optional, Union, Any

from typing_extensions import Literal
from vobject.base import VBase

from .davclient import DAVClient
from .lib.url import URL

if sys.version_info >= (3,):
    from urllib.parse import ParseResult, SplitResult
else:
    from urlparse import ParseResult, SplitResult


class DAVObject(object):
    id: Optional[str]
    url: Optional[URL]
    client: Optional[DAVClient]
    parent: Optional[DAVObject]
    name: Optional[str]
    def __init__(
        self,
        client: Optional[DAVClient] = ...,
        url: Union[None, str, ParseResult, SplitResult, URL] = ...,
        parent: Optional[DAVObject] = ...,
        name: Optional[str] = ...,
        id: Optional[str] = ...,
        **extra: Any,
    ) -> None: ...
    def delete(self) -> None: ...

class Principal(DAVObject):
    def calendars(self) -> List[Calendar]: ...

class Calendar(DAVObject):
    def add_event(self, ical: str) -> Event: ...
    def event_by_uid(self, uid: str) -> Event: ...
    def date_search(
        self,
        start: datetime.datetime,
        end: datetime.datetime,
        compfilter: Optional[Literal["VEVENT"]] = ...,
        expand: Union[bool, Literal["maybe"]] = ...,
    ) -> List[Event]: ...

class CalendarObjectResource(DAVObject):
    vobject_instance: VBase

class Event(CalendarObjectResource): ...
