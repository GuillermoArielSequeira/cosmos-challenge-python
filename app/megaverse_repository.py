from app.cometh_strategy import ComethStrategy
from app.soloon_strategy import SoloonStrategy
from app.polyanet_strategy import PolyanetStrategy

from app.models.input_element import NewElementService


class MegaVerseRepository:

  def __init__(self) -> None:
    self.strategy_mapper = {
    "COMETH": ComethStrategy(),
    "SOLOON": SoloonStrategy(),
    "POLYANET": PolyanetStrategy(),
  }

  def get_correct_mapper(self,element):
    match element:
      case "POLYANET":
        return { 'element_type': 'POLYANET'}
      case "SPACE":
        return { 'element_type': 'SPACE'} 
      case "RED_SOLOON":
        return { 'element_type': 'SOLOON', 'color': 'red'}
      case "DOWN_COMETH":
        return { 'element_type': 'COMETH', 'direction': 'down'}
      case _:
        return {}

  def create_element(self, new_element_service: NewElementService):
    elementMapper = self.get_correct_mapper(new_element_service.element)
    strategy = self.strategy_mapper[elementMapper.element_type]
    
    new_element_cp = new_element_service.copy()
    new_element_cp.pop("element")    

    elementMapper_cp = elementMapper.copy() 
    elementMapper_cp.pop('element_type')

    params = {
      *elementMapper_cp,
      *new_element_cp
    }
    strategy.create(params)
    