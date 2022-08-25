from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


# selectProduct
try:
    print("Product-Selection page ready")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'plan-card__button'))).click()
except TimeoutException:
    print("Product-Selection page timeout")

# contact
try:
    print("Contact page ready")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "first-name"))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(User.first)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(User.last)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "email-address"))).send_keys(User.email)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "phone-number"))).send_keys(User.phone)
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Next")]'))).click()
except TimeoutException:
    print("Contact-Credit page timeout")

# driver.find_element('xpath', '// span[contains(text(), "Next")]').click()



# credit
try:
    print("Credit page ready")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Month")]'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@aria-label="birth-month"]'))).send_keys(User.month)
    keyboard.send("enter")

    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Day")]'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@aria-label="birth-day"]'))).send_keys(User.day)
    keyboard.send("enter")

    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[contains(text(), "Year")]'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// input[@aria-label="birth-year"]'))).send_keys(User.year)
    keyboard.send("enter")

    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "ssn"))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "ssn"))).send_keys(User.ssn)

    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Submit")]'))).click()
except TimeoutException:
    print("Credit page timeout")


# installation
try:
    print("Installation ready")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// div[@aria-disabled="false"]'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Next")]'))).click()
except TimeoutException:
    print("Installation timeout")

# payment
try:
    print("Payment ready")
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "autopay"))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// label/div[@class="checkbox"]'))).click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// span[contains(text(), "Submit Order")]'))).click()
except TimeoutException:
    print("Payment timeout")

# confirmation
try:
    print("Confirmation ready")
    confirmation = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('xpath', '// *[contains(text(), "Confirmation")]')))
    print('confirmation: ', confirmation)
except TimeoutException:
    print("Confirmation timeout")