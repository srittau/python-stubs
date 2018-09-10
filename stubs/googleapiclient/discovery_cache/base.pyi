import abc
from typing import Optional


class Cache(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def get(self, url: str) -> Optional[str]: ...
  @abc.abstractmethod
  def set(self, url: str, content: str) -> None: ...
