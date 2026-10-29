import pytest
import requests


@pytest.mark.duckduckgo
@pytest.mark.api
def test_duckduckgo_instant_answer_api():
      #arrange
      url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

      #act
      response = requests.get(url)
      body = response.json()

      #assert
      assert response.status_code
      assert 'Python' in body['AbstractText']
