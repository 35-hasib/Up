name = 'Hasibur_Rahman'
pas = '#&35.Ha$ib'


import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


i = 0

while True:
    print('mission started....!')
    try:
        driver = webdriver.Chrome()

        driver.maximize_window()
        driver.delete_all_cookies()
        driver.get('https://codeforces.com/enter?back=%2F')
    
        driver.close();
        i = i+1
    except:
        print("An Error Found ....!")
    if i == 1:
        break