from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# Guaranteed internet speeds
DOWNLOAD = 300
UPLOAD = 100


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(os.environ['CHROME_DRIVER_PATH']))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        # click privacy button
        consent = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        consent.click()
        time.sleep(1)

        # click go
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        go.click()

        # check the report
        time.sleep(60)

        self.down = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        # log in
        time.sleep(5)
        email = self.driver.find_element(By.CSS_SELECTOR, "div input")
        email.send_keys(os.environ['TWITTER_ID'])
        time.sleep(2)
        next_1 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div')
        next_1.click()
        time.sleep(5)

        number = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        number.send_keys(os.environ['TWITTER_PHONE'])
        time.sleep(2)
        next_2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        next_2.click()
        time.sleep(5)

        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(os.environ['TWITTER_PW'])
        time.sleep(5)
        log_in_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
        log_in_btn.click()
        time.sleep(5)

        # tweet
        tweet_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
        tweet_input.send_keys(f"It's not what you guaranteed dear. upload:{self.up} Mbps, and download:{self.down} Mbps")
        tweet_btn = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_btn.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.up < UPLOAD or bot.down < DOWNLOAD:
    bot.tweet_at_provider()

bot.driver.quit()