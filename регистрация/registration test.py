import telebot
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
driver = webdriver.Chrome()

driver.get('https://dev.mineplex.io/ru')
driver.implicitly_wait(15)
refID = driver.find_element_by_css_selector('#passwordForDev_devPassword').send_keys('Gw1pqh5yxQ')
refID_Button = driver.find_element_by_css_selector('#passwordForDev > div.MuiBox-root.jss101 > button').click()
driver.implicitly_wait(15)
regLink = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div/div[1]/div[1]/div[2]/div/button[2]'))
).click()

time.sleep(2)
namefield = driver.find_element_by_xpath('//*[@id="loginForm_firstName"]').send_keys('auto')
Lnamefield = driver.find_element_by_xpath('//*[@id="loginForm_lastName"]').send_keys('user dima')
Passfield = driver.find_element_by_xpath('//*[@id="loginForm_password"]').send_keys('DanyDany@42198')
twoPassfield = driver.find_element_by_xpath('//*[@id="loginForm_confirmPassword"]').send_keys('DanyDany@42198')

newwindow = 'window.open("https://tempmail.plus/ru")'
driver.execute_script(newwindow)
 # Переместите ручку для работы на вновь открытой странице
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(15)
copy = driver.find_element_by_xpath('//*[@id="pre_copy"]').click()
driver.implicitly_wait(15)

x = pyperclip.paste()
print(x)

token = ('5571918009:AAHw4rhhXBbZmIR1olPyHu_tHHtwuGaqYAQ')
bot = telebot.TeleBot(token)
CHANNEL_NAME = '@MP_qa'

text = (x)
bot.send_message(CHANNEL_NAME, text)

driver.switch_to.window(driver.window_handles[0])

LoginField = driver.find_element_by_xpath('//*[@id="loginForm_email"]').send_keys(x)

checkOne = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/form/fieldset/div/fieldset[1]/label/span[1]/span/input').click()
checkOne = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/form/fieldset/div/fieldset[2]/label/span[1]/span/input').click()
time.sleep(1)
nextbutton = driver.find_element_by_xpath('//*[@id="loginForm"]/div[6]/button').click()

driver.switch_to.window(driver.window_handles[1])
myMail = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#container-body > div.container-xl.body > div.inbox > div.mail"))
)
myMail.click()
gogogo = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'tr:nth-child(3) > td > div > a > font'))
).click()

time.sleep(5)
