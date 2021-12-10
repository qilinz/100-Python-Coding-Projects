import os
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

FORM_LINK = "https://forms.gle/Fs1d2bYXuVNePpFF6"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C" \
              "%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A" \
              "-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C" \
              "%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A" \
              "%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse" \
              "%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A" \
              "%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse" \
              "%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B" \
              "%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# STEP 1: gather info from zillow
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Accept-Language": "en-us",
}
response = requests.get(ZILLOW_LINK, headers=headers)
response.raise_for_status()

data = response.text
soup = BeautifulSoup(data, "html.parser")
#
# # print(soup.prettify())

# flats = soup.select(selector="li article")
flats = soup.select(".list-card-info")

data_list = []
for i, flat in enumerate(flats):
    # print(flat)
    # print("   ")
    # print(flat.find("address").getText())
    # print(flat.find(class_="list-card-price").getText()[:6])
    # print(flat.find("a").get("href"))

    if flat.find("address") is not None:
        data_list.append(
            {
                "address": flat.find("address").getText(),
                "price": flat.find(class_="list-card-price").getText()[:6],
                "link": flat.find("a").get("href"),
            }
        )
# format the web link
for flat in data_list:
    if flat["link"][0] == "/":
        flat["link"] = f"https://www.zillow.com{flat['link']}"

# fill the google form
driver = webdriver.Chrome(service=Service(os.environ['CHROME_DRIVER_PATH']))
driver.get(FORM_LINK)
time.sleep(5)


for flat in data_list:
    address = driver.find_element(By.XPATH,
                                  '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address.send_keys(flat['address'])
    price = driver.find_element(By.XPATH,
                                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(flat['price'])
    link = driver.find_element(By.XPATH,
                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(flat['link'])
    btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    btn.click()
    time.sleep(2)
    submit_another = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
    time.sleep(5)

driver.quit()
