# Fourth test - expected result -> Check click button "Guest Log in"
import re

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# absolute_path = os.path.dirname(__file__)
# relative_path = "/"
# full_path = os.path.join(absolute_path, relative_path)
# print(f'Path: {absolute_path}')
# print ('Path:' + full_path)

options = Options()
options.add_argument("--no-sandbox")

# driver = webdriver.Chrome(service=Service(absolute_path+'chromedriver'), options=options)
# driver = webdriver.Chrome(service=Service(absolute_path+'\\chromedriver.exe'), options=options)
driver = webdriver.Chrome(service=Service('C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe'), options=options)

driver.get("https://qauto.forstudy.space/")

time.sleep(2)

user = "guest"
password = "welcome2qauto"
driver.get("https://" + user + ":" + password + "@" + "qauto.forstudy.space/")
# driver.get("https://qauto.forstudy.space/")

guest = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class*='guest']"))).get_attribute("formcontrolname")
time.sleep(2)

elem = driver.find_element(By.CSS_SELECTOR, "button[class*='guest']")
elem.click()
time.sleep(2)

driver.close()