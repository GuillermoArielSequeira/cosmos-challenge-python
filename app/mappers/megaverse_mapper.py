def get_correct_mapper(element):
  match element:
    case "POLYANET":
      return { 'element_type': 'POLYANET'}
    case "SPACE":
      return { 'element_type': 'SPACE'} 
    case "RED_SOLOON":
      return { 'element_type': 'SOLOON', 'color': 'red'}
    case "BLUE_SOLOON":
      return { 'element_type': 'SOLOON', 'color': 'blue'}
    case "PURPLE_SOLOON":
      return { 'element_type': 'SOLOON', 'color': 'purple'}
    case "WHITE_SOLOON":
      return { 'element_type': 'SOLOON', 'color': 'white'}
    case "DOWN_COMETH":
      return { 'element_type': 'COMETH', 'direction': 'down'}
    case "UP_COMETH":
      return { 'element_type': 'COMETH', 'direction': 'up'}
    case "LEFT_COMETH":
      return { 'element_type': 'COMETH', 'direction': 'left'}
    case "RIGHT_COMETH":
      return { 'element_type': 'COMETH', 'direction': 'right'}
    case _:
      return {}

def get_correct_mapper_to_delete(element):
  match element:
    case 0:
      return { 'element_type': 'POLYANET'}
    case 1:
      return { 'element_type': 'SOLOON'}
    case 2:
      return { 'element_type': 'COMETH'}
    case _:
      return {}