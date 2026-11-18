from app.megaverse_repository import MegaVerseRepository
from app.models.input_element import CreateElementRequest, EraseElementRequest

class MegaVerseService:
  def __init__(self,repository: MegaVerseRepository) -> None:
    self.repository = repository


  def solve_map(self, candidate_id, matrix):
    # simulamos pegada al cliente  on candidate_id
    for i,row in enumerate(matrix):
      for j,element in enumerate(row):
        if element == 'SPACE':
          continue
        element_request_params = {
          "candidate_id":candidate_id,
          "element": element,
          "row": i,
          "column": j
        }
        element_request = CreateElementRequest(**element_request_params)
        self.repository.create_element(element_request)

  def erase_map(self, candidate_id, erase_element):
    # simulamos pegada al cliente  on candidate_id
    matrix = erase_element.get("map").get("content")
    for i,row in enumerate(matrix):
      for j,column in enumerate(row):
        if(column == None):
          continue
          
        type_element = column.get("type")
        element_request_params = {
        "candidate_id":candidate_id,
        "element_type": type_element,
        "row": i,
        "column": j
        }
        element_request = EraseElementRequest(**element_request_params)
        self.repository.erase_element(element_request)