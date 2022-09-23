from cgitb import text
import math
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 


driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/huge_form.html")
more = driver.find_elements_by_tag_name("input")
for element in more:
    element.send_keys("Мой ответ")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
