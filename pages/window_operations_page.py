import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class WindowOptions(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def multiwin(self):

        search_box = self.chromedriver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
        search_box.send_keys("Selenium", Keys.ENTER)
        time.sleep(3)
        self.chromedriver.find_element(By.XPATH, "(//div[@id='wikipedia-search-result-link']/a)[1]").click()
        self.chromedriver.find_element(By.XPATH, "(//div[@id='wikipedia-search-result-link']/a)[2]").click()
        self.chromedriver.find_element(By.XPATH, "(//div[@id='wikipedia-search-result-link']/a)[3]").click()
        # self.chromedriver.find_element(By.XPATH, "(//div[@id='wikipedia-search-result-link']/a)[4]").click()

        '''Switching between the Tabs'''
        get_win_list = self.chromedriver.window_handles
        print(get_win_list)

        '''Last opened window is the first window '''

        self.chromedriver.switch_to.window(get_win_list[3])
        time.sleep(3)
        third_win = self.chromedriver.find_element(By.XPATH, "(//span[text()='Selenium (software)'])[1]").text
        assert third_win == 'Selenium (software)', "first win message are not same"
        self.chromedriver.close()

        self.chromedriver.switch_to.window(get_win_list[1])
        time.sleep(3)
        second_win = self.chromedriver.find_element(By.XPATH, "(//span[text()='Selenium in biology'])[1]").text
        assert second_win == 'Selenium in biology', "second win message are not same"
        self.chromedriver.close()

        self.chromedriver.switch_to.window(get_win_list[2])
        time.sleep(3)
        first_win = self.chromedriver.find_element(By.XPATH, "(//span[text()='Selenium'])[1]").text
        assert first_win == 'Selenium', "first win message are not same"
        self.chromedriver.close()


        # self.chromedriver.switch_to.window(get_win_list[3])
        #
        # self.chromedriver.switch_to.window(get_win_list[0])


