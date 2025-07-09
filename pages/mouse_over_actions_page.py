from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class Mouse_action(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def mouse_actions(self):
        MA = ActionChains(self.chromedriver)

        '''Double click for element'''

        field1 = self.chromedriver.find_element(By.ID, "field1")
        field1.clear()
        field1.send_keys("Pradeep")
        btn = self.chromedriver.find_element(By.XPATH, "//button[text()='Copy Text']")
        MA.double_click(btn).perform()

        '''drag and drop for mouse over actions'''
        source = self.chromedriver.find_element(By.ID, "draggable")
        destination = self.chromedriver.find_element(By.ID, "droppable")
        MA.drag_and_drop(source,destination).perform()

        '''side bar moving using mouse action'''

        right_bar = self.chromedriver.find_element(By.XPATH, "(//span[@class = 'ui-slider-handle ui-corner-all ui-state-default'])[1]")
        left_bar = self.chromedriver.find_element(By.XPATH, "(//span[@class = 'ui-slider-handle ui-corner-all ui-state-default'])[2]")
        MA.click_and_hold(right_bar).move_by_offset(50,0).release().perform()
        MA.click_and_hold(left_bar).move_by_offset(50, 0).release().perform()

