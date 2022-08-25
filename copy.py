from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
site = 'http://localhost/'
driver.get(site)
driver.maximize_window()

# serviceability
# driver.find_element(By.ID, "street-address").send_keys("30 Hodge Ave Ansonia")
# driver.implicitly_wait(5)

# driver.find_element('xpath', '// div[contains(text(), "30 Hodge Ave - Ansonia CT 06401")]').click()
# driver.find_element('xpath', '// span[contains(text(), "Check availability")]').click()

# serviceability
try:
    print("Address-Check page")
    driver.find_element(By.ID, "street-address").send_keys("30 Hodge Ave Ansonia")
    driver.find_element('xpath', '// div[contains(text(), "30 Hodge Ave - Ansonia CT 06401")]').click()
    driver.find_element('xpath', '// span[contains(text(), "Check availability")]').click()
except TimeoutException:
    print("Address-Check pageage timeout")

# selectProduct
try:
    print("Product-Selection page ready")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'plan-card__button'))).click()
except TimeoutException:
    print("Product-Selection page timeout")

# contact
try:
    print("Contact page ready")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("CHARLES")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("KKEEKYT")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email-address"))).send_keys("charles@mail.com")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "phone-number"))).send_keys("704-839-4726")
except TimeoutException:
    print("Contact-Credit page timeout")

driver.find_element('xpath', '// span[contains(text(), "Check availability")]').click()

# credit
try:
    print("Credit page ready")
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("CHARLES")
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys("KKEEKYT")
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email-address"))).send_keys("charles@mail.com")
    # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "phone-number"))).send_keys("704-839-4726")
except TimeoutException:
    print("Credit page timeout")

driver.find_element('xpath', '// span[contains(text(), "Check availability")]').click()