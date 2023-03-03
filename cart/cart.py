import os
import sys
from dotenv import load_dotenv
from products import products
from full import full
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Users import Doris as User
from products import products
import keyboard

load_dotenv()
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# site = 'http://localhost/'
site = 'https://qat02.frontier.com/buy'
driver.get(site)
driver.maximize_window()
driver.implicitly_wait(5)

page = sys.argv[1]
product = sys.argv[2]

if product == 'fiber':
    address = os.environ.get('FIBER')
elif product == 'copper':
    address = os.environ.get('COPPER')
else:
    pass

if page == 'products':
    products(WebDriverWait, driver, EC, By, TimeoutException, address, product)
elif page == 'full':
    full(WebDriverWait, driver, EC, By, TimeoutException, address, product)
else:
    print('No page given')
