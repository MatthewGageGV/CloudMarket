import unittest
from user import User
from item import Item
from controller import Controller


class UserTest(unittest.TestCase):
    def test_user(self):
        temp = User(1000)
        self.assertEqual(temp.getBalance(), 1000)


class ItemTest(unittest.TestCase):
    def test_user(self):
        temp = Item("Test Item", 500, 100.00, 150.00)
        self.assertEqual(temp.name, "Test Item")
        self.assertEqual(temp.time, 500)
        self.assertEqual(temp.price, 100.00)
        self.assertEqual(temp.buy_price, 150.00)


class test_check_balance(unittest.TestCase):
    def test_check_balance(self):
        result = Controller.check_balance(50.00, 150.00)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()