from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Users import Charles as User
from tkinter import *
import json

driver = webdriver.Chrome()
site = 'http://localhost/'
driver.get(site)
driver.maximize_window()
driver.implicitly_wait(10)

def get_browser_console_log():
    try:
        log = driver.get_log('browser')
        obj = json.dumps(log, indent = 2) 
        print(obj)
    except TimeoutException:
        print("Timeout")

get_browser_console_log()