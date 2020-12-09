# incomplete

from typing import Any, Optional, Type, TypeVar

_T = TypeVar("_T")


class LDAPException(Exception): ...

class LDAPOperationResult(LDAPException):
    def __new__(
        cls: Type[_T],
        result: Optional[Any] = ...,
        description: Optional[Any] = ...,
        dn: Optional[Any] = ...,
        message: Optional[Any] = ...,
        response_type: Optional[Any] = ...,
        response: Optional[Any] = ...,
    ) -> _T: ...
    def __init__(
        self,
        result: Optional[Any] = ...,
        description: Optional[Any] = ...,
        dn: Optional[Any] = ...,
        message: Optional[Any] = ...,
        response_type: Optional[Any] = ...,
        response: Optional[Any] = ...,
    ) -> None: ...

class LDAPInvalidCredentialsResult(LDAPOperationResult): ...

class LDAPExceptionError(LDAPException): ...
class LDAPPasswordIsMandatoryError(LDAPExceptionError): ...
