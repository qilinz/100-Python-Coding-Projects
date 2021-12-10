from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

# start webdriver
s = Service("/Users/karin/Documents/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location"
           "=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# sign in linkedin
time.sleep(1)
sign_in_page = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_page.click()
time.sleep(1)

# enter sign in infos
email = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
email.send_keys(os.environ['LINKEDIN_EMAIL'])
password.send_keys(os.environ['LINKEDIN_PW'])
sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()
time.sleep(1)

# find all the job items
job_list = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

count = 0
for job in job_list:
    # click the job
    job.click()
    time.sleep(1)
    # save it
    save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    save_button.click()
    time.sleep(2)

    # close the save notification
    close_button = driver.find_element(By.CSS_SELECTOR, '.artdeco-button__icon svg')
    close_button.click()

    time.sleep(2)

    count += 1
    if count == 10:
        break

driver.quit()