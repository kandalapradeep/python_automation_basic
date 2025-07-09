from datetime import datetime
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")
driver.maximize_window()


Target_date_str = "2023-6-30"
Target_date = datetime.strptime(Target_date_str, "%Y-%m-%d")
Target_day = Target_date.day
Target_year = Target_date.year
Target_Month = Target_date.month


'''second type of calender selection'''

driver.find_element(By.ID, "second_date_picker").click()
time.sleep(2)
date_str = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']").text

Current_date_object = datetime.strptime(date_str, "%B %Y")
Current_month = int(Current_date_object.strftime("%m"))
Current_year = int(Current_date_object.strftime("%Y"))

'''Future Date selection condition'''

while Current_month < Target_Month or Current_year < Target_year:
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@data-handler='next']").click()
    date_str = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']").text
    date_object = datetime.strptime(date_str, "%B %Y")
    Current_month = int(date_object.strftime("%m"))
    Current_year = int(date_object.strftime("%Y"))

'''Past Date selection condition'''

while Current_month > Target_Month or Current_year > Target_year:
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[@data-handler='prev']").click()
    date_str = driver.find_element(By.XPATH, "//div[@class='ui-datepicker-title']").text
    date_object = datetime.strptime(date_str, "%B %Y")
    Current_month = int(date_object.strftime("%m"))
    Current_year = int(date_object.strftime("%Y"))

if Current_month == Target_Month:
    select_Date = driver.find_element(By.XPATH,
                                      "//table[@class='ui-datepicker-calendar']//td[not(contains(@class,'ui-datepicker-other-month'))]//a[text()='" + str(
                                          Target_day) + "']")
    select_Date.click()

time.sleep(10)