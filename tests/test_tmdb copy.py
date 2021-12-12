from requests.api import request
import tmdb_client
from unittest.mock import Mock

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url
   #assert poster_url == "https://image.tmdb.org/t/p/w342/some-poster-path"

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def some_function_to_mock():
   raise Exception("Original was called")

def test_mocking(monkeypatch):
   my_mock = Mock()
   my_mock.return_value = 2

   monkeypatch.setattr("tests.test_tmdb.some_function_to_mock", my_mock)
   result = some_function_to_mock()
   assert result == 2

def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   #assert movies_list == mock_movies_list
   assert movies_list is None

"""
   def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"

    response = requests.get(endpoint_f, headers=headers)
    return response

    response.raise_for_status()
    return response.json()



def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

"""    

def test_call_tmdb_api(monkeypatch):
   mock_call_tmdb_api=['Movie 1', 'Movie 4']
   requests_mock=Mock()
   response=requests_mock.return_value
   response.json.return_value=mock_call_tmdb_api
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_list2 = tmdb_client.call_tmdb_api("movie/popular")
   assert movies_list2 == mock_call_tmdb_api