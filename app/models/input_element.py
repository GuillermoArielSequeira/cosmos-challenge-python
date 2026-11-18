from typing import Optional
from dataclasses import dataclass

@dataclass
class InputElement:
 row:str
 column:str
 candidate_id:str 

@dataclass
class CreateElement(InputElement):
  color:Optional[str] = None
  direction:Optional[str] = None

@dataclass
class EraseElement(InputElement):
  pass

@dataclass
class CreateElementRequest(InputElement):
  element:str

@dataclass
class EraseElementRequest(InputElement):
  element_type:int 