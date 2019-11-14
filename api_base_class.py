

class APIBaseClass:
    """ Base class which all APIs will inherit from. """
    
    def __init__(self, _id: str, secret=None):
        self.id = _id
        self.secret = secret
