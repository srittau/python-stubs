# incomplete

from types import TracebackType
from typing import Any, Optional, Type, Union
from typing_extensions import Literal

from .server import Server

class Connection:
    # incomplete
    response: Optional[Any]
    def __init__(
        self,
        server: Union[Server, str],
        user: Optional[str] = ...,
        password: Optional[str] = ...,
        auto_bind: int = ...,
        version: int = ...,
        authentication: Optional[Literal["ANONYMOUS", "SIMPLE", "SASL", "NTLM"]] = ...,
        client_strategy: Literal["SYNC", "SAFE_SYNC", "ASYNC", "LDIF", "RESTARTABLE", "REUSABLE", "MOCK_SYNC", "MOCK_ASYNC", "ASYNC_STREAM"] = ...,
        auto_referrals: bool = ...,
        auto_range: bool = ...,
        sasl_mechanism: Optional[str] = ...,
        sasl_credentials: Optional[Any] = ...,
        check_names: bool = ...,
        collect_usage: bool = ...,
        read_only: bool = ...,
        lazy: bool = ...,
        raise_exceptions: bool = ...,
        pool_name: Optional[str] = ...,
        pool_size: Optional[str] = ...,
        pool_lifetime: Optional[int] = ...,
        cred_store: Optional[Any] = ...,
        fast_decoder: bool = ...,
        receive_timeout: Optional[Any] = ...,
        return_empty_attributes: bool = ...,
        use_referral_cache: bool = ...,
        auto_escape: bool = ...,
        auto_encode: bool = ...,
        pool_keepalive: Optional[Any] = ...,
        source_address: Optional[str] = ...,
        source_port: Optional[int] = ...,
        source_port_list: Optional[Any] = ...,
    ) -> None: ...
    def __enter__(self) -> Connection: ...
    def __exit__(
        self, exc_type: Optional[Type[BaseException]], exc_val: Optional[BaseException], exc_tb: Optional[TracebackType],
    ) -> Optional[Literal[False]]: ...
    def bind(self, read_server_info: bool = ..., controls: Optional[Any] = ...) -> Any: ...
    def search(
        self,
        search_base: str,
        search_filter: str,
        search_scope: Literal["BASE", "LEVEL", "SUBTREE"] = ...,
        dereference_aliases: Literal["NEVER", "SEARCH", "FINDING_BASE", "ALWAYS"] = ...,
        attributes: Optional[Any] = ...,
        size_limit: int = ...,
        time_limit: int = ...,
        types_only: bool = ...,
        get_operational_attributes: bool = ...,
        controls: Optional[Any] = ...,
        paged_size: Optional[int] = ...,
        paged_criticality: bool = ...,
        paged_cookie: Optional[str] = ...,
        auto_escape: Optional[bool] = ...,
    ) -> Any: ...
