from typing import Optional, Type, Any

from httplib2 import Http

from oauth2client.client import Credentials

from .discovery_cache.base import Cache
from .http import HttpRequest
from .model import Model

class Resource(object):
    def __getattr__(self, item: str) -> Any: ...

def build(serviceName: str,
          version: str,
          *,
          http: Optional[Http] = ...,
          discoveryServiceUrl: str = ...,
          developerKey: Optional[str] = ...,
          model: Optional[Model] = ...,
          requestBuilder: Type[HttpRequest] = ...,
          credentials: Optional[Credentials] = ...,
          cache_discovery: bool = ...,
          cache: Optional[Cache] = ...) -> Resource: ...
