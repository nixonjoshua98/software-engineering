from api_base_class import APIBaseClass

class NewsAPI(APIBaseClass):
    def __init__(self, _id, secret=None):
        super().__init__(_id, secret)

    def get_headlines(self) -> list: ...
