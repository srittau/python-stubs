from typing import Tuple, Optional, Union, Type

from ..utils.handlers import HasRounds, HasRawSalt, HasRawChecksum, GenericHandler

class Pbkdf2DigestHandler(HasRounds, HasRawSalt, HasRawChecksum, GenericHandler):
    setting_kwds: Tuple[str, str, str] = ...
    checksum_chars: str = ...
    default_salt_size: int = ...
    max_salt_size: int = ...
    default_rounds: Optional[int] = ...
    min_rounds: int = ...
    max_rounds: int = ...
    rounds_cost: str = ...
    @classmethod
    def from_string(cls, hash: Union[str, bytes]) -> Pbkdf2DigestHandler: ...  # type: ignore
    def to_string(self) -> bytes: ...  # type: ignore

# dynamically created by create_pbkdf2_hash()
class _DynamicPbkdf2DigestHandler(Pbkdf2DigestHandler):
    name: str
    ident: str
    checksum_size: int
    encoded_checksum_size: int

def create_pbkdf2_hash(hash_name: str, digest_size: int, rounds: int = ..., ident: Optional[str] = ...,
                       module: str = ...) -> Type[_DynamicPbkdf2DigestHandler]: ...

pbkdf2_sha1: Type[_DynamicPbkdf2DigestHandler]
pbkdf2_sha256: Type[_DynamicPbkdf2DigestHandler]
pbkdf2_sha512: Type[_DynamicPbkdf2DigestHandler]
