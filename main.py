"""Runs the CloudMarket application"""
from view import View
from model import Model


#-MAIN-------------------------------------------
model = Model()
View(model).run()