from unittest.mock import Mock, call

from app.megaverse_service import MegaVerseService
from app.models.input_element import CreateElementRequest, EraseElement, EraseElementRequest

def test_erase_map():
  repository = Mock()

  service = MegaVerseService(repository)
  service.erase_map(1,{
    "map": {
        "content": [
            [{"type": 0}, None],
            [None, {"type": 1, "color": "red"}]
        ]
    }})


  llamadas_esperadas = [
    call(EraseElementRequest(   
    row=0,
    column=0,
    candidate_id=1,
    element_type=0
    )),
    call(EraseElementRequest(
    row=1,
    column=1,
    candidate_id=1,
    element_type=1
    ))
  ]   

  repository.erase_element.assert_has_calls(llamadas_esperadas)
  assert repository.erase_element.call_count == 2

def test_solve_map():
  repository = Mock()
  service = MegaVerseService(repository)
  service.solve_map(1,[
     ["POLYANET", "SPACE", "SPACE"],
     ["SPACE", "RIGHT_COMETH", "SPACE"],
     ["SPACE", "SPACE", "PURPLE_SOLOON"]
   ])

  llamadas_esperadas = [
    call(CreateElementRequest(
      row=0,
      column=0,
      candidate_id=1,
      element='POLYANET'  
    )),
    call(CreateElementRequest(
      row=1,
      column=1,
      candidate_id=1,
      element='RIGHT_COMETH'  
    )),
    call(CreateElementRequest(
      row=2,
      column=2,
      candidate_id=1,
      element='PURPLE_SOLOON' 
    ))
  ]
  repository.create_element.assert_has_calls(llamadas_esperadas)
  assert repository.create_element.call_count == 3