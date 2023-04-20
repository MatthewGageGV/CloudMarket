"""contains functions which determine valid or invalid inputs"""

from decimal import Decimal

class Check:
    """contains functions which determine valid or invalid inputs"""
    def check_balance(balance, bid_value):
        """checks if the user has enough money to bid"""
        if balance < Decimal(bid_value):
            return False
        return True

    def check_string(string, data_type):
        """checks if the string is correctly formatted"""
        if data_type == "name":
            if not string.replace(" ", "").isalpha():
                return 1
            return 0
        elif data_type == "time":
            if not string.isdigit():
                return 2
            return 0
        elif data_type == "price":
            if not string.isdigit():
                try:
                    float(string)
                except:
                    return 3
        return 0

    def checkPrice(min_bid, buy_price):
        """checks if the bid price is greater than the buy price"""
        if min_bid > buy_price:
            return False
        return True

    def buyItem(item_num, user, itemlist):
        """checks if the user can buy the item, then performs the buy if true"""
        can_buy = Check.check_balance(user.getBalance(), itemlist.getItem(item_num).buy_price)
        if can_buy:
            user.setBalance(float(user.getBalance()) - float(itemlist.getItem(item_num).buy_price))
            itemlist.removeItem(item_num)
            return True
        return False

    def checkTime(itemlist):
        """reduces the time of each item in item list"""
        for i in range(itemlist.getLength() - 1, -1, -1):
            itemlist.getItem(i).time = itemlist.getItem(i).time - 1
            if itemlist.getItem(i).time <= -1:
                itemlist.removeItem(i)
