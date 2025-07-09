from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base_page.base_page import BasePage


class DropDownList(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def dropdownlist(self):

        droplist_country = Select(self.chromedriver.find_element(By.ID, "country"))
        droplist_country.select_by_visible_text("France")

        # droplist_country.select_by_index(3)
        # droplist_country.select_by_value("france")
        # droplist_country.deselect_by_index(3)

        droplist_colors = Select(self.chromedriver.find_element(By.ID, "colors"))
        droplist_colors.select_by_value("yellow")

        droplist_animals = Select(self.chromedriver.find_element(By.ID, "animals"))
        droplist_animals.select_by_index(4)


