import random

from newsapi import NewsApiClient

# Keyword extraction module
from rake_nltk import Rake

class NewsAPI:
    ID = "2b6e854826644184a33debfa683e698a"
    
    def __init__(self):       
        self.newsapi = NewsApiClient(api_key=self.ID)

    # Private method
    def __get_headlines(self, country: str, category: str) -> list:
        
        top_headlines = self.newsapi.get_top_headlines(category=category,
                                                       language="en",
                                                       country=country)
        # Return only yhe article titles
        return [h["title"] for h in top_headlines["articles"]]

    def get_keywords(self, numWords: int, country: str, category: str) -> list:
        """
        Extracts keywords from headlines

        Params:
            numWords <int>: maximum number of keywords which will be returned
        
        Returns:
            Returns a list of keywords based on the current headlines.
        """

        words = []
        rake = Rake(max_length=1)

        headlines = self.__get_headlines(country, category)

        for h in headlines:
            rake.extract_keywords_from_text(h)

            # Add the list from rake to the words list
            words.extend(rake.get_ranked_phrases())

        # Shuffle the list so the keywords will be randomised.
        random.shuffle(words)

        return words[0:numWords]

        

        
