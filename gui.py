from datetime import datetime, timedelta, time
from decimal import Decimal
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.uix.label import Label
from user import User
from item import Item
from buyscreen import BuyScreen
from homescreen import HomeScreen
from imagebutton import ImageButton
from sellscreen import SellScreen
from errorpopup import ErrorPopup
from popups import Popups
from itemlist import ItemList
from check import Check
from model import Model


class CloudMarket(App):
    """manages the gui of the program"""

    def build(self):
        Window.size = (1000, 575)
        Clock.schedule_interval(self.update, 1)
        self.icon = "imgs/WindowIcon.png"
        GUI = Builder.load_file("main.kv")
        return GUI

    def __init__(self, pmodel):
        self.model = pmodel
        self.curr_item = -1
        self.curr_item = -1
        self.curr_popup = None
        self.error_popup = None
        self.error_message = None
        self.tracklist_active = False
        self.wishlist_active = False
        super().__init__()

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
        elif screen_manager.current == 'track_screen':
            curr = 4
        elif screen_manager.current == 'wish_screen':
            curr = 5
        if screen_name == 'home_screen':
            next_screen = 1
        elif screen_name == 'buy_screen':
            next_screen = 2
        elif screen_name == 'sell_screen':
            next_screen = 3
        elif screen_name == 'track_screen':
            next_screen = 4
        elif screen_name == 'wish_screen':
            next_screen = 5
        if next_screen > curr:
            screen_manager.transition.direction = 'left'
        else:
            screen_manager.transition.direction = 'right'
        screen_manager.current = screen_name

    def on_start(self):
        self.root.ids.sell_screen.ids.dropdown.dismiss()
        # name, time, price, buy_price
        item_ids = self.root.ids.buy_screen.ids
        for i in range(self.model.itemlist.getLength()):
            item = getattr(item_ids, "item_name_" + str(i + 1))
            item.text = self.model.itemlist.getItem(i).name
            temp_time = self.model.itemlist.getItem(i).time
            temp = datetime.min + timedelta(minutes=temp_time)
            timer = time(temp.hour, temp.minute)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "item_time_" + str(i + 1))
            item.text = str(timer)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "item_price_" + str(i + 1))
            item.text = "${:.2f}".format(self.model.itemlist.getItem(i).price)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "item_buy_" + str(i + 1))
            item.text = "${:.2f}".format(self.model.itemlist.getItem(i).buy_price)
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "bid_button_" + str(i + 1))
            item.disabled = False
            item.opacity = 1
            item = getattr(item_ids, "buy_button_" + str(i + 1))
            item.disabled = False
            item.opacity = 1
        for i in range(self.model.itemlist.getLength(), 9):
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
        if(self.tracklist_active):
            displaylist = []
            for i in range(self.model.itemlist.getLength()):
                if(self.model.itemlist.getItem(i).track):
                    displaylist.append(self.model.itemlist.getItem(i))
            self.root.ids.buy_screen.ids.bidtracking.opacity = 1
            self.root.ids.buy_screen.ids.wishlisttitle.opacity = 0
            for i in range(len(displaylist)):
                item = getattr(item_ids, "item_name_" + str(i + 1))
                item.text = displaylist[i].name
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_price_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_buy_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].buy_price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "bid_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "buy_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist), 9):
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist) - 1, -1, -1):
                seconds = displaylist[i].time
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                timer_seconds = seconds % 60
                timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.text = timer
        elif(self.wishlist_active):
            displaylist = []
            for i in range(self.model.itemlist.getLength()):
                if(self.model.itemlist.getItem(i).wishlist):
                    displaylist.append(self.model.itemlist.getItem(i))
            self.root.ids.buy_screen.ids.wishlisttitle.opacity = 1
            self.root.ids.buy_screen.ids.bidtracking.opacity = 0
            for i in range(len(displaylist)):
                item = getattr(item_ids, "item_name_" + str(i + 1))
                item.text = displaylist[i].name
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_price_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_buy_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].buy_price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "bid_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "buy_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist), 9):
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist) - 1, -1, -1):
                seconds = displaylist[i].time
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                timer_seconds = seconds % 60
                timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.text = timer
        else:
            self.root.ids.buy_screen.ids.wishlisttitle.opacity = 0
            self.root.ids.buy_screen.ids.bidtracking.opacity = 0
            for i in range(self.model.itemlist.getLength()):
                item = getattr(item_ids, "item_name_" + str(i + 1))
                item.text = self.model.itemlist.getItem(i).name
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_price_" + str(i + 1))
                item.text = "${:.2f}".format(self.model.itemlist.getItem(i).price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_buy_" + str(i + 1))
                item.text = "${:.2f}".format(self.model.itemlist.getItem(i).buy_price)
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 1
                item.disabled = False
            for i in range(self.model.itemlist.getLength(), 9):
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(self.model.itemlist.getLength() - 1, -1, -1):
                seconds = self.model.itemlist.getItem(i).time
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                timer_seconds = seconds % 60
                timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.text = timer
            Check.checkTime(self.model.itemlist)

    def show_popup(self, item_num):
        """shows the popup"""
        self.curr_item = item_num
        show = Popups()
        popup_window = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                            background="imgs/PopupBackground.png",
                            size_hint=(None, None), size=(300, 170))
        popup_window.overlay_color = (0, 0, 0, .3)
        popup_window.open()
        self.curr_popup = popup_window

    def submit_bid(self, bid_value):
        """submits the bid"""
        if Check.check_string(str(bid_value), "price") == 3:
            self.error_message = "Prices cannot contain anything" \
                                    "\n         other than numbers"
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(None, None), size=(300, 170))
            error_popup.overlay_color = (0, 0, 0, .4)
            error_popup.open()
            self.error_popup = error_popup
            return
        can_buy = Check.check_balance(self.model.default_user.getBalance(), bid_value)
        if can_buy:
            bid_value = Decimal(bid_value)
            if bid_value > self.model.itemlist.getItem(self.curr_item).price:
                self.model.itemlist.getItem(self.curr_item).price = bid_value
                self.model.default_user.setBalance(float(self.model.default_user.getBalance()) - float(bid_value))
                self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.model.default_user.getBalance())
                self.curr_popup.dismiss()
                self.buyscreen_notif("Bid submitted!")
                for i in range(0, self.model.itemlist.getLength()):
                    if(self.model.itemlist.getItem(self.curr_item).id == self.model.itemlist.getItem(i).id and self.model.itemlist.getItem(i).track):
                        return
                self.model.itemlist.getItem(self.curr_item).track = True
            else:
                self.error_message = "Bid must be higher than current bid!"
                show = ErrorPopup()
                error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                    background="imgs/PopupBackground.png",
                                    size_hint=(None, None), size=(300, 170))
                error_popup.overlay_color = (0, 0, 0, 0)
                error_popup.open()
                self.error_popup = error_popup
        else:
            self.error_message = "Not enough funds in account!"
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(None, None), size=(300, 170))
            error_popup.overlay_color = (0, 0, 0, 0)
            error_popup.open()
            self.error_popup = error_popup
            return False

    def submit_item(self, name, ptime, min_bid, buy_price):
        """submits item to item list"""
        if Check.check_string(str(name), "name") == 1:
            self.error_message = "Name cannot contain special\n     characters or numbers"
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(None, None), size=(300, 170))
            error_popup.overlay_color = (0, 0, 0, .4)
            error_popup.open()
            self.error_popup = error_popup
            return
        if Check.check_string(str(min_bid), "price") == 3:
            self.error_message = "Prices cannot contain anything" \
                                    "\n         other than numbers"
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(None, None), size=(300, 170))
            error_popup.overlay_color = (0, 0, 0, .4)
            error_popup.open()
            self.error_popup = error_popup
            return
        if Check.check_string(str(buy_price), "price") == 3:
            self.error_message = "Prices cannot contain anything" \
                                    "\n         other than numbers"
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(None, None), size=(300, 170))
            error_popup.overlay_color = (0, 0, 0, .4)
            error_popup.open()
            self.error_popup = error_popup
            return
        if Check.check_string(str(ptime), "time") == 2:
            self.error_message = "Time is represented by\n      positive integers"
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(None, None), size=(300, 170))
            error_popup.overlay_color = (0, 0, 0, .4)
            error_popup.open()
            self.error_popup = error_popup
            return
        ptime = int(ptime)
        min_bid = Decimal(min_bid)
        buy_price = Decimal(buy_price)
        if self.model.itemlist.getLength() >= 9:
            self.sellscreen_notif("List is currently full")
            return
        if not Check.checkPrice(min_bid, buy_price):
            self.error_message = "Starting bid must be less than buy price."
            show = ErrorPopup()
            error_popup = Popup(title="", content=show, separator_color=(0, 0, 0, 0),
                                background="imgs/PopupBackground.png",
                                size_hint=(None, None), size=(300, 170))
            error_popup.overlay_color = (0, 0, 0, .4)
            error_popup.open()
            self.error_popup = error_popup
        else:
            new_item = Item(name, ptime, min_bid, buy_price)
            self.model.itemlist.addItem(new_item)
            self.sellscreen_notif("Item Successfully submitted!")

    def wishlist_item(self, item_num):
        """adds item to wishlist"""
        if(self.model.itemlist.getItem(item_num).wishlist):
            self.model.itemlist.getItem(item_num).removeFromWishlist()
            self.buyscreen_notif(self.model.itemlist.getItem(item_num).name + " removed from wishlist!")
            return
        self.model.itemlist.getItem(item_num).addToWishlist()
        self.buyscreen_notif(self.model.itemlist.getItem(item_num).name + " Wishlisted!")

    def buy_item(self, item_num):
        """Check if the user can buy items"""
        # If they can buy
        item = self.model.itemlist.getItem(item_num)
        if Check.buyItem(item_num, self.model.default_user, self.model.itemlist):
            self.root.ids.buy_screen.ids.balance_label.text = "${:.2f}".format(self.model.default_user.getBalance())
            self.buyscreen_notif("Bought " + item.name + "!")
        else:
            self.buyscreen_notif("Not enough funds in account!")

    def switchlist(self, list):
        if(list == "tracklist"):
            self.tracklist_active = True
            self.wishlist_active = False
        elif(list == "wishlist"):
            self.wishlist_active = True
            self.tracklist_active = False
        elif(list == "buylist"):
            self.wishlist_active = False
            self.tracklist_active = False
        self.updateUI()

    def updateUI(self):
        item_ids = self.root.ids.buy_screen.ids
        if(self.tracklist_active):
            displaylist = []
            for i in range(self.model.itemlist.getLength()):
                if(self.model.itemlist.getItem(i).track):
                    displaylist.append(self.model.itemlist.getItem(i))
            self.root.ids.buy_screen.ids.bidtracking.opacity = 1
            self.root.ids.buy_screen.ids.wishlisttitle.opacity = 0
            for i in range(len(displaylist)):
                item = getattr(item_ids, "item_name_" + str(i + 1))
                item.text = displaylist[i].name
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_price_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_buy_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].buy_price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "bid_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "buy_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist), 9):
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist) - 1, -1, -1):
                seconds = displaylist[i].time
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                timer_seconds = seconds % 60
                timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.text = timer
        elif(self.wishlist_active):
            displaylist = []
            for i in range(self.model.itemlist.getLength()):
                if(self.model.itemlist.getItem(i).wishlist):
                    displaylist.append(self.model.itemlist.getItem(i))
            self.root.ids.buy_screen.ids.wishlisttitle.opacity = 1
            self.root.ids.buy_screen.ids.bidtracking.opacity = 0
            for i in range(len(displaylist)):
                item = getattr(item_ids, "item_name_" + str(i + 1))
                item.text = displaylist[i].name
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_price_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_buy_" + str(i + 1))
                item.text = "${:.2f}".format(displaylist[i].buy_price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "bid_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "buy_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist), 9):
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(len(displaylist) - 1, -1, -1):
                seconds = displaylist[i].time
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                timer_seconds = seconds % 60
                timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.text = timer
        else:
            self.root.ids.buy_screen.ids.wishlisttitle.opacity = 0
            self.root.ids.buy_screen.ids.bidtracking.opacity = 0
            for i in range(self.model.itemlist.getLength()):
                item = getattr(item_ids, "item_name_" + str(i + 1))
                item.text = self.model.itemlist.getItem(i).name
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_price_" + str(i + 1))
                item.text = "${:.2f}".format(self.model.itemlist.getItem(i).price)
                item.opacity = 1
                item.disabled = False
                item = getattr(item_ids, "item_buy_" + str(i + 1))
                item.text = "${:.2f}".format(self.model.itemlist.getItem(i).buy_price)
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 1
                item.disabled = False
            for i in range(self.model.itemlist.getLength(), 9):
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
                item = getattr(item_ids, "wish_button_" + str(i + 1))
                item.opacity = 0
                item.disabled = True
            for i in range(self.model.itemlist.getLength() - 1, -1, -1):
                seconds = self.model.itemlist.getItem(i).time
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                timer_seconds = seconds % 60
                timer = "{:02d}:{:02d}:{:02d}".format(hours, minutes, timer_seconds)
                item = getattr(item_ids, "item_time_" + str(i + 1))
                item.text = timer

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
        self.model.default_user.setBalance(self.model.default_user.getBalance() + float(value))
        self.root.ids.buy_screen.ids.balance_label.text = self.model.default_user.formatBalance()

    def get_price(self):
        """returns current items price as dollar format"""
        return self.model.itemlist.getItemPrice(self.curr_item)

    def get_error(self):
        """gets the current error message"""
        return self.error_message