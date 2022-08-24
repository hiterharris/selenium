from selenium import webdriver
from selenium.webdriver.common.by import By

# open site in Chrome
driver = webdriver.Chrome()
site = 'https://codepen.io/'
driver.get(site)

# click "Log In"
login = driver.find_element('xpath', '// a[contains(text(), "Log In")]')
login.click()

# get elements
username = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")
submit = driver.find_element(By.ID, "log-in-button")

# fill inputs, submit
username.send_keys("hiterharris@comcast.net")
password.send_keys("hhh92891")
submit.click()
