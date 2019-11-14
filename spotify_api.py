from api_base_class import APIBaseClass

class SpotifyAPI(APIBaseClass):
    """ Derived class which will interface with the Spotify API """
    
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
