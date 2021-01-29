from typing import Any, Optional
from typing_extensions import Literal


class Server:
    # incomplete
    def __init__(
        self,
        host: str,
        port: Optional[int] = ...,
        use_ssl: bool = ...,
        allowed_referral_hosts: Optional[Any] = ...,
        get_info: Literal["NO_INFO", "DSA", "SCHEMA", "ALL"] = ...,
        tls: Optional[Any] = ...,
        formatter: Optional[Any] = ...,
        connect_timeout: Optional[Any] = ...,
        mode: Literal["IP_SYSTEM_DEFAULT", "IP_V4_ONLY", "IP_V6_ONLY", "IP_V4_PREFERRED", "IP_V6_PREFERRED"] = ...,
        validator: Optional[Any] = ...,
    ) -> None: ...
