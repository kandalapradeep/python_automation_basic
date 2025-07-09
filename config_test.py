import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

ops = webdriver.ChromeOptions()
ops.add_argument("--use-fake-device-for-media-stream")
ops.add_argument("--use-fake-ui-for-media-stream")
ops.add_argument('--disable-notifications')

driver = None


@pytest.fixture(scope="class")
def init_browser():
    global driver

    '''Initialize the first WebDriver instance.'''
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=ops)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.back()
    driver.forward()

    yield driver
    driver.quit()
