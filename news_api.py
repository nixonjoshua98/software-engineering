import requests # Import Requests library for HTTP GET requests
import random

from rake_nltk import Rake # Keyword extraction module

class NewsAPI:
    URL = "https://newsapi.org/v2/top-headlines" # Target URl for the news API.

    ID = "2b6e854826644184a33debfa683e698a"
    
    def __init__(self):
        self.params = {"country": "gb", "apiKey": self.ID}

        self.rake = Rake(max_length=1)

    # Private method
    def __send_request(self):
        """
        Send a get request to the News API.
        
        Returns:
            Returns the request object.
        """
                
        request = requests.get(url=self.URL, params=self.params)

        # Throw an error if the request was denied.
        request.raise_for_status()

        return request

    # Private method
    def __get_headlines(self):
        """
        Send a get request to the News API.
        
        Returns:
            Returns a list containing todays headlines.
        """

        request = self.__send_request()

        return [h["title"] for h in request.json()[u'articles']]

    def get_keywords(self, numWords: int) -> list:
        """
        Extracts keywords from headlines

        Params:
            numWords <int>: maximum number of keywords which will be returned
        
        Returns:
            Returns a list of keywords based on the current headlines.
        """
                
        headlines = self.__get_headlines()

        words = []

        # Extract the keywords using the Rake module.
        for h in headlines:
            self.rake.extract_keywords_from_text(h)

            words.extend(self.rake.get_ranked_phrases())

        random.shuffle(words) # Shuffle the list so the keywords will be randomised.

        return words[0:numWords]

        

        
