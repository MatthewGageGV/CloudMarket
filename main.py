"""Runs the CloudMarket application"""
from datetime import datetime, timedelta, time
from decimal import Decimal
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.uix.label import Label

class User:
    """Creates the user object"""
    def __init__(self, temp_id, temp_name, balance):
        self.user_id = temp_id
        self.name = temp_name
        self.balance = balance


class Bid:
    """Creates the bid object"""
    def __init__(self, temp_item_id, temp_user_id, temp_bid_value):
        self.item_id = temp_item_id
        self.user_id = temp_user_id
        self.bid_value = temp_bid_value


class Popups(FloatLayout):
    """Creates the bid popup window"""


class ErrorPopup(FloatLayout):
    """Creates the error popup window"""


class Item:
    """Creates the item object"""
    def __init__(self, name, temp_time, price, buy_price):
        self.name = name
        self.time = temp_time
        self.price = price
        self.buy_price = buy_price


class HomeScreen(Screen):
    """Creates the homescreen"""
    counter = 1


class BuyScreen(Screen):
    """Creates the buyscreen"""
    balance = 1000.00

    def balance_to_string(self):
        """converts balance to dollar format"""
        return "${:.2f}".format(self.balance)


class SellScreen(Screen):
    """Creates the sellscreen"""


class ImageButton(ButtonBehavior, Image):
    """Creates an ImageButton"""


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



