from selenium.webdriver.common.by import By

from base_page.base_page import BasePage


class Alert_options(BasePage):

    def __init__(self, chromedriver):
        self.chromedriver = chromedriver
        self.base = BasePage(chromedriver)

    def alertoptions(self):
        self.chromedriver.find_element(By.ID, "alertBtn").click()
        alert_click = self.chromedriver.switch_to.alert
        alert_click.accept()
        self.chromedriver.find_element(By.ID, "confirmBtn").click()
        alert_click.dismiss()
        self.chromedriver.find_element(By.ID, "promptBtn").click()
        alert_click.send_keys("pradeep")
        print(alert_click.text, "Get the Text from Popup")
        alert_click.accept()
        get_text = self.base.get_text("demo", By.ID)
        assert get_text == "Hello pradeep! How are you today?", "you Text is not matching.."


