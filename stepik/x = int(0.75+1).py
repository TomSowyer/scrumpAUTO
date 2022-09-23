from cgitb import text
import math
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('/Users/dimaprisepov/Downloads/chromedriver 4')
driver.get('http://suninjuly.github.io/redirect_accept.html')
time.sleep(0.2)

button = driver.find_element_by_tag_name("button").click()


name = driver.find_element_by_name('firstname').send_keys("name")
lastname = driver.find_element_by_name('lastname').send_keys("lastname")
email = driver.find_element_by_name('email').send_keys("tomsowyertest@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__)) 
file_path = os.path.join(current_dir, 'file.txt')    
otp = driver.find_element_by_xpath('//*[@id="file"]').send_keys(file_path)


button = driver.find_element_by_tag_name("button")

button.click()
