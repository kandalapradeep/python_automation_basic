from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def send_text(self, locator, value):
        """Send keys to an element."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(value)

    def send_keys_element_located(self, locator, value):
        """Send keys to an element."""
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        element.send_keys(value)

    def send_keys_with_enter(self, locator, value):
        """Send keys to an element."""
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.send_keys(value)
        element.send_keys(Keys.ENTER)

    def get_text(self, locator, by=By.XPATH):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((by, locator)))
        return element.text

    def mouse_hover(self, locator):
        tutorials = self.driver.find_element(By.XPATH, locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(tutorials).perform()

    def element_till_clickable(self, locator, by_type=By.XPATH):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((by_type, locator))).click()
