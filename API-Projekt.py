from dotenv import load_dotenv
from os import getenv
import requests
import random

# Indlæs API key
load_dotenv("key.env")
API_KEY = getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY ikke fundet. Tjek at 'key.env' eksisterer og API_KEY er sat korrekt.")

# TMDB endpoint
url = "https://api.themoviedb.org/3/movie/popular"

# Query parameters (V3 bruger APIkey i URL!)
params = {
    "api_key": API_KEY,
    "language": "en-US",
    "page": 1
}
# Request
response = requests.get(url, params=params)
data = response.json()

# Debug hvis noget går galt:
# print(data)

if "results" not in data:
    print("Fejl fra TMDB:", data)
else:
    film = random.choice(data["results"])
    print("Titel:", film["title"])
