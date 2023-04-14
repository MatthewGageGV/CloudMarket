class TrackList:
    """Creates the wishscreen"""
    def __init__(self):
        self.list = []
        
    def addItem(self, item):
        self.list.append(item)

    def getItem(self, value):
        return self.list[value]
    
    def getLength(self):
        return len(self.list)
    
    def removeItem(self, value):
        del self.list[value]

