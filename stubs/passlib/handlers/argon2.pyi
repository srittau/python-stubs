# incomplete

class argon2:
    @classmethod
    def hash(cls, secret: str | bytes) -> str: ...
    @classmethod
    def verify(cls, secret: str | bytes, hash: str | bytes) -> bool: ...
