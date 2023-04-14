import uuid

class Item:
    """Creates the item object"""
    def __init__(self, name, temp_time, price, buy_price):
        self.id = str(uuid.uuid4())
        self.name = name
        self.time = temp_time
        self.price = price
        self.buy_price = buy_price
        self.wishlist = False
        self.track = False

    def addToWishlist(self):
        self.wishlist = True

    def removeFromWishlist(self):
        self.wishlist = False