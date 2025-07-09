import requests
from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class Broken_links(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def brokenlinks(self):

        links = self.chromedriver.find_elements(By.XPATH, "//h4[text()='Broken Links']/following-sibling::a")
        count = 0

        for link in links:
            URL = link.get_attribute('href')
            try:
                res = requests.head(URL)
                #print(res.status_code, res)
            except:
                None
            if res.status_code >= 400:
                count += 1
                print("Broken links details ", URL)
            else:
                print("non broken links ", URL)
        print("Total number of broken links", count)
