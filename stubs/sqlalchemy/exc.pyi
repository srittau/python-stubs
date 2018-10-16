from typing import ClassVar


class SQLAlchemyError(Exception):
    code: ClassVar[str]

class StatementError(SQLAlchemyError): ...
class DBAPIError(StatementError): ...
class DatabaseError(DBAPIError): ...
class IntegrityError(DatabaseError): ...