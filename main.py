from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime, timedelta, time
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from decimal import Decimal
from kivy.animation import Animation
from kivy.uix.label import Label


# User Object Class
class User:
    def __init__(self, tempID, tempName, balance):
        self.ID = tempID
        self.name = tempName
        self.balance = balance


# Bid Object Class
class Bid:
    def __init__(self, itemID, userID, bidValue):
        self.itemId = itemID
        self.userId = userID
        self.bidValue = bidValue

# Popup Window Class
class Popups(FloatLayout):
    pass

# Item Object Class
class Item:
    def __init__(self, name, time, price, buy_price):
        self.name = name
        self.time = time
        self.price = price
        self.buy_price = buy_price


# Class for the home screen
class HomeScreen(Screen):
    counter = 1
    pass


# Class for the buy screen
class BuyScreen(Screen):
    balance = 1000.00
    def balance_to_string(self):
        return "${:.2f}".format(self.balance)
    pass


# Class for the Sell screen
class SellScreen(Screen):
    pass


# Class for buttons with an image icon
class ImageButton(ButtonBehavior, Image):
    pass


GUI = Builder.load_file("main.kv")
items = []
item1 = Item("Shoes", 1800, 25.00, 50.00)
item2 = Item("Phone", 3600, 500.00, 750.00)
item3 = Item("TV", 10, 600.00, 800.00)
item4 = Item("Laptop", 2700, 300.00, 400.00)
item5 = Item("Shirt", 900, 15.00, 35.00)
items.append(item1)
items.append(item2)
items.append(item3)
items.append(item4)
items.append(item5)

