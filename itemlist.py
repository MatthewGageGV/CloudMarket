"""this class represents the list of items"""
from item import Item

class ItemList:
    """this class represents the list of items"""
    def __init__(self):
        self.list = []
        self.addItem(Item("Shoes", 1800, 25.00, 50.00))
        self.addItem(Item("Phone", 3600, 500.00, 750.00))
        self.addItem(Item("TV", 10, 600.00, 800.00))
        self.addItem(Item("Shirt", 900, 15.00, 35.00))
        self.addItem(Item("Laptop", 2700, 300.00, 400.00))

    def addItem(self, item):
        """adds the entered item to the list"""
        self.list.append(item)

    def getItem(self, value):
        """gets an item from the list by index"""
        return self.list[value]

    def getItemByID(self, pid):
        """gets an item from the list by the item id"""
        for i in range(len(self.list)):
            if self.list[i].id == pid:
                return self.list[i]
        return None

    def getLength(self):
        """returns the length of the list"""
        return len(self.list)

    def removeItem(self, value):
        """removes an item from the list by index value"""
        del self.list[value]

    def getItemPrice(self,value):
        """gets the price of the item by index value"""
        return f"${self.list[value].price:.2f}"
