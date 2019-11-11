from api_base_class import APIBaseClass


class NewsAPI(APIBaseClass):
    """ Derived class which will interface with the News API """
    
    def __init__(self, _id, secret=None):
        super().__init__(_id, secret)  # Call the base class initiliser

    def get_headlines(self) -> list:
        """
        Send a get request to the News API.

        Returns:
            Returns a list containing todays headlines.
        """
