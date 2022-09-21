import telebot
import pyperclip
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome('/Users/dimaprisepov/Downloads/chromedriver 5') 

driver.get('https://dev.mineplex.io/ru')
time.sleep(3)
regLink = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div[1]/div[1]/div[2]/div/button[2]')
regLink.click()
time.sleep(2)
namefield = driver.find_element_by_xpath('//*[@id="loginForm_firstName"]')
Lnamefield = driver.find_element_by_xpath('//*[@id="loginForm_lastName"]')
Passfield = driver.find_element_by_xpath('//*[@id="loginForm_password"]')
twoPassfield = driver.find_element_by_xpath('//*[@id="loginForm_confirmPassword"]')

namefield.send_keys('auto')
Lnamefield.send_keys('user dima')
Passfield.send_keys('DanyDany@42198')
twoPassfield.send_keys('DanyDany@42198')

newwindow = 'window.open("https://tempmail.plus/ru")'
driver.execute_script(newwindow)
 # Переместите ручку для работы на вновь открытой странице
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
copy = driver.find_element_by_xpath('//*[@id="pre_copy"]')
copy.click()
time.sleep(1)

x = pyperclip.paste()
print(x)

token = ('5571918009:AAHw4rhhXBbZmIR1olPyHu_tHHtwuGaqYAQ')
bot = telebot.TeleBot(token)
CHANNEL_NAME = '@MP_qa'

text = (x)
bot.send_message(CHANNEL_NAME, text)

driver.switch_to.window(driver.window_handles[0])

LoginField = driver.find_element_by_xpath('//*[@id="loginForm_email"]')
LoginField.send_keys(x)

checkOne = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/form/fieldset/div/fieldset[1]/label/span[1]/span/input').click()
checkOne = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div[2]/form/fieldset/div/fieldset[2]/label/span[1]/span/input').click()
time.sleep(1)
nextbutton = driver.find_element_by_xpath('//*[@id="loginForm"]/div[6]/button').click()

driver.switch_to.window(driver.window_handles[1])
myMail = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#container-body > div.container-xl.body > div.inbox > div.mail"))
)
myMail.click()
time.sleep(3)
gogogo = driver.find_element_by_css_selector('tr:nth-child(3) > td > div > a > font').click()

time.sleep(8)

