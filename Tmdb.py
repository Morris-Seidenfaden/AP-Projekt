from dotenv import load_dotenv
from os import getenv
import requests

load_dotenv("key.env")
API_KEY = getenv("API_KEY")


BASE_URL = "https://api.themoviedb.org/3"
