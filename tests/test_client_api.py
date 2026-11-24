from unittest.mock import MagicMock,patch
from app.clients.client_api import ClientApiClient
import pytest
import httpx
from unittest.mock import call



@pytest.fixture
def service_api():
  service = ClientApiClient()
  return service

@patch("app.clients.client_api.httpx.post")
def test_create_polynate(mock_post,service_api):
  mock_response = MagicMock()
  mock_response.status_code = 201
  mock_post.return_value = mock_response
  
  
  service_api.create_polyanet(1,"1","1")
  mock_post.assert_called_once_with("http://localhost:5001/polyanets", data={"candidateId":1, "row": "1", "column":"1"})

@patch("app.clients.client_api.time.sleep")
@patch("app.clients.client_api.httpx.post")
def test_attemps_service(mock_post,mock_sleep, service_api):
  response_429 = MagicMock()
  response_429.status_code = 429
  response_429.raise_for_status.side_effect = httpx.HTTPStatusError(
    "Too Many Requests",
    request=httpx.Request("POST", "http://localhost:5001/polyanets"),
    response=httpx.Response(429)
  )
  response_201 = MagicMock()
  response_201.status_code = 201
  # side_effect no sirve solamente para simular respuestas, también permite simular excepciones y comportamientos personalizados.
  mock_post.side_effect = [
    response_429,
    response_429,
    response_201
  ]

  service_api.create_polyanet(1, "1", "1")

  assert mock_post.call_count == 3
  assert mock_sleep.call_count == 2
  mock_sleep.assert_has_calls([
    call(1),
    call(2)
  ])

@patch("app.clients.client_api.time.sleep")
@patch("app.clients.client_api.httpx.post")
def test_maximum_retry_attempts(mock_post,mock_sleep, service_api):
  response_429 = MagicMock()
  response_429.status_code = 429
  response_429.raise_for_status.side_effect = httpx.HTTPStatusError(
    "Too Many Requests",
    request=httpx.Request("POST", "http://localhost:5001/polyanets"),
    response=httpx.Response(429)
  )
  mock_post.return_value = response_429

  with pytest.raises(RuntimeError, match="Maximum retry attempts exceeded"):
    service_api.create_polyanet(1, "1", "1")

  assert mock_post.call_count == 10
  assert mock_sleep.call_count == 9
  assert mock_sleep.call_args_list == [
    call(1),
    call(2),
    call(4),
    call(8),
    call(8),
    call(8),
    call(8),
    call(8),
    call(8),
  ]

@patch("app.clients.client_api.time.sleep")
@patch("app.clients.client_api.httpx.post")
def test_http_error_without_retry(mock_post,mock_sleep, service_api):
  response_500 = MagicMock()
  response_500.status_code = 500
  response_500.raise_for_status.side_effect = httpx.HTTPStatusError(
    "Internal server error",
    request=httpx.Request("POST", "http://localhost:5001/polyanets"),
    response=httpx.Response(500)
  )
  # return_value: simular un valor de retorno
  mock_post.return_value = response_500

  with pytest.raises(httpx.HTTPStatusError):
    service_api.create_polyanet(1, "1", "1")

  mock_post.assert_called_once()
  mock_sleep.assert_not_called()
  
  