from requests.api import request
import tmdb_client
import pytest
from unittest.mock import Mock
from main import app

def test_call_tmdb_api(monkeypatch):
   movie_id="580489"
   mock_call_tmdb_api=['Movie 1']
   requests_mock=Mock()
   response=requests_mock.return_value
   response.json.return_value=mock_call_tmdb_api
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   single_movie = tmdb_client.call_tmdb_api(f"movie/{movie_id}")
   assert single_movie == mock_call_tmdb_api


def test_get_single_movie_not_None():
   movie_id="580489"
   movie_580489 = tmdb_client.get_single_movie(movie_id)
   assert movie_580489 is not None

def test_get_single_movie_mock(monkeypatch):
   movie_id="580489"
   mock_get_single_movie=['Movie 1']
   requests_mock=Mock()
   response=requests_mock.return_value
   response.json.return_value=mock_get_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   single_movie2 = tmdb_client.call_tmdb_api(f"movie/{movie_id}")
   assert single_movie2 == mock_get_single_movie


def test_get_movie_image_not_None():
   movie_id="580489"
   movie_image_580489 = tmdb_client.get_single_movie(movie_id)
   assert movie_image_580489 is not None

def test_get_movie_images_mock(monkeypatch):
   movie_id="580489"
   mock_get_movie_images=['Movie images']
   requests_mock=Mock()
   response=requests_mock.return_value
   response.json.return_value=mock_get_movie_images
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_images = tmdb_client.call_tmdb_api(f"movie/{movie_id}/images")
   assert movie_images == mock_get_movie_images


def test_get_single_movie_cast_not_None():
   movie_id="580489"
   movie_cast_580489 = tmdb_client.get_single_movie_cast(movie_id)
   assert movie_cast_580489 is not None

def test_get_single_movie_cast_mock(monkeypatch):
   movie_id="580489"
   cast=1
   mock_get_movie_cast=1
   requests_mock=Mock()
   response=requests_mock.return_value
   response.json.return_value=mock_get_movie_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_cast = tmdb_client.call_tmdb_api(f"movie/{movie_id}/credits[{cast}]")
   assert movie_cast == mock_get_movie_cast

@pytest.mark.parametrize('list_type', (
  ("top_rated"), 
  ("upcoming"),
  ("popular"),
  ("now_playing")
))

def test_homepage(list_type,monkeypatch):
   api_mock = Mock(return_value={'results': []})
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       response = client.get(f'/?list_type={list_type}')
       assert response.status_code == 200
       api_mock.assert_called_once_with(f'movie/{list_type}')
