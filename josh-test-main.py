import subprocess

print("Attempting to install packages...")

for package in {"requests", "spotipy", "rake-nltk"}:
    p = subprocess.call(f"pip install {package}", shell=True)

from news_api import NewsAPI
from spotify_api import SpotifyAPI

news = NewsAPI()
spotify = SpotifyAPI(" ")

keywords = news.get_keywords(2)

print("\nKeywords:", keywords, end = 2 * "\n")

tracks = spotify.search_for_tracks(keywords)

print("Tracks:")

for t in tracks:
    print("-", t)

while 1: pass
