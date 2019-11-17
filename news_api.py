from api_base_class import APIBaseClass

# Import Requests library for HTTP GET requests
import requests
import random

from rake_nltk import Rake

class NewsAPI(APIBaseClass):
    """ Derived class which will interface with the News API """

    URL = "https://newsapi.org/v2/top-headlines" # NewsAPI URL to fire a GET request to
    
    def __init__(self, _id: str, secret=None):
        super().__init__(_id, secret)  # Call the base class initiliser

        self.params = {"country": "gb", "apiKey": self.id}

    def send_request(self):
        request = requests.get(url=self.URL, params=self.params)
        
        request.raise_for_status()

        return request
        
    def get_headlines(self) -> list:
        """
        Send a get request to the News API.
        
        Returns:
            Returns a list containing todays headlines.
        """

        r = Rake(max_length=1)

        request = self.send_request()

        words = []

        for h in request.json()[u'articles']:
            r.extract_keywords_from_text(h["title"])

            words.extend(r.get_ranked_phrases())

        random.shuffle(words)

        return words[0:1]
