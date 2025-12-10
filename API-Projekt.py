from dotenv import load_dotenv
from os import getenv
import requests
import random

load_dotenv("key.env")
API_KEY = getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY ikke fundet. Tjek at 'key.env' eksisterer og API_KEY er sat korrekt.")

url = "https://api.themoviedb.org/3/movie/popular"

params = {
    "api_key": API_KEY,
    "language": "en-US",
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()


if "results" not in data:
    print("Fejl fra TMDB:", data)
else:
    film = random.choice(data["results"])
    print("Titel:", film["title"])
