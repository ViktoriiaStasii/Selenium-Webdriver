import re
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
# import time

# absolute_path = os.path.dirname(__file__)
# relative_path = "/"
# full_path = os.path.join(absolute_path, relative_path)
# print(f'Path: {absolute_path}')
# print ('Path:' + full_path)

def test_Guest_Login():
    options = Options()
    options.add_argument("--no-sandbox")

    # driver = webdriver.Chrome(service=Service(absolute_path+'chromedriver'), options=options)
    # driver = webdriver.Chrome(service=Service(absolute_path+'\\chromedriver.exe'), options=options)
    driver = webdriver.Chrome(service=Service('C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe'), options=options)
    driver.get("https://qauto.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto.forstudy.space/")

    goButton = driver.find_element(By.CSS_SELECTOR, "button[class*='guest']")
    goButton.send_keys("Selenium")
    goButton.click()
    time.sleep(2)

def test_Guest_Logout():
    options = Options()
    options.add_argument("--no-sandbox")

    # driver = webdriver.Chrome(service=Service(absolute_path+'chromedriver'), options=options)
    # driver = webdriver.Chrome(service=Service(absolute_path+'\\chromedriver.exe'), options=options)
    driver = webdriver.Chrome(service=Service('C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe'), options=options)
    driver.get("https://qauto.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto.forstudy.space/")

    goButton = driver.find_element(By.XPATH, "//button[contains(text(),'Guest log in')]")
    goButton.send_keys("Selenium")
    goButton.click()
    time.sleep(2)

    goButton = driver.find_element(By.XPATH, "//button[@id='userNavDropdown']")
    goButton.send_keys("Selenium")
    goButton.click()
    time.sleep(2)

    goButton = driver.find_element(By.CSS_SELECTOR, "button[class*='user-nav_link']")
    goButton.send_keys("Selenium")
    goButton.click()

def test_Found_addCarBrand():
    options = Options()
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(absolute_path + 'chromedriver'), options=options)
    driver = webdriver.Chrome(service=Service(absolute_path + '\\chromedriver.exe'), options=options)
    # driver = webdriver.Chrome(service=Service('C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe'), options=options)
    driver.get("https://qauto.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto.forstudy.space/")

    goButton = driver.find_element(By.CSS_SELECTOR, "button[class*='guest']")
    goButton.send_keys("Selenium")
    goButton.click()

    goButton = driver.find_element(By.XPATH, "//button[contains(text(),'Add car')]")
    goButton.send_keys("Selenium")
    goButton.click()

    try:
        element = driver.find_element(By.ID, "addCarBrand")
        print("Element found")
    except NoSuchElementException:
        print("No element found")

def test_Check_click_button_GuestLogin():
    options = Options()
    options.add_argument("--no-sandbox")

    # driver = webdriver.Chrome(service=Service(absolute_path+'chromedriver'), options=options)
    # driver = webdriver.Chrome(service=Service(absolute_path+'\\chromedriver.exe'), options=options)
    driver = webdriver.Chrome(service=Service('C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe'), options=options)
    driver.get("https://qauto.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto.forstudy.space/")

    guest = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[class*='guest']"))).get_attribute("formcontrolname")
    elem = driver.find_element(By.CSS_SELECTOR, "button[class*='guest']")
    elem.click()

def test_Check_click_button_Addcar():
    options = Options()
    options.add_argument("--no-sandbox")

    # driver = webdriver.Chrome(service=Service(absolute_path+'chromedriver'), options=options)
    # driver = webdriver.Chrome(service=Service(absolute_path+'\\chromedriver.exe'), options=options)
    driver = webdriver.Chrome(service=Service('C:/Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe'), options=options)
    driver.get("https://qauto.forstudy.space/")

    user = "guest"
    password = "welcome2qauto"
    driver.get("https://" + user + ":" + password + "@" + "qauto.forstudy.space/")

    goButton = driver.find_element(By.XPATH, "//button[contains(text(),'Guest log in')]")
    goButton.send_keys("Selenium")
    goButton.click()

    guest = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Add car')]"))).get_attribute("formcontrolname")
    elem = driver.find_element(By.XPATH, "//button[contains(text(),'Add car')]")
    elem.click()

    driver.close()