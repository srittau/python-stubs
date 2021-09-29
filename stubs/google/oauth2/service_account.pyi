from collections.abc import Mapping, Sequence
from typing import Any

class Credentials:
    def __init__(self,
        signer: Any,
        service_account_email: str,
        token_uri: str,
        scopes: Sequence[str] | None = ...,
        default_scopes: Sequence[str] | None = ...,
        subject: str | None = ...,
        project_id: str | None = ...,
        quota_project_id: str | None = ...,
        additional_claims: Mapping[str, str] | None = ...,
        always_use_jwt_access: bool | None = ...,
) -> None: ...
    @classmethod
    def from_service_account_file(cls, filename: str, **kwargs: Any) -> Credentials: ...

    def with_scopes(self, scopes: Sequence[str] | None, default_scopes: Sequence[str] | None = ...) -> Credentials: ...
    def with_subject(self, subject: str | None) -> Credentials: ...

    # incomplete
