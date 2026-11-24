import httpx
import time
from functools import partial

class ClientApiClient:

  def _request_with_retry(self,request):
   for attempt in range(10):
    try:
      response = request()
      response.raise_for_status() 
      return response
    except httpx.HTTPStatusError as e:
      if e.response.status_code != 429:
        raise      
      
      if attempt == 9:
        raise RuntimeError("Maximum retry attempts exceeded") from e
      wait_time = min(2 ** attempt, 8)  
      time.sleep(wait_time)
      


      


  def create_polyanet(self,canidate_id,row,column):
    post_prepared = partial(
      httpx.post,
      "http://localhost:5001/polyanets",
      data={"candidateId":canidate_id, "row": row, "column":column}
    )
    
    return self._request_with_retry(post_prepared)