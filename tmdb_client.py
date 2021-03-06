import requests
import os
api_token = os.environ.get("TMDB_API_TOKEN", "")
#api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MjUxMDZmMjM5NDhjMWQzNDBiNjcxYjUxMWYxNjExNyIsInN1YiI6IjYxOWU0NWEzMzEwMzI1MDA0MzZiN2JiNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xhHIchVIGim0YU97QwzCT5s26JNqGViD7moe15F8Py8"

def headers_f(endpoint_f):
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint_f, headers=headers)
    return response

def call_tmdb_api(endpoint):
    full_url = f"https://api.themoviedb.org/3/{endpoint}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(full_url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    response=headers_f(endpoint)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many, list_type):
    
    if list_type not in ["top_rated", "upcoming", "popular", "now_playing"]:
        list_type="popular"
    data=get_movies_list(list_type)
    return data["results"][:how_many]

def get_cast(movie_id,how_many2):
    data2 = get_single_movie_cast(movie_id)
    return data2[:how_many2]

def get_movies_list(list_type):
    return call_tmdb_api(f"movie/{list_type}")

def get_single_movie(movie_id):
    return call_tmdb_api(f"movie/{movie_id}")

def get_movie_images(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/images")

def get_single_movie_cast(movie_id):
    return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]
