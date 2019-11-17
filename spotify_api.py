from api_base_class import APIBaseClass

import spotipy
import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials

username="nixon.anita"

class SpotifyAPI(APIBaseClass):
    """ Derived class which will interface with the Spotify API """

    URL = "https://api.spotify.com/v1/recommendations"
    
    def __init__(self, _id, secret=None):
        super().__init__(_id, secret)  # Call the base class initiliser

        self.credentials = SpotifyClientCredentials(self.id, self.secret)

    def get_songs(self, numSongs: int) -> list:
        """
        Send a get request to the Spotify API.

        Args:
            numSongs: Number of songs wanted.

        Returns:
            Returns a list containing song titles.
        """

        #token = util.prompt_for_user_token(username, client_id=self.id, client_secret=self.secret, redirect_uri="http://localhost:8888/callback")            
        
        spotify = spotipy.Spotify(client_credentials_manager=self.credentials)
        
        results = spotify.search(q="artist: Eminem", type='artist')

        print(results)

spotify = SpotifyAPI(
    "977f90e4dc0b4afb98bcab0b6fd466bf",
    "aa12f933b7ef4475bba30d0009977816"
    )

songs = spotify.get_songs(5)

print(songs)
