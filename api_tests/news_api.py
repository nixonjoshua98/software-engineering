# Import Requests library for HTTP GET requests
import requests

# NewsAPI URL to fire a GET request to
URL = "https://newsapi.org/v2/top-headlines"
# Params for retrieving top headlines from GB and our API Key (API Key must be present otherwise the API request will fail (401))
PARAMS = {"country": "gb", "apiKey": "2b6e854826644184a33debfa683e698a"}

# Initiate our GET request to NewsAPI
request = requests.get(url = URL, params= PARAMS)

# Retrieve JSON data from the response and read the articles key in the dictionary response
## Articles is a unicode array so python formats it as u'articles', without this u the key will not be found
articles = request.json()[u'articles']

# Print total articles returned
print('Total articles returned: ', len(articles))