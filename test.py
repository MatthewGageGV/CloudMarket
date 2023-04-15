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


if __name__ == '__main__':
    unittest.main()