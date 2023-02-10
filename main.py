from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.core.window import Window
import datetime


# User Object Class
class User:
    def __init__(self, tempID, tempName):
        self.ID = tempID
        self.name = tempName


# Bid Object Class
class Bid:
    def __init__(self, itemID, userID, bidValue):
        self.itemId = itemID
        self.userId = userID
        self.bidValue = bidValue


# Item Object Class
class Item:
    def __init__(self, itemID, name, image, desc, sellerID, endDate):
        self.itemID = itemID
        self.name = name
        self.image = image
        self.desc = desc
        self.sellerID = sellerID
        self.endDate = endDate


# Class for the home screen
class HomeScreen(Screen):
    counter = 1
    pass


# Class for the buy screen
class BuyScreen(Screen):
    pass


# Class for the Sell screen
class SellScreen(Screen):
    pass


# Class for buttons with an image icon
class ImageButton(ButtonBehavior, Image):
    pass


GUI = Builder.load_file("main.kv")


# Class of the application
class CloudMarket(App):
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

    # Tasks performed once per second
    def update(self, dt):
        current_time = datetime.datetime.now()
        end_date_string = "2023-02-04 12:00:00"
        end_date = datetime.datetime.strptime(end_date_string, "%Y-%m-%d %H:%M:%S")
        time_remaining = end_date - current_time
        total_seconds = time_remaining.total_seconds()
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = "{:.0f}:{:.0f}:{:.0f}:{:02.0f}".format(days, hours, minutes, seconds)
        HomeScreen.counter = "Time Remaining: " + time_string
#       self.root.ids.home_screen.ids.title_label.text = str(HomeScreen.counter)


# -MAIN---------------------------------------------------------------------------------------------------
CloudMarket().run()
