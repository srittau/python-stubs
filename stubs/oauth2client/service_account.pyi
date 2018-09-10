from typing import Protocol, Optional, Union, Iterable, Mapping

from .client import AssertionCredentials

class _Readable(Protocol):
    def read(self) -> bytes: ...

class ServiceAccountCredentials(AssertionCredentials):
    @classmethod
    def from_p12_keyfile_buffer(cls,
                                service_account_email: str, file_buffer: _Readable, private_key_password: Optional[str] = ...,
                                scopes: Union[str, Iterable[str]] = ..., token_uri: str = ..., revoke_uri: str = ...) \
            -> ServiceAccountCredentials: ...
    def create_with_claims(self, claims: Mapping[str, str]) -> ServiceAccountCredentials: ...
    def create_delegated(self, sub: str) -> ServiceAccountCredentials: ...
