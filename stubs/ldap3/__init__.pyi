# incomplete

from typing import Literal

from .core.connection import Connection as Connection
from .core.server import Server as Server

ANONYMOUS: Literal["ANONYMOUS"]
SIMPLE: Literal["SIMPLE"]
SASL: Literal["SASL"]
NTLM: Literal["NTLM"]

IP_SYSTEM_DEFAULT: Literal["IP_SYSTEM_DEFAULT"]
IP_V4_ONLY: Literal["IP_V4_ONLY"]
IP_V6_ONLY: Literal["IP_V6_ONLY"]
IP_V4_PREFERRED: Literal["IP_V4_PREFERRED"]
IP_V6_PREFERRED: Literal["IP_V6_PREFERRED"]

BASE: Literal["BASE"]
LEVEL: Literal["LEVEL"]
SUBTREE: Literal["SUBTREE"]

DEREF_NEVER: Literal["NEVER"]
DEREF_SEARCH: Literal["SEARCH"]
DEREF_BASE: Literal["FINDING_BASE"]
DEREF_ALWAYS: Literal["ALWAYS"]

SYNC: Literal["SYNC"]
SAFE_SYNC: Literal["SAFE_SYNC"]
ASYNC: Literal["ASYNC"]
LDIF: Literal["LDIF"]
RESTARTABLE: Literal["RESTARTABLE"]
REUSABLE: Literal["REUSABLE"]
MOCK_SYNC: Literal["MOCK_SYNC"]
MOCK_ASYNC: Literal["MOCK_ASYNC"]
ASYNC_STREAM: Literal["ASYNC_STREAM"]

NONE: Literal["NO_INFO"]
DSA: Literal["DSA"]
SCHEMA: Literal["SCHEMA"]
ALL: Literal["ALL"]
