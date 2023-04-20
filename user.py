"""class for representing the user object"""


class User:
    """Creates the user object"""

    def __init__(self, balance):
        self.balance = balance

    def getBalance(self):
        """returns the users balance"""
        return self.balance

    def setBalance(self, newBalance):
        """sets the users balance to the input"""
        self.balance = newBalance

    def formatBalance(self):
        """formats teh balance into a dollar format"""
        return f"${self.balance:.2f}"
