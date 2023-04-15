"""Runs the CloudMarket application"""
from datetime import datetime, timedelta, time
from gui import CloudMarket
from model import Model


#-MAIN-------------------------------------------
model = Model()
cloudmarket = CloudMarket(model).run()