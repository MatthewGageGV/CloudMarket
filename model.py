"""Creates the user object"""
from itemlist import ItemList
from user import User

class Model:
    """Creates the user object"""
    def __init__(self):
        self.itemlist = ItemList()
        self.default_user = User(1000)
