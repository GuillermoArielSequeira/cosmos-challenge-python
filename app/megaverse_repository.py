from app.base_element_strategy import BaseElementStrategy
from app.cometh_strategy import ComethStrategy
from app.mappers.megaverse_mapper import get_correct_mapper
from app.soloon_strategy import SoloonStrategy
from app.polyanet_strategy import PolyanetStrategy
from dataclasses import asdict

from app.models.input_element import CreateElement, CreateElementRequest, EraseElementRequest


class MegaVerseRepository:

  def __init__(self) -> None:
    self.strategy_mapper: dict[str, BaseElementStrategy] = {
    "COMETH": ComethStrategy(),
    "SOLOON": SoloonStrategy(),
    "POLYANET": PolyanetStrategy(),
  }

  def create_element(self, new_element_service: CreateElementRequest) -> None:
    elementMapper = get_correct_mapper(new_element_service.element)
    element_type = elementMapper.get('element_type')
    if element_type == None or element_type == "SPACE":
      return None
    strategy = self.strategy_mapper[element_type]
    
    create_element_param = {
      "row": new_element_service.row,
      "column": new_element_service.column,
      "candidate_id": new_element_service.candidate_id,
      "color": elementMapper.get('color'),
      "direction": elementMapper.get('direction')
    }
    
    create_strategy_param = CreateElement(**create_element_param)

    strategy.create(create_strategy_param)

  def erase_element(self, erase_element_repository: EraseElementRequest):
    pass

    