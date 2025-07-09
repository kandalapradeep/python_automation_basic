import time
from base_page.base_page import BasePage


class openinit():

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver

    def pass_URL_to_browser(self):
        self.chromedriver.get("https://testautomationpractice.blogspot.com/")

