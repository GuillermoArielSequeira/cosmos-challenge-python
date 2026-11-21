import pytest

from app.mappers.megaverse_mapper import get_correct_mapper


@pytest.mark.parametrize(
  "element, expected",
  [
    ("POLYANET",{ 'element_type': 'POLYANET'}),
    ("SPACE",{ 'element_type': 'SPACE'}),
    ("RED_SOLOON",{ 'element_type': 'SOLOON', 'color': 'red'}),
    ("BLUE_SOLOON",{ 'element_type': 'SOLOON', 'color': 'blue'}),
    ("PURPLE_SOLOON",{ 'element_type': 'SOLOON', 'color': 'purple'}),
    ("WHITE_SOLOON",{ 'element_type': 'SOLOON', 'color': 'white'}),
    ("DOWN_COMETH", { 'element_type': 'COMETH', 'direction': 'down'}),
    ("UP_COMETH",{ 'element_type': 'COMETH', 'direction': 'up'}),
    ("LEFT_COMETH",{ 'element_type': 'COMETH', 'direction': 'left'}),
    ("RIGHT_COMETH",{ 'element_type': 'COMETH', 'direction': 'right'}),
    ("UNKNOWN_ELEMENT", {})
  ]
)
def test_get_correct_mapper(element, expected):
  assert get_correct_mapper(element) == expected