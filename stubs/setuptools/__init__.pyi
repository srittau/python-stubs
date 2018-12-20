from typing import Iterable, List, Any


class PackageFinder:
    @classmethod
    def find(cls, where: str = ..., exclude: Iterable[str] = ..., include: Iterable[str] = ...) -> List[str]: ...

find_packages = PackageFinder.find

def setup(**attrs: Any) -> Any: ...
