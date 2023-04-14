class User:
    """Creates the user object"""
    def __init__(self, balance):
        self.balance = balance

    def getBalance(self):
        return self.balance
    
    def setBalance(self, newBalance):
        self.balance = newBalance

    def formatBalance(self):
        return "${:.2f}".format(self.balance)