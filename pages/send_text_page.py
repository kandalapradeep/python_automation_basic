from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class Provide_input(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def send_data(self):
        self.base.send_text((By.ID, "name"), "Pradeep")
        self.base.send_text((By.ID, "email"), "Pradeep@yopmail.com")
        self.base.send_text((By.ID, "phone"), 9876543234)
        self.base.send_text((By.ID, "textarea"), "4th cross 1st Mail Japan")

        '''radio buttons click'''
        self.base.element_till_clickable("male", By.ID)

        '''click for checkboxs'''

        self.base.element_till_clickable("sunday", By.ID)
        self.base.element_till_clickable("monday", By.ID)
        self.base.element_till_clickable("saturday", By.ID)
