"""test class for CloudMarket"""

import unittest
from user import User
from item import Item
from itemlist import ItemList
from model import Model
from errorpopup import ErrorPopup
from popups import Popups
from check import Check
from buyscreen import BuyScreen
from homescreen import HomeScreen
from imagebutton import ImageButton
from sellscreen import SellScreen
from view import View

class testItem(unittest.TestCase): 
    def testItem(self):
        """tests for item class"""
        temp = Item("Test Item", 500, 100.00, 150.00)
        self.assertEqual(temp.name, "Test Item")
        self.assertEqual(temp.time, 500)
        self.assertEqual(temp.price, 100.00)
        self.assertEqual(temp.buy_price, 150.00)
        self.assertEqual(temp.wishlist, False)
        self.assertEqual(temp.track, False)

class testWishlist(unittest.TestCase):
    """tests for wishlist functionality"""
    def testWishList(self):
        """tests for wishlist functionality"""
        temp = Item("Test Item", 500, 100.00, 150.00)
        temp.addToWishlist()
        self.assertEqual(temp.wishlist, True)
        temp.removeFromWishlist()
        self.assertEqual(temp.wishlist, False)

class testUser(unittest.TestCase):
    """tests for user object"""
    def testUser(self):
        """tests for wishlist functionality"""
        temp = User(1000)
        self.assertEqual(temp.getBalance(), 1000)

class testItemList(unittest.TestCase):
    """tests for itemlist object"""
    def testItemList(self):
        """tests for wishlist functionality"""
        temp = ItemList()
        result = temp.getItem(0).name
        self.assertEqual(result, "Shoes")
        result = temp.getItem(0).time
        self.assertEqual(result, 1800)
        result = temp.getItem(0).price
        self.assertEqual(result, 25.00)
        result = temp.getItem(0).buy_price
        self.assertEqual(result, 50.00)
        result = temp.getItem(0).wishlist
        self.assertEqual(result, False)
        result = temp.getItem(0).track
        self.assertEqual(result, False)

class testGetItemByID(unittest.TestCase):
    """tests for getitembyid method"""
    def testGetItemByID(self):
        """tests for wishlist functionality"""
        temp = ItemList()
        tempItem = Item("Test", 1000, 20.00, 30.00)
        temp.addItem(tempItem)
        self.assertEqual(tempItem.id, temp.getItemByID(tempItem.id).id)
        self.assertEqual(temp.getItemByID("awpoeijf"), None)

class testRemoveItem(unittest.TestCase):
    """tests for removing item from itemlist"""
    def testRemoveItem(self):
        """tests for wishlist functionality"""
        model = Model()
        temp = model.itemlist
        tempItem = temp.getItem(2)
        temp.removeItem(2)
        self.assertNotIn(tempItem, temp.list)

class testGetItemPrice(unittest.TestCase):
    """tests for removing item from itemlist"""
    def testGetItemPrice(self):
        """tests for wishlist functionality"""
        temp = ItemList()
        self.assertEqual(temp.getItemPrice(0), "$25.00")

class testItemListLength(unittest.TestCase):
    """tests for item list length"""
    def testItemListLength(self):
        """tests for wishlist functionality"""
        temp = ItemList()
        self.assertEqual(temp.getLength(), 5)

class testFormatBalance(unittest.TestCase):
    """tests for balance formtating"""
    def testFormatBalance(self):
        """tests for wishlist functionality"""
        temp = User(3000)
        temp = temp.formatBalance()
        self.assertEqual(temp, "$3000.00")

class testSetBalance(unittest.TestCase):
    """tests for balance setting"""
    def testSetBalance(self):
        """tests for wishlist functionality"""
        temp = User(1000)
        temp.setBalance(500)
        result= temp.getBalance()
        self.assertEqual(result, 500)

class testCheckBalance(unittest.TestCase):
    """tests for check balance"""
    def testCheckString(self):
        """tests for wishlist functionality"""
        result = Check.check_string("Test", "name")
        self.assertEqual(result, 0)
        result = Check.check_string("Test1", "name")
        self.assertEqual(result, 1)
        result = Check.check_string("200", "time")
        self.assertEqual(result, 0)
        result = Check.check_string("200f", "time")
        self.assertEqual(result, 2)
        result = Check.check_string("200.00", "price")
        self.assertEqual(result, 0)
        result = Check.check_string("200f", "price")
        self.assertEqual(result, 3)

class testCheckString(unittest.TestCase):
    """tests for check string"""
    def testCheckString(self):
        """tests for wishlist functionality"""
        self.assertEqual(Check.check_string("Test", "name"), 0)
        self.assertEqual(Check.check_string("Test1", "name"), 1)
        self.assertEqual(Check.check_string("200", "time"), 0)
        self.assertEqual(Check.check_string("200f", "time"), 2)
        self.assertEqual(Check.check_string("200.00", "price"), 0)
        self.assertEqual(Check.check_string("200f", "price"), 3)
        self.assertEqual(Check.check_string("200", "price"), 0)
        self.assertEqual(Check.check_string("200", "prices"), 0)

class testCheckBalance2(unittest.TestCase):
    """tests for check balance"""
    def testCheckBalance2(self):
        """tests for wishlist functionality"""
        self.assertEqual(Check.check_balance(100.00, 150.00), False)
        self.assertEqual(Check.check_balance(150.00, 100.00), True)

class testCheckPrice(unittest.TestCase):
    """tests for check price"""
    def testCheckPrice(self):
        """tests for wishlist functionality"""
        self.assertEqual(Check.checkPrice(150.00, 100.00), False)
        self.assertEqual(Check.checkPrice(100.00, 150.00), True)

class testBuyItem(unittest.TestCase):
    """tests for buying items"""
    def testBuyItem(self):
        """tests for wishlist functionality"""
        user = User(1000)
        itemlist = ItemList()
        result = Check.buyItem(0, user, itemlist)
        self.assertEqual(result, True)
        user.setBalance(0)
        result = Check.buyItem(0, user, itemlist)
        self.assertEqual(result, False)

class testCheckTime(unittest.TestCase):
    """tests for check time"""
    def testCheckTime(self):
        """tests for wishlist functionality"""
        itemlist = ItemList()
        item = Item("test", -1, 100.00, 115.00)
        itemlist.addItem(item)
        Check.checkTime(itemlist)
        self.assertNotIn(item, itemlist.list)

class testView(unittest.TestCase):
    """tests for view class"""
    def testView(self):
        """tests for wishlist functionality"""
        model = Model()
        view = View(model)
        view.run()
        model.itemlist.getItem(0).track = True
        model.itemlist.getItem(0).addToWishlist()
        view.curr_item = 0
        view.change_screen('buy_screen')
        current = view.root.ids['screen_manager'].current
        self.assertEqual('buy_screen', current)
        view.change_screen('sell_screen')
        current = view.root.ids['screen_manager'].current
        self.assertEqual('sell_screen', current)
        view.change_screen('home_screen')
        current = view.root.ids['screen_manager'].current
        self.assertEqual('home_screen', current)
        view.change_screen('sell_screen')
        current = view.root.ids['screen_manager'].current
        self.assertEqual('sell_screen', current)
        view.change_screen('home_screen')
        view.switchlist("tracklist")
        self.assertEqual(view.tracklist_active, True)
        self.assertEqual(view.wishlist_active, False)
        self.assertEqual(view.switchlist("wronginput"), None)
        view.update(0)
        view.switchlist("wishlist")
        self.assertEqual(view.wishlist_active, True)
        self.assertEqual(view.tracklist_active, False)
        view.update(0)
        view.wishlist_item(3)
        result = view.model.itemlist.getItem(3).wishlist
        self.assertEqual(result, True)
        view.wishlist_item(0)
        view.buy_item(0)
        view.model.itemlist.addItem(Item("Temp", 1000, 3000, 6000))
        view.buy_item(4)
        result = view.model.itemlist.getLength()
        self.assertEqual(result, 5)
        view.switchlist("buylist")
        self.assertEqual(view.wishlist_active, False)
        view.error_message = 'Bid must be higher than current bid!'
        self.assertEqual(view.tracklist_active, False)
        result = view.model.default_user.getBalance()
        view.get_money(1000)
        self.assertEqual(view.model.default_user.getBalance(), result+1000)
        result = view.get_price()
        self.assertEqual(result, '$500.00')
        error = view.get_error()
        self.assertEqual(error, 'Bid must be higher than current bid!')


if __name__ == '__main__':
    unittest.main()
