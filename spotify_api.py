import spotipy
import subprocess
import os
import dataclasses
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials
from json.decoder import JSONDecodeError

from news_api import NewsAPI

@dataclasses.dataclass
class Track:
    artists: list
    album: str
    name: str

class SpotifyAPI(object):
    SCOPE = "user-read-private user-read-playback-state user-modify-playback-state"
    
    CLIENT_ID = "977f90e4dc0b4afb98bcab0b6fd466bf"
    CLIENT_SECRET = "aa12f933b7ef4475bba30d0009977816"

    URI = "http://localhost:8888/callback"

    def __init__(self, username: str):
        self.username = username
        self.spotifyObject = None

        os.environ["SPOTIPY_CLIENT_ID"] = self.CLIENT_ID
        os.environ["SPOTIPY_CLIENT_SECRET"] = self.CLIENT_SECRET
        os.environ["SPOTIPY_REDIRECT_URI"] = self.URI

        token = self.get_permission()
        
        self.create_object(token)

    def get_permission(self) -> str:
        try:
            token = util.prompt_for_user_token(self.username, self.SCOPE)
            
        except (AttributeError, JSONDecodeError):
            os.remove(f".cache-{self.username}")

            token = util.prompt_for_user_token(self.username, self.SCOPE)

        return token

    def create_object(self, token: str):
        self.spotifyObject = spotipy.Spotify(auth=token)

    def search_for_tracks(self, words: list) -> list:
        results = self.spotifyObject.search(f"{','.join(words)}")

        tracks = []
        
        for track in results["tracks"]["items"]:
            album_name = track["album"]["name"]
            track_name = track["name"]
            artists = [a["name"] for a in track["album"]["artists"]]

            tracks.append(Track(artists, album_name, track_name))

        return tracks

key_words = NewsAPI("2b6e854826644184a33debfa683e698a").get_headlines()
spotify_api = SpotifyAPI(" ")

print("Keywords:", key_words)

tracks = spotify_api.search_for_tracks(key_words)

for i in tracks:
    print(i)








    
