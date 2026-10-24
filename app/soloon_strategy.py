from app.base_element_strategy import BaseElementStrategy
from app.models.input_element import CreateElement,EraseElement

class SoloonStrategy(BaseElementStrategy):
  
  def create(self, new_element: CreateElement) -> None:
    print(f'create SoloonStrategy element in colum {new_element.column} '
    f'and row {new_element.row} '
    f'and candidate is {new_element.candidate_id}'
    )

  def erase(self, element: EraseElement)-> None:
    print(f'erase element in colum{element.column} and row {element.row} and candidate is {element.candidate_id}')