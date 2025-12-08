from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv("key.env")
API_KEY = getenv("API_KEY")


BASE_URL = "https://api.themoviedb.org/3"

def get_popular_movies():
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": API_KEY, "language": "en-US"}
    return requests.get(url, params=params).json()["results"]


def search_movies(query):
    url = f"{BASE_URL}/search/movie"
    params = {"api_key": API_KEY, "query": query}
    return requests.get(url, params=params).json()["results"]


def get_movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {"api_key": API_KEY, "append_to_response": "credits"}
    return requests.get(url, params=params).json()


def get_genres():
    url = f"{BASE_URL}/genre/movie/list"
    params = {"api_key": API_KEY}
    return requests.get(url, params=params).json()["genres"]