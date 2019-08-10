class PlainCredentials(object):
    TYPE: str
    username: str
    password: str
    erase_on_connect: bool
    def __init__(self, username: str, password: str, erase_on_connect: bool = ...) -> None: ...

class ExternalCredentials(object): ...
