from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import os
import time


class AutoFollowBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(os.environ['CHROME_DRIVER_PATH']))

    def log_in(self):
        self.driver.get("https://www.instagram.com/")
        # cookie setting
        cookie = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]')
        cookie.click()
        time.sleep(5)

        # log in
        email = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        email.send_keys(os.environ['INS_ID'])
        password.send_keys(os.environ['INS_PW'])
        time.sleep(2)

        login_btn = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        login_btn.click()
        time.sleep(10)

    def find_account(self, name):
        search_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/nav/div[2]/div/div/div[2]/input')
        search_input.send_keys(name)
        time.sleep(2)
        search_input.send_keys(Keys.ENTER)
        search_input.send_keys(Keys.ENTER)
        time.sleep(10)

    def follow(self, limit):
        # check the following
        following_page = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[3]/a')
        following_page.click()
        time.sleep(5)

        followings = self.driver.find_elements(By.CSS_SELECTOR, "li div div button")
        count = 0
        # follow the accounts until the limit is met
        for _ in followings:
            # ensure the account is not followed
            if _.text == "Follow":
                _.click()
                count += 1
                time.sleep(5)

            if count >= limit:
                break


bot = AutoFollowBot()
bot.log_in()
bot.find_account("insta_dog")
bot.follow(2)
