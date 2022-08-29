from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Users import Charles as User
import keyboard

driver = webdriver.Chrome()
site = 'http://localhost/'
driver.get(site)
driver.maximize_window()
driver.implicitly_wait(5)

# serviceability
try:
    print("Address-Check page ready")
    driver.find_element(By.ID, "street-address").send_keys(User.address)
except TimeoutException:
    print("Address-Check pageage timeout")

driver.find_element('xpath', '// div[contains(text(), "30 Hodge Ave - Ansonia CT 06401")]').click()
keyboard.send("enter")
keyboard.send("enter")