# Third test - expected result -> Found elements "addCarBrand" and "addCarMileage"
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os

absolute_path = os.path.dirname(__file__)
relative_path = "/"
full_path = os.path.join(absolute_path, relative_path)
print(f'Path: {absolute_path}')
print ('Path:' + full_path)

options = Options()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(absolute_path+'chromedriver'), options=options)
driver = webdriver.Chrome(service=Service(absolute_path+'\\chromedriver.exe'), options=options)
# driver = webdriver.Chrome(service=Service('C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe'), options=options)

driver.get("https://qauto.forstudy.space/")

time.sleep(2)

user = "guest"
password = "welcome2qauto"
driver.get("https://" + user + ":" + password + "@" + "qauto.forstudy.space/")
# driver.get("https://qauto.forstudy.space/")

goButton = driver.find_element(By.CSS_SELECTOR, "button[class*='guest']")
goButton.send_keys("Selenium")
goButton.click()
time.sleep(2)

goButton = driver.find_element(By.XPATH, "//button[contains(text(),'Add car')]")
goButton.send_keys("Selenium")
goButton.click()
time.sleep(2)

try:
    element = driver.find_element(By.ID, "addCarBrand")
    print("Element found")
except NoSuchElementException:
    print("No element found")

####

element = driver.find_element(By.ID, "addCarMileage")
if element.is_displayed():
    print("Element found")
    found = True
else:
    print("Element not found")
    found = False

assert found

driver.close()




