from api_base_class import APIBaseClass

import requests # Import Requests library for HTTP GET requests

class NewsAPI(APIBaseClass):
    """ Derived class which will interface with the News API """
    def __init__(self, _id, secret=None):
        super().__init__(_id, secret)  # Call the base class initiliser
        self.URL = "https://newsapi.org/v2/top-headlines" # NewsAPI URL to fire a GET request to
        self.PARAMS = {"country": "gb", "apiKey": "2b6e854826644184a33debfa683e698a"}
    def get_headlines(self) -> list:
        """
        Send a get request to the News API.
        Returns:
            Returns a list containing todays headlines.
        """
        request = requests.get(url = URL, params= PARAMS)
        request.raise_for_status()

        # Retrieve JSON data from the response and read the articles key in the dictionary response
        ## Articles is a unicode array so python formats it as u'articles', without this u the key will not be found
        articles = request.json()[u'articles']
        # Articles is an array of news objects
        return articles
