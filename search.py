import time
from selenium.webdriver.common.by import By
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

options=Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://www.themoviedb.org/")
driver.maximize_window()
time.sleep(2)

driver.find_element (By.XPATH, "//button[contains(text(),'Accept All Cookies')]").click()
time.sleep(2)


input = driver.find_element(By.ID, 'inner_search_v4')
input.send_keys('Titanic')
input.send_keys(Keys.RETURN)
time.sleep(2)

user = 'Aisulu'
secret = '1234'
button=driver.find_element(By.XPATH, '//a[@href="/login" and text()="Login"]').click()
login=driver.find_element(By.ID, 'username')
login.send_keys(user)
password=driver.find_element(By.ID, 'password')
password.send_keys(secret)
driver.find_element(By.ID, 'login_button').click()

driver.find_element(By.CSS_SELECTOR, "li.user a").click()

driver.find_element(By.XPATH, "/html/body/div[11]/div/div[1]/div/div[4]/p/a").click()

#driver.find_element(By.CSS_SELECTOR,"div.settings_content div.group a").click()