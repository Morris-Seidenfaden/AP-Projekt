import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv
from os import getenv
import requests

# Indlæs API-nøgle
load_dotenv("key.env")
API_KEY = getenv("API_KEY")

BASE_URL = "https://api.themoviedb.org/3"


# API-FUNKTIONER

def search_movies(query):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "query": query
    }
    response = requests.get(url, params=params)
    return response.json().get("results", [])


# GUI-FUNKTIONER

def perform_search():
    query = search_entry.get()

    if not query:
        messagebox.showwarning("Fejl", "Indtast en søgning")
        return

    results = search_movies(query)
    result_box.delete("1.0", tk.END)

    if not results:
        result_box.insert(tk.END, "Ingen film fundet.")
        return

    for movie in results[:5]:
        title = movie.get("title", "Ukendt titel")
        description = movie.get("overview", "Ingen beskrivelse")
        release_date = movie.get("release_date", "Ukendt")
        rating = movie.get("vote_average", "Ingen rating")

        year = release_date[:4] if release_date != "Ukendt" else "Ukendt"

        result_box.insert(tk.END, f"Titel: {title}\n")
        result_box.insert(tk.END, f"Udgivelsesår: {year}\n")
        result_box.insert(tk.END, f"Rating: {rating}\n")
        result_box.insert(tk.END, f"Beskrivelse: {description}\n")
        result_box.insert(tk.END, "-" * 40 + "\n")


# TKINTER GUI

root = tk.Tk()
root.title("Film Database")
root.geometry("600x500")

title_label = tk.Label(root, text="Film-søgning", font=("Arial", 18))
title_label.pack(pady=10)

search_entry = tk.Entry(root, width=40, font=("Arial", 12))
search_entry.pack(pady=5)

search_button = tk.Button(
    root,
    text="Søg",
    font=("Arial", 12),
    command=perform_search
)
search_button.pack(pady=10)

result_box = tk.Text(root, wrap=tk.WORD, width=70, height=20)
result_box.pack(pady=10)

root.mainloop()
