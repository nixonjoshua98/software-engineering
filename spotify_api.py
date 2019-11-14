from api_base_class import APIBaseClass

import spotipy

class SpotifyAPI(APIBaseClass):
    """ Derived class which will interface with the Spotify API """

    URL = "https://api.spotify.com/v1/recommendations"
    
    def __init__(self, _id, secret=None):
        super().__init__(_id, secret)  # Call the base class initiliser

    def get_songs(self, numSongs: int) -> list:
        """
        Send a get request to the Spotify API.

        Args:
            numSongs: Number of songs wanted.

        Returns:
            Returns a list containing song titles.
        """

        spotify = spotipy.Spotify()

        results = spotify.search(q="artist:" + "Eminem", type="artist")

        items = results["artists"]["items"]

        print(items)
        

spotify = SpotifyAPI(
    "8f4d7a6dd25f4f84b48082e7eeba73d7",
    "4ebb0f15af7a4dd68b604fb66635131f"
    )

songs = spotify.get_songs(5)

print(songs)
