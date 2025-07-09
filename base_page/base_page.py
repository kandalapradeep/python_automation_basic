from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.action = ActionChains(self.driver)


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
    
        def wait_till_element_invisible(self, locator: str, by_type=By.XPATH):
        self.wait.until(EC.invisibility_of_element((by_type, locator)))

    def wait_till_element_present(self, locator: str, by_type=By.XPATH):
        self.wait.until(EC.presence_of_all_elements_located((by_type, locator)))

        def wait_till_alert_present(self):
        self.wait.until(EC.alert_is_present())

    def wait_for_element_to_load(self, locator: str):
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))

    # ========== Advanced Interactions ==========

    def scroll_to_element(self, locator: str, by_type=By.XPATH):
        element = self.get_element(locator, by_type)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def move_to_element(self, locator: str, by_type=By.XPATH):
        element = self.get_element(locator, by_type)
        self.action.move_to_element(element).perform()

    def move_to_offset(self, x_offset=5, y_offset=5):
        self.action.move_by_offset(x_offset, y_offset).perform()

        def goto_url(self, url):
        self.driver.get(url)

    def refresh_window(self):
        self.driver.refresh()

    def get_title(self) -> str:
        return self.driver.title

    def open_new_window(self, index=0):
        self.driver.execute_script("window.open()")
        if index != 0:
            self.driver.switch_to.window(self.driver.window_handles[index])

    def is_page_loaded(self) -> bool:
        state = self.driver.execute_script("return document.readyState;")
        return state == "complete"

    # ========== Element Actions ==========

    def click_element(self, locator: str, by_type=By.XPATH, retries=3, wait_time=10):
        for attempt in range(retries):
            try:
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable((by_type, locator))
                )
                element.click()
                logging.info(f"Clicked element: {locator}")
                return
            except ElementClickInterceptedException:
                logging.warning(f"Click intercepted on {locator}, retrying...")
                time.sleep(1)
            except NoSuchElementException:
                logging.error(f"Element not found: {locator}")
                return

    def js_click_element(self, locator: str, by_type=By.XPATH):
        element = self.get_element(locator, by_type)
        self.driver.execute_script("arguments[0].click();", element)

    def send_keys(self, locator: str, by_type=By.XPATH, value=""):
        try:
            WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((by_type, locator)))
            element = self.driver.find_element(by_type, locator)

            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

            element.clear()
            element.send_keys(value)

            logging.info(f"Sent keys to element: {locator} with value: {value}")
        except TimeoutException:
            logging.error(f"Timeout waiting for element: {locator}")
        except ElementNotInteractableException:
            logging.error(f"Element not interactable: {locator}")
        except StaleElementReferenceException:
            logging.error(f"Stale element reference: {locator}")

