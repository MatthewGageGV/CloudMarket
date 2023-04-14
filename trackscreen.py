from kivy.uix.screenmanager import Screen

class TrackScreen(Screen):
    """Creates the trackscreen"""
    balance = 1000.00

    def balance_to_string(self):
        """converts balance to dollar format"""
        return "${:.2f}".format(self.balance)