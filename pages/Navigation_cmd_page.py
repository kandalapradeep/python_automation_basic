import time

from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class Navigation_Actions(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def navigation_BF(self):

        '''Navigation CMD back(),forward(),refresh()'''

        self.chromedriver.find_element(By.XPATH, "(//div[@id='laptops']/a)[1]").click()
        time.sleep(2)
        assert self.chromedriver.title == 'Apple', "both the titles are not same"
        self.chromedriver.back()

        # self.chromedriver.find_element(By.XPATH, "(//div[@id='laptops']/a)[2]").click()
        # time.sleep(2)
        # assert self.chromedriver.title == 'lenovo', "both the titles are not same"
        # self.chromedriver.back()

        self.chromedriver.find_element(By.XPATH, "(//div[@id='laptops']/a)[3]").click()
        time.sleep(2)
        assert self.chromedriver.title == 'Computers, Monitors & Technology Solutions | Dell India', f"both the titles are not same, {self.chromedriver.title}"
        self.chromedriver.back()
