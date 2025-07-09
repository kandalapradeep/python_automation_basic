from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class TableActions(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def normaltable(self):

        '''Static  Table code'''

        # rows = self.chromedriver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr")
        # coiumns_name = self.chromedriver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th")
        #
        # for r in range(2, len(rows)+1):
        #     for c in range(1, len(coiumns_name)+1):
        #         get_name = self.chromedriver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        #         if get_name == "Selenium":
        #             print(self.chromedriver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text)

        '''Dynamic Table code '''

        Drow = self.chromedriver.find_elements(By.XPATH, "//table[@id='taskTable']/tbody/tr")
        Dcolumn = self.chromedriver.find_elements(By.XPATH, "//table[@id='taskTable']/thead/tr/th")

        for Dr in range(1, len(Drow)+1):
            for Dc in range(1, len(Dcolumn)+1):
                get_dname = self.chromedriver.find_element(By.XPATH, "//table[@id='taskTable']/tbody/tr["+str(Dr)+"]/td["+str(Dc)+"]").text
                print(get_dname)