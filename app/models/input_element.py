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
class NewElementService(InputElement):
  element = {
  'POLYANET': 'POLYANET',
  'RED_SOLOON': 'RED_SOLOON',
  'BLUE_SOLOON': 'BLUE_SOLOON',
  'PURPLE_SOLOON': 'PURPLE_SOLOON',
  'WHITE_SOLOON': 'WHITE_SOLOON',
  'DOWN_COMETH': 'DOWN_COMETH',
  'UP_COMETH': 'UP_COMETH',
  'LEFT_COMETH': 'LEFT_COMETH',
  'RIGHT_COMETH': 'RIGHT_COMETH',
  'SPACE': 'SPACE',
  }