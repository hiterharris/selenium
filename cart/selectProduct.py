from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
site = 'http://localhost/'
driver.get(site)
driver.maximize_window()
driver.implicitly_wait(5)

street = driver.find_element(By.ID, "street-address")
street.send_keys("30 Hodge Ave Ansonia")
driver.implicitly_wait(5)

address = driver.find_element('xpath', '// div[contains(text(), "30 Hodge Ave - Ansonia CT 06401")]').click()
check_availability = driver.find_element('xpath', '// span[contains(text(), "Check availability")]').click()

try:
    select_plan = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'plan-card__button')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

select_plan.click()