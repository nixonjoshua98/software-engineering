import spotipy

from spotipy import util
from spotipy.oauth2 import SpotifyClientCredentials

import os
import dataclasses

from json.decoder import JSONDecodeError

@dataclasses.dataclass
class Track:
    """
    Storage class for tracks which will be returned from the SpotifyAPI
    """
    
    artists: list
    album: str
    name: str

class SpotifyAPI:
    #SCOPE = "user-read-private user-read-playback-state user-modify-playback-state"
    SCOPE = " "
    
    CLIENT_ID = "977f90e4dc0b4afb98bcab0b6fd466bf"
    CLIENT_SECRET = "aa12f933b7ef4475bba30d0009977816"

    URI = "http://localhost:8888/callback"

    def __init__(self, username: str):
        self.username = username
        self.spotifyObject = None

        os.environ["SPOTIPY_CLIENT_ID"] = self.CLIENT_ID
        os.environ["SPOTIPY_CLIENT_SECRET"] = self.CLIENT_SECRET
        os.environ["SPOTIPY_REDIRECT_URI"] = self.URI

        token = self.__get_permission()
        
        self.__create_object(token)

    # Private method
    def __get_permission(self) -> str:
        try:
            token = util.prompt_for_user_token(self.username, self.SCOPE)
            
        except (AttributeError, JSONDecodeError) as e:
            os.remove(f".cache-{self.username}")

            token = util.prompt_for_user_token(self.username, self.SCOPE)

        return token

    # Private method
    def __create_object(self, token: str):
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







    
