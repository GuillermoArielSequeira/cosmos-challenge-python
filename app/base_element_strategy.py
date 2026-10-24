from abc import ABC, abstractmethod

from app.models.input_element import CreateElement,EraseElement

class BaseElementStrategy(ABC):
  @abstractmethod
  def create(self, new_element: CreateElement) -> None:
    pass
  @abstractmethod
  def erase(self, element_to_delete: EraseElement)-> None:
    pass