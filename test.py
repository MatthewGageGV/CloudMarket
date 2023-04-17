import unittest
from user import User
from item import Item
from check import Check
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
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.label import Label
import main

class testUser(unittest.TestCase):
    def testUser(self):
        temp = User(1000)
        self.assertEqual(temp.getBalance(), 1000)

class testItem(unittest.TestCase):
    def testItem(self):
        temp = Item("Test Item", 500, 100.00, 150.00)
        self.assertEqual(temp.name, "Test Item")
        self.assertEqual(temp.time, 500)
        self.assertEqual(temp.price, 100.00)
        self.assertEqual(temp.buy_price, 150.00)
        self.assertEqual(temp.wishlist, False)
        self.assertEqual(temp.track, False)

class testWishlist(unittest.TestCase):
    def testWishList(self):
        temp = Item("Test Item", 500, 100.00, 150.00)
        temp.addToWishlist()
        self.assertEqual(temp.wishlist, True)
        temp.removeFromWishlist()
        self.assertEqual(temp.wishlist, False)

class testItemList(unittest.TestCase):
    def testItemList(self):
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
    def testGetItemByID(self):
        temp = ItemList()
        tempItem = Item("Test", 1000, 20.00, 30.00)
        temp.addItem(tempItem)
        self.assertEqual(tempItem.id, temp.getItemByID(tempItem.id).id)
        self.assertEqual(temp.getItemByID("awpoeijf"), None)

class testRemoveItem(unittest.TestCase):
    def testRemoveItem(self):
        model = Model()
        temp = model.itemlist
        tempItem = temp.getItem(2)
        temp.removeItem(2)
        self.assertNotIn(tempItem, temp.list)

class testGetItemPrice(unittest.TestCase):
    def testGetItemPrice(self):
        temp = ItemList()
        self.assertEquals(temp.getItemPrice(0), "$25.00")

class testItemListLength(unittest.TestCase):
    def testItemListLength(self):
        temp = ItemList()
        self.assertEqual(temp.getLength(), 5)

class testFormatBalance(unittest.TestCase):
    def testFormatBalance(self):
        temp = User(3000)
        temp = temp.formatBalance()
        self.assertEqual(temp, "$3000.00")

class testSetBalance(unittest.TestCase):
    def testSetBalance(self):
        temp = User(1000)
        temp.setBalance(500)
        result= temp.getBalance()
        self.assertEqual(result, 500)

class testCheckBalance(unittest.TestCase):
    def testCheckString(self):
        self.assertEquals(Check.check_string("Test", "name"), 0)
        self.assertEquals(Check.check_string("Test1", "name"), 1)
        self.assertEquals(Check.check_string("200", "time"), 0)
        self.assertEquals(Check.check_string("200f", "time"), 2)
        self.assertEquals(Check.check_string("200.00", "price"), 0)
        self.assertEquals(Check.check_string("200f", "price"), 3)

class testCheckString(unittest.TestCase):
    def testCheckString(self):
        self.assertEquals(Check.check_string("Test", "name"), 0)
        self.assertEquals(Check.check_string("Test1", "name"), 1)
        self.assertEquals(Check.check_string("200", "time"), 0)
        self.assertEquals(Check.check_string("200f", "time"), 2)
        self.assertEquals(Check.check_string("200.00", "price"), 0)
        self.assertEquals(Check.check_string("200f", "price"), 3)
        self.assertEquals(Check.check_string("200", "price"), 0)
        self.assertEquals(Check.check_string("200", "prices"), 0)

class testCheckBalance(unittest.TestCase):
    def testCheckBalance(self):
        self.assertEquals(Check.check_balance(100.00, 150.00), False)
        self.assertEquals(Check.check_balance(150.00, 100.00), True)

class testCheckPrice(unittest.TestCase):
    def testCheckPrice(self):
        self.assertEquals(Check.checkPrice(150.00, 100.00), False)
        self.assertEquals(Check.checkPrice(100.00, 150.00), True)

class testBuyItem(unittest.TestCase):
    def testBuyItem(self):
        user = User(1000)
        itemlist = ItemList()
        self.assertEquals(Check.buyItem(0, user, itemlist), True)
        user.setBalance(0)
        self.assertEquals(Check.buyItem(0, user, itemlist), False)

class testCheckTime(unittest.TestCase):
    def testCheckTime(self):
        itemlist = ItemList()
        item = Item("test", -1, 100.00, 115.00)
        itemlist.addItem(item)
        Check.checkTime(itemlist)
        self.assertNotIn(item, itemlist.list)

class testView(unittest.TestCase):
    def testView(self):
        model = Model()
        view = View(model)
        view.run()
        model.itemlist.getItem(0).track = True
        model.itemlist.getItem(0).addToWishlist()
        view.curr_item = 0
        view.change_screen('buy_screen')
        current = view.root.ids['screen_manager'].current
        self.assertEquals('buy_screen', current)
        view.change_screen('sell_screen')
        current = view.root.ids['screen_manager'].current
        self.assertEquals('sell_screen', current)
        view.change_screen('home_screen')
        current = view.root.ids['screen_manager'].current
        self.assertEquals('home_screen', current)
        view.switchlist("tracklist")
        self.assertEquals(view.tracklist_active, True)
        self.assertEquals(view.wishlist_active, False)
        view.update(0)
        view.switchlist("wishlist")
        self.assertEquals(view.wishlist_active, True)
        self.assertEquals(view.tracklist_active, False)
        view.update(0)
        view.show_popup(1)


if __name__ == '__main__':
    unittest.main()