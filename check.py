from decimal import Decimal

class Check:
    def check_balance(balance, bid_value):
        if balance < Decimal(bid_value):
            return False
        return True
    
    #returns 0 if the input is valid, 1 if it is not a valid name, 2 if it is not a valid time, and 3 if it is not a valid price
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
    
    #checks if minimum bid is higher than the buy price
    def checkPrice(min_bid, buy_price):
        if min_bid > buy_price:
            return False
        return True
        
    def buyItem(item_num, user, itemlist):
        can_buy = Check.check_balance(user.getBalance(), itemlist.getItem(item_num).buy_price)
        if can_buy:
            user.setBalance(float(user.getBalance()) - float(itemlist.getItem(item_num).buy_price))
            itemlist.removeItem(item_num)
            return True
        else:
            return False

    def checkTime(itemlist):
        for i in range(itemlist.getLength() - 1, -1, -1):
            # seconds = itemlist.getItem(i).time
            itemlist.getItem(i).time = itemlist.getItem(i).time - 1
            if itemlist.getItem(i).time <= -1:
                itemlist.removeItem(i)