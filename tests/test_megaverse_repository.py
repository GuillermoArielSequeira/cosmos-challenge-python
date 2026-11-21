from unittest.mock import Mock
import pytest

from app.megaverse_repository import MegaVerseRepository
from app.models.input_element import CreateElement, CreateElementRequest, EraseElement, EraseElementRequest
from app.base_element_strategy import BaseElementStrategy


@pytest.fixture
def repository_with_mock_strategies():
  polynet_mock = Mock(spec=BaseElementStrategy)
  soloon_mock = Mock(spec=BaseElementStrategy)
  cometh_mock = Mock(spec=BaseElementStrategy)
  
  repository = MegaVerseRepository()
  repository.strategy_mapper["POLYANET"] = polynet_mock
  repository.strategy_mapper["SOLOON"] = soloon_mock
  repository.strategy_mapper["COMETH"] = cometh_mock

  return repository


def test_create_polyanet(repository_with_mock_strategies):

  create_element = CreateElementRequest(
      row=0,
      column=0,
      candidate_id=1,
      element='POLYANET'
  )
  repository_with_mock_strategies.create_element(create_element)


  repository_with_mock_strategies.strategy_mapper["SOLOON"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["COMETH"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["POLYANET"].create.assert_called_once_with(CreateElement(
      row=0,
      column=0,
      candidate_id=1, 
    ))

def test_create_soloon(repository_with_mock_strategies):


  create_element = CreateElementRequest(
    row=0,
    column=0,
    candidate_id=1,
    element='PURPLE_SOLOON'
  )

  repository_with_mock_strategies.create_element(create_element)


  repository_with_mock_strategies.strategy_mapper["POLYANET"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["COMETH"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["SOLOON"].create.assert_called_once_with(CreateElement(
      row=0,
      column=0,
      candidate_id=1,
      color='purple' 
    ))

def test_create_cometh(repository_with_mock_strategies):

  create_element = CreateElementRequest(
    row=0,
    column=0,
    candidate_id=1,
    element='RIGHT_COMETH'
  )

  repository_with_mock_strategies.create_element(create_element)


  repository_with_mock_strategies.strategy_mapper["POLYANET"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["SOLOON"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["COMETH"].create.assert_called_once_with(CreateElement(
      row=0,
      column=0,
      candidate_id=1,
      direction='right' 
    ))

def test_erase_polyanet(repository_with_mock_strategies):
  erase_element = EraseElementRequest(
    row="0",
    column="0",
    candidate_id=1,
    element_type=0
  )
  repository_with_mock_strategies.erase_element(erase_element)
  repository_with_mock_strategies.strategy_mapper["COMETH"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["SOLOON"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["POLYANET"].erase.assert_called_once_with(EraseElement(
    row="0",
    column="0",
    candidate_id=1
  ))
  

def test_erase_sollon(repository_with_mock_strategies):
  erase_element = EraseElementRequest(
    row="1",
    column="1",
    candidate_id=1,
    element_type=1
  )
  repository_with_mock_strategies.erase_element(erase_element)
  repository_with_mock_strategies.strategy_mapper["COMETH"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["POLYANET"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["SOLOON"].erase.assert_called_once_with(EraseElement(
    row="1",
    column="1",
    candidate_id=1
  ))

def test_erase_cometh(repository_with_mock_strategies):
  erase_element = EraseElementRequest(
    row="2",
    column="2",
    candidate_id=1,
    element_type=2
  )
  repository_with_mock_strategies.erase_element(erase_element)
  repository_with_mock_strategies.strategy_mapper["SOLOON"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["POLYANET"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["COMETH"].erase.assert_called_once_with(EraseElement(
    row="2",
    column="2",
    candidate_id=1
  ))

def test_erase_invalid_element(repository_with_mock_strategies):
  erase_element = EraseElementRequest(
    row="2",
    column="2",
    candidate_id=1,
    element_type=99
  )
  with pytest.raises(ValueError, match="Unknown element type"):
    repository_with_mock_strategies.erase_element(erase_element)

  repository_with_mock_strategies.strategy_mapper["SOLOON"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["POLYANET"].erase.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["COMETH"].erase.assert_not_called()

def test_create_space(repository_with_mock_strategies):
  create_element = CreateElementRequest(
    row=0,
    column=0,
    candidate_id=1,
    element='SPACE'
  )

  result = repository_with_mock_strategies.create_element(create_element)
  assert result is None


  repository_with_mock_strategies.strategy_mapper["POLYANET"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["SOLOON"].create.assert_not_called()
  repository_with_mock_strategies.strategy_mapper["COMETH"].create.assert_not_called()