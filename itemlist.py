from item import Item

class ItemList:
    """Creates the wishscreen"""
    def __init__(self):
        self.list = []
        self.addItem(Item("Shoes", 1800, 25.00, 50.00))
        self.addItem(Item("Phone", 3600, 500.00, 750.00))
        self.addItem(Item("TV", 10, 600.00, 800.00))
        self.addItem(Item("Shirt", 900, 15.00, 35.00))
        self.addItem(Item("Laptop", 2700, 300.00, 400.00))
        
    def addItem(self, item):
        self.list.append(item)

    def getItem(self, value):
        return self.list[value]
    
    def getItemByID(self, pid):
        for i in range(len(self.list)):
            if(self.list[i].id == pid):
                return self.list[i]
        return
    
    def getLength(self):
        return len(self.list)
    
    def removeItem(self, value):
        del self.list[value]

    def getItemPrice(self,value):
        return "${:.2f}".format(self.list[value].price)