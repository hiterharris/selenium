from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
site = 'https://na.spatime.com/tblc1000/9690060/home'
driver.get(site)

driver.implicitly_wait(5)
view_services = driver.find_element('xpath', '// span[contains(text(), " View services ")]').click()
driver.implicitly_wait(5)
driver.find_element('xpath', '// span[contains(text(), "80 minute Ballantyne Relaxation Massage")]').click()
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '// span[contains(text(), " Book now ")]'))))

driver.implicitly_wait(5)
date = driver.find_element(By.CLASS_NAME, 'selected').text
print('date: ', date)

time = driver.find_element(By.CLASS_NAME, "time-slot-title").text
print('time: ', time)
