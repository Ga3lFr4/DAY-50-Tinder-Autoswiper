from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os

load_dotenv('variables.env')
fb_login = os.getenv('FB_LOGIN')
fb_pw = os.getenv('FB_PW')
phone = os.getenv('PHONE')

chromedriver = "/Users/gael/Desktop/100_days_code/*Tools/chromedriver"

driver = webdriver.Chrome(chromedriver)

driver.get("https://tinder.com/")
time.sleep(1)
create_acc = driver.find_element(By.XPATH, '//*[@id="o-98920890"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button/div[2]/div[2]')
create_acc.click()

time.sleep(1)
facebook_login = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login.click()

time.sleep(1)
whandle = driver.window_handles[1]
driver.switch_to.window(whandle)

time.sleep(1)
accept_cookies = driver.find_elements(By.TAG_NAME, 'button')
accept_cookies[-1].click()

email = driver.find_element(By.NAME, 'email')
email.click()
email.send_keys(fb_login)

pw = driver.find_element(By.NAME, 'pass')
pw.click()
pw.send_keys(fb_pw)

submit_button = driver.find_element(By.NAME, "login")
submit_button.click()

time.sleep(5)
driver.switch_to.window(driver.window_handles[0])

time.sleep(5)
allow_localisation = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div/div/div[3]/button[1]')
allow_localisation.click()

time.sleep(5)
disallow_notifications = driver.find_element(By.XPATH, '//*[@id="o-1827301966"]/main/div/div/div/div[3]/button[2]')
disallow_notifications.click()

time.sleep(10)
counter = 0
while counter < 100:
    time.sleep(1)
    body = driver.find_element(By.TAG_NAME, "body")
    body.send_keys(Keys.ARROW_LEFT)
    counter += 1

