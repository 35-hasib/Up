import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains



print('mission started....!')
driver = webdriver.Chrome()

driver.maximize_window()
driver.delete_all_cookies()
driver.get('https://google.com/')

print('page opened....!')