class CloudMarket(App):
    """contains all the methods of the app"""
    curr_item = -1
    curr_popup = None
    error_popup = None
    error_message = None
    balance = 1000.00
    default_user = User(1, "John Doe", balance)

    def build(self):
        Window.size = (1000, 575)
        Clock.schedule_interval(self.update, 1)
        self.icon = "imgs/WindowIcon.png"
        return GUI

    def change_screen(self, screen_name):
        """changes the active screen"""
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

    def on_start(self):
        self.root.ids.sell_screen.ids.dropdown.dismiss()
        # name, time, price, buy_price
        item_ids = self.root.ids.buy_screen.ids
        for i in range(len(items)):
            item = getattr(item_ids, "item_name_" + str(i + 1))
            item.text = items[i].name
            temp_time = items[i].time
            temp = datetime.min + timedelta(minutes=temp_time)
            timer = time(temp.hour, temp.minute)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "item_time_" + str(i + 1))
            item.text = str(timer)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "item_price_" + str(i + 1))
            item.text = "${:.2f}".format(items[i].price)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "item_buy_" + str(i + 1))
            item.text = "${:.2f}".format(items[i].buy_price)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "bid_button_" + str(i + 1))
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "buy_button_" + str(i + 1))
            item.disabled = False
            item.opacity = 1
        for i in range(len(items), 9):
            item = getattr(item_ids, "item_name_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "item_time_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "item_price_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "item_buy_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "bid_button_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "buy_button_" + str(i + 1))
            item.opacity = 0
            item.disabled = True

    # Tasks performed once per second
    def update(self, dt):
        """tasks which are executed every second"""
        item_ids = self.root.ids.buy_screen.ids
        for i in range(len(items)):
            item = getattr(item_ids, "item_name_" + str(i + 1))
            item.text = items[i].name
            item.opacity = 1
            item.disabled = False
            item = getattr(item_ids, "item_price_" + str(i + 1))
            item.text = "${:.2f}".format(items[i].price)
            item.opacity = 1
            item.disabled = False
            item = getattr(item_ids, "item_buy_" + str(i + 1))
            item.text = "${:.2f}".format(items[i].buy_price)
            item.opacity = 1
            item.disabled = False
            item = getattr(item_ids, "item_time_" + str(i + 1))
            item.opacity = 1
            item.disabled = False
            item = getattr(item_ids, "bid_button_" + str(i + 1))
            item.opacity = 1
            item.disabled = False
            item = getattr(item_ids, "buy_button_" + str(i + 1))
            item.opacity = 1
            item.disabled = False
        for i in range(len(items), 9):
            item = getattr(item_ids, "item_name_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "item_time_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "item_price_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "item_buy_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "bid_button_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
            item = getattr(item_ids, "buy_button_" + str(i + 1))
            item.opacity = 0
            item.disabled = True
        for i in range(len(items) - 1, -1, -1):
            seconds = items[i].time
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            timer_seconds = seconds % 60
            timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
            item = getattr(item_ids, "item_time_" + str(i + 1))
            item.text = timer
            items[i].time = items[i].time - 1
            if items[i].time <= -1:
                del items[i]

    def show_popup(self, item_num):
        """shows the popup"""
        self.curr_item = item_num
        show = Popups()
        popup_window = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                            background="imgs/PopupBackground.png",
                            size_hint=(.3, .3))
        popup_window.overlay_color = (0, 0, 0, .3)
        popup_window.open()
        self.curr_popup = popup_window

    def submit_bid(self, bid_value):
        """submits the bid"""
        if not self.check_string(str(bid_value), "price"):
            return
        # Reject bid if user cannot afford
        can_buy = self.check_balance_bid(bid_value)
        if can_buy:
            bid_value = Decimal(bid_value)
            if bid_value > items[self.curr_item].price:
                items[self.curr_item].price = bid_value
                self.balance = float(self.balance) - float(bid_value)
                self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.balance)
                self.curr_popup.dismiss()
                self.buyscreen_notif("Bid submitted!")
            else:
                self.error_message = "Bid must be higher than current bid!"
                show = ErrorPopup()
                error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                    background="imgs/PopupBackground.png",
                                    size_hint=(.3, .3))
                error_popup.overlay_color = (0, 0, 0, 0)
                error_popup.open()
                self.error_popup = error_popup

    def check_balance(self, bid_value):
        """checks the users balance"""
        if self.balance < Decimal(bid_value):
            self.buyscreen_notif("Not enough funds in account!")
            return False
        return True

    def check_balance_bid(self, bid_value):
        """checks the users balance for bids"""
        if self.balance < Decimal(bid_value):
            self.error_message = "Not enough funds in account!"
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(.3, .3))
            error_popup.overlay_color = (0, 0, 0, 0)
            error_popup.open()
            self.error_popup = error_popup
            return False
        return True

    def submit_item(self, name, ptime, min_bid, buy_price):
        """submits item to item list"""
        if (self.check_string(name, "name") and self.check_string(ptime, "time")
                and self.check_string(min_bid, "price")
                and self.check_string(buy_price, "price")):
            ptime = int(ptime)
            min_bid = Decimal(min_bid)
            buy_price = Decimal(buy_price)
            if len(items) >= 9:
                self.sellscreen_notif("List is currently full")
                return
            if min_bid > buy_price:
                self.error_message = "Starting bid must be less than buy price."
                show = ErrorPopup()
                error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                    background="imgs/PopupBackground.png",
                                    size_hint=(.3, .3))
                error_popup.overlay_color = (0, 0, 0, .4)
                error_popup.open()
                self.error_popup = error_popup
            else:
                new_item = Item(name, ptime, min_bid, buy_price)
                items.append(new_item)
                self.sellscreen_notif("Item Successfully submitted!")

    def check_string(self, string, data_type):
        """checks if the string is correctly formatted"""
        if data_type == "name":
            if not string.replace(" ", "").isalpha():
                self.error_message = "Name cannot contain special\n     characters or numbers"
                show = ErrorPopup()
                error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                    background="imgs/PopupBackground.png",
                                    size_hint=(.3, .3))
                error_popup.overlay_color = (0, 0, 0, .4)
                error_popup.open()
                self.error_popup = error_popup
                return False
            return True
        if data_type == "time":
            if not string.isdigit():
                self.error_message = "Time is represented by integers"
                show = ErrorPopup()
                error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                    background="imgs/PopupBackground.png",
                                    size_hint=(.3, .3))
                error_popup.overlay_color = (0, 0, 0, .4)
                error_popup.open()
                self.error_popup = error_popup
                return False
            return True
        if data_type == "price":
            if not string.isdigit():
                try:
                    float(string)
                except:
                    self.error_message = "Prices cannot contain anything" \
                                         "\n         other than numbers"
                    show = ErrorPopup()
                    error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                        background="imgs/PopupBackground.png",
                                        size_hint=(.3, .3))
                    error_popup.overlay_color = (0, 0, 0, .4)
                    error_popup.open()
                    self.error_popup = error_popup
                    return False
        return True

    def buy_item(self, item_num):
        """Check if the user can buy items"""
        can_buy = self.check_balance(items[item_num].buy_price)
        # If they can buy
        if can_buy:
            self.balance = float(self.balance) - float(items[item_num].buy_price)
            BuyScreen.balance = self.balance
            self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.balance)
            self.buyscreen_notif("Bought " + items[item_num].name + "!")
            del items[item_num]

    def buyscreen_notif(self, text):
        """Displays notification on buyscreen"""
        label = Label(text=text, font_size='20sp', color=(1, 1, 1, 1))
        label.size_hint = (1, .15)
        animation = Animation(color=(1, 1, 1, 0), duration=3)
        animation.start(label)
        self.root.ids.buy_screen.add_widget(label)
        return label

    def sellscreen_notif(self, text):
        """Displays notification on sellscreen"""
        label = Label(text=text, font_size='20sp', color=(1, 1, 1, 1))
        label.size_hint = (1, .3)
        animation = Animation(color=(1, 1, 1, 0), duration=3)
        animation.start(label)
        self.root.ids.sell_screen.add_widget(label)
        return label

    def close_error(self):
        """closes the error popup"""
        self.error_popup.dismiss()

    def get_money(self, value):
        """handles the get money button"""
        self.balance += float(value)
        self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.balance)

    def get_price(self):
        """returns current items price as dollar format"""
        return "${:.2f}".format(items[self.curr_item].price)

    def get_error(self):
        """gets the current errorm message"""
        return self.error_message


# -MAIN--------------------------------------------------------------------------------------------
CloudMarket().run()