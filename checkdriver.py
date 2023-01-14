from selenium import webdriver
from webdriver_auto_update import check_driver

class Checker:

    def __init__(self, path):
        self.path = path

    def cdc(self):
        check_driver(self.path)
        return
