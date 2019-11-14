from rake_nltk import Rake # Keyword extraction library
import requests # Import Requests library for HTTP GET requests

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

text = """ISIS Suspect Trapped at Turkish-Greek Border Is to Be Deported to U.S. - The New York Times""" # Test headline
split_test = text.split(" - ")[0] # Split string at ' - ' which indicated the publisher and exclude this from our keyword searching
r.extract_keywords_from_text(split_test) # Extract all keywords
a = r.get_ranked_phrases()  # Get keywords ranked highest to lowest relevance
print(a) # Print output

