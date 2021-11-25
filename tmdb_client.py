import requests
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0MjUxMDZmMjM5NDhjMWQzNDBiNjcxYjUxMWYxNjExNyIsInN1YiI6IjYxOWU0NWEzMzEwMzI1MDA0MzZiN2JiNSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.xhHIchVIGim0YU97QwzCT5s26JNqGViD7moe15F8Py8"


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_cast(movie_id,how_many2):
    data2 = get_single_movie_cast(movie_id)
    return data2[:how_many2]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()