# Class of the application
class CloudMarket(App):
    curr_item = -1
    balance = 1000.00
    default_user = User(1, "John Doe", balance);

    # Builds the UI
    def build(self):
        Window.size = (1000, 575)
        Clock.schedule_interval(self.update, 1)
        return GUI

    # Changes the screen to the entered screen id
    def change_screen(self, screen_name):
        curr = None
        next_screen = None
        screen_manager = self.root.ids['screen_manager']
        if screen_manager.current == 'home_screen':
            curr = 1
        elif screen_manager.current == 'buy_screen':
            curr = 2
        elif screen_manager.current == 'sell_screen':
            curr = 3
        if screen_name == 'home_screen':
            next_screen = 1
        elif screen_name == 'buy_screen':
            next_screen = 2
        elif screen_name == 'sell_screen':
            next_screen = 3
        if next_screen > curr:
            screen_manager.transition.direction = 'left'
        else:
            screen_manager.transition.direction = 'right'
        screen_manager.current = screen_name

    # Tasks performed once when the app is launched
    def on_start(self):
        self.root.ids.sell_screen.ids.dropdown.dismiss()
        # name, time, price, buy_price
        item_ids = self.root.ids.buy_screen.ids
        for i in range(len(items)):
            item = getattr(item_ids, "item_name_" + str(i+1))
            item.text = items[i].name
            temp_time = items[i].time
            temp = datetime.min + timedelta(minutes=temp_time)
            t = time(temp.hour, temp.minute)
            item.opacity = 1
            item = getattr(item_ids, "item_time_" + str(i+1))
            item.text = str(t)
            item.opacity = 1
            item = getattr(item_ids, "item_price_" + str(i+1))
            item.text = "${:.2f}".format(items[i].price)
            item.opacity = 1
            item = getattr(item_ids, "item_buy_" + str(i+1))
            item.text = "${:.2f}".format(items[i].buy_price)
            item.opacity = 1
            item = getattr(item_ids, "bid_button_" + str(i+1))
            item.opacity = 1
            item = getattr(item_ids, "buy_button_" + str(i+1))
            item.opacity = 1
        for i in range(len(items), 9):
            item = getattr(item_ids, "item_name_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "item_time_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "item_price_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "item_buy_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "bid_button_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "buy_button_" + str(i+1))
            item.opacity = 0

    # Tasks performed once per second
    def update(self, dt):
        item_ids = self.root.ids.buy_screen.ids
        for i in range(len(items)):
            item = getattr(item_ids, "item_name_" + str(i+1))
            item.text = items[i].name
            item.opacity = 1
            item = getattr(item_ids, "item_price_" + str(i+1))
            item.text = "${:.2f}".format(items[i].price)
            item.opacity = 1
            item = getattr(item_ids, "item_buy_" + str(i+1))
            item.text = "${:.2f}".format(items[i].buy_price)
            item.opacity = 1
            item = getattr(item_ids, "item_time_" + str(i+1))
            item.opacity = 1
            item = getattr(item_ids, "bid_button_" + str(i+1))
            item.opacity = 1
            item = getattr(item_ids, "buy_button_" + str(i+1))
            item.opacity = 1

        for i in range(len(items), 9):
            item = getattr(item_ids, "item_name_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "item_time_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "item_price_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "item_buy_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "bid_button_" + str(i+1))
            item.opacity = 0
            item = getattr(item_ids, "buy_button_" + str(i+1))
            item.opacity = 0
        for i in range(len(items)-1, -1, -1):
            seconds = items[i].time
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            timer_seconds = seconds % 60
            t = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
            item = getattr(item_ids, "item_time_" + str(i+1))
            item.text = t
            items[i].time = items[i].time - 1
            if items[i].time <= -1:
                del items[i]

    def show_popup(self, item_num):
        show = Popups()
        self.curr_item = item_num
        popupWindow = Popup(title="Bid Window", content=show, size_hint=(None, None), size=(300, 170))
        popupWindow.open()


    def submit_bid(self, bid_value):
        if not self.check_string(str(bid_value), "price"):
            return
        # Reject bid if user cannot afford
        can_buy = self.check_balance_bid(bid_value)
        if (can_buy):
            bid_value = Decimal(bid_value)
            if (bid_value > items[self.curr_item].price):
                items[self.curr_item].price = bid_value
                self.balance = float(self.balance) - float(bid_value)
                self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.balance)
            else:
                errorWindow = Popup(title="Bid must be higher than pre-existing bid!", size_hint=(None, None), size=(300, 170))
                errorWindow.open()

    def check_balance(self, bid_value):
        if self.balance < Decimal(bid_value):
            self.buyscreen_notif("Not enough funds in account!")
            return False
        else:
            return True

    def check_balance_bid(self, bid_value):
        if self.balance < Decimal(bid_value):
            errorWindow = Popup(title="Not enough funds in account!", size_hint=(None, None), size=(300, 170))
            errorWindow.open()
            return False
        else:
            return True

    def submit_item(self, name, ptime, min_bid, buy_price):
        if (self.check_string(name, "name") and self.check_string(ptime, "time") and self.check_string(min_bid, "price")
        and self.check_string(buy_price, "price")):
            ptime = int(ptime)
            min_bid = Decimal(min_bid)
            buy_price = Decimal(buy_price)
            if (min_bid > buy_price):
                errorWindow = Popup(title="Starting bid must be less than buy price.", size_hint=(None, None),
                                    size=(300, 170))
                errorWindow.open()
            else:
                print(ptime)
                new_item = Item(name, ptime, min_bid, buy_price)
                items.append(new_item)
                for i in range(len(items)):
                    print(items[i].name)
                    self.sellscreen_notif("Item Successfully submitted!")

    def check_string(self, string, type):
        if (type == "name"):
            if (not string.isalpha()):
                errorWindow = Popup(title="Name cannot contain special characters or numbers", size_hint=(None, None),
                                    size=(300, 170))
                errorWindow.open()
                return False
            else:
                return True
        if (type == "time"):
            if (not string.isdigit()):
                errorWindow = Popup(title="Time is represented by integers", size_hint=(None, None),
                                    size=(300, 170))
                errorWindow.open()
                return False
            else:
                return True
        if (type == "price"):
            if (not string.isdigit()):
                try:
                    float(string)
                except:
                    errorWindow = Popup(title="Prices cannot contain anything other than numbers", size_hint=(None, None),
                                        size=(300, 170))
                    errorWindow.open()
                    return False
        return True

    def buy_item(self, item_num):
        # Check if the user can buy items
        can_buy = self.check_balance(items[item_num].buy_price)
        # If they can buy
        if (can_buy):
            self.balance = float(self.balance) - float(items[item_num].buy_price)
            BuyScreen.balance = self.balance
            self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.balance)
            self.buyscreen_notif("Bought " + items[item_num].name + "!")
            del items[item_num]

    def buyscreen_notif(self, text):
        label = Label(text=text, font_size='20sp', color=(1, 1, 1, 1))
        label.size_hint = (1, .15)
        animation = Animation(color=(1, 1, 1, 0), duration=3)
        animation.start(label)
        self.root.ids.buy_screen.add_widget(label)
        return label

    def sellscreen_notif(self, text):
        label = Label(text=text, font_size='20sp', color=(1, 1, 1, 1))
        label.size_hint = (1, .3)
        animation = Animation(color=(1, 1, 1, 0), duration=3)
        animation.start(label)
        self.root.ids.sell_screen.add_widget(label)
        return label

    def get_money(self, value):
        self.balance += float(value)
        self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.balance)
        return


# -MAIN---------------------------------------------------------------------------------------------------
CloudMarket().run()