from typing import Optional, Type, Union

from .handlers.pbkdf2 import Pbkdf2DigestHandler

# dynamically created by create_pbkdf2_hash()
class _DynamicPbkdf2DigestHandler(Pbkdf2DigestHandler):
    name: str
    ident: str
    checksum_size: int
    encoded_checksum_size: int

    @classmethod
    def from_string(cls, hash: Union[str, bytes]) -> _DynamicPbkdf2DigestHandler: ...  # type: ignore
    def to_string(self) -> str: ...

def create_pbkdf2_hash(hash_name: str, digest_size: int, rounds: int = ..., ident: Optional[str] = ...,
                       module: str = ...) -> Type[_DynamicPbkdf2DigestHandler]: ...

pbkdf2_sha1: Type[_DynamicPbkdf2DigestHandler]
pbkdf2_sha256: Type[_DynamicPbkdf2DigestHandler]
pbkdf2_sha512: Type[_DynamicPbkdf2DigestHandler]
