from typing import Type, Any

from httplib2 import Http

from google.oauth2.service_account import Credentials
from oauth2client.client import Credentials as OACredentials

from .discovery_cache.base import Cache
from .http import HttpRequest
from .model import Model

class Resource(object):
    def __getattr__(self, item: str) -> Any: ...

def build(
    serviceName: str,
    version: str,
    *,
    http: Http | None = ...,
    discoveryServiceUrl: str = ...,
    developerKey: str | None = ...,
    model: Model | None = ...,
    requestBuilder: Type[HttpRequest] = ...,
    credentials: Credentials | OACredentials | None = ...,
    cache_discovery: bool = ...,
    cache: Cache | None = ...,
) -> Resource: ...
