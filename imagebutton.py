"""necessary class for kivy"""
from kivy.uix.button import ButtonBehavior
from kivy.uix.image import Image


class ImageButton(ButtonBehavior, Image):
    """Creates an ImageButton"